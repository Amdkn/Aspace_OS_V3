---
id: B2_AREA_SUPERMAN_EXTRACTION_QUEUE
layer: B2_AREA_SUPERVISION
surface: Jerry Area J01 LD01 Business
domain: Growth
b2_owner: Superman
b3_swarm: Guardians
status: SHADOW_ACTIVE
updated: 2026-05-29
source_corpus: 20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/07_Growth/Yann_Leonardi
---

# Superman Extraction Queue — Backlog Guardians (corpus Yann Leonardi)

Backlog réel du swarm Guardians : distiller les ressources Yann Leonardi en principes (v2) + tactiques actionnables. Chaque item = un JTBD que Superman score RICE (P5) et assigne à un Guardian. Source = connaissance, pas agent.

## Statut global

| Catégorie | Total | Distillé | Reste |
|-----------|-------|----------|-------|
| Frameworks (nourrissent les principes) | ~17 | 12 ✅ | ~5 (tactiques) |
| Case studies (illustrations) | ~38 | 0 | ~38 |

> **v2 (2026-05-28)** : Lot 1 frameworks principaux distillés → **6 nouveaux principes P13-P18** dans `03_SUPERMAN_GROWTH_PRINCIPLES.md` (total 18). Reste : Q5/Q8/Q9/Q10/Q12 (tactiques sous principes existants) + Lot 2 case studies.

## Rock actif B3

```yaml
rock_id: J01-B2-GROWTH-2026-01
status: active_shadow
owner_b2: Superman
assigned_swarm: Guardians
north_star_metric: "ICP-qualified AaaS opportunities generated from non-paid channels"
definition_of_done:
  - "AaaS ICP filter with explicit rejection criteria exists."
  - "Voice-of-customer packet contains 5 sourced pain statements."
  - "Painkiller message packet contains 3 testable variants."
  - "First non-paid experiment has RICE score, lead indicator, lag indicator, and proof plan."
```

## JTBD actif — premier lancement

| JTBD | Lead | Supports | Source | Output | Statut |
|------|------|----------|--------|--------|--------|
| `J01-B3-GROWTH-2026-001` | Gamora | Mantis, Star-Lord, Groot | Q1/Q7/P8/P13/P16 | ICP filter + VOC packet + 3 painkiller hypotheses + RICE score | `READY` |

## Lot 0 — DÉJÀ DISTILLÉ (→ 03_SUPERMAN_GROWTH_PRINCIPLES.md v1)

- [x] AARRR framework → P1, P2, P3, P12
- [x] What is Growth Hacking (8 truths) → P1, P6, T-Shaped
- [x] Growth Hacking Process → P4, P5, P6, P7
- [x] Vitamine/Painkiller/Candy → P8
- [x] Les clients dont vous ne voulez pas → P9, P10, P11

## Lot 1 — FRAMEWORKS PRIORITAIRES (v2 principes) — Gamora/Rocket lead

> Priorité haute : ces ressources créent de nouveaux principes ou affinent les existants. RICE à scorer par Superman.

| # | Ressource | Principe | Guardian | Statut |
|---|-----------|----------|----------|--------|
| Q1 | Product-Market Fit + How do you know if you have PMF | **P13** (test Sean Ellis 40%) | Gamora | ✅ distillé v2 |
| Q2 | Inbound vs Content Marketing | **P18** (infrastructure vs création) | StarLord | ✅ distillé v2 |
| Q3 | SEO bases référencement | **P14** (4 intentions de recherche) | StarLord | ✅ distillé v2 |
| Q4 | Cocon sémantique (internal linking) | **P14** (silos + jus de lien) | StarLord | ✅ distillé v2 |
| Q5 | 3 conseils SEO résultats immédiats | tactique sous P14 | StarLord | ⏳ reste |
| Q6 | Opt-in : 4 erreurs collecte emails | **P15** (discipline opt-in) | Rocket | ✅ distillé v2 |
| Q7 | Process Com 6 types de personnalités | **P16** (message-persona fit) | StarLord | ✅ distillé v2 |
| Q8 | 5 Instagram marketing tips | tactique (hook<3s, save ratio, DM auto) | StarLord/Rocket | ⏳ reste |
| Q9 | 5 erreurs Facebook Ads | tactique (acquisition payante) | Rocket | ⏳ reste |
| Q10 | Marketing automation (Mautic) | tactique sous P2/P18 | Rocket | ⏳ reste |
| Q11 | Onboarding : exemple Superhuman | **P13 + P17** (PMF + concierge/gatekeeping) | Gamora/Rocket | ✅ distillé v2 |
| Q12 | Stop using a traditional blog / Dropshipping / Un créatif ou marketeux | méta-positionnement | StarLord | ⏳ reste |

## Lot 2 — CASE STUDIES (illustrations des principes) — distillation légère

> Priorité basse : ne créent pas de principe, mais **illustrent** les principes existants. Distiller en 1-2 lignes "quel principe ce cas démontre". Batch quand Lot 1 fini.

**Marques / Growth** : Red Bull, Doctolib, Twitch, Slack, Starbucks, Rolex, Meero, Wish, Asphalte, Le Slip Français, Le Bon Marché, Clubhouse, Superhuman.
**Personnalités / Créateurs** : Léna Situations, Khaby Lame, Jul, Booba (+ Harvard), NWA, Yomi Denzel, Stéphane Edouard, Osama Ammar, Alexandre Astier, JP Fanguin (MLM).
**Rebranding / Crise** : Jaguar (destroy to reborn), Domino's, Crisis Marketing Covid, OK Boomer, Trump vs BLM (clivage), LinkedIn weirdness.
**Business models** : PMU (absurd strategy), Coffee shop scam, Stranger Things (nostalgie), "cette maladie rapporte gros", "sa petite entreprise ne connaît pas la crise".

## Protocole d'extraction (JTBD type)

```yaml
jtbd_id: J01-B3-GROWTH-EXTRACT-NN
source_resource: resource_xxx.md
guardian: assigned
job_statement: "Distiller [ressource] en principe/tactique actionnable L2 Growth, écarter le boilerplate Obsidian/RAG/souveraineté hors-sujet."
output:
  - principe ajouté/affiné dans 03_SUPERMAN_GROWTH_PRINCIPLES.md (si framework)
  - OU 1 ligne d'illustration mappée à un principe existant (si case study)
proof_required: "diff du fichier principes + citation source"
anti_pattern: "ne PAS recopier affine_deal_drafts.md (pollué : duplication, vides, hors-sujet L1)"
```

## Note qualité (dette identifiée)

`affine_deal_drafts.md` (92KB) du corpus est **non exploitable en l'état** : duplication massive, entrées vides, boilerplate générique, contenu détourné vers Life OS (Obsidian/RAG personnel) au lieu de L2 Growth business. **Ne pas l'utiliser comme source.** Travailler directement depuis les `resource_*.md` individuels. Régénération propre = item séparé (hors backlog Growth, plutôt tâche Ops/Pipelines 12th Doctor).

*B2 backlog under Superman. Feeds B3 Guardians via JTBD. Last sync: 2026-05-29*

---

## Inbox v3 — à distiller par Superman (ajout A0 2026-05-31)

- **The Playbook for a $100M AI Agency** (`YT-8ktcSaSTvxk`, Nate Herkelman) — fiche : `03_Resources_Geordi/01_Guides/07_Growth/playbook-for-a-100m-ai-agency.md`. Concepts : **positionnement mid-market** (ni TPE volatiles ni grands comptes lents), **défendabilité post-2027** (intégrations profondes vs automatisations superficielles obsolètes avec les LLM natifs), **découplage de la prestation** en conseil full-stack (discovery/ROI/architecture) packagé en actifs reproductibles + **Exit Playbook / Built-to-Sell**. → nuance le positionnement & la défendabilité de la doctrine Growth ; ponts Ops (P19 audit, P21 marge) + Sales (S6 cabinet conseil).
