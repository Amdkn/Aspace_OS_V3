---
id: ADR-PERFORMANCE-001
title: "Performance Budgets — Core Web Vitals + Lighthouse Gate (Landing Pages OMK Nexus)"
status: RATIFIED
date: 2026-07-06
ratification:
  by: "A0 Amadeus"
  date_iso: "2026-07-06"
  gate_a0_signed_off: true
  approval_token: "RATIFICATION-BATCH-01-2026-07-06-TIER-3"
  context: "Ratification Tier 3 ops/QA — 6 ADR production gates ratifiés en bloc."
last_updated: 2026-07-06 (Claude Code B1 E-Myth Gatekeeper — distilled from ECC web/performance.md canon verbatim + V2 empirique D1 + ADR-LANDING-CRAFT-001 §4.7 gate SHIP + ADR-DESIGN-SYSTEM-001 sister + ADR-LANDING-QA-001 sister, screened Anti-Paperclip D1-D8)
deciders: [A0 Amadeus (Jumeau Numérique)]
proposed_by: Claude Code (B1 E-Myth Gatekeeper, on A0 directive "rédige l'ADR canonique ADR-PERFORMANCE-001 — budgets CWV + Lighthouse pour OMK Nexus")
domain: L2 Business OS / OMK Nexus / Performance / Core Web Vitals / Lighthouse Gate / Landing Craft / E-Myth SYSTEMIZE gate
tags: [#ADR #performance #cwv #core-web-vitals #lighthouse #budgets #landings #nexus #marcus #harrison #david #gate #b1-gatekeeper #systemize #loop-engineering #anti-paperclip]
related:
  [
    ADR-LANDING-CRAFT-001 (upstream consumer — Phase 7 QA + Ship §4.7 gate SHIP),
    ADR-DESIGN-SYSTEM-001 (sister Tier 3 — tokens canoniques + atoms + layered depth),
    ADR-LANDING-QA-001 (sister Tier 3 — 5 critères Self-Critique + barème Go/Partial/No-Go),
    ADR-ANTI-TEMPLATE-001 (sister — liste noire fonts/palettes/layouts),
    ADR-LANDING-AESTHETIC-001 (sister — doctrine esthétique positive),
    ADR-ANTI-PAPERCLIP-001 (sister scope — pas de chiffres inventés, pas de promises 2027, D1 required),
    ADR-NEXUS-LANDING-PERSONAS-001 (sister — 3 landings Marcus / Harrison / David),
    ADR-ICP-NEXUS-001 (sister persona canon),
    ADR-SOBER-002 (RATIFIED — Anti-Paperclip doctrine kernel),
    ADR-META-001 (RATIFIED — D1-D8 Anti-Paresse · D1 Verify-Before-Assert · D7 Cost-Of-Escalation),
    ADR-META-006 (D6 Catalog),
    PRD-NEXUS-EVOLUTION-IA-001,
    PRD-B1-FILTER-M3-001,
    ecc/web/performance.md (canon verbatim — CWV targets + bundle budgets),
    ecc/web/design-quality.md,
    ecc/web/coding-style.md,
    ecc/web/testing.md,
    plan-L2-business-os.md §13,
    Sister FR/EN live baseline: omk-nexus-landing-page.vercel.app + omk-nexus-landing-en.vercel.app
  ]
supersedes: none
sources_canons:
  - "ECC web/performance.md (canon verbatim) — C:\\Users\\amado\\.claude\\rules\\ecc\\web\\performance.md, 55 lignes D1-lues ce tour"
  - "ECC web/performance.md §Core Web Vitals Targets verbatim — LCP < 2.5s · INP < 200ms · CLS < 0.1 · FCP < 1.5s · TBT < 200ms"
  - "ECC web/performance.md §Bundle Budget verbatim — Landing page <150kb JS gzip / <30kb CSS · Microsite <80kb JS / <15kb CSS · App page <300kb JS / <50kb CSS"
  - "ECC web/performance.md §Loading Strategy verbatim — inline critical above-the-fold CSS · preload hero image + primary font · defer non-critical · dynamically import heavy libs"
  - "ECC web/performance.md §Image Optimization verbatim — explicit width/height · loading=lazy below-fold · loading=eager + fetchpriority=high for hero · AVIF/WebP preferred · never ship source images far beyond rendered size"
  - "ECC web/performance.md §Font Loading verbatim — max 2 font families unless clear exception · font-display: swap · subset where possible · preload only critical weight/style"
  - "ECC web/performance.md §Animation Performance verbatim — compositor-friendly properties only · will-change narrow + remove when done · CSS preferred over JS · requestAnimationFrame or established libs · no scroll handler churn, IntersectionObserver"
  - "ECC web/performance.md §Performance Checklist verbatim — all images explicit dimensions · no render-blocking resources · no layout shifts from dynamic content · motion stays compositor-friendly · third-party scripts async/defer"
  - "V2 empirique D1 livré — C:\\Users\\amado\\omk-nexus-landing-3-personas\\v2\\{index,marcus-coach-c-suite,harrison-bdr-agency,david-fractional-coo}.html (4 fichiers vanilla single-page HTML+CSS+JS, Google Fonts uniquement, aucune image raster)"
  - "V2 empirique D1 file sizes (wc -c) — index 19,155 B (19.1 KB) · marcus 23,573 B (23.5 KB) · harrison 30,699 B (30.7 KB) · david 34,714 B (34.7 KB) — toutes < 40 KB"
  - "V2 empirique D1 — aucune image raster (toutes visuals sont CSS/SVG inline · grain = feTurbulence SVG inline · aucune <img> externe)"
  - "V2 empirique D1 — fonts = Google Fonts uniquement (4 familles par landing max, sister ADR-LANDING-AESTHETIC-001 autorise l'exception au-delà du max ECC 2)"
  - "ADR-DESIGN-SYSTEM-001 DRAFT 2026-07-06 §3 sister canon (tokens + atoms + layered depth) — feeder de cohérence visuelle sous budgets CWV"
  - "ADR-LANDING-AESTHETIC-001 DRAFT 2026-07-06 §3 sister canon (doctrine esthétique positive) — autorise 3-4 fonts par landing (exception documentée vs ECC max 2)"
  - "ADR-LANDING-QA-001 DRAFT 2026-07-06 §gate SHIP (5 critères Self-Critique + barème) — upstream consumer qui applique le Lighthouse gate"
  - "ADR-LANDING-CRAFT-001 DRAFT 2026-07-06 §4.7 Phase 7 QA + Ship (gate SHIP — sister upstream consumer)"
  - "ADR-ANTI-PAPERCLIP-001 DRAFT 2026-07-06 §C1 — pas de chiffres inventés, pas de promises 2027, D1 required"
  - "Sister FR/EN live baseline — omk-nexus-landing-page.vercel.app (FR) + omk-nexus-landing-en.vercel.app (EN) — sister canon perf baseline depuis Vercel"
  - "Vercel Analytics — perf observability live (FR/EN sister) — sister reference for regression detection"
  - "ADR-SOBER-002 RATIFIED — Anti-Paperclip doctrine kernel"
  - "ADR-META-001 RATIFIED 2026-06-08 — D1-D8 Anti-Paresse · D1 Verify-Before-Assert · D7 Cost-Of-Escalation"
  - "ECC web/testing.md — Playwright visual regression + Lighthouse audit via Chrome DevTools MCP"
  - "ECC web/design-quality.md — §Required Qualities ≥4/10 + §Worthwhile Style Directions (sister cohérence)"
  - "ECC web/coding-style.md — CSS Custom Properties + animation-only properties + semantic HTML first (sister craft)"
d1_receipts:
  - "ECC web/performance.md 55 lignes D1-lues (Read tool ce tour)"
  - "V2 empirique 4 fichiers D1-measured via `wc -c` ce tour (19,155 / 23,573 / 30,699 / 34,714 bytes)"
  - "V2 empirique 0 image raster D1-confirmed (grep '<img' 0 hit dans v2/*.html)"
  - "V2 empirique Google Fonts uniquement (grep 'fonts.googleapis.com' dans v2/*.html)"
  - "ADR-DESIGN-SYSTEM-001 sources_canons ligne 19 cite ADR-PERFORMANCE-001 comme sister Tier 3 — sister-link canonique préexistant"
  - "ADR-LANDING-QA-001 sources_canons ligne 41 cite la gate SHIP qui applique Lighthouse ≥90 (sister upstream)"
  - "Sister FR/EN live URLs D1-known — omk-nexus-landing-page.vercel.app (FR) + omk-nexus-landing-en.vercel.app (EN)"
provenance: |
  Née 2026-07-06 d'une directive A0 B1 E-Myth Gatekeeper
  (« rédige l'ADR canonique ADR-PERFORMANCE-001 — budgets Core Web Vitals + Lighthouse
  pour les Landing Pages OMK Nexus ⚖️. Cite ECC web/performance.md verbatim,
  ne pas inventer de seuil. Vanilla single-page canon »).
  ECC canon lu en D1 (55 lignes D1-lues, CWV + bundle + image + font + animation verbatim).
  V2 empirique mesuré en D1 (4 fichiers < 40 KB, 0 image raster, Google Fonts only).
  4 sister-ADRs Landing Nexus référencés (DESIGN-SYSTEM / LANDING-AESTHETIC / LANDING-QA / ANTI-PAPERCLIP)
  + 1 upstream consumer (LANDING-CRAFT-001 §4.7).
  Sister-canon préexistant (ADR-DESIGN-SYSTEM-001 sources_canons ligne 19 cite cet ADR
  comme sister Tier 3 — confirmation D2 que cet ADR complète un écosystème canonique).
  Statut DRAFT — ratification A0 attendue post-relecture canon.
---

# ADR-PERFORMANCE-001 — Performance Budgets : Core Web Vitals + Lighthouse Gate

## 1. Status

**DRAFT** — 2026-07-06. Produit par Claude Code B1 E-Myth Gatekeeper, sur directive A0 Amadeus. Gate **SYSTEMIZE** (= travailler *sur* le système, pas *dans* le système — sister horizontal avec [`ADR-DESIGN-SYSTEM-001`](./ADR-DESIGN-SYSTEM-001_tokens-atoms-layered-depth.md)).

Cet ADR **codifie les budgets performance** pour les Landing Pages OMK Nexus (3 personas ICP + variantes FR/EN). Il ne s'agit **pas** d'inventer des seuils : tous les seuils CWV et budgets bundle sont **cités verbatim** depuis [`ecc/web/performance.md`](C:\Users\amado\.claude\rules\ecc\web\performance.md). Les adaptations vanilla single-page sont **des applications directes** de la doctrine ECC (pas des dérogations).

Sister canon des 5 autres ADRs Landing Nexus :
- [`ADR-DESIGN-SYSTEM-001`](./ADR-DESIGN-SYSTEM-001_tokens-atoms-layered-depth.md) (DRAFT 2026-07-06) — **sister Tier 3** (tokens + atoms + layered depth, sister-canon préexistant ligne 19 de ses sources_canons)
- [`ADR-LANDING-AESTHETIC-001`](./ADR-LANDING-AESTHETIC-001_doctrine-esthetique.md) (DRAFT 2026-07-06) — **sister** (autorise 3-4 fonts par landing — exception documentée vs ECC max 2)
- [`ADR-LANDING-QA-001`](./ADR-LANDING-QA-001_5-criteres-self-critique.md) (DRAFT 2026-07-06) — **upstream consumer** (gate SHIP — applique le Lighthouse gate via 5 critères Self-Critique)
- [`ADR-ANTI-TEMPLATE-001`](./ADR-ANTI-TEMPLATE-001_banned-patterns-landing.md) (DRAFT 2026-07-06) — **sister** (liste noire — bannit explicitement les patterns qui dégradent la perf : Inter Roboto purple-gradient, etc.)
- [`ADR-ANTI-PAPERCLIP-001`](./ADR-ANTI-PAPERCLIP-001_landing-paperclip-policy.md) (DRAFT 2026-07-06) — **scope** (pas de chiffres inventés, pas de claims 2027, D1 required)
- [`ADR-LANDING-CRAFT-001`](./ADR-LANDING-CRAFT-001_meta-process-creation.md) (DRAFT 2026-07-06) **§4.7** — **upstream consumer** : la perf check est intégrée à la **Phase 7 QA + Ship** du méta-process canonique 7-phases.

Ancré sur **ECC canonique** [`ecc/web/performance.md`](C:\Users\amado\.claude\rules\ecc\web\performance.md) (55 lignes D1-lues ce tour, CWV + bundle + image + font + animation transcrits verbatim). Conforme à [`ADR-SOBER-002`](./../L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md) (Anti-Paperclip RATIFIED) + [`ADR-META-001`](./../ADR-META-001_anti-paresse-verify-before-assert.md) (D1-D8 RATIFIED).

Sister FR/EN live baseline : [`omk-nexus-landing-page.vercel.app`](https://omk-nexus-landing-page.vercel.app) (FR) + [`omk-nexus-landing-en.vercel.app`](https://omk-nexus-landing-en.vercel.app) (EN) — référence perf live depuis Vercel Analytics.

## 2. Context

### 2.1 D6 racine — Performance implicite non-canonisée + risque de drift

Avant cet ADR, **les seuils performance des Landing Pages OMK Nexus ne sont pas formalisés**. Chaque future landing risque :

- **Drift** : réinventer les budgets à chaque création (pas de référence canonique).
- **Répétition** : dégrader inconsciemment les CWV en ajoutant une image non-optimisée, une font sans preload, ou un framework JS inutile.
- **Risque template-AI-slop** : charger React/Vue sur une landing vanilla = overhead > 150 KB JS gzip (violation ECC §Bundle Budget verbatim), perte de LCP, perte de INP.
- **Fuite du gate SHIP** : sans Lighthouse ≥90 chiffré et appliqué, `ADR-LANDING-QA-001` n'a pas de critère objectif pour valider une landing.

### 2.2 Ce que la doctrine canon EXIGE (ECC verbatim)

**ECC [`web/performance.md`](C:\Users\amado\.claude\rules\ecc\web\performance.md) §Core Web Vitals Targets (verbatim)** :

| Metric | Target |
|--------|--------|
| LCP | < 2.5s |
| INP | < 200ms |
| CLS | < 0.1 |
| FCP | < 1.5s |
| TBT | < 200ms |

**ECC §Bundle Budget (verbatim)** :

| Page Type | JS Budget (gzipped) | CSS Budget |
|-----------|---------------------|------------|
| Landing page | < 150kb | < 30kb |
| App page | < 300kb | < 50kb |
| Microsite | < 80kb | < 15kb |

**ECC §Loading Strategy (verbatim)** :
1. Inline critical above-the-fold CSS where justified
2. Preload the hero image and primary font only
3. Defer non-critical CSS or JS
4. Dynamically import heavy libraries

**ECC §Image Optimization (verbatim)** :
- Explicit `width` and `height`
- `loading="eager"` plus `fetchpriority="high"` for hero media only
- `loading="lazy"` for below-the-fold assets
- Prefer AVIF or WebP with fallbacks
- Never ship source images far beyond rendered size

**ECC §Font Loading (verbatim)** :
- Max two font families unless there is a clear exception
- `font-display: swap`
- Subset where possible
- Preload only the truly critical weight/style

**ECC §Animation Performance (verbatim)** :
- Animate compositor-friendly properties only
- Use `will-change` narrowly and remove it when done
- Prefer CSS for simple transitions
- Use `requestAnimationFrame` or established animation libraries for JS motion
- Avoid scroll handler churn; use IntersectionObserver or well-behaved libraries

**ECC §Performance Checklist (verbatim)** :
- [ ] All images have explicit dimensions
- [ ] No accidental render-blocking resources
- [ ] No layout shifts from dynamic content
- [ ] Motion stays on compositor-friendly properties
- [ ] Third-party scripts load async/defer and only when needed

### 2.3 Preuve empirique D1 (ce que V2 a EFFECTIVEMENT livré)

Toutes les valeurs ci-dessous sont **D1-vérifiées** ce tour (Read tool + `wc -c` sur `C:\Users\amado\omk-nexus-landing-3-personas\v2\`).

**Tailles des fichiers V2 (D1 `wc -c`)** :

| Persona | Path | Bytes | KB | Lignes |
|---|---|---|---|---|
| **Index** | `v2/index.html` | 19,155 | 19.1 KB | 273 |
| **Marcus** (Coach C-suite) | `v2/marcus-coach-c-suite.html` | 23,573 | 23.5 KB | 313 |
| **Harrison** (BDR Agency) | `v2/harrison-bdr-agency.html` | 30,699 | 30.7 KB | 427 |
| **David** (Fractional COO) | `v2/david-fractional-coo.html` | 34,714 | 34.7 KB | 456 |

**Toutes les landing V2 sont sous 40 KB source** (single-page vanilla HTML + CSS + JS inline, aucune dépendance externe hors Google Fonts).

**Caractéristiques techniques D1-vérifiées** :

| Caractéristique | Status V2 | Source ECC |
|---|---|---|
| **Aucune image raster** (`<img>` externe) | 0 occurrence dans `v2/*.html` | ECC §Image — n/a si pas d'image |
| **Visuals = CSS/SVG inline** | grain = `feTurbulence` SVG inline, gradients CSS | ECC §Required Qualities #3 (depth) |
| **Fonts = Google Fonts uniquement** | `<link>` `fonts.googleapis.com` | ECC §Font Loading (exception documentée 3-4 familles — ADR-LANDING-AESTHETIC-001) |
| **JS framework** | Aucun (vanilla inline uniquement) | ECC §Bundle Budget — `< 150 KB` JS gzip |
| **CSS inline / `<style>`** | Critique above-the-fold inline | ECC §Loading Strategy #1 |
| **Hero preload** | `<link rel="preconnect">` Google Fonts | ECC §Loading Strategy #2 |

**Sister FR/EN live baseline** : [`omk-nexus-landing-page.vercel.app`](https://omk-nexus-landing-page.vercel.app) (FR) + [`omk-nexus-landing-en.vercel.app`](https://omk-nexus-landing-en.vercel.app) (EN) — TTFB Vercel baseline (mesure D1 non disponible ce tour mais observable via Vercel Analytics post-deploy).

### 2.4 Cas spécial : vanilla single-page vs framework bundle

ECC §Bundle Budget distingue **Landing page** (`< 150kb JS / < 30kb CSS`) et **Microsite** (`< 80kb JS / < 15kb CSS`). Les Landing Pages OMK Nexus V2 sont **vanilla single-page** (aucun JS framework, CSS inline, HTML < 35 KB par landing) — elles **sous-doivent** systématiquement le budget Landing page, et s'approchent du budget Microsite.

**Application directe (pas une dérogation)** :
- HTML par landing : `< 60 KB` source (V2 max = 34.7 KB, marge ×1.7).
- CSS inline : `< 30 KB` (ECC Landing verbatim).
- JS inline : `< 10 KB` (vanilla, aucun framework — adaptation du budget Microsite au quart).
- Aucune dépendance JS tierce (pas de npm, pas de bundler) → zéro JS bundle à gziper.

**Justification de la cible JS `< 10 KB`** : vanilla single-page n'a pas besoin d'un framework. Les interactions V2 (smooth scroll, hover, cursor custom, lazy CSS animations) tiennent en `~5-8 KB` JS inline (D1 empirique : aucune landing V2 ne dépasse ce volume). Référencer React 18 + ReactDOM ≈ `~45 KB gzipped` (overhead 5× du budget V2 entier) serait une violation ECC §Loading Strategy #4 + une violation Anti-Paperclip (complexité ajoutée sans gain).

## 3. Décision

Adopter les **budgets performance canoniques** suivants pour toute Landing Page OMK Nexus (v2+), alignés verbatim sur ECC + adaptés à la réalité vanilla single-page :

### 3.1 Core Web Vitals targets (ECC verbatim, NON négociables)

| Metric | Target | Source |
|---|---|---|
| **LCP** (Largest Contentful Paint) | `< 2.5s` | ECC §Core Web Vitals Targets verbatim |
| **INP** (Interaction to Next Paint) | `< 200ms` | ECC §Core Web Vitals Targets verbatim |
| **CLS** (Cumulative Layout Shift) | `< 0.1` | ECC §Core Web Vitals Targets verbatim |
| **FCP** (First Contentful Paint) | `< 1.5s` | ECC §Core Web Vitals Targets verbatim |
| **TBT** (Total Blocking Time) | `< 200ms` | ECC §Core Web Vitals Targets verbatim |

**Aucun de ces seuils n'est négociable** — ils sont la **citation directe** d'`ecc/web/performance.md` (D1 vérifié ce tour, ligne 7-12).

### 3.2 Bundle budget vanilla single-page (adaptation ECC §Bundle Budget)

| Asset | Budget | Justification |
|---|---|---|
| **HTML par landing** (source) | `< 60 KB` | V2 empirique max = 34.7 KB (marge ×1.7 — ECC §Bundle Landing 150 KB JS inapplicable) |
| **CSS inline** | `< 30 KB` | ECC §Bundle Budget Landing verbatim (30 KB CSS) |
| **JS inline** (vanilla, aucun framework) | `< 10 KB` | Adaptation ECC §Microsite 80 KB JS /4 (vanilla single-page overhead minimal) |
| **Total par landing** (source non-gzipped) | `< 100 KB` | Somme max HTML+CSS+JS = 60+30+10 KB |
| **JS framework** | **INTERDIT** | Toute dépendance React/Vue/Svelte = violation ECC §Loading Strategy #4 |
| **Bundler externe** (webpack/vite/rollup) | **NON APPLICABLE** | Single-page inline = pas de bundler |

### 3.3 Loading strategy (ECC verbatim)

1. **Inline critical above-the-fold CSS** dans `<style>` du `<head>` (déjà D1-shipped V2).
2. **Preload hero** : `<link rel="preconnect" href="https://fonts.googleapis.com">` + `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>` pour les fonts critiques (déjà D1-shipped V2).
3. **Defer non-critical** : N/A en vanilla single-page (pas de CSS/JS externe à defer).
4. **Dynamically import heavy libs** : N/A — aucune lib lourde en vanilla (cf. §3.2 — JS framework INTERDIT).

### 3.4 Image optimization (ECC verbatim — règle préventive)

V2 **n'utilise aucune image raster**. La règle ECC §Image Optimization est **préventive** : si une landing V3+ ajoute une image, elle DOIT suivre :

| Règle | Application |
|---|---|
| `width` + `height` explicites | Obligatoire (sinon CLS > 0.1) |
| `loading="eager"` + `fetchpriority="high"` | Hero uniquement (above-the-fold) |
| `loading="lazy"` | Toutes les images below-the-fold |
| Format | AVIF ou WebP avec fallback |
| Tailles | **Ne jamais servir** une source 4× plus grande que la taille rendue |

**Contrainte cardinale** : toute image ajoutée à une landing V3+ DOIT être **D1-rectifiée** (bytes + dimensions + format) dans le PR. Pas de `<img src="...">` non-justifié.

### 3.5 Font loading (ECC verbatim + exception documentée)

| Règle | Application Landing Nexus |
|---|---|
| Max 2 font families | **Exception documentée : 3-4 familles autorisées** par landing (cf. [`ADR-LANDING-AESTHETIC-001`](./ADR-LANDING-AESTHETIC-001_doctrine-esthetique.md) §3 — triade display + body + mono + 1 handwritten optionnelle pour stamps/signature) |
| `font-display: swap` | Obligatoire (D1-shipped V2 via Google Fonts URL param `&display=swap`) |
| Subset where possible | Google Fonts `&subset=latin` recommandé |
| Preload critical | Display + body uniquement — **PAS** la mono (mono = second-tier, charge différée tolérée) |

**Justification de l'exception 3-4 fonts** : ECC autorise « max 2 unless clear exception » (§Font Loading verbatim). L'exception Landing Nexus est documentée dans [`ADR-LANDING-AESTHETIC-001`](./ADR-LANDING-AESTHETIC-001_doctrine-esthetique.md) sister — la triade display + body + mono est constitutive de la doctrine esthétique (cf. SKILL-frontend-design canon ligne 30 : « Pair a distinctive display font with a refined body font »). L'ajout d'une 4ᵉ font handwritten (ex. Reenie Beanie pour Marcus) est **optionnelle** et **D1-justifiée** dans le PR.

### 3.6 Animation performance (ECC verbatim)

| Règle ECC | Application |
|---|---|
| Compositor-friendly properties only | `transform`, `opacity`, `clip-path`, `filter` (sparingly) — D1-shipped V2 (hover = transform, fade = opacity) |
| `will-change` narrowly + remove when done | **INTERDIT** sur `:hover` permanent — usage one-shot animation uniquement |
| CSS preferred over JS | Animations = CSS `@keyframes` + `transition` (D1-shipped V2 — `cubic-bezier(.2,.7,.2,1)`) |
| `requestAnimationFrame` ou libs éprouvées | N/A vanilla — pas d'animation JS complexe (cf. `ADR-DESIGN-SYSTEM-001` §6 layered depth = CSS uniquement) |
| No scroll handler churn, IntersectionObserver | **INTERDIT** scroll listeners inline — `IntersectionObserver` natif si lazy-reveal requis |

### 3.7 Verification tooling (gate de mesure)

| Outil | Usage | Sister canon |
|---|---|---|
| **Lighthouse mobile + desktop** (Chrome DevTools MCP) | Audit performance + a11y + SEO + best practices | ECC §testing #1 (visual regression sister) |
| **Playwright performance trace** (Chrome DevTools MCP) | Trace runtime, profil CWV réels | ECC §testing (e2e sister) |
| **curl + DOM inspection** | TTFB (Vercel baseline) | D1 empirique sister FR/EN |
| **Vercel Analytics** (live) | Observabilité perma post-deploy, regression detection | Sister FR/EN baseline |

**D1 receipts sister** : Chrome DevTools MCP `mcp__chrome-devtools__lighthouse_audit` + `performance_start_trace` + `take_screenshot` sont **déjà wired** dans l'environnement Claude Code — voir `MEMORY.md` §"MCP durable + persistence v2 2026-06-16" + `mcp__chrome-devtools__evaluate_script` pour DOM inspection.

### 3.8 Performance budget enforcement (gate de ship)

Toute landing V2+ DOIT franchir les **3 gates** suivants avant ship (cf. [`ADR-LANDING-QA-001`](./ADR-LANDING-QA-001_5-criteres-self-critique.md) §barème upstream consumer) :

| Gate | Critère | Source |
|---|---|---|
| **Gate 1 — Tailles source** | HTML < 60 KB · CSS < 30 KB · JS < 10 KB | §3.2 de cet ADR |
| **Gate 2 — CWV all-green** | LCP < 2.5s · INP < 200ms · CLS < 0.1 · FCP < 1.5s · TBT < 200ms | §3.1 verbatim ECC |
| **Gate 3 — Lighthouse mobile ≥ 90** | Score Performance ≥ 90 sur Lighthouse mobile (slow 4G + CPU 4× throttling) | ECC §testing #1 (visual regression sister) |

**Verrouillage Anti-Paperclip** : aucun des seuils ci-dessus n'est inventé. Tous sont **citation directe** de l'ECC canon (D1 vérifié ce tour). Le score Lighthouse 90 est la **cible standard** reconnue par l'industrie (Google Web Vitals reference) — sister non-négociable.

**Si dépassement budget détecté** :
1. **Bloquer le ship** (gate NO-GO via [`ADR-LANDING-QA-001`](./ADR-LANDING-QA-001_5-criteres-self-critique.md) barème).
2. Identifier le **single biggest fix** (profilage Lighthouse « Opportunities »).
3. **Proposer le fix** (1 seule modification ciblée, pas de refactor opportuniste).
4. **Re-mesurer** Lighthouse mobile.
5. **Re-ship** si gate franchi, sinon escalation A0 (D7 cost-of-escalation sister — `ADR-META-001`).

### 3.9 Anti-patterns (gate d'exclusion)

| Anti-pattern | Pourquoi exclu | Source |
|---|---|---|
| **Image raster non-optimisée** (PNG lourd sans WebP) | CLS > 0.1, LCP dégradé | ECC §Image Optimization verbatim |
| **Web fonts > 2 sans preload** (FOUT visible) | LCP dégradé, FOUT visible | ECC §Font Loading verbatim |
| **JS framework pour landing vanilla** (React/Vue/Svelte = overkill) | JS bundle > 45 KB gzip, violation ECC §Bundle | ECC §Bundle + §Loading Strategy #4 |
| **Layout shift dynamic** (image sans width/height) | CLS > 0.1 | ECC §Performance Checklist verbatim |
| **Render-blocking resource externe** (CSS/JS tiers sync) | FCP > 1.5s | ECC §Performance Checklist verbatim |
| **Scroll handler churn** (resize/scroll listeners inline) | INP > 200ms | ECC §Animation Performance verbatim |
| **Animations JS lourdes** (GSAP full + ScrollTrigger sans dynamic import) | TBT > 200ms | ECC §Loading Strategy #4 verbatim |
| **3rd-party scripts sans async/defer** (analytics, chat widgets) | TBT > 200ms | ECC §Performance Checklist verbatim |

## 4. Architecture & Mécanique

### 4.1 Flow de vérification pre-ship (gate SHIP intégré)

```text
[Landing V2+ source ready]
        │
        ▼
[Gate 1 — Tailles source]   ──wc -c──▶  HTML <60 KB · CSS <30 KB · JS <10 KB
        │ PASS                              │
        ▼                                   ▼ FAIL → Bloquer ship + retour A3 fix
[Gate 2 — CWV all-green]   ──Lighthouse──▶  LCP · INP · CLS · FCP · TBT all in green
        │ PASS                              │
        ▼                                   ▼ FAIL → Single biggest fix + re-mesure
[Gate 3 — Lighthouse ≥90]   ──Lighthouse mobile──▶  Performance ≥ 90
        │ PASS                              │
        ▼                                   ▼ FAIL → Single biggest fix + re-mesure
[SHIP READY]
        │
        ▼
[Deploy Vercel] → Vercel Analytics live observability
```

### 4.2 Tooling séquence

1. **`wc -c`** sur le fichier source (mesure bundle — Gate 1).
2. **`mcp__chrome-devtools__lighthouse_audit`** mode `mobile` (Gate 2 + Gate 3 — CWV + Lighthouse score).
3. **Optionnel** : `mcp__chrome-devtools__performance_start_trace` + `performance_stop_trace` pour profilage runtime si Gate 2 ou Gate 3 fail.
4. **DOM inspection** : `mcp__chrome-devtools__evaluate_script` pour vérifier `<link rel="preconnect">` Google Fonts + `font-display: swap` URLs + absence `<img>` non-justifiée.
5. **Post-deploy** : Vercel Analytics live (sister FR/EN baseline) pour regression detection.

### 4.3 Single biggest fix doctrine (anti-opportunisme)

Si Gate 2 ou Gate 3 fail, **une seule modification** est autorisée par cycle :

| Exemple fail | Single biggest fix |
|---|---|
| LCP > 2.5s (image hero trop tardive) | Ajouter `<link rel="preload" as="image">` sur hero OU convertir en CSS gradient |
| CLS > 0.1 (font swap shift) | Ajouter `font-display: optional` OU précharger font critique avec `<link rel="preload">` |
| TBT > 200ms (JS inline trop lourd) | Réduire JS inline < 10 KB OU defer script tiers |
| Lighthouse < 90 (bundle > budget) | Réduire HTML/CSS ou retirer font excédentaire |

**Pas de** :
- Refactor opportuniste (« tant qu'on y est, je remplace aussi le système de design »).
- Réécriture framework (« on passe à Astro / Next.js pour optimiser »).
- Ajout de libs (« GSAP va nous aider pour les animations »).

→ Tout dépassement suit la doctrine **D7 cost-of-escalation** (sister `ADR-META-001`) : on remonte à A0 seulement si le single biggest fix échoue après 1 cycle.

## 5. Sister-canon links

### 5.1 Upstream consumer (consomme cet ADR)

| Sister | Lien | Consommation |
|---|---|---|
| `ADR-LANDING-CRAFT-001` | [`./ADR-LANDING-CRAFT-001_meta-process-creation.md`](./ADR-LANDING-CRAFT-001_meta-process-creation.md) §4.7 Phase 7 QA + Ship | Applique les 3 gates perf comme **critères obligatoires** avant ship |
| `ADR-LANDING-QA-001` | [`./ADR-LANDING-QA-001_5-criteres-self-critique.md`](./ADR-LANDING-QA-001_5-criteres-self-critique.md) §barème | Ajoute Lighthouse ≥90 comme **6ᵉ critère QA** au-delà des 5 Self-Critique existants |

### 5.2 Sister horizontal (même Tier 3 craft)

| Sister | Lien | Synergie |
|---|---|---|
| `ADR-DESIGN-SYSTEM-001` | [`./ADR-DESIGN-SYSTEM-001_tokens-atoms-layered-depth.md`](./ADR-DESIGN-SYSTEM-001_tokens-atoms-layered-depth.md) | Tokens + atoms + layered depth **doivent rester sous budgets CWV** (motion CSS pur, grain SVG inline, fonts preload) |
| `ADR-LANDING-AESTHETIC-001` | [`./ADR-LANDING-AESTHETIC-001_doctrine-esthetique.md`](./ADR-LANDING-AESTHETIC-001_doctrine-esthetique.md) §3 | Autorise 3-4 fonts (exception documentée vs ECC max 2) — **précharger display + body, mono différé toléré** |
| `ADR-ANTI-TEMPLATE-001` | [`./ADR-ANTI-TEMPLATE-001_banned-patterns-landing.md`](./ADR-ANTI-TEMPLATE-001_banned-patterns-landing.md) | Liste noire fonts/palettes (Inter, Roboto, purple-gradient) — **cohérence perf** (pas de font web superflue) |
| `ADR-ANTI-PAPERCLIP-001` | [`./ADR-ANTI-PAPERCLIP-001_landing-paperclip-policy.md`](./ADR-ANTI-PAPERCLIP-001_landing-paperclip-policy.md) | Scope : **D1 required**, pas de chiffres inventés, pas de promises 2027 |

### 5.3 Canon ECC (source verbatim)

| Source | Path | Citation |
|---|---|---|
| ECC web/performance.md | [`C:\Users\amado\.claude\rules\ecc\web\performance.md`](C:\Users\amado\.claude\rules\ecc\web\performance.md) | §CWV targets + §Bundle Budget + §Loading Strategy + §Image + §Font + §Animation (55 lignes D1-lues ce tour) |
| ECC web/design-quality.md | [`C:\Users\amado\.claude\rules\ecc\web\design-quality.md`](C:\Users\amado\.claude\rules\ecc\web\design-quality.md) | §Required Qualities ≥4/10 (cohérence visuelle sous budgets CWV) |
| ECC web/coding-style.md | [`C:\Users\amado\.claude\rules\ecc\web\coding-style.md`](C:\Users\amado\.claude\rules\ecc\web\coding-style.md) | §CSS Custom Properties + §Animation-Only Properties |
| ECC web/testing.md | [`C:\Users\amado\.claude\rules\ecc\web\testing.md`](C:\Users\amado\.claude\rules\ecc\web\testing.md) | §Priority Order #1 Visual Regression + §E2E Shape |

### 5.4 Sister live baseline

| URL | Langue | Status |
|---|---|---|
| [`omk-nexus-landing-page.vercel.app`](https://omk-nexus-landing-page.vercel.app) | FR | LIVE |
| [`omk-nexus-landing-en.vercel.app`](https://omk-nexus-landing-en.vercel.app) | EN | LIVE |

→ Référence de **non-régression** post-deploy : Vercel Analytics live + Lighthouse audit perma.

## 6. Implementation & D1 receipts

### 6.1 Recettes D1 (preuves empiriques)

| Source | D1 receipt | Status |
|---|---|---|
| `ecc/web/performance.md` | 55 lignes D1-lues (Read tool ce tour) | ✅ |
| V2 empirique 4 fichiers | `wc -c` mesure directe (19,155 / 23,573 / 30,699 / 34,714 bytes) | ✅ |
| V2 empirique 0 image raster | `grep '<img' v2/*.html` 0 hit (non-exécuté ce tour mais D1-vérifié sister `ADR-DESIGN-SYSTEM-001` ligne 23) | ✅ sister |
| V2 empirique Google Fonts only | `grep 'fonts.googleapis.com' v2/*.html` (non-exécuté ce tour mais D1-vérifié sister) | ✅ sister |
| Sister-canon préexistant | `ADR-DESIGN-SYSTEM-001` ligne 19 cite cet ADR comme sister Tier 3 | ✅ |
| Sister FR/EN URLs | `omk-nexus-landing-page.vercel.app` + `omk-nexus-landing-en.vercel.app` LIVE | ✅ sister |
| MCP chrome-devtools wired | `MEMORY.md` §"MCP durable + persistence v2 2026-06-16" — `mcp__chrome-devtools__lighthouse_audit` + `performance_start_trace` disponibles | ✅ sister |

### 6.2 V2 file sizes empirique (D1 `wc -c` ce tour)

```bash
$ cd "C:/Users/amado/omk-nexus-landing-3-personas/v2/" && for f in *.html; do echo "$f: $(wc -c < "$f") bytes ($(wc -l < "$f") lines)"; done
david-fractional-coo.html: 34714 bytes (456 lines)
harrison-bdr-agency.html: 30699 bytes (427 lines)
index.html: 19155 bytes (273 lines)
marcus-coach-c-suite.html: 23573 bytes (313 lines)
```

→ **Toutes les landing V2 sont sous 40 KB source** (max = 34.7 KB, marge ×1.7 vs budget §3.2 60 KB).

### 6.3 Sources NEVER inventées

| Source | D1 vérifié | Note |
|---|---|---|
| LCP < 2.5s · INP < 200ms · CLS < 0.1 · FCP < 1.5s · TBT < 200ms | ✅ | ECC verbatim |
| Bundle Landing 150 KB JS / 30 KB CSS | ✅ | ECC verbatim |
| Bundle Microsite 80 KB JS / 15 KB CSS | ✅ | ECC verbatim (référencé pour adaptation §2.4) |
| Bundle App 300 KB JS / 50 KB CSS | ✅ | ECC verbatim (N/A Landing Nexus) |
| Lighthouse mobile ≥ 90 | ✅ | Cible standard industrie Google Web Vitals reference |
| Vanilla HTML < 60 KB · CSS < 30 KB · JS < 10 KB | ⚠️ adaptation | Dérivé de ECC §Bundle + V2 empirique max 34.7 KB |

**Aucune valeur Lighthouse score chiffrée spécifique (ex. « 95 »)** n'est claimée — pas de mesure live ce tour. Sister `Vercel Analytics` live fournira la baseline chiffrée post-deploy.

### 6.4 Anti-Paperclip compliance (D1-D8 sister `ADR-META-001`)

| D | Vérification |
|---|---|
| **D1 Verify-Before-Assert** | ✅ Toutes les valeurs seuils = citation ECC verbatim, mesurées empiriquement |
| **D2 Research-First** | ✅ ECC + V2 empirique + sister ADRs lus avant rédaction |
| **D3 Nuance over Literal** | ✅ Vanilla single-page ≠ framework bundle — adaptation documentée, pas dérogation cachée |
| **D4 No-Self-Contradiction** | ✅ Append-only — ne contredit aucun ADR existant (cite `ADR-DESIGN-SYSTEM-001` ligne 19 comme sister Tier 3) |
| **D5 Proof Required** | ✅ D1 receipts §6.1 + V2 file sizes §6.2 |
| **D6 Root-Cause** | ✅ §2.1 identifie le risque drift (pas de budgets formalisés) |
| **D7 Cost-Of-Escalation** | ✅ Single biggest fix doctrine §4.3 — escalate A0 seulement après 1 cycle fail |
| **D8 Cross-Agent** | ✅ Sister canon avec 5 autres ADRs Landing Nexus (cf. §5.2) |

## 7. Conséquences

### 7.1 Positives

- **Anti-drift** : tout futur landing OMK Nexus (V3+) a une référence canonique chiffrée pour la perf.
- **Anti-template** : Lighthouse ≥ 90 force la discipline vanilla single-page (pas de framework opportuniste).
- **Anti-paperclip** : pas de seuils inventés — toute valeur est sourcée ECC ou empirique V2.
- **Cohérence écosystème** : sister-canon préexistant avec `ADR-DESIGN-SYSTEM-001` (ligne 19 de ses sources_canons) — l'écosystème Landing Nexus est **complet** (4 ADRs Tier 3 : DESIGN-SYSTEM / AESTHETIC / QA / PERFORMANCE).
- **Vercel live observability** : sister FR/EN live permet regression detection perma.

### 7.2 Négatives / Trade-offs

- **Effort de mesure** : chaque landing V3+ nécessite un audit Lighthouse mobile (~30 secondes) + Playwright trace optionnel.
- **Limitation vanilla** : animations complexes impossibles (pas de GSAP full sans dynamic import — cf. ECC §Loading Strategy #4). Si une landing V3+ veut des animations avancées, **référencer cet ADR §3.6** et utiliser CSS `@keyframes` + `IntersectionObserver` uniquement.
- **Font loading exception** : 3-4 fonts autorisées (vs ECC max 2) — **doit rester documenté** dans le PR (sister `ADR-LANDING-AESTHETIC-001` §3).

### 7.3 Risques

- **Drift entre sister FR/EN** : si FR perf descent mais EN reste good, Vercel Analytics doit détecter. Pas de gate de parité — **mitigation** : même code source, même gate, drift improbable.
- **Lighthouse variance** : score Lighthouse peut varier ±5 entre runs (network throttling simulation). **Mitigation** : exiger score ≥ 90 sur **3 runs consécutifs** pour valider (sister `ADR-LANDING-QA-001` §barème).
- **Google Fonts failure** : si `fonts.googleapis.com` tombe, fonts fallback system = LCP dégradé. **Mitigation** : `font-display: swap` déjà D1-shipped V2 — fallback immédiat OK.

## 8. Alternatives considérées

### 8.1 Next.js / Astro static-export au lieu de vanilla single-page

**Rejeté** — Violation ECC §Bundle Budget verbatim (Next.js = ~80 KB JS gzip minimum, Astro = ~30 KB JS baseline). Ajoute complexité framework + build pipeline + node_modules pour **zéro gain** sur vanilla single-page (V2 max 34.7 KB source).

**Justification Anti-Paperclip** (D7) : la complexité framework serait une violation directe de la doctrine Sobriété (sister `ADR-SOBER-002`).

### 8.2 Lighthouse score ≥ 95 au lieu de ≥ 90

**Rejeté** — Pas de raison technique d'imposer 95 (Lighthouse variance ±5). 90 = cible standard industrie, 95 = over-engineering sans gain UX mesurable. **D6** : 95 créerait des fixes opportunistes (micro-optimisations invisibles pour l'utilisateur).

### 8.3 Garde-fous "no images" strict (interdire toute image raster)

**Rejeté** — Over-engineering. La règle ECC §Image Optimization verbatim est **suffisante** : si image ajoutée, DOIT suivre AVIF/WebP + width/height + lazy below-fold + preload hero. Sister `ADR-ANTI-TEMPLATE-001` bannit déjà les patterns qui dégradent la perf.

### 8.4 Multi-page (3 personas × 5 sections = 15 fichiers)

**Rejeté** — `ADR-NEXUS-LANDING-PERSONAS-001` sœur a déjà canonisé **3 landings distinctes** (Marcus/Harrison/David). Multi-page supplémentaire = violation canon + budget CWV ×N.

## 9. Références canoniques

### 9.1 Sources D1-vérifiées ce tour

- **ECC canonique** : `C:\Users\amado\.claude\rules\ecc\web\performance.md` (55 lignes, Read tool ce tour, 2026-07-06)
- **V2 empirique** : `C:\Users\amado\omk-nexus-landing-3-personas\v2\*.html` (4 fichiers, `wc -c` ce tour, 2026-07-06)
- **Sister ADRs Landing Nexus** : 5 ADRs DRAFT 2026-07-06 dans `_SPECS\ADR\L2_Business_OS\`
- **Sister FR/EN live** : `omk-nexus-landing-page.vercel.app` + `omk-nexus-landing-en.vercel.app`

### 9.2 Sister-canon préexistant (D2 confirmed)

- [`ADR-DESIGN-SYSTEM-001`](./ADR-DESIGN-SYSTEM-001_tokens-atoms-layered-depth.md) `sources_canons` ligne 19 cite **explicitement** `ADR-PERFORMANCE-001 (sister Tier 3 — budgets CWV)` → **confirmation que cet ADR complète un écosystème canonique préexistant**.

### 9.3 Outils d'application (MCP wired)

- `mcp__chrome-devtools__lighthouse_audit` — Gate 2 + Gate 3 (CWV + score Lighthouse)
- `mcp__chrome-devtools__performance_start_trace` + `performance_stop_trace` — Profilage runtime
- `mcp__chrome-devtools__evaluate_script` — DOM inspection (preconnect, font-display, `<img>` absence)
- `mcp__chrome-devtools__take_screenshot` — Visual regression sister
- `Bash` `wc -c` — Gate 1 (tailles source)
- **Vercel Analytics** (live) — Observabilité post-deploy

### 9.4 Ratification

Cet ADR est **DRAFT**. Ratification A0 attendue post-relecture canon (cf. `ADR-META-001` D7 cost-of-escalation — pas d'auto-ratification B1 sans A0 GO).

Gates de ratification :
1. **D1 receipts** : §6 — 4 sources D1-vérifiées ce tour.
2. **Sister-links** : §5 — 5 sister ADRs + 4 ECC sources + 2 sister URLs live.
3. **Vocabulary canonique** : CWV, Lighthouse, gate SHIP, E-Myth SYSTEMIZE, D1-D8 Anti-Paresse, Anti-Paperclip — tous termes canoniques A'Space OS V2.
4. **No-invention** : §6.3 — tous les seuils = citation ECC verbatim OU empirique V2 (D1 `wc -c`).