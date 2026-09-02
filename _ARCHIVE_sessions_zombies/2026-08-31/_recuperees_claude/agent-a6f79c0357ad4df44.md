---
session: agent-a6f79c0357ad4df44
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\de35c5f1-6944-47f6-b8bc-849452b0313a\subagents\agent-a6f79c0357ad4df44.jsonl
debut: 2026-07-25T10:24:56.709Z
fin: 2026-07-25T10:29:37.078Z
messages_utilisateur: 1
reponses_assistant: 1
titre: "You are a skill creator sub-agent. Read this brief, then execute. ## Mission Create a NEW skill `/youtube-to-B…"
---

## >>> UTILISATEUR #1

You are a skill creator sub-agent. Read this brief, then execute.

## Mission

Create a NEW skill `/youtube-to-Businessos` at `C:\Users\amado\.claude\skills\youtube-to-Businessos\SKILL.md`.

## What this skill does

Takes a YouTube transcript OR an existing Geordi guide and routes it directly to the **8 Business OS domains** (RH & Méta-Gouvernance, Ops, Growth, Cognition, People, Finance, IT/R&D, Legal) WITHOUT going through the B1 Gatekeeper filter layer. This is for the case where A+ wants a quick per-domain routing (like `/youtube-to-B1filter` but bypassing the B1 Green Lantern lens).

## Sister skills to reference (don't duplicate)

1. `/youtube-to-para` (`C:\Users\amado\.claude\skills\youtube-to-para\SKILL.md`) : ingestion + ADR drafts (funnel ENTRÉE)
2. `/youtube-to-guide` (`C:\Users\amado\.claude\skills\youtube-to-guide\`) : distillation premium par vidéo
3. `/youtube-to-B1filter` (`C:\Users\amado\.claude\skills\youtube-to-B1filter\SKILL.md`) : filtre B1 Green Lantern + 6 livres + Triptyques
4. `/b1-filter` (`C:\Users\amado\.claude\skills\b1-filter\SKILL.md`) : deterministic LD sweep

## 8 Business OS domains (per ADR-CANON-001 + ADR-RH-META-GOUVERNANCE-001)

| # | Domain | Lead B2 | Squad B3 | Triptyque |
|---|---|---|---|---|
| 01 | **RH & Méta-Gouvernance** (was People) | Green Lantern | X-Men | T1 LEAD |
| 02 | **Ops** | Batman | Fantastic Four | T1 member |
| 03 | **Growth** | Flash | Avengers | T2 |
| 04 | **Cognition & Savoir** | J'onn J'onzz | Illuminati | T2 |
| 05 | **People** (note: 01 = RH, 05 = People — keep distinct) | Superman | Guardians of the Galaxy | T2 |
| 06 | **Finance** | Wonder Woman | Thunderbolts | DUO |
| 07 | **IT/R&D** | Light + Cyborg | Kang Dynasty | T1 member |
| 08 | **Legal & Conformité** | Aquaman | Eternals | DUO |

(Note: the Canon has TWO People entries — old `01_People` (now re-cast as RH & Méta-Gouvernance per ADR-RH-META-GOUVERNANCE-001) and `05_People` (Superman × Guardians, classical HR). The skill must respect this dual mapping and route accordingly.)

## Structure to create

1. **Frontmatter** with name `youtube-to-Businessos`, description with trigger phrases ("youtube to businessos", "route to business domain", "skip b1 filter", "direct 8-domain routing", "AI Tool X for Sales/Finance/etc").

2. **§0 Why this skill exists** — D3 nuance : A+ sometimes wants direct 8-domain routing without the B1 Green Lantern lens overhead. This skill is the **fast path** when the resource is clearly a business function delivery (not an agent/staffing/HR question).

3. **§1 Routing table** — for each of the 8 domains, give 5-10 trigger keywords / filename patterns that route to it. Especially:
   - "AI Tool / Automate / SaaS for [Sales Pipeline / Finance Tracking / Code Gen / etc]" → the BUSINESS DOMAIN (not 08_People)
   - "RPA / SOP / Workflow / Systemize" → 02_Ops
   - "Funnel / Ads / Acquisition / Growth Hack" → 03_Growth
   - "Second Brain / NotebookLM / Knowledge Base / Obsidian" → 04_Cognition
   - "Onboarding / Culture / Talent / HR" → 05_People (classical HR, NOT 01)
   - "Pricing / Unit Economics / LTV:CAC / Billing" → 06_Finance
   - "API / SDK / Infra / Code-from-scratch / DevOps" → 07_IT
   - "RGPD / CCPA / AI-Act / Compliance / NDA" → 08_Legal
   - "AI Agents / Sub-agents / SOUL / Multi-agent / Swarm" → 01_RH & Méta-Gouvernance

4. **§2 Workflow** — 4-step pipeline:
   - Input : transcript or Geordi guide path
   - Step 1 : Read frontmatter + first 200 lines (no full read, anti-pattern D6 context blowup)
   - Step 2 : Match against §1 routing table → assign domain
   - Step 3 : Emit `domain: 0X_<Domain>` frontmatter (D4 append-only)
   - Step 4 : If matched to 01_RH & Méta-Gouvernance, flag for X-Men Coach review (link to `/youtube-to-B1filter`)

5. **§3 §Trio+ update** — note this skill joins the family:
   - `/youtube-to-para` : ENTRÉE funnel (ingestion)
   - `/youtube-to-guide` : DISTILLATION premium (8 sections)
   - `/youtube-to-B1filter` : FILTRE B1 GATEKEEPER (Green Lantern lens + 6 livres)
   - **`/youtube-to-Businessos` (CE skill)** : ROUTAGE DIRECT 8 DOMAINES BUSINESS (fast path, no B1 lens)
   - `/b1-filter` : SWEEP déterministe (frontmatter LD)
   - `/youtube-takeout-to-lifeos` : CAPTURE bulk takeout

6. **§4 Doctrine ancrage** — D1-D8 :
   - D1 : 0 domain invented, match by keyword evidence
   - D2 : read `/youtube-to-B1filter` §1 routing table first to avoid conflict
   - D3 : nuance = BUSINESS FUNCTION not HUMAN ROLE (the AI Tool routing fix)
   - D4 : append-only frontmatter
   - D5 : "routed" = `grep "domain: 0X" <path>` = 1 + `wc -c` ≥ 1000
   - D6 : anti-context-blowup (200 lines max read)
   - D7 : no auto-ratify of any ADR
   - D8 : can be parallelized via /swarm-orchestrator (8 sub-agents, 1 per domain)

7. **§5 Anti-patterns** :
   - ❌ Routing "AI Tool for X" to 08_People (legacy mis-routing — D6 root cause)
   - ❌ Mixing 01_RH & Méta-Gouvernance with 05_People classical HR
   - ❌ Routing a resource to multiple domains (pick the PRIMARY one, secondary in `cross_domain: [...]`)

8. **§6 Cross-refs** — link to all 4 sister skills + ADR-CANON-001 + ADR-RH-META-GOUVERNANCE-001

## Constraints

- **D4 append-only** on sister skills : DO NOT modify `/youtube-to-para`, `/youtube-to-guide`, `/youtube-to-B1filter`, `/b1-filter`. Just create the new skill.
- **Read each sister SKILL.md** before writing yours (D2 research-first) — D1 receipt : list the 4 files you read.
- **Skill must be self-contained** : assume the user invokes `/youtube-to-Businessos` standalone, no prerequisites.
- **D1 receipts** : list sister files read, structure created, sections added.
- **No scripts/** needed — this skill is pure routing logic, no Python.

## Output

Write `C:\Users\amado\.claude\skills\youtube-to-Businessos\SKILL.md` directly. Return:
1. D1 receipts (which sister files you read, structure created)
2. The 8-domain routing table (markdown, copy-pasteable)
3. Confirmation that NO sister skill was modified (D4 append-only)

### assistant

## Skill Created — D1 Receipts

**File created** : `C:\Users\amado\.claude\skills\youtube-to-Businessos\SKILL.md` (8.5K chars, 9 sections)

### D1 Receipts — Sister files read (D2 research-first)

| Sister file | Path | Bytes read |
|---|---|---|
| `/youtube-to-para` | `C:\Users\amado\.claude\skills\youtube-to-para\SKILL.md` | 259 lines (full read) |
| `/youtube-to-guide` | `C:\Users\amado\.claude\skills\youtube-to-guide\SKILL.md` | 335 lines (full read) |
| `/youtube-to-B1filter` | `C:\Users\amado\.claude\skills\youtube-to-B1filter\SKILL.md` | 269 lines (full read) |
| `/b1-filter` | `C:\Users\amado\.claude\skills\b1-filter\SKILL.md` | 87 lines (full read) |

### Structure créée (9 sections)

1. **Frontmatter** — name `youtube-to-Businessos` + description with 6 trigger phrases
2. **§0 Why this skill exists** — D3 nuance : fast path NO B1 lens for clear business-function deliveries
3. **§1 Les 8 Domaines Business OS** — canonical mapping table with DUAL People mapping (01_RH & Méta-Gouvernance vs 05_People classical HR)
4. **§2 Routing table** — 8 domains × 5-10 keywords + filename patterns each
5. **§3 Workflow** — 4-step pipeline (INPUT → SCORING → EMIT FRONTMATTER → X-Men coach flag conditionnel)
6. **§4 §Trio+ update** — 6-row table distinguishing all YouTube/B1 skills
7. **§5 Doctrine ancrage** — D1-D8 + ADR-SOBER-003 PPR
8. **§6 Anti-patterns** — 7 anti-patterns (including the legacy mis-routing D6 root cause)
9. **§7 Cross-refs** — 4 sister skills + 4 ADR canoniques + mindsets
10. **§8 Open follow-ups** — 5 Phase 2 autonomy items

### 8-Domain Routing Table (copy-pasteable)

| # | Domain (frontmatter `domain:`) | Lead B2 | Squad B3 | Triptyque | Routing keywords |
|---|---|---|---|---|---|
| 01 | `RH & Méta-Gouvernance` | Green Lantern | X-Men | T1 LEAD | ai agent, sub-agent, SOUL, multi-agent, swarm, agentic, MCP server, harness pattern |
| 02 | `Ops` | Batman | Fantastic Four | T1 member | RPA, SOP, workflow automation, systemize, runbook, n8n, Zapier |
| 03 | `Growth` | Flash | Avengers | T2 | funnel, ads, acquisition, growth hack, SEO, PLG, go-to-market |
| 04 | `Cognition & Savoir` | J'onn J'onzz | Illuminati | T2 | second brain, NotebookLM, Obsidian, RAG, vector DB, PARA, knowledge graph |
| 05 | `People` (classical HR) | Superman | Guardians | T2 | onboarding, culture, talent, HR, hiring, recruiting, performance review, DEI |
| 06 | `Finance` | Wonder Woman | Thunderbolts | DUO | pricing, unit economics, LTV, CAC, billing, runway, burn rate, ARR, MRR, Stripe |
| 07 | `IT/R&D` | Light + Cyborg | Kang Dynasty | T1 member | API, SDK, infra, DevOps, Kubernetes, TypeScript, Next.js, Supabase |
| 08 | `Legal & Conformité` | Aquaman | Eternals | DUO | RGPD, CCPA, AI-Act, compliance, NDA, MSA, SOC2, ISO 27001, data privacy |

### D4 Confirmation — NO sister skill modified

- `/youtube-to-para/SKILL.md` : **untouched** (read-only)
- `/youtube-to-guide/SKILL.md` : **untouched** (read-only)
- `/youtube-to-B1filter/SKILL.md` : **untouched** (read-only)
- `/b1-filter/SKILL.md` : **untouched** (read-only)
- Only created the new skill at the new path

### Key design decisions

- **No scripts/** : pure routing logic (algorithme scoring documenté en mental model, pas implémenté en Python — le skill reste déclaratif)
- **DUAL People mapping respecté** : `01_RH & Méta-Gouvernance` (Green Lantern × X-Men, agentique) vs `05_People` (Superman × Guardians, HR classique) — triage par D3 nuance, pas par keyword seul
- **AI Tool routing fix (D6 #2026-07-22)** : "AI Tool for X" route vers le business function X (Growth/Finance/Ops/IT), PAS vers 08_People (legacy mis-routing)
- **D3 nuance advisory X-Men coach review** : quand routed vers 01_RH & Méta-Gouvernance, recommend `/youtube-to-B1filter` (PPR lane, pas un gate A0)
- **Anti-context-blowup** : 200 lignes max read + `/swarm-chunk-transcript` si > 6K chars
- **PPR lane** : routing = D4 append-only, jamais d'A0 HITL pour le routage (seules les ratifications ADR sont destructives)
