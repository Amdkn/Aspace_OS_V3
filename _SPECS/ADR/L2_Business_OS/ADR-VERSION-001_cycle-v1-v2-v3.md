---
adr_id: ADR-VERSION-001
title: "Cycle de versionnement canonique V1 V2 V3 + archive pédagogique pour Landing Pages OMK Nexus"
status: RATIFIED
created_iso: "2026-07-06"
ratified_iso: "2026-07-06"
ratification:
  by: "A0 Amadeus"
  date_iso: "2026-07-06"
  gate_a0_signed_off: true
  approval_token: "RATIFICATION-BATCH-01-2026-07-06-TIER-3"
  context: "Ratification Tier 3 ops/QA — 6 ADR production gates ratifiés en bloc."
author: B1 E-Myth Gatekeeper (canon A'Space OS V2)
owner_domain: B2-04 Superman Growth / B3-4 Rocket (analytics-grade experimentation gate)
owner_b1: B1 Summers Nexus OMK BOS (per ADR-L2-AAAS-001 §D2 Nexus row)
sister_canon:
  - ADR-LANDING-QA-001_5-criteres-self-critique.md            # 5-criteria self-critique gate (sister, RATIFIED)
  - ADR-DEPLOY-001 (planned)                                   # gate enforcement deploy (sister-of-sister, à créer sister ADR-DEPLOY-001)
  - ADR-META-001_anti-paresse-verify-before-assert.md          # D4 append-only + no-hard-delete (sister, RATIFIED)
  - ADR-LANDING-CRAFT-001_meta-process-creation.md             # meta-process (sister)
  - ADR-ANTI-TEMPLATE-001_banned-patterns-landing.md          # banned patterns (sister)
  - ADR-DESIGN-SYSTEM-001_tokens-atoms-layered-depth.md       # design system (sister)
  - ADR-LANDING-AESTHETIC-001_doctrine-esthetique.md          # doctrine esthétique (sister)
  - ADR-LANDING-COPY-001_doctrine-copywriting.md              # doctrine copywriting (sister)
  - ADR-MULTIPAGE-001_wireframe-sitemap.md                    # sitemap + wireframe (sister)
  - ADR-NEXUS-LANDING-PERSONAS-001_3-landings-distinctes-icp.md # 3 ICP distincts (sister)
sources_canons:
  d1_paths:
    - "C:\\Users\\amado\\omk-nexus-landing-3-personas\\index.html"                              # V1 root — Coach (Marcus) — 117 KB approx
    - "C:\\Users\\amado\\omk-nexus-landing-3-personas\\marcus-coach-c-suite.html"                # V1 root — Marcus persona
    - "C:\\Users\\amado\\omk-nexus-landing-3-personas\\david-fractional-coo.html"                # V1 root — David persona
    - "C:\\Users\\amado\\omk-nexus-landing-3-personas\\harrison-bdr-agency.html"                 # V1 root — Harrison persona
    - "C:\\Users\\amado\\omk-nexus-landing-3-personas\\v2\\index.html"                           # V2 canon — Coach (Marcus) ~108 KB
    - "C:\\Users\\amado\\omk-nexus-landing-3-personas\\v2\\marcus-coach-c-suite.html"             # V2 canon — Marcus
    - "C:\\Users\\amado\\omk-nexus-landing-3-personas\\v2\\david-fractional-coo.html"             # V2 canon — David
    - "C:\\Users\\amado\\omk-nexus-landing-3-personas\\v2\\harrison-bdr-agency.html"              # V2 canon — Harrison
    - "C:\\Users\\amado\\omk-nexus-landing-3-personas\\_qa\\compare.html"                         # Archive pédagogique V1↔V2 — 6 iframes sandboxés (déjà implémenté)
    - "C:\\Users\\amado\\omk-nexus-landing-3-personas\\_qa\\checklist.html"                       # QA checklist gate
    - "C:\\Users\\amado\\omk-nexus-landing-3-personas\\_screenshots\\00_index.png"                 # V1 screenshot — index Coach
    - "C:\\Users\\amado\\omk-nexus-landing-3-personas\\_screenshots\\v2_00_index.png"              # V2 screenshot — index Coach
    - "C:\\Users\\amado\\omk-nexus-landing-3-personas\\_screenshots\\01_marcus_coach.png"          # V1 Marcus screenshot
    - "C:\\Users\\amado\\omk-nexus-landing-3-personas\\_screenshots\\v2_01_marcus.png"             # V2 Marcus screenshot
    - "C:\\Users\\amado\\omk-nexus-landing-3-personas\\_screenshots\\02_harrison_bdr.png"          # V1 Harrison screenshot
    - "C:\\Users\\amado\\omk-nexus-landing-3-personas\\_screenshots\\v2_02_harrison.png"           # V2 Harrison screenshot
    - "C:\\Users\\amado\\omk-nexus-landing-3-personas\\_screenshots\\03_david_coo.png"            # V1 David screenshot
    - "C:\\Users\\amado\\omk-nexus-landing-3-personas\\_screenshots\\v2_03_david.png"               # V2 David screenshot
  docs_doctrines:
    - "_SPECS\\ADR\\META\\ADR-META-001_anti-paresse-verify-before-assert.md (D4 append-only)"
    - "CLAUDE.md §'Loi du Checkpoint Profond' (sister doctrine)"
    - "_SPECS\\PRD\\PRD-PORTFOLIO-B1-FRANCHISE §6 (Tier 3 PRD-UNIT-ECON-PROOF-001)"
    - "ADR-LANDING-QA-001_5-criteres-self-critique.md (gate enforcement)"
doctrines_invoked:
  - ADR-META-001 D4 (append-only, no-hard-delete — `_TRASH_<date>/` retirement pattern)
  - CLAUDE.md §'Loi du Checkpoint Profond' (Anti-Technicien — inventory avant purge)
  - ADR-LANDING-QA-001 (5-critères self-critique gate — sister enforcement)
  - ADR-LANDING-CRAFT-001 (meta-process création — sister)
tags: [versioning, landing-pages, omk-nexus, v1-v2-v3, cycle, archive-pedagogique, d4-append-only, e-myth, gatekeeping]
supersedes: null
superseded_by: null
version: 1
patch: 0
---

# ADR-VERSION-001 — Cycle de versionnement canonique V1 V2 V3 + archive pédagogique (Landing Pages OMK Nexus)

## 0. Résumé exécutif

Cet ADR établit le **cycle de versionnement canonique** pour les Landing Pages de l'écosystème OMK Nexus ⚖️ (per ADR-ICP-NEXUS-001 ICP Nexus structuration). Trois états canoniques — `V_n` (deploy canonique live), `V_n.draft` (workspace local), `V_n.archive` (audit complet + retention pédagogique) — forment la grille d'horizon H30 (cycle 12WY = 12 semaines cible). Une **archive pédagogique auto-générée** (`_qa/compare_v{n-1}_v{n}.html`, 6 iframes sandboxés lazy-load + screenshots pairés) systématise la régression visuelle et la progression craft entre versions, sœur de `_qa/compare.html` déjà implémentée pour la transition V1→V2.

**Doctrine D4 append-only** : aucune version canonique n'est jamais hard-deleted (sister-canon `ADR-META-001_anti-paresse-verify-before-assert.md` D4 + `CLAUDE.md §'Loi du Checkpoint Profond'`). Les retraits passent par `_TRASH_<date>_reason/` ou `_archive/v{n}_{YYYY-MM-DD}/` avec retention pédagogique.

**Métadonnées de version** : frontmatter `_meta/version.json` (n, prev_n, date_iso, go_a0_signed_off, improvements, regressions_checked) + `git tag v{n}.{patch}` conventionnel + commit `version(v{n}): <summary>`. Aucune invention de cycle : le rythme idéal = 1 version majeure par cycle 12WY (12 semaines) ; cycles courts = hotfixes `v_n.{patch}`.

**Diff empirique V1↔V2** (D1 receipts) : Inter Tight + Roboto (V1) → Outfit + Manrope + IBM Plex Sans (V2, sister `ADR-ANTI-TEMPLATE-001_banned-patterns-landing.md` banned-patterns) ; ~117 KB → ~108 KB (compression + token density) ; V1 sans atmosphère → V2 grain SVG + custom cursor + layered shadows (sister `ADR-DESIGN-SYSTEM-001_tokens-atoms-layered-depth.md`) ; V1 0 élément signature → V2 3 éléments signature distincts (sister `ADR-LANDING-AESTHETIC-001_doctrine-esthetique.md`).

---

## 1. Contexte et problème

### 1.1 Problème (leçon empirique V1→V2)

La transition V1 → V2 des Landing Pages OMK Nexus ⚖️ (réalisée 2026-06-27 — Phase A Coach-spearhead SHIPPED per `wiki/hand_offs/omk_nexus_phase_a_RETARGET_coach_first_2026-06-27.md`) a démontré **3 manquements procéduraux** que cet ADR corrige :

| Manquement V1 | Symptôme observé | Coût pédagogique |
|---|---|---|
| **Pas de versionning explicite** | V1 et V2 ont coexisté dans le même repo (V1 root, V2 dans `v2/`) sans état `_archive/` ni `_TRASH_<date>/` ; confusion sur ce qui est canon | Régressions silencieuses (Inter Tight + Roboto violations bannies par `ADR-ANTI-TEMPLATE-001` mais réintroduites par erreur en V1) |
| **Pas d'archive pédagogique auto** | Le comparatif V1↔V2 a été construit manuellement après-coup (`_qa/compare.html`, 6 iframes sandboxés lazy-load) au lieu d'être généré à chaque release | 30 min de reconstruction à chaque itération + perte de mémoire des régressions atom-level |
| **Pas de gate 5/5 formalisé** | Les 5 critères self-critique (sister `ADR-LANDING-QA-001_5-criteres-self-critique.md`) ont été appliqués rétroactivement sur V2 ; V1 ne les satisfaisait pas | Drift entre la promesse craft (B1 gatekeeper E-Myth) et la livraison B3 (technicien) |

### 1.2 Réponse canonique (sisters)

| Sister-canon | Domaine | Lien |
|---|---|---|
| `ADR-LANDING-QA-001_5-criteres-self-critique.md` | Gate enforcement 5 critères | Sister immédiate (RATIFIED 2026-06-XX) |
| `ADR-LANDING-CRAFT-001_meta-process-creation.md` | Meta-process création landing | Sister craft canon |
| `ADR-ANTI-TEMPLATE-001_banned-patterns-landing.md` | Banned-patterns | Sister design anti-template |
| `ADR-DESIGN-SYSTEM-001_tokens-atoms-layered-depth.md` | Design system tokens + layered depth | Sister atmosphere |
| `ADR-LANDING-AESTHETIC-001_doctrine-esthetique.md` | Doctrine esthétique + 3 éléments signature | Sister craft visuel |
| `ADR-LANDING-COPY-001_doctrine-copywriting.md` | Copywriting doctrine | Sister copy craft |
| `ADR-MULTIPAGE-001_wireframe-sitemap.md` | Wireframe + sitemap | Sister structure |
| `ADR-NEXUS-LANDING-PERSONAS-001_3-landings-distinctes-icp.md` | 3 ICP distincts | Sister structuration 3 personas |
| `ADR-META-001_anti-paresse-verify-before-assert.md` | D4 append-only | Sister doctrine (RATIFIED) |
| `CLAUDE.md §'Loi du Checkpoint Profond'` | Anti-technicien | Sister doctrine utilisateur |

### 1.3 Diff empirique V1↔V2 (D1 receipts — leçon pédagogique)

Le tableau suivant documente les **6 transitions atomiques** observées entre V1 (root `omk-nexus-landing-3-personas/`) et V2 (root `omk-nexus-landing-3-personas/v2/`). Ces transitions constituent la **référence pédagogique** capturée dans `_qa/compare.html` (6 iframes sandboxés) et `_screenshots/` (4 paires PNG) :

| # | V1 (anti-pattern) | V2 (canon) | Sister-canon | Preuve D1 |
|---|---|---|---|---|
| 1 | **Inter Tight + Roboto** (fonts SaaS-grade par défaut, violation `ADR-ANTI-TEMPLATE-001 §banned-fonts`) | **Outfit + Manrope + IBM Plex Sans** (3-fonts stratifiées : display / body / mono) | `ADR-ANTI-TEMPLATE-001_banned-patterns-landing.md §1.2` | Inspection manuelle `<link href="fonts.googleapis.com/css2?family=Inter:...">` vs `family=Outfit:wght@400;500;600;700;800&family=Manrope:...&family=IBM+Plex+Sans:...` |
| 2 | **~117 KB / page** (HTML+CSS+fonts, payload lourd) | **~108 KB / page** (~-8% via compression + token density + clamp() fluide) | `ADR-DESIGN-SYSTEM-001 §tokens` + `§atoms` | `wc -c` sur `index.html` V1 vs V2 ; `gzip -c | wc -c` |
| 3 | **Pas d'atmosphère** (flat layout, ombres minimales, palette safe) | **Grain SVG + custom cursor + layered shadows** (depth via 3 surfaces empilées, gradient mesh + grain overlay) | `ADR-DESIGN-SYSTEM-001 §layered-depth` | Screenshots `_screenshots/00_index.png` vs `v2_00_index.png` + inspection `body::before { background: url('grain.svg') }` |
| 4 | **0 élément signature** (CTA stock, hero générique) | **3 éléments signature distincts par persona** (Marcus: lineage timeline ; Harrison: terminal pipeline ; David: blueprint grid) | `ADR-LANDING-AESTHETIC-001 §3-elements-signature` | Screenshots pairés `_screenshots/01_marcus_coach.png` vs `v2_01_marcus.png` etc. |
| 5 | **Tokens utilitaires Tailwind génériques** (palette safe gray-on-white + 1 accent) | **Tokens custom OKLCH** + 3 palettes distinctes par ICP (Coach/Nexus = gold ; BDR = terminal green ; COO = atelier blue) | `ADR-DESIGN-SYSTEM-001 §tokens-custom` + `ADR-LANDING-AESTHETIC-001 §palette-semantic` | Inspection `:root { --color-surface, --color-accent: oklch(...) }` |
| 6 | **Copy générique "Transform your business with AI"** | **Copy cinématique par persona** (Marcus: lineage ; Harrison: terminal ; David: atelier) — sister `ADR-LANDING-COPY-001` | `ADR-LANDING-COPY-001 §copywriting-cinematique` | Inspection `<h1>` + `<p class="hero-sub">` |

> **D6 lesson shipped** : la transition V1↔V2 a validé que les **6 transitions atomiques** doivent être documentées DANS le présent ADR, sœur de `_qa/compare.html` (déjà implémenté). Aucune invention : tout est mesuré sur les fichiers réels.

---

## 2. Décision

### 2.1 3 états canoniques (grille d'horizon H30 / cycle 12WY)

| État | Symbole | Localisation | Live ? | A0_signed_off | Sister-gate |
|---|---|---|---|---|---|
| **`V_n`** (deploy canonique live) | `V_n` | `omk-nexus-landing-3-personas/v{n}/` OU `omk-nexus-landing-3-personas/` (si V1 historique) | **OUI** (production Vercel) | REQUIS | `ADR-LANDING-QA-001` 5/5 PASS + CWV all-green + A11y WCAG 2.2 AA + `ADR-DEPLOY-001` (sister) |
| **`V_n.draft`** (workspace local en construction) | `V_n.draft` | `omk-nexus-landing-3-personas/_draft/v{n}/` (workspace local) | **NON** (jamais live) | NON REQUIS (état intermédiaire autorisé) | Aucun (gate check pendant build, pas avant deploy) |
| **`V_n.archive`** (audit complet + retention pédagogique) | `V_n.archive` | `omk-nexus-landing-3-personas/_archive/v{n}_{YYYY-MM-DD}/` | **NON** (jamais live) | REQUIS au moment de l'archivage | `_qa/compare_v{n-1}_v{n}.html` généré + screenshots pairés + entry `_meta/version.json` |

> **D4 doctrine (sister `ADR-META-001 D4`)** : aucun hard-delete d'une version archivée. Retirement pattern = `_TRASH_<date>_reason/` si nécessaire (ex. : `_TRASH_2026-07-06_outdated-v1-anti-pattern/`), sister-canon `CLAUDE.md §'Loi du Checkpoint Profond'`.

### 2.2 Workflow de version (5 étapes canoniques)

```
[Trigger] → [Build] → [Gate] → [Deploy] → [Archive]
   ↓          ↓         ↓        ↓           ↓
 A0 GO    V_n.draft   5/5 +   V_n →     V_{n-1} →
 OR      screenshots  CWV +   prod     _archive/
 itération pairés     A11y             + compare.html
 majeure V_n /                          + entry
 V_{n-1}                                version.json
```

**Étape 1 — Trigger** :
- **Option A** : novo gate A0 ratification (per `ADR-LANDING-CRAFT-001 §meta-process` step 6) — A0 signe la ratification et déclenche la release.
- **Option B** : itération majeure sur les 5 critères self-critique (sister `ADR-LANDING-QA-001`) — un ou plusieurs critères passent de FAIL à PASS ou vice-versa, OU un redesign majeur d'un élément signature.

**Étape 2 — Build (V_n.draft)** :
- Workspace local `_draft/v{n}/` avec 4 fichiers (3 personas + `index.html`) — sister `ADR-MULTIPAGE-001_wireframe-sitemap.md` structure.
- Captures screenshots pairés en parallèle : `v{n}_01_marcus.png` + `v{n-1}_01_marcus.png` pour comparaison atomique (sister `ADR-LANDING-AESTHETIC-001 §3-elements-signature`).
- Le build n'est PAS live — `_draft/` est explicitement exclu du déploiement Vercel (`.vercelignore` ou `outputDirectory` config).

**Étape 3 — Gate (5/5 critères + CWV + A11y)** :
- Sister `ADR-LANDING-QA-001_5-criteres-self-critique.md` : 5 critères (Anti-Template, Anti-Paperclip, Self-Critique craft, PRD-UNIT-ECON-PROOF-001 cohérence, A11y WCAG 2.2 AA).
- **CWV all-green** : LCP < 2.5s, INP < 200ms, CLS < 0.1 (per `CLAUDE.md §web/performance.md`).
- **A11y WCAG 2.2 AA validated** : audit automatisé (axe / Lighthouse) + revue manuelle focus trap + screen reader.
- Sister `ADR-DEPLOY-001` (planned) : gate enforcement pré-deploy.

**Étape 4 — Deploy (V_n → production)** :
- Sister `ADR-DEPLOY-001` : convention de déploiement (Vercel, GitHub mirror, env vars, DNS, smoke test post-deploy).
- Tag `git tag v{n}.{patch}` conventionnel + commit `version(v{n}): <summary>` (sister `CLAUDE.md §git-workflow.md`).
- Frontmatter `_meta/version.json` mis à jour avec `{n: n, prev_n: n-1, date_iso, go_a0_signed_off: true, improvements: [...], regressions_checked: [...]}`.

**Étape 5 — Archive (V_{n-1} → `_archive/`)** :
- Création `omk-nexus-landing-3-personas/_archive/v{n-1}_{YYYY-MM-DD}/` avec copie des 4 fichiers canoniques de V_{n-1}.
- Génération `_qa/compare_v{n-1}_v{n}.html` (6 iframes sandboxés lazy-load, sœur de `_qa/compare.html` déjà implémenté pour V1↔V2).
- Screenshots pairés `_screenshots/v{n-1}_XX_<persona>.png` + `_screenshots/v{n}_XX_<persona>.png` (4 paires).
- Entry dans `_meta/version.json` documentant `improvements` (delta craft) + `regressions_checked` (régressions atomiques vérifiées).

### 2.3 Convention de nommage fichiers (D4 append-only)

| Pattern | Exemple | Localisation | Signification |
|---|---|---|---|
| `omk-nexus-landing-3-personas/index.html` | V1 root | `omk-nexus-landing-3-personas/` (legacy V1) | V1 historique (avant adoption ADR-VERSION-001) — sister `_qa/compare.html` |
| `omk-nexus-landing-3-personas/v2/index.html` | V2 canonique live | `omk-nexus-landing-3-personas/v2/` | V2 = version courante live (Phase A Coach-spearhead SHIPPED 2026-06-27) |
| `omk-nexus-landing-3-personas/v3/index.html` | V3 future | `omk-nexus-landing-3-personas/v3/` | V3 = prochaine itération majeure (post W3 cycle 12WY Q3 2026) |
| `omk-nexus-landing-3-personas/_archive/v{n}_{YYYY-MM-DD}/index.html` | Archive | `omk-nexus-landing-3-personas/_archive/v{n}_{YYYY-MM-DD}/` | Retention pédagogique post-deploy V_{n+1} |
| `omk-nexus-landing-3-personas/_draft/v{n}/index.html` | Workspace build | `omk-nexus-landing-3-personas/_draft/v{n}/` | Build en cours, jamais live |
| `omk-nexus-landing-3-personas/_qa/compare_v{n-1}_v{n}.html` | Comparatif pédagogique | `omk-nexus-landing-3-personas/_qa/` | 6 iframes sandboxés lazy-load V_{n-1}↔V_n |
| `omk-nexus-landing-3-personas/_TRASH_<date>_reason/` | Retirement | `omk-nexus-landing-3-personas/_TRASH_<date>_reason/` | D4 append-only sister `ADR-META-001` — jamais hard-delete |
| `omk-nexus-landing-3-personas/_meta/version.json` | Métadonnées | `omk-nexus-landing-3-personas/_meta/` | Frontmatter version canonique |

### 2.4 Archive pédagogique auto-générée

L'archive pédagogique est l'**artefact central** de cet ADR. Sister de `_qa/compare.html` (déjà implémenté pour V1↔V2), elle est auto-générée à chaque release et **doit** contenir :

1. **6 iframes sandboxés** lazy-load (3 personas × 2 versions V_{n-1}+V_n) — pattern `sandbox="allow-scripts allow-same-origin"` + `loading="lazy"`.
2. **4 paires screenshots** `_screenshots/v{n-1}_XX_<persona>.png` + `_screenshots/v{n}_XX_<persona>.png` pour comparaison atomique (sister `ADR-LANDING-AESTHETIC-001 §3-elements-signature`).
3. **Diff textuel inline** : `font-family`, `color`, `box-shadow`, `transform`, `--color-accent` extraction auto + annotation des 6 transitions atomiques (sister `ADR-ANTI-TEMPLATE-001` + `ADR-DESIGN-SYSTEM-001`).
4. **Notes ADR-VERSION documente** : `improvements` (delta craft) + `regressions_checked` (régressions atomiques vérifiées) — sister `_meta/version.json`.
5. **Référence canonique sister-canon** : chaque transition pointe vers l'ADR sister qui la justifie (ex. transition Inter→Outfit → `ADR-ANTI-TEMPLATE-001 §banned-fonts`).

> **D6 lesson shipped** : `_qa/compare.html` V1↔V2 est le **prototype canonique** de l'archive pédagogique. Tout V_n↔V_{n-1} futur doit suivre le même pattern. **Pas d'invention** : la structure 6 iframes + 4 paires screenshots + diff textuel est mesurée sur `_qa/compare.html` existant.

---

## 3. Rationale

### 3.1 Pourquoi 3 états canoniques (et pas 4 ou 5) ?

Trois états couvrent **toutes les transitions réelles** observées :

- **`V_n` (deploy)** = état stationnaire canonique, accessible aux visiteurs live (sister `ADR-ICP-NEXUS-001` ICP Nexus structuration — landing = front du funnel).
- **`V_n.draft` (build)** = état transitoire workspace, jamais exposé, permet itération rapide sans risque de régression live (sister `CLAUDE.md §git-workflow.md` branches).
- **`V_n.archive` (pedagogical retention)** = état permanent post-release, sister `ADR-META-001 D4` append-only + `CLAUDE.md §'Loi du Checkpoint Profond'`.

Un 4e état "**`V_n.staging`**" est rejeté car **Vercel preview deployments** jouent déjà ce rôle (chaque PR = staging auto, sister `ADR-DEPLOY-001` planned). Un 5e état "**`V_n.hotfix`**" est rejeté car les hotfixes sont des `v_n.{patch}` du même état `V_n` (cycle court, sister §2.5 cycle idéal).

### 3.2 Pourquoi 5/5 critères + CWV + A11y comme gate ?

Sister `ADR-LANDING-QA-001_5-criteres-self-critique.md` codifie déjà les 5 critères canoniques (Anti-Template, Anti-Paperclip, Self-Critique craft, PRD-UNIT-ECON-PROOF-001 cohérence, A11y WCAG 2.2 AA). Sister `CLAUDE.md §web/performance.md` codifie les CWV targets (LCP < 2.5s, INP < 200ms, CLS < 0.1). Le gate est donc **3-sisters conjonction** : 5 critères fonctionnels + CWV performance + A11y accessibilité = deploy-ready.

### 3.3 Pourquoi cycle 12WY (12 semaines) ?

Le cycle 12WY (per `ADR-L2-AAAS-001 §solarpunk-cycle` + Morty Mindset FOCUS cadence) cadence déjà tous les autres livrables canon (ADR ratification, ICP iteration, pricing canon update). Aligner le cycle landing sur 12WY évite la **dérive de cadence** entre livrables et landing. Cycles courts (<12 sem) = hotfix `v_n.{patch}` sans ceremonie full.

### 3.4 Pourquoi D4 append-only ?

Sister `ADR-META-001_anti-paresse-verify-before-assert.md D4` codifie l'append-only comme doctrine cross-agent (Claude/Codex/Gemini). Sister `CLAUDE.md §'Loi du Checkpoint Profond'` codifie l'inventory avant purge. Hard-delete d'une version archivée = perte de mémoire pédagogique = D6 lesson (per `wiki/hand_offs/` 2026-03-05 perte `A0_Memory`). **Aucune exception** : retirement passe par `_TRASH_<date>_reason/` avec documentation explicite.

### 3.5 Alternatives rejetées

| Alternative | Pourquoi rejetée |
|---|---|
| **Tag-only git** (`git tag v1.0, v2.0, ...`) sans `_archive/` | Pas de retention pédagogique atomique (impossible de comparer `_qa/compare_v1_v2.html` si V1 a été overwrite par V2 dans le repo) |
| **Branches-only** (`main`, `release/v2`, `release/v3`) | Drift entre branches non-géré, sister `CLAUDE.md §web/git-workflow.md` recommande tags pour releases canon |
| **Semver strict** (`v{n}.{patch}.{build}`) | Sur-ingénierie pour landing pages statiques (sister `ADR-DESIGN-SYSTEM-001 §tokens`), un `v_n.{patch}` suffit pour hotfixes |
| **No archive pédagogique** (juste git log) | Perte de mémoire visuelle (régressions atom-level non-documentées), sister `ADR-LANDING-AESTHETIC-001 §3-elements-signature` exige preuve visuelle |

---

## 4. Implémentation

### 4.1 Phase 1 — Préparation (W1 cycle 12WY Q3 2026 = semaine 06/29 - 07/05)

**Objectif** : outillage auto-génération `_qa/compare_v{n-1}_v{n}.html` + script git tag canonique.

**Livrables** :
1. **Script `_scripts/gen-compare.sh`** (PowerShell-compatible) :
   - Input : `prev_v_dir`, `current_v_dir`, `output_html_path`, `screenshots_dir`.
   - Output : `_qa/compare_v{n-1}_v{n}.html` avec 6 iframes sandboxés lazy-load.
   - Sister de `_qa/compare.html` (déjà implémenté) — **NE PAS réinventer**, forker le pattern existant.
2. **Script `_scripts/gen-version-meta.sh`** :
   - Input : `n`, `prev_n`, `date_iso`, `improvements[]`, `regressions_checked[]`.
   - Output : `_meta/version.json` canonique.
3. **Hook `PostToolUse` (sister `CLAUDE.md §hooks.md`)** : après chaque Write/Edit sur `omk-nexus-landing-3-personas/v{n}/*.html`, suggestion de régénération `_meta/version.json`.

**Critères PASS Phase 1** :
- [ ] Script `_scripts/gen-compare.sh` exécuté sur V1↔V2 produit un HTML visuellement équivalent à `_qa/compare.html` existant (test de régression visuelle).
- [ ] Script `_scripts/gen-version-meta.sh` produit un JSON valide parseable par `python -m json.tool`.
- [ ] Hook PostToolUse configuré dans `~/.claude/settings.json` (sister `ADR-META-005_hooks-automation.md`).

### 4.2 Phase 2 — Adoption V2 (W2 = 07/06 - 07/12)

**Objectif** : back-fill V2 dans le pattern canonique ADR-VERSION-001 (V1 = historique pre-ADR, V2 = première version conforme).

**Livrables** :
1. Déplacer `omk-nexus-landing-3-personas/v2/` vers `omk-nexus-landing-3-personas/v2/` (inchangé) + ajouter `_meta/version.json` pour V2.
2. Déplacer `omk-nexus-landing-3-personas/` (V1 root) vers `omk-nexus-landing-3-personas/_archive/v1_2026-06-27/` (date du Phase A SHIPPED).
3. Générer `omk-nexus-landing-3-personas/_qa/compare_v1_v2.html` (sœur de `_qa/compare.html`).
4. `_meta/version.json` V2 = `{n: 2, prev_n: 1, date_iso: "2026-06-27", go_a0_signed_off: true, improvements: [...6 transitions V1↔V2...], regressions_checked: [...]}`.
5. Git tag `v2.0` + commit `version(v2): Phase A Coach-spearhead SHIPPED 2026-06-27 — 6 transitions atomiques (Inter→Outfit, Roboto→Manrope, 3 éléments signature, grain SVG, custom cursor, layered shadows)`.

**Critères PASS Phase 2** :
- [ ] V2 canon `_meta/version.json` créé avec les 6 transitions V1↔V2 documentées.
- [ ] V1 déplacé dans `_archive/v1_2026-06-27/` (D4 append-only respecté).
- [ ] `_qa/compare_v1_v2.html` généré et visuellement équivalent à `_qa/compare.html` (test de régression).
- [ ] Git tag `v2.0` + commit message conformes aux conventions `CLAUDE.md §git-workflow.md`.

### 4.3 Phase 3 — V3 première release canonique (W3-W4 = 07/13 - 07/26)

**Objectif** : valider le cycle end-to-end sur V3 (première release suivant le pattern ADR-VERSION-001 de bout en bout).

**Livrables** :
1. `_draft/v3/` workspace de build (4 fichiers, sister `ADR-MULTIPAGE-001_wireframe-sitemap.md`).
2. Screenshots pairés `_screenshots/v2_XX_<persona>.png` + `_screenshots/v3_XX_<persona>.png` (4 paires).
3. Gate 5/5 PASS + CWV all-green + A11y WCAG 2.2 AA (sister `ADR-LANDING-QA-001`).
4. Deploy V3 → production (sister `ADR-DEPLOY-001` planned).
5. Archive V2 → `_archive/v2_2026-MM-DD/` + `_qa/compare_v2_v3.html` auto-généré.
6. `_meta/version.json` V3 = `{n: 3, prev_n: 2, date_iso, go_a0_signed_off, improvements, regressions_checked}`.
7. Git tag `v3.0` + commit `version(v3): <summary>`.

**Critères PASS Phase 3** :
- [ ] V3 deployed live et 5/5 critères PASS vérifiables sur le site live.
- [ ] CWV all-green (Lighthouse audit) + A11y WCAG 2.2 AA (axe audit).
- [ ] V2 archivé dans `_archive/v2_2026-MM-DD/` (D4 append-only).
- [ ] `_qa/compare_v2_v3.html` généré et inspectable.
- [ ] Git tag `v3.0` + commit canonique.

### 4.4 Sister-outillage (per ADR-DEPLOY-001 planned)

- **Vercel** : `omk-nexus-landing-3-personas/v{n}/` comme root de déploiement (sister `ADR-DEPLOY-001`).
- **GitHub mirror** : sister `wiki/hand_offs/handoff_github_vercel_separation_2026-06-17.md` (4/4 repos AMD→OMK/ABC mirror OK 2026-06-17).
- **DNS** : sister `ADR-ICP-NEXUS-001 §landing-domain` (URL live : `omk-nexus-landing-page.vercel.app` 2026-07-04 per `MEMORY.md §Nexus EN landing DEPLOYED`).
- **Smoke test post-deploy** : sister `ADR-DEPLOY-001 §smoke-test` (curl + Lighthouse + axe via Playwright MCP).

---

## 5. Critères d'acceptation et gate enforcement

### 5.1 Gate enforcement (sister `ADR-LANDING-QA-001`)

Le gate est **3-sisters conjonction** :

| Sister | Critère | Statut |
|---|---|---|
| `ADR-LANDING-QA-001 §1` | **Anti-Template** : aucun pattern banni par `ADR-ANTI-TEMPLATE-001` (Inter Tight, Roboto, gradient blob, CTA stock) | REQUIS (5/5 PASS) |
| `ADR-LANDING-QA-001 §2` | **Anti-Paperclip** : aucun contenu généré par paperclip policy violation (sister `ADR-ANTI-PAPERCLIP-001_landing-paperclip-policy.md`) | REQUIS (5/5 PASS) |
| `ADR-LANDING-QA-001 §3` | **Self-Critique craft** : 4 qualités design requises (hierarchy, rhythm, depth, motion) + 3 éléments signature (sister `ADR-LANDING-AESTHETIC-001`) | REQUIS (5/5 PASS) |
| `ADR-LANDING-QA-001 §4` | **PRD-UNIT-ECON-PROOF-001 cohérence** : chiffres coût-fixe-vs-Jevons SOURCÉS sur le PRD (sister `PRD-PORTFOLIO-B1-FRANCHISE §6 Tier 3`) | REQUIS (5/5 PASS) |
| `ADR-LANDING-QA-001 §5` | **A11y WCAG 2.2 AA** : automated + manual review (focus trap, screen reader, color contrast) | REQUIS (5/5 PASS) |
| `CLAUDE.md §web/performance.md` | **CWV all-green** : LCP < 2.5s, INP < 200ms, CLS < 0.1, FCP < 1.5s, TBT < 200ms | REQUIS (Lighthouse audit) |
| `CLAUDE.md §web/security.md` | **CSP + HTTPS + headers** : nonce-based CSP, HSTS, X-Frame-Options DENY, etc. | REQUIS (audit) |
| `ADR-DEPLOY-001 §gate` | **Deploy gate** : smoke test post-deploy + rollback plan ready | REQUIS (sister planned) |

**Statut gate** : `5/5 + CWV + A11y + Security + Deploy = 9/9 PASS` pour autoriser le déploiement V_n → production.

### 5.2 Critères D4 append-only (sister `ADR-META-001 D4`)

| Critère | Vérification |
|---|---|
| Aucune version canonique hard-deleted | `git log --diff-filter=D --name-only` sur `omk-nexus-landing-3-personas/` ne montre aucun `v{n}/*.html` deleted |
| Retirement pattern respecté | Tout retirement passe par `_TRASH_<date>_reason/` avec README explicite |
| Inventory avant purge | Sister `CLAUDE.md §'Loi du Checkpoint Profond'` — l'agent DOIT présenter la liste des fichiers à retirer à A0 avant `Remove-Item` ou `rd /s /q` |
| `_meta/version.json` append-only | Chaque release ajoute une entry, ne réécrit jamais une entry antérieure |

### 5.3 Critères PRD-UNIT-ECON-PROOF-001 (sister `PRD-PORTFOLIO-B1-FRANCHISE §6 Tier 3`)

Le Tier 3 du PRD portfolio B1 Franchise exige la **table de preuve coût-fixe-vs-Jevons** avec **VRAIS chiffres mesurés sur notre propre usage** (38M tokens/jour déjà documentés per `MEMORY.md §ADR-LLM-COST-COMPARE-001`). Cela résout le warning `PRD-NEXUS §7.6` : **plus jamais un chiffre non sourcé sur une landing**.

**Critère** : chaque landing V_n publiée contient au moins 1 chiffre sourcé sur l'usage propre OMK (tokens/jour, runway mois, LTV/CAC mesuré). Le gate vérifie la présence du bloc `<section data-pinned="unit-econ-proof">` avec `data-source="harness-2026-07-04"` ou équivalent.

---

## 6. Risques et trade-offs

### 6.1 Risques

| Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|
| **Drift entre gate et craft réel** (les 5 critères sont satisfaits formellement mais le design est générique) | Moyenne | Élevé (régression craft) | Self-Critique manuelle A0 + screenshot pairé `v{n-1}` vs `v{n}` avant sign-off ; sister `ADR-LANDING-CRAFT-001 §meta-process step 6` |
| **Cycle 12WY trop court** (V_n doit sortir avant que les 5 critères soient satisfaits) | Faible | Élevé | Hotfix `v_n.{patch}` autorisé pour correction rapide sans ceremonie full ; cycle long = report à W13 |
| **Archive pédagogique obsolète** (`_qa/compare.html` non régénéré pour les hotfixes) | Moyenne | Moyen | Sister `_meta/version.json` documente chaque hotfix ; `_qa/compare_v{n}_v{n+1}.html` régénéré uniquement pour les versions majeures |
| **Vercel preview ≠ production** (le site live diffère du `_draft/v{n}/` workspace) | Faible | Élevé | Sister `ADR-DEPLOY-001 §smoke-test` — post-deploy curl + screenshot Playwright |
| **Hard-delete accidentel d'une `_archive/`** | Faible | Élevé (D4 violation) | Sister `CLAUDE.md §'Loi du Checkpoint Profond'` + `ADR-META-001 D4` — inventory avant purge A0-signed |
| **Git force-push réécrit l'history** (`git push --force` sur une branche release) | Faible | Élevé (perte canon) | Interdit explicitement §7 anti-patterns + sister `CLAUDE.md §git-workflow.md §force-push` |

### 6.2 Trade-offs

| Trade-off | Choix | Justification |
|---|---|---|
| **Convention de nommage** `v{n}/` vs branches git | `v{n}/` directories | Simplicité (sister `ADR-MULTIPAGE-001_wireframe-sitemap.md` structure), pas de drift branches, tag git en complément |
| **Archive pédagogique** auto-générée vs manuelle | **Auto-générée** (script `_scripts/gen-compare.sh`) | Reproductible, scalable, sœur de `_qa/compare.html` existant ; manuelle = drift + perte |
| **5 critères + CWV + A11y + Security + Deploy** (9/9 PASS) | Tous requis | Pas de demi-mesure — sister `ADR-LANDING-QA-001` gate strict |
| **Cycle 12 sem** vs hotfix `v_n.{patch}` | 12 sem idéal + hotfix autorisé | Aligne sur cycle canonique `ADR-L2-AAAS-001 §solarpunk-cycle`, hotfix pour réactivité |

---

## 7. Anti-patterns interdits

| Anti-pattern | Raison | Sister-canon |
|---|---|---|
| **Hard-delete d'une V_n.archive** | D4 violation, perte de mémoire pédagogique | `ADR-META-001 D4` + `CLAUDE.md §'Loi du Checkpoint Profond'` |
| **Skip la capture `_qa/compare_v{n-1}_v{n}.html`** | Perte de preuve visuelle des transitions atomiques | `ADR-LANDING-AESTHETIC-001 §3-elements-signature` |
| **Deploy V_n.draft sans gate 9/9 PASS** | Risque régression live, sister `ADR-DEPLOY-001` gate | `ADR-LANDING-QA-001` + `CLAUDE.md §web/performance.md` |
| **Force-push git history sur une branche release** | Perte canon, réécriture history | `CLAUDE.md §git-workflow.md §force-push` |
| **V_n.archive copié comme V_{n+1}** (copier-coller au lieu d'itérer) | Drift craft, sister `ADR-LANDING-CRAFT-001 §meta-process` | `ADR-ANTI-TEMPLATE-001 §banned-clone` |
| **Plus de 1 version majeure par cycle 12WY** | Cadence cassée, drift avec Morty Mindset FOCUS | `ADR-L2-AAAS-001 §solarpunk-cycle` |
| **Tag git sans commit canonique** (`git tag v3.0` sans message de version) | Pas de traçabilité | `CLAUDE.md §git-workflow.md §conventional-commits` |
| **`_meta/version.json` réécriture** (overwrite au lieu d'append) | D4 violation | `ADR-META-001 D4` |
| **Skip le `_TRASH_<date>_reason/` retirement pattern** | Pas de trace du pourquoi du retirement | `ADR-META-001 D4` + `CLAUDE.md §'Loi du Checkpoint Profond'` |

---

## 8. Conséquences

### 8.1 Positives

- **Mémoire craft préservée** : `_qa/compare_v{n-1}_v{n}.html` documente atom-level les transitions, sœur de `_qa/compare.html` V1↔V2 déjà implémenté.
- **Gate enforcement systématisé** : 9/9 PASS obligatoires avant deploy, sister `ADR-LANDING-QA-001` + `ADR-DEPLOY-001`.
- **D4 append-only respecté** : aucune version canonique jamais hard-deleted, sister `ADR-META-001` + `CLAUDE.md §'Loi du Checkpoint Profond'`.
- **Cycle 12WY aligné** : cadence landing cohérente avec autres livrables canon (ADR, ICP, pricing).
- **Métadonnées canoniques** : `_meta/version.json` documente `improvements` + `regressions_checked` à chaque release.

### 8.2 Négatives (coûts)

- **Effet overhead par release** : ~30 min de plus par version majeure (génération `_qa/compare_*.html` + `_meta/version.json` + screenshots pairés).
- **Stockage `_archive/` cumulatif** : ~108 KB × N versions × 4 fichiers = `~432 KB × N` cumulés. Mitigé par hotfix `v_n.{patch}` (pas de `_archive/`).
- **Discipline requise** : D4 append-only + inventory avant purge = A0 HITL sur chaque retirement (sister `ADR-META-001 D4`).

### 8.3 Neutres (observabilités)

- **Git history** : tags `v{n}.{patch}` offrent une traçabilité release-by-release.
- **Wiki canon** : chaque release ajoute un entry dans `wiki/hand_ffs/` (sister `CLAUDE.md §wiki/log.md`).

---

## 9. Références canoniques (sisters + D1 receipts)

### 9.1 Sister-canon (ADR/L2_Business_OS/)

| ADR | Sujet | Statut |
|---|---|---|
| `ADR-LANDING-QA-001_5-criteres-self-critique.md` | 5-critères self-critique gate | RATIFIED (sister immédiate) |
| `ADR-DEPLOY-001 (planned)` | Deploy gate enforcement | À créer sister-of-sister |
| `ADR-LANDING-CRAFT-001_meta-process-creation.md` | Meta-process création landing | Sister |
| `ADR-ANTI-TEMPLATE-001_banned-patterns-landing.md` | Banned patterns landing | Sister |
| `ADR-DESIGN-SYSTEM-001_tokens-atoms-layered-depth.md` | Design system tokens + layered depth | Sister |
| `ADR-LANDING-AESTHETIC-001_doctrine-esthetique.md` | Doctrine esthétique + 3 éléments signature | Sister |
| `ADR-LANDING-COPY-001_doctrine-copywriting.md` | Doctrine copywriting | Sister |
| `ADR-MULTIPAGE-001_wireframe-sitemap.md` | Wireframe + sitemap | Sister |
| `ADR-NEXUS-LANDING-PERSONAS-001_3-landings-distinctes-icp.md` | 3 ICP distincts (Marcus / Harrison / David) | Sister |
| `ADR-ICP-NEXUS-001_icp-nexus-structuration.md` | ICP Nexus structuration | Sister |
| `ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md` | AaaS doctrine 3 variants (Solaris / Nexus / Orbiter) | Sister |
| `ADR-AAAS-PRICING-001_aaas-pricing-canon.md` | Pricing canon | Sister |
| `ADR-ANTI-PAPERCLIP-001_landing-paperclip-policy.md` | Anti-paperclip landing | Sister |
| `ADR-OPS-009_worker-git-commit-doctrine.md` | Worker git commit doctrine | Sister |

### 9.2 Sister-doctrine (cross-référencement)

| Doctrine | Source | Règle |
|---|---|---|
| D4 append-only | `ADR-META-001_anti-paresse-verify-before-assert.md §D4` | Pas de hard-delete, `_TRASH_<date>_reason/` retirement |
| Loi du Checkpoint Profond | `CLAUDE.md §'Loi du Checkpoint Profond'` | Inventory avant purge, A0 HITL sur dossiers >100MB |
| CWV targets | `CLAUDE.md §web/performance.md` | LCP < 2.5s, INP < 200ms, CLS < 0.1 |
| A11y WCAG 2.2 AA | `CLAUDE.md §web/security.md` | focus trap, screen reader, color contrast |
| Conventional commits | `CLAUDE.md §git-workflow.md` | `<type>: <description>` + corps optionnel |
| Pas de force-push | `CLAUDE.md §git-workflow.md` | History canon immutable |

### 9.3 D1 receipts (paths absolus empiriques)

| Type | Path | Signification |
|---|---|---|
| **V1 archive** | `C:\Users\amado\omk-nexus-landing-3-personas\index.html` | V1 root — Coach (Marcus) ~117 KB |
| **V1 archive** | `C:\Users\amado\omk-nexus-landing-3-personas\marcus-coach-c-suite.html` | V1 Marcus persona |
| **V1 archive** | `C:\Users\amado\omk-nexus-landing-3-personas\david-fractional-coo.html` | V1 David persona |
| **V1 archive** | `C:\Users\amado\omk-nexus-landing-3-personas\harrison-bdr-agency.html` | V1 Harrison persona |
| **V2 canon** | `C:\Users\amado\omk-nexus-landing-3-personas\v2\index.html` | V2 canon — Coach ~108 KB |
| **V2 canon** | `C:\Users\amado\omk-nexus-landing-3-personas\v2\marcus-coach-c-suite.html` | V2 Marcus |
| **V2 canon** | `C:\Users\amado\omk-nexus-landing-3-personas\v2\david-fractional-coo.html` | V2 David |
| **V2 canon** | `C:\Users\amado\omk-nexus-landing-3-personas\v2\harrison-bdr-agency.html` | V2 Harrison |
| **Archive pédagogique** | `C:\Users\amado\omk-nexus-landing-3-personas\_qa\compare.html` | Comparatif V1↔V2 — 6 iframes sandboxés (prototype canonique) |
| **QA checklist** | `C:\Users\amado\omk-nexus-landing-3-personas\_qa\checklist.html` | QA checklist gate |
| **Screenshot V1** | `C:\Users\amado\omk-nexus-landing-3-personas\_screenshots\00_index.png` | V1 — index Coach |
| **Screenshot V2** | `C:\Users\amado\omk-nexus-landing-3-personas\_screenshots\v2_00_index.png` | V2 — index Coach |
| **Screenshot V1 Marcus** | `C:\Users\amado\omk-nexus-landing-3-personas\_screenshots\01_marcus_coach.png` | V1 — Marcus |
| **Screenshot V2 Marcus** | `C:\Users\amado\omk-nexus-landing-3-personas\_screenshots\v2_01_marcus.png` | V2 — Marcus |
| **Screenshot V1 Harrison** | `C:\Users\amado\omk-nexus-landing-3-personas\_screenshots\02_harrison_bdr.png` | V1 — Harrison |
| **Screenshot V2 Harrison** | `C:\Users\amado\omk-nexus-landing-3-personas\_screenshots\v2_02_harrison.png` | V2 — Harrison |
| **Screenshot V1 David** | `C:\Users\amado\omk-nexus-landing-3-personas\_screenshots\03_david_coo.png` | V1 — David |
| **Screenshot V2 David** | `C:\Users\amado\omk-nexus-landing-3-personas\_screenshots\v2_03_david.png` | V2 — David |

### 9.4 Wiki canonique (hand_offs)

| Handoff | Date | Sujet |
|---|---|---|
| `wiki/hand_offs/omk_nexus_phase_a_RETARGET_coach_first_2026-06-27.md` | 2026-06-27 | OMK Nexus Phase A Coach-spearhead SHIPPED (V1→V2 transition) |
| `wiki/hand_offs/p2_4d_coach_spearhead_DONE.md` | 2026-07-04 | P2.4d Coach spearhead CLOSED (V2 canon live) |
| `wiki/hand_ffs/handoff_github_vercel_separation_2026-06-17.md` | 2026-06-17 | GitHub+Vercel mirror+deploy (4/4 repos) |
| `wiki/hand_offs/handoff_life_os_deploy_v1_0_2026-06-17.md` | 2026-06-17 | Life OS V1.0 deploy |

### 9.5 PRD canonique (Tier 3 unit-econ-proof)

| PRD | Section | Sujet |
|---|---|---|
| `PRD-PORTFOLIO-B1-FRANCHISE §6 Tier 3` | Tier 3 PRD-UNIT-ECON-PROOF-001 | Table de preuve coût-fixe-vs-Jevons avec VRAIS chiffres mesurés |
| `PRD-NEXUS §7.6` | Warning chiffres non sourcés | Résolu par cet ADR (gate §5.3) |

---

## 10. D6 lessons shipped + changelog

### 10.1 D6 lessons (révèle les apprentissages critiques)

1. **Leçon V1→V2** : sans versionning explicite, les régressions atomiques (Inter Tight + Roboto) réapparaissent silencieusement. Sister `_qa/compare.html` est devenu le prototype canonique de l'archive pédagogique.
2. **Leçon commit atomique** : la transition Inter→Outfit + Roboto→Manrope + 3 éléments signature doit être commité en UN seul commit atomique `version(v2): <summary>` pour préserver la cohérence craft.
3. **Leçon gate enforcement** : les 5 critères self-critique doivent être appliqués **DURANT** le build, pas rétroactivement après. V1 ne les satisfaisait pas, et la rétro-application sur V2 a coûté ~30 min de reconstruction.

### 10.2 Changelog

| Version | Date | Auteur | Changement |
|---|---|---|---|
| v1.0 | 2026-07-06 | B1 E-Myth Gatekeeper | Création initiale — DRAFT |

---

**FIN ADR-VERSION-001** — Statut : DRAFT, en attente ratification A0.

Sister-canon principal : `ADR-LANDING-QA-001_5-criteres-self-critique.md` (gate 5 critères RATIFIED).
Sister-canon secondaire : `ADR-META-001 D4` (append-only), `CLAUDE.md §'Loi du Checkpoint Profond'` (inventory avant purge), `ADR-LANDING-CRAFT-001` (meta-process).
Sister-of-sister planned : `ADR-DEPLOY-001` (deploy gate enforcement).