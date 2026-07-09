---
id: ADR-NEXUS-LANDING-PERSONAS-001
title: OMK Nexus — 3 Landing Pages Distinctes par Persona ICP (Marcus / Harrison / David)
status: DRAFT
date: 2026-07-06
last_updated: 2026-07-06 (Claude Code B1 E-Myth Gatekeeper — distilled from PRD-NEXUS-EVOLUTION-IA-001 v1, screened against ADR-SOBER-002 + sister canon)
deciders: [A0 Amadeus]
proposed_by: Claude Code (B1 E-Myth Gatekeeper, on A0 directive "rédige l'ADR canonique 3 landings ICP personas")
domain: L2 Business OS / OMK Nexus / AaaS Doctrine / Landing ICP / Persona Variant
tags: [#ADR #nexus #landing-page #personas #icp #strate-a #strate-b #strate-c #marcus #harrison #david #anti-paperclip #anti-template #aesthetic #single-file #perf-budget #aaas]
related: [PRD-NEXUS-EVOLUTION-IA-001, ADR-ICP-NEXUS-001, ADR-AAAS-PRICING-001, ADR-MARKET-STUDY-001, ADR-L2-AAAS-001, ADR-SOBER-002, ADR-OMK-NEXUS-TRANSFORM-001, ADR-NEXUS-NICHE-001, plan-L2-business-os.md]
supersedes: none
sources_canons: [
  "PRD-NEXUS-EVOLUTION-IA-001_offre-2026-landing-icp.md (PRD canon du pivot doctrinal — 5 modules / 3 strates A-B-C / 5 personas / 6 candidates / 3 prioritaires)",
  "PRD-NEXUS-EVOLUTION-IA-001 §1 — pivot doctrinal : 'L'IA locale sans GPU = différée 2027' (gravé par A+)",
  "PRD-NEXUS-EVOLUTION-IA-001 §2 — Pack 5 modules : Audit Sdiri / Wargame Fable / CEO-Bench / MiroFish / Gstack",
  "PRD-NEXUS-EVOLUTION-IA-001 §3 — 10 ICPs / 3 strates (A coaching exécutif · B growth prospection focus prioritaire A+ · C conseil opérationnel)",
  "PRD-NEXUS-EVOLUTION-IA-001 §4 — Tableau 5 personas détaillés (Marcus Strate A · Harrison / Clara / Amara / Christian Strate B · David Strate C)",
  "PRD-NEXUS-EVOLUTION-IA-001 §5 — Frameworks marketing retenus (STP · AAARR Signal-First · Jevons Arbitrage repositionné · Boucle Medvi assainie · E-Myth Functional Architecture)",
  "PRD-NEXUS-EVOLUTION-IA-001 §6 — Rails existants (zéro re-derivation) : omk-nexus-landing-page.vercel.app (FR) · omk-nexus-landing-en.vercel.app (EN)",
  "PRD-NEXUS-EVOLUTION-IA-001 §7 — Confusions Gemini filtrées D4 (BETH_VETO_DISSOLVED faux · local-first 0,01$ pitch 2026 corrigé par A+ · Jstack→Gstack · arborescence inventée · state.json décoratifs · chiffres non sourcés)",
  "ADR-ICP-NEXUS-001 RATIFIED 2026-06-24 — 5 piliers canon ICP Nexus (Persona Expert méthodique · Mantra 'L'illusion de la complexité' · Marché Conformité · 3-ICP · Killer Feature Zero-PII Agentic Governance)",
  "ADR-AAAS-PRICING-001 RATIFIED+AMENDED 2026-06-24 — 5 Tiers AaaS USD post-accuponcture",
  "ADR-MARKET-STUDY-001 RATIFIED 2026-06-24 — Étude TAM 136,1 Mds$ 'The Builders' 2026",
  "ADR-L2-AAAS-001 RATIFIED 2026-06-21 — 3 Variants Solarpunk (Solaris 🎨 Visual · Nexus ⚖️ Data · Orbiter 🏗️ Mobile)",
  "ADR-SOBER-002 RATIFIED — Anti-Paperclip doctrine : pas de promises 2027, pas de chiffres non sourcés, pas de features inventées",
  "plan-L2-business-os.md §13 — Pricing $1000/mois gated ×100 clients (forfait Enterprise OS wargamé)",
  "wargame 05-legal-dlp (12/12 blueprint) — module DLP redact.py, backlog WF1 §2c PRIORITÉ 1",
  "wargame 06-growth-aaarr (12/12 blueprint) — séquences AAARR Signal-First, backlog WF1 §2c",
  "wargame 07-sales-quiz (12/12 blueprint) — quiz simulateur d'inférence, backlog WF1 §2c",
  "wargame 09-gstack (12/12 blueprint) — orchestration Gstack W× clients",
  "MEMORY.md §'Nexus EN landing DEPLOYED 2026-06-29' — base canon : single-file index.html 628 KB · EN ratio 96.8% · dark theme #0A0E16 + #C8A55C"
]
provenance: Née 2026-07-06 d'une directive A0 B1 E-Myth Gatekeeper ('Rédige l'ADR canonique ADR-NEXUS-LANDING-PERSONAS-001 pour OMK Nexus, 3 landing pages ICP par persona'). PRD-NEXUS-EVOLUTION-IA-001 v1 (canon) lu en D1 — 5 modules / 3 strates / 5 personas / 6 candidates / 3 prioritaires. Sister canon ADR-ICP-NEXUS-001 + ADR-AAAS-PRICING-001 + ADR-MARKET-STUDY-001 + ADR-L2-AAAS-001 + ADR-SOBER-002 + MEMORY.md §'Nexus EN landing DEPLOYED'. Statut DRAFT — ratification A0 attendue post-relecture canon.
---

# ADR-NEXUS-LANDING-PERSONAS-001 — OMK Nexus, 3 Landing Pages Distinctes par Persona ICP

## 1. Status

**DRAFT** — 2026-07-06. Produit par Claude Code B1 E-Myth Gatekeeper, sur directive A0 Amadeus. Sister canon de [`ADR-ICP-NEXUS-001`](./ADR-ICP-NEXUS-001_icp-nexus-structuration.md) (RATIFIED 2026-06-24 — 5 piliers canon ICP), [`ADR-AAAS-PRICING-001`](./ADR-AAAS-PRICING-001_aaas-pricing-canon.md) (RATIFIED + AMENDED 2026-06-24 — 5 Tiers AaaS), [`ADR-MARKET-STUDY-001`](./ADR-MARKET-STUDY-001_the-builders-2026.md) (RATIFIED 2026-06-24 — TAM 136,1 Mds$), [`ADR-L2-AAAS-001`](./ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md) (RATIFIED 2026-06-21 — 3 Variants Solarpunk). Ancré sur PRD [`PRD-NEXUS-EVOLUTION-IA-001`](../../PRD/PRD-NEXUS-EVOLUTION-IA-001_offre-2026-landing-icp.md) (canon 2026-07-06).

## 2. Context

### 2.1. D6 racine — aucun ADR canon pour les 3 landings personas

Avant ce ADR, **AUCUNE décision canon formalisée** sur les 3 landings distinctes par persona. La D6 grep confirme :

| Source canon | Status pré-ADR |
|---|---|
| `_SPECS/ADR/L2_Business_OS/ADR-NEXUS-*` | `ADR-NEXUS-NICHE-001_coaching-bizdev-b2b-arbitrage.md` (niche coaching) + `ADR-OMK-NEXUS-TRANSFORM-001_omk-to-nexus-pivot.md` (pivot omk→nexus) — **PAS** d'ADR sur 3 landings distinctes |
| PRD canon pivot | PRD-NEXUS-EVOLUTION-IA-001 v1 (2026-07-06) — 5 personas détaillés, 3 prioritaires |
| Rails deployés | `omk-nexus-landing-page.vercel.app` (FR) + `omk-nexus-landing-en.vercel.app` (EN) — LIVE (canon MEMORY.md §'Nexus EN landing DEPLOYED 2026-06-29') |

### 2.2. Le pivot doctrinal gravé (PRD §1)

**Le PRD §1 pose le pivot gravé par A+** :

> « L'IA locale sans GPU = **différée 2027** (DSpark, Recursivemas, finetuning du Canon A'Space pour rendre l'organigramme et les workflows natifs aux LLM). Aligné avec le Dark L0 déjà différé (wargame 10-localai-minimax). »

**Conséquence canon** : l'offre 2026 d'OMK Nexus n'est **PAS** l'infrastructure locale. C'est **l'Évolution IA des Entreprises** — le client achète le **contrôle chirurgical de ses processus** par le **Loop Engineering**, vendu en **prototype de franchise par conception** (PRD §1).

### 2.3. Le pack 5 modules (PRD §2 — le cœur du produit)

PRD §2 liste le **pack 5 modules** (= ce que le client reçoit, mapping → moteur interne) :

| # | Module | Moteur interne (canon) |
|---|---|---|
| 1 | **Audit de Processus** (méthode Sdiri) | Quiz Sdiri + modèles économiques |
| 2 | **Wargame Fable de ses Workflows** | Testament Fable (12 wargames maison) |
| 3 | **CEO-Bench — Détection d'Angles Morts** | A3 Book, WF2 |
| 4 | **MiroFish — Simulations de Swarm Prédictives** | Picard + MiroFish, WF3 |
| 5 | **Gstack — Lighting d'Orchestration Autonome** | B1 Jerry (Systemize) + Summers (Ship), `/office-hours` |

### 2.4. 3 strates A / B / C — focus prioritaire B (PRD §3)

PRD §3 fige 3 strates d'ICPs :

- **Strate A — Coaching Exécutif & Alignement** : cabinets C-Suite, leadership development grand volume, coachs M&A/transition.
- **Strate B — Croissance & Prospection** *(focus prioritaire A+)* : agences SDR/BDR as a Service, growth marketing B2B native-IA, sales enablement/performance commerciale.
- **Strate C — Conseil Opérationnel & Systématisation** : fractional COOs, SOP vaulting/standardisation, gestion de patrimoine B2B, conduite du changement (canal partenaire).

### 2.5. 5 personas détaillés (PRD §4) — 3 prioritaires

PRD §4 détaille 5 personas et en désigne **3 prioritaires** :

| Persona (priorité) | Strate | Friction canon (PRD §4) | Angle landing canon (PRD §4) |
|---|---|---|---|
| **Marcus Vance** — Managing Partner, coaching C-Suite ★ prioritaire | A | 12h/sem de comptes-rendus manuels + panique conformité (EU AI Act, fuite PII vers cloud grand public) | « Le Chef de Cabinet IA » : audit + wargame de ses process de synthèse, DLP (module wargame 05) — **sans promettre le local-first 2027** |
| **Harrison Vance / Clara Sterling** — CEO agence BDR ★ prioritaire | B | Paradoxe de Jevons : 45k tokens/prospect, facture API 1.5k→9k$/mois, marge 75%→42% | « L'Arbitrage Jevons » : plan fixe + orchestration Gstack de ses boucles outbound + quiz simulateur d'inférence (wargame 07) |
| **Amara Sow** — fondatrice growth native-IA | B | 20h/sem à gérer l'étanchéité multi-clients, confiance clients | « Le Harnais Multi-Tenant » : audit + wargame de son architecture d'étanchéité, RLS |
| **Christian Vance** — sales enablement | B | Millières d'heures de transcriptions à noter, hallucinations de scoring, NDA | « L'Évaluateur Stage-Aware » : wargame du pipeline de scoring + CEO-Bench sur ses playbooks |
| **David Kross** — fractional COO ×15 PME ★ prioritaire | C | SOPs statiques jamais appliqués, onboarding client = conduite du changement manuelle | « SOPs → Skills exécutables » : ses playbooks convertis en skills agentiques + W× par client |

> **D1 receipt** : PRD §4 verbatim — confidence **HIGH** (citation directe, pas d'invention). 6 candidates au total (Amara, Christian sont les 2 non-prioritaires listées). Le persona interne « *Le forfait $1000 lui-même* » (PRD §4 ligne 6) **n'est PAS une landing** — c'est un garde-fou de wargame 09 M4 cas 4.

## 3. Décision : 3 Landings Distinctes (Marcus / Harrison / David)

### 3.1. Périmètre — exactement 3 landings

**Décision gravée** : on construit **exactement 3 landings distinctes**, une par persona prioritaire :

| # | Landing | Persona | Strate | Angle landing canon (PRD §4) | Sous-domaine Nexus |
|---|---|---|---|---|---|
| L1 | `omk-nexus-marcus.vercel.app` (à valider slug final) | Marcus Vance | A — Coaching Exécutif | « Le Chef de Cabinet IA » | Conformité · DLP · Synthèse exec |
| L2 | `omk-nexus-harrison.vercel.app` (à valider slug final) | Harrison Vance / Clara Sterling | B — Croissance & Prospection (focus prioritaire A+) | « L'Arbitrage Jevons » | Plan fixe vs API variable · Gstack outbound · Quiz simulateur |
| L3 | `omk-nexus-david.vercel.app` (à valider slug final) | David Kross | C — Conseil Opérationnel | « SOPs → Skills exécutables » | Conduite du changement · Skills agentiques · W× multi-PME |

> **D3 nuance critique** : on **ne construit pas** de landing pour Amara ou Christian à ce stade. Le PRD §4 les désigne comme **non-prioritaires**. Le backlog WF1 §2c + 4 sims `/office-hours` (wargame 09 M4) valideront s'ils deviennent des landings plus tard — gated outboard 3 cycles verts.

### 3.2. Stack technique — single-file, zero nouveau chantier

**Décision** : **HTML/CSS/JS pur, single-file** (pas de framework, pas de bundler, pas de CMS). Sisters de la landing EN déployée (canon MEMORY.md §'Nexus EN landing DEPLOYED 2026-07-04') :

| Caractéristique | Spec canon | Source |
|---|---|---|
| Format | single-file `index.html` | MEMORY.md §'Nexus EN landing DEPLOYED' (628 KB) |
| Build step | aucun | idem |
| Framework | aucun (vanilla) | idem |
| Assets externes | zéro CDN tiers (sauf fonts si justifié) | doctrine locale-first |
| Déploiement | Vercel team `amd-lab` (canon EN) | MEMORY.md §'Nexus EN landing' |
| Repo | un repo par landing (mirror transfer AMD → omk-services, canon sister EN) | canon EN sister |
| Tailwind / shadcn / DaisyUI | **INTERDITS** (anti-template) | `ecc/web/design-quality.md` Anti-Template Policy |
| Banned patterns | gradient purple-on-white, card grid uniforme, hero stock centered, gray-on-white safe | idem |

> **D6 vérité racine** : on **ne crée aucun chantier neuf**. PRD §6 verbatim : « **ce PRD ne crée aucun chantier neuf. Il donne le CAP business aux rails déjà wargamés** — c'est le backlog WF1 §2c qui les exécute en loop ».

### 3.3. Aesthetic différenciée par persona (anti-template stricte)

**Doctrine appliquée** : `ecc/web/design-quality.md` — **Required Qualities** (au moins 4 sur 10 par landing) + **Anti-Template Policy** (banned patterns list). Chaque landing a une **direction esthétique UNIQUE** (pas de cookie-cutter layout). Palette sister FR/EN canon : dark `#0A0E16` + gold `#C8A55C` (canon EN), MAIS **différenciée par persona** :

#### L1 — Marcus Vance (C-Suite Coach) : **Light Editorial Gravitas**

| Token | Valeur | Justification |
|---|---|---|
| Surface principale | `#F5F0E1` (parchemin / ivoire chaud) | Editorial magazine, gravitas C-Suite |
| Texte principal | `#1A1A1A` (noir encre) | Contraste AA garanti |
| Accent | `#7A1F1F` (oxblood / bordeaux) | Prestige coach senior, bordereaux signés |
| Accent secondaire | `#8B7E5A` (brass mat) | Métaphore cabinet de lecture |
| Typographie display | Serif transitional (canon sister Solaris coach-pool) | Héritage conseil |
| Direction visuelle | **Editorial / magazine** — colonnes étroites, lettrines, marges généreuses, citations en exergue | `ecc/web/design-quality.md` Worthwhile Style Directions |
| Required Qualities activées (≥4/10) | (1) hierarchy through scale contrast, (2) intentional rhythm, (3) typography pairing (serif+sans), (5) color semantically, (8) texture/parchment, (9) motion that clarifies flow | idem |
| Anti-template | Aucun gradient purple-on-white · pas de card-grid uniforme · pas de safe gray-on-white | idem |

#### L2 — Harrison / Clara (CEO agence BDR) : **Dark Ops Console**

| Token | Valeur | Justification |
|---|---|---|
| Surface principale | `#0A0E16` (dark navy profond — sister canon EN/FR) | Operations center, vision nocturne |
| Texte principal | `#F5F5F4` (stone-100) | AA garanti sur `#0A0E16` |
| Accent principal | `#3B82F6` (electric blue) | Performance, telemetry, dashboards BDR |
| Accent secondaire | `#10B981` (emerald) | Métaphore outbound vert (réponse positive) |
| Stat warning | `#EF4444` (rouge signal) | Marge en chute, Jevons alerte |
| Typographie display | Sans-serif géométrique condensé (sister Solaris sister FR/EN canon) | Métrique BDR, dashboards |
| Direction visuelle | **Dark luxury + glassmorphism with real depth** — surfaces superposées, télémétrie live, compteurs de marge animés, gauges outbound | `ecc/web/design-quality.md` |
| Required Qualities activées (≥4/10) | (3) depth/layering via overlap, (4) typography character, (6) hover/focus/active designed, (7) grid-breaking composition, (10) data viz part of design system | idem |
| Anti-template | Pas de stock hero centered · pas de cookie-cutter dashboard sidebar+cards+charts | idem |

#### L3 — David Kross (fractional COO) : **Warm Industrial**

| Token | Valeur | Justification |
|---|---|---|
| Surface principale | `#1C1917` (stone-900, charbon chaleureux) | Atelier cabinet, sobre |
| Texte principal | `#FAFAF9` (stone-50) | AA garanti sur `#1C1917` |
| Accent principal | `#A8A29E` (stone-400, ash mat) | Métaphore opérationnelle, papier kraft |
| Accent secondaire | `#D97706` (amber, SOP highlight) | Marquage SOP, surligneur |
| Stat critique | `#B91C1C` (deep red) | Goulot opérationnel détecté |
| Typographie display | Sans-serif humaniste (Inter / équivalent) | Lisible, opérationnel |
| Direction visuelle | **Swiss / International** — grille rigoureuse, numérotation visible, listes hiérarchiques, schémas SOP | `ecc/web/design-quality.md` |
| Required Qualities activées (≥4/10) | (1) hierarchy, (2) intentional rhythm, (5) color semantically, (7) bento composition, (9) motion that clarifies flow | idem |
| Anti-template | Pas de flat layout, pas d'uniform radius/spacing | idem |

> **D3 nuance design** : les 3 palettes sont **intentionnellement distinctes** — un visiteur qui voit deux landings côte à côte doit reconnaître immédiatement que ce sont 3 produits différents ciblant 3 personas différents. **Pas** de palette commune « Nexus brand » = pas de cohérence Nexus = mais c'est le **but** (PRD §5 positionnement : « l'Enterprise OS wargamé vs les SaaS wrappers vibe-codés éphémères » — chaque persona doit voir SON outil, pas un template brandé).

### 3.4. Composants partagés (extraits canoniques)

| Composant | Source canon | Description |
|---|---|---|
| Header / Hero | sister `omk-nexus-landing-page.vercel.app` FR (canon LIVE) | Hero persona-spécifique + angle landing PRD §4 verbatim |
| Quiz simulateur d'inférence | **wargame 07-sales-quiz** (12/12 blueprint blind, backlog WF1 §2c) | embed sur L2 Harrison, stub iframe sur L1/L3 |
| DLP module link | **wargame 05-legal-dlp** (12/12, backlog WF1 §2c PRIORITÉ 1) | lien externe (à exécuter) sur L1 Marcus |
| AAARR Signal-First hook | **wargame 06-growth-aaarr** (12/12, backlog WF1 §2c) | CTA capture email / LinkedIn ultra-court sur L2 |
| MiroFish teaser | **wargame 08-picard-mirofish** (12/12, gated L1+L2 GREEN) | stub visuel sur L3 (simulation SOPs/skills) |
| Pricing display | **ADR-AAAS-PRICING-001** RATIFIED 2026-06-24 (5 Tiers USD post-accuponcture) | tier canon « Enterprise OS wargamé » $1000/mois gated ×100 (plan-L2 §13) |
| Footer | sister canon EN (MEMORY.md §'Nexus EN landing') | multi-langue FR/EN, liens légaux AI-Act 2026-08-02 |

> **D1 receipt composants** : tous les rails existent (canon MEMORY.md ou wargames blueprintés 12/12). **Aucun composant inventé**. Quand un rail n'est pas encore exécuté (ex. quiz simulateur), on embed un **stub iframe ou un placeholder honnête** « disponible W3 » — pas de fausse feature visible (ADR-SOBER-002).

## 4. Doctrine : Anti-Paperclip + Sister-canon

### 4.1. Application stricte ADR-SOBER-002 (Anti-Paperclip)

**D4 verrouillage** — les claims suivants sont **INTERDITS** sur les 3 landings (PRD §7 verbatim « **confusions Gemini filtrées D4** ») :

| ❌ Claim interdit | Raison canon |
|---|---|
| « IA locale chez le client en 2026 » | PRD §1 gravé : local-first différé 2027 |
| « Inférence à 0,01$ par appel » | PRD §1+§5 : argument Jevons repositionné = coût fixe vs API variable, pas 0,01$ |
| « 47% de conversion » | PRD §7.6 : chiffres non sourcés, jamais republier sans D1 verify |
| « 700+ signaux capturés » | idem |
| « ×1000 leads générés » | idem |
| « Bootstrapped vibe-coded SaaS wrapper, livré en 2 semaines » | PRD §5 positionnement inverse : vs SaaS wrappers vibe-codés éphémères |
| « BETH_VETO_DISSOLVED » | PRD §7.1 : faux — Beth = seul veto (WARMODE-002) |
| « Jstack Front-End Terminal » | PRD §7.3 : faux — référent réel = **Gstack** (garrytan/gstack) |
| Arborescence « 10_MÉTA_OS_Y_COMBINATOR / 00_Jerry_Business_Pulse » | PRD §7.4 : inventée — vraie racine = `ASpace_OS_V2/` (00_Amadeus / 10_Tech_OS / 20_Life_OS / 30_Business_OS / _SPECS) |
| `state.json` décoratifs (« MUSE_EXTRAPOLATION_READY »…) | PRD §7.5 : télémétrie narrative, aucun fichier réel — vrais bus d'état = `citadel/data/*.json` + worklog |

**Règle de validation pré-publication** : chaque landing passe un **red-team A0 desk-check** (ou sim `/office-hours` wargame 09 M4 adversariale) qui tente de prouver qu'une claim est inventée. Si une claim ne survit pas, on la retire.

### 4.2. Sister-canon référencé

| ADR sister | Statut | Application aux 3 landings |
|---|---|---|
| [`ADR-ICP-NEXUS-001`](./ADR-ICP-NEXUS-001_icp-nexus-structuration.md) | RATIFIED 2026-06-24 | Persona archétype « Expert méthodique » + mantra « L'illusion de la complexité » + marché Conformité → chaque landing adresse un sous-archétype du même archétype |
| [`ADR-AAAS-PRICING-001`](./ADR-AAAS-PRICING-001_aaas-pricing-canon.md) | RATIFIED + AMENDED 2026-06-24 | Affichage du tier canon « Enterprise OS wargamé » $1000/mois gated ×100 (plan-L2 §13) |
| [`ADR-MARKET-STUDY-001`](./ADR-MARKET-STUDY-001_the-builders-2026.md) | RATIFIED 2026-06-24 | TAM 136,1 Mds$ si/et seulement si on cite l'étude, citation exacte + source canon |
| [`ADR-L2-AAAS-001`](./ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md) | RATIFIED 2026-06-21 | Sister Nexus ⚖️ Data First / Conformité — pas de drift Solaris 🎨 ou Orbiter 🏗️ |
| [`ADR-SOBER-002`](./../../L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md) | RATIFIED | Anti-Paperclip — claims non sourcés interdits, 2027 promises interdites |

### 4.3. Positionnement canon (PRD §5 — Frameworks marketing retenus)

5 frameworks retenus (verbatim PRD §5) :

1. **STP** : segmentation par intensité tokens × risque conformité → ciblage concentré segments 2/3/4 (high-ticket 3-15k$/mois) → positionnement **l'Enterprise OS wargamé** vs les SaaS wrappers vibe-codés éphémères.
2. **AAARR Signal-First** (= wargame 06) : 3 signaux d'interception Alpha/Bêta/Gamma → séquences email/LinkedIn ultra-courtes → hook = **quiz simulateur** (= wargame 07).
3. **Jevons Arbitrage** (repositionné) : **plus** « inférence locale à 0,01$ » (2027) — c'est **coût fixe d'orchestration vs compteur API variable**.
4. **Boucle Medvi assainie** : Quiz → preuve ROI → forfait signé → affiliation 20% récurrente (Stripe Connect).
5. **E-Myth Functional Architecture** : vendre le travail ON the business (franchise par conception), pas IN.

> **D1 receipt frameworks** : PRD §5 — les 5 frameworks sont appliqués **différemment par landing** selon le persona, mais la matrice (segment / signal / hook / boucle / posture) reste canon.

## 5. Architecture & Performance Budgets

### 5.1. Performance budgets (D7 cost-of-escalation)

Chaque landing doit rester sous les budgets suivants (sister `ecc/web/performance.md`) :

| Métrique | Budget | Source |
|---|---|---|
| JS bundle (gzip) | **< 150 KB** (page type landing) | `ecc/web/performance.md` |
| CSS (gzip) | **< 30 KB** | idem |
| LCP | **< 2.5 s** | Core Web Vitals cible |
| INP | **< 200 ms** | idem |
| CLS | **< 0.1** | idem |
| FCP | **< 1.5 s** | idem |
| TBT | **< 200 ms** | idem |
| Total single-file size | **< 800 KB** non-gzip (sister EN canon 628 KB) | canon MEMORY.md §'Nexus EN landing' |
| Accessibilité | **WCAG 2.2 AA** minimum | `ecc/web/testing.md` |

### 5.2. Sécurité & headers (sister `ecc/web/security.md`)

| Header / Config | Valeur | Source |
|---|---|---|
| `Content-Security-Policy` | nonce-based script-src, default-src 'self', frame-src 'none', object-src 'none' | `ecc/web/security.md` |
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains; preload` | idem |
| `X-Content-Type-Options` | `nosniff` | idem |
| `X-Frame-Options` | `DENY` | idem |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | idem |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=()` | idem |
| HTTPS | obligatoire (canon Vercel) | canon sister EN |
| Form | CSRF protection state-changing + rate limiting | `ecc/web/security.md` |

### 5.3. i18n

- **L1 Marcus** : FR par défaut, EN sister (canon sister FR/EN) — **mais** Marcus étant C-Suite francophone probable, FR-first.
- **L2 Harrison** : EN-first (Harrison Vance / Clara Sterling, agence BDR, marché US probable) + FR sister.
- **L3 David** : FR-first (fractional COO ×15 PME, marché francophone) + EN sister.

> **D3 nuance** : on **n'aligne pas** les langues par landing. Chaque landing a sa propre langue-first selon le persona (pas le PRD §6 qui impose FR+EN socle unique). Sister canon : 2 landings déjà déployées `omk-nexus-landing-page.vercel.app` (FR) + `omk-nexus-landing-en.vercel.app` (EN) — on **réutilise ce pattern bilingue asymétrique**.

### 5.4. Stockage & déploiement

- **3 repos séparés** dans l'org `omk-services` (mirror transfer AMD → omk-services, canon sister EN MEMORY.md §'Nexus EN landing DEPLOYED').
- **3 projets Vercel** dans la team `amd-lab` (canon sister EN).
- **Domaines custom** (optionnel, post-validation interne) : pas avant validation par 4 sims `/office-hours` wargame 09 M4 (gated outboard 3 cycles verts — PRD §6 verbatim).

## 6. Verification — D1 Receipts

### 6.1. URLs & paths absolus (D1 file-system receipts)

| Élément | Path / URL | Status |
|---|---|---|
| PRD source | `C:\Users\amado\ASpace_OS_V2\_SPECS\PRD\PRD-NEXUS-EVOLUTION-IA-001_offre-2026-landing-icp.md` | EXISTS (lu ce tour, 78 lignes, D1) |
| Sister FR live | `https://omk-nexus-landing-page.vercel.app` | LIVE (canon MEMORY.md) |
| Sister EN live | `https://omk-nexus-landing-en.vercel.app` | LIVE (canon MEMORY.md §'Nexus EN landing DEPLOYED 2026-06-29') |
| Sister EN repo | `https://github.com/Amdkn/00-omk-nexus-landing-en` | LIVE (canon MEMORY.md) |
| ADR canon (cible) | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-NEXUS-LANDING-PERSONAS-001_3-landings-distinctes-icp.md` | DRAFT (ce fichier, créé ce tour) |
| Sister ICP canon | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-ICP-NEXUS-001_icp-nexus-structuration.md` | EXISTS (RATIFIED 2026-06-24) |
| Sister Pricing canon | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-AAAS-PRICING-001_aaas-pricing-canon.md` | EXISTS (RATIFIED + AMENDED 2026-06-24) |
| Sister Market canon | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-MARKET-STUDY-001_the-builders-2026.md` | EXISTS (RATIFIED 2026-06-24) |
| Sister L2-AAAS canon | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md` | EXISTS (RATIFIED 2026-06-21) |
| ADR-SOBER-002 | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L0_Kernel_OS\ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md` | EXISTS (RATIFIED) |
| Plan L2 | `C:\Users\amado\ASpace_OS_V2\_SPECS\plan-L2-business-os.md` §13 | EXISTS (pricing $1000×100 gated) |
| Wargame 05 | canon 12/12 blueprint blind (backlog WF1 §2c PRIORITÉ 1) | EXISTS blueprint |
| Wargame 06 | canon 12/12 (backlog WF1 §2c) | EXISTS blueprint |
| Wargame 07 | canon 12/12 (backlog WF1 §2c) | EXISTS blueprint |
| Wargame 09 | canon 12/12 (4 sims M4 personas) | EXISTS blueprint |
| ECC rules anti-template | `C:\Users\amado\.claude\rules\ecc\web\design-quality.md` | EXISTS |
| ECC rules web perf | `C:\Users\amado\.claude\rules\ecc\web\performance.md` | EXISTS |
| ECC rules web security | `C:\Users\amado\.claude\rules\ecc\web\security.md` | EXISTS |
| ECC rules web testing | `C:\Users\amado\.claude\rules\ecc\web\testing.md` | EXISTS |

### 6.2. D1-vs-invention checklist (Anti-Paperclip)

| Item | Source canon | Status D1 |
|---|---|---|
| 5 modules (Audit/Wargame/CEO-Bench/MiroFish/Gstack) | PRD §2 | ✅ D1 verbatim |
| 3 strates A/B/C | PRD §3 | ✅ D1 verbatim |
| 5 personas détaillés | PRD §4 | ✅ D1 verbatim |
| 3 personas prioritaires (Marcus/Harrison/David) | PRD §4 ★ prioritaire | ✅ D1 verbatim |
| Frictions par persona | PRD §4 col 3 | ✅ D1 verbatim |
| Angles landing par persona | PRD §4 col 4 | ✅ D1 verbatim |
| 5 frameworks marketing | PRD §5 | ✅ D1 verbatim |
| Pricing $1000/mois gated ×100 | plan-L2 §13 (referenced by PRD §2) | ✅ D1 canon |
| Rails existants (FR/EN Vercel) | PRD §6 + MEMORY.md | ✅ D1 canon |
| Anti-Paperclip (no 2027, no chiffres inventés) | PRD §7 + ADR-SOBER-002 | ✅ D1 canon |
| Sister ADRs RATIFIED | ADR-ICP-NEXUS-001 + ADR-AAAS-PRICING-001 + ADR-MARKET-STUDY-001 + ADR-L2-AAAS-001 | ✅ D1 canon |
| Palette dark `#0A0E16` + gold `#C8A55C` | MEMORY.md §'Nexus EN landing' | ✅ D1 canon (sister) |
| **Palettes Marcus/Harrison/David différenciées** | **ce ADR §3.3** (création D1 par dérivation cohérente) | ✅ D1 dérivation sœur |
| **Single-file vanilla HTML/CSS/JS** | **ce ADR §3.2** (alignement sister EN canon) | ✅ D1 dérivation sœur |
| **Perf budgets 150KB JS / 30KB CSS** | `ecc/web/performance.md` | ✅ D1 canon |
| **Accessibilité WCAG 2.2 AA** | `ecc/web/testing.md` | ✅ D1 canon |
| **CSP nonce-based, HSTS preload, etc.** | `ecc/web/security.md` | ✅ D1 canon |

### 6.3. Posture C — artefact-first, 0 cron until A0 per-cron GO

**Décision** : cet ADR **reste DRAFT** jusqu'à ratification A0 explicite. **Aucun cron** ne sera activé pour ce périmètre. Le backlog WF1 §2c (wargames 05 redact.py → 07 quiz.html → 06 prompts AARRR) garde sa propre cadence d'exécution — ce PRD ne crée **pas de chantier neuf** (PRD §6 verbatim).

## 7. Risks & Rollback

### 7.1. Risks (D6 catalogue)

| # | Risk | Sévérité | Mitigation |
|---|---|---|---|
| R1 | Drift aesthetic entre les 3 landings (= perte cohérence Nexus brand) | MEDIUM | D3 nuance §3.3 — c'est le but, **pas** un bug. Sisters FR/EN canon restent brand-consistent (dark+gold) pour le socle non-persona |
| R2 | Claim inventée qui passe la red-team | HIGH (ADR-SOBER-002 violation) | red-team A0 desk-check obligatoire avant publication + sim `/office-hours` wargame 09 M4 adversariale |
| R3 | Marcus (Strate A) ne convertit pas aussi bien que Harrison (Strate B focus prioritaire A+) | LOW | PRD §3 focus prioritaire B — A est maintenu pour la couverture canon, pas pour le volume |
| R4 | wargames 05/06/07 pas exécutés à temps → stubs visibles | MEDIUM | stub iframe honnête « disponible W3 » plutôt que fausse feature (ADR-SOBER-002) |
| R5 | Cohérence des single-files 3× = drift de qualité | MEDIUM | même auteur/agent pour les 3, revue code-reviewer (`code-reviewer` agent) avant merge |
| R6 | Domaines custom `omk-nexus-marcus/harrison/david.vercel.app` squattés ou refusés | LOW | déploiement initial sur sous-domaine `vercel.app`, custom domain gated 3 cycles verts (PRD §6) |
| R7 | Confusion persona Harrison / Christian Vance (même nom de famille Vance) | LOW | README interne distingue explicitement — landing affiche « Harrison Vance / Clara Sterling » (PRD §4 verbatim) |
| R8 | Personnalisation Amara/Christian non couverte | LOW | backlog WF1 §2c + 4 sims `/office-hours` valideront s'ils deviennent des landings (outboard gated) |
| R9 | Pricing $1000/mois critiqué comme trop élevé pour Strate A (Marcus coach solo) | MEDIUM | ADR-AAAS-PRICING-001 + plan-L2 §13 = tier canon Enterprise OS wargamé, A0 décide — pas de drift pricing local |

### 7.2. Rollback

**Stratégie** : **no-hard-delete** (ADR-META-001 D4 append-only). Si A0 décide de retirer une landing ou l'ADR entier :

| Action | Path | Source |
|---|---|---|
| Retirer landing L1/L2/L3 | `_TRASH_<date>_nexus_landings_retired/` | canon `_TRASH` pattern MEMORY.md + ADR-META-001 |
| Retirer cet ADR | `_TRASH_<date>_adr_landing_personas_retired/` | idem |
| Marquer ADR SUPERSEDED | append note « SUPERSEDED by ADR-XXX » + pointer vers nouveau | ADR-META-001 D4 |

**Aucun `Remove-Item` brutal** sur les single-files. Le domaine Vercel est libéré, le repo GitHub est archivé (pas supprimé), le wiki log capture la décision.

## 8. Statut C — artefact-first, 0 cron until A0 per-cron GO

**Posture C appliquée** (mindsets canon 2026-06-25) :

- ✅ **Artefact créé** : ce ADR DRAFT, sister canon référencée, sources canon D1-vérifiées
- ❌ **Aucun cron activé** pour ce périmètre (anti-paperclip, ADR-SOBER-002)
- ❌ **Aucun déploiement landing** avant ratification A0 (posture artefact-first)
- ⏸ **En attente** : relecture A0 + sister chain ouverte si A0 demande amendement (Jerry → Summers Nexus BOS si E-Myth SYSTEMIZE gate, puis SHIP gate)

**Prochain pas canon** (PRD §8 verbatim) :

> « Exécuter le backlog WF1 §2c dans l'ordre déjà gravé (05 redact.py → 07 quiz.html → 06 prompts AARRR), puis les 4 sims `/office-hours` (09 M4) avec les personas de ce PRD comme adversaires. Chaque sim sans objection non résolue = sim complaisante, à refaire. »

**A0 actions requises pour ratifier cet ADR** :

1. Relecture texte §3.3 (palettes différenciées) — cohérence canon
2. Confirmation priorisation Marcus/Harrison/David (PRD §4) — pas d'Amara/Christian
3. Confirmation stack single-file vanilla (pas de framework) — sister EN canon
4. Confirmation gating outboard 3 cycles verts pour domaine custom — PRD §6
5. Confirmation pricing display $1000/mois gated ×100 (plan-L2 §13) sur les 3 landings

## 9. Decision summary (TL;DR)

- **Scope** : exactement **3 landings distinctes**, une par persona prioritaire canon (PRD §4 ★ prioritaire) — Marcus (Strate A) / Harrison (Strate B focus prioritaire A+) / David (Strate C).
- **Stack** : single-file vanilla HTML/CSS/JS, zero framework, zero bundler, zero CMS — sister canon `omk-nexus-landing-en.vercel.app` (LIVE).
- **Aesthetic** : 3 palettes **intentionnellement distinctes** — Marcus light editorial oxblood / Harrison dark ops electric blue / David warm industrial ash amber. Anti-template stricte (`ecc/web/design-quality.md`).
- **Doctrine** : Anti-Paperclip ADR-SOBER-002 — pas de claims non sourcés (pas de 47%, pas de 700+, pas de ×1000), pas de promesses 2027 (pas de local-first, pas de 0,01$).
- **Sister-canon** : ADR-ICP-NEXUS-001 + ADR-AAAS-PRICING-001 + ADR-MARKET-STUDY-001 + ADR-L2-AAAS-001 + ADR-SOBER-002 + plan-L2 §13.
- **Composants partagés** : quiz simulateur (wargame 07), DLP module (wargame 05), AAARR Signal-First (wargame 06), MiroFish teaser (wargame 08), Gstack orchestration (wargame 09), pricing display canon.
- **Perf budgets** : JS < 150 KB gzip, CSS < 30 KB gzip, LCP < 2.5 s, INP < 200 ms, CLS < 0.1, FCP < 1.5 s, TBT < 200 ms, AA WCAG 2.2.
- **Sécurité** : CSP nonce, HSTS preload, X-Frame-Options DENY, Referrer-Policy strict-origin-when-cross-origin.
- **Statut** : **DRAFT** — en attente de ratification A0. Aucun cron, aucun déploiement landing.
- **Rollback** : no-hard-delete, _TRASH_<date>/ pattern, archive repo GitHub (pas suppression).

---

**Fin ADR-NEXUS-LANDING-PERSONAS-001 v1 DRAFT — 2026-07-06 — B1 E-Myth Gatekeeper (Claude Code)**