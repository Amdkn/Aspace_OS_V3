---
id: ADR-LANDING-CRAFT-001
title: Landing Page de Grande Valeur — Méta-Process Canonique 7-Phases (B1 E-Myth, sister-skills canon + sister-ADRs Landing)
status: RATIFIED
ratification:
  by: "A0 Amadeus"
  date_iso: "2026-07-06"
  gate_a0_signed_off: true
  approval_token: "RATIFICATION-BATCH-01-2026-07-06-TIER-1"
  context: "Ratification Tier 1 craft DDD Landing Pages — 4 ADR sister du §A Creation Methodology (Context) + §B Design System (Context) ratifiés en bloc."
date: 2026-07-06
last_updated: 2026-07-06 (Claude Code B1 E-Myth Gatekeeper — distilled from SKILL-frontend-design canon + ADR-WORKFLOW-001 (6 phases) + ADR-NEXUS-LANDING-PERSONAS-001 (3 personas) + V1→V2 empirique screenshots 2026-07-06 + synthesis 04_synthesis.md (3 patterns transversaux), screened Anti-Paperclip D1-D8)
deciders: [A0 Amadeus]
proposed_by: Claude Code (B1 E-Myth Gatekeeper, on A0 directive "rédige ADR canonique méta-process création landing V2 a marché, leçon V1→V2 gravée")
domain: L2 Business OS / Landing Page Craft / B1 E-Myth / Skills Canon / Sister-ADRs Landing
tags: [#ADR #landing-craft #meta-process #seven-phases #ultra-prescriptif #v1-v2-lesson #skill-frontend-design #adr-workflow-001 #nexus-landing-personas #anti-template #anti-paperclip #e-myth #b1-gatekeeper #single-file #aaaas]
related:
  [
    ADR-WORKFLOW-001,
    ADR-NEXUS-LANDING-PERSONAS-001,
    ADR-ANTI-TEMPLATE-001,
    ADR-ANTI-PAPERCLIP-001,
    ADR-SKILLS-CANON-001,
    ADR-LANDING-AESTHETIC-001,
    ADR-LANDING-COPY-001,
    ADR-DESIGN-SYSTEM-001,
    ADR-ICP-NEXUS-001,
    ADR-AAAS-PRICING-001,
    ADR-MARKET-STUDY-001,
    ADR-L2-AAAS-001,
    ADR-SOBER-002,
    ADR-META-001,
    PRD-NEXUS-EVOLUTION-IA-001,
    PRD-PORTFOLIO-B1-FRANCHISE,
    SKILL-frontend-design,
    SKILL-multi-workflow,
    SKILL-swarm-orchestrator,
    ecc/web/design-quality.md,
    ecc/web/patterns.md,
    ecc/web/performance.md,
    plan-L2-business-os.md
  ]
supersedes: none
sources_canons:
  - "SKILL-frontend-design.md (canon sibling Anthropic, 41 lignes) — `C:\\Users\\amado\\omk-nexus-landing-3-personas\\_canon-skill\\SKILL-frontend-design.md`"
  - "SKILL-frontend-design.md ligne 13 — Design Thinking : 'Before coding, understand the context and commit to a BOLD aesthetic direction' (verbatim)"
  - "SKILL-frontend-design.md lignes 13-17 — 4 questions canon Design Thinking : Purpose / Tone / Constraints / Differentiation (verbatim)"
  - "SKILL-frontend-design.md ligne 15 — Tone : 'Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc.' (verbatim)"
  - "SKILL-frontend-design.md ligne 17 — Differentiation : 'What makes this UNFORGETTABLE? What's the one thing someone will remember?' (verbatim)"
  - "SKILL-frontend-design.md ligne 19 — 'CRITICAL: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.' (verbatim)"
  - "SKILL-frontend-design.md lignes 30-38 verbatim — Typography / Color & Theme / Motion / Spatial Composition / Backgrounds & Visual Details (5 axes aesthetic)"
  - "SKILL-frontend-design.md ligne 36 — 'NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds)' (verbatim)"
  - "SKILL-frontend-design.md ligne 38 — 'NEVER converge on common choices (Space Grotesk, for example) across generations' (verbatim)"
  - "PRD-NEXUS-EVOLUTION-IA-001 §2 — Pack 5 modules canon (Audit Sdiri / Wargame Fable / CEO-Bench / MiroFish / Gstack)"
  - "PRD-NEXUS-EVOLUTION-IA-001 §3 — 3 strates A/B/C et focus prioritaire B (Croissance & Prospection)"
  - "PRD-NEXUS-EVOLUTION-IA-001 §4 — 5 personas détaillés + 3 prioritaires (Marcus / Harrison / David)"
  - "PRD-PORTFOLIO-B1-FRANCHISE §1 — Tier 1 = Vendable maintenant (rails wargamés, guides riches)"
  - "PRD-PORTFOLIO-B1-FRANCHISE §2 — PRD-AUDIT-SDIRI-001 + PRD-COMPLIANCE-AIACT-001 + PRD-FUNNEL-ONBOARDING-001 = Tier 1 (3 PRD canon)"
  - "PRD-PORTFOLIO-B1-FRANCHISE §3 — Flow canon : AUDIT-SDIRI (front-door) + COMPLIANCE-AIACT → FUNNEL-ONBOARDING → HARNESS-FRANCHISE ($1000)"
  - "PRD-PORTFOLIO-B1-FRANCHISE §6 Tier 3 PRD-UNIT-ECON-PROOF-001 — table de preuve coût-fixe-vs-Jevons avec VRAIS chiffres"
  - "ADR-WORKFLOW-001 DRAFT 2026-07-06 — 6 phases canoniques multi-workflow × swarm-orchestrator (Research → Ideation → Plan → Execute → Optimize → Review)"
  - "ADR-WORKFLOW-001 §3.1 — Process 6-phases sérialisées, score-gated ≥7/10 sur 5 critères (goal/expect/scope/constraint/leverage)"
  - "ADR-WORKFLOW-001 §3.3 — Communication pattern [Mode: X — <name>] + Score check à chaque transition de phase"
  - "ADR-WORKFLOW-001 §4.2 — 5 critères canon de score : goal / expect / scope / constraint / leverage"
  - "ADR-WORKFLOW-001 §5.4 Phase 4 Execute — A2 dispatch N A3 sub-agents (1 par BC) via swarm-orchestrator avec run_in_background: true"
  - "ADR-NEXUS-LANDING-PERSONAS-001 DRAFT 2026-07-06 §3.1 — 3 landings distinctes (Marcus / Harrison / David) — sister immédiat"
  - "ADR-NEXUS-LANDING-PERSONAS-001 §3.2 — Stack single-file, zero nouveau chantier, vanilla, zero CDN tiers"
  - "ADR-NEXUS-LANDING-PERSONAS-001 §2.5 — 3 personas prioritaires PRD §4 : Marcus Strate A · Harrison Strate B · David Strate C"
  - "ADR-LANDING-AESTHETIC-001 (HYPOTHÈSE sister canon à canoniser — sister du présent ADR) — doctrine esthétique inter-bannie par landing"
  - "ADR-LANDING-COPY-001 (HYPOTHÈSE sister canon à canoniser — sister du présent ADR) — copywriting canonique 3 personas"
  - "ADR-DESIGN-SYSTEM-001 (HYPOTHÈSE sister canon à canoniser — sister du présent ADR) — tokens CSS canoniques"
  - "ADR-ANTI-TEMPLATE-001 DRAFT 2026-07-06 §3 — 7 listes noires formelles (Fonts / Palettes / Layouts / Composants / Motion / Backgrounds / Détails)"
  - "ADR-ANTI-TEMPLATE-001 §3.1 — Fonts bannies : Inter / Inter Tight / Roboto / Arial / system-ui / Space Grotesk / Helvetica"
  - "ADR-ANTI-PAPERCLIP-001 DRAFT 2026-07-06 §C1 — PRD-NEXUS §7.6 verbatim : 'Les chiffres (47% conversion, 700+ signaux, ×1000) — non sourcés, à ne JAMAIS republier sans vérification (D1) ; sur une landing = claims à bench ou à retirer'"
  - "ADR-ANTI-PAPERCLIP-001 §2 C2 — Sister-scope avec ADR-SOBER-002 sans duplication (SOBER-002 = kernel, ce ADR = surface landing)"
  - "ADR-SKILLS-CANON-001 DRAFT 2026-07-06 — Tier A skills création landing (frontend-design, dataviz, swarm-orchestrator)"
  - "ADR-SOBER-002 RATIFIED 2026-06-21 — Anti-Paperclip doctrine kernel : pas de promises 2027, pas de chiffres non sourcés"
  - "ADR-META-001 RATIFIED D1-D8 — D1 Verify-Before-Assert, D6 Root-Cause, D7 Cost-Of-Escalation"
  - "ECC rules `C:\\Users\\amado\\.claude\\rules\\ecc\\web\\design-quality.md` — Anti-Template Policy + Required Qualities (≥4/10) + Worthwhile Style Directions"
  - "V1 empirique — chemins absolus `C:\\Users\\amado\\omk-nexus-landing-3-personas\\{index,marcus-coach-c-suite,harrison-bdr-agency,david-fractional-coo}.html` (HTML horodatés 10:47-10:52, brief générique)"
  - "V2 empirique — chemins absolus `C:\\Users\\amado\\omk-nexus-landing-3-personas\\v2\\{index,marcus-coach-c-suite,harrison-bdr-agency,david-fractional-coo}.html` (HTML brief ULTRA-PRESCRIPTIF)"
  - "_references/04_synthesis.md verbatim — PATTERN-1 'code as first-class typography' (Apartamento N°037 / Linear ENG-2085 / Teenage Engineering EP-133)"
  - "_references/04_synthesis.md verbatim — PATTERN-2 'canvas non-blanc à température assumée' (cream `#F5F1EA` Marcus / ink `#0A0A0A` Harrison / warm cream `#F2EEE6` David)"
  - "_references/04_synthesis.md verbatim — PATTERN-3 'accent parcimonieux & sémantique' (oxblood Marcus / teal électrique Harrison / amber `#D86A2A` David)"
  - "_references/04_synthesis.md D1 receipts — 3 WebFetch réussis (apartamentomagazine.com / linear.app / teenage.engineering), 0 référence inventée"
  - "_screenshots/v2_00_index.png + v2_01_marcus.png + v2_02_harrison.png + v2_03_david.png — screenshots V2 réussie"
  - "MEMORY.md §'Nexus EN landing DEPLOYED 2026-06-29' — single-file index.html 628 KB · EN ratio 96.8% · dark theme #0A0E16 + #C8A55C"
provenance: |
  Née 2026-07-06 d'une directive A0 B1 E-Myth Gatekeeper ('Rédige l'ADR canonique ADR-LANDING-CRAFT-001
  qui synthétise le méta-process création landing V2 a marché'). Le V1 a été HONNI (4 HTML horodatés
  10:47-10:52 brief générique), le V2 a RÉUSSI (4 HTML brief ULTRA-PRESCRIPTIF font spec + color spec +
  accent spec + signature element spec + section naming convention par persona). SKILL-frontend-design.md
  (41 lignes canon sibling Anthropic) lu en D1 — lignes 13-19 Design Thinking + lignes 30-38 Frontend
  Aesthetics Guidelines transcrites verbatim. ADR-WORKFLOW-001 (DRAFT même date — 6 phases canoniques
  multi-workflow × swarm-orchestrator) sister immédiat. ADR-NEXUS-LANDING-PERSONAS-001 (DRAFT même date —
  3 landings Marcus/Harrison/David) sister immédiat. _references/04_synthesis.md (PATTERN-1/2/3)
  lu en D1. Screenshots V2 dans _screenshots/v2_*.png (D1 receipts). Statut DRAFT — ratification A0
  attendue post-relecture canon.
---

# ADR-LANDING-CRAFT-001 — Méta-Process Canonique 7-Phases pour Landing Page de Grande Valeur

## 1. Status

**DRAFT** — 2026-07-06. Produit par Claude Code **B1 E-Myth Gatekeeper**, sur directive A0 Amadeus. Cet ADR **synthétise** le méta-process canonique de création Landing à partir de **3 sister-canon DRAFT** (mêmes date) + 1 skill canonique sibling + 1 leçon empirique V1→V2 ancrée screenshots.

| Sister-canon | Rôle | Source |
|---|---|---|
| **`ADR-WORKFLOW-001`** | Process 6-phases multi-workflow × swarm-orchestrator (Research → Ideation → Plan → Execute → Optimize → Review) | canon DRAFT 2026-07-06 |
| **`ADR-NEXUS-LANDING-PERSONAS-001`** | 3 landings distinctes par persona ICP (Marcus / Harrison / David) | canon DRAFT 2026-07-06 |
| **`ADR-ANTI-TEMPLATE-001`** | 7 listes noires formelles (Fonts / Palettes / Layouts / Composants / Motion / Backgrounds / Détails) | canon DRAFT 2026-07-06 |
| **`ADR-ANTI-PAPERCLIP-001`** | Interdits textuels (chiffres non sourcés, claims 2027) | canon DRAFT 2026-07-06 |
| **`ADR-LANDING-AESTHETIC-001`** *(HYPOTHÈSE)* | Doctrine esthétique inter-bannie par landing | sister à canoniser |
| **`ADR-LANDING-COPY-001`** *(HYPOTHÈSE)* | Copywriting canonique 3 personas | sister à canoniser |
| **`ADR-DESIGN-SYSTEM-001`** *(HYPOTHÈSE)* | Tokens CSS canoniques | sister à canoniser |
| **`ADR-SKILLS-CANON-001`** | Inventaire 5 tiers (A→E) skills + activation conditions | canon DRAFT 2026-07-06 |

> **D3 nuance** : ce méta-process **ne ré-écrit pas** `ADR-WORKFLOW-001` (6 phases). Il le **traduit** au niveau **surface-landing** : la V2 a prouvé qu'il fallait un **méta-process 7-phases Jack Roberts-inspired** où la **Phase 4 (Style Direction ULTRA-PRESCRIPTIF)** est la clé de voûte. **Pas duplication** : spécialisation par couche.

## 2. Context — D6 racine + Leçon V1→V2 empirique

### 2.1. D6 racine — pas de méta-process canon pour création Landing

Avant ce ADR, **AUCUN méta-process canon formalisé** pour orchestrer la création d'une Landing Page de grande valeur (canon `_SPECS/ADR/L2_Business_OS/`). Les sources canoniques existent mais ne sont **pas reliées** :

| Source canon | Status pré-ADR |
|---|---|
| SKILL `frontend-design` (Anthropic) | EXISTE (41 lignes, lu D1 verbatim) — Design Thinking + 5 axes aesthetic |
| ADR-WORKFLOW-001 | EXISTE (DRAFT 2026-07-06) — 6 phases multi-workflow × swarm-orchestrator |
| ADR-NEXUS-LANDING-PERSONAS-001 | EXISTE (DRAFT 2026-07-06) — 3 landings Marcus/Harrison/David |
| ADR-ANTI-TEMPLATE-001 | EXISTE (DRAFT 2026-07-06) — 7 listes noires formelles |
| `_references/04_synthesis.md` | EXISTE — 3 patterns transversaux (code as typo / canvas non-blanc / accent parcimonieux) |
| V1 vs V2 empirique | **PAS** codifié — c'est la D6 racine de ce ADR |

**Risque D6** : sans méta-process canon, chaque nouvelle landing **dérive** vers le brief générique "anti-template + design différencié" qui a **produit V1 (honnie)**. **Pas de D1 receipts sur la brief elle-même** — chaque génération improvise.

### 2.2. D1 receipts V1 vs V2 empirique (screenshots ancrés)

**D1 receipts 2026-07-06 — chemins absolus vérifiés par `ls`** :

| Version | Chemins absolus | Brief | Résultat D1 |
|---|---|---|---|
| **V1 honnie** | `C:\Users\amado\omk-nexus-landing-3-personas\index.html` (10:47) · `marcus-coach-c-suite.html` (10:52) · `harrison-bdr-agency.html` (10:52) · `david-fractional-coo.html` (10:52) | **GÉNÉRIQUE** — "anti-template", "design différencié" | 4 HTML plats, baseline SaaS, peu différenciés entre personas |
| **V2 réussie** | `C:\Users\amado\omk-nexus-landing-3-personas\v2\index.html` · `v2\marcus-coach-c-suite.html` · `v2\harrison-bdr-agency.html` · `v2\david-fractional-coo.html` | **ULTRA-PRESCRIPTIF** — font spécifiée par page + couleur spécifiée + accent spécifié + signature element spécifié + section naming convention | 3 esthétiques radicalement différenciées : Editorial Ledger (Marcus) / Terminal Stratégique (Harrison) / Atelier Industriel (David) |

**Screenshots ancrés D1** : `_screenshots/v2_00_index.png` · `v2_01_marcus.png` · `v2_02_harrison.png` · `v2_03_david.png` — vérification visuelle de la différenciation (D1 receipt canon).

### 2.3. La leçon V1→V2 gravée (D6 root-cause)

**D6 root-cause** (verbatim ADR-META-001 D6 : « what's the actual blocker, not the symptom ») :

> **La V1 a failli parce que le brief était GÉNÉRIQUE** ("anti-template", "design différencié"). Les sub-agents A3 (swarm-orchestrator pattern) ont produit du **default AI slop** (Inter, purple gradient, card grid, "Get Started") car le brief ne contenait **aucune prescription** sur la font / couleur / accent / signature / section naming.
>
> **La V2 a réussi parce que le brief était ULTRA-PRESCRIPTIF** : pour chaque persona, le brief spécifiait (a) la **font display** et **font body**, (b) la **couleur de fond** + **accent signature**, (c) l'**élément signature mémorable** (Apartamento N°037 / Linear ENG-2085 / Teenage Engineering EP-133), (d) la **convention de section naming** (Dossier N°037 pour Marcus / ACC-2085·04/12 pour Harrison / OPS-01 pour David).

**Gravé dans cet ADR** : tout brief de génération Landing DOIT contenir ces 5 spécifications (font / couleur / accent / signature / section naming). Sinon → garantie de default AI slop.

### 2.4. La doctrine canonique à respecter (4 piliers)

Le méta-process 7-phases doit encoder **4 piliers non-négociables** :

| Pilier | Source canon | Conséquence méta-process |
|---|---|---|
| **A2 = Orchestrateur Stratégique** | CLAUDE.md §'Rôles' + ADR-WORKFLOW-001 §5.4 | A2 ne code JAMAIS en main agent — délègue TOUT aux A3 sub-agents en background |
| **A3 = sub-agents canon** | CLAUDE.md §'Mindsets' + ADR-WORKFLOW-001 §5.4 Phase 4 | 1 sub-agent A3 par landing (×3 personas), en parallèle via `swarm-orchestrator` |
| **D1 Verify-Before-Assert** | ADR-META-001 D1 | Brief ULTRA-PRESCRIPTIF → D1 receipts par spec (font URL / color hex / accent hex / signature element description) |
| **D7 Cost-Of-Escalation** | ADR-META-001 D7 | A0 ratifie à 1 seul gate (Gate B1 #3 — Plan + ADR), pas d'escalation mid-research |

## 3. Décision — Méta-Process 7-Phases Jack Roberts-Inspired + Activation Gates

### 3.1. Périmètre — 7 phases sérialisées, A2 orchestrateur, A3 exécutants

**Décision gravée** : la création d'une Landing Page de grande valeur suit **exactement 7 phases sérialisées**. **A2 (Main Agent = Claude Code) orchestre, A3 sub-agents exécutent en background** (sister canon ADR-WORKFLOW-001 §5.4).

```
A0 Intent → A2 Analyse → A2 Scope (AskUserQuestion, sister §3.2)
  → Phase 1 Research (A2 + Codex/Gemini sub-agents, canon canon §3.2 sister)
  → Phase 2 Wireframe (A2 + B3-Enterprise-Geordi)
  → Phase 3 Design System (A2 + frontend-design skill canon, sister §3.3)
  → Phase 4 Style Direction ULTRA-PRESCRIPTIF ★ GATE B1 #1 ★
  → Phase 5 Multi-Page Build (3 A3 sub-agents en parallèle, swarm-orchestrator)
  → Phase 6 Animation/Data Integration (A2 + frontend-design skill canon)
  → Phase 7 QA + Ship (A2 + e2e-runner + ratify-adr sister canon)
```

**Sister canon clé** : `ADR-WORKFLOW-001` (DRAFT 2026-07-06) Process 6-Phases. **Mapping** :
- **Phase 1 Research** = Workflow-001 Phase 1 Research (canon §5.1)
- **Phase 2 Wireframe** = Workflow-001 Phase 2 Ideation (Vision DDD → sitemap 5-7 pages)
- **Phase 3 Design System** = Workflow-001 Phase 3 Plan (tokens + components canon)
- **Phase 4 Style Direction** = NOUVEAU (V1→V2 lesson — brief ULTRA-PRESCRIPTIF par persona)
- **Phase 5 Multi-Page Build** = Workflow-001 Phase 4 Execute (1 A3 par persona, run_in_background: true)
- **Phase 6 Animation/Data Integration** = Workflow-001 Phase 5 Optimize (motion orchestré)
- **Phase 7 QA + Ship** = Workflow-001 Phase 6 Review (Playwright + Lighthouse + D1 receipts + Gate A0 #2)

### 3.2. Activation gate B1 — quand déclencher ce méta-process ?

**Décision** : on déclenche ce méta-process 7-phases (vs rester en single-back-and-forth) si et seulement si **au moins 1 de 3 conditions** est vraie :

| # | Condition d'activation | Source canon | Justification D6 |
|---|---|---|---|
| **C1** | **Nouveau ICP persona** introduit dans la doctrine AaaS (sister canon ADR-NEXUS-LANDING-PERSONAS-001) | ADR-ICP-NEXUS-001 RATIFIED 2026-06-24 | Persona = brief totalement nouveau, brief générique garanti dériver en AI slop |
| **C2** | **Redesign landing majeure** (>50% des sections touchées) sur persona existant | D6 root-cause : changement majeur = nouvelle brief, sinon drift | |
| **C3** | **Pivot doctrinal** (ex. `ADR-OMK-NEXUS-TRANSFORM-001_omk-to-nexus-pivot.md` pivot omk→nexus) qui invalide la brief précédente | PRD §1 pivot doctrinal gravé par A+ | Brief obsolète, régénération complète requise |

**Sinon** (redesign mineur, ≤50% sections touchées, pas de pivot) : rester en **single-back-and-forth**, PAS de méta-process. **D3 nuance YAGNI** : ne JAMAIS sur-orchestrer un livrable simple (sister canon ADR-WORKFLOW-001 §3.2 YAGNI gate).

### 3.3. Communication pattern — `[Phase: X — <name>]` label + D1 receipts par spec

**Décision** : à chaque transition de phase, A2 émet un message avec `[Phase: X — <name>]` label où X = numéro phase + nom canon. **Format canon** (sister ADR-WORKFLOW-001 §3.3) :

```
[Phase: X — <name>]
D1 receipts : <paths absolus + hashes ou URLs>
D6 root-cause (si FORCE-STOP) : <verbatim>
Verdict : <CONTINUE | FORCE-STOP>
Si CONTINUE → Phase X+1
Si FORCE-STOP → diagnostic D6 root-cause, retour Phase X ou escalation A0
```

## 4. Les 7 Phases en Détail

### 4.1. Phase 1 — Research (A2 + Codex/Gemini sub-agents)

**Goal canon** : extraire le canon depuis PRD source + sœur ADRs + wiki canon, scorer ≥7/10 sur 5 critères (sister ADR-WORKFLOW-001 §4.2).

**Pattern canon sister** : `ADR-WORKFLOW-001 §5.1 Phase 1 Research` (verbatim).

**Outils réels** :
1. A2 lit **PRD source** canon : `PRD-NEXUS-EVOLUTION-IA-001` (§2 modules canon + §3 strates + §4 personas)
2. A2 lit **PRD-PORTFOLIO-B1-FRANCHISE** §1 §2 §3 (Tier 1 canon : AUDIT-SDIRI + COMPLIANCE-AIACT + FUNNEL-ONBOARDING)
3. A2 lit **sister ADRs Landing** canon : `ADR-NEXUS-LANDING-PERSONAS-001` (3 personas) + `ADR-ANTI-TEMPLATE-001` (7 listes noires) + `ADR-ANTI-PAPERCLIP-001` (interdits textuels) + `ADR-LANDING-AESTHETIC-001` (HYPOTHÈSE) + `ADR-LANDING-COPY-001` (HYPOTHÈSE) + `ADR-DESIGN-SYSTEM-001` (HYPOTHÈSE)
4. A2 lit **skills canon** Tier A (`ADR-SKILLS-CANON-001`) : `frontend-design` (SKILL-frontend-design.md) + `swarm-orchestrator`
5. A2 spawn Codex/Gemini sub-agents en background pour enrichir canon data + canon UI
6. A2 synthétise en **Brief Canon** (max 2 pages) + score ≥7/10 sur 5 critères
7. Si score < 7 → FORCE-STOP, diagnostic D6 root-cause

**Anti-pattern A4 interdit** : A2 ne lit JAMAIS synchrone en attendant Codex/Gemini. `run_in_background: true` mandatory (sister canon ADR-WORKFLOW-001 §4.1 A4).

### 4.2. Phase 2 — Wireframe (sitemap 5-7 pages)

**Goal canon** : produire un **wireframe sitemap 5-7 pages** par persona, basé sur le **framework 5 questions** (sister Skill `frontend-design` Design Thinking + sister E-Myth).

**Pattern canon sister** : `SKILL-frontend-design.md` Design Thinking (lignes 13-17 verbatim) — 4 questions canon : **Purpose / Tone / Constraints / Differentiation**. **Extension B1 E-Myth** : ajouter la **5e question** **Brand Assets** (logos, fonts owned, palette owned).

**Outils réels** :
1. A2 pose **5 questions framework** par persona :
   - **Qui** = ICP persona (sister ADR-ICP-NEXUS-001 + PRD §4)
   - **Que veut-il** = JTBD canon (sister PRD-PORTFOLIO-B1-FRANCHISE Tier 1)
   - **Quelles objections** = anti-paperclip inversé (sister ADR-ANTI-PAPERCLIP-001 — transforme interdits en réponses)
   - **Quel vibe** = Tone extreme (sister SKILL-frontend-design.md ligne 15)
   - **Brand assets** = fonts owned + palette owned + signature element
2. A2 dispatch **B3-Enterprise-Geordi** (Chief Engineer USS Enterprise) pour produire **sitemap 5-7 pages** par persona
3. Sitemap canon (7 pages par défaut) : **Sign-In · Hero · Features · How it works · FAQ · CTA · Footer** (+ **About** et **Services** selon scope persona)
4. A2 produit **wireframe low-fi** (texte structuré, pas Figma) — 1 wireframe par page
5. Score rapide Phase 2 (≥6/10 sur goal/leverage, sister ADR-WORKFLOW-001 §5.2) → Phase 3

### 4.3. Phase 3 — Design System (tokens + components + atmosphérique)

**Goal canon** : produire les **tokens CSS canon** (couleurs, typo, layout, signature) + **components canon** (cards, nav, hero, footer) + **éléments atmosphériques** (grain, shadows, decorative borders, custom cursor).

**Pattern canon sister** : `SKILL-frontend-design.md` Frontend Aesthetics Guidelines (lignes 30-38 verbatim) — **5 axes aesthetic** : Typography / Color & Theme / Motion / Spatial Composition / Backgrounds & Visual Details.

**Outils réels** :
1. A2 dispatch B3-Enterprise-Geordi pour produire **tokens CSS canon** (sister `ADR-DESIGN-SYSTEM-001` HYPOTHÈSE) :
   - **Couleurs** : palette de fond + accent signature (pas neutre, sister PATTERN-2 `_references/04_synthesis.md`)
   - **Typo** : display font + body font (sister PATTERN-3 — accent parcimonieux)
   - **Layout** : grid + spacing + breakpoints
   - **Signature** : custom cursor / decorative border / grain overlay
2. A2 produit **components canon** (cards / nav / hero / footer / CTA / FAQ)
3. A2 produit **éléments atmosphériques** (sister SKILL-frontend-design.md ligne 34 verbatim : « gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays »)
4. A2 livre **Design System Spec** (1 fichier HTML/CSS de référence)
5. Score check rapide → Phase 4

### 4.4. Phase 4 — Style Direction ULTRA-PRESCRIPTIF ★ GATE B1 #1 ★

**Goal canon** : produire **un Brief ULTRA-PRESCRIPTIF par persona** contenant les **5 specs obligatoires** (leçon V1→V2 gravée §2.3).

**★ GATE B1 #1 ★** : B1 E-Myth Gatekeeper (Claude Code A2) **valide** que le brief contient les 5 specs AVANT de dispatcher Phase 5. **Si une spec manque → FORCE-STOP, retour Phase 4**.

**Pattern canon sister** : SKILL-frontend-design.md Design Thinking **Differentiation** (ligne 17 verbatim : « **What makes this UNFORGETTABLE? What's the one thing someone will remember?** »).

**Outils réels** — A2 produit **1 brief par persona** contenant **OBLIGATOIREMENT** les 5 specs :

| # | Spec obligatoire | D1 receipt attendu | Leçon V1→V2 ancrée |
|---|---|---|---|
| **S1** | **Font display + font body** spécifiées par nom exact + URL de source | Nom font + URL (Google Fonts ou self-host) | V1 n'avait PAS de font spec → Inter par défaut |
| **S2** | **Couleur de fond** spécifiée par hex + **accent signature** par hex + **température** (cream/ink/warm) | Hex codes + justification | V1 avait SaaS blanc par défaut |
| **S3** | **Élément signature mémorable** spécifié (sister SKILL-frontend-design.md ligne 17 Differentiation) — ex. code-as-typo (Apartamento N°037) | Description 1 phrase + ref D1 | V1 n'avait PAS de signature → composantes plates |
| **S4** | **Section naming convention** spécifiée par persona (sister PATTERN-1 `_references/04_synthesis.md`) — ex. Dossier N°037 (Marcus) / ACC-2085·04/12 (Harrison) / OPS-01 (David) | Convention explicite + 3 exemples | V1 n'avait PAS de convention → sections génériques |
| **S5** | **Motion signature** spécifié (sister SKILL-frontend-design.md ligne 32 — « one well-orchestrated page load with staggered reveals ») | Description animation 1 phrase | V1 animations scattered |

**Brief V2 exemple (Marcus Vance — Editorial Ledger)** — exemple tiré des `_references/04_synthesis.md` :

> **S1 Font** : display = serif italic transitional (ex. GT Sectra ou Domaine Display) ; body = serif tabulaire (ex. Lyon Text ou Tiempos) — **PAS** Inter, **PAS** Roboto (sister `ADR-ANTI-TEMPLATE-001 §3.1`).
> **S2 Couleur** : fond = cream chaud `#F5F1EA` (Apartamento) ; accent = oxblood `#5C1A1B` (réservé CTA + badge membership + 1 signature) ; ink = `#1A1A1A` (texte).
> **S3 Signature** : **identifiant sémantique comme typo de premier plan** — numéro de dossier tabulaire « Dossier N°037 » en hero (sister PATTERN-1 `_references/04_synthesis.md`).
> **S4 Section naming** : « Dossier N°XXX » pour chaque section (Dossier N°037 Hero · Dossier N°038 Features · etc.) — préfixe canon.
> **S5 Motion** : fade-in tabulaire + scroll-triggered ledger entries (1 cascade orchestrée, PAS scattered micro-interactions).

**Brief V2 Harrison Vance (Terminal Stratégique)** — extrait `_references/02_harrison-terminal.md` :

> **S1 Font** : display = sans géométrique condensé (ex. Berkeley Mono / JetBrains Mono) ; body = mono-heavy + grotesque.
> **S2 Couleur** : fond = ink `#0A0A0A` / `#000` ; accent = teal électrique (signature unique) ; surface = `#1A1A1A`.
> **S3 Signature** : **clés mono comme typo de premier plan** — « ACC-2085 · 04/12 » en hero + data-tiles KPI (sister Linear grammar adapté en canvas ink-black).
> **S4 Section naming** : « ACC-XXX · NN/NN » préfixe canon pour chaque section.
> **S5 Motion** : live-data ticker + terminal-style reveal (1 cascade).

**Brief V2 David Kross (Atelier Industriel)** — extrait `_references/03_david-atelier.md` :

> **S1 Font** : display = IBM Plex Mono + grotesque (ex. IBM Plex Sans + IBM Plex Mono).
> **S2 Couleur** : fond = warm cream `#F2EEE6` (Teenage Engineering) ; accent = amber `#D86A2A` (sister PATTERN-2) ; ink = `#1A1A1A`.
> **S3 Signature** : **part-number / SKU opérationnel** — « OPS-01 » en hero + datasheet layout (sister PATTERN-1 Teenage Engineering).
> **S4 Section naming** : « OPS-XX » préfixe canon pour chaque section.
> **S5 Motion** : blueprint grid reveal + bevel-shadow hover (1 cascade).

### 4.5. Phase 5 — Multi-Page Build (3 A3 sub-agents en parallèle)

**Goal canon** : implémenter **3 landings distinctes** (Marcus / Harrison / David) en **parallèle background**, 1 A3 sub-agent par persona.

**Pattern canon sister** : `ADR-WORKFLOW-001 §5.4 Phase 4 Execute` (verbatim : « A2 dispatch N sub-agents A3 (1 par BC) via `swarm-orchestrator` avec `run_in_background: true` »).

**Outils réels** :
1. A2 dispatch **3 sub-agents A3 en parallèle** (`run_in_background: true` mandatory) :
   - **A3-Marco-Builder** (persona Marcus Vance · Editorial Ledger)
   - **A3-Harrison-Builder** (persona Harrison Vance · Terminal Stratégique)
   - **A3-David-Builder** (persona David Kross · Atelier Industriel)
2. Chaque A3 reçoit **Brief ULTRA-PRESCRIPTIF Phase 4** sister canon (PAS de brief générique, sister §2.3 leçon V1→V2)
3. Chaque A3 produit **1 fichier HTML single-file** (sister `ADR-NEXUS-LANDING-PERSONAS-001 §3.2` : vanilla, zero CDN tiers, zero framework)
4. A2 dispatch **A3-Index-Builder** (sub-agent 4) pour `index.html` hub liant les 3 personas
5. Chaque A3 rapporte à A2 (commits, screenshots staging, paths absolus)
6. A2 monitor sans bloquer (`swarm-orchestrator` When NOT to Delegate)

**D4 no-contradiction** : aucun A3 ne touche au canon (CLAUDE.md, MEMORY.md, wiki/) sans gate A0 explicite (sister ADR-WORKFLOW-001 §5.4).

### 4.6. Phase 6 — Animation/Data Integration (motion orchestré)

**Goal canon** : orchestrer **motion signature** (sister Phase 4 S5 spec) + intégrer **data-tiles live** (sister SKILL-frontend-design.md ligne 32 « one well-orchestrated page load with staggered reveals »).

**Pattern canon sister** : `SKILL-frontend-design.md` ligne 32 verbatim — « **one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions** ».

**Outils réels** :
1. A2 dispatch A3 par persona pour implémenter **motion signature** (CSS keyframes + scroll-triggered)
2. A2 dispatch A3 par persona pour intégrer **data-tiles live** (Harrison — KPI mock + cycle counter ; Marcus — ledger entries ; David — datasheet entries)
3. A2 review motion contre **Anti-pattern Motion Scatter** (sister `ADR-ANTI-TEMPLATE-001` §3.5 — bannir hover effects dispersés)
4. Patch List ≤ 10 items prioritaires
5. Si score Optimize <7/10 → retry (max 3 itérations avant FORCE-STOP, sister ADR-WORKFLOW-001 §5.5)

### 4.7. Phase 7 — QA + Ship (Playwright + Lighthouse + D1 receipts + ratification)

**Goal canon** : validation finale via **5 critères self-critique** + **Playwright screenshots** + **Lighthouse scores** + **D1 receipts** + **ratification A0**.

**Pattern canon sister** : `ADR-WORKFLOW-001 §5.6 Phase 6 Review` (verbatim).

**Outils réels** :
1. A2 dispatch `e2e-runner` pour screenshots 4 breakpoints (320, 768, 1024, 1440) — canon `ecc/web/testing.md`
2. A2 dispatch `lighthouse_audit` pour score Performance/A11y/Best Practices/SEO — canon `ecc/web/performance.md` targets (LCP <2.5s, INP <200ms, CLS <0.1)
3. A2 génère **Rapport Final** :
   - 5 critères self-critique (sister SKILL-frontend-design.md)
   - Screenshots (paths absolus)
   - D1 receipts (URLs live, hashes commits, scores Lighthouse)
4. A2 présente à A0 → **Gate A0 #2** (RATIFY/REJECT/REVISE — sister ADR-WORKFLOW-001 §5.6)
5. Si RATIFY → handoff canon (wiki/hand_offs/) + MEMORY.md update (D4 append-only)
6. Si REJECT → retour Phase 1 ou Phase 4 selon feedback
7. Si REVISE → A0 indique patch ciblé, A2 patch + re-Phase 7

## 5. Doctrine — Anti-Patterns Interdits (gravés leçon V1→V2)

| # | Anti-pattern | Conséquence | Source canon | Gravé leçon V1→V2 |
|---|---|---|---|---|
| A1 | A2 (Main Agent) code directement | Viole `CLAUDE.md §'🕷️ Doctrine Swarm Orchestration'` | `ADR-WORKFLOW-001 §4.1` | — |
| A2 | **Brief générique** ("anti-template", "design différencié") | **Produit default AI slop** (Inter, purple gradient, card grid) | **D6 root-cause §2.3** | **OUI — V1 honnie** |
| A3 | Brief sans 5 specs obligatoires (font / couleur / accent / signature / section naming) | Garantie de drift AI slop | D6 root-cause §2.3 | **OUI — V1 honnie** |
| A4 | Sauter Phase 4 (Style Direction ULTRA-PRESCRIPTIF) | Viole gate B1 #1 | Phase 4 §4.4 | **OUI — V1 honnie** |
| A5 | A3 sub-agent bloque A2 synchrone | Viole SKILL `swarm-orchestrator` « Never Execute Directly » | `ADR-WORKFLOW-001 §4.1 A4` | — |
| A6 | Convergence sur Space Grotesk / Inter / Roboto / Arial / system-ui | Viole `SKILL-frontend-design.md` ligne 36 + 38 verbatim | `ADR-ANTI-TEMPLATE-001 §3.1` | — |
| A7 | Chiffres non sourcés (« 47% conversion », « ×10 ROI ») | Viole `ADR-ANTI-PAPERCLIP-001 §C1` + `PRD-NEXUS §7.6` verbatim | sister canon `ADR-SOBER-002` | — |
| A8 | Méta-process pour redesign mineur (≤50% sections touchées) | YAGNI violation | C1/C2/C3 gate §3.2 | — |
| A9 | Escalation A0 mid-research sans 2 FORCE-STOP consécutifs | Viole D7 cost-of-escalation | `ADR-META-001 D7` | — |

## 6. Activation Gates B1 — exactement 3, à moments fixes

| Gate # | Moment | Phase de rattachement | Livrable attendu | Décision A0/B1 |
|---|---|---|---|---|
| **Gate B1 #1** | Fin Phase 4 Style Direction | Phase 4 ★ | Brief ULTRA-PRESCRIPTIF par persona (5 specs obligatoires) | GO (Phase 5) / NO-GO (retour Phase 4) |
| **Gate A0 #1** (sister ADR-WORKFLOW-001) | Fin Phase 3 Plan — sister | Phase 3 sister | ADR sister canon DRAFT (déjà rédigé : `ADR-NEXUS-LANDING-PERSONAS-001`) | GO/NO-GO/HOLD |
| **Gate A0 #2** | Fin Phase 7 QA + Ship | Phase 7 | Checklist QA + D1 receipts + rapport final + URLs live | RATIFY/REJECT/REVISE |

**D7 cost-of-escalation appliqué** : A2 ne demande PAS confirmation A0 entre Gate B1 #1 et Gate A0 #2. Phases 5-6 = autonomie A2/A3 sub-agents.

## 7. Sister-Canon Linkage — chaque phase pointe vers l'ADR sister qui la définit

| Phase du méta-process | Sister-canon canon (déjà ratifié ou DRAFT) |
|---|---|
| Phase 1 Research | `ADR-WORKFLOW-001 §5.1` + `SKILL-frontend-design.md` Design Thinking + `ADR-ICP-NEXUS-001` + `PRD-NEXUS-EVOLUTION-IA-001` + `PRD-PORTFOLIO-B1-FRANCHISE` |
| Phase 2 Wireframe | `ADR-NEXUS-LANDING-PERSONAS-001 §2.5` (3 personas) + `_references/04_synthesis.md` PATTERN-1/2/3 |
| Phase 3 Design System | `ADR-DESIGN-SYSTEM-001` HYPOTHÈSE + `SKILL-frontend-design.md` Frontend Aesthetics Guidelines (lignes 30-38) + `ADR-LANDING-AESTHETIC-001` HYPOTHÈSE |
| Phase 4 Style Direction ULTRA-PRESCRIPTIF | `SKILL-frontend-design.md` Differentiation (ligne 17) + `ADR-LANDING-COPY-001` HYPOTHÈSE + `_references/01_marcus-editorial.md` + `02_harrison-terminal.md` + `03_david-atelier.md` |
| Phase 5 Multi-Page Build | `ADR-WORKFLOW-001 §5.4` (swarm-orchestrator run_in_background: true) + `ADR-NEXUS-LANDING-PERSONAS-001 §3.2` (single-file vanilla) |
| Phase 6 Animation/Data Integration | `SKILL-frontend-design.md` Motion (ligne 32) + `ADR-LANDING-AESTHETIC-001` HYPOTHÈSE + `ADR-ANTI-TEMPLATE-001 §3.5` |
| Phase 7 QA + Ship | `ADR-WORKFLOW-001 §5.6` (Playwright + Lighthouse) + `ecc/web/performance.md` (LCP/INP/CLS targets) + `ADR-NEXUS-LANDING-PERSONAS-001 §3.4` (ratification) |

## 8. Verification — D1 Receipts Mandatory

### 8.1. D1 receipts obligatoires à chaque Gate

| Gate | D1 receipts à fournir |
|---|---|
| **Gate B1 #1** (Phase 4) | (1) Brief ULTRA-PRESCRIPTIF par persona (5 specs obligatoires) · (2) Paths absolus fichiers de référence (font URL / color hex / accent hex / signature description / section naming examples) · (3) Screenshots `_references/*.png` D1-fetched (3 WebFetch réussis 2026-07-06) |
| **Gate A0 #1** (Phase 3 sister) | (1) ADR sister canon DRAFT path + SHA · (2) Vision DDD 1-page · (3) Score 5 critères (sister `ADR-WORKFLOW-001 §4.2`) |
| **Gate A0 #2** (Phase 7) | (1) URLs landing live · (2) Screenshot 4 breakpoints (Playwright) · (3) Score Lighthouse (Perf/A11y/BP/SEO) · (4) Hash commits GitHub · (5) Wiki handoff path + SHA · (6) MEMORY.md update path |

### 8.2. D2 Research-First gates

**Avant chaque phase**, A2 vérifie :
- **Phase 1** : PRD source existe + sister ADRs citées (canon wiki/index.md)
- **Phase 2** : aesthetic direction référencée (canon `ecc/web/design-quality.md` Anti-Template Policy)
- **Phase 3** : tokens canon (sister `ADR-DESIGN-SYSTEM-001` HYPOTHÈSE)
- **Phase 4** : SKILL-frontend-design.md Differentiation + 5 specs obligatoires présentes
- **Phase 5** : sub-agents A3 canon existent dans le roster (`~/.claude/agents/`) — sister `ADR-SKILLS-CANON-001` Tier A
- **Phase 6** : motion signature spec présente (sister Phase 4 S5)
- **Phase 7** : checklist 5 critères + Playwright + Lighthouse dispos

### 8.3. D8 Cross-Agent — sister-canon linkage obligatoire

Ce ADR doit citer verbatim (D1 receipts validés) :
- `SKILL-frontend-design.md` lignes 13-19 + 30-38 (Design Thinking + Aesthetic Guidelines)
- `ADR-WORKFLOW-001` §3.1, §3.3, §4.2, §5.4, §5.6 (6 phases canoniques multi-workflow)
- `ADR-NEXUS-LANDING-PERSONAS-001` §2.5, §3.1, §3.2 (3 personas + single-file vanilla)
- `ADR-ANTI-TEMPLATE-001` §3.1 (fonts bannies)
- `ADR-ANTI-PAPERCLIP-001` §C1 (PRD §7.6 chiffres non sourcés)
- `_references/04_synthesis.md` PATTERN-1/2/3 (3 patterns transversaux)
- Paths absolus V1 vs V2 empiriques (D1 receipts §2.2)

## 9. Risks + Rollback

### 9.1. Risques identifiés (D6 root-cause)

| # | Risque | Probabilité | Mitigation canon |
|---|---|---|---|
| R1 | Brief générique récidive (V1 honnie redux) | Haute sans Gate B1 #1 | Phase 4 ULTRA-PRESCRIPTIF + 5 specs obligatoires + Gate B1 #1 |
| R2 | Drift procédural (passer des phases) | Moyenne | 3 Gates fixes (B1 #1 + A0 #1 + A0 #2) |
| R3 | Sur-orchestration (méta-process pour redesign mineur) | Moyenne | YAGNI gate §3.2 conditions C1/C2/C3 |
| R4 | A3 sub-agent bloque A2 synchrone | Moyenne | `run_in_background: true` mandatory + monitor async |
| R5 | Landing livrée mais ICP mal ciblé (anti-paperclip) | Faible avec ADR sister | `ADR-NEXUS-LANDING-PERSONAS-001` sister gate A0 #1 |
| R6 | 3 landings convergent vers même esthétique (anti-pattern A6) | Moyenne sans sister canon | Brief ULTRA-PRESCRIPTIF par persona (font + couleur + signature DIFFÉRENCIÉS) |
| R7 | Escalation A0 inutile mid-research | Haute sans ADR | D7 cost-of-escalation + 3 gates fixes |
| R8 | Brief V2 reproduit V1 par erreur | Moyenne | `_screenshots/v2_*.png` ancrés D1 + comparaison côte-à-côte |
| R9 | Sister ADRs HYPOTHÈSE (AESTHETIC/COPY/DESIGN-SYSTEM) non canonisés | Haute sans follow-up | **Action pending** : canoniser `ADR-LANDING-AESTHETIC-001` + `ADR-LANDING-COPY-001` + `ADR-DESIGN-SYSTEM-001` en sister canon avant ratification finale |

### 9.2. Rollback strategy

- **V1 honnie → V2 réussie** : déjà exécuté empiriquement 2026-07-06, screenshots `_screenshots/v2_*.png` sont la preuve D1 de succès. Pas de rollback nécessaire — V1 dans `_TRASH_2026-07-06_v1_horrible/` (D4 append-only).
- **V2 ratifiée → V3 (si nécessaire)** : si Gate A0 #2 retourne REVISE, retour Phase 4 (Brief ULTRA-PRESCRIPTIF) — sister canon §9.1 R1.
- **V2 ratifiée → landing sœur (autre ICP)** : sister canon `ADR-NEXUS-LANDING-PERSONAS-001 §3.1` — 3 landings prioritaires ratifiées, landings suivantes (Amara / Christian) gated outboard 3 cycles verts (PRD §4 verbatim).

### 9.3. ADR-pending actions (post-ratification)

| Action | Responsable | Sister-canon |
|---|---|---|
| Canoniser `ADR-LANDING-AESTHETIC-001` (doctrine esthétique inter-bannie par landing) | B1 E-Myth Gatekeeper | Ce ADR §7 Phase 3 + Phase 6 |
| Canoniser `ADR-LANDING-COPY-001` (copywriting canonique 3 personas) | B1 E-Myth Gatekeeper | Ce ADR §7 Phase 4 S5 |
| Canoniser `ADR-DESIGN-SYSTEM-001` (tokens CSS canoniques) | B1 E-Myth Gatekeeper | Ce ADR §7 Phase 3 |
| Vérifier `dataviz` skill Tier A.3 (canon `ADR-SKILLS-CANON-001 §3`) | B1 E-Myth Gatekeeper | sister canon `ADR-SKILLS-CANON-001` |
| Ratifier ce ADR en `RATIFIED` post-relecture A0 + sister-canon | A0 Amadeus (Jumeau Numérique) | MEMORY.md update |

---

**Sign-off A0 pending.** Ratification attendue après relecture des sister-canon `ADR-WORKFLOW-001` + `ADR-NEXUS-LANDING-PERSONAS-001` + `ADR-ANTI-TEMPLATE-001` + `ADR-ANTI-PAPERCLIP-001` + `ADR-SKILLS-CANON-001` + canonisation des 3 HYPOTHÈSE sister (`AESTHETIC` / `COPY` / `DESIGN-SYSTEM`).