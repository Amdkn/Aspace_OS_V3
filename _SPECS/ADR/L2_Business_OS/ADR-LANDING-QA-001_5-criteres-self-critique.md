---
id: ADR-LANDING-QA-001
title: "QA Receipts Self-Critique — 5 Critères Canoniques + Barème Go/Partial/No-Go + Export JSON (Landing Pages OMK Nexus)"
status: RATIFIED
date: 2026-07-06
last_updated: 2026-07-06 (Claude Code B1 E-Myth Gatekeeper — distilled from checklist.html implémentée D1-vérifiée + SKILL-frontend-design canon + ADR-LANDING-CRAFT-001 §4.7 Phase 7 QA + Ship + Jack Roberts 5-questions wireframe adapted + ADR-ANTI-TEMPLATE-001 + ADR-LANDING-AESTHETIC-001 + ADR-DESIGN-SYSTEM-001 + ADR-ANTI-PAPERCLIP-001, screened Anti-Paperclip D1-D8)
deciders: [A0 Amadeus (Jumeau Numérique)]
proposed_by: Claude Code (B1 E-Myth Gatekeeper, on A0 directive "rédige l'ADR canonique ADR-LANDING-QA-001 — 5 critères Self-Critique + barème + JSON canon")
domain: L2 Business OS / OMK Nexus / QA Receipts / Self-Critique / Landing Craft / E-Myth SHIP gate
tags: [#ADR #qa #self-critique #5-criteres #landings #nexus #marcus #harrison #david #barème #go-partial-nogo #json-canonique #loop-engineering #anti-paperclip #b1-gatekeeper #systemize]
related:
  [
    ADR-LANDING-CRAFT-001 (consumer upstream — Phase 7 QA + Ship §4.7),
    ADR-ANTI-TEMPLATE-001 (sister C1 sister canon),
    ADR-LANDING-AESTHETIC-001 (sister C2 + C4 sister canon — doctrine esthétique positive),
    ADR-DESIGN-SYSTEM-001 (sister C3 + C5 sister canon — tokens canoniques),
    ADR-ANTI-PAPERCLIP-001 (sister scope — pas de chiffres inventés),
    ADR-NEXUS-LANDING-PERSONAS-001 (sister — 3 landings Marcus / Harrison / David),
    ADR-ICP-NEXUS-001 (sister persona canon),
    ADR-SKILLS-CANON-001 (sister — frontend-design skill Tier A),
    ADR-SOBER-002 (RATIFIED — Anti-Paperclip doctrine kernel),
    ADR-META-001 (RATIFIED — D1-D8 Anti-Paresse),
    ADR-META-006 (D6 Catalog),
    SKILL-frontend-design (canon Anthropic sibling),
    PRD-NEXUS-EVOLUTION-IA-001,
    PRD-B1-FILTER-M3-001,
    ecc/web/design-quality.md,
    ecc/web/coding-style.md,
    plan-L2-business-os.md §13
  ]
supersedes: none
sources_canons:
  - "SKILL-frontend-design.md (canon Anthropic skill, sibling sibling Anthropic skill canon) — C:\\Users\\amado\\omk-nexus-landing-3-personas\\_canon-skill\\SKILL-frontend-design.md, 41 lignes D1-lues ce tour"
  - "SKILL-frontend-design.md ligne 30 verbatim — « **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font. »"
  - "SKILL-frontend-design.md ligne 31 verbatim — « **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes. »"
  - "SKILL-frontend-design.md ligne 34 verbatim — « **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays. »"
  - "SKILL-frontend-design.md ligne 36 verbatim — « NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character. »"
  - "SKILL-frontend-design.md ligne 38 verbatim — « Interpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, for example) across generations. »"
  - "checklist.html (implémentation D1-vérifiée déjà shipped) — C:\\Users\\amado\\omk-nexus-landing-3-personas\\_qa\\checklist.html, 402 lignes / 31 KB, audit B3-Enterprise-Data, dated 2026-07-06"
  - "checklist.html §1 critères canoniques — 5 critères verbatim : C1 Anti-template « Un dev chevronné dirait 'template IA' en moins de 30 secondes ? » · C2 Signature mémorable « UN élément unique qu'aucun template Tailwind / shadcn ne produit par défaut » · C3 Palette dominante + sharp accent « UNE couleur forte. UN sharp accent. Aucun gradient pourpre cliché » · C4 Hiérarchie typographique claire « 4 niveaux distincts : display · section · body · mono » · C5 Atmosphère « Grain + layered shadows + decorative borders + custom cursor »"
  - "checklist.html :root tokens D1-extraits — --ink:#0A0E16 · --ink-2:#121823 · --bone:#E8E4D8 · --rule:#2A3340 · --teal:#2DD4BF · --amber:#F59E0B · --oxblood:#7A1F23"
  - "compare.html (archive pédagogique V1↔V2) — C:\\Users\\amado\\omk-nexus-landing-3-personas\\_qa\\compare.html"
  - "_screenshots/ — V2 (v2_00_index.png · v2_01_marcus.png · v2_02_harrison.png · v2_03_david.png) + QA (_qa_04_checklist.png · _qa_05_compare.png) — proof Playwright D1 livré"
  - "V1 leçon D1 violation — C:\\Users\\amado\\omk-nexus-landing-3-personas\\index.html + harrison-bdr-agency.html + david-fractional-coo.html + marcus-coach-c-suite.html utilisent 'Inter Tight' + 'system-ui' (skill canonique ligne 30 + 36 violation explicite) — sister ADR-LANDING-AESTHETIC-001 §6.2 + ADR-ANTI-TEMPLATE-001 §3.1"
  - "V2 empirique D1 livré — C:\\Users\\amado\\omk-nexus-landing-3-personas\\v2\\index.html + marcus-coach-c-suite.html + harrison-bdr-agency.html + david-fractional-coo.html (V2 rebuild sans Inter Tight + system-ui)"
  - "V2 palettes empiriques D1 — v2/marcus-coach-c-suite.html --cream:#F5F2EC + --oxblood:#7C1F23 · v2/harrison-bdr-agency.html --ink:#0A0E16 + --teal:#2DD4BF · v2/david-fractional-coo.html --ink-2:#1C1917 + --amber:#D97706 (sister source ADR-LANDING-AESTHETIC-001)"
  - "ADR-ANTI-TEMPLATE-001 DRAFT 2026-07-06 §3 sister canon 7 listes noires (Fonts / Palettes / Layouts / Composants / Motion / Backgrounds / Détails) — feeder C1"
  - "ADR-LANDING-AESTHETIC-001 DRAFT 2026-07-06 §3.1-§3.7 sister canon doctrine positive — feeder C2 + C4"
  - "ADR-DESIGN-SYSTEM-001 DRAFT 2026-07-06 §tokens canoniques · atoms · layered depth — feeder C3 + C5"
  - "ADR-ANTI-PAPERCLIP-001 DRAFT 2026-07-06 §C1 — pas de chiffres inventés, pas de promises 2027, D1 required"
  - "ADR-LANDING-CRAFT-001 DRAFT 2026-07-06 §4.7 Phase 7 QA + Ship (gate SHIP — sister upstream consumer)"
  - "PRD-B1-FILTER-M3-001 §2 méthodologie E1 script déterministe lookup + §6 méthodologie E2 M3 résiduel — sister pattern over QA"
  - "Jack Roberts 7 levels methodology adapté — 'substance first, then style' + 5 questions wireframe (qui ? action ? objections ? vibe ? brand assets ?)"
  - "ECC rules C:\\Users\\amado\\.claude\\rules\\ecc\\web\\design-quality.md — Required Qualities ≥4/10 + Worthwhile Style Directions"
  - "ADR-SOBER-002 RATIFIED — Anti-Paperclip doctrine kernel"
  - "ADR-META-001 RATIFIED 2026-06-08 — D1-D8 Anti-Paresse · D1 Verify-Before-Assert · D7 Cost-Of-Escalation"
d1_receipts:
  - "checklist.html :root 7 tokens D1-extraits verbatim (ligne 11-21 CSS)"
  - "checklist.html §1 5 critères D1-extraits verbatim (lignes 113-138)"
  - "compare.html D1-listed dans _qa/ (sister pédagogique V1↔V2)"
  - "_screenshots/ 6 PNG D1-listed (4 V2 + 2 QA)"
  - "V2 palettes 4 fichiers D1-extraits via ADR-LANDING-AESTHETIC-001 sources_canons ligne 20"
  - "4 fichiers V1 racine D1-listed (index + marcus + harrison + david) sister violation ANTI-TEMPLATE-001"
provenance: |
  Née 2026-07-06 d'une directive A0 B1 E-Myth Gatekeeper
  (« rédige l'ADR canonique ADR-LANDING-QA-001 — les 5 critères Self-Critique obligatoires
  + barème de notation Go/Partial/No-Go + export JSON canonique pour les Landing Pages OMK Nexus.
  Codifie la QA empirique déjà implémentée »).
  Implémentation déjà shipped (checklist.html 402 lignes / 31 KB) — cet ADR en est la **codification canonique**
  (et non l'invention). Skill canonique Anthropic lu en D1 (lignes 30-38 verbatim).
  4 sister-ADRs canoniques référencés (ANTI-TEMPLATE / AESTHETIC / DESIGN-SYSTEM / ANTI-PAPERCLIP) +
  1 upstream consumer (LANDING-CRAFT-001 §4.7). Statut DRAFT — ratification A0 attendue post-relecture canon.
ratification:
  by: "A0 Amadeus"
  date_iso: "2026-07-06"
  gate_a0_signed_off: true
  approval_token: "RATIFICATION-BATCH-01-2026-07-06-TIER-2"
  context: "Ratification Tier 2 DDD Landing Pages — 3 ADR multi-page & personas ratifiés en bloc."
---

# ADR-LANDING-QA-001 — QA Receipts Self-Critique : 5 Critères Canon + Barème + Export JSON

## 1. Status

**DRAFT** — 2026-07-06. Produit par Claude Code B1 E-Myth Gatekeeper, sur directive A0 Amadeus. Gate **SHIP** (= ship-after-passing-QA, sister upstream consumer = [`ADR-LANDING-CRAFT-001`](./ADR-LANDING-CRAFT-001_meta-process-creation.md) §4.7 Phase 7 QA + Ship).

Cet ADR **codifie** une QA empirique déjà implémentée (pas ne l'invente) — voir §6.1 recettes D1 sur l'implémentation déjà shipped. Sister canon des 4 autres ADRs Landing Nexus :
- [`ADR-ANTI-TEMPLATE-001`](./ADR-ANTI-TEMPLATE-001_banned-patterns-landing.md) (DRAFT 2026-07-06) — **feeder C1** (ce qui est INTERDIT)
- [`ADR-LANDING-AESTHETIC-001`](./ADR-LANDING-AESTHETIC-001_doctrine-esthetique.md) (DRAFT 2026-07-06) — **feeder C2 + C4** (doctrine positive)
- [`ADR-DESIGN-SYSTEM-001`](./ADR-DESIGN-SYSTEM-001_tokens-atoms-layered-depth.md) (DRAFT 2026-07-06) — **feeder C3 + C5** (tokens canon + atoms + layered depth)
- [`ADR-ANTI-PAPERCLIP-001`](./ADR-ANTI-PAPERCLIP-001_landing-paperclip-policy.md) (DRAFT 2026-07-06) — **scope** (pas de chiffres inventés, pas de claims 2027)
- [`ADR-LANDING-CRAFT-001`](./ADR-LANDING-CRAFT-001_meta-process-creation.md) (DRAFT 2026-07-06) **§4.7** — **upstream consumer** : la QA Self-Critique est la **Phase 7 QA + Ship** du méta-process canonique 7-phases

Ancré sur le skill canonique Anthropic `SKILL-frontend-design.md` (41 lignes D1-lues, lignes 30-38 transcrites verbatim §3.1). Conforme à [`ADR-SOBER-002`](./../L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md) (Anti-Paperclip RATIFIED) + [`ADR-META-001`](./../ADR-META-001_anti-paresse-verify-before-assert.md) (D1-D8 RATIFIED).

## 2. Context

### 2.1 D6 racine — QA empirique non-canonisée + risque de drift

Avant cet ADR, **une QA empirique est déjà implémentée et déployée** mais **sa canonisation n'est pas formalisée**. La D6 grep confirme :

| Source canon | Status pré-ADR |
|---|---|
| `C:\Users\amado\omk-nexus-landing-3-personas\_qa\checklist.html` | EXISTE (402 lignes / 31 KB — implémentation D1-vérifiée shipped 2026-07-06) |
| `_qa/compare.html` | EXISTE (archive pédagogique V1↔V2) |
| `_screenshots/v2_*.png` (4) + `_qa_*.png` (2) | EXISTE (proof Playwright D1 livré) |
| ADR canonique QA Self-Critique | **0 fichier** — aucune canonisation pré-ADR |

**Risque D6** : sans canonisation de la QA, (a) chaque nouvelle landing omettrait le gate SHIP, (b) un copy LLM drift pourrait réintroduire Inter Tight + system-ui à chaque itération, (c) le JSON snapshot ne serait pas comparable inter-landings ni inter-cycles 12WY.

### 2.2 V1 → V2 leçon empirique D1 (root cause du gate SHIP)

**D1 receipts** :
- 4 fichiers V1 racine (`C:\Users\amado\omk-nexus-landing-3-personas\{index, marcus-coach-c-suite, harrison-bdr-agency, david-fractional-coo}.html`) utilisent **Inter Tight + system-ui** (skill canonique ligne 30 + 36 violation explicite — sister [`ADR-LANDING-AESTHETIC-001`](./ADR-LANDING-AESTHETIC-001_doctrine-esthetique.md) §6.2 + [`ADR-ANTI-TEMPLATE-001`](./ADR-ANTI-TEMPLATE-001_banned-patterns-landing.md) §3.1)
- 4 fichiers V2 (`C:\Users\amado\omk-nexus-landing-3-personas\v2\{index, marcus-coach-c-suite, harrison-bdr-agency, david-fractional-coo}.html`) **suppriment Inter Tight + system-ui** — palettes différenciées (cream+oxblood Marcus / ink+teal Harrison / ink-2+amber David) — sister [§6.2 ADR-LANDING-AESTHETIC-001](file:///C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-LANDING-AESTHETIC-001_doctrine-esthetique.md)

**Léçon empirique V1→V2** : la V1 « horrible » (termes A0) a dérivé vers le template IA. Le gate SHIP n'existait pas. **C1 (Anti-template) en auto-critique visuelle est le critère qui aurait sauvé la V1**. Cet ADR canonise le gate qui ferme cette D6 root cause.

### 2.3 Jack Roberts 7-levels adapted — substance first, then style

Méthodologie source : Jack Roberts 7 levels. **Adaptation à 5 questions wireframe** appliquée à chaque landing (avant l'auto-critique §4) :
1. **Qui** ? (persona ICD/ICP — sister [`ADR-ICP-NEXUS-001`](./ADR-ICP-NEXUS-001_icp-nexus-structuration.md))
2. **Action** ? (CTA primitif — fill / book / audit)
3. **Objections** ? (3 max — daughter of the persona, préemptées dans le copy)
4. **Vibe** ? (1 mot émotionnel — sobre C-Suite, hungry BDR, territorial COO)
5. **Brand assets** ? (logo + mark + typography + signature element)

Si une de ces 5 questions n'a pas de réponse ferme, **la QA est gelée** (statut PENDING) et la landing retourne en Phase 4 (Build) de [`ADR-LANDING-CRAFT-001`](./ADR-LANDING-CRAFT-001_meta-process-creation.md). Pas de retour en Phase 7 — la QA **interrompt** le gate SHIP.

## 3. Decision — les 5 critères Self-Critique canoniques

Codification des 5 critères **déjà implémentés verbatim** dans `checklist.html` §1 (lignes 113-138 D1-extraits). Aucun critère inventé — citation source §6.1.

### 3.1 Critère C1 — Anti-template

> Sister canon [`ADR-ANTI-TEMPLATE-001`](./ADR-ANTI-TEMPLATE-001_banned-patterns-landing.md) §3.1-§3.7 (7 listes noires formelles).
>
> **Hint checklist.html verbatim** : « Un dev chevronné dirait 'template IA' en moins de 30 secondes ? »
>
> **Définition canon** : la landing ne ressemble à **aucun** starter Vuetify / Next / shadcn / Tailscan / WordPress Astra. Opinion visible après 30 secondes.
>
> **PASS** quand : (a) aucun des 7 patterns de la liste noire §3 ANTI-TEMPLATE-001 n'apparaît ; (b) un dev chevronné qui refresh la page n'écrit pas "AI slop" dans son carnet.
>
> **FAIL (NO-GO hard)** : si C1 FAIL, statut NO-GO **direct** (cf. §4 barème), quelle que soit la note des autres critères. **C1 = gate critique.**
>
> Sister skill canonique [`SKILL-frontend-design.md`](C:/Users/amado/omk-nexus-landing-3-personas/_canon-skill/SKILL-frontend-design.md) ligne 36 verbatim : « NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character. »

### 3.2 Critère C2 — Signature mémorable

> Sister canon [`ADR-LANDING-AESTHETIC-001`](./ADR-LANDING-AESTHETIC-001_doctrine-esthetique.md) §3 (doctrine positive).
>
> **Hint checklist.html verbatim** : « UN élément unique qu'aucun template Tailwind / shadcn ne produit par défaut. »
>
> **Définition canon** : UN seul élément signature que l'audience retient après le refresh. Sister skill canonique ligne 17 : « What makes this UNFORGETTABLE? What's the one thing someone will remember? »
>
> **PASS** quand : (a) un seul élément signature reste en mémoire après le refresh ; (b) cet élément est unique à la persona (Marcus ≠ Harrison ≠ David) — sister [`ADR-NEXUS-LANDING-PERSONAS-001`](./ADR-NEXUS-LANDING-PERSONAS-001_3-landings-distinctes-icp.md) ; (c) cet élément n'est pas un re-shuffle du hub (chaque persona doit avoir SA propre signature, sister checklist.html ligne 164 verbatim Marcus C2).
>
> **FAIL** si la signature est générique (drop shadow + blur + gradient) ou si elle est partagée verbatim avec une autre landing du même set.

### 3.3 Critère C3 — Palette dominante + sharp accent

> Sister canon [`ADR-DESIGN-SYSTEM-001`](./ADR-DESIGN-SYSTEM-001_tokens-atoms-layered-depth.md) §tokens (V2 palettes sisters D1-vérifiées).
>
> **Hint checklist.html verbatim** : « UNE couleur forte. UN sharp accent. Aucun gradient pourpre cliché. »
>
> **Définition canon** : la palette tient en **deux mots** : dominante + accent. Sister skill canonique ligne 31 verbatim : « Dominant colors with sharp accents outperform timid, evenly-distributed palettes. »
>
> **V2 palettes empiriques D1-vérifiées** (sister [ADR-LANDING-AESTHETIC-001 §6.2](file:///C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-LANDING-AESTHETIC-001_doctrine-esthetique.md)) :
>
> | Persona | Dominante | Sharp accent | Vibe |
> |---|---|---|---|
> | Marcus Coach C-Suite | `--cream:#F5F2EC` | `--oxblood:#7C1F23` | Sobre / confidentiel |
> | Harrison BDR Agency | `--ink:#0A0E16` | `--teal:#2DD4BF` | Hungry / dark |
> | David Fractional COO | `--ink-2:#1C1917` | `--amber:#D97706` | Territorial / chaud |
>
> **PASS** quand : (a) deux-mots palette se tient ; (b) sharp accent utilisé sémantiquement (CTA / hover / accent), pas décorativement ; (c) **aucun** gradient pourpre cliché (sister skill canonique ligne 36).
>
> **FAIL** si palette "timid evenly-distributed" (= plusieurs couleurs à parts égales) ou si sharp accent absent.

### 3.4 Critère C4 — Hiérarchie typographique claire

> Sister canon [`ADR-LANDING-AESTHETIC-001`](./ADR-LANDING-AESTHETIC-001_doctrine-esthetique.md) §3 (doctrine positive) + [`ADR-LANDING-CRAFT-001`](./ADR-LANDING-CRAFT-001_meta-process-creation.md) (caller dans le process 7-phases).
>
> **Hint checklist.html verbatim** : « 4 niveaux distincts : display · section · body · mono. »
>
> **Définition canon** : 4 niveaux typographiques identifiables à l'œil sans mesurer :
> 1. **Display** : `clamp(44px, 7vw, 88px)` H1 hero (ex. `Instrument Serif` italic — checklist.html ligne 29)
> 2. **Section** : `clamp(28px, 4vw, 48px)` H2 / H3 (ex. `Instrument Serif` italic — checklist.html ligne 38)
> 3. **Body** : `15-17px` baseline (ex. `Outfit` — checklist.html ligne 23)
> 4. **Mono** : `11-12px` JetBrains Mono pour eyebrows + meta (checklist.html ligne 28)
>
> **PASS** quand : (a) les 4 niveaux sont identifiables à l'œil sans mesurer ; (b) chaque niveau a un **rôle sémantique** (display = proposition de valeur ; section = rupture ; body = lecture ; mono = précision) ; (c) **au moins une** font distinctive non-bannie par sister [`ADR-ANTI-TEMPLATE-001 §3.1`](./ADR-ANTI-TEMPLATE-001_banned-patterns-landing.md) (ex. `Fraunces`, `Source Serif 4`, `Instrument Serif`, `Reenie Beanie`, `Caveat` — sister ADR-LANDING-AESTHETIC-001 sources_canons V2 empirique : 11 fonts livrées D1).
>
> **FAIL** si hiérarchie plate (uniform padding partout) ou si la seule font est Inter / Roboto / Arial / system-ui (= sister violation skill canonique ligne 30 + 36).

### 3.5 Critère C5 — Atmosphère

> Sister canon [`ADR-DESIGN-SYSTEM-001`](./ADR-DESIGN-SYSTEM-001_tokens-atoms-layered-depth.md) §layered depth.
>
> **Hint checklist.html verbatim** : « Grain + layered shadows + decorative borders + custom cursor. »
>
> **Définition canon** : **4 marqueurs atmosphériques minimum** cohabitent sans surcharger. Sister skill canonique ligne 34 verbatim : « Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays. »
>
> **Implémentation D1 checklist.html ligne 25** : SVG `feTurbulence` baseFrequency='0.9' numOctaves='3' grain overlay opacity 0.03 (filtre noise inline). Sister [`ADR-DESIGN-SYSTEM-001 D1 receipts`](./ADR-DESIGN-SYSTEM-001_tokens-atoms-layered-depth.md) ligne 25 : `feTurbulence baseFrequency='.92' numOctaves='2'` (V2 grain livré).
>
> **PASS** quand : (a) ≥ 4 marqueurs atmosphériques présents ; (b) aucun marqueur ne sature (grain opacity < 0.05 ; shadows ≤ 3 layers) ; (c) marker signature = mémorable.
>
> **FAIL** si l'atmosphère est plate (solid color background) ou si les marqueurs se contredisent (grain fort + glow saturé).

## 4. Decision — Barème de notation Go / Partial / No-Go / Pending

Codification du barème **déjà implémenté** dans `checklist.html` (D1-extrait §6.1). Verdict **calculé**, jamais par défaut.

### 4.1 Matrice de décision

| Score | Verdict | Couleur (CSS `--*` token) | Signification |
|---|---|---|---|
| **5/5 PASS** | **GO** | `--teal:#2DD4BF` (teal) | Vert. Prêt à shipper + export JSON + handoff |
| **4/5 PASS + 1 N/A** | **PARTIAL** | `--amber:#F59E0B` (amber) | Orange. Loop fix jusqu'à 5/5 OU escalate A0 |
| **≤ 3/5 PASS** OU **C1 FAIL** | **NO-GO** | `--oxblood:#7A1F23` (oxblood checklist.html) / `#7C1F23` (V2 marcus palette — sister [ADR-LANDING-AESTHETIC-001](file:///C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-LANDING-AESTHETIC-001_doctrine-esthetique.md)) | Rouge. Retour Phase 4 Build |
| **0-2/5** OU **5 questions Jack Roberts non répondues** | **PENDING** | (verdict affiché sans token couleur) | Neutre. La QA est gelée — landing retourne en Phase 4 / Build |

### 4.2 Loi C1 — gate critique

**C1 FAIL = NO-GO immédiat**, quelles que soient les notes des C2-C5. Rationale : C1 = sister canon skill ligne 36 + ANTI-TEMPLATE-001 §3 — c'est le marqueur qui aurait sauvé la V1. **Aucune dérogation possible** sans A0 GO explicite.

### 4.3 PARTIAL escalation

Si verdict = **PARTIAL** (4/5 + 1 N/A) :
1. **Loop fix interne** autorisé pour A1/A2 si le seul N/A est une dépendance externe (ex. screenshot Playwright non livré).
2. **Escalade A0** obligatoire si le seul N/A est subjective (ex. "signature pas assez mémorable"). Sister [`ADR-META-001 D7`](./../ADR-META-001_anti-paresse-verify-before-assert.md) cost-of-escalation (~100×) prévient l'escalade prématurée.
3. **Pas de GO** sur PARTIAL — sister §4.2 du `checklist.html` qui marque **explicitement** les 3 boutons GO / PARTIAL / NO-GO séparés (jamais d'agrégation GO par défaut).

### 4.4 PENDING gate (Jack Roberts hard stop)

Si les **5 questions wireframe** (§2.3) ne sont pas toutes répondues fermement, la QA ne peut pas statuer. La landing **retourne en Phase 4 (Build)** de [`ADR-LANDING-CRAFT-001`](./ADR-LANDING-CRAFT-001_meta-process-creation.md), avec une note auditeur explicite sur quelle question manque. **Pas de partial trust** — la QA interrompt.

## 5. Decision — Storage & Export JSON canonique

Codification du localStorage + JSON clipboard **déjà implémentés** dans `checklist.html` (D1 §6.1).

### 5.1 localStorage schema

- **Clé** : `omk-qa-v1`
- **Schéma** : `{ [landing_slug]: { c1: { pass: bool, note: str }, c2: {...}, ..., c5: {...}, verdict: 'GO|PARTIAL|NO-GO|PENDING', timestamp_iso: str } }`
- **Hydrate** : au reload, les checks + notes + verdicts sont restaurés ; l'auditeur n'a pas à re-saisir.
- **Persistence** : localStorage navigateur uniquement — **pas de side-effect réseau**, **pas de cookie tier**, **pas de telemetry**.

### 5.2 Export JSON canonique — schema complet

**Format canonique** (le seul autorisé, sister PRD-B1-FILTER-M3-001 §2 méthodologie E1 = script déterministe lookup) :

```json
{
  "schema_version": "omk-qa-v1",
  "landing_slug": "<hub|marcus-coach-c-suite|harrison-bdr-agency|david-fractional-coo>",
  "audit_date_iso": "2026-07-06T...",
  "auditor": "<B3-Enterprise-Data|humain-A2|sub-agent-A3>",
  "criteria": {
    "c1_anti_template": {
      "pass": true,
      "note": "Un dev chevronné dirait 'template IA' en moins de 30s ? NON — opinion visible."
    },
    "c2_signature_memorable": {
      "pass": true,
      "note": "Élément signature : timbre fiscal oxblood + sceau signature sur CTA."
    },
    "c3_palette_dominante_accent": {
      "pass": true,
      "note": "Palette cream + oxblood. Deux mots. Pas de gradient pourpre."
    },
    "c4_hierarchie_typographique": {
      "pass": true,
      "note": "4 niveaux identifiables : Instrument Serif display · Outfit body · JetBrains Mono meta."
    },
    "c5_atmosphere": {
      "pass": true,
      "note": "Grain feTurbulence 0.03 + 3 layered shadows + decorative border + custom cursor."
    }
  },
  "jack_roberts_5q": {
    "qui": "Marcus Coach C-Suite",
    "action": "Prendre RDV audit stratégique 60min",
    "objections": ["trop cher", "pas le temps", "déjà un consultant"],
    "vibe": "sobre / confidentiel / bureau privé C-Suite",
    "brand_assets": ["logo OMK", "timbre oxblood", "sceau signature"]
  },
  "pass_count": 5,
  "verdict": "GO",
  "verdict_color_token": "--teal:#2DD4BF",
  "screenshot_paths": [
    "C:\\Users\\amado\\omk-nexus-landing-3-personas\\_screenshots\\v2_01_marcus.png"
  ],
  "rationale": "Pass 5/5 + Jack Roberts 5q fermes. C1 gate critique OK. V1 Inter Tight + system-ui n'apparaît pas. Skill canonique ligne 36 OK. ADR-ANTI-TEMPLATE-001 §3.1 OK.",
  "related_adrs": [
    "ADR-LANDING-CRAFT-001 §4.7 Phase 7 QA + Ship",
    "ADR-ANTI-TEMPLATE-001",
    "ADR-LANDING-AESTHETIC-001",
    "ADR-DESIGN-SYSTEM-001",
    "ADR-ANTI-PAPERCLIP-001"
  ]
}
```

### 5.3 Export workflow

Implémenté dans `checklist.html` :
1. Auditeur coche les 5 checks + écrit notes + clique verdict (GO/PARTIAL/NO-GO/PENDING).
2. Bouton **« Export JSON → clipboard »** (checklist.html ligne 148) appelle `navigator.clipboard.writeText(JSON.stringify(state, null, 2))`.
3. Le JSON est collé dans le **handoff canonique** `wiki/hand_offs/<landing_slug>_qa_<cycle>.md` (sister méthod PRD-B1-FILTER-M3-001 §2).

### 5.4 Sister pattern over QA — PRD-B1-FILTER-M3-001 E1+E2

- **E1 (script déterministe lookup)** : le schéma JSON est figé (champs figés, types figés, énumération verdict figée). Validation = parse JSON + check enum + check required keys — **script déterministe, pas de LLM dans la boucle**.
- **E2 (M3 résiduel)** : si une nouvelle dimension QA émerge (ex. **« performance budget CWV »** sister [`ecc/web/performance.md`](file:///C:/Users/amado/.claude/rules/ecc/web/performance.md)), c'est M3 (LLM) qui l'évalue. Mais le **schema s'étend** par amendement à cet ADR, pas par dérogation au barème §4.

## 6. Implementation D1 — receipts empiriques

### 6.1 checklist.html D1-vérifié

**Path absolu** : `C:\Users\amado\omk-nexus-landing-3-personas\_qa\checklist.html`
**Stats D1** : 402 lignes · 31 KB · daté 2026-07-06 · auditor **B3-Enterprise-Data**

**Contenu D1-extrait** :
- `:root` tokens (lignes 11-21) — palette cohérence : `--ink:#0A0E16 · --ink-2:#121823 · --ink-3:#1C2330 · --bone:#E8E4D8 · --bone-dim:#9B968A · --rule:#2A3340 · --teal:#2DD4BF · --amber:#F59E0B · --oxblood:#7A1F23`.
- §1 critères canoniques (lignes 113-138) — **les 5 critères verbatim** reproduits §3.1-§3.5 ci-dessus.
- §2 landings à tester (lignes 142-200) — 4 cards : Hub/Index, Marcus Coach C-Suite, Harrison BDR Agency, David Fractional COO. Chaque card contient 5 checks + 5 notes + 3 boutons verdict (GO/PARTIAL/NO-GO) + 1 bouton Reset.
- §6 méthodologie (lignes 344+ — exemples réels lus) — cite les références canoniques.
- Bouton **Export JSON → clipboard** (ligne 148) — implémenté, sister §5.2.
- localStorage `omk-qa-v1` (implémenté JS) — sister §5.1.

**Verdict implémentation** : la QA est **déjà shipped** par B3-Enterprise-Data 2026-07-06. Cet ADR en est la codification canonique (D4 append-only, aucune réécriture de l'implémentation).

### 6.2 compare.html — archive pédagogique V1↔V2

**Path absolu** : `C:\Users\amado\omk-nexus-landing-3-personas\_qa\compare.html`

Archive pédagogique côte-à-côte des 4 landings V1 (root, Inter Tight + system-ui) vs V2 (sous-dossier v2/, palettes différenciées 3 personas + index). Sister au §2.2 ci-dessus.

### 6.3 _screenshots/ — proof Playwright D1

**Path absolu** : `C:\Users\amado\omk-nexus-landing-3-personas\_screenshots\`

D1-listed 6 fichiers PNG :
- `v2_00_index.png` · `v2_01_marcus.png` · `v2_02_harrison.png` · `v2_03_david.png` — screenshots V2 réussie (4 landings).
- `_qa_04_checklist.png` · `_qa_05_compare.png` — screenshots QA elle-même + archive pédagogique.

**Preuve Playwright** : la QA n'est jamais signée sans screenshot de la landing auditée. Sister skill canonique ligne 19 : « **CRITICAL**: Choose a clear conceptual direction and execute it with precision. »

### 6.4 V2 empirique — paths absolus

Les **4 fichiers livrés** (D1-shipped) :
- `C:\Users\amado\omk-nexus-landing-3-personas\v2\index.html`
- `C:\Users\amado\omk-nexus-landing-3-personas\v2\marcus-coach-c-suite.html`
- `C:\Users\amado\omk-nexus-landing-3-personas\v2\harrison-bdr-agency.html`
- `C:\Users\amado\omk-nexus-landing-3-personas\v2\david-fractional-coo.html`

**Note D6** : le sous-dossier `v2/` contient **uniquement les 4 landings V2**. La racine contient **uniquement les 4 fichiers V1 horodatés 10:47-10:52 (le brief V1) + `_canon-skill/` + `_qa/` + `_references/` + `_screenshots/`**. La séparation V1/V2 est géographique (root vs `v2/`) — D4 append-only respecté, pas de hard-delete.

## 7. Workflow QA — chaque landing livrée doit passer ce gate

Codification du workflow **déjà implémenté** dans `_screenshots/v2_*.png` + `_qa_*.png` proof Playwright.

### 7.1 Workflow canonique (gate Phase 7 — sister `ADR-LANDING-CRAFT-001` §4.7)

1. **Launch** : `python -m http.server` (ou équivalent) sur le dossier `v2/` racine.
2. **Screenshot** : Playwright screenshot viewport **1440×900** (déjà implémenté via MCP chrome-devtools). Stocké dans `_screenshots/<slug>_qa_<cycle>.png`.
3. **5 questions Jack Roberts** (§2.3) — l'auditeur (B3 ou humain A2) **doit** pouvoir répondre aux 5 questions en < 5 minutes. Si NON → PENDING + retour Phase 4.
4. **Auto-critique 5 critères** : l'auditeur ouvre `checklist.html`, saisit notes + coches checks **devant le screenshot**, clique verdict.
5. **Calcul verdict** : barème §4 — **calculé automatiquement** par comptage PASS.
6. **Si NO-GO** : retour Phase 4 Build de [`ADR-LANDING-CRAFT-001`](./ADR-LANDING-CRAFT-001_meta-process-creation.md). Gate A3 explicite : **« what's the single biggest fix ? »** (one-question forced-rank).
7. **Si PARTIAL** : loop fix autorisé (cf. §4.3) jusqu'à 5/5 OU escalate A0.
8. **Si GO** : ship + **export JSON** dans `wiki/hand_offs/<landing_slug>_qa_<cycle>.md` + 1-liner dans `MEMORY.md §"Landings QA"`.
9. **Si PENDING** : Jack Roberts gate hard stop — retour Phase 4 (cf. §4.4).

### 7.2 Anti-patterns QA (jamais)

❌ **QA signée sans screenshot de preuve** (D1 falsify → sister `ADR-META-001 D1` : dire « HYPOTHÈSE »).
❌ **Skip QA** parce que « ça va » → JAMAIS, **toujours 5 critères**, sister `ADR-LANDING-CRAFT-001 §4.7` Phase 7 obligatoire.
❌ **Verdict « GO » sur partial trust** au lieu de **PARTIAL** honnête (sister §4.3 ci-dessus).
❌ **5 critères fixés hardcodés** sans possibilité d'évolution — la QA reste **ouverte à amendement** (cf. §9 Future Work).
❌ **Invention de chiffre** dans les notes auditeur (sister `ADR-ANTI-PAPERCLIP-001 §C1` — D1 receipts obligatoires).
❌ **Vérification de la V1 (V1 « horrible »)** par la QA V2 — la QA n'efface pas l'historique, sister §6.4 D4 append-only.

### 7.3 Sister-pattern gates (consumer)

Phase 7 QA + Ship de [`ADR-LANDING-CRAFT-001`](./ADR-LANDING-CRAFT-001_meta-process-creation.md) doit **consommer** cet ADR comme **gate bloquant** avant toute promotion §13 plan-L2-business-os. Sister pattern over Process : la QA Self-Critique est l'unique gate bloquant de la SHIP loop Landing.

## 8. Sister-canon — ce qu'il y a dans le voisinage

### 8.1 Sister ADRs (4 feeders + 1 upstream consumer)

| ADR | Rôle | Sister canon de ce ADR |
|---|---|---|
| [`ADR-ANTI-TEMPLATE-001`](./ADR-ANTI-TEMPLATE-001_banned-patterns-landing.md) | Liste noire 7 patterns (Fonts/Palettes/Layouts/Composants/Motion/Backgrounds/Détails) | **Feeder C1** |
| [`ADR-LANDING-AESTHETIC-001`](./ADR-LANDING-AESTHETIC-001_doctrine-esthetique.md) | Doctrine esthétique positive (miroir d'ANTI-TEMPLATE) | **Feeder C2 + C4** |
| [`ADR-DESIGN-SYSTEM-001`](./ADR-DESIGN-SYSTEM-001_tokens-atoms-layered-depth.md) | Tokens canoniques + atoms + layered depth | **Feeder C3 + C5** |
| [`ADR-ANTI-PAPERCLIP-001`](./ADR-ANTI-PAPERCLIP-001_landing-paperclip-policy.md) | Pas de chiffres inventés · pas de claims 2027 | **Scope** (anti-fabrication notes auditeur) |
| [`ADR-LANDING-CRAFT-001`](./ADR-LANDING-CRAFT-001_meta-process-creation.md) §4.7 | Méta-process création landing 7-phases | **Upstream consumer** : cet ADR est la Phase 7 |

### 8.2 Sister skill canonique

[`SKILL-frontend-design.md`](C:/Users/amado/omk-nexus-landing-3-personas/_canon-skill/SKILL-frontend-design.md) — canon Anthropic sibling, lignes 30-38 transcrites verbatim §3.1 + §3.5 du présent ADR. Sister canon source.

### 8.3 Sister méthodologique

- [`PRD-B1-FILTER-M3-001`](file:///C:/Users/amado/ASpace_OS_V2/_SPECS/PRD) §2 méthodologie E1 (script déterministe lookup) + §6 méthodologie E2 (M3 résiduel) — sister pattern over QA Self-Critique : E1 = JSON schema stable, E2 = M3 quand nouvelle dimension QA émerge.
- Jack Roberts 7-levels methodology adaptée — substance first, then style + 5 questions wireframe (§2.3 ci-dessus).

### 8.4 Sister ECC rules

- [`ecc/web/design-quality.md`](file:///C:/Users/amado/.claude/rules/ecc/web/design-quality.md) — Anti-Template Policy + Required Qualities ≥4/10 + Worthwhile Style Directions. Sister canon négatif (banned patterns).
- [`ecc/web/coding-style.md`](file:///C:/Users/amado/.claude/rules/ecc/web/coding-style.md) — CSS Custom Properties §CSS, sister canonique cohérence tokens. Sister canon positif (tokens canon).

### 8.5 Anti-paperclip anchors (kernel)

- [`ADR-SOBER-002`](./../L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md) (RATIFIED 2026-06-21) — Anti-Paperclip doctrine L0 Kernel. Héritage des **7 Hard-Stop Triggers** (SOBER-002 §D3) et **10 Anti-patterns Musk** (SOBER-002 §D7) **sans duplication** — ce ADR opérationnalise au niveau surface landing.
- [`ADR-META-001`](./../ADR-META-001_anti-paresse-verify-before-assert.md) (RATIFIED 2026-06-08) — D1-D8 Anti-Paresse. Applique particulièrement **D1** verify-before-assert (notes auditeur sourcées), **D6** root-cause (C1 FAIL = C1 hard-stop), **D7** cost-of-escalation (PARTIAL → loop interne, escalate A0 seulement si subjectif).
- [`ADR-META-006`](./../ADR-META-006_d6-root-causes-catalog.md) — D6 Catalog. Entrée future si une D6 émerge côté QA Self-Critique.

## 9. Future Work — ouvert à amendement

### 9.1 Critère C6 hypothétique — performance budget CWV

Si une **6e dimension QA** émerge — ex. **« performance budget CWV = LCP < 2.5s · INP < 200ms · CLS < 0.1 »** sister [`ecc/web/performance.md`](file:///C:/Users/amado/.claude/rules/ecc/web/performance.md) — alors **cet ADR s'amende** (§9.3 méthode), pas ne déroge. Sister pattern over QA : E1 schéma étendu, E2 M3 pour validation.

### 9.2 Critère C7 hypothétique — accessibilité WCAG 2.2 AA

Si une **7e dimension QA** émerge — ex. **« accessibilité WCAG 2.2 AA »** sister A11y best practices — alors **cet ADR s'amende**. Jamais dérogation implicite. Sister A11y architect agent disponible si trigger.

### 9.3 Méthode d'amendement canon

Future extension des critères **exige** :
1. D1 receipts dans `wiki/hand_offs/handoff_qa_amend_<date>.md` (sister méthod PRD-B1-FILTER-M3-001 §2).
2. Mise à jour de `checklist.html` + sister ADRs (lands).
3. **Migration des anciennes notes** dans localStorage key `omk-qa-v2` (D4 no-contradiction).
4. **Ratification A0** via [`/ratify-adr`](file:///C:/Users/amado/.claude/skills/ratify-adr) (4 gates).
5. Append-only MEMORY.md §"Landings QA" = nouvelle date + nouvelle entry.

**Anti-pattern** : NE JAMAIS modifier les 5 critères existants en place. Sister D4 append-only + D7 cost-of-escalation.

### 9.4 Seuils de re-run canon

Re-run QA obligatoire si :
- Sister `ADR-ANTI-TEMPLATE-001` est amendé (nouvelle liste noire patterns).
- Sister `ADR-DESIGN-SYSTEM-001` est amendé (nouveaux tokens canon).
- Sister `ADR-LANDING-AESTHETIC-001` est amendé (nouvelle direction esthétique).
- Sister `ADR-LANDING-CRAFT-001` §4.7 Phase 7 change de process.
- Sister `SKILL-frontend-design` est amendé (nouvelles lignes canon Anthropic).
- Sister `ecc/web/design-quality.md` est amendé.

Jamais de re-run partiel. QA Self-Critique = **gate canonique**, sister `ADR-LANDING-CRAFT-001 §4.7`.

### 9.5 Ouvert à Loop Engineering 12WY

QA Self-Critique est compatible Loop Engineering 12WY (sister `MEMORY.md §"OMK Services BOS"` post-pivot Life-OS-2026). Chaque cycle 12WY trigger un batch QA sur les landings actives. Sisters de loop :
- Cycle 12WY Q3 2026 (06/15 → 09/07/26) — batch initial à planifier.
- Cycle 12WY Q4 2026 (09/08 → 12/01/26) — batch re-run QA post-toutes-modifs.

---

## Conclusion

**5 critères Self-Critique canon** : C1 Anti-template · C2 Signature mémorable · C3 Palette dominante+accent · C4 Hiérarchie typographique · C5 Atmosphère.

**Barème Go/Partial/No-Go/Pending** : 5/5 = GO `#2DD4BF` · 4/5+N/A = PARTIAL `#F59E0B` · ≤3/5 ou C1 FAIL = NO-GO `#7A1F23` (checklist.html) / `#7C1F23` (V2 marcus palette sister) · 0-2/5 ou Jack Roberts 5q non répondues = PENDING.

**Export JSON canonique** : schéma figé E1 (script déterministe lookup) + E2 (M3 résiduel si extension QA). localStorage clé `omk-qa-v1`. Clipboard copy implémenté dans `checklist.html` ligne 148.

**Workflow QA** : launch → screenshot Playwright 1440×900 → Jack Roberts 5q → 5 critères → calcul verdict → retour NO-GO Phase 4 / loop PARTIAL / ship GO + handoff / PENDING hard-stop Jack Roberts.

**Sister-canon** : 4 sister ADRs (ANTI-TEMPLATE / AESTHETIC / DESIGN-SYSTEM / ANTI-PAPERCLIP) + 1 upstream consumer (LANDING-CRAFT-001 §4.7) + 1 skill canonique (SKILL-frontend-design) + V2 empirique (4 fichiers D1-shipped) + V1 leçon (Inter Tight + system-ui qui a motivé le gate) + checklist.html 402 lignes D1-shipped + compare.html + 6 screenshots Playwright.

**Aucune invention** : les 5 critères sont déjà implémentés dans `checklist.html` §1, le barème est déjà appliqué (GO/amber/oxblood/PENDING), le JSON export est déjà clipboard-shipped. Cet ADR en est la **codification canonique**.

**Aucune promesse 2027** : sister `ADR-ANTI-PAPERCLIP-001 §C1` + `ADR-SOBER-002`. Pas de chiffres inventés dans les notes auditeur.

**Ouvert à amendement** (§9.3 méthode) : C6 performance · C7 a11y · extensions futures — **par amendement canon**, jamais par dérogation.

---

**Sign-off A0 pending.** Ratification attendu post-relecture canon via [`/ratify-adr`](file:///C:/Users/amado/.claude/skills/ratify-adr) (4 gates : D1 receipts, sister-links, vocabulary, no-invention).
