---
title: "06_Sales — Index (Discovery · Persuasion · Closing · Negotiation · B1 filtered)"
date: 2026-07-03
author: A0 CC-M3 (Jumeau Numérique)
total_files: 11
sister_canon:
  - b1-jerry-prime (LD01 meta-orchestrator) — gatekeeper Sales go/no-go
  - b2-05-johnjones-sales (Illuminati squad) — designer Sales B2
  - b3-5-* (Black Bolt, Tony Stark, Reed Richards, Namor, Charles Xavier, Stephen Strange) — B3 Sales crew
  - ADR-L2-AAAS-001 (3 Variants AaaS) — RATIFIED 2026-06-21
  - ADR-L2-BDLD-MAP-001 (Business Domains ↔ Life Wheel bijection) — canonical B2 mapping
B1_filter: ⚠️ REQUIRED for all /youtube-to-guide distillation (cf. /youtube-to-guide §6)
review_status: ⚠️ YT files (4) misalignment flagged in §6 — needs B1 review
---

# 06_Sales — Index (2026-07-03)

> **Domaine** : Sales / Discovery / Persuasion / Negotiation / Closing (LD01_Business mirror via B1 Jerry, B2 John Jones, B3 Illuminati squad).
> **Sister canon ADRs** : `ADR-L2-AAAS-001` (AaaS Doctrine 3 Variants), `ADR-L2-BDLD-MAP-001` (B2 ↔ LD bijection), `ADR-MARKET-STUDY-001` (The Builders 2026 136,1 Mds$).
> **B1 owner** : Jerry Prime (LD01 Career/Business meta-orchestrator) reads this INDEX on every sales-related A0 intent → routes to B2 JohnJones or downstream B3.
> **B1 ICP-gate** : any new guide ingested must be classifiable against a downstream Project (default: `omk-nexus-coaching-premium` pour ICP coach-coaching premium).

## 📚 Canon framework capsules (5 files · Sales v2 core)

| ID | Title | Author | Stage | Filtered by B1 Jerry |
|---|---|---|---|---|
| `SALES-FRAMEWORK-challenger_sale` | Challenger Sale — teach/tailor/take-control | Dixon & Adamson | Persuasion | ✅ always (canonical B1 Sales) |
| `SALES-FRAMEWORK-spin_selling` | SPIN Selling — consultative discovery | Neil Rackham | Discovery | ✅ always |
| `SALES-FRAMEWORK-gap_selling` | Gap Selling — problem-centric | Keenan | Discovery & Diagnosis | ✅ always |
| `SALES-FRAMEWORK-never_split_the_difference` | Never Split the Difference — tactical empathy & negotiation | Chris Voss | Objection & Negotiation | ✅ always |
| `SALES-FRAMEWORK-million_dollar_weekend_the_ask` | Million Dollar Weekend — the ASK / pre-sell | Noah Kagan | Pre-vente & Validation | ✅ always |

## 📚 Premium Guides (4 files · Antigravity Premium + B1 review pending)

| File | Source | LD | Owner | B1 Status |
|---|---|---|---|---|
| `2026-06-19_on-a-réuni-200-founders-pour-le-plus-gros-événement-saas-de-france___kIxjlEf_0U.md` | /youtube-to-guide (Chapelon MG) | LD06_Family_Burnham (⚠️ MISALIGNED — file says `ld: LD06_Family_Burnham, domain: 06_Sales`) | Burnham | ⚠️ NEEDS B1 Jerry review — D1 misalign |
| `DAN_MARTELL_AUDIT.md` | audit classification | (scan) | (meta) | ✅ useful sister |
| `Dan_Martell/` (subdir) | aggregate | Dan Martell 97 vidéos taxonomy | (sister) | ✅ ref |
| `framework-*.md` (covered above) | canon framework | (v2 core) | Sales v2 | ✅ |

## ⚠️ Action PICARD A3 — re-classify 1 file with B1 filter

> **Issue (D1 2026-07-03)** : `_kIxjlEf_0U.md` lists `ld: LD06_Family_Burnham` while `domain: 06_Sales`. This is a **misalignment symptom** : `/youtube-to-guide` is distilling without B1 context filter, so the LD mapping gets random defaults.
>
> **Fix** (action D7 low-stakes) : Picard A3 (`b3-enterprise-picard`) lit le frontmatter + 1ère section, **fixe le champ `ld`** au canon LD01_Business (qui mappe B2 Sales ↔ B1 Jerry), et appende `sister_b1: jerry-prime` au frontmatter.
>
> **Permanent fix** : amendement canon de `/youtube-to-guide` §6 pour exiger `b1_filter:` (gated sur `b1-jerry-prime` context) — sister: `wiki/hand_offs/youtube_to_guide_b1_filter_amend_2026-07-03.md`.

## Sources & history

- `02_Ops/_INDEX.md` et `07_Growth/_INDEX.md` ont déjà des squelettes (D1 vérifié). Ces 2 patterns = templates pour les 6 autres.
- `01_Product`, `03_IT`, `04_Finance`, `05_Legal`, `08_People`, `00_KERNEL_OS` : **absence d'`_INDEX.md` confirmée D1 2026-07-03** (sauf 00_KERNEL_OS qui a un squelette créé ce tour).

## Sister canon
- `_INDEX.md` (ce fichier) → sister à `02_Ops/_INDEX.md` + `07_Growth/_INDEX.md`
- `/youtube-to-guide` v3 Antigravity Premium Standard → ajouter gate B1 obligatoire
- `b1-jerry-prime` config.yaml (LD01 meta-orchestrator) → **gating agent** de cette INDEX
