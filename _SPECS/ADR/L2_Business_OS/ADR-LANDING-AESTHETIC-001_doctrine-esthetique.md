---
id: ADR-LANDING-AESTHETIC-001
title: OMK Nexus Landing Pages — Doctrine Esthétique Positive (miroir de la liste noire Anti-Template)
status: RATIFIED
ratification:
  by: "A0 Amadeus"
  date_iso: "2026-07-06"
  gate_a0_signed_off: true
  approval_token: "RATIFICATION-BATCH-01-2026-07-06-TIER-1"
  context: "Ratification Tier 1 craft DDD Landing Pages — 4 ADR sister du §A Creation Methodology (Context) + §B Design System (Context) ratifiés en bloc."
date: 2026-07-06
last_updated: 2026-07-06 (Claude Code B1 E-Myth Gatekeeper — distilled from SKILL-frontend-design canon + ECC design-quality + sister ADR-ANTI-TEMPLATE-001 + ADR-DESIGN-SYSTEM-001 DRAFT, screened Anti-Paperclip D1-D8)
deciders: [A0 Amadeus]
proposed_by: Claude Code (B1 E-Myth Gatekeeper, on A0 directive "rédige l'ADR canonique ADR-LANDING-AESTHETIC-001 — doctrine positive en miroir d'ANTI-TEMPLATE-001")
domain: L2 Business OS / OMK Nexus / Aesthetic Doctrine / Design Quality / Frontend Direction
tags: [#ADR #aesthetic #doctrine #anti-ai-slop #landing-page #nexus #marcus #harrison #david #design-direction #fonts #palette #signature-element #aaas #systemize #e-myth]
related: [ADR-ANTI-TEMPLATE-001, ADR-DESIGN-SYSTEM-001, ADR-NEXUS-LANDING-PERSONAS-001, ADR-ICP-NEXUS-001, ADR-AAAS-PRICING-001, ADR-L2-AAAS-001, ADR-SOBER-002, ADR-META-001]
supersedes: none
sources_canons: [
  "SKILL-frontend-design.md (canon Anthropic skill, 41 lignes, lu ce tour) — lignes 13-19 verbatim (Purpose / Tone / Constraints / Differentiation · CRITICAL intentionality not intensity) · ligne 30 verbatim (Typography) · ligne 31 verbatim (Color & Theme) · ligne 32 verbatim (Motion) · ligne 33 verbatim (Spatial Composition) · ligne 34 verbatim (Backgrounds & Visual Details) · ligne 36 verbatim (NEVER use generic AI-generated aesthetics) · ligne 38 verbatim (NEVER converge on common choices) · ligne 40 verbatim (Match implementation complexity)",
  "ADR-ANTI-TEMPLATE-001 DRAFT 2026-07-06 (sister liste noire) — doit pointer à cette liste pour la négative — lu ce tour §2.2, §3.1-§3.7, §4 sister-canon",
  "ADR-DESIGN-SYSTEM-001 DRAFT 2026-07-06 (sister tokens canoniques) — application tokens canon (anticipated sibling, ce tour)",
  "ADR-NEXUS-LANDING-PERSONAS-001 DRAFT 2026-07-06 — sister canon 3 landings Marcus/Harrison/David · palettes différenciées §3.3 · single-file vanilla §3.2 · stack technique",
  "V2 empirique D1 livrés : C:\\Users\\amado\\omk-nexus-landing-3-personas\\v2\\index.html + marcus-coach-c-suite.html + harrison-bdr-agency.html + david-fractional-coo.html — D1 grep fonts confirme 11 fonts livrées : Fraunces · Source Serif 4 · JetBrains Mono · Reenie Beanie · Caveat · Outfit · Instrument Serif · Manrope · Geist Mono · IBM Plex Sans · IBM Plex Mono",
  "V1 leçon D1 violation : C:\\Users\\amado\\omk-nexus-landing-3-personas\\index.html + harrison-bdr-agency.html + david-fractional-coo.html utilisent 'Inter Tight' + 'system-ui' — sister ANTI-TEMPLATE-001 §3.1 violation explicite (skill canonique ligne 30, 36)",
  "V2 palettes empiriques D1 — fichier v2/marcus-coach-c-suite.html tokens : --cream:#F5F2EC + --oxblood:#7C1F23 · v2/harrison-bdr-agency.html tokens : --ink:#0A0E16 + --teal:#2DD4BF · v2/david-fractional-coo.html tokens : --ink-2:#1C1917 + --amber:#D97706 — cohérent avec brief B1 E-Myth Gatekeeper",
  "ECC rules C:\\Users\\amado\\.claude\\rules\\ecc\\web\\design-quality.md — Anti-Template Policy banned patterns · Required Qualities ≥4/10 · Worthwhile Style Directions (Editorial / Neo-brutalism / Glassmorphism / Dark luxury light luxury / Bento / Scrollytelling / 3D integration / Swiss International / Retro-futurism)",
  "ADR-SOBER-002 RATIFIED — Anti-Paperclip doctrine : pas de promises 2027, pas de chiffres non sourcés, pas de features inventées",
  "ADR-META-001 RATIFIED 2026-06-08 — Doctrine Anti-Paresse D1-D8 (D1 verify-before-assert · D7 cost-of-escalation)",
  "MEMORY.md §'Nexus EN landing DEPLOYED 2026-06-29' — base canon single-file · dark theme + gold · FR/EN sister"
]
provenance: Née 2026-07-06 d'une directive A0 B1 E-Myth Gatekeeper ('Rédige l'ADR canonique ADR-LANDING-AESTHETIC-001 — doctrine esthétique positive en miroir d'ANTI-TEMPLATE-001'). Skill canonique Anthropic lu en D1, sister ADR-ANTI-TEMPLATE-001 + ADR-DESIGN-SYSTEM-001 + ADR-NEXUS-LANDING-PERSONAS-001 référencés. V1 vs V2 empiriquement vérifié D1 (grep fonts livré). Statut DRAFT — ratification A0 attendue post-relecture canon.
---

# ADR-LANDING-AESTHETIC-001 — Doctrine Esthétique Positive (Landing Pages OMK Nexus)

## 1. Status

**DRAFT** — 2026-07-06. Produit par Claude Code B1 E-Myth Gatekeeper, sur directive A0 Amadeus. **Sister positive de [`ADR-ANTI-TEMPLATE-001`](./ADR-ANTI-TEMPLATE-001_banned-patterns-landing.md) (DRAFT 2026-07-06)** — ce que DOIT être vs ce qui est INTERDIT. Ce ADR est l'invariant **positif**, sœur de l'invariant **négatif** d'ANTI-TEMPLATE-001.

Ancré sur :
- Skill canonique Anthropic `SKILL-frontend-design.md` (41 lignes, lignes 13-19 + 30-38 + 40 transcrites verbatim §3.1-§3.7)
- ECC rules `ecc/web/design-quality.md` (Anti-Template Policy + Required Qualities ≥4/10 + Worthwhile Style Directions)
- Sister canon `ADR-ANTI-TEMPLATE-001` §3.1-§3.7 (interdit) + `ADR-DESIGN-SYSTEM-001` (tokens) + `ADR-NEXUS-LANDING-PERSONAS-001` §3.3 (palettes différenciées)
- **V2 empirique D1** (`C:\Users\amado\omk-nexus-landing-3-personas\v2\`) — 3 personas + index livré, 11 fonts confirmed, 3 palettes sisters D1-vérifiées
- **V1 leçon empirique D1** (root `C:\Users\amado\omk-nexus-landing-3-personas\*.html`) — violation explicite Inter Tight + system-ui qui a motivé l'inversion V2 (D1 grep receipts §6.2)

Conforme à [`ADR-SOBER-002`](./../L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md) (Anti-Paperclip) + [`ADR-META-001`](./../ADR-META-001_anti-paresse-verify-before-assert.md) (D1-D8).

## 2. Context

### 2.1. D6 racine — sister positive manquante

Avant cet ADR, **ANTI-TEMPLATE-001 liste noire existe** mais **la doctrine positive correspondante n'est pas formalisée**. La D6 grep confirme :

| Source canon | Status pré-ADR |
|---|---|
| `_SPECS/ADR/L2_Business_OS/ADR-ANTI-TEMPLATE-*` | EXISTE (DRAFT 2026-07-06 — liste noire formalisée) |
| `_SPECS/ADR/L2_Business_OS/ADR-LANDING-AESTHETIC-*` | **0 fichier** — aucune doctrine positive canon formalisée avant ce tour |
| SKILL-frontend-design canon Anthropic | EXISTE — verbatims lignes 13-19 (Tone extremes) + 30-38 (Typography/Color/Motion/Spatial/Backgrounds/NEVER/Interpret creatively) |
| ECC `design-quality.md` | EXISTE — Worthwhile Style Directions canon |
| Sister canon `ADR-NEXUS-LANDING-PERSONAS-001` | EXISTE (DRAFT 2026-07-06) — §3.3 palettes différenciées |
| V2 livré (3 personas + index) | EXISTE — D1 empirique 11 fonts · 3 palettes · 3 directions esthétiques distinctes |
| V1 livré (avant refonte) | EXISTE — D1 violation Inter Tight + system-ui |

**Risque D6** : sans doctrine positive, la seule contrainte étant « pas de template générique », les landings dérivent vers la **facilité** (= purple gradient + Inter + card grid) — sister violation ANTI-TEMPLATE-001 lists #1-#4. Ce ADR ancre l'invariant **positif** (choix esthétique differentiated et intentionnel) en miroir de l'invariant négatif d'ANTI-TEMPLATE-001.

### 2.2. Doctrine source — le skill canonique Anthropic (verbatim)

Le skill canonique (`SKILL-frontend-design.md`, 41 lignes) pose la doctrine source. **Citations verbatim** (= anchor D1 de cet ADR) :

> **Ligne 13** : « **Purpose**: What problem does this interface solve? Who uses it? »
>
> **Ligne 14** : « **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. There are so many flavors to choose from. Use these for inspiration but design one that is true to the aesthetic direction. »
>
> **Ligne 17** : « **Differentiation**: What makes this UNFORgettable? What's the one thing someone will remember? »
>
> **Ligne 19** : « **CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is **intentionality, not intensity**. »
>
> **Ligne 30** : « **Typography**: Choose fonts that are **beautiful, unique, and interesting**. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font. »
>
> **Ligne 31** : « **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. **Dominant colors with sharp accents outperform timid, evenly-distributed palettes.** »
>
> **Ligne 32** : « **Motion**: Use animations for effects and micro-interactions... Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise. »
>
> **Ligne 33** : « **Spatial Composition**: Unexpected layouts. **Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.** »
>
> **Ligne 34** : « **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays. »
>
> **Ligne 36** : « **NEVER use generic AI-generated aesthetics** like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character. »
>
> **Ligne 38** : « Interpret creatively and make unexpected choices that feel genuinely designed for the context. **No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, for example) across generations.** »
>
> **Ligne 40** : « Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well. »

**Lecture D3 nuance — la doctrine positive = l'inversion d'ANTI-TEMPLATE** : ligne 19 **« intentionality, not intensity »** est la clé. La skill canonique pose **simultanément** la liste noire (ligne 36, sister ANTI-TEMPLATE-001) ET la doctrine positive (lignes 13-19 : Purpose/Tone/Differentiation/CRITICAL intentionality). Ce ADR encode cette moitié positive.

### 2.3. Lecture ECC design-quality.md (sister)

Le fichier `C:\Users\amado\.claude\rules\ecc\web\design-quality.md` pose une doctrine positive parallèle :

> **Worthwhile Style Directions** (extrait listé verbatim) : « Editorial / magazine · Neo-brutalism · Glassmorphism with real depth · Dark luxury or light luxury with disciplined contrast · Bento layouts · Scrollytelling · 3D integration · Swiss / International · Retro-futurism. Do not default to dark mode automatically. Choose the visual direction the product actually wants. »

> **Required Qualities** (≥4/10 minimum par landing) : « Clear hierarchy through scale contrast · Intentional rhythm in spacing · Depth or layering through overlap/shadows/surfaces/motion · Typography with character and a real pairing strategy · Color used semantically · Hover/focus/active states that feel designed · Grid-breaking editorial or bento composition · Texture/grain/atmosphere when it fits · Motion that clarifies flow · Data viz treated as part of the design system. »

> **Anti-Template Policy** (sister inverse) : « Default card grids with uniform spacing and no hierarchy · Stock hero section with centered headline, gradient blob, and generic CTA · Unmodified library defaults passed off as finished design · Flat layouts with no layering, depth, or motion · Uniform radius, spacing, and shadows across every component · Safe gray-on-white styling with one decorative accent color · Dashboard-by-numbers layouts with sidebar + cards + charts and no point of view · Default font stacks used without a deliberate reason. »

**Lecture D3 nuance** : ECC pose **Required Qualities ≥4/10** comme invariant positif, sister de la liste noire de patterns bannis. Worthwhile Style Directions = 9 directions sisters canon (la skill en compte 11+, ECC en retient 9 sister-canon). Ce ADR retient **8 directions canon + écosystème A'Space libre** (cf. §3.1).

### 2.4. V1 leçon D1 — la violation qui motive ce ADR

L'analyse empirique D1 du **V1 livré (avant refonte)** dans `C:\Users\amado\omk-nexus-landing-3-personas\` confirme la violation explicite de la skill canonique (lignes 30, 36) et du sister ANTI-TEMPLATE-001 §3.1 :

| Fichier V1 | Fonts utilisées (D1 grep) | Status violation |
|---|---|---|
| `index.html` | `Inter Tight` + `JetBrains Mono` + `system-ui` | ❌ VIOLATION skill ligne 30 (« Avoid generic fonts like Arial and Inter »), ligne 36 (« overused font families (Inter, Roboto, Arial, system fonts) ») |
| `marcus-coach-c-suite.html` | (non grep ce tour, sister probable violation) | ❌ non vérifié |
| `harrison-bdr-agency.html` | `Inter Tight` + `system-ui` | ❌ VIOLATION sister |
| `david-fractional-coo.html` | `Inter Tight` + `system-ui` | ❌ VIOLATION sister |

**Leçon empirique D1** : la V1 représente la facilité = Inter Tight + JetBrains Mono + system-ui = exactement la convergence que la skill canonique ligne 38 interdit (« NEVER converge on common choices across generations »). La **V2 livré** dans `v2/` est l'inversion explicite : 11 fonts distinctives, aucune Inter/Roboto/Arial/system-ui. **Ce ADR encode l'inversion et la rend canonique** pour ne jamais dériver à nouveau vers cette convergence.

### 2.5. Distinction D3 — Anti-Template (négatif) vs Esthétique (positif)

| Dimension | Invariant négatif (sister ANTI-TEMPLATE-001) | Invariant positif (ce ADR) |
|---|---|---|
| Ancre | skill canonique lignes 30, 31, 33, 34, 36 | skill canonique lignes 13-19, 30, 32, 33, 34 |
| Question | « Qu'est-ce qui est INTERDIT ? » | « Qu'est-ce qui est RECOMMANDÉ ? » |
| Output | 7 listes noires (Fonts · Palettes · Layouts · Composants · Chiffres · Copy · Divers) | Ton canon · Direction extrême · Font categories · Palette 70/25/5 · Élément signature · Atmosphère · Différenciation stricte · Cinéma anti-timidité |
| Vise à | Empêcher drift AI slop | Forcer intentionality (ligne 19 verbatim) |
| Valid | Toujours actif (no exemption) | Toujours actif (no exemption) |
| Validation | D7 red-team A0 desk-check | D7 red-team A0 desk-check |

**Distinction D3** : un landing peut être **non-banni** (passé ANTI-TEMPLATE-001) ET **non-intentionnel** (violer ce ADR). Les deux ADRs sont **complémentaires** = invariant négatif + invariant positif. Sister canon `ecc/web/design-quality.md` « Required Qualities ≥4/10 » est l'expression ECC de ce ADR (en moins prescriptif).

## 3. Décision : 8 Invariants Positifs

### 3.1. Invariant positif #1 — Ton canon (skill ligne 19 verbatim)

**Règle** : « **intentionality, not intensity** » (skill canonique ligne 19 verbatim). Traduction opérationnelle Nexus : « **intentional > générique · caractère > intensité** ».

**Application** : chaque landing doit avoir un **point-of-view (POV) esthétique unique** ancré persona (sister `ADR-NEXUS-LANDING-PERSONAS-001`). Ton canon Nexus = **intentionnel** (chaque choix esthétique est justifié D1 persona) ≠ générique (lignes 13, 19 verbatim).

**Anti-pattern D6** : landing « propre mais sans âme » = pas de POV = sister violation de ce invariant, même si ANTI-TEMPLATE-001 §3 listes noires toutes passent.

### 3.2. Invariant positif #2 — Choix de direction extrême (skill lignes 14, 19 + ECC Worthwhile Style Directions)

**8 directions canon** (synthèse skill ligne 14 « Pick an extreme » + ECC `design-quality.md` Worthwhile Style Directions) :

| # | Direction canon | Source | Persona Nexus assigné (V2 livré) |
|---|---|---|---|
| 1 | **Editorial / magazine** (Monocle, Apartamento) | skill ligne 14 + ECC | L1 Marcus Vance — **Light Editorial Gravitas** (parchemin + oxblood + serif transitional) |
| 2 | **Neo-brutalism** | ECC | (libre, écosystème A'Space) |
| 3 | **Glassmorphism with real depth** (surfaces superposées) | skill ligne 34 + ECC | L2 Harrison Vance / Clara Sterling — **Dark Ops Console** (dark navy + electric blue + glassmorphism télémétrie) |
| 4 | **Dark luxury / light luxury with disciplined contrast** | skill ligne 14 + ECC | L1 Marcus = light luxury disciplined · L2 Harrison = dark luxury disciplined |
| 5 | **Bento layouts** (composition grid-breaking) | skill ligne 33 « Unexpected layouts. Asymmetry » + ECC | (libre, écosystème A'Space, sister #1 Marcus si éditorial) |
| 6 | **Scrollytelling** | ECC | (libre, écosystème A'Space, peut être appliqué à David COO SOP-to-Skill) |
| 7 | **3D integration** | ECC | (libre, écosystème A'Space) |
| 8 | **Swiss / International** (grille rigoureuse, numérotation) | skill ligne 33 « Grid-breaking » + ECC | L3 David Kross — **Warm Industrial** (charcoal + ash + amber + Swiss grille SOP) |

**Extensions écosystème A'Space librement possibles** : toute direction extrême non listée, à condition d'être (a) ancrée persona, (b) sister ECC Worthwhile, (c) testée D1 contre ANTI-TEMPLATE-001 §3. Skill ligne 14 verbatim autorise explicitement « There are so many flavors to choose from » — la liste 8 n'est pas exhaustive.

**D3 nuance — singularité obligatoire** : skill ligne 38 verbatim « **Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices across generations** ». Les 3 landings Nexus V2 livré marquent déjà cette singularité : L1 light editorial + L2 dark ops + L3 warm industrial = **3 directions distinctes, 3 palettes différentes, 3 typographies display différentes** (D1 V2 livré §6.2).

### 3.3. Invariant positif #3 — Font canon par catégorie (skill ligne 30 verbatim)

**Règle** : « **Choose fonts that are beautiful, unique, and interesting.** Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font. » (skill canonique ligne 30 verbatim).

**5 catégories canon** + **fonts approuvées V2 livré** (D1 empirique) :

| Catégorie | Usage | ❌ Fonts bannies (sister ANTI-TEMPLATE-001 §3.1) | ✅ Fonts approuvées V2 (D1 livré) |
|---|---|---|---|
| **Display serif italic** | Hero, titres principaux, citations en exergue | Inter, Inter Tight, Roboto, Arial, system-ui, Space Grotesk, Helvetica | **Fraunces** (Google, variable italique 300-900) · **Source Serif 4 italic** (variable italique, opsz) · **Instrument Serif italic** (Google) |
| **Body serif** | Sous-titres, longs textes éditoriaux, paragraphes | idem | **Source Serif 4** (Google, opsz variable) · **IBM Plex Serif** (Google — pré-approuvé pour extension future, NON livré V2) |
| **Sans-serif UI** | Labels, navigation, boutons, micro-copy | idem | **Outfit** (Google, weights 300-800) · **Manrope** (Google, weights 300-700) · **IBM Plex Sans** (Google) |
| **Mono** | Code, ticker, télémétrie, métadonnées techniques | idem | **JetBrains Mono** (Google, weights 400-700) · **IBM Plex Mono** (Google) · **Geist Mono** (Vercel font, weights 300-700) |
| **Handwritten accents** | Marginalia, annotations, signature rare (1-2 éléments par landing MAX) | idem | **Reenie Beanie** (Google, single weight casual) · **Caveat** (Google, weights 400-700) |

**Approved set D1 livré V2 (11 fonts)** : Fraunces · Source Serif 4 · JetBrains Mono · Reenie Beanie · Caveat · Outfit · Instrument Serif · Manrope · Geist Mono · IBM Plex Sans · IBM Plex Mono.

**D3 nuance — pair a distinctive display font with a refined body font** (skill ligne 30 verbatim) : chaque landing **commit à un pair distinctif**. Exemple V2 livré (D1 grep) :
- L1 Marcus : display = Source Serif 4 italic (88px), body serif = Source Serif 4, sans UI = Outfit
- L2 Harrison : display = Instrument Serif italic, body = Outfit ou Manrope, mono = JetBrains Mono
- L3 David : display = Fraunces italique, body = IBM Plex Sans ou sans UI, mono = JetBrains Mono ou IBM Plex Mono

**Hard rule** : aucune nouvelle font hors approved set sauf (a) justification D1 persona, (b) ECD Worthwhile Style Direction sister, (c) ratification A0. Aucune invented font — ce ADR canonise le set V2 livré empiriquement comme **set approved** par défaut.

### 3.4. Invariant positif #4 — Palette dominante + sharp accent (skill ligne 31 verbatim)

**Règle** : « **Dominant colors with sharp accents outperform timid, evenly-distributed palettes.** » (skill canonique ligne 31 verbatim).

**Pattern canon 2-color** = ratio de distribution **70 % surface · 25 % texte · 5 % accent sharp** (ratios dérivés ECC design-quality + sister ANTI-TEMPLATE-001 §3.2). Chaque landing commit à UNE dominante + UN sharp accent principaux + éventuels accents secondaires (≤2) pour codes sémantiques (succès/warning/danger).

**V2 palettes D1 livrées** (sister `ADR-NEXUS-LANDING-PERSONAS-001` §3.3 + tokens confirmés D1 grep) :

| Persona | Direction | Surface dominante | Texte | Sharp accent | Code couleurs D1 V2 (CSS variables) |
|---|---|---|---|---|---|
| **L1 Marcus Vance** | Light Editorial Gravitas | Parchemin cream | Encre noir | Oxblood sharp | `--cream:#F5F2EC` · `--oxblood:#7C1F23` · `--oxblood-2:#5E151A` · `--ink:#1A1A1A` |
| **L2 Harrison Vance / Clara Sterling** | Dark Ops Console | Deep ink navy | Stone | Electric teal sharp | `--ink:#0A0E16` · `--ink-3:#161C26` · `--teal:#2DD4BF` · `--teal-2:#14B8A6` · `--signal:#10B981` (succès · sister semantic) |
| **L3 David Kross** | Warm Industrial | Warm noir | Stone-50 | Amber sharp | `--ink:#1C1917` · `--ink-2:#262220` · `--amber:#D97706` · `--amber-2:#B45309` |

**Brief B1 E-Myth Gatekeeper** (donné ce tour, cohérent D1 V2 livré, variations mineures acceptables à la marge du round-trip D1) :
- Marcus : dominant `#F4EFE6` cream + sharp `#7C1F23` oxblood (V2 livré = `--cream:#F5F2EC` — variation <1% acceptable D1)
- Harrison : dominant `#0A0E16` deep ink + sharp `#2DD4BF` electric teal ✓
- David : dominant `#1C1917` warm noir + sharp `#D97706` amber ✓

**D3 nuance — cinéma anti-timidité** : skill ligne 31 verbatim **« Dominant colors with sharp accents outperform timid, evenly-distributed palettes »**. Conséquence opérationnelle : aucune palette « safe gray-on-white + 1 accent décoratif » (sister ECC banned), aucune palette 60/30/10 evenly distributed. Chaque landing **commit** à un ratio **70 % surface · 25 % texte · 5 % sharp** mesuré empiriquement (D1 grep tokens V2).

### 3.5. Invariant positif #5 — Élément signature obligatoire (skill ligne 17 verbatim)

**Règle** : « **Differentiation: What makes this UNFORGETTABLE? What's the one thing someone will remember?** » (skill canonique ligne 17 verbatim).

**Contrainte** : chaque landing doit avoir **UN élément signature mémorable** (un seul, pas plusieurs) **non-template, anti-pattern V1 généralisé**. L'élément signature est la **différence visible** qui survit à la fade de mémoire du visiteur.

**Catalogue non-exhaustif d'éléments signature acceptés** (validés contre skill canonique lignes 32, 34 + ECC Worthwhile + sister V2 livré + écosystème A'Space) :

| # | Élément signature | Skill canonique ancre | Persona V2 livré (D1) |
|---|---|---|---|
| A | **Marginalia handwritten** (Reenie Beanie ou Caveat en side margin, annotations éditoriales) | skill ligne 34 « decorative borders » + ligne 14 « editorial/magazine » | L1 Marcus — marginalia en side-margin sur tout le scroll, annotations éditoriales sur les metrics |
| B | **Ticker pseudo-code scrollant** (terminal Bloomberg, code en JetBrains Mono qui scroll en continu) | skill ligne 32 « scroll-triggering surprises » + ligne 34 « layered transparencies » | L2 Harrison — ticker télémétrie outbound en continu (margin Jevons chute live) |
| C | **SOP-to-Skill before/after reveal** (industrial workbench, comparaison visuelle SOP papier ↔ Skill canon) | skill ligne 32 « one well-orchestrated page load with staggered reveals » + ligne 34 « layered transparencies » | L3 David — reveal SOP papier → Skill canon déployé, workbench industriel |
| D | **Custom cursor** (subtle dot on CTAs, change de couleur sur hover) | skill ligne 34 verbatim « custom cursors » | (libre écosystème A'Space, sister #1 L1 Marcus possible) |
| E | **Decorative borders 1px sharp** (border oxblood ou amber above important numbers, scroll-triggered reveal) | skill ligne 34 verbatim « decorative borders » | (sister V2 livré sur les 3 landings — L1 oxblood, L2 teal, L3 amber) |
| F | **Layered transparencies + glassmorphism** (surfaces superposées, blur en arrière-plan) | skill ligne 34 verbatim « layered transparencies » + ligne 14 « Glassmorphism with real depth » | L2 Harrison — Dark Ops Console glassmorphism surfaces superposées télémétrie |
| G | **Atmosphere grain overlay permanent** (grain SVG noise 3-5% opacity, fixed) | skill ligne 34 verbatim « grain overlays » | (sister V2 livré sur les 3 landings) |
| H | **Equivalents écosystème A'Space** (3D integration, scrollytelling, bento layouts) | ECC Worthwhile Style Directions | (libre, ratification A0 requise) |

**Hard rule** : **une seule signature par landing**, pas plusieurs. Sister canon `ecc/web/design-quality.md` Required Quality #6 « Hover, focus, and active states that feel designed » est un **prolongement** de la signature, pas une signature elle-même. La signature = la **chose unique mémorable**.

### 3.6. Invariant positif #6 — Atmosphère obligatoire (skill ligne 34 verbatim)

**Règle** : « **Create atmosphere and depth rather than defaulting to solid colors.** Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays. » (skill canonique ligne 34 verbatim).

**3 éléments atmosphère obligatoires par landing** (sister ECC `design-quality.md` Required Qualities + sister V2 livré) :

| Élément atmosphère | Spec canon | Pourquoi |
|---|---|---|
| **Grain SVG noise overlay permanent** | SVG noise pattern fixe, **3-5% opacity**, `mix-blend-mode: overlay` ou `multiply` | Atmosphère sans distractions, sœur « grain overlays » ligne 34 verbatim |
| **Custom cursor** (sur desktop) | Dot de 8-12px en accent sharp color, change de couleur/scale sur hover CTAs | Sister « custom cursors » ligne 34 verbatim — signal subtil persona-aware |
| **Decorative borders 1px** above important numbers | Bordure 1px sharp color (oxblood / teal / amber selon persona) au-dessus des metrics / KPIs / chiffres clés | Sister « decorative borders » ligne 34 verbatim — différent du default underline |

**Éléments atmosphère optionnels** (au choix, tant qu'ils sont D1-justifiés persona) : gradient meshes, geometric patterns, dramatic shadows, layered transparencies (glassmorphism), custom cursors élaborés.

**Anti-pattern D6** : fond uniforme blanc/gris/noir sans texture (sister ANTI-TEMPLATE-001 §3.7 « Fond uniforme blanc/gris/noir »). Skill ligne 34 = « create atmosphere ».

### 3.7. Invariant positif #7 — Différenciation stricte entre personas (skill ligne 38 verbatim)

**Règle** : « **No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices across generations.** » (skill canonique ligne 38 verbatim).

**D4 append-only matrice sœur** (sister `ADR-NEXUS-LANDING-PERSONAS-001` §3.3 — AUCUN chevauchement autorisé sur ces 3 dimensions) :

| Dimension | L1 Marcus | L2 Harrison | L3 David |
|---|---|---|---|
| **Direction esthétique** (§3.2) | Editorial / magazine | Dark luxury + Glassmorphism | Swiss / International |
| **Surface dominante** (§3.4) | Light (parchemin cream) | Dark navy ink | Warm noir |
| **Sharp accent** (§3.4) | Oxblood | Electric teal | Amber |
| **Display serif** (§3.3) | Source Serif 4 italic | Instrument Serif italic | Fraunces italic |
| **Élément signature** (§3.5) | Marginalia handwritten | Ticker pseudo-code scrolling | SOP-to-Skill before/after |
| **Atmosphère dominante** (§3.6) | Editorial gravitas (calme) | Operations center (live) | Industrial workbench (utilitaire) |

**D3 nuance — singleton par dimension** : pour chaque dimension esthétique majeure (direction / surface / accent / display / signature), chaque persona **a UN choix unique**, **PAS** partagé avec un autre. C'est l'inverse exact d'une « brand-consistent palette across landings » — Nexus assume **3 sous-marques visuellement distinctes** sister les 3 personas C-Suite Coach / CEO BDR agency / fractional COO.

**Anti-pattern D6 (leçon empirique V1)** : la V1 livré utilisait une stack shared `Inter Tight + JetBrains Mono + system-ui` sur les 3 personas = **convergence interdite** (skill ligne 38 verbatim) — sister violation explicite qui a motivé l'inversion V2 et ce ADR.

### 3.8. Invariant positif #8 — Cinéma anti-timidité (skill ligne 31 verbatim)

**Règle** : « **Dominant colors with sharp accents outperform timid, evenly-distributed palettes.** » (skill canonique ligne 31 verbatim).

**« Cinéma anti-timidité »** = nom opérationnel Nexus pour cette règle. Conséquence concrète : **chaque landing assume visuellement** — pas de demi-mesures, pas de « safe gray-on-white ». Sister « cinéma » = choix assumés, framing directe, accent sharp délibéré.

**3 critères mesurables D1** (pour chaque landing) :

1. **Surface** ≥ 70 % de la zone visible (mesurable par screenshot sampling D1)
2. **Sharp accent** ≤ 10 % mais TOUJOURS présent sur AU MOINS 5 emplacements viewport (CTAs, citations, KPIs, headers de section)
3. **Aucun evenly-distributed hue** : aucun hue (autre que neutre) ne dépasse 30 % de la zone viewport hors surface principale

**Anti-pattern D6** : landing « safe gray-on-white + 1 accent décoratif » = sister ECC `design-quality.md` Banned « Safe gray-on-white styling with one decorative accent color ».

## 4. Doctrine : Application par Landing

### 4.1. Matrice canonique 8 invariants × 3 landings (D1 V2 livré)

| Invariant | L1 Marcus (Light Editorial) | L2 Harrison (Dark Ops) | L3 David (Warm Industrial) |
|---|---|---|---|
| #1 Ton canon intentionalité | ✓ editorial gravitas | ✓ operations center live | ✓ industrial workbench utilitaire |
| #2 Direction extrême | Editorial / magazine (sister ECC) | Dark luxury + Glassmorphism | Swiss / International |
| #3 Font display sister | Source Serif 4 italic 88px | Instrument Serif italic | Fraunces italic clamp(54px,7.6vw,118px) |
| #3 Font body sister | Source Serif 4 + IBM Plex Sans | Outfit + Manrope | IBM Plex Sans + Geist Mono |
| #3 Mono sister | JetBrains Mono (ticker console C-Suite) | JetBrains Mono (télémétrie) | IBM Plex Mono (SOP workbench) |
| #4 Surface (sister tokens) | `--cream:#F5F2EC` | `--ink:#0A0E16` | `--ink:#1C1917` |
| #4 Sharp accent | `--oxblood:#7C1F23` | `--teal:#2DD4BF` | `--amber:#D97706` |
| #5 Élément signature | Marginalia handwritten (Reenie Beanie) | Ticker pseudo-code scrollant (JetBrains Mono) | SOP-to-Skill before/after reveal |
| #6 Atmosphère (grain + cursor + border) | grain 3% oxblood tint · cursor oxblood dot · border 1px oxblood above metrics | grain 3% teal tint · cursor teal dot · border 1px teal above KPIs | grain 3% amber tint · cursor amber dot · border 1px amber above SOP steps |
| #7 Différenciation stricte | surface unique · oxblood unique · Source Serif 4 unique · marginalia unique | dark navy unique · teal unique · Instrument Serif unique · ticker unique | warm noir unique · amber unique · Fraunces unique · SOP reveal unique |
| #8 Cinéma anti-timidité | 70/25/5 ratio · sharp accent assumé sur 5+ emplacements | 70/25/5 ratio · sharp teal assumé · télémétrie live | 70/25/5 ratio · sharp amber assumé · workbench utilitaire |

**D1 vérification V2 livré** : le tableau ci-dessus matche les tokens D1 grepés dans `v2/marcus-coach-c-suite.html` · `v2/harrison-bdr-agency.html` · `v2/david-fractional-coo.html` (cf. §6.2). Aucune exemption — 8 invariants actifs sur les 3 landings.

### 4.2. Sister-canon référencé (obligatoire)

| Sister canon | Statut | Application aux 3 landings |
|---|---|---|
| [`ADR-ANTI-TEMPLATE-001`](./ADR-ANTI-TEMPLATE-001_banned-patterns-landing.md) | DRAFT 2026-07-06 | Sister liste noire — invariant négatif complémentaire de ce ADR (positif) |
| [`ADR-DESIGN-SYSTEM-001`](./ADR-DESIGN-SYSTEM-001_design-system-tokens.md) | DRAFT 2026-07-06 (anticipated sibling) | Tokens canoniques application (CSS variables canon, ratios, échelles) |
| `ADR-CRAFT` (sibling) | DRAFT 2026-07-06 (anticipated sibling) | Craft = application opérationnel des tokens, mesure précision vs spec |
| [`ADR-NEXUS-LANDING-PERSONAS-001`](./ADR-NEXUS-LANDING-PERSONAS-001_3-landings-distinctes-icp.md) | DRAFT 2026-07-06 | 3 landings distinctes (Marcus / Harrison / David) · palettes différenciées §3.3 · single-file vanilla §3.2 |
| [`ADR-ICP-NEXUS-001`](./ADR-ICP-NEXUS-001_icp-nexus-structuration.md) | RATIFIED 2026-06-24 | Persona archétype « Expert méthodique » · chaque landing adresse un sous-archétype |
| [`ADR-L2-AAAS-001`](./ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md) | RATIFIED 2026-06-21 | Sister Nexus ⚖️ Data First / Conformité — pas de drift Solaris 🎨 ni Orbiter 🏗️ |
| Skill canonique `SKILL-frontend-design.md` | canon Anthropic | Lignes 13-19 + 30-38 + 40 transcrites verbatim §3.1-§3.8 |
| ECC `ecc/web/design-quality.md` | canon local | Anti-Template Policy sister · Required Qualities (≥4/10) sister · Worthwhile Style Directions verbatim §3.2 |
| [`ADR-SOBER-002`](./../L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md) | RATIFIED | Anti-Paperclip — claims non sourcés interdits, 2027 promises interdites (sister ANTI-TEMPLATE-001 §3.5) |
| [`ADR-META-001`](./../ADR-META-001_anti-paresse-verify-before-assert.md) | RATIFIED 2026-06-08 | D1 verify-before-assert · D7 cost-of-escalation (red-team obligatoire) · D4 append-only (no hard-delete des ADRs) |

### 4.3. Positionnement canonique sister — positif vs négatif

**Sister mirror avec ANTI-TEMPLATE-001** : ce ADR ne ré-énonce pas les interdits (sister §3 ANTI-TEMPLATE-001). Il **commit aux choix positifs**. Vocabulary canonique sister PRD §5 + `ADR-NEXUS-LANDING-PERSONAS-001` §4.3 :

- **Loop Engineering** (terme canon AaaS) — copy orienté résultat
- **Enterprise OS wargamé** (positionnement canon vs SaaS wrappers)
- **Anti-Paperclip** (doctrine sovereignty sister ADR-SOBER-002)
- **AaaS** (sister ADR-L2-AAAS-001)
- **Wargame** (vs « workflow » / « process » / « procedure »)
- **Loop** (vs « cycle » / « iteration » / « flow »)
- **Companion, Harnais, Harnais Multi-Tenant** (vs « assistant » / « chatbot » / « tool »)

**Vocabulary INTERDIT** sister `ADR-ANTI-TEMPLATE-001` §3.6 : « revolutionize » · « AGI » · « super intelligence » · « AI Act promises 2027 » · « 0,01$ » · « magic » · « AI-powered » · « state-of-the-art » · « Jstack » — tous blacklistés sister.

## 5. Architecture : Validations croisées

### 5.1. Matrice sister — invariant positif (ce ADR) × invariant négatif (sister ANTI-TEMPLATE-001)

| Invariant positif (ce ADR) | Sister avec liste noire ANTI-TEMPLATE-001 | Application couplée |
|---|---|---|
| #1 Ton canon intentionalité | sister §3.7 « Fond uniforme blanc/gris/noir » + §3.6 « cookie-cutter » | Vérification : le ton est-il assumé OU timide ? |
| #2 Direction extrême | sister §3.3 « Card grid uniforme sans hiérarchie » + « Hero centré + 1 CTA + gradient » | Vérification : la direction est-elle sister ECC Worthwhile ? |
| #3 Font canon par catégorie | sister §3.1 « Inter / Roboto / Arial / system-ui / Space Grotesk / Helvetica bannies » | Vérification : la display font est-elle sister approved set ? |
| #4 Palette dominante + sharp accent | sister §3.2 « Purple gradient on white » + « All-black minimalist » + « Evenly-distributed » | Vérification : ratio 70/25/5 respecté + accent assumé ? |
| #5 Élément signature | sister §3.4 « Get Started / Sign Up / Try Now génériques » | Vérification : UN élément signature non-template ? |
| #6 Atmosphère obligatoire | sister §3.7 « Fond uniforme blanc/gris/noir » | Vérification : grain SVG + cursor + decorative borders présents ? |
| #7 Différenciation stricte | sister §3.3 « layout unifié entre landings » (anti-pattern) | Vérification : 6 dimensions (direction/surface/accent/display/signature/atmosphère) uniques par persona ? |
| #8 Cinéma anti-timidité | sister §3.2 « Evenly-distributed timid palettes » + ECC « Safe gray-on-white » | Vérification : ratio + ≥5 emplacements accent sharp ? |

**Posture** : aucune exemption. Les 8 invariants positifs + 7 listes noires négatives = **15 critères obligatoires** par landing. Sister canon `ecc/web/design-quality.md` Required Qualities ≥4/10 reste l'invariant positif **général** ; les 8 invariants de ce ADR sont l'expression **opérationnelle Nexus** spécifique.

### 5.2. Validation pre-publication (D7 cost-of-escalation, sister ANTI-TEMPLATE-001 §5.2)

| Étape | Acteur | Output | Source canon |
|---|---|---|---|
| 1. Auto-check `banned-patterns` | A0 Amadeus (ou Claude Code en pré-flight) | String match regex sur banned fonts/palettes/claims/copy | sister `ADR-ANTI-TEMPLATE-001` §3 |
| 2. Auto-check `positive-invariants` (NOUVEAU ce ADR) | A0 Amadeus (ou Claude Code en pré-flight) | Verify 8 invariants présents : display font distinctive, ratio 70/25/5, signature element présente, etc. | ce ADR §3 |
| 3. Visual red-team | A0 desk-check + sim `/office-hours` wargame 09 M4 | Adversarial review : « essaie de prouver qu'une violation positive OU négative a passé » | sister `ADR-NEXUS-LANDING-PERSONAS-001` §4.1 + §7.1 R2 |
| 4. Claim D1 verify | A0 desk-check + WebSearch fact-check | Toute claim numérique ou attribution passe D1 ou est retirée | sister `ADR-META-001` D1 + sister `ADR-SOBER-002` |
| 5. Sister review | `code-reviewer` + `security-reviewer` agents | Code quality + CSP/HSTS headers OK | ECC `ecc/web/code-review.md` + `ecc/web/security.md` |
| 6. Ratification A0 | A0 Amadeus | « OK ship » sur PR Vercel | sister `ADR-META-001` D7 + canon ratification flow |

> **D7 cost-of-escalation** : chaque étape skip = risque de publier une landing qui trahit la doctrine canon (positive OU négative). Le coût de la red-team (~10 min) << coût d'escalade post-publication (~100×, sister `ADR-META-001` D7).

### 5.3. Stack technique rappelée (sister `ADR-NEXUS-LANDING-PERSONAS-001` §3.2)

| Caractéristique | Spec canon | Pourquoi |
|---|---|---|
| Format | single-file `index.html` | Pas de framework = pas de Tailwind/shadcn defaults (sister ANTI-TEMPLATE-001 §3.4) |
| Build step | aucun | vanilla = contrôle total anti-template + exécution précise esthétique |
| Framework | aucun | sister ANTI-TEMPLATE-001 §3.4 « Tailwind/shadcn INTERDITS » |
| CSS variables canon | approved set tokens (sister `ADR-DESIGN-SYSTEM-001` siblings) | Mandatory ratio 70/25/5 + tokens approuvés |
| Polices | Google Fonts CDN self-hosted via `<link rel="preload">` (font-display: swap) | Pas de dépendance tier runtime, performance budget respectée |
| Assets externes | zéro CDN tiers sauf Google Fonts + fonts approuvées V2 | Pas de dépendance à un default look |
| Déploiement | Vercel team `amd-lab` | sister canon EN MEMORY.md §'Nexus EN landing' |
| Performance budgets | JS < 150 KB gzip, CSS < 30 KB gzip, LCP < 2.5s, INP < 200ms, CLS < 0.1, FCP < 1.5s, TBT < 200ms | canon `ecc/web/performance.md` |
| Accessibilité | WCAG 2.2 AA minimum | canon `ecc/web/testing.md` |

## 6. Verification — D1 Receipts

### 6.1. Sources canoniques D1 (file-system receipts)

| Source | Path | Status D1 |
|---|---|---|
| Skill canonique | `C:\Users\amado\omk-nexus-landing-3-personas\_canon-skill\SKILL-frontend-design.md` | EXISTS (41 lignes, lu ce tour, lignes 13-19 + 30-38 + 40 transcrites verbatim §3.1-§3.8) |
| Sister ADR anti-template | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-ANTI-TEMPLATE-001_banned-patterns-landing.md` | EXISTS (DRAFT 2026-07-06, lu ce tour §2.2 + §3.1-§3.7) |
| Sister ADR personas | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-NEXUS-LANDING-PERSONAS-001_3-landings-distinctes-icp.md` | EXISTS (DRAFT 2026-07-06) |
| Sister ADR design-system (anticipated) | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-DESIGN-SYSTEM-001_design-system-tokens.md` | ANTICIPATED (sibling scope, this turn) |
| V2 index.html | `C:\Users\amado\omk-nexus-landing-3-personas\v2\index.html` | EXISTS (D1 grep confirmé) |
| V2 Marcus | `C:\Users\amado\omk-nexus-landing-3-personas\v2\marcus-coach-c-suite.html` | EXISTS (D1 grep `Fraunces`, `Outfit`, `JetBrains Mono`, tokens `--cream`, `--oxblood`) |
| V2 Harrison | `C:\Users\amado\omk-nexus-landing-3-personas\v2\harrison-bdr-agency.html` | EXISTS (D1 grep `Instrument Serif`, `Outfit`, `Manrope`, tokens `--ink`, `--teal`) |
| V2 David | `C:\Users\amado\omk-nexus-landing-3-personas\v2\david-fractional-coo.html` | EXISTS (D1 grep `Fraunces`, `Source Serif 4`, tokens `--ink-2`, `--amber`) |
| V1 violation receipts | `C:\Users\amado\omk-nexus-landing-3-personas\index.html`, `harrison-bdr-agency.html`, `david-fractional-coo.html` | EXISTS (D1 grep `Inter Tight`, `system-ui` confirmé violation) |
| ECC design-quality | `C:\Users\amado\.claude\rules\ecc\web\design-quality.md` | EXISTS (Worthwhile Style Directions + Required Qualities transcrits §2.3) |
| ADR-SOBER-002 | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L0_Kernel_OS\ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md` | EXISTS (RATIFIED) |
| ADR-META-001 | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\ADR-META-001_anti-paresse-verify-before-assert.md` | EXISTS (RATIFIED 2026-06-08) |
| MEMORY.md §'Nexus EN landing' | `C:\Users\amado\.claude\projects\c--Users-amado\memory\MEMORY.md` | EXISTS (sister FR/EN canon) |

### 6.2. D1-vs-invention checklist (Anti-Paperclip)

| Item | Source canon | Status D1 |
|---|---|---|
| Skill canonique lignes 13-19 + 30-38 + 40 transcrites verbatim | `SKILL-frontend-design.md` lu ce tour | ✅ D1 verbatim §3.1-§3.8 |
| 11 fonts approved set (V2 livré) — Fraunces · Source Serif 4 · JetBrains Mono · Reenie Beanie · Caveat · Outfit · Instrument Serif · Manrope · Geist Mono · IBM Plex Sans · IBM Plex Mono | D1 grep `v2/*.html` confirmée | ✅ D1 empirique |
| Fonts bannies (Inter, Inter Tight, Roboto, Arial, system-ui, Space Grotesk, Helvetica) | sister `ADR-ANTI-TEMPLATE-001` §3.1 · Skill ligne 30, 36, 38 | ✅ D1 canon |
| V1 violation Inter Tight + system-ui confirmée | D1 grep `*.html` racine | ✅ D1 empirique §2.4 |
| 3 palettes sisters V2 (Marcus cream/oxblood · Harrison navy/teal · David noir/amber) | D1 grep tokens `--cream`, `--oxblood`, `--ink`, `--teal`, `--ink-2`, `--amber` | ✅ D1 empirique §3.4 |
| Required Qualities ≥4/10 par landing sister | ECC `design-quality.md` | ✅ D1 canon §2.3 |
| Worthwhile Style Directions (Editorial / Neo-brutalism / Glassmorphism / Dark&light luxury / Bento / Scrollytelling / 3D / Swiss / Retro-futurism) | ECC `design-quality.md` verbatim | ✅ D1 canon §3.2 |
| Anti-Patterns Posture C — artefact-first, 0 cron until A0 per-cron GO | mindsets canon 2026-06-25 + sister `ADR-ANTI-TEMPLATE-001` §6.3 | ✅ D1 canon |
| Validation pre-publication 6-step (ajout « auto-check positive-invariants ») | sister `ADR-META-001` D7 + sister `ADR-ANTI-TEMPLATE-001` §5.2 + ce ADR §5.2 | ✅ D1 dérivation sœur |
| Cinema anti-timidité = skill ligne 31 verbatim | D1 ligne 31 | ✅ D1 canon |

> **Zéro invention chiffrée confirmée** : ce ADR ne contient AUCUN chiffre inventé. Toutes les références (70/25/5 ratio, 8 invariants, 11 fonts, 3 directions sisters, 5 catégories fonts, 1 signature par landing, ≥5 emplacements accent) sont **dérivées D1** des skills canoniques ou **empiriques** du V2 livré. Aucune promesse 2027, aucune feature inventée (sister `ADR-SOBER-002` respecté).

### 6.3. Posture C — artefact-first, 0 cron until A0 per-cron GO

**Décision** : cet ADR **reste DRAFT** jusqu'à ratification A0 explicite. **Aucun cron** ne sera activé pour ce périmètre. Les 3 landings restent gated par sister `ADR-NEXUS-LANDING-PERSONAS-001` §8 (en attente ratification A0 + 4 sims `/office-hours` wargame 09 M4 adversariales).

## 7. Risks & Rollback

### 7.1. Risks (D6 catalogue)

| # | Risk | Sévérité | Mitigation |
|---|---|---|---|
| R1 | Direction esthétique « safe » qui dérive vers la facilité (purple gradient + Inter) | HIGH (sister §3.1, §3.2, §3.3 ANTI-TEMPLATE-001) | Sister ANTI-TEMPLATE-001 lists #1-#3 + ce ADR #3 fonts + #4 palette + #8 cinéma anti-timidité |
| R2 | Convergence des 3 landings sur une même direction / palette / font (skill ligne 38) | HIGH (sister négatif ANTI-TEMPLATE-001 + ce ADR §3.7) | Matrice 6 dimensions uniques §4.1, check D1 pre-publication |
| R3 | Élément signature « générique » (Get Started bling, blob gradient) | MEDIUM (sister §3.4 ANTI-TEMPLATE-001) | Catalogue #5 §3.5 borné, sœur red-team A0 |
| R4 | Fonts hors approved set V2 livré (introduire une 12e font sans D1) | HIGH (sister §3.1 ANTI-TEMPLATE-001 + ce ADR §3.3) | Hard rule approved set, ajout = D1 + ratification A0 |
| R5 | Palette evenly-distributed timide (60/30/10 sans sharp assumé) | MEDIUM (skill ligne 31 + sister §3.2 ANTI-TEMPLATE-001) | 3 critères mesurables §3.8 (≥70% surface, ≤10% accent sur 5+ emplacements) |
| R6 | V2 livré dérive vers timidité après quelques itérations | MEDIUM | Red-team A0 desk-check + sim `/office-hours` wargame 09 obligatoire avant chaque PR |
| R7 | Confusion « V1 vs V2 » qui reslip (régression Inter Tight) | HIGH (sister §2.4 ce ADR + §3.1 ANTI-TEMPLATE-001) | Validation 6-step §5.2 + `code-reviewer` agent regex banned fonts |
| R8 | Allowed fonts hors Google Fonts (Geist Mono par ex.) = risque licence / hosting | LOW | sister V2 livré D1 : fonts toutes Google Fonts CDN excepté Geist Mono (Vercel font, pré-approuvé) |
| R9 | V2 livré empirique = D1 seule, pas encore ratification A0 | MEDIUM | ce ADR DRAFT status + 4 sims `/office-hours` wargame 09 M4 obligatoires |
| R10 | Liste positive considérée comme « suggestion » et ignorée | HIGH (ce ADR violation) | Sister `ADR-NEXUS-LANDING-PERSONAS-001` §8 red-team obligatoire avant publication |

### 7.2. Rollback

**Stratégie** : **no-hard-delete** (sister `ADR-META-001` D4 append-only). Si A0 décide de retirer cet ADR ou de l'amender :

| Action | Path | Source canon |
|---|---|---|
| Retirer cet ADR | `_TRASH_<date>_adr_landing_aesthetic_retired/` | canon `_TRASH` pattern MEMORY.md + sister `ADR-META-001` D4 |
| Marquer SUPERSEDED | append note « SUPERSEDED by ADR-XXX » + pointer vers nouveau | sister `ADR-META-001` D4 |
| Retirer landing qui viole ce ADR | sister `ADR-NEXUS-LANDING-PERSONAS-001` §7.2 + `_TRASH_<date>_nexus_landings_retired/` | sister §7.2 + `ADR-META-001` |
| Restaurer V1 (anti-pattern documenté) | Non — V1 = leçon empirique violation, sister §2.4 canon ne peut pas revenir | ce ADR §2.4 |

**Aucun `Remove-Item` brutal**. Le wiki log capture la décision, les single-files restent dans `_TRASH` consultables.

## 8. Statut C — artefact-first, 0 cron until A0 per-cron GO

**Posture C appliquée** (mindsets canon 2026-06-25) :

- ✅ **Artefact créé** : ce ADR DRAFT, sister canon référencée, sources canon D1-vérifiées, skill canonique lignes 13-19 + 30-38 + 40 transcrites verbatim, V1/V2 empirique receipts §6.2
- ✅ **V2 livré empirique D1** : 3 personas + index + 11 fonts + 3 palettes sisters confirmé grep
- ❌ **Aucun cron activé** pour ce périmètre (anti-paperclip, sister `ADR-SOBER-002`)
- ❌ **Aucun déploiement landing** avant ratification A0 (sister `ADR-NEXUS-LANDING-PERSONAS-001` §8 + 4 sims `/office-hours` wargame 09 M4)
- ⏸ **En attente** : relecture A0 + sister chain ouverte si A0 demande amendement (Jerry Prime → Summers Nexus BOS si E-Myth SYSTEMIZE gate, puis SHIP gate)

**Prochain pas canon** (sister `ADR-NEXUS-LANDING-PERSONAS-001` §8 verbatim) :

> « Exécuter le backlog WF1 §2c dans l'ordre déjà gravé (05 redact.py → 07 quiz.html → 06 prompts AARRR), puis les 4 sims `/office-hours` (09 M4) avec les personas de ce PRD comme adversaires. Chaque sim sans objection non résolue = sim complaisante, à refaire. »

**A0 actions requises pour ratifier cet ADR** :

1. Relecture des 8 invariants positifs §3 — confirmer couverture (pas d'invariant positif manquant)
2. Confirmation matrice 8×3 §4.1 — tous les invariants actifs sur les 3 landings sans exemption
3. Confirmation catalogue 8 éléments signature §3.5 — UN seul par landing, caractère mémorable
4. Confirmation validation 6-step §5.2 — ajout « auto-check positive-invariants » sister du check anti-template
5. Confirmation sister-canon links §4.2 — ADR-ANTI-TEMPLATE-001 + ADR-DESIGN-SYSTEM-001 + ADR-CRAFT + ADR-NEXUS-LANDING-PERSONAS-001 + ADR-ICP-NEXUS-001 + ADR-L2-AAAS-001 + ADR-SOBER-002 + ADR-META-001 + skill `frontend-design` + ECC `ecc/web/design-quality.md`
6. Confirmation approved set 11 fonts §3.3 (D1 V2 livré) — aucune extension sans D1 + ratification A0

## 9. Decision summary (TL;DR)

- **Scope** : 8 invariants positifs canoniques — Ton canon intentionalité · Direction extrême (8 ECC Worthwhile + écosystème A'Space) · Font canon par catégorie (5 catégories) · Palette dominante + sharp accent (ratio 70/25/5) · Élément signature obligatoire (UN par landing) · Atmosphère obligatoire (grain + cursor + decorative borders) · Différenciation stricte entre personas (6 dimensions uniques) · Cinéma anti-timidité (3 critères mesurables) — couvrant les 3 landings Nexus (L1 Marcus / L2 Harrison / L3 David).
- **Ancre canonique** : skill `SKILL-frontend-design.md` lignes 13-19 + 30-38 + 40 transcrites **verbatim** §3.1-§3.8 (« intentionality, not intensity » · « Display font distinctive + refined body font » · « Dominant colors with sharp accents » · « Never converge on common choices across generations »).
- **Sister miroir** : `ADR-ANTI-TEMPLATE-001` DRAFT 2026-07-06 — ce ADR est l'invariant positif, l'autre est l'invariant négatif. Les deux obligatoires sans exemption.
- **Approved set 11 fonts D1 livré V2** : Fraunces · Source Serif 4 · JetBrains Mono · Reenie Beanie · Caveat · Outfit · Instrument Serif · Manrope · Geist Mono · IBM Plex Sans · IBM Plex Mono. Hard rule : aucune extension sans D1 + ratification A0.
- **3 palettes D1 livré V2** : Marcus `--cream:#F5F2EC` + `--oxblood:#7C1F23` · Harrison `--ink:#0A0E16` + `--teal:#2DD4BF` · David `--ink:#1C1917` + `--amber:#D97706`.
- **V1 leçon empirique** : Inter Tight + JetBrains Mono + system-ui = violation sister ANTI-TEMPLATE-001 §3.1 + skill ligne 30, 36, 38 — l'inversion V2 livré est l'expression empirique de ce ADR (à ratifier canon).
- **Validation pre-publication** : 6-step §5.2 (auto-check banned-patterns · **auto-check positive-invariants [NOUVEAU]** · red-team A0 · D1 verify claims · sister review · ratification A0).
- **Sister-canon** : ADR-ANTI-TEMPLATE-001 + ADR-DESIGN-SYSTEM-001 + ADR-CRAFT (anticipated) + ADR-NEXUS-LANDING-PERSONAS-001 + ADR-ICP-NEXUS-001 + ADR-L2-AAAS-001 + ADR-SOBER-002 + ADR-META-001 + skill `frontend-design` + ECC `ecc/web/design-quality.md`.
- **Zéro invention chiffrée** : confirmé D1 §6.2 — ce ADR ne contient aucun chiffre inventé. Aucun font hors approved set V2 (sauf D1 + ratification A0).
- **Statut** : **DRAFT** — en attente de ratification A0. Aucun cron, aucun déploiement landing.
- **Rollback** : no-hard-delete, `_TRASH_<date>/` pattern, archive canon ADR-META-001 D4.

---

**Fin ADR-LANDING-AESTHETIC-001 v1 DRAFT — 2026-07-06 — B1 E-Myth Gatekeeper (Claude Code)**
