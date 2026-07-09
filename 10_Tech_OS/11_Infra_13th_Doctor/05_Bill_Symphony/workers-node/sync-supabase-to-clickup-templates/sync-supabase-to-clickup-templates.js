'use strict';
try { require('dotenv').config({ path: require('path').join(__dirname, '.env') }); } catch (_) { /* opt */ }
/*
 * Symphony Phase 2 — Worker Node: tenant_<slug>.sops (Active) → ClickUp list "Active SOPs Master Templates"
 *
 * Convention titre task : "[SOP_ID] {Domain} — {Title}"  (cf. ADR-ID-001 D5)
 * Tag d'idempotence    : "sop:<SOP_ID>"                  (cf. ADR-CK-FREE-001 D4)
 *
 * Conforme :
 *   ADR-MESH-L2-001 (Notion=WHAT, Supabase=cache, ClickUp=WHEN)
 *   ADR-CK-FREE-001 (zero Custom Field, tags + title-prefix only)
 *   ADR-HEART-002   (K1/K3 via try/catch + DLQ)
 *   ADR-INFRA-001   (PM2 cron, autorestart:false)
 *
 * Env requis (cf. ecosystem.config.js + .env):
 *   PG_CONNECTION_STRING
 *   PROJECT_SLUG          (default 'aspace_solaris')
 *   CLICKUP_TOKEN         (Personal API Token pk_xxx)
 *   CLICKUP_TARGET_LIST_ID (default '901416812179' = Active SOPs Master Templates)
 *   DRY_RUN               ('1' to preview without writing to ClickUp)
 */

const { Client: PgClient } = require('pg');
const fs = require('fs');
const path = require('path');

const cfg = {
  pgConn: process.env.PG_CONNECTION_STRING,
  projectSlug: process.env.PROJECT_SLUG || 'aspace_solaris',
  clickupToken: process.env.CLICKUP_TOKEN,
  targetListId: process.env.CLICKUP_TARGET_LIST_ID || '901416812179',
  dryRun: process.env.DRY_RUN === '1',
  dlqDir: process.env.DLQ_DIR || '/home/amadeus/symphony-workers/_dlq',
};

if (!cfg.pgConn) { console.error('[FATAL] PG_CONNECTION_STRING missing'); process.exit(2); }
if (!cfg.clickupToken && !cfg.dryRun) { console.error('[FATAL] CLICKUP_TOKEN missing'); process.exit(2); }

const tenantSchema = `tenant_${cfg.projectSlug}`;
const startedAt = Date.now();
const CLICKUP_API = 'https://api.clickup.com/api/v2';

// ============================================================================
// DLQ helper
// ============================================================================
function donnaDLQ(source, reason, payload) {
  try {
    fs.mkdirSync(cfg.dlqDir, { recursive: true });
    const fpath = path.join(cfg.dlqDir, `${source}-${Date.now()}.json`);
    fs.writeFileSync(fpath, JSON.stringify({ timestamp: new Date().toISOString(), source, reason, payload }, null, 2));
    console.warn(`[DLQ] ${fpath}`);
  } catch (e) { console.error(`[DLQ ERROR] ${e.message}`); }
}

// ============================================================================
// ClickUp API helper (with K3 auth guard)
// ============================================================================
async function clickup(method, endpoint, body) {
  const url = `${CLICKUP_API}${endpoint}`;
  const opts = {
    method,
    headers: {
      'Authorization': cfg.clickupToken,
      'Content-Type': 'application/json',
    },
  };
  if (body) opts.body = JSON.stringify(body);

  const resp = await fetch(url, opts);
  const text = await resp.text();
  const data = text ? JSON.parse(text) : null;

  if (resp.status === 401 || resp.status === 403) {
    donnaDLQ('sync-supabase-to-clickup-templates', 'K3_AUTH_HALT', {
      status: resp.status, endpoint, message: data?.err || data?.ECODE || text,
    });
    throw new Error(`K3 PANIC HALT: ClickUp ${resp.status}. Rotate CLICKUP_TOKEN.`);
  }
  if (!resp.ok) {
    throw new Error(`ClickUp ${method} ${endpoint} → ${resp.status}: ${text}`);
  }
  return data;
}

// ============================================================================
// Fetch active SOPs from Supabase
// ============================================================================
async function fetchActiveSops() {
  const pg = new PgClient({ connectionString: cfg.pgConn });
  await pg.connect();
  try {
    await pg.query(`SET search_path = ${tenantSchema}`);
    const { rows } = await pg.query(
      `SELECT sop_id, title, domain, status, owner_vp, executor_b3, trigger,
              build_gate, loom_url, context_pack_url, notion_page_id, last_audited
         FROM sops
        WHERE status = 'Active'
        ORDER BY domain, number`);
    return rows;
  } finally {
    await pg.end();
  }
}

// ============================================================================
// Index existing ClickUp tasks by tag sop:<SOP_ID>
// ============================================================================
async function indexExistingTasks() {
  const tasks = [];
  let page = 0;
  while (true) {
    const data = await clickup('GET', `/list/${cfg.targetListId}/task?include_closed=true&subtasks=false&page=${page}`);
    if (!data.tasks || data.tasks.length === 0) break;
    tasks.push(...data.tasks);
    if (data.tasks.length < 30) break;  // ClickUp returns 30 per page
    page++;
  }
  const byTag = {};
  for (const t of tasks) {
    for (const tag of (t.tags || [])) {
      if (tag.name.startsWith('sop:')) {
        byTag[tag.name.slice(4)] = t;
      }
    }
  }
  console.log(`  indexed ${tasks.length} existing tasks (${Object.keys(byTag).length} sop-tagged)`);
  return byTag;
}

// ============================================================================
// Build/Update task per SOP
// ============================================================================
function buildTaskPayload(sop) {
  const desc = [
    `**SOP_ID**: \`${sop.sop_id}\``,
    `**Domain**: ${sop.domain}`,
    `**Owner**: ${sop.owner_vp || '—'}`,
    `**Executor squads**: ${(sop.executor_b3 || []).join(', ') || '—'}`,
    '',
    `**Trigger**: ${sop.trigger || '—'}`,
    `**Build Gate**: ${sop.build_gate || '—'}`,
    `**Last audited**: ${sop.last_audited || '—'}`,
    '',
    `🔗 Notion: https://www.notion.so/${sop.notion_page_id.replace(/-/g, '')}`,
    sop.loom_url ? `📹 Loom: ${sop.loom_url}` : null,
    sop.context_pack_url ? `📦 Context Pack: ${sop.context_pack_url}` : null,
    '',
    `_Auto-synced by Symphony worker sync-supabase-to-clickup-templates. Edits will be overwritten._`,
  ].filter(Boolean).join('\n');

  return {
    name: `[${sop.sop_id}] ${sop.domain} — ${sop.title}`,
    description: desc,
    tags: [`sop:${sop.sop_id}`, `dom:${sop.domain.toLowerCase()}`, 'sop:template'],
    priority: 3,  // 1=urgent, 2=high, 3=normal, 4=low
    // status omitted → ClickUp uses list default (avoids CRTSK_001)
  };
}

async function upsertTaskForSop(sop, existing) {
  const payload = buildTaskPayload(sop);

  if (existing) {
    // Update existing task (PUT excludes tags — handled separately)
    const updatePayload = {
      name: payload.name,
      description: payload.description,
    };
    if (cfg.dryRun) {
      console.log(`  [DRY] would UPDATE ${existing.id} ← ${payload.name}`);
      return 'updated';
    }
    await clickup('PUT', `/task/${existing.id}`, updatePayload);
    return 'updated';
  } else {
    if (cfg.dryRun) {
      console.log(`  [DRY] would CREATE ${payload.name}`);
      return 'created';
    }
    await clickup('POST', `/list/${cfg.targetListId}/task`, payload);
    return 'created';
  }
}

// ============================================================================
// Log synthesis to symphony_log
// ============================================================================
async function logSummary(summary) {
  const pg = new PgClient({ connectionString: cfg.pgConn });
  await pg.connect();
  try {
    await pg.query(`SET search_path = ${tenantSchema}`);
    await pg.query(
      `INSERT INTO symphony_log (worker, level, message, payload)
       VALUES ('sync-supabase-to-clickup-templates', 'INFO', 'Sync completed', $1::jsonb)`,
      [JSON.stringify(summary)]);
  } finally {
    await pg.end();
  }
}

// ============================================================================
// MAIN
// ============================================================================
(async () => {
  console.log(`[start] tenant=${tenantSchema} list=${cfg.targetListId} dryRun=${cfg.dryRun}`);

  console.log('[1/3] Fetch active SOPs from Supabase...');
  const sops = await fetchActiveSops();
  console.log(`  ${sops.length} active SOPs`);
  if (sops.length === 0) {
    console.log('Nothing to sync.');
    process.exit(0);
  }

  console.log('[2/3] Index existing ClickUp tasks...');
  const existing = cfg.dryRun ? {} : await indexExistingTasks();

  console.log('[3/3] Upsert tasks...');
  let created = 0, updated = 0;
  for (const sop of sops) {
    try {
      const res = await upsertTaskForSop(sop, existing[sop.sop_id]);
      if (res === 'created') created++;
      else updated++;
      console.log(`  ${res === 'created' ? '+' : '↻'} ${sop.sop_id}: ${sop.title}`);
    } catch (err) {
      donnaDLQ('sync-supabase-to-clickup-templates', 'upsert_failed', {
        sop_id: sop.sop_id, message: err.message,
      });
      console.error(`  ✗ ${sop.sop_id}: ${err.message}`);
    }
  }

  const durMs = Date.now() - startedAt;
  const summary = { fetched: sops.length, created, updated, duration_ms: durMs };
  console.log(`[ok] ${JSON.stringify(summary)}`);

  if (!cfg.dryRun) await logSummary(summary);
  process.exit(0);
})().catch(err => {
  console.error(`[FATAL] ${err.message}`);
  if (err.stack) console.error(err.stack);
  process.exit(1);
});
