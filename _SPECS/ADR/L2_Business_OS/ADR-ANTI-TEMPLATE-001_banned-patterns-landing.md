---
id: ADR-ANTI-TEMPLATE-001
title: OMK Nexus Landing Pages — Liste Noire Formelle des Patterns Bannis (Anti-AI Slop)
status: RATIFIED
ratification:
  by: "A0 Amadeus"
  date_iso: "2026-07-06"
  gate_a0_signed_off: true
  approval_token: "RATIFICATION-BATCH-01-2026-07-06-TIER-0"
  context: "Ratification Tier 0 foundational DDD Landing Pages — 4 ADR bases (ANTI-TEMPLATE + ANTI-PAPERCLIP + SKILLS-CANON + WORKFLOW) ratifiés en bloc suite Phase 5 multi-workflow validée."
date: 2026-07-06
last_updated: 2026-07-06 (Claude Code B1 E-Myth Gatekeeper — distilled from SKILL-frontend-design canon + ADR-SOBER-002 + ADR-META-001 + ADR-NEXUS-LANDING-PERSONAS-001, screened Anti-Paperclip D1-D8)
deciders: [A0 Amadeus]
proposed_by: Claude Code (B1 E-Myth Gatekeeper, on A0 directive "rédige l'ADR canonique ADR-ANTI-TEMPLATE-001 pour les 3 landings Nexus")
domain: L2 Business OS / OMK Nexus / Anti-Template / Design Quality / Aesthetic Doctrine
tags: [#ADR #anti-template #anti-ai-slop #landing-page #nexus #marcus #harrison #david #aesthetic #banned-patterns #doctrine #aaas #systemize #e-myth]
related: [ADR-NEXUS-LANDING-PERSONAS-001, PRD-NEXUS-EVOLUTION-IA-001, ADR-ICP-NEXUS-001, ADR-AAAS-PRICING-001, ADR-L2-AAAS-001, ADR-SOBER-002, ADR-META-001]
supersedes: none
sources_canons: [
  "SKILL-frontend-design.md (canon Anthropic skill, 41 lignes, lu ce tour) — lignes 30-38 verbatim (Typography / Color & Theme / Motion / Spatial Composition / Backgrounds & Visual Details / NEVER use generic AI-generated aesthetics / Interpret creatively)",
  "PRD-NEXUS-EVOLUTION-IA-001 §7 — confusions Gemini filtrées D4 (chiffres non sourcés, claims AI-Act promises 2027, BETH_VETO_DISSOLVED faux, Jstack→Gstack)",
  "ADR-NEXUS-LANDING-PERSONAS-001 DRAFT 2026-07-06 — sister canon 3 landings Marcus/Harrison/David (palettes différenciées, single-file vanilla)",
  "ADR-ICP-NEXUS-001 RATIFIED 2026-06-24 — 5 piliers canon ICP Nexus (persona 'Expert méthodique', mantra 'L'illusion de la complexité')",
  "ADR-AAAS-PRICING-001 RATIFIED+AMENDED 2026-06-24 — 5 Tiers AaaS USD post-accuponcture (référencé pour affichage pricing canon)",
  "ADR-L2-AAAS-001 RATIFIED 2026-06-21 — 3 Variants Solarpunk (Solaris 🎨 · Nexus ⚖️ · Orbiter 🏗️)",
  "ADR-SOBER-002 RATIFIED — Anti-Paperclip doctrine : pas de promises 2027, pas de chiffres non sourcés, pas de features inventées",
  "ADR-META-001 RATIFIED 2026-06-08 — Doctrine Anti-Paresse D1-D8 (D1 verify-before-assert · D7 cost-of-escalation)",
  "MEMORY.md §'Nexus EN landing DEPLOYED 2026-06-29' — base canon : single-file index.html 628 KB · EN ratio 96.8% · dark theme #0A0E16 + #C8A55C",
  "ECC rules C:\\Users\\amado\\.claude\\rules\\ecc\\web\\design-quality.md — Anti-Template Policy + Required Qualities (≥4/10) + Worthwhile Style Directions"
]
provenance: Née 2026-07-06 d'une directive A0 B1 E-Myth Gatekeeper ('Rédige l'ADR canonique ADR-ANTI-TEMPLATE-001'). SKILL-frontend-design.md (41 lignes) lu en D1 — lignes 30-38 transcrites verbatim, sister canon ADR-NEXUS-LANDING-PERSONAS-001 + PRD-NEXUS-EVOLUTION-IA-001 + ADR-SOBER-002 + ADR-META-001 + MEMORY.md. Statut DRAFT — ratification A0 attendue post-relecture canon.
---

# ADR-ANTI-TEMPLATE-001 — Liste Noire Formelle des Patterns Bannis (Landing Pages OMK Nexus)

## 1. Status

**DRAFT** — 2026-07-06. Produit par Claude Code B1 E-Myth Gatekeeper, sur directive A0 Amadeus. Sister canon de [`ADR-NEXUS-LANDING-PERSONAS-001`](./ADR-NEXUS-LANDING-PERSONAS-001_3-landings-distinctes-icp.md) (DRAFT 2026-07-06 — 3 landings Marcus/Harrison/David) et [`ADR-ICP-NEXUS-001`](./ADR-ICP-NEXUS-001_icp-nexus-structuration.md) (RATIFIED 2026-06-24). Ancré sur le skill canonique Anthropic `SKILL-frontend-design.md` (41 lignes, lignes 30-38 transcrites verbatim §3.1) et la doctrine Anti-Template Policy `ecc/web/design-quality.md`. Conforme à [`ADR-SOBER-002`](./../L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md) (Anti-Paperclip) + [`ADR-META-001`](./../ADR-META-001_anti-paresse-verify-before-assert.md) (D1-D8).

## 2. Context

### 2.1. D6 racine — pas de liste noire formelle pour les landings Nexus

Avant cet ADR, **aucune décision canon formalisée** sur les patterns bannis. La D6 grep confirme :

| Source canon | Status pré-ADR |
|---|---|
| `_SPECS/ADR/L2_Business_OS/ADR-ANTI-TEMPLATE-*` | **0 fichier** — aucune liste noire formelle avant ce tour |
| SKILL-frontend-design canon Anthropic | EXISTE (`C:\Users\amado\omk-nexus-landing-3-personas\_canon-skill\SKILL-frontend-design.md`, 41 lignes) — mais transposé tel quel dans le code, pas dans un ADR |
| ECC rules design-quality | EXISTE (`C:\Users\amado\.claude\rules\ecc\web\design-quality.md`) — Anti-Template Policy + Required Qualities (≥4/10) |
| Sister canon ADR-NEXUS-LANDING-PERSONAS-001 | DRAFT 2026-07-06 — §3.3 palettes différenciées, mais pas de **liste noire canonique** |

**Risque D6** : sans liste noire formelle, chaque landing risque de dériver vers le même template "AI slop" (= Inter + purple gradient + card grid + "Get Started"), trahissant la doctrine Anti-Paperclip ADR-SOBER-002 et la différenciation aesthetic entre les 3 personas (PRD §4 verbatim, sister ADR-NEXUS-LANDING-PERSONAS-001 §3.3).

### 2.2. Doctrine source — le skill canonique Anthropic (verbatim)

Le skill canonique (`SKILL-frontend-design.md`, 41 lignes) pose la doctrine source. **Citation verbatim lignes 30-38** (= anchor D1 de cet ADR) :

> **Ligne 30** : « **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font. »
>
> **Ligne 31** : « **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes. »
>
> **Ligne 32** : « **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise. »
>
> **Ligne 33** : « **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density. »
>
> **Ligne 34** : « **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays. »
>
> **Ligne 36** : « **NEVER use generic AI-generated aesthetics** like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character. »
>
> **Ligne 38** : « Interpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. **NEVER converge on common choices (Space Grotesk, for example) across generations**. »

**Lecture D3 nuance** : la ligne 36 liste explicitement (a) les font families bannies — Inter, Roboto, Arial, system fonts — et (b) les palettes cliché — purple gradients on white backgrounds. La ligne 38 étend la liste noire à **toute convergence commune** (Space Grotesk nommé en exemple non-exhaustif). Cette doctrine est **transversale** : elle s'applique aux 3 landings Nexus (L1 Marcus, L2 Harrison, L3 David) sans exception.

### 2.3. Cohérence avec Anti-Paperclip ADR-SOBER-002

La liste noire couvre **deux dimensions** distinctes mais complémentaires :

1. **Aesthetic Anti-Template** (ce ADR) — interdiction des patterns visuels génériques (font / palette / layout / composant)
2. **Claim Anti-Paperclip** (ADR-SOBER-002 sister) — interdiction des claims non sourcés (chiffres inventés, témoignages fictifs, AI-Act promises 2027)

**Distinction D3** : un landing peut avoir une aesthetic Anti-Template parfaite mais claimer des chiffres inventés (violation ADR-SOBER-002) — les deux ADRs sont **complémentaires, pas redondants**. Le présent ADR se concentre sur **(1)** et référence **(2)** quand une liste noire chevauche les deux (ex. « 47% conversion » est interdit pour double raison : (a) non sourcé D1, (b) cliché de "social proof" AI slop).

## 3. Décision : 7 Listes Noires Formelles

### 3.1. Liste Noire #1 — Fonts (ancre skill canonique lignes 30, 36, 38)

| ❌ Font bannie | Justification canon | ✅ Direction de remplacement acceptée |
|---|---|---|
| **Inter** | Skill ligne 30 : « Avoid generic fonts like Arial and Inter » · Ligne 36 : « overused font families (Inter, Roboto, Arial, system fonts) » | Serif transitional pour L1 Marcus (gravitas éditoriale) · Sans-serif géométrique condensé pour L2 Harrison (métrique BDR) · Sans humaniste pour L3 David (lisibilité opérationnelle) — chaque landing a SA font distinctive |
| **Inter Tight** | Variante Inter — même famille générique (skill ligne 36) | Sister de Inter ci-dessus |
| **Roboto** | Skill ligne 36 verbatim : « overused font families (Inter, Roboto, Arial, system fonts) » | Sister ci-dessus — Google Material default, anti-distinctif |
| **Arial** | Skill ligne 30 verbatim : « Avoid generic fonts like Arial and Inter » · Ligne 36 | Sister ci-dessus — fallback HTML générique, marqueur "lazy design" |
| **system-ui** | Skill ligne 36 verbatim : « system fonts » | Sister ci-dessus — chaque landing COMMIT à une font ownable |
| **Space Grotesk** | Skill ligne 38 verbatim : « NEVER converge on common choices (Space Grotesk, for example) across generations » | Sister ci-dessus — convergence AI slop, désigne explicitement le pattern |
| **Helvetica** (et Helvetica Neue) | Skill ligne 30 esprit générique · ligne 36 « overused font families » | Sister ci-dessus — présente comme "safe choice" mais marqueur default |

**D3 nuance — exceptions tolérées** :

- **Display font en <8% du copy total** : acceptable d'utiliser une font "neutre" (system-ui) UNIQUEMENT pour les micro-labels (badges, timestamps, metadata) sous 8% du total copy. **Justification** : skill ligne 30 demande « pair a distinctive display font with a refined body font » — la refined body font peut être system-ui si la display est distinctive. **Mais** : le display doit TOUJOURS être non-banni.
- **Variable fonts** : autorisées SI la variable axis est exploitée (poids, largeur, optical size) — pas juste pour avoir "Inter Variable" déguisé.

### 3.2. Liste Noire #2 — Palettes Clichés (ancre skill canonique lignes 31, 36)

| ❌ Palette cliché | Justification canon | ✅ Direction de remplacement acceptée |
|---|---|---|
| **Gradient purple-on-white** | Skill ligne 36 verbatim : « cliched color schemes (particularly **purple gradients on white backgrounds**) » | L1 Marcus : parchemin `#F5F0E1` + oxblood `#7A1F1F` · L2 Harrison : dark navy `#0A0E16` + electric blue `#3B82F6` · L3 David : charcoal `#1C1917` + amber `#D97706` — **3 palettes sisters** (PRD §4 + ADR-NEXUS-LANDING-PERSONAS-001 §3.3 canon) |
| **All-black minimalist vide** | Skill ligne 31 : « Dominant colors with sharp accents outperform timid, evenly-distributed palettes » — all-black = evenement-distributed timid | L1 Marcus : surface parchemin (chaud, éditorial) · L2 Harrison : dark navy + accents sharp (electric blue / emerald / red signal) · L3 David : charcoal + amber sharp — chaque palette a **accent sharp** |
| **Dark mode automatique sans raison** | ECC `design-quality.md` : « Do not default to dark mode automatically » — dark mode doit servir une raison narrative (operations center Harrison) | L1 Marcus : LIGHT (gravitas éditoriale C-Suite) · L2 Harrison : DARK (operations center BDR, sister canon EN `#0A0E16`) · L3 David : WARM DARK (atelier cabinet) — chaque choix est **ancré persona** |
| **Palette evenly-distributed (timid)** | Skill ligne 31 verbatim : « Dominant colors with sharp accents outperform timid, evenly-distributed palettes » | Ratio sister : **70% surface · 25% texte · 5% accent sharp** par landing (cf. sister ADR-NEXUS-LANDING-PERSONAS-001 §3.3 tokens) |

**D3 nuance — tokens acceptables** (DÉRIVÉS des 3 palettes sisters, pas inventés) :

| Persona | Surface | Texte | Accent principal | Accent secondaire | Stat |
|---|---|---|---|---|---|
| L1 Marcus | `#F5F0E1` (parchemin) | `#1A1A1A` (noir encre) | `#7A1F1F` (oxblood) | `#8B7E5A` (brass mat) | n/a |
| L2 Harrison | `#0A0E16` (dark navy) | `#F5F5F4` (stone-100) | `#3B82F6` (electric blue) | `#10B981` (emerald) | `#EF4444` (signal) |
| L3 David | `#1C1917` (stone-900) | `#FAFAF9` (stone-50) | `#A8A29E` (stone-400) | `#D97706` (amber) | `#B91C1C` (deep red) |

> **Source canon tokens** : ADR-NEXUS-LANDING-PERSONAS-001 §3.3 — D1 sister (lu ce tour). Chaque landing respecte AA WCAG 2.2 (canon `ecc/web/testing.md`).

### 3.3. Liste Noire #3 — Layouts (ancre skill canonique lignes 33, 36)

| ❌ Layout banni | Justification canon | ✅ Direction de remplacement acceptée |
|---|---|---|
| **Card grid uniforme sans hiérarchie** | ECC `design-quality.md` Anti-Template Policy : « Default card grids with uniform spacing and no hierarchy » · Skill ligne 33 : « Unexpected layouts. Asymmetry » | L1 Marcus : **Editorial / magazine** (colonnes étroites, lettrines, marges généreuses, citations en exergue) · L2 Harrison : **Dark luxury + glassmorphism** (surfaces superposées, télémétrie live, compteurs animés) · L3 David : **Swiss / International** (grille rigoureuse, numérotation visible, listes hiérarchiques, schémas SOP) — 3 directions sisters canon |
| **Hero centré avec 1 CTA + gradient** | ECC `design-quality.md` : « Stock hero section with centered headline, gradient blob, and generic CTA » | L1 Marcus : hero asymétrique, citation en exergue, 2 CTA hiérarchisés (audit vs wargame) · L2 Harrison : hero split (dashboard à gauche / copy à droite), CTA primaire « Lance le quiz simulateur » · L3 David : hero sobre, SOP en vignette, CTA « Convertis ta première SOP » |
| **Dashboard-by-numbers sans POV** | ECC `design-quality.md` : « Dashboard-by-numbers layouts with sidebar + cards + charts and no point of view » | L2 Harrison a un dashboard (autorisé par sister canon §3.3 — **Dark Ops Console**) mais **avec POV** : télémétrie marge Jevons (en chute), outbound vert/rouge, gauge animée — pas un dashboard "by numbers" sans thèse |
| **Hero "stock" avec blob** | ECC `design-quality.md` : « Stock hero section with centered headline, gradient blob, and generic CTA » | Aucun landing Nexus n'utilise de blob gradient — chaque hero a une **direction distinctive** ancrée persona |

### 3.4. Liste Noire #4 — Composants (ancre skill canonique lignes 33, 36)

| ❌ Composant banni | Justification canon | ✅ Direction de remplacement acceptée |
|---|---|---|
| **shadcn template non-customisé** | ECC `design-quality.md` : « Unmodified library defaults passed off as finished design » · Skill ligne 36 : « cookie-cutter design that lacks context-specific character » | Composants sur-mesure par landing : Hero persona-spécifique (sister ADR-NEXUS-LANDING-PERSONAS-001 §3.4) · Quiz simulateur d'inférence (sister canon wargame 07) · DLP module link (sister canon wargame 05) · AAARR Signal-First hook (sister canon wargame 06) · MiroFish teaser (sister canon wargame 08) |
| **Tailwind defaults (sans surcouche)** | ECC `design-quality.md` : « Unmodified library defaults » · Anti-template stricte | **Tailwind/shadcn INTERDITS** par sister canon ADR-NEXUS-LANDING-PERSONAS-001 §3.2 (« stack technique — single-file vanilla HTML/CSS/JS »). Toutes les 3 landings = vanilla, CSS custom via variables, zero framework UI |
| **"Get Started / Sign Up / Try Now" génériques** | ECC `design-quality.md` Anti-Template Policy · Skill ligne 36 « cookie-cutter » | CTA persona-spécifiques : L1 Marcus « Demande ton audit Sdiri » / « Wargame tes workflows » · L2 Harrison « Lance le quiz simulateur » / « Calcule ton arbitrage Jevons » · L3 David « Convertis ta première SOP » / « W× tes 15 clients » |
| **Footer générique "© 2026 Company"** | Anti-template : footer = signature, pas placeholder | Footer multi-langue FR/EN, liens légaux AI-Act 2026-08-02 (sister canon EN MEMORY.md §'Nexus EN landing'), mention AaaS canon « Enterprise OS wargamé vs SaaS wrappers vibe-codés éphémères » |

### 3.5. Liste Noire #5 — Chiffres & Claims (ancre ADR-SOBER-002 sister)

| ❌ Claim interdit | Raison canon (Anti-Paperclip) |
|---|---|
| **« 47% conversion »** | PRD §7.6 + ADR-SOBER-002 : chiffres non sourcés, jamais republier sans D1 verify |
| **« 1000+ clients »** | idem |
| **« ×10 ROI »** (ou « ×1000 leads ») | idem |
| **« 700+ signaux capturés »** | PRD §7.6 verbatim — interdit |
| **Témoignages inventés** (« Jane Smith, CEO of FakeCorp ») | ADR-SOBER-002 : pas de feature inventée → pas de faux client non plus |
| **Logos clients fictifs** (grilles « trusted by » avec marques inventées) | idem — risque légal + violation Anti-Paperclip |
| **« Boostrapped vibe-coded SaaS wrapper, livré en 2 semaines »** | PRD §5 positionnement **inverse** : « vs SaaS wrappers vibe-codés éphémères » — l'auto-positionnement comme wrapper détruit le positionnement canon |
| **Citations inventées attribuées à Gartner / McKinsey / Forbes** | PRD §7.6 — chiffres/attributions non sourcés interdits |

> **Règle de validation pré-publication** (sister canon ADR-NEXUS-LANDING-PERSONAS-001 §4.1) : chaque landing passe un **red-team A0 desk-check** (ou sim `/office-hours` wargame 09 M4 adversariale) qui tente de prouver qu'une claim est inventée. Si une claim ne survit pas, on la retire. **D7 cost-of-escalation** : red-team obligatoire avant merge.

### 3.6. Liste Noire #6 — Copy / Jargon AI Hype (ancre skill canonique ligne 36 + ADR-SOBER-002)

| ❌ Terme / tournure bannie | Raison canon | ✅ Remplacement acceptable |
|---|---|---|
| **« revolutionize »** (ou « disrupt », « 10× your... ») | Skill ligne 36 « cliched » · PRD §5 positionnement vs SaaS hype | « transform », « industrialise », « rends opérationnel » — copy orienté **résultat client**, pas hype |
| **« AGI », « super intelligence »** | PRD §1 gravé : local-first sans GPU **différé 2027**, AGI hors scope canon | « IA agentique », « orchestration », « boucle outillée » — terms canon AaaS |
| **« AI Act promises 2027 »** (local-first, inférence on-device) | PRD §1 verbatim : « L'IA locale sans GPU = différée 2027 (DSpark, Recursivemas, finetuning du Canon A'Space) » · **INTERDIT** sur les 3 landings | « Conforme AI-Act 2026-08-02 » (canon, sister ADR-NEXUS-LANDING-PERSONAS-001 §4.1) — pitch = conformité **avant** 2027, pas local-first |
| **« 0,01$ par appel »** (ou pricing miracle) | PRD §1+§5 verbatim : argument Jevons **repositionné** = coût fixe vs API variable, **PAS** 0,01$ (qui est l'argument 2027 local) | « Plan fixe vs compteur API variable » (sister ADR-NEXUS-LANDING-PERSONAS-001 §4.3 framework #3) |
| **« state-of-the-art », « best-in-class », « world-class »** | Skill ligne 36 « cookie-cutter » | « canon », « audité », « référence interne », citations exactes sister |
| **« magic », « AI-powered », « GPT under the hood »** | Skill ligne 36 « generic AI-generated aesthetics » | « orchestration AaaS », « Loop Engineering », « Enterprise OS wargamé » — vocabulary canon |
| **« BETH_VETO_DISSOLVED »** (et autres refs canon inventées) | PRD §7.1 verbatim : faux — Beth = seul veto (WARMODE-002) | Refs canon **vérifiées D1** uniquement |
| **« Jstack »** (ou « J-stack », « JStack ») | PRD §7.3 verbatim : faux — référent réel canon = **Gstack** (garrytan/gstack) | **Gstack** uniquement |

### 3.7. Liste Noire #7 — Anti-Patterns Divers

| ❌ Anti-pattern | Raison canon | ✅ Remplacement acceptable |
|---|---|---|
| **« Trusted by 1000+ companies »** (grille logos inventés) | Liste noire #5 sister · ADR-SOBER-002 | Refs vérifiées D1 uniquement (si existante) **OU** section « Comment ça marche » avec processus visible |
| **Cookie banner préchargé sur hero** (avant interaction) | ECC `ecc/web/security.md` + UX | Cookie banner après interaction (lazy) · CSP nonce-based |
| **Animation infinie en hero** (clignotement, particules) | Skill ligne 32 : « one well-orchestrated page load with staggered reveals » (one-shot, pas infini) | Staggered reveals one-shot au load · scroll-triggered surprises · hover/focus states designed |
| **Fond uniforme blanc/gris/noir** | Skill ligne 34 : « Create atmosphere and depth rather than defaulting to solid colors » | Gradient meshes, noise textures, geometric patterns, layered transparencies — chaque landing a SA texture |
| **« Learn more » / « Read more »** (CTA vague) | Anti-template · skill ligne 36 « cookie-cutter » | CTA persona-spécifique sister §3.4 |
| **Stock photo de bureau / poignée de main / gens souriants** | ECC `design-quality.md` Anti-Template Policy · Skill ligne 36 « cookie-cutter » | Illustrations custom OU absence d'image (le copy + la typography portent le hero) |

## 4. Doctrine : Sister-canon + Application par Landing

### 4.1. Application stricte par landing (sister ADR-NEXUS-LANDING-PERSONAS-001 §3.3)

| # | Landing | Persona | Direction esthétique canon (sister) | Banned lists actives |
|---|---|---|---|---|
| **L1** | Marcus Vance | C-Suite Coach ★ prioritaire | **Light Editorial Gravitas** (parchemin + oxblood + brass) — `ecc/web/design-quality.md` Worthwhile Style Directions | Toutes — Fonts #1 (serif transitional), Palette #2 (parchemin), Layout #3 (éditorial), Composant #4 (CTA persona), Claims #5 (zéro), Copy #6 (zéro AGI), Divers #7 |
| **L2** | Harrison Vance / Clara Sterling | CEO agence BDR ★ prioritaire | **Dark Ops Console** (dark navy + electric blue + emerald) — sister canon EN `MEMORY.md §'Nexus EN landing'` | Toutes — Fonts #1 (sans-serif géométrique condensé), Palette #2 (dark navy), Layout #3 (glassmorphism), Composant #4 (quiz simulateur wargame 07), Claims #5 (zéro), Copy #6 (Jevons repositionné), Divers #7 |
| **L3** | David Kross | fractional COO ×15 PME ★ prioritaire | **Warm Industrial** (charcoal + ash + amber) — `ecc/web/design-quality.md` Worthwhile Style Directions | Toutes — Fonts #1 (sans humaniste), Palette #2 (charcoal + amber), Layout #3 (Swiss), Composant #4 (CTA « Convertis SOP »), Claims #5 (zéro), Copy #6 (zéro), Divers #7 |

### 4.2. Sister-canon référencé

| Sister canon | Statut | Application aux 3 landings |
|---|---|---|
| [`ADR-NEXUS-LANDING-PERSONAS-001`](./ADR-NEXUS-LANDING-PERSONAS-001_3-landings-distinctes-icp.md) | DRAFT 2026-07-06 | 3 landings distinctes (Marcus / Harrison / David) · palettes différenciées §3.3 · single-file vanilla §3.2 · composants partagés §3.4 |
| [`ADR-ICP-NEXUS-001`](./ADR-ICP-NEXUS-001_icp-nexus-structuration.md) | RATIFIED 2026-06-24 | Persona archétype « Expert méthodique » · mantra « L'illusion de la complexité » · marché Conformité — chaque landing adresse un sous-archétype |
| [`ADR-AAAS-PRICING-001`](./ADR-AAAS-PRICING-001_aaas-pricing-canon.md) | RATIFIED + AMENDED 2026-06-24 | Affichage tier canon « Enterprise OS wargamé » $1000/mois gated ×100 (plan-L2 §13) — **PAS** de pricing inventé |
| [`ADR-L2-AAAS-001`](./ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md) | RATIFIED 2026-06-21 | Sister Nexus ⚖️ Data First / Conformité — pas de drift Solaris 🎨 ni Orbiter 🏗️ |
| [`ADR-SOBER-002`](./../L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md) | RATIFIED | Anti-Paperclip — claims non sourcés interdits, 2027 promises interdites (sister §3.5 + §3.6 de ce ADR) |
| [`ADR-META-001`](./../ADR-META-001_anti-paresse-verify-before-assert.md) | RATIFIED 2026-06-08 | D1 verify-before-assert (claims D1 uniquement) · D7 cost-of-escalation (red-team obligatoire) · D4 append-only (no hard-delete des ADRs) |
| Skill canonique `SKILL-frontend-design.md` | canon Anthropic | Lignes 30-38 transcrites verbatim §3.1-§3.7 |
| ECC `design-quality.md` | canon local | Anti-Template Policy + Required Qualities (≥4/10) + Worthwhile Style Directions |

### 4.3. Positionnement canonique — vocabulaire obligatoire

**Vocabulary canonique** sister (PRD §5 + ADR-NEXUS-LANDING-PERSONAS-001 §4.3) — **À UTILISER** sur les 3 landings, dans le copy, les CTA, les titres, les footer, les alt-text :

- **« Loop Engineering »** (terme canon AaaS)
- **« Enterprise OS wargamé »** (positionnement canon vs SaaS wrappers)
- **« Anti-Paperclip »** (doctrine sovereignty sister ADR-SOBER-002)
- **« AaaS »** (sister ADR-L2-AAAS-001)
- **« Wargame »** (vs « workflow », « process », « procedure »)
- **« Loop »** (vs « cycle », « iteration », « flow »)
- **« Companion », « Harnais », « Harnais Multi-Tenant »** (vs « assistant », « chatbot », « tool »)

**Vocabulary INTERDIT** (cf. §3.6 sister copy blacklist) : « revolutionize », « AGI », « super intelligence », « AI Act promises 2027 », « 0,01$ », « magic », « AI-powered », « state-of-the-art ».

## 5. Architecture : Matrice Acceptable vs Banned

### 5.1. Matrice canonique 7×3 (lands × lists)

| Banned list | L1 Marcus (Light Editorial) | L2 Harrison (Dark Ops) | L3 David (Warm Industrial) |
|---|---|---|---|
| #1 Fonts (Inter/Roboto/Arial/system-ui/Space Grotesk/Helvetica) | ✅ ACTIVE | ✅ ACTIVE | ✅ ACTIVE |
| #2 Palettes (purple-gradient/all-black/default-dark/even-distributed) | ✅ ACTIVE | ✅ ACTIVE | ✅ ACTIVE |
| #3 Layouts (card-grid/stock-hero/dashboard-by-numbers/blob) | ✅ ACTIVE | ✅ ACTIVE (sauf dashboard POV) | ✅ ACTIVE |
| #4 Composants (shadcn-default/Tailwind-default/génériques-CTA) | ✅ ACTIVE | ✅ ACTIVE | ✅ ACTIVE |
| #5 Chiffres (47%/1000+/×10/invented-testimonials) | ✅ ACTIVE | ✅ ACTIVE | ✅ ACTIVE |
| #6 Copy (revolutionize/AGI/2027-promise/0,01$/Jstack) | ✅ ACTIVE | ✅ ACTIVE | ✅ ACTIVE |
| #7 Divers (logos-invented/cookie-preload/infinite-anim/stock-photo) | ✅ ACTIVE | ✅ ACTIVE | ✅ ACTIVE |

**Posture** : aucune exemption. Les 7 lists sont actives sur les 3 landings sans exception. Sister canon `ecc/web/design-quality.md` Required Qualities ≥4/10 par landing reste l'invariant positif — ce ADR est l'invariant **négatif** (= liste noire).

### 5.2. Validation pre-publication (D7 cost-of-escalation)

| Étape | Acteur | Output | Source canon |
|---|---|---|---|
| 1. Auto-check `banned-patterns.md` | A0 Amadeus (ou Claude Code en pré-flight) | Markdown check : aucun terme banni présent dans le code source (string match + regex) | ce ADR §3 |
| 2. Visual red-team | A0 desk-check + sim `/office-hours` wargame 09 M4 | Adversarial review : « essaie de prouver qu'un pattern AI slop a passé » | ADR-NEXUS-LANDING-PERSONAS-001 §4.1 + §7.1 R2 sister |
| 3. Claim D1 verify | A0 desk-check + WebSearch fact-check (skill canon `context7-mcp` si library, `WebSearch` si claim externe) | Toute claim numérique ou attribution passe D1 ou est retirée | ADR-META-001 D1 + ADR-SOBER-002 sister |
| 4. Sister review | `code-reviewer` agent + `security-reviewer` agent | Code quality + CSP/HSTS headers OK | ECC `ecc/web/code-review.md` + `ecc/web/security.md` |
| 5. Ratification A0 | A0 Amadeus | « OK ship » sur PR Vercel | ADR-META-001 D7 + canon ratification flow |

> **D7 cost-of-escalation** : chaque étape skip = risque de publier une landing qui trahit la doctrine canon. Le coût de la red-team (~10 min) << coût d'escalade post-publication (~100×, ADR-META-001 D7).

### 5.3. Stack technique rappelée (sister ADR-NEXUS-LANDING-PERSONAS-001 §3.2)

| Caractéristique | Spec canon | Pourquoi |
|---|---|---|
| Format | single-file `index.html` | Pas de framework = pas de Tailwind/shadcn defaults (banned list #4) |
| Build step | aucun | vanilla = contrôle total anti-template |
| Framework | aucun | sister canon §3.2 « Tailwind/shadcn INTERDITS » |
| Assets externes | zéro CDN tiers (sauf fonts si justifié D1) | Pas de dépendance à un default look |
| Déploiement | Vercel team `amd-lab` | canon sister EN MEMORY.md §'Nexus EN landing' |
| Performance budgets | JS < 150 KB gzip, CSS < 30 KB gzip, LCP < 2.5s, INP < 200ms, CLS < 0.1, FCP < 1.5s, TBT < 200ms | canon `ecc/web/performance.md` |
| Accessibilité | WCAG 2.2 AA minimum | canon `ecc/web/testing.md` |

## 6. Verification — D1 Receipts

### 6.1. Sources canoniques D1 (file-system receipts)

| Source | Path | Status D1 |
|---|---|---|
| Skill canonique | `C:\Users\amado\omk-nexus-landing-3-personas\_canon-skill\SKILL-frontend-design.md` | EXISTS (41 lignes, lu ce tour, lignes 30-38 transcrites verbatim §2.2) |
| Sister ADR personas | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-NEXUS-LANDING-PERSONAS-001_3-landings-distinctes-icp.md` | EXISTS (DRAFT 2026-07-06, lu ce tour) |
| PRD canon | `C:\Users\amado\ASpace_OS_V2\_SPECS\PRD\PRD-NEXUS-EVOLUTION-IA-001_offre-2026-landing-icp.md` | EXISTS (canon 2026-07-06) — §7 confusions filtrées référencé |
| ADR-ICP-NEXUS-001 | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-ICP-NEXUS-001_icp-nexus-structuration.md` | EXISTS (RATIFIED 2026-06-24) |
| ADR-AAAS-PRICING-001 | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-AAAS-PRICING-001_aaas-pricing-canon.md` | EXISTS (RATIFIED + AMENDED 2026-06-24) |
| ADR-L2-AAAS-001 | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md` | EXISTS (RATIFIED 2026-06-21) |
| ADR-SOBER-002 | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L0_Kernel_OS\ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md` | EXISTS (RATIFIED) |
| ADR-META-001 | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\ADR-META-001_anti-paresse-verify-before-assert.md` | EXISTS (RATIFIED 2026-06-08) |
| ECC design-quality | `C:\Users\amado\.claude\rules\ecc\web\design-quality.md` | EXISTS |
| MEMORY.md §'Nexus EN landing' | `C:\Users\amado\.claude\projects\c--Users-amado\memory\MEMORY.md` | EXISTS (sister FR/EN canon) |

### 6.2. D1-vs-invention checklist (Anti-Paperclip)

| Item | Source canon | Status D1 |
|---|---|---|
| Skill canonique lignes 30-38 transcrites verbatim | `SKILL-frontend-design.md` lu ce tour | ✅ D1 verbatim §2.2 |
| Fonts bannies (Inter, Inter Tight, Roboto, Arial, system-ui, Space Grotesk, Helvetica) | Skill ligne 30, 36, 38 verbatim | ✅ D1 canon |
| Palettes cliché (purple gradient, all-black, default dark, evenly-distributed) | Skill ligne 31, 36 verbatim + ECC `design-quality.md` | ✅ D1 canon |
| Layouts clichés (card grid uniforme, hero centré, dashboard-by-numbers, blob) | ECC `design-quality.md` Anti-Template Policy + skill ligne 33 | ✅ D1 canon |
| Composants banned (shadcn default, Tailwind default, "Get Started" génériques) | ECC `design-quality.md` + sister ADR-NEXUS-LANDING-PERSONAS-001 §3.2 « Tailwind/shadcn INTERDITS » | ✅ D1 canon |
| Claims interdits (chiffres non sourcés, témoignages inventés, logos fictifs) | PRD §7.6 + ADR-SOBER-002 | ✅ D1 canon |
| Copy jargon (revolutionize, AGI, AI Act promises 2027, 0,01$, magic, state-of-the-art) | PRD §1, §5, §7 + ADR-SOBER-002 + skill ligne 36 | ✅ D1 canon |
| Jstack → Gstack | PRD §7.3 verbatim | ✅ D1 canon |
| 3 palettes sisters (Marcus/Harrison/David) — tokens surface/texte/accent | ADR-NEXUS-LANDING-PERSONAS-001 §3.3 sister | ✅ D1 dérivation sœur |
| Pricing $1000/mois gated ×100 (référencé mais PAS inventé) | plan-L2 §13 + ADR-AAAS-PRICING-001 | ✅ D1 canon (pour l'affichage, sister ADR) |
| Worthwhile Style Directions sisters | ECC `design-quality.md` | ✅ D1 canon |
| Required Qualities ≥4/10 par landing | ECC `design-quality.md` | ✅ D1 canon |
| Validation pre-publication 5-step | ADR-META-001 D7 + sister ADR §4.1 | ✅ D1 dérivation sœur |

> **Zéro invention chiffrée confirmée** : ce ADR ne contient AUCUN chiffre inventé (pas de « 47% », pas de « 1000+ », pas de « ×10 ROI »). Toutes les références numériques sisters pointent vers les ADRs canoniques (plan-L2 §13, ADR-AAAS-PRICING-001, etc.).

### 6.3. Posture C — artefact-first, 0 cron until A0 per-cron GO

**Décision** : cet ADR **reste DRAFT** jusqu'à ratification A0 explicite. **Aucun cron** ne sera activé pour ce périmètre. Les 3 landings restent gated par sister ADR-NEXUS-LANDING-PERSONAS-001 §8 (en attente ratification A0 + 4 sims `/office-hours` wargame 09 M4 adversariales).

## 7. Risks & Rollback

### 7.1. Risks (D6 catalogue)

| # | Risk | Sévérité | Mitigation |
|---|---|---|---|
| R1 | Drift aesthetic entre les 3 landings (= perte cohérence Nexus brand) | MEDIUM | Sister ADR-NEXUS-LANDING-PERSONAS-001 §3.3 — c'est le but, **PAS** un bug. Sisters FR/EN canon restent brand-consistent (dark + gold) pour le socle non-persona |
| R2 | Claim inventée qui passe la red-team | HIGH (ADR-SOBER-002 violation) | red-team A0 desk-check obligatoire avant publication + sim `/office-hours` wargame 09 M4 adversariale (§5.2 ce ADR) |
| R3 | Font "neutre" utilisée par erreur comme display (>8% copy) | MEDIUM | check string match `banned-fonts` + visuel red-team |
| R4 | Composant shadcn réintroduit subrepticement (build step caché) | MEDIUM | sister ADR §3.2 « vanilla strict » + `code-reviewer` agent avec regex Tailwind/shadcn |
| R5 | « Local-first 2027 » ou « 0,01$ » qui reslip dans le copy | HIGH (PRD §1 violation) | check string match `banned-claims` + adversarial review |
| R6 | Confusion « Jstack » qui reslip | MEDIUM (PRD §7.3 violation) | check string match + sister ADR-NEXUS-LANDING-PERSONAS-001 red-team |
| R7 | Testimonial / logo inventé pour « Trusted by » | HIGH (ADR-SOBER-002) | section « Trusted by » retirée par défaut — pas d'invention |
| R8 | Stock photo de poignée de main / bureau | MEDIUM | pas de photo OU illustration custom D1-vérifiée |
| R9 | Tailwind CDN ajouté en dépendance « rapide » | HIGH (sister ADR §3.2 violation) | review dependencies + `code-reviewer` agent |
| R10 | Liste noire considérée comme « suggestion » et ignorée | HIGH (ce ADR violation) | sister ADR-NEXUS-LANDING-PERSONAS-001 red-team obligatoire (§5.2 ce ADR) |

### 7.2. Rollback

**Stratégie** : **no-hard-delete** (ADR-META-001 D4 append-only). Si A0 décide de retirer cet ADR ou de l'amender :

| Action | Path | Source canon |
|---|---|---|
| Retirer cet ADR | `_TRASH_<date>_adr_anti_template_retired/` | canon `_TRASH` pattern MEMORY.md + ADR-META-001 |
| Marquer SUPERSEDED | append note « SUPERSEDED by ADR-XXX » + pointer vers nouveau | ADR-META-001 D4 |
| Retirer landing qui viole ce ADR | sister ADR-NEXUS-LANDING-PERSONAS-001 §7.2 + `_TRASH_<date>_nexus_landings_retired/` | sister §7.2 + ADR-META-001 |

**Aucun `Remove-Item` brutal**. Le wiki log capture la décision, les single-files restent dans `_TRASH` consultables.

## 8. Statut C — artefact-first, 0 cron until A0 per-cron GO

**Posture C appliquée** (mindsets canon 2026-06-25) :

- ✅ **Artefact créé** : ce ADR DRAFT, sister canon référencée, sources canon D1-vérifiées, skill canonique lignes 30-38 transcrites verbatim
- ❌ **Aucun cron activé** pour ce périmètre (anti-paperclip, ADR-SOBER-002)
- ❌ **Aucun déploiement landing** avant ratification A0 (sister ADR-NEXUS-LANDING-PERSONAS-001 §8 + 4 sims `/office-hours` wargame 09 M4)
- ⏸ **En attente** : relecture A0 + sister chain ouverte si A0 demande amendement (Jerry → Summers Nexus BOS si E-Myth SYSTEMIZE gate, puis SHIP gate)

**Prochain pas canon** (sister ADR-NEXUS-LANDING-PERSONAS-001 §8 verbatim) :

> « Exécuter le backlog WF1 §2c dans l'ordre déjà gravé (05 redact.py → 07 quiz.html → 06 prompts AARRR), puis les 4 sims `/office-hours` (09 M4) avec les personas de ce PRD comme adversaires. Chaque sim sans objection non résolue = sim complaisante, à refaire. »

**A0 actions requises pour ratifier cet ADR** :

1. Relecture des 7 listes noires §3 — confirmer couverture (pas de banned pattern manquant)
2. Confirmation matrice 7×3 §5.1 — toutes les lists actives sur les 3 landings sans exemption
3. Confirmation validation 5-step §5.2 — red-team A0 desk-check + sims `/office-hours` obligatoires
4. Confirmation vocabulary canonique §4.3 — terms Loop Engineering / Enterprise OS wargamé / Anti-Paperclip / AaaS obligatoires
5. Confirmation sister-canon links §4.2 — ADR-NEXUS-LANDING-PERSONAS-001 + ADR-ICP-NEXUS-001 + ADR-AAAS-PRICING-001 + ADR-L2-AAAS-001 + ADR-SOBER-002 + ADR-META-001

## 9. Decision summary (TL;DR)

- **Scope** : 7 listes noires formelles (Fonts · Palettes · Layouts · Composants · Chiffres · Copy · Divers) couvrant les 3 landings Nexus (L1 Marcus / L2 Harrison / L3 David).
- **Ancre canonique** : skill `SKILL-frontend-design.md` lignes 30-38 transcrites **verbatim** §2.2 (Inter/Roboto/Arial/system fonts bannis · purple-gradient cliché · cookie-cutter interdit · Space Grotesk convergence interdite).
- **Anti-Paperclip couplé** : sister canon ADR-SOBER-002 (pas de claims inventés, pas de 2027 promises, pas de Jstack).
- **Pas d'exemption** : matrice 7×3 §5.1 — toutes les lists actives sur les 3 landings sans exception (gated par sister ADR-NEXUS-LANDING-PERSONAS-001 red-team).
- **Vocabulary canonique sister** : Loop Engineering · Enterprise OS wargamé · Anti-Paperclip · AaaS · Wargame · Companion — termes obligatoires §4.3.
- **Vocabulary interdit sister** : revolutionize · AGI · AI-Act 2027 promise · 0,01$ · magic · AI-powered · state-of-the-art · Jstack — tous blacklistés §3.6.
- **Validation pre-publication** : 5-step §5.2 (auto-check banned-patterns · red-team A0 · D1 verify claims · sister review · ratification A0).
- **Sister-canon** : ADR-NEXUS-LANDING-PERSONAS-001 + ADR-ICP-NEXUS-001 + ADR-AAAS-PRICING-001 + ADR-L2-AAAS-001 + ADR-SOBER-002 + ADR-META-001 + skill `frontend-design` + ECC `ecc/web/design-quality.md`.
- **Zéro invention chiffrée** : confirmé D1 §6.2 — ce ADR ne contient aucun chiffre inventé.
- **Statut** : **DRAFT** — en attente de ratification A0. Aucun cron, aucun déploiement landing.
- **Rollback** : no-hard-delete, `_TRASH_<date>/` pattern, archive canon ADR-META-001 D4.

---

**Fin ADR-ANTI-TEMPLATE-001 v1 DRAFT — 2026-07-06 — B1 E-Myth Gatekeeper (Claude Code)**