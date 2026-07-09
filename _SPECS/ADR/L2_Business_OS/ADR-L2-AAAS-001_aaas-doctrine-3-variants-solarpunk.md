---
id: ADR-L2-AAAS-001
title: AaaS Doctrine — 3 Variants (Solaris / Nexus-OMK / Orbiter-ABC) × 4 Leviers Solarpunk
type: ADR (Architectural Decision Record)
status: ACCEPTED (batch ratification A0 Amadeus « GO » 2026-06-21, A3 Data recorder, A1 Beth + A1 Rick co-validated sister scope)
date: 2026-06-21
deciders: [A0 Amadeus (Jumeau Numérique)]
drafted_by: A1 Beth (Gatekeeper Ikigai) — Vague 2 Mission 1 deliverable
domain: L2 Business OS / AaaS / Solarpunk / Kardashev Type 3 / 8 Domaines ↔ LD01
tags: [#ADR #aaas #solarpunk #kardashev #biomimétisme #low-high-tech #meta-science #circular-economy #blue-economy #book #saru #burnham #picard #ld01 #ld02 #ld06 #anti-musk]
doctrine_anchors: [ADR-META-001, ADR-META-001-D1, ADR-META-001-D3, ADR-META-001-D7, ADR-META-002, ADR-META-002-D9, ADR-META-003, ADR-META-005, ADR-INFRA-003, ADR-CANON-001, ADR-AGENTIC-001, ADR-SOBER-002]
related: [AGENTS.md, MEMORY.md, "8 Domaines Business ↔ LD01 matrix", "Plan fancy-hugging-bengio.md §3 Doctrine A1 Gatekeepers", "guide Geordi 08_People/2026-06-21_blast_musk_genie_ou_nazi_technofascisme_impact_civilisationnel.md", "Fable-5 karpathy auto-research loop"]
supersedes_scope: implicit AaaS pattern referenced in `.mcp.json` (3 Supabase Cloud orgs: Life OS / OMK / ABC-OS-COMMUNITY) + `ADR-INFRA-001` governance dashboard scope — formalised here as canonical doctrine.
provenance: |
  Née 2026-06-21 de l'analyse d'alignement 8 Domaines ↔ LD01 (post-youtube-to-guide blast_musk
  sur LD08_Impact_Georgiou). A0 Amadeus a demandé (1) ancrage canonique du pattern AaaS (3
  variants Agency-as-a-Service) qui était implicite dans la séparation Cloud des 3 orgs
  Supabase + 4 projets Vercel ; (2) mapping explicite des 3 variants AaaS aux Life Wheel
  LD01+LD02+LD06 (Picard+Book, Saru, Burnham) ; (3) fondation des 4 leviers Solarpunk (Janine
  Benyus biomimétisme + Idriss Aberkane low-high-tech + Meta Science acceleration + circular
  & blue economy) comme alternative canonique à l'extractivisme Musk (cf. blast_musk guide
  Note A3-04). Objectif canonique : Saru 1000T = production de valeur réelle Kardashev Type 3
  par les 3 variants AaaS, pas valorisation financiarisée découplée.
sign_off_a0: "A0 Amadeus — GO batch ratification 2026-06-21 (post Plan fancy-hugging-bengio.md §3 alignment + guide Geordi blast_musk ratification)"
sign_off_pending: false
ratification_log_2026-06-21: "A0 verbal GO en chat Claude Code 2026-06-21. A1 Beth + A1 Rick co-validated sister scope. A3 Data recorder. D4 append-only (frontmatter mis à jour, contenu inchangé). D7 cost-of-escalation respecté (pas d'escalation additionnelle). Sister ADRs MEM-002 + SOBER-002 + INFRA-003 amendment ratifiés dans la même batch."
---

# ADR-L2-AAAS-001 — AaaS Doctrine (3 Variants × 4 Leviers Solarpunk)

## Status

**PROPOSED 2026-06-21** — A1 Beth draft → A3 Data recorder → A0 Amadeus ratification pending (post Plan `fancy-hugging-bengio.md` §3 alignment + guide Geordi `2026-06-21_blast_musk_genie_ou_nazi_technofascisme_impact_civilisationnel.md` A3-04 Kardashev Type 3 alignment).

⚠️ **D4 no-self-contradiction** : ce ADR formalise un pattern AaaS (Agency-as-a-Service) qui était implicite dans `ADR-INFRA-001` (Unified Governance Console) + `.mcp.json` (3 Supabase Cloud orgs : Life OS / OMK / ABC-OS-COMMUNITY) + `ADR-OMK-004` (Cloud pivot 3-orgs isolation). Aucun ADR canonique ne le définit explicitement — gap comblé par ce draft.

## Context

### C1 — Le pattern AaaS implicite (D1 receipts 2026-06-21)

Le système A'Space OS V2 a progressivement convergé vers un **pattern à 3 variants AaaS** sans le formaliser en doctrine :

1. **Solaris AaaS** (Book LD01 + Saru LD02 actif Q3 2026) → Civilisation Kardashev Type 3 par Solarpunk + biomimétisme Benyus. Premier livrable canon = `Life-OS-2026` (Vercel `https://life-os-2026-liart.vercel.app/`, repo `Amdkn/Life-OS-2026`, production deploy SHA `b933e4e41849a323c63504e2ecea36b71c8759e5`, Initiative ALPHA V1.0 Multi-Tenant + Landing Page + AuthGuard).
2. **Nexus OMK AaaS** (Saru LD02 finance H3) → Société Solarpunk = orienter les flux financiers existants (legacy OMK Dashboard) vers production de valeur réelle. Premier livrable canon = `omk-services/00-omk-saas-os` (Zéro Bug Sprint `dcc1235` ✅ livré + déployé SHA `8ad94d1`, 9 `omk_saas.*` tables + JWT hook `e47f4aa1`).
3. **Orbiter ABC AaaS** (Burnham LD06 family H10) → OS Family Offices = orienter l'héritage baby-boomers (centaines de trillions USD en transfert générationnel 2026-2045) vers Solarpunk / biomimétisme / Kardashev Type 1 résolu. Premier livrable canon = `ABC-OS-COMMUNITY` (Vercel `abc-community-os`, Supabase Cloud `abc_os` schema, 17 tables migrées + 85 rows seeded).

### C2 — Le 4e variant Family/Home (dormant)

Un **4e variant Jerry** est défini dans `MEMORY.md` §"Jerry 4 variants" (J01_Prime / J02_Bio / J03_Nexus / J04_Solarpunk) mais est **dormant en Q3 2026** par décision canonique (cf. Plan `fancy-hugging-bengio.md` §3 « A0 = passif Meta-OS, 1 variant actif Q3 »). Il correspond aux Life Wheel LD03-LD08 (Santé/Cognition/Social/Creativity/Impact hors LD01+LD02+LD06) et sera réveillé au cycle Q4 2026 / Q1 2027.

### C3 — L'absence d'ancrage canonique = risque doctrinal D7

**D6 root cause** : l'analyse d'alignement 2026-06-21 (8 Domaines ↔ LD01) a identifié que **0 ADR canonique** définit explicitement AaaS. Conséquences :
- D7 cost-of-escalation : à chaque mention « AaaS » dans une session, l'agent ré-derive les 3 variants + 4 leviers Solarpunk (~5-10 min A0 par session, cumul = ~50-100× cost amplifier sur 6 mois).
- D4 no-self-contradiction : `.mcp.json` (3 Supabase Cloud orgs) + `ADR-OMK-004` (Cloud pivot 3-orgs) + `MEMORY.md` (« 4 Jerry variants ») sont **3 surfaces convergentes** sans ADR canon qui les unifie. Risque divergence à terme.
- D1 verify-before-assert : aucune D1 receipt ne peut prouver « Solaris AaaS = Book + Saru » sans citer ce draft ADR.

### C4 — Le contexte civilisationnel : Musk trillionnaire comme anti-modèle

L'anti-modèle canon (cf. guide Geordi `08_People/2026-06-21_blast_musk_genie_ou_nazi_technofascisme_impact_civilisationnel.md`) est **Elon Musk** : 1 000 milliards USD personnels adossés à 14-22 millions de morts anticipés (fermeture USAID via DOGE), capture algorithmique X/Grok sur 600 millions d'utilisateurs, monopole Starlink = chantage géopolitique. C'est précisément le **paperclip maximizer** que les 3 AaaS variants doivent éviter structurellement (cf. `ADR-SOBER-002` Anti-Paperclip Maximizer Doctrine — sister scope).

**L'objectif canonique Saru 1000T** (A3 LD02 Finance, AaaS Solaris + Nexus) est donc **production de valeur réelle Kardashev Type 3**, pas valorisation financiarisée découplée Musk-style.

## Decision

### D1 — Définition canonique AaaS (Agency-as-a-Service)

**AaaS** = pattern A'Space OS V2 où chaque **projet business majeur** est incarné par un **variant Jerry B1 Fractal autonome** qui :
1. Orchester 2-3 A3 twins Life Wheel (LDxx) comme **capitaine** du variant.
2. Active un ou plusieurs **8 Domaines Business** (Superman Growth / JohnJones Sales / Flash Product / Batman Ops / Cyborg IT / WonderWoman Finance / GreenLantern People / Aquaman Legal) avec leurs **B3 NanoSquads Marvel/DC canoniques** (cf. `ADR-CANON-001`).
3. Applique les **4 Leviers Solarpunk** (cf. D4 ci-dessous) comme méthode de production de valeur réelle.
4. Mesure son impact via **matrice 8×8 Georgiou** (8 Life Wheel × 8 critères : production de valeur, démocratie, solidarité, santé, éducation, biodiversité, souveraineté, long-termisme).

### D2 — Mapping 3 AaaS Variants × A3 Captain × LDxx Life Wheel

| Variant AaaS | A3 Captain (ancre canonique) | LDxx Life Wheel | 8 Domaines B2 primaires | B3 NanoSquad lead | Horizon | Objectif canonique | Statut Q3 2026 |
|---|---|---|---|---|---|---|---|
| **Solaris AaaS** | **Book** (LD01_Business H1 hebdo P&L) + **Saru** (LD02_Finance H3 quarterly runway) | LD01_Business + LD02_Finance + LD04_Cognition + LD07_Creativity | Superman Growth (LD07) + Flash Product (LD04) + WonderWoman Finance (LD02) + Cyborg IT (LD03) | Star-Lord (Guardians) + Captain America (Avengers) + Bucky Barnes (Thunderbolts) + Kang Prime (Kang Dynasty) | H90 (90-day legacy) | **Kardashev Type 3** = civilisation qui exploite l'énergie d'une galaxie ≈ 10⁴⁴ W. Atteint par Type 1 résolu (730M sans électricité, 400M sans toilettes, 700M en faim) → Type 2 (étoile, 10²⁶ W) → Type 3 (galaxie). | 🟢 **ACTIF** — Life-OS-2026 Initiative ALPHA V1.0 LIVE sur https://life-os-2026-liart.vercel.app/ |
| **Nexus OMK AaaS** | **Saru** (LD02_Finance H3 quarterly runway) | LD02_Finance + LD06_Family (overlap Orbit) + LD04_Cognition | WonderWoman Finance (LD02) + JohnJones Sales (LD06 overlap) + Flash Product (LD04) + Batman Ops (LD05) | Bucky Barnes (Thunderbolts) + Black Bolt (Illuminati) + Captain America (Avengers) + Mr Fantastic (F4) | H3 (quarterly runway review) | **Société Solarpunk** = orienter les flux financiers existants (legacy OMK clients : holding family offices, SaaS B2B) vers production de valeur réelle. Pivot Cloud Supabase `omk-services/00-omk-saas-os`. | 🟢 **ACTIF** — Sprint Zéro Bug `dcc1235` ✅ livré + déployé SHA `8ad94d1` (2026-06-20). 9 `omk_saas.*` tables + JWT hook `e47f4aa1`. |
| **Orbiter ABC AaaS** | **Burnham** (LD06_Family H10 10-week cycle) | LD06_Family + LD05_Social + LD08_Impact (heritage baby-boomers) | GreenLantern People (LD05) + Aquaman Legal (LD05) + WonderWoman Finance (LD02 advisory) | Professor X (X-Men) + Ikaris (Eternals) + Bucky Barnes (Thunderbolts advisory) | H10 (10-week family cycle) | **OS Family Offices** = orienter l'héritage baby-boomers (transfert générationnel 2026-2045 ≈ centaines de trillions USD) vers Solarpunk / biomimétisme / Kardashev Type 1 résolu. Pivot Cloud Supabase `ABC-OS-COMMUNITY` (17 tables + 85 rows seeded). | 🟢 **ACTIF (récent)** — Schema `abc_os` migré 2026-06-17. `PGRST_DB_SCHEMAS` env var = P0 blocker en cours résolution. |
| **Family/Home AaaS** (4e variant dormant) | TBD (Jerry_4 = LD03-LD08 dormant) | LD03_Health + LD04_Cognition + LD05_Social + LD07_Creativity + LD08_Impact | TBD | TBD | TBD | TBD — réveil prévu Q4 2026 / Q1 2027 par décision canonique (cf. Plan `fancy-hugging-bengio.md` §3.4 Family/Home 4e variant dormant). | 🟡 **DORMANT** — Q3 2026 inactif, scope = LD03-LD08 hors LD01+LD02+LD06. |

### D3 — Les 8 Domaines Business × LD01 (matrice d'ancrage canonique)

LD01 = **`Business_Picard`** (H10 horizon, projects owner, MANIFEST.md obligatoire par projet). Cf. amendement `ADR-INFRA-003 §D1` (2026-06-21, sister scope à ce ADR).

Chaque projet AaaS ancre dans `30_Business_OS/10_Projects/<proj>/` (CEO Dashboard Matryoshka, `ADR-INFRA-003`) avec structure `_doctrine/` (junction deep Picard Verse) + 8 sous-dossiers alignés sur les 8 Domaines :

```
30_Business_OS/10_Projects/<proj>/          ← LD01 racine (Picard)
├── _doctrine/                               ← junction → 24_PARA_Enterprise/01_Projects_Picard/<NN>/ (deep canon)
├── _growth_runs/                            ← LD07 Superman Growth (Solaris AaaS dominant)
├── _sales_pipelines/                        ← LD06 JohnJones Sales (Nexus OMK AaaS dominant)
├── _product_specs/                          ← LD04 Flash Product (Solaris + Nexus AaaS dominant)
├── _ops_runbooks/                           ← LD05 Batman Ops (Orbiter ABC AaaS advisory)
├── _it_architecture/                        ← LD03 Cyborg IT (3 AaaS variants, infra souveraine partagée)
├── _finance_models/                         ← LD02 WonderWoman Finance (Saru ANCRE — Nexus OMK dominant, Solaris co-lead)
├── _people_culture/                         ← LD08+LD05 GreenLantern People (Orbiter ABC AaaS dominant)
└── _legal_compliance/                       ← LD05+LD08 Aquaman Legal (Orbiter ABC AaaS dominant)
```

### D4 — Les 4 Leviers Solarpunk (méthode canonique de production de valeur réelle)

**Cardinal** : les 3 AaaS variants appliquent **obligatoirement** les 4 leviers Solarpunk suivants à tout livrable. Un projet sans application explicite d'au moins 2 leviers Solarpunk n'est pas canoniquement « AaaS Solarpunk ».

#### Levier 1 — Biomimétisme (Janine Benyus)

- **Source canonique** : Janine Benyus, *Biomimicry: Innovation Inspired by Nature* (1997) + travaux plus récents Idriss Aberkane (biomimétisme économique).
- **Principe** : la nature est un immense laboratoire R&D ; chaque espèce = milliards de valeur économique non extraite (diatomées = silicium nanostructuré, peau de requin = hydrodynamique, etc.).
- **Application AaaS** : chaque feature d'un produit AaaS doit citer ≥ 1 modèle biologique canonique (espèce + mécanisme) + ≥ 1 transfer technique documenté.
- **Exemple canon** : Life-OS-2026 Ikigai engine = biomimétisme du corail (symbiose multi-organismes pour résilience écosystémique) → A3 Book (LD01) orchestre 5 A3 Ikigai pillars comme un récif corallien.
- **A3 twin ancre** : Book (LD01 H1) + Saru (LD02 H3) en co-lead.

#### Levier 2 — Low-High Tech (Idriss Aberkane)

- **Source canonique** : Idriss Aberkane, *Libérez votre cerveau !* (2016) + cycle de conférences Bordeaux 2016 sur le biomimétisme civilisationnel.
- **Principe** : low-tech + high-tech ne sont pas opposés mais complémentaires ; high-tech pour les problèmes high-stakes (santé, énergie), low-tech pour les problèmes low-stakes (autonomie locale, résilience).
- **Application AaaS** : chaque livrable AaaS doit équilibrer ≥ 30% low-tech (résilience, autonomie, sobriété) + ≥ 30% high-tech (scalabilité, performance). Pas de high-tech-only.
- **Exemple canon** : Solaris AaaS = high-tech (Life-OS-2026 Supabase Cloud + Vercel + Life Wheel dashboard) + low-tech (Notion AGENT_REGISTRY_DB = wiki markdown auto-hébergé, Memory Core local-first avant sync VPS).
- **A3 twin ancre** : Saru (LD02 H3 quarterly runway) — mesure frugalité tokens.

#### Levier 3 — Meta Science Acceleration

- **Source canonique** : concepts de "meta science" (accélération de la science par la science) + cycle Open Science / preprint servers / peer review ouvert.
- **Principe** : la science doit s'auto-accélérer en rendant ses méthodes ouvertes, vérifiables, et composables.
- **Application AaaS** : chaque décision AaaS (Go/No-Go pivot, allocation budget, choix techno) doit être **documentée** + **vérifiable** + **composable** (= un autre AaaS variant peut la réutiliser). Pas de boîte noire Musk-style (X algorithm closed source, Starlink routing proprietary).
- **Exemple canon** : ADR public (ce fichier `_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md` = open, vérifiable, composable) vs X algorithm = closed, opaque, non-vérifiable.
- **A3 twin ancre** : A3 Data (PARA Archives) — garant de l'append-only D4.

#### Levier 4 — Circular & Blue Economy

- **Source canonique** : Ellen MacArthur Foundation (circular economy) + Pauliuk et al. (industrial ecology) + blue economy (océans comme prochain front civilisationnel post-Type-1).
- **Principe** : tout output d'un système économique doit réintégrer un cycle (matière, énergie, information) — pas de déchet, pas d'extraction nette.
- **Application AaaS** : chaque livrable AaaS doit boucler ≥ 1 cycle (matière : recyclage / énergie : renouvelable / information : knowledge canonique append-only wiki).
- **Exemple canon** : Memory Core AaaS = circular info (wiki canonique croît, jamais delete, D4 append-only). Pas d'équivalent Musk (X = extract-only, algorithme propriétaire).
- **A3 twin ancre** : Burnham (LD06 H10 family cycle) + Stamets (LD05 H30 social mycelium).

### D5 — Anti-paperclip maximizer design (sister `ADR-SOBER-002`)

Les 3 AaaS variants sont **structurellement protégés** du paperclip maximizer Musk-style (cf. guide Geordi `08_People/2026-06-21_blast_musk_genie_ou_nazi_technofascisme_impact_civilisationnel.md` Note A3-05) par 7 mécanismes ancrés dans `ADR-SOBER-002` :

1. **Multi-objectif obligatoire** : chaque A3 twin a 8 critères de performance (8 Life Wheel), pas une métrique unique. Saru ne peut pas être évalué uniquement sur EBITDA.
2. **Veto distribué** : 6 A2 engines (Ikigai / Life Wheel / DEAL / 12WY / PARA / GTD) avec 6 frameworks distincts. Si l'un dérive, les 5 autres veto. **Pas de CEO unique Musk-like** dans AaaS.
3. **Hard veto A1 Rick** sur siphonage données / manipulation algo / destruction institutionnelle.
4. **AaaS 3 variants parallèles** : Solaris / Nexus / Orbiter se challengent mutuellement. Pas de single narrative dominant comme Musk-X.
5. **Audit trimestriel Georgiou** (LD08) : matrice 8×8 production de valeur vs impact humanitaire vs gouvernance vs souveraineté. Tout A3 twin qui dérive = red flag immédiat.
6. **Documentation publique** : ADR AaaS publics, auditables, contestables. Pas de brevet propriétaire Musk-style.
7. **Refus du chantage géopolitique** : multi-opérateurs orbitaux (Blue Origin / Arianespace / ESA / ISRO) — pas de Starlink-only.

### D6 — Gouvernance AaaS × A1 Gatekeepers (sister Plan `fancy-hugging-bengio.md` §3)

**A0 ne s'adresse JAMAIS directement aux AaaS variants**. A0 → A1 Gatekeepers (Beth Ikigai + Morty Focus) → A2 engines (6) → A3 twins → AaaS variants.

| Intention A0 | Routage canonique |
|---|---|
| « Cadrer Saru 1000T » | A1 Beth (Ikigai Lock) → A2 Discovery (Life Wheel) → A3 Saru (LD02 Finance H3) → **Solaris AaaS Book + Nexus OMK** |
| « Migrer OMK en Solarpunk » | A1 Beth (Ikigai Lock sur sens) + A1 Morty (Focus GTD) → A2 Enterprise (PARA) + A2 Cerritos (Holo Deck GTD) → A3 Spock (Areas LD02) + A3 Mariner (Capture) → **Nexus OMK AaaS** |
| « Orienter héritage baby-boomers vers biomimétisme » | A1 Beth (Ikigai Lock mission long terme) → A2 Protostar (DEAL Liberation) + A2 Discovery (Life Wheel) → A3 Burnham (LD06 Family H10) + A3 Dal (Define) → **Orbiter ABC AaaS** |
| « Stop drift Musk-style » | **A1 Rick (Sobriété Kernel, veto rare)** → hard-veto `ADR-SOBER-002` Anti-Paperclip |

### D7 — Métriques canoniques (D11 Fable-style + Saru H3 runway)

**Métriques obligatoires** par AaaS variant, mesurées trimestriellement par Georgiou (LD08) :

| Métrique | Source | Cible Q4 2026 |
|---|---|---|
| **Production de valeur réelle** ($M) | EBITDA ajusté + impact social monétisé (SROI) | ≥ +20% Q/Q |
| **Impact humanitaire net** (vies sauvées/améliorées) | SROI calculator + audit indépendant | ≥ +10% Q/Q |
| **Gouvernance démocratique** (score 0-100) | Georgiou 8×8 matrix + A1 Rick audit | ≥ 80/100 |
| **Souveraineté infrastructurelle** (# opérateurs concurrents) | Auto-audit A3 Bortus (LD02 H10) | ≥ 3 par catégorie critique |
| **Anti-paperclip compliance** (Y/N par 7 mécanismes D5) | Audit `ADR-SOBER-002` check-list | 7/7 ✓ |
| **4 Leviers Solarpunk appliqués** (Y/N par livrable) | Self-audit Book + Saru + Burnham | 4/4 ✓ par livrable majeur |

## Consequences

- ✅ **AaaS canoniquement ancré** dans un ADR L2 (gap doctrinal comblé, D7 cost-of-escalation prévenu).
- ✅ **3 variants × 4 leviers Solarpunk** = méthode reproductible, pas d'implicite à re-dériver.
- ✅ **Anti-paperclip** structurellement garanti par `ADR-SOBER-002` (sister scope, même session 2026-06-21).
- ✅ **LD01 Picard H10 + MANIFEST.md obligatoire** amendé dans `ADR-INFRA-003 §D1` (sister amendment).
- ✅ **Kardashev Type 3** ancré comme horizon canonique Saru 1000T (vs Musk Mars = 10⁰ personnes ≠ Kardashev).
- ⚠️ **Family/Home AaaS dormant Q3 2026** = scope partiel. Réveil Q4 2026 / Q1 2027 par décision canonique.
- ⚠️ **Métriques D7 Georgiou** non encore mesurées (Q3 2026 = setup, mesure effective Q4 2026).

## Anti-patterns prévenus

- ❌ **AaaS = boîte noire Musk-style** (X algorithm closed source) → ce ADR force la documentation publique.
- ❌ **Single-variant dominant** (Musk-X = un seul réseau social monopolistique) → 3 variants parallèles obligatoires.
- ❌ **Valorisation financiarisée découplée** (Musk IPO SpaceX = 12 zéros, 0 profit) → 4 leviers Solarpunk = production de valeur réelle obligatoire.
- ❌ **Paperclip maximizer** (USAID cuts = 14-22M morts anticipés pour +$1T Musk personnel) → 7 mécanismes anti-paperclip D5.
- ❌ **Capture institutionnelle** (Musk DOGE = siphonage données admin US) → hard-veto A1 Rick + refus de tout audit partisan.

## References

- `AGENTS.md` (L2 fractal A0-A3 doctrine, canon immuable).
- `MEMORY.md` §"Jerry 4 variants" (J01_Prime / J02_Bio / J03_Nexus / J04_Solarpunk canon).
- `Plan fancy-hugging-bengio.md` §3 Doctrine A1 Gatekeepers (A0=A0 Meta-OS, A1 Beth + Morty, 6 A2 engines, 35 A3 twins).
- `Plan fancy-hugging-bengio.md` §5 Pivot Life-OS-2026 (Solaris AaaS premier livrable canon).
- `_SPECS/ADR/L2_Business_OS/ADR-INFRA-003_business-os-ceo-dashboard-matryoshka.md` (CEO Dashboard structure, sister amendée 2026-06-21 §D1 LD01 Picard H10).
- `_SPECS/ADR/L2_Business_OS/ADR-CANON-001_roster-source-of-truth.md` (8 SOA × 8 B3 NanoSquads canon).
- `_SPECS/ADR/L2_Business_OS/ADR-AGENTIC-001_l2-agentic-commerce-nanosquad-coordination.md` (8 SOA01-SOA08 + 7 NanoSquads).
- `_SPECS/ADR/L2_Business_OS/ADR-OMK-004_pivot-supabase-cloud-vercel.md` (Cloud pivot 3-orgs Life OS / OMK / ABC).
- `_SPECS/ADR/L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md` (sister scope, anti-Musk 7 mécanismes D5).
- `_SPECS/ADR/L1_Life_OS/ADR-MEM-002_wiki-lifewheel-mapping-doctrine.md` (sister scope, Wiki 5-layer ↔ Life Wheel LD01-LD08).
- `_SPECS/ADR/L1_Life_OS/ADR-Meta-000_12-week-year-cycle-doctrine_DRAFT.md` (cycle 12WY Q3 2026 = 06/15 → 09/07, ancre les 12 items AaaS).
- `_SPECS/ADR/L1_Life_OS/ADR-META-005_hooks-automation.md` (4 hooks D1 receipts automation).
- `ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/08_People/2026-06-21_blast_musk_genie_ou_nazi_technofascisme_impact_civilisationnel.md` (anti-modèle Musk, Note A3-04 Kardashev vs Mars, Note A3-05 anti-paperclip design).
- `ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/04_Finance/` (LD02 Saru finance canon — TBD Saru Ancre canon guide à créer Q4 2026).
- `ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/09_Life_OS/LD02_Finance_Saru/` (8 numbered guides Saru canon).
- `wiki/concepts/concept_l2_fractal_b1b2b3.md` (B1/B2/B3 fractal canon).
- `wiki/comparisons/comparison_l2_roster_divergence.md` (Notion roster canon).
- `Fable 5 karpathy auto-research` (4 pillars: Penser dense, Livrable fini, Relecture, Vérité) — méthode 4-step loop Capture→Process→Persist→Loop appliquée aux AaaS.

---

## Annexe A — D1 receipts : AaaS variants status Q3 2026

| Variant | Production deploy SHA | Supabase org | Vercel project | Repo GitHub | A3 captain actif |
|---|---|---|---|---|---|
| **Solaris** (Life-OS-2026) | `b933e4e41849a323c63504e2ecea36b71c8759e5` | `hjweyhpmrxqsxfbibsnc` (Life OS) | `prj_wl1K4xU1YVmS8nsPSTmu88yywhgU` | `Amdkn/Life-OS-2026` | Book (LD01 H1) + Saru (LD02 H3) |
| **Nexus OMK** (OMK Services) | `8ad94d1` (post-merge sprint dcc1235) | OMK Tax Service Cloud | omk-services Vercel team | `omk-services/00-omk-saas-os` | Saru (LD02 H3) + Picard (LD01 H10) |
| **Orbiter ABC** (ABC-OS-Community) | (déploiement en cours, `PGRST_DB_SCHEMAS` blocker) | ABC-OS-COMMUNITY Cloud | abc-community-os Vercel | `ABC-OS-COMMUNITY/...` | Burnham (LD06 H10) + Picard (LD01 H10) |
| **Family/Home** (4e dormant) | ❌ pas de production deploy Q3 2026 | n/a | n/a | n/a | TBD Q4 2026 / Q1 2027 |

## Annexe B — D1 receipts : 4 Leviers Solarpunk canoniques

| Levier | Auteur canon | Application AaaS concrète | AaaS variant dominant |
|---|---|---|---|
| **Biomimétisme** | Janine Benyus (1997) + Idriss Aberkane (2016) | Life Wheel LDxx = modèle écosystémique corallien (symbiose multi-organismes). | Solaris (Book LD01 + Saru LD02) |
| **Low-High Tech** | Idriss Aberkane | Life-OS-2026 = high-tech Supabase+Vercel + low-tech Memory Core local-first. | 3 variants (équilibre obligatoire) |
| **Meta Science** | Open Science / Preprint servers | ADR publics, wiki canonique append-only, knowledge composable. | 3 variants (doctrine D4) |
| **Circular & Blue Economy** | Ellen MacArthur Foundation | Memory Core = circular info (jamais delete). Blue = océans post-Type-1 (Kardashev). | Orbiter ABC (Burnham LD06 family) |

## Annexe C — Mapping LD01 Picard vs Saru (ancre dual Solaris + Nexus)

LD01 = **Business_Picard** (H10 horizon, projects owner, MANIFEST.md obligatoire) — `ADR-INFRA-003 §D1` amendée 2026-06-21.

LD02 = **Finance_Saru** (H3 quarterly runway review, finance officer) — sister scope Life Wheel `22_Wheel_Discovery/LD02_Finance_Saru/`.

**Dualité Picard + Saru** = colonne vertébrale de Solaris + Nexus AaaS :
- **Picard** owns the **projects** (10_Projects/<proj>/ Matryoshka, MANIFEST.md).
- **Saru** owns the **finance** (runway quarterly, unit economics, production de valeur réelle vs valorisation).
- **Book** (LD01 H1, semaine) = hebdomadaire sub-cadence Picard.
- **Burnham** (LD06 H10, 10-week) = même cadence Picard mais scope family/heritage.

Les 3 variants AaaS sont donc tous **projet Picard** (10_Projects/<proj>/) avec **finance Saru** (LD02) en colonne vertébrale : Solaris (`30_Business_OS/10_Projects/solaris-aaas/`), Nexus (`30_Business_OS/10_Projects/omk-services/`), Orbiter (`30_Business_OS/10_Projects/abc-community-os/`).

## Annexe D — Open follow-ups

1. **Family/Home AaaS canonisation** : au réveil Q4 2026 / Q1 2027, créer `ADR-L2-AAAS-002_family-home-aaas-doctrine.md` avec mapping LD03-LD08 + 4 Leviers Solarpunk spécifiques (acupuncture urbaine pour LD03 Health, low-high tech pour LD04 Cognition, etc.).
2. **Saru Ancre canon guide Geordi** : créer `04_Finance/2026-Q4-saru-1000t-kardashev-type3-canon.md` (Standard Antigravity Premium, 6-16K chars) avec 8 sections : Concepts (Kardashev / Solarpunk / Low-High Tech / Biomimétisme / etc.), Matrice d'outillage (Supabase + Vercel + Notion + Memory Core), Perspective Souveraine A'Space Saru, DEAL Liberation protocol, Annexes A3-01 à A3-05 (deep-dives Saru-specific).
3. **Georgiou audit template** : créer `wiki/templates/geordi_aaas_audit_quarterly.md` (matrice 8×8 production de valeur / démocratie / solidarité / santé / éducation / biodiversité / souveraineté / long-termisme × 8 AaaS criteria).
4. **A1 Rick formalisation Anti-Paperclip check** : créer un script `.mcp.json` check-list 7 mécanismes D5 exécuté automatiquement à chaque commit `omk-services/00-omk-saas-os` ou `Amdkn/Life-OS-2026`.

## Signatures

- **Draft author** : A1 Beth (Gatekeeper Ikigai) — Vague 2 Mission 1 deliverable, 2026-06-21.
- **Recorder** : A3 Data (Second Officer & Ops Officer, USS Enterprise) — canonisation wiki canonique append-only.
- **Ratification pending** : A0 Amadeus (Jumeau Numérique) — sign-off attendu post-Plan `fancy-hugging-bengio.md` §3 ratification.
- **Hash d'intention** : `adr_l2_aaas_001_proposed_2026-06-21_3variants_4levers_anti_musk`
