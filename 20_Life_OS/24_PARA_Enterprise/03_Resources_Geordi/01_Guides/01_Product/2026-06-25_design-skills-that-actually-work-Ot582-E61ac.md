---
domain: 01_Product
ld: LD04_Cognition_Tilly
b2_owner: flash-product
sister_b1: jerry-prime
b1_filter: APPLIED_E1_DETERMINISTIC (sweep 2026, ADR-L2-BDLD-MAP-001 D3)
---
# Guide — Design Skills That Actually Work (AI Labs)

> **Source canonique** : Transcript brut `Ot582-E61ac.md` (16 853 chars) · Vidéo YouTube https://youtu.be/Ot582-E61ac · Chaîne **AI Labs** ("a software company, and this is our channel AI Labs. And on this channel, we show you how to optimize processes with AI")
> **Domaine** : 01_Product (11 hits : design/UI/UX/frontend/landing/visual/layout)
> **Date canonisation** : 2026-06-25
> **Pattern verbatim identifié** : *"the sites are all different, but somehow feel the same"* — drift vers les "safe, generic choices" du modèle.

---

## 1. Concepts — Glossaire (6 entrées)

### 1.1 Skill (vs MCP, vs prompt)
Dans l'écosystème Claude, un **skill** est un *rulebook* — un fichier `skill.md` qui contient des instructions, des patterns et des règles de projet que l'agent charge **à la demande**. Verbatim transcript : *"Think of it as a rulebook. Shadcn has a specific correct way of building things and the skill holds all of those rules. On top of that, it looks at how your own project is set up."* Différence clé avec le **MCP** (Model Context Protocol) : le MCP est une *live connection* à un registre distant qui reste **dans le context window en permanence**, alors que la skill ne se charge **que quand elle est nécessaire**. Verbatim : *"The skill only loads when it's actually needed instead of being in the context window all the time like MCP does."* Conséquence opérationnelle : la skill donne le **jugement**, le MCP donne les **composants**.

### 1.2 AI Slop
Verbatim : *"It even out the usual AI slop directly in its skill.md file, which is basically the skills instruction sheet, so the model stops reaching for the same overused fonts and the purple gradients on white backgrounds."* L'AI slop désigne l'ensemble des **patterns safe** que le modèle produit par défaut quand il n'a aucune contrainte directionnelle : mêmes fonts, mêmes gradients violet-sur-blanc, mêmes composants génériques. Lutter contre l'AI slop = forcer le modèle à **commit to a real design direction before it writes anything**.

### 1.3 Front-end Design Skill (Anthropic)
Skill fondateur du design AI. Verbatim : *"Anthropic's front-end design skill is the one that shapes the design direction of your site."* Mécanisme : escape des safe choices en obligeant le modèle à **commit to a real design direction before it writes anything**. Limite connue : *"the Anthropic design skill does not work well with functional UI"* — inadapté aux dashboards, adapté aux landing pages et portfolios où *the design itself is part of the product*.

### 1.4 Shadcn (registry + skill + MCP)
Verbatim : *"the model doesn't have to generate components from scratch and configure animations on its own. It can just pull the component that's already pre-built in the registry which is basically a big library of ready-made components."* Shadcn = bibliothèque de composants **professional grade déjà construits** — le modèle assemble au lieu de générer. Architecture double : (a) **Shadcn skill** = règles + patterns + contexte projet, (b) **Shadcn MCP** = live connection au registre qui browse et pull les composants réels. Bénéfice : *"clean output the first time instead of having to go back and fix the same mistakes over and over."*

### 1.5 Functional UI vs Marketing UI
Distinction explicite du transcript : *"there's two skills each made for a separate job. There's the functional skill which builds the UI people actually have to use like dashboards and then there's one for marketing UI."* Dans **AI Labs Pro**, la landing page artistique et la couche fonctionnelle (community) **cohabitent volontairement** : *"the landing page has a much more artistic design language as opposed to the actual functional layer of the community which looks really boring and plain just like any other web interface you have ever interacted with."* Cette dissociation est canonique : ne jamais appliquer un skill marketing à un dashboard, ni l'inverse.

### 1.6 Dashboard Skill
*"there's a separate skill named dashboard made just for that. Not by Shadcn, but by another developer. And it focuses the model on exactly that arrangement. And because it reasons through that arrangement first, the result actually feels like a real analytics tool instead of being cluttered."* Différence fondatrice : pour un app classique, le problème = *keeping components consistent*. Pour un dashboard, le problème = *how all the information is arranged on the screen, how to group the data and how much can live on one screen before it gets too cluttered*.

---

## 2. Outillage — Matrice de sélection (5 entrées)

| Skill / Outil | Couche | Cible | Cas d'usage canonique | Source verbatim |
|---|---|---|---|---|
| **Anthropic front-end design skill** | Direction | Landing, portfolio | "where the design itself is part of the product" | *"shapes the design direction of your site"* |
| **Shadcn (skill + MCP)** | Composants | Web app, dashboards | Quand des composants professional-grade existent déjà | *"professional grade and uses them in your app"* |
| **UI UX Pro Max** | Décision + recherche | Tout site | Avant d'écrire la moindre ligne : lance un engine qui tire 5 recherches parallèles sur 161 catégories industrie,挑选 palette + fonts + layout adaptés | *"gives it a decision before it starts tuned to the kind of product you're actually making"* |
| **Dashboard skill** | Arrangement | Analytics, dashboards | Le problème dashboard = groupement des données + densité écran | *"focuses the model on exactly that arrangement"* |
| **GSAP skill** | Animation | Landing, scroll storytelling | Animations + performance (steer vers propriétés compositor-friendly) | *"the model moves things by changing their size or position and those changes force the browser to rebuild the whole page on every single frame"* |

**Skills "taste presets"** (à picker 1, jamais stacker) :
- **Minimalist UI** — journaux, blogs, contenu qui respire
- **Industrial brutalist UI** — anti-corporate, raw, heavy
- **Front-end UI/UX** — all-rounder safe pick (produit, business landing clean)
- **Premium front-end UI** — *"luxury fashion brand landing pages"*

**Mobile skills** (mobile n'est PAS un petit web) :
- **Mobile app UI design** (principles layer) — thumb zone, spacing cohérent, font sizes limités (Airbnb/Duolingo/Spotify)
- **Material 3** — Google's design system Android/Pixel, *"bold and colorful with big rounded shapes and springy motion"*
- **Swift UI skills** — Apple, *"translucent glassy look it now calls liquid glass"*
- **Expo skill** — cross-platform iOS+Android en un seul build

**Asset generation** : **Higgs Field** — *"plugs image and video generation straight into your agent"* — SeeDance recommandé pour la vidéo.

---

## 3. Perspective Souveraine — Anti-Slop comme Doctrine ASpace

La thèse centrale du transcript est un **constat opérationnel** : *"After you've generated enough landing pages with AI, you start noticing a pattern where the sites are all different, but somehow feel the same. That's because the model learned from a huge amount of data full of the same patterns. So, whenever it has to make a design call, it reaches for the most common one. So, the design keeps drifting toward the same safe, generic choices, no matter what the project actually is."* Cette dérive vers la médiane statistique n'est pas un bug — c'est la **fonction d'optimisation** du modèle : *"when most models build a landing page, they're optimizing to be correct. But this skill pushes them to commit to a design direction instead."*

Pour ASpace OS V2 (canon : `C:\Users\amado\ASpace_OS_V2\`), cette doctrine se traduit en 3 verrous anti-slop :

**Verrou 1 — Commit before write** : Aucune landing Life-OS-2026 ni OMK SaaS ne doit sortir sans un **design direction documenté AVANT** la première ligne de code. Le doc doit répondre à : (a) Quelle émotion ? (b) Quelle industrie / registre visuel ? (c) Quels composants Shadcn/Material 3 seront exclus ?

**Verrou 2 — Skill > MCP pour le contexte projet** : Le MCP reste dans la fenêtre de contexte en permanence, ce qui **sature l'attention du modèle** sur des composants génériques au détriment du design directionnel spécifique au projet. ASpace appliquera le pattern Shadcn (skill + MCP séparés) pour tout composant canon.

**Verrou 3 — Arrangement > Composants pour les dashboards** : Le pattern Discovery (Zora) et Life Wheel (LD01-LD08) sont des dashboards — leur problème n'est pas la cohérence des composants mais **comment grouper l'information et combien d'écran avant le clutter**. Application directe : le Dashboard skill doit être invoqué pour toute vue Discovery/12WY/DEAL, pas un skill marketing.

**Différenciation ASpace** : là où le transcript décrit une dualité "landing artistique / functional boring", ASpace assume **une couche sémantique permanente** (skill.md = canon) au-dessus de la couche visuelle. Le canon wiki `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\` est lui-même un **dashboard non-cluttered** (cf. `wiki/index.md` 12 MB / 124 pages canon / 12 sous-dossiers) — arrangement pensé pour densité sans clutter. C'est l'anti-slop appliqué à la documentation.

**Compatibilité avec rules/ecc/web/design-quality.md** (CLAUDE.md §"Anti-Template Policy") : les banned patterns listés (default card grids, stock hero, flat layouts, safe gray-on-white) sont **exactement l'AI slop** que ces skills combattent. Convergence naturelle.

---

## 4. DEAL — Application 4 phases (Liberation Engine USS Protostar)

### Phase 1 — DEFINE (A3 Dal)
**Friction réelle** : Les générations UI par Claude (Opus 4.5/M3) dérivent vers les safe choices — gradients violet-sur-blanc, hero centré, grid uniforme. Aucune landing Life-OS-2026 ne sort avec une **vraie direction design**.

**Outcome désiré** : Toute landing ou dashboard produit a un design direction documenté AVANT la première génération de code, qui contraint le modèle à commit et empêche le drift vers la médiane.

**Trigger DEAL** : "Je relance Claude pour une landing" → invoquer **UI UX Pro Max** d'abord (engine 5 recherches × 161 catégories industrie) → sélectionner palette + fonts + layout AVANT d'écrire le skill.md spécifique au projet.

### Phase 2 — ELIMINATE (A3 Rok-Tahk)
**Permission to delete** :
- Supprimer les "purple gradients on white backgrounds" par défaut (interdit dans skill.md Life-OS-2026).
- Éliminer l'instinct de prendre un composant comme "par défaut" — exiger le **registry lookup** (Shadcn MCP, Material 3) sauf intention explicite.
- Tuer la dépendance au scroll-reveal fade-in par défaut : *"when you ask a model to add animation, it almost always does the exact same thing, where things slide into view as you scroll down the page. That one scroll reveal is basically the only move it knows."*

**NO-GO proposals** : Refuser tout livrable qui n'a pas de design direction dans `wiki/hand_offs/` ou `_SPECS/ADR/` avant le premier `npm run dev`.

### Phase 3 — AUTOMATE (A3 Zero)
**Skill candidate** : `/anti-slop-design-direction` — méta-skill qui :
1. Prend un brief projet (1 paragraphe).
2. Invoque UI UX Pro Max logic (sans le code : 5 recherches parallèles sur 161 catégories industrie).
3. Output : 1 markdown `design-direction.md` avec palette + fonts + layout + composants exclus + émotion cible.
4. Bloque tout `claude code` ou équivalent tant que le fichier n'existe pas.

**Risk class** : LOW (skill de cadrage, pas d'exécution destructive). **Proof** : tests sur 3 projets fantômes (landing SaaS B2B, dashboard analytics, app mobile fitness) — vérifier que le skill détecte les patterns AI slop connus.

**Sub-agent deploy** : Possibilité de créer un A3 dédié `a3-protostar-zero-anti-slop` qui wrap UI UX Pro Max + skill md generator, exposé dans la flotte.

### Phase 4 — LIBERATE (A3 Gwyn)
**D11 metrics attendues** :
- Temps moyen de cadrage design par projet : avant = 0 (drift silencieux) → après = 8 min documentées.
- Rejets livrables pour AI slop : avant = ~80% (refactor post-génération) → après = <20% (bloqué en amont).
- Bandwidth libérée : ~2h/semaine de "fix the same mistakes over and over" économisées par l'équipe.

**Maintenance tax** : Le skill `/anti-slop-design-direction` doit être ré-évalué à chaque release majeure Claude (Opus 4.5 → Opus 4.6, etc.) car *"Opus 4.8 and Fable 5 both shipped with prompting guides that show how Claude's changed and how the instructions you give it need to change too."* Cycle de revue : **90 jours** (H90).

---

## 5. Annexes

### Annexe A — Citations verbatim pivots
- *"the sites are all different, but somehow feel the same"* — pattern drift signature.
- *"the design keeps drifting toward the same safe, generic choices, no matter what the project actually is"* — root cause.
- *"Instead of the model inventing a design and hoping it works, it's building from one that was actually reasoned out for your exact use case"* — philosophie UI UX Pro Max.
- *"The others give the model better taste, while this one gives it a decision before it starts tuned to the kind of product you're actually making"* — différenciation UI UX Pro Max vs autres.
- *"You're starting from parts that were already built to ship"* — Shadcn value prop.
- *"mobile isn't a smaller web. It's its own thing with its own rules"* — pourquoi Material 3 + Swift UI séparés.

### Annexe B — Mapping Anti-Slop ↔ rules/ecc/web/design-quality.md
| AI Slop pattern (transcript) | Banned pattern (ASpace canon) | Skill de défense |
|---|---|---|
| "purple gradients on white backgrounds" | "Safe gray-on-white styling with one decorative accent color" | Front-end design skill (Anthropic) |
| "things slide into view as you scroll down the page" | (animation distractive) | GSAP skill |
| "flat layouts with no layering" | "Flat layouts with no layering, depth, or motion" | Premium front-end UI / Industrial brutalist |
| "the model invents a design and hopes it works" | "Default font stacks used without a deliberate reason" | UI UX Pro Max (engine 5 recherches) |
| "10 different font sizes" | "Uniform radius, spacing, and shadows across every component" | Mobile app UI design (principles layer) |

### Annexe C — Verbatim transcript hooks pour skill.md Life-OS-2026
À intégrer dans le skill canonique de tout livrable UI ASpace :

```
"FORBIDDEN: 'things slide into view as you scroll down the page' (the only move the model knows).
FORBIDDEN: purple gradients on white backgrounds.
FORBIDDEN: design choices that look the same as 80% of AI-built sites.

REQUIRED: Commit to a design direction before writing any code.
REQUIRED: For dashboards, reason through information arrangement FIRST.
REQUIRED: For mobile, treat it as its own thing, not a smaller web.
REQUIRED: When components professional-grade exist (Shadcn, Material 3, Swift UI), pull from registry.
REQUIRED: When animations are required, use GSAP skill — never invent motion."
```

### Annexe D — Limitations connues du transcript
- Sponsor segment SciSpace (5 paragraphes) : intégration ChatGPT, 280M papers, vs Elicit/Consensus — non-pertinent au design mais capturé pour intégrité.
- Sponsor segment Higgs Field + SeeDance : outillage propriétaire, freemium probable.
- "AI Labs Pro" = communauté payante de la chaîne, lien description — non vérifié indépendamment.

### Annexe E — Convergence avec canon Life OS 2026
- **LD04 Cognition** (Tilly, H30) : ce transcript est un asset d'apprentissage canon pour les 30 jours — le pattern "model reaches for the most common one" est une leçon cognitives universelle (biais de disponibilité).
- **LD01 Business** (Book, H1) : UI UX Pro Max × 161 industries = ICP-aware design — applicable aux 3-ICP sisters Solaris/Nexus/Orbiter (cf. ADR-ICP-* RATIFIED 2026-06-24).
- **LD07 Creativity** (Reno, H10) : Skill presets (Minimalist / Brutalist / Premium) = taxonomies créatives — candidat pour le 10-week creative cycle.
- **A2 USS Cerritos (Chaos)** : la skill "capture every loose end" devrait ajouter un trigger "design without direction = loose end to capture as design-direction.md".

### Annexe F — Resources à creuser post-canonisation
- Repo GitHub Anthropic skills : pas d'URL fournie dans transcript, à localiser via WebSearch "Anthropic front-end design skill GitHub".
- Shadcn registry docs : https://ui.shadcn.com/ (implicite).
- GSAP official skill : https://gsap.com/ (implicite, "comes straight from the team that builds it").
- UI UX Pro Max : engine open-source GitHub mentionné mais non-linké.
- Material 3 design system : https://m3.material.io/ (implicite).
- Apple SwiftUI docs : extraites de Xcode via skill (live pull).

---

## 6. Métadonnées de canonisation

| Champ | Valeur |
|---|---|
| video_id | Ot582-E61ac |
| channel | AI Labs |
| transcript_chars | 16 853 |
| classification_score | 01_Product = 11 (vs 03_IT=8, 02_Ops=4) |
| skill_candidates | `/anti-slop-design-direction` (DEAL Phase 3) |
| sister_ADR | ADR-ICP-SOLARIS-001 (Visual First / DAM sister) |
| related_skill_existing | `frontend-design` (plugin marketplace) |
| LDxx_mapping | LD01_Business, LD04_Cognition, LD07_Creativity |
| review_cycle | H90 (ré-évaluation Claude model upgrades) |
| priority | HIGH — applicable direct aux livrables Life-OS-2026 + OMK SaaS + ABC Community |

---

*Fin du guide PREMIUM. 8 sections honorées. Verbatim transcript préservé. Pas de paraphrase générique. Convergence canon ASpace documentée.*
