'use strict';
try { require('dotenv').config({ path: require('path').join(__dirname, '.env') }); } catch (_) {}
/*
 * Symphony Phase 2 — Bridge: Airtable Briefs 'Approuvé' → ClickUp S2-4 Fast-Track tasks
 *
 * Idempotence : tag ClickUp `br:<BRIEF_ID>` (Airtable formula)
 * Cible       : list "Gestion Fast-Track" (901416200299) dans folder S2-4 Triage
 * Routage      : si Type de Format = texte → +1 task S3-5 Forge Textuelle
 *                si Type de Format = visuel → +1 task S3-6 Forge Visuelle
 *
 * Convention titre task : "[BR-<ID>] CL-<slug> — <Type campagne>"
 * Conforme : ADR-MESH-L2-001 (Airtable=HOW MUCH source), ADR-ID-001 (BRIEF_ID format),
 *            ADR-CK-FREE-001 (tags-only idempotence), ADR-HEART-002 (DLQ + K3 halt)
 */

const fs = require('fs');
const path = require('path');

const cfg = {
  airtableToken: process.env.AIRTABLE_BEARER_AUTH,
  airtableBaseId: process.env.AIRTABLE_BASE_ID || 'appmWf5Xm7w9Ae0ky',
  briefsTableId: process.env.AIRTABLE_BRIEFS_TABLE_ID || 'tblqo7cjdpImMoaVq',
  clickupToken: process.env.CLICKUP_TOKEN,
  fastTrackListId: process.env.CLICKUP_FASTTRACK_LIST_ID || '901416200299',
  forgeTextListId: process.env.CLICKUP_FORGE_TEXT_LIST_ID || null,    // optional routing
  forgeVisualListId: process.env.CLICKUP_FORGE_VISUAL_LIST_ID || null, // optional routing
  dryRun: process.env.DRY_RUN === '1',
  dlqDir: process.env.DLQ_DIR || '/home/amadeus/symphony-workers/_dlq',
};

if (!cfg.airtableToken) { console.error('[FATAL] AIRTABLE_BEARER_AUTH missing'); process.exit(2); }
if (!cfg.clickupToken && !cfg.dryRun) { console.error('[FATAL] CLICKUP_TOKEN missing'); process.exit(2); }

const startedAt = Date.now();

function donnaDLQ(source, reason, payload) {
  try {
    fs.mkdirSync(cfg.dlqDir, { recursive: true });
    const fpath = path.join(cfg.dlqDir, `${source}-${Date.now()}.json`);
    fs.writeFileSync(fpath, JSON.stringify({ timestamp: new Date().toISOString(), source, reason, payload }, null, 2));
    console.warn(`[DLQ] ${fpath}`);
  } catch (e) { console.error(`[DLQ ERROR] ${e.message}`); }
}

// ============================================================================
// Airtable helper
// ============================================================================
async function airtable(endpoint, params = {}) {
  const url = new URL(`https://api.airtable.com/v0/${cfg.airtableBaseId}/${endpoint}`);
  Object.entries(params).forEach(([k, v]) => url.searchParams.set(k, v));
  const resp = await fetch(url.toString(), {
    headers: { 'Authorization': `Bearer ${cfg.airtableToken}` },
  });
  if (resp.status === 401 || resp.status === 403) {
    donnaDLQ('bridge-airtable-to-clickup', 'K3_AIRTABLE_AUTH', { status: resp.status });
    throw new Error(`K3 HALT: Airtable ${resp.status}. Rotate AIRTABLE_BEARER_AUTH.`);
  }
  if (!resp.ok) throw new Error(`Airtable ${resp.status}: ${await resp.text()}`);
  return resp.json();
}

// ============================================================================
// ClickUp helper
// ============================================================================
async function clickup(method, endpoint, body) {
  const resp = await fetch(`https://api.clickup.com/api/v2${endpoint}`, {
    method,
    headers: { 'Authorization': cfg.clickupToken, 'Content-Type': 'application/json' },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (resp.status === 401 || resp.status === 403) {
    donnaDLQ('bridge-airtable-to-clickup', 'K3_CLICKUP_AUTH', { status: resp.status });
    throw new Error(`K3 HALT: ClickUp ${resp.status}. Rotate CLICKUP_TOKEN.`);
  }
  if (!resp.ok) throw new Error(`ClickUp ${method} ${endpoint}: ${resp.status} ${await resp.text()}`);
  return resp.json();
}

// ============================================================================
// Fetch approved briefs from Airtable
// ============================================================================
async function fetchApprovedBriefs() {
  // Filter: Statut du Brief = "Approuvé" (URL-encoded)
  const filter = `{Statut du Brief}='Approuvé'`;
  const briefs = [];
  let offset = undefined;
  do {
    const params = { filterByFormula: filter, pageSize: 100 };
    if (offset) params.offset = offset;
    const data = await airtable(cfg.briefsTableId, params);
    briefs.push(...(data.records || []));
    offset = data.offset;
  } while (offset);
  return briefs;
}

// ============================================================================
// Resolve linked client(s) → CLIENT_ID slug
// ============================================================================
const clientCache = {};
async function resolveClient(recordId) {
  if (clientCache[recordId]) return clientCache[recordId];
  const data = await airtable(`tbluaIHfq2HPUDh1M/${recordId}`);
  const name = data.fields?.['Nom de l\'Agence Cliente'] || data.fields?.['Nom commercial'] || 'unknown-client';
  // Convert to slug-friendly form per ADR-ID-001 D2
  const slug = name.toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '')
    .slice(0, 24);
  clientCache[recordId] = `CL-${slug}`;
  return clientCache[recordId];
}

// ============================================================================
// Index existing ClickUp tasks in target list by tag br:<BRIEF_ID>
// ============================================================================
async function indexExistingTasksByBrief(listId) {
  const byBrief = {};
  let page = 0;
  while (true) {
    const data = await clickup('GET', `/list/${listId}/task?include_closed=true&subtasks=false&page=${page}`);
    if (!data.tasks?.length) break;
    for (const t of data.tasks) {
      for (const tag of (t.tags || [])) {
        if (tag.name.startsWith('br:')) byBrief[tag.name.slice(3)] = t;
      }
    }
    if (data.tasks.length < 30) break;
    page++;
  }
  return byBrief;
}

// ============================================================================
// MAIN
// ============================================================================
(async () => {
  console.log(`[start] base=${cfg.airtableBaseId} list=${cfg.fastTrackListId} dryRun=${cfg.dryRun}`);

  console.log('[1/3] Fetch approved briefs from Airtable...');
  const briefs = await fetchApprovedBriefs();
  console.log(`  ${briefs.length} approved briefs`);
  if (briefs.length === 0) { process.exit(0); }

  console.log('[2/3] Index existing ClickUp tasks (idempotence)...');
  const existing = cfg.dryRun ? {} : await indexExistingTasksByBrief(cfg.fastTrackListId);
  console.log(`  ${Object.keys(existing).length} pre-existing tasks tagged br:*`);

  console.log('[3/3] Create missing tasks...');
  let created = 0, skipped = 0, errors = 0;

  for (const brief of briefs) {
    try {
      const f = brief.fields || {};
      const briefId = f['ID du Brief'] || brief.id;
      if (existing[briefId]) { skipped++; continue; }

      const clientRefs = f['🌞 Clients & Workspaces'] || [];
      const clientId = clientRefs.length ? await resolveClient(clientRefs[0]) : 'CL-unknown';

      const typeCampagne = f['Type de Campagne'] || 'Brief';
      const typeFormat   = f['Type de Format Demandé'] || '';
      const objectif     = f['Objectif de la Campagne'] || '—';
      const deadline     = f['Deadline Souhaitée'] || null;
      const resourcesUrl = f['Lien vers les Ressources Brutes'] || f['Lien vers les Ressources / Raw Assets'] || null;

      const desc = [
        `**BRIEF_ID**: \`${briefId}\``,
        `**Client**: ${clientId}`,
        `**Type**: ${typeCampagne}${typeFormat ? ' / ' + typeFormat : ''}`,
        `**Objectif**: ${objectif}`,
        deadline ? `**Deadline**: ${deadline}` : null,
        resourcesUrl ? `**Resources**: ${resourcesUrl}` : null,
        '',
        `🔗 Airtable: https://airtable.com/${cfg.airtableBaseId}/${cfg.briefsTableId}/${brief.id}`,
        '',
        `_Auto-created by Symphony bridge-airtable-to-clickup. Tag \`br:${briefId}\` ensures idempotence._`,
      ].filter(Boolean).join('\n');

      const payload = {
        name: `[${briefId}] ${clientId} — ${typeCampagne}`,
        description: desc,
        tags: [`br:${briefId}`, `cl:${clientId.slice(3)}`, 'sym:auto', `status:approved`],
        priority: 2,
        // status omitted → ClickUp list default (avoids CRTSK_001)
      };

      if (cfg.dryRun) {
        console.log(`  [DRY] would CREATE in ${cfg.fastTrackListId}: ${payload.name}`);
      } else {
        const newTask = await clickup('POST', `/list/${cfg.fastTrackListId}/task`, payload);

        // Optional: shadow task in Forge list based on Type de Format
        const formatLower = String(typeFormat).toLowerCase();
        let forgeListId = null;
        if (formatLower.match(/text|copy|article|post|email/) && cfg.forgeTextListId) {
          forgeListId = cfg.forgeTextListId;
        } else if (formatLower.match(/visuel|image|video|carousel|motion/) && cfg.forgeVisualListId) {
          forgeListId = cfg.forgeVisualListId;
        }
        if (forgeListId) {
          await clickup('POST', `/list/${forgeListId}/task`, {
            name: `[${briefId}] ${clientId} — Production ${typeFormat}`,
            description: `Linked brief: ${cfg.fastTrackListId}/task/${newTask.id}\n\n${desc}`,
            tags: [`br:${briefId}`, `cl:${clientId.slice(3)}`, 'sym:auto'],
            priority: 2,
          });
          console.log(`    + forge task in ${forgeListId}`);
        }
      }
      created++;
      console.log(`  + ${briefId} (${clientId})`);
    } catch (err) {
      errors++;
      donnaDLQ('bridge-airtable-to-clickup', 'brief_create_failed', {
        airtable_id: brief.id, message: err.message,
      });
      console.error(`  ✗ ${brief.id}: ${err.message}`);
    }
  }

  const durMs = Date.now() - startedAt;
  console.log(`[ok] {fetched:${briefs.length}, created:${created}, skipped:${skipped}, errors:${errors}, duration_ms:${durMs}}`);
  process.exit(errors > 0 && created === 0 ? 1 : 0);
})().catch(err => {
  console.error(`[FATAL] ${err.message}`);
  if (err.stack) console.error(err.stack);
  process.exit(1);
});
