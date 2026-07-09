'use strict';
// Load .env if present (out-of-band secrets on VPS, never committed)
try { require('dotenv').config({ path: require('path').join(__dirname, '.env') }); } catch (_) { /* optional */ }
/*
 * Symphony Phase 2 — Worker Node: Notion MASTER_SOP_DB → Supabase tenant.<slug>.sops
 *
 * Conforme :
 *   - ADR-MESH-L2-001 (Notion=WHAT, Supabase = miroir local pour Symphony)
 *   - ADR-INFRA-001  (PM2 VPS prod, autorestart:false + cron_restart)
 *   - ADR-HEART-002  (anti-panique: K3 auth halt, K1 verify, DLQ)
 *   - ADR-ID-001     (SOP_ID canonique SOP-L2-{DOMAIN}-{NN})
 *
 * Env requis (cf. ecosystem.config.js):
 *   NOTION_TOKEN          — Internal Integration Bearer
 *   NOTION_DATABASE_ID    — MASTER_SOP_DB id
 *   PG_CONNECTION_STRING  — postgres://postgres:PWD@127.0.0.1:5432/postgres
 *   PROJECT_SLUG          — ex: aspace_solaris (→ schema tenant_aspace_solaris)
 *   DRY_RUN               — '1' pour preview SQL sans appliquer
 */

const { Client: NotionClient } = require('@notionhq/client');
const { Client: PgClient } = require('pg');
const fs = require('fs');
const path = require('path');

// ============================================================================
// 0. Config & guards
// ============================================================================

const cfg = {
  notionToken: process.env.NOTION_TOKEN,
  notionDbId: process.env.NOTION_DATABASE_ID || '6b07315e-06ca-4652-9049-d72a1e79e906',
  pgConn: process.env.PG_CONNECTION_STRING,
  projectSlug: process.env.PROJECT_SLUG || 'aspace_solaris',
  dryRun: process.env.DRY_RUN === '1',
  dlqDir: process.env.DLQ_DIR || '/home/amadeus/symphony-workers/_dlq',
};

if (!cfg.notionToken) {
  console.error('[FATAL] NOTION_TOKEN env var missing');
  process.exit(2);
}
if (!cfg.pgConn) {
  console.error('[FATAL] PG_CONNECTION_STRING env var missing');
  process.exit(2);
}

const tenantSchema = `tenant_${cfg.projectSlug}`;
const startedAt = Date.now();

// ============================================================================
// Donna DLQ helper
// ============================================================================

function donnaDLQ(source, reason, payload) {
  try {
    fs.mkdirSync(cfg.dlqDir, { recursive: true });
    const fname = `${source}-${Date.now()}.json`;
    const fpath = path.join(cfg.dlqDir, fname);
    fs.writeFileSync(fpath, JSON.stringify({
      timestamp: new Date().toISOString(),
      source,
      reason,
      payload,
    }, null, 2));
    console.warn(`[DLQ] ${fpath}`);
    return fpath;
  } catch (err) {
    console.error(`[DLQ ERROR] cannot write: ${err.message}`);
    return null;
  }
}

// ============================================================================
// 1. Fetch all SOPs from Notion
// ============================================================================

async function fetchSops() {
  const notion = new NotionClient({ auth: cfg.notionToken });
  const results = [];
  let cursor = undefined;
  let page = 0;

  while (true) {
    page++;
    try {
      const resp = await notion.databases.query({
        database_id: cfg.notionDbId,
        page_size: 100,
        start_cursor: cursor,
      });
      results.push(...resp.results);
      console.log(`  page ${page} → ${resp.results.length} (cumul ${results.length})`);
      if (!resp.has_more) break;
      cursor = resp.next_cursor;
    } catch (err) {
      // K3 guard: halt on auth failure, no retry
      if (err.code === 'unauthorized' || err.status === 401 || err.status === 403) {
        donnaDLQ('sync-notion-to-supabase', 'K3_AUTH_HALT', {
          status: err.status, code: err.code, message: err.message,
        });
        throw new Error(`K3 PANIC HALT: ${err.status}/${err.code}. Rotate NOTION_TOKEN.`);
      }
      // Other errors: log and rethrow
      donnaDLQ('sync-notion-to-supabase', 'notion_query_failed', {
        page, message: err.message, status: err.status,
      });
      throw err;
    }
  }
  return results;
}

// ============================================================================
// 2. Map Notion page → row object
// ============================================================================

function plainText(richTextArr) {
  if (!Array.isArray(richTextArr)) return null;
  const s = richTextArr.map(t => t.plain_text || '').join('');
  return s.length ? s : null;
}

function mapPage(page) {
  const p = page.properties || {};
  const title = plainText(p.Title?.title) || '';
  const domain = p.Domain?.select?.name || null;
  const status = p.Status?.select?.name || null;
  const number = p.Number?.number ?? null;
  const ownerVp = p.Owner_VP?.select?.name || null;
  const executorB3 = Array.isArray(p.Executor_B3?.multi_select)
    ? p.Executor_B3.multi_select.map(x => x.name)
    : [];
  const trigger = plainText(p.Trigger?.rich_text);
  const buildGate = plainText(p.Build_Gate?.rich_text);
  const templateVersion = plainText(p.Template_Version?.rich_text);
  const loomUrl = p.Loom_URL?.url || null;
  const contextPackUrl = p.Context_Pack_URL?.url || null;
  const lastAudited = p.Last_Audited?.date?.start || null;

  if (!domain || number == null) {
    donnaDLQ('sync-notion-to-supabase', 'missing_domain_or_number', {
      page_id: page.id, title, domain, number,
    });
    return null;
  }

  const nn = String(Math.trunc(number)).padStart(2, '0');
  const sopId = `SOP-L2-${domain.toUpperCase()}-${nn}`;

  return {
    sop_id: sopId,
    notion_page_id: page.id,
    title,
    domain,
    status,
    owner_vp: ownerVp,
    executor_b3: executorB3,
    trigger,
    build_gate: buildGate,
    template_version: templateVersion,
    loom_url: loomUrl,
    context_pack_url: contextPackUrl,
    number,
    last_audited: lastAudited,
    notion_updated_at: page.last_edited_time,
  };
}

// ============================================================================
// 3. UPSERT into Supabase (parameterized — no SQL injection)
// ============================================================================

async function upsertRows(rows) {
  const pg = new PgClient({ connectionString: cfg.pgConn });
  await pg.connect();

  try {
    await pg.query('BEGIN');
    await pg.query(`SET LOCAL search_path = ${tenantSchema}`);

    const upsertSql = `
      INSERT INTO sops (
        sop_id, notion_page_id, title, domain, status, owner_vp, executor_b3,
        trigger, build_gate, template_version, loom_url, context_pack_url,
        number, last_audited, synced_at, notion_updated_at
      ) VALUES (
        $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, now(), $15
      )
      ON CONFLICT (notion_page_id) DO UPDATE SET
        sop_id            = EXCLUDED.sop_id,
        title             = EXCLUDED.title,
        domain            = EXCLUDED.domain,
        status            = EXCLUDED.status,
        owner_vp          = EXCLUDED.owner_vp,
        executor_b3       = EXCLUDED.executor_b3,
        trigger           = EXCLUDED.trigger,
        build_gate        = EXCLUDED.build_gate,
        template_version  = EXCLUDED.template_version,
        loom_url          = EXCLUDED.loom_url,
        context_pack_url  = EXCLUDED.context_pack_url,
        number            = EXCLUDED.number,
        last_audited      = EXCLUDED.last_audited,
        synced_at         = now(),
        notion_updated_at = EXCLUDED.notion_updated_at
    `;

    for (const r of rows) {
      await pg.query(upsertSql, [
        r.sop_id, r.notion_page_id, r.title, r.domain, r.status, r.owner_vp,
        r.executor_b3, r.trigger, r.build_gate, r.template_version,
        r.loom_url, r.context_pack_url, r.number, r.last_audited,
        r.notion_updated_at,
      ]);
    }

    await pg.query(
      `INSERT INTO symphony_log (worker, level, message, payload)
       VALUES ('sync-notion-to-supabase', 'INFO', 'Sync completed',
               jsonb_build_object('count', $1::int, 'duration_ms', $2::int))`,
      [rows.length, Date.now() - startedAt]
    );

    await pg.query('COMMIT');
  } catch (err) {
    await pg.query('ROLLBACK').catch(() => {});
    donnaDLQ('sync-notion-to-supabase', 'pg_upsert_failed', { message: err.message });
    throw err;
  } finally {
    await pg.end();
  }
}

// ============================================================================
// MAIN
// ============================================================================

(async () => {
  console.log(`[start] tenant=${tenantSchema} dryRun=${cfg.dryRun} at=${new Date().toISOString()}`);

  console.log('[1/3] Fetching SOPs from Notion...');
  const pages = await fetchSops();
  console.log(`  total fetched: ${pages.length}`);

  console.log('[2/3] Mapping...');
  const rows = pages.map(mapPage).filter(Boolean);
  console.log(`  valid rows: ${rows.length}`);

  if (cfg.dryRun) {
    console.log('[DRY-RUN] sample rows:');
    console.log(JSON.stringify(rows.slice(0, 3), null, 2));
    console.log(`(${rows.length} rows total — not written)`);
    process.exit(0);
  }

  console.log('[3/3] Upsert into Supabase...');
  await upsertRows(rows);

  const durMs = Date.now() - startedAt;
  console.log(`[ok] ${rows.length} SOPs upserted in ${durMs}ms → ${tenantSchema}.sops`);
  process.exit(0);
})().catch(err => {
  console.error(`[FATAL] ${err.message}`);
  if (err.stack) console.error(err.stack);
  process.exit(1);
});
