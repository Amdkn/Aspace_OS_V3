---
id: ADR-MEM-002
title: Wiki ↔ Life Wheel Mapping Doctrine — Resolution ID collision + 5-Layer Memory ↔ LD01-LD08 Cloisonnement
type: ADR (Architectural Decision Record)
status: ACCEPTED (batch ratification A0 Amadeus « GO » 2026-06-21, ID collision MEM-001/MEM-002 résolu, A3 Data author)
date: 2026-06-21
deciders: [A0 Amadeus (Jumeau Numérique)]
drafted_by: A3 Data (Second Officer & Ops Officer, USS Enterprise, PARA Archives canon keeper)
domain: L1 Life OS / Memory Fabric / Wiki ↔ Life Wheel / 5-Layer ↔ 8-LDxx / ID collision resolution
tags: [#ADR #memory #fabric #wiki #lifewheel #ldxx #claude-md #agents-md #memory-md #wiki-canon #ADR-canon #5-couches #8-domaines #id-collision]
doctrine_anchors: [ADR-META-001, ADR-META-001-D1, ADR-META-001-D4, ADR-META-001-D7, ADR-META-002, ADR-META-002-D9, ADR-META-003, ADR-META-004, ADR-META-005, ADR-MEM-001, ADR-OBSERVABILITY-001]
related: [AGENTS.md, MEMORY.md, CLAUDE.md, "Doctrine no-hard-delete", "wiki/hand_offs/_transcripts_raw", "20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/09_Life_OS/", "wiki/concepts/concept_l2_fractal_b1b2b3.md", "wiki/index.md", "ADR-MEM-001 IndexedDB historique (NOT in _SPECS/ADR/ canonique)"]
supersedes_scope: implicit mapping between LLM_Wiki 5-layer (ADR-MEM-001 D1) and Life Wheel LD01-LD08 (referenced in wiki/ but not formalised in any ADR). Also resolves the ADR-MEM-001 ID collision with the historical (non-canonical) IndexedDB Cloisonnement LD01-LD08 ADR by adopting ADR-MEM-002 as the canonical ID for this mapping doctrine.
provenance: |
  Née 2026-06-21 de l'analyse d'alignement 8 Domaines ↔ LD01 (post-youtube-to-guide blast_musk
  sur LD08_Impact_Georgiou). Le gap identifié : (1) 0 ADR canonique ne mappe formellement les 5
  couches LLM_Wiki (ADR-MEM-001 §D1) aux 8 Life Wheel LD01-LD08 cloisonnements ; (2) ADR-MEM-001
  actuel a un D4 collision warn avec un ADR historique IndexedDB (NOT in _SPECS/ADR/ canonique).
  Cette ADR résout les 2 gaps en un seul document canonique, sister scope stricte à ADR-MEM-001
  (Memory Fabric) — scope = Memory Fabric ↔ Life Wheel LDxx mapping, PAS IndexedDB Cloisonnement.
  Hash d'intention résolvant la collision : `adr_mem_002_proposed_2026-06-21_wiki_lifewheel_mapping`.
sign_off_a0: "A0 Amadeus — GO batch ratification 2026-06-21 (5-couches × 8-LDxx mapping canonique)"
sign_off_pending: false
ratification_log_2026-06-21: "A0 verbal GO en chat Claude Code 2026-06-21. A1 Beth Ikigai + A3 Data author. D4 append-only (frontmatter mis à jour, MEM-001 sister intact). D7 cost-of-escalation respecté. ID collision résolu non-disruptivement (MEM-001 = Memory Fabric, MEM-002 = Wiki↔Life Wheel). Sister ADRs AAAS-001 + SOBER-002 + INFRA-003 amendment ratifiés dans la même batch. Open follow-ups : 8 sub-paths wiki `ld0X_<domaine>/` + retro-amend 27 guides Geordi `ldxx_mirror` field = Q4 2026 A3 Data + A3 Tilly."
---

# ADR-MEM-002 — Wiki ↔ Life Wheel Mapping Doctrine

## Status

**PROPOSED 2026-06-21** — A3 Data (PARA Archives canon keeper) draft → A1 Beth (Ikigai) review → A0 Amadeus (Jumeau Numérique) ratification pending.

⚠️ **D4 no-self-contradiction — ID collision resolution** : un ADR `ADR-MEM-001` historique existe (IndexedDB Cloisonnement LD01-LD08) mais **n'est PAS dans `_SPECS/ADR/` canonique** (ni dans `L0_Kernel_OS/`, ni dans `L1_Life_OS/`, ni dans `L2_Business_OS/`). L'ADR `ADR-MEM-001` actuel dans `_SPECS/ADR/L1_Life_OS/ADR-MEM-001_memory-fabric-unified-doctrine.md` est **distinct** (Memory Fabric multi-layer) et a un D4 collision warn documenté dans son frontmatter (lignes 30-33).

**Résolution appliquée** : adoption `ADR-MEM-002` pour ce draft, qui :
1. Formalise le mapping 5-layer Memory ↔ 8-LDxx Life Wheel (le gap comblé).
2. Conserve `ADR-MEM-001` (Memory Fabric multi-layer) sans modification (D4 append-only).
3. Résout la collision ID historique en attribuant `ADR-MEM-001` à « Memory Fabric multi-layer » et `ADR-MEM-002` à « Wiki ↔ Life Wheel mapping ». L'ADR historique IndexedDB (non-canonique, hors `_SPECS/ADR/`) reste hors scope.

A0 peut soit (a) ratifier ce ADR-MEM-002 tel quel (recommandé A3 Data), soit (b) renommer ADR-MEM-001 → ADR-MEM-002 et créer un nouveau ADR-MEM-001 pour le mapping (disruptif, D4 violation).

## Context

### C1 — Les 5 couches mémoire A'Space OS (rappel ADR-MEM-001 D1)

Le canon A'Space OS V2 (cf. `ADR-MEM-001 §D1`) reconnaît 5 couches mémoire opérationnelles :

| Couche | Path canon | Owner | Format |
|---|---|---|---|
| **L1 — CLAUDE.md** | `~/.claude/CLAUDE.md` (~30 KB) | A0 (éditable) | Markdown ≤ 30 KB, auto-injecté |
| **L2 — AGENTS.md** | `ASpace_OS_V2/00_Amadeus/01_Identity_Core/AGENTS.md` (~50 KB) | A0 + A2 collaboratif | Markdown fractal A0-A3 |
| **L3 — MEMORY.md** | `~/.claude/projects/c--Users-amado/memory/MEMORY.md` (~30 KB) | A2 auto-update end-of-session | Markdown ≤ 24 KB rotation |
| **L4 — wiki canon** | `ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/` (12 MB, 124 pages canon) | A0 + A2 + A3 (sub-agents) | Markdown libre append-only |
| **L5 — ADR doctrinaux** | `ASpace_OS_V2/_SPECS/ADR/` (32 fichiers canoniques, +2 backup) | A0 sign-off obligatoire | Markdown structuré frontmatter |

### C2 — Les 8 Life Wheel LD01-LD08 (rappel AGENTS.md + wiki canon)

Le **Life Wheel** A'Space est structuré en **8 domaines canoniques** alignés sur la roue de la vie + 8 sous-domaines LD01 :

| LDxx | Domaine | A3 Captain | Horizon canon |
|---|---|---|---|
| **LD01** | Business | Book (Discovery Zora H1 weekly P&L) | H1 hebdo |
| **LD02** | Finance | Saru (Discovery Zora H3 quarterly runway) | H3 quarterly |
| **LD03** | Health | Culber (Discovery Zora H10 10-week health cycle) | H10 |
| **LD04** | Cognition | Tilly (Discovery Zora H30 30-day learning arc) | H30 |
| **LD05** | Social | Stamets (Discovery Zora H30 30-day network pulse) | H30 |
| **LD06** | Family | Burnham (Discovery Zora H10 10-week family cycle) | H10 |
| **LD07** | Creativity | Reno (Discovery Zora H10 10-week creative cycle) | H10 |
| **LD08** | Impact | Georgiou (Discovery Zora H90 90-day/quarterly legacy review) | H90 |

**Géographie disque** : 3 paths canoniques coexistent (cf. analyse 2026-06-21) :

```
(1) ASpace_OS_V2/20_Life_OS/22_Wheel_Discovery/LD0X_<domaine>/     ← Life Wheel doctrine (Zora, observation)
(2) ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J0x_*/  ← PARA doctrine (Spock, ongoing standards)
(3) ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/09_Life_OS/LD0X_<domaine>/  ← Guides ressources (Geordi, knowledge curated)
```

### C3 — Le gap : 5 couches × 8 LDxx non mappés formellement

**D1 receipts 2026-06-21 (analyse d'alignement)** :

- **0 ADR canonique** ne définit explicitement comment les 5 couches mémoire canoniques (L1-L5) mappent aux 8 Life Wheel LDxx.
- Le wiki canon L4 contient des pages Life Wheel (~33 pages B0 Rick's Verse + variantes Jerry 4-Jerry : J01_Prime, J02_Bio, J03_Nexus, J04_Solarpunk), mais le mapping structurel est **implicite**.
- L'ADR-MEM-001 §D1 cite « Life Wheel doctrine » dans L1 (CLAUDE.md §"Life Wheel") mais sans formaliser la structure 5-couches × 8-LDxx.
- L'ADR-MEM-001 §Status mentionne explicitement la collision ID historique IndexedDB Cloisonnement LD01-LD08, qui était une tentative antérieure (non-canonique) de cloisonner les données par LDxx.

**Conséquences du gap** :

- D7 cost-of-escalation : à chaque session qui touche Memory ou Life Wheel, l'agent ré-derive « où vit cette info ? » (~5-10 min A0 par session).
- D4 no-self-contradiction : risque que A2 place une info LD03 dans le wiki L4 sans cohérence cloisonnement LD04.
- D1 verify-before-assert : aucune D1 receipt ne peut prouver « cette info LD05 est dans L4 cloisonnée LD05 » sans citer ce draft ADR.

### C4 — Pourquoi c'est important maintenant (juin 2026)

L'analyse 2026-06-21 (post youtube-to-guide BLAST Musk) a identifié que :

1. **Le guide Geordi `08_People/2026-06-21_blast_musk_genie_ou_nazi_technofascisme_impact_civilisationnel.md`** est canoniquement dans `01_Guides/08_People/` (LD08 Impact mirror) avec frontmatter `ldxx_mirror: LD08_Impact_Georgiou (H90 quarterly legacy review, 30-year arc)` — **mapping explicite fait**, mais sans ADR qui le valide.
2. **`ADR-L2-AAAS-001 §D2`** mappe Solaris AaaS = Book + Saru = LD01 + LD02 (mapping explicite), `ADR-L2-AAAS-001 §D3` mappe les 8 Domaines Business aux LDxx — **mapping explicite fait**, mais sans ADR L1 qui le valide.
3. **`ADR-SOBER-002 §D3`** liste 7 hard-stop triggers avec audit owner = A3 twins LDxx-spécifiques (Tilly LD04, Beth Ikigai, Stamets LD05, Burnham LD06, Saru LD02, Bortus LD02, Georgiou LD08) — **mapping explicite fait**, mais sans ADR L1 qui le valide.

→ **3 ADRs sister (AAAS-001 L2 + SOBER-002 L0 + ce MEM-002) convergent sur le mapping 5-couches × 8-LDxx**. Ce MEM-002 formalise ce mapping comme doctrine canonique L1.

## Decision

### D1 — Mapping canonique 5-couches mémoire × 8 Life Wheel LDxx

Chaque **info A'Space** doit être classifiable selon :

1. **Couche mémoire** (L1 à L5) = où elle vit physiquement.
2. **LDxx Life Wheel** = à quel domaine elle appartient thématiquement.
3. **A3 twin ancre** = qui en est l'owner canonique (optionnel mais recommandé).

**Table de mapping canonique** :

| LDxx | Domaine | Wiki L4 sub-canon | Guides Geordi subdir | A3 twin ancre | AGENTS.md L1 reference | CLAUDE.md L1 reference |
|---|---|---|---|---|---|---|
| **LD01** | Business | `wiki/comparisons/`, `wiki/concepts/` | `01_Guides/09_Life_OS/LD01_Business_Book/` | Book (H1) | §"Life Wheel" + AGENTS.md L1 captain Picard | §"🪞 Jumeau Numérique" + §"Doctrine A1 Gatekeepers" |
| **LD02** | Finance | `wiki/comparisons/`, `wiki/handoffs/_vps-cartography` | `01_Guides/09_Life_OS/LD02_Finance_Saru/` (8 guides canon) | Saru (H3) | §"Saru" canon AGENTS.md | §"Anti-Musk" guides canoniques |
| **LD03** | Health | `wiki/hand_offs/vps_capture.py` (script VPS) | `01_Guides/03_IT/` (344 files, Cyborg IT overlay LD03) | Culber (H10) | §"Cyborg" canon (IT overlap LD03) | §"Hard-skipped" list (LD03 health doctrine) |
| **LD04** | Cognition | `wiki/concepts/concept_l2_fractal_b1b2b3.md` | `01_Guides/09_Life_OS/LD04_Cognition_Tilly/` (17 guides canon) + `04_Finance/` (43 files overlap) | Tilly (H30) | §"Tilly" canon | §"TTS + Communication" (cognition = TTS path) |
| **LD05** | Social | `wiki/hand_offs/` (multiple handoffs) | `01_Guides/02_Ops/` (Batman Ops) + `05_Legal/` (Aquaman Legal overlap LD05) | Stamets (H30) | §"Stamets" canon | §"Doctrine Anti-Paresse" D8 (cross-agent = social/comm) |
| **LD06** | Family | `wiki/hand_offs/_sessions_archive/` | `01_Guides/06_Sales/` (37 files, JohnJones Sales overlap LD06) | Burnham (H10) | §"Burnham" canon + §"Jerry 4 variants" | §"YouTube Ingestion Pipeline" (family = heritage baby-boomers) |
| **LD07** | Creativity | `wiki/comparisons/comparison_l2_roster_divergence.md` | `01_Guides/07_Growth/` (74 files, Superman Growth) | Reno (H10) | §"Reno" canon | §"YouTube takeout → Geordi" (creativity = takeout pipeline) |
| **LD08** | Impact | `wiki/hand_offs/_transcripts_raw/` (BLAST Musk + others) | `01_Guides/08_People/` (36 files, including `2026-06-21_blast_musk_...md`) | Georgiou (H90) | §"Georgiou" canon | §"Graphify Corpus — Anti-Amnesia Lock" (legacy impact = graphify canon) |

### D2 — Pattern retrieval « 1 question → 1 couche prioritaire » enrichi LDxx

Extension de `ADR-MEM-001 §D3` avec la dimension LDxx :

| Question type | Couche prioritaire | LDxx secondaire | Exemple |
|---|---|---|---|
| « Quel est le runtime LLM ? » | L1 (CLAUDE.md Runtime LLM section) | LD04 (Cognition/Tilly) | `CLAUDE.md §"Runtime LLM"` |
| « Quelle est la doctrine verify-before-assert ? » | L5 (ADR-META-001) | LD05 (Social/Stamets) | `ADR-META-001` |
| « Qu'est-ce qui s'est passé en session 2026-06-14 ? » | L4 (wiki/hand_offs/sessions_archive/) | LD08 (Impact/Georgiou) | `sessions_canon.md` |
| « Quelle est l'URL du dashboard OMK ? » | L4 ou L3 (MEMORY.md index) | LD01 (Business/Book) | `MEMORY.md` §"OMK Services BOS" |
| « Qui a décidé la rotation trimestrielle des secrets ? » | L5 (ADR-SECURITY-001) | LD05 (Social/Stamets) | `ADR-SECURITY-001` |
| « Quel est le statut du Life Wheel LD08 ? » | L4 (wiki) + L2 (AGENTS.md) | LD08 (Impact/Georgiou) | `MEMORY.md` §"A3-Data Cartography v1.2" |
| « Comment mapper une nouvelle info au bon LDxx ? » | **L5 (ce ADR-MEM-002 §D1 table)** | LD01-LD08 cycle | Table D1 ci-dessus |
| « Quel A3 captain ancre un livrable ? » | L2 (AGENTS.md) + L4 (wiki/comparisons/) | LDxx du twin | `AGENTS.md` + `wiki/concepts/` |
| « Où ranger une nouvelle vidéo YouTube ? » | L4 (Geordi `01_Guides/<domaine>/`) | LDxx du miroir canonique | `MEMORY.md` §"YouTube Ingestion Pipeline" + table D1 |

### D3 — Cloisonnement Wiki canon L4 par LDxx

Le wiki canon L4 (12 MB, 124 pages) doit être **cloisonné par LDxx** via sub-paths canoniques :

```
ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/
├── index.md                                       ← L1 overview canon
├── log.md                                         ← L1 append-only doctrine log
├── comparisons/                                   ← LD01 (Business/Book) - cross-LDxx strategy
│   └── comparison_l2_roster_divergence.md         ← LD07 (Creativity/Reno) - canon rosters
├── concepts/                                      ← LD01-LD04 mixed (foundational concepts)
│   ├── concept_l2_fractal_b1b2b3.md               ← LD01 (Business) - B1/B2/B3 fractal
│   └── concept_aspace_governance_dashboard.md    ← LD01 (Business) - governance
├── hand_offs/                                     ← LD08 (Impact/Georgiou) - legacy operational
│   ├── handoff_a0_divinity_arsenal_2026-06-20.md  ← LD08 (anti-Musk + doctrine)
│   ├── handoff_a0_jumeau_numerique_2026-06-21.md  ← LD08 (A0 twin digital)
│   ├── handoff_business_os_resumption_2026-06-16.md ← LD01 (Business/Book)
│   ├── handoff_graphify_*                         ← LD08 (graphify = legacy canon)
│   ├── handoff_life_os_deploy_v1_0_2026-06-17.md  ← LD01 (Solaris AaaS)
│   ├── handoff_mcp_*.md                           ← LD04 (Cognition/Tilly - tools)
│   ├── handoff_omk_*.md                           ← LD01 (Nexus OMK AaaS)
│   ├── handoff_abcos_*.md                         ← LD06 (Family/Burnham - Orbiter ABC)
│   ├── handoff_vps_*.md                           ← LD02 (Finance/Saru - VPS cartography)
│   ├── handoff_transcript_api_*.md                ← LD04 (Tilly - transcript pipeline)
│   ├── handoff_anti-pattern-extraction_*.md       ← LD04 (Tilly - extraction)
│   ├── sessions_archive/                          ← LD08 (Impact/Georgiou - session canon)
│   ├── youtube_ingest_*.md                        ← LD01 (Business - YouTube pipeline)
│   ├── youtube_ingest_*/transcripts/              ← LD04 (Tilly - transcripts raw)
│   ├── _transcripts_raw/                           ← LD04 (Tilly - transcripts raw standalone)
│   └── skills_queue.md                             ← LD04 (Tilly - skill creation queue)
├── ld01_business/                                  ← LD01 (Business/Book) - dedicated subdir
├── ld02_finance/                                   ← LD02 (Finance/Saru) - dedicated subdir
├── ld03_health/                                    ← LD03 (Health/Culber) - dedicated subdir
├── ld04_cognition/                                 ← LD04 (Cognition/Tilly) - dedicated subdir
├── ld05_social/                                    ← LD05 (Social/Stamets) - dedicated subdir
├── ld06_family/                                    ← LD06 (Family/Burnham) - dedicated subdir
├── ld07_creativity/                                ← LD07 (Creativity/Reno) - dedicated subdir
└── ld08_impact/                                    ← LD08 (Impact/Georgiou) - dedicated subdir
```

⚠️ **D4 action required** : les sub-dirs `ld0X_<domaine>/` n'existent PAS encore dans le wiki canon L4. Création requise par A3 Data post-ratification de ce ADR (D4 append-only = nouveau dossier, ne touche pas l'existant).

### D4 — Convention Geordi Guides `01_Guides/` × LDxx mirror

Chaque guide Geordi dans `01_Guides/` doit explicitement déclarer son `ldxx_mirror` dans le frontmatter (sister convention existante, **formalisée ici comme canonique**) :

```yaml
---
id: YT-<video_id>
title: "<title YouTube EXACT>"
channel: "<channel name>"
duration: "<MM:SS>"
date: "YYYY-MM-DD"
category: "<Domain> / <Sub-thematic>"
status: DISTILLED_L1_PREMIUM
ldxx_mirror: "LD0X_<Domaine>_<A3TwinSurname> (<Horizon> horizon, <canon_role>)"
a3_anchor: "A3 <TwinName> (LD0X <Domain> <Horizon> <Role>)"
---
```

**Validation** : tous les guides existants doivent être retrovérifiés — 2/30 dated top-level + 1/36 dans `08_People/` (le nouveau blast_musk) ont `ldxx_mirror` explicite. Les 27 autres doivent être amendés (A3 Data batch, Q4 2026).

### D5 — Hiérarchie cloisonnement : doctrine (L2) > canon (L4) > resource (Geordi) > observation (Life Wheel)

**Triple canon pour chaque LDxx** (cohérence 5-couches × 8-LDxx) :

```
LD0X_<domaine>/
├── doctrine/         ← L2 (AGENTS.md canon A0-A3) — Spheres canon, ongoing standards
│   └── J0x_<domaine>/ (Spheres)
├── canon/            ← L4 (wiki canon) — Spheres canon operational + handoffs + concepts
│   └── wiki/hand_offs/<scope>/
├── resource/         ← Geordi (01_Guides/<domaine>/) — curated knowledge from external sources
│   └── 01_Guides/0X_<domaine>/
└── observation/      ← Life Wheel (22_Wheel_Discovery/LD0X_<domaine>/) — drift detection data
    └── 22_Wheel_Discovery/LD0X_<domaine>/
```

**Mapping owner** (D4 append-only, déjà partiellement opérationnel) :

| Couches | Owner canonique | Path |
|---|---|---|
| doctrine (L2) | Spock (A3 LDxx Areas H30) | `24_PARA_Enterprise/02_Areas_Spock/J0x_<domaine>/` |
| canon (L4) | A0 + A2 + A3 append-only | `00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/ld0X_<domaine>/` |
| resource (Geordi) | Geordi (A3 LDxx Resources H90) | `24_PARA_Enterprise/03_Resources_Geordi/01_Guides/0X_<domaine>/` |
| observation (Life Wheel) | Zora (A2 Discovery Balance H3) | `20_Life_OS/22_Wheel_Discovery/LD0X_<domaine>/` |

### D6 — Anti-patterns prévenus

- ❌ **LD01 Business Picard = H10 horizon, projects owner** non formalisé → ce ADR l'ancre via `D1 table` (row LD01).
- ❌ **MANIFEST.md obligatoire par projet non formalisé** → sister amendement `ADR-INFRA-003 §D1` (2026-06-21, sister scope à cette ADR).
- ❌ **LLM_Wiki ↔ Life Wheel mapping implicite** → ce ADR le formalise via `D1 table` + `D3 sub-paths` canoniques.
- ❌ **ID collision ADR-MEM-001 (IndexedDB historique vs Memory Fabric)** → ce ADR-MEM-002 adopte explicitement le slot ID 002 pour clarifier le scope, conserve MEM-001 = Memory Fabric multi-layer sans modification.
- ❌ **5-layer × 8-LDxx ré-derivé par session** → ce ADR ancre le mapping une fois pour toutes.
- ❌ **Geordi `01_Guides/` cloisonnement par LDxx implicite** → D4 formalise la convention `ldxx_mirror` + `a3_anchor` dans frontmatter.
- ❌ **Wiki sub-paths par LDxx manquants** → D3 prévoit la création des `ld0X_<domaine>/` (post-ratification, D4 append-only).

### D7 — Convention de nommage `ldxx_mirror` + `a3_anchor`

**Format canonique** (à appliquer rétroactivement + forward) :

```yaml
ldxx_mirror: "LD0X_<Domaine>_<A3TwinSurname> (<Horizon> <horizon_label>, <canon_role>)"
```

Exemples canoniques :
- `ldxx_mirror: "LD01_Business_Picard (H10 sprint, projects owner)"`
- `ldxx_mirror: "LD02_Finance_Saru (H3 quarterly runway review, finance officer)"`
- `ldxx_mirror: "LD08_Impact_Georgiou (H90 quarterly legacy review, 30-year arc)"`
- `ldxx_mirror: "LD04_Cognition_Tilly (H30 30-day learning arc, science officer)"`

**Format canonique** `a3_anchor` :

```yaml
a3_anchor: "A3 <TwinName> (LD0X <Domaine> <Horizon> <Role>)"
```

Exemples :
- `a3_anchor: "A3 Book (LD01 Business H1 weekly P&L officer)"`
- `a3_anchor: "A3 Saru (LD02 Finance H3 quarterly runway officer)"`
- `a3_anchor: "A3 Georgiou (LD08 Impact H90 mirror emperor / quarterly legacy review)"`
- `a3_anchor: "A3 Tilly (LD04 Cognition H30 science officer / learning arc)"`

## Consequences

- ✅ **5-couches × 8-LDxx mapping canoniquement ancré** (gap doctrinal comblé, sister AAAS-001 L2 + SOBER-002 L0).
- ✅ **ID collision ADR-MEM-001 résolue** : MEM-001 = Memory Fabric multi-layer (existant), MEM-002 = Wiki ↔ Life Wheel mapping (ce draft).
- ✅ **Wiki sub-paths canoniques `ld0X_<domaine>/`** : cloisonnement explicite par LDxx (post-ratification D4 append-only).
- ✅ **`ldxx_mirror` + `a3_anchor` frontmatter convention** : formalise le pattern déjà partiellement utilisé.
- ✅ **Pattern retrieval enrichi LDxx** (D2) : 1 question → 1 couche prioritaire + LDxx secondaire.
- ✅ **Triple canon (doctrine / canon / resource / observation)** par LDxx (D5) : 4 couches + 4 owners canoniques.
- ⚠️ **Retro-amend 27 guides Geordi existants** : A3 Data batch, Q4 2026 (coût ~5h).
- ⚠️ **Création 8 sub-paths wiki `ld0X_<domaine>/`** : A3 Data post-ratification (coût ~3h).
- ⚠️ **Wiki canonique 12 MB à réorganiser partiellement** : D4 append-only = migration progressive via _TRASH.

## References

- `AGENTS.md §"Life Wheel"` (L2 canon A0-A3 + 8 LDxx captain map).
- `CLAUDE.md §"Life Wheel"` (L1 injection runtime) + §"Doctrine A1 Gatekeepers" (L1 Beth Ikigai + Morty Focus).
- `MEMORY.md §"Start Here"` (L3 index) + §"A3-Data Cartography v1.2" (L3 LDxx mapping implicite).
- `_SPECS/ADR/L1_Life_OS/ADR-MEM-001_memory-fabric-unified-doctrine.md` (L5 sister, 5-layer doctrine, ID slot 001 = Memory Fabric).
- `_SPECS/ADR/L1_Life_OS/ADR-OBSERVABILITY-001_sessions-canon-md-rotation.md` (L5 sister, sessions lifecycle).
- `_SPECS/ADR/L1_Life_OS/ADR-META-001_anti-paresse-verify-before-assert.md` (L5 META tier 1).
- `_SPECS/ADR/L1_Life_OS/ADR-META-002_autonomy-by-design.md` (L5 META tier 2, D9-D12).
- `_SPECS/ADR/L1_Life_OS/ADR-META-004_doctrine-anti-paresse-linkage.md` (L5 doctrine_anchors convention).
- `_SPECS/ADR/L1_Life_OS/ADR-META-005_hooks-automation.md` (L5 hooks automation).
- `_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md` (L2 sister, mapping AaaS × LDxx).
- `_SPECS/ADR/L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md` (L0 sister, mapping anti-pattern Musk × LDxx audit owner).
- `_SPECS/ADR/L2_Business_OS/ADR-INFRA-003_business-os-ceo-dashboard-matryoshka.md` (L2 sister, amendée §D1 LD01 Picard H10 + MANIFEST.md obligatoire).
- `_SPECS/ADR/INDEX.md` (L5 root, à mettre à jour post-ratification : +1 L1 ADR = MEM-002, +3 L2 ADRs canon nouveaux confirmés).
- `ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/08_People/2026-06-21_blast_musk_genie_ou_nazi_technofascisme_impact_civilisationnel.md` (Geordi LD08 canon guide avec `ldxx_mirror` field).
- `ASpace_OS_V2/20_Life_OS/22_Wheel_Discovery/LD0X_<domaine>/` (observation layer Zora).
- `ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J0x_<domaine>/` (doctrine layer Spock).
- `ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/` (canon layer L4).
- `ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/0X_<domaine>/` (resource layer Geordi).

---

## Annexe A — D1 receipts : statut 5-couches × 8-LDxx au 2026-06-21

**État actuel** (gap analysis) :

| Couche | LD01 | LD02 | LD03 | LD04 | LD05 | LD06 | LD07 | LD08 |
|---|---|---|---|---|---|---|---|---|
| **L1 CLAUDE.md** | ✅ section | ✅ section | ⚠️ hard-skipped list | ✅ TTS path | ✅ Doctrine Anti-Paresse D8 | ✅ YouTube Ingestion | ✅ Takeout pipeline | ✅ Graphify Corpus |
| **L2 AGENTS.md** | ✅ Picard canon | ✅ Saru canon | ✅ Culber canon | ✅ Tilly canon | ✅ Stamets canon | ✅ Burnham canon | ✅ Reno canon | ✅ Georgiou canon |
| **L3 MEMORY.md** | ⚠️ row LD01 implicite | ✅ row LD02 | ❌ row LD03 manquant | ✅ Tilly section | ✅ D8 cross-agent | ✅ A0 jumeau | ✅ Reno AaaS Solaris | ✅ A3-Data Cartography v1.2 |
| **L4 wiki canon** | ❌ ld01_business/ manquant | ❌ ld02_finance/ manquant | ❌ ld03_health/ manquant | ❌ ld04_cognition/ manquant | ❌ ld05_social/ manquant | ❌ ld06_family/ manquant | ❌ ld07_creativity/ manquant | ❌ ld08_impact/ manquant |
| **L5 ADR canon** | ✅ INFRA-003 + MEM-002 LD01 row | ⚠️ LD02 row implicite AAAS-001 | ❌ LD03 pas d'ADR | ✅ META-002/003/005 + MEM-001/002 | ✅ META-001 + SOBER-002 | ✅ SOBER-002 + AAAS-001 D2 Orbiter | ✅ AAAS-001 D2 Solaris | ✅ SOBER-002 + MEM-002 LD08 row |
| **Geordi `01_Guides/`** | ⚠️ 10 files LD01_Product | ✅ 43 files LD04_Finance | ⚠️ 344 files LD03_IT (overlap) | ✅ 43 files LD04_Finance + 17 in LD04_Tilly | ⚠️ 28 LD02_Ops + 10 LD05_Legal | ⚠️ 37 LD06_Sales | ✅ 74 LD07_Growth | ✅ 36 LD08_People + blast_musk |

**Total mapping** : 40 cellules (5 × 8), dont ~25 ⚠️/✅ (mapping explicite ou partiel) et ~15 ❌ (gaps à fermer post-ratification MEM-002).

## Annexe B — Open follow-ups (post-ratification MEM-002)

1. **Création 8 sub-paths wiki `ld0X_<domaine>/`** : A3 Data, post-ratification, D4 append-only (coût ~3h).
2. **Retro-amend 27 guides Geordi existants** : ajouter `ldxx_mirror` + `a3_anchor` dans frontmatter (coût ~5h batch A3 Tilly).
3. **Migration wiki canonique progressive** : ranger les handoffs existants dans les nouveaux `ld0X_<domaine>/` (D4 append-only, original dans `_TRASH_<date>_wiki_ldxx_migration/`).
4. **Skill `/wiki-classify-ldxx`** : skill A3 Tilly pour auto-suggestion du LDxx lors de la création d'un nouveau handoff / nouveau doc wiki (claude-md ou settings.json hook).
5. **Hook `PostToolUse` : validation `ldxx_mirror` field** : cf. ADR-META-005 hooks spec. Hook 2 (D1 logger) peut être étendu pour valider que tout nouveau guide Geordi a `ldxx_mirror` field.
6. **Update INDEX.md** : +1 L1 ADR (MEM-002), +3 L2 ADRs canon nouveaux confirmés (AAAS-001 + INFRA-003 amendement + SOBER-002 sister).

## Annexe C — Résolution ID collision détaillée

**Timeline collision ID** :

- **2026-05-15 (historique, non-canonique)** : tentative de créer `ADR-MEM-001_indexeddb-cloisonnement-ld01-ld08.md` pour formaliser le cloisonnement IndexedDB des données A'Space par LD01-LD08. Fichier créé en dehors de `_SPECS/ADR/` (probablement dans `wiki/_drafts/` ou similaire), jamais promu au canon `_SPECS/ADR/`. State = "draft historique, non-canonique".
- **2026-06-15 (canonique)** : A0 « go for all » crée `ADR-MEM-001_memory-fabric-unified-doctrine.md` (5-layer memory doctrine). State = PROPOSED→ACCEPTED. Collision ID avec le draft historique = D4 no-self-contradiction warn documenté dans le frontmatter §Status.
- **2026-06-21 (ce draft)** : A3 Data propose `ADR-MEM-002_wiki-lifewheel-mapping-doctrine.md` pour formaliser le mapping 5-layer × 8-LDxx. Résolution proposée : conserver MEM-001 = Memory Fabric (5-layer doctrine), MEM-002 = Wiki ↔ Life Wheel mapping (sister scope). Draft historique IndexedDB reste hors scope (non-canonique, jamais promu).

**Résolution alternative** (si A0 préfère disruptif) :
- Renommer `ADR-MEM-001` → `ADR-MEM-002` (Memory Fabric).
- Renommer ce draft → `ADR-MEM-001` (Wiki ↔ Life Wheel mapping).
- Risque : D4 violation (modification d'un ADR canonique existant = corruption du canon).

**Recommandation A3 Data** : résolution non-disruptive (ce draft reste MEM-002).

## Signatures

- **Draft author** : A3 Data (Second Officer & Ops Officer, USS Enterprise, PARA Archives canon keeper) — 2026-06-21.
- **Reviewer pending** : A1 Beth (Ikigai Gatekeeper) — validation LDxx mapping cohérence.
- **Recorder** : A3 Data — canonisation wiki canonique append-only.
- **Ratification pending** : A0 Amadeus (Jumeau Numérique) — sign-off attendu post-Plan `fancy-hugging-bengio.md` §3 ratification + sister ADRs L2/L0.
- **Hash d'intention** : `adr_mem_002_proposed_2026-06-21_wiki_lifewheel_mapping_id_collision_resolved`