---
adr_id: ADR-MULTIPAGE-001
title: "Doctrine Multi-Page & Sitemap Canonique pour Landing Pages OMK Nexus"
version: 0.1
status: RATIFIED
date_created: 2026-07-06
date_ratified: 2026-07-06
authors:
  - role: B1 E-Myth Gatekeeper
    handle: A0-Jumeau-Numerique
  - role: Source doctrine
    handle: Jack Roberts (methodology transcript)
level: L2_Business_OS
category: Wireframe / Sitemap / Multi-Page Doctrine
tags:
  - wireframe
  - sitemap
  - multi-page
  - single-page-focal
  - landing-page
  - substance-first
  - e-myth
  - omk-nexus
sisters_immediate:
  - ADR-LANDING-CRAFT-001 §4.2 (Phase 2 Wireframe)
  - ADR-LANDING-CRAFT-001 §4.5 (Phase 5 Multi-Page Build)
  - ADR-NEXUS-LANDING-PERSONAS-001 §3.2 (single-file vanilla canon)
sisters_construction:
  - ADR-NEXUS-EVOLUTION-IA-001 §5 (modules existants)
  - ADR-NEXUS-EVOLUTION-IA-001 §6 (rails existants)
  - plan-L2 §5.4 (Holding → Filiales VERSION FINALE)
references_v2_empirique:
  - C:\Users\amado\omk-nexus-landing-3-personas\v2\ (3 personas + index, single-page actuel)
  - https://omk-nexus-landing-page.vercel.app (FR, LIVE)
  - https://omk-nexus-landing-en.vercel.app (EN, LIVE)
sources_canons:
  - id: JACK-ROBERTS-METHODOLOGY
    type: video-transcript
    section: "Maintenant nous avons besoin de penser à ce que veut le site web → page d'accueil, page contact, page services, etc."
    lesson: "Avant de penser au design / aux couleurs / aux typos, il faut d'abord penser à ce que veut le site web — c'est-à-dire : quelles pages, quels rôles, quel parcours. Le style vient ensuite sur la substance."
  - id: ADR-LANDING-CRAFT-001-§4.2
    type: sister-adr
    section: "Phase 2 Wireframe"
    role: "sister immédiate — wireframe substance-first avant pixel"
  - id: ADR-LANDING-CRAFT-001-§4.5
    type: sister-adr
    section: "Phase 5 Multi-Page Build"
    role: "sister construction — implémentation sitemap multi-page"
  - id: ADR-NEXUS-EVOLUTION-IA-001
    type: sister-adr
    section: "§5 modules + §6 rails existants"
    role: "ancre modules / rails à câbler dans le sitemap"
  - id: ADR-NEXUS-LANDING-PERSONAS-001
    type: sister-adr
    section: "§3.2 single-file vanilla"
    role: "sister sister — pattern single-file à étendre / hybrider"
  - id: V2-EMPIRIQUE
    type: filesystem
    path: C:\Users\amado\omk-nexus-landing-3-personas\v2\
    role: "3 personas + index, actuellement single-page. Cet ADR codifie la ROADMAP multi-page pour ces 3 personas."
  - id: PLAN-L2-§5.4
    type: plan
    section: "Holding → Filiales VERSION FINALE"
    role: "ancre structurelle Holding hub + filiales par ICP"
anti_patterns_sister:
  - ADR-ANTI-TEMPLATE-001 (pas Inter/Roboto/Arial)
  - ADR-PAPERCLIP-002 (anti-page-unique sans sitemap)
ratification:
  by: "A0 Amadeus"
  date_iso: "2026-07-06"
  gate_a0_signed_off: true
  approval_token: "RATIFICATION-BATCH-01-2026-07-06-TIER-2"
  context: "Ratification Tier 2 DDD Landing Pages — 3 ADR multi-page & personas ratifiés en bloc."
---

# ADR-MULTIPAGE-001 — Doctrine Multi-Page & Sitemap Canonique

## 1. Context & Intent

**Constat empirique V2 (D1)** : 3 landing pages OMK Nexus (`omk-nexus-landing-3-personas/v2/`) sont actuellement **single-page monolithiques**, livrées sans sitemap défini en amont. Le style (palette `or-nuit`, typo premium, motion sobre) a été travaillé avant la structure (parcours, rôles de pages, hiérarchie).

**Méthodologie Jack Roberts (verbatim)** :

> *"Maintenant nous avons besoin de penser à ce que veut le site web"*
> — *"page d'accueil, page contact, page services, etc."*

Lesson substance-first : **avant de penser au design (couleurs / typo / motion), il faut d'abord penser à ce que veut le site web — c'est-à-dire : quelles pages, quels rôles, quel parcours utilisateur.** Le style vient ensuite, sur la substance.

**Intent** : codifier la doctrine **substance-first, then style** appliquée au sitemap + wireframe des Landing Pages OMK Nexus ⚖️. Définir :
- un **sitemap canonique 7 pages type**
- **3 patterns** applicables (Single-page focal / Multi-page écosystème / Hybrid)
- les **5 questions wireframe** Jack Roberts
- les **anti-patterns** (page-unique sans sitemap, page d'atterrissage = hero seul, multi-page sans hiérarchie)

Sisters immédiates : `ADR-LANDING-CRAFT-001 §4.2` (Phase 2 Wireframe) et `ADR-LANDING-CRAFT-001 §4.5` (Phase 5 Multi-Page Build).

## 2. Decision

### 2.1 Principe fondamental

> **Substance first, then style. Pas de page unique monolithique sans sitemap.**

Chaque landing OMK Nexus est **inscrite dans un écosystème de pages (sitemap)**, pas isolée. Avant d'écrire la première ligne de HTML / CSS / JS, on produit :

1. Le **sitemap canonique** (quelles URLs, quels rôles).
2. Le **wireframe 5 questions** (qui, action, objections, vibe, assets).
3. La **structure hiérarchique par page** (nav → hero → modules → pricing → FAQ → CTA → footer).

### 2.2 Sitemap canonique 7 pages type

Pour une **landing ICP complète** (multi-page écosystème ou hybride), les 7 pages canon :

| # | Page canon | Rôle | URL pattern | Présence |
|---|---|---|---|---|
| 1 | `index.html` | **Hub porte d'entrée** | `/` ou `/<hub>/` | obligatoire si multi-page / hybride |
| 2 | `<persona>.html` ou `services.html` | **Page d'atterrissage ICP** (manifest + modules + pricing + CTA) | `/<persona>/` ou `/services/` | obligatoire — c'est la landing |
| 3 | `pricing.html` | **Détail pricing** (si pas inclus dans `<persona>.html`) | `/pricing/` | optionnelle — peut être inline |
| 4 | `how-it-works.html` | **Détails wireframe Phase 2** (méthode, processus, étapes) | `/how-it-works/` | recommandée si > 3 modules |
| 5 | `faq.html` | **Objections / Q&A** | `/faq/` | recommandée si ICP a 3+ objections |
| 6 | `about.html` | **Manifest + cocréateurs** (crédibilité, équipe, doctrine) | `/about/` | recommandée pour ICP Conformité |
| 7 | `contact.html` | **CTA final** (form / email / calendar) | `/contact/` | obligatoire — pas de landing sans CTA final |

**OU** pattern single-page focal (cf. §2.4.1) si ≤ 5 modules / 1 ICP unique.

### 2.3 Structure hiérarchique par page (canon)

Chaque page du sitemap respecte la même hiérarchie verticale pour **cohérence cross-page** et **Information X-Ray** :

```
┌─────────────────────────────────────────────┐
│ NAV BAR (brand left · manifest center · CTA right)
├─────────────────────────────────────────────┤
│ HERO (manifeste court + CTA primaire + CTA secondaire)
├─────────────────────────────────────────────┤
│ MODULES / SERVICES (5 cards ou 3-4 sections)
├─────────────────────────────────────────────┤
│ PRICING (si applicable, sinon dans la landing)
├─────────────────────────────────────────────┤
│ FAQ (3-7 objections)
├─────────────────────────────────────────────┤
│ CTA FINAL (action unique attendue)
├─────────────────────────────────────────────┤
│ FOOTER (manifest signature + liens sibling ships)
└─────────────────────────────────────────────┘
```

**Information X-Ray pattern** : chaque section rend **UNE chose claire**. Une section = une information. Pas de section à moitié (un module qui explique deux concepts distincts = deux sections).

### 2.4 Patterns applicables

#### 2.4.1 Pattern A — Single-page focal

**Quand** : landing marketing ICP, 3 personas OMK Nexus, ≤ 5 modules, 1 ICP unique, exploration rapide.

**Forme** : 1 seul URL avec sections numérotées (`§1.0`, `[M01]`, `WORKBENCH 01`) qui délimitent les areas. **Section count = 3-7** (pas plus, sinon → Pattern B).

**V2 empirique** : `omk-nexus-landing-3-personas/v2/` — chaque persona (Marcus / Harrison / David) est actuellement en single-page focal. Conforme au Pattern A.

**Sister canon** : `ADR-NEXUS-LANDING-PERSONAS-001 §3.2` (single-file vanilla).

#### 2.4.2 Pattern B — Multi-page écosystème

**Quand** : ICP veut explorer en profondeur, > 5 modules, services détaillés, équipe, méthode, contact séparé.

**Forme** : 5-7 URLs distinctes (cf. §2.2 sitemap canon), chacune avec sa hiérarchie (§2.3), footer cohérent entre pages.

**Déclencheurs** :
- > 5 modules à présenter
- ICP Conformité (besoin de manifest + about + équipe)
- Pricing détaillé multi-tiers (pas inline)
- Méthode / processus long (how-it-works séparé)

#### 2.4.3 Pattern C — Hybrid

**Quand** : Holding hub + filiales par ICP (cf. `plan-L2 §5.4` Holding → Filiales VERSION FINALE).

**Forme** :
- `index.html` = Hub holding (porte d'entrée, choix de l'ICP).
- `<persona>.html` × N = Landing ICP par persona (Marcus / Harrison / David).
- `about.html` + `contact.html` partagés entre toutes les landings.

**V2 roadmap** : 3 personas OMK Nexus (Marcus / Harrison / David) → 1 hub + 3 landings + 2 partagés = 6 URLs. Sister FR (`omk-nexus-landing-page.vercel.app`) et EN (`omk-nexus-landing-en.vercel.app`) → × 2 = **12 URLs canon potentielles** (cf. §2.5).

### 2.5 Routes canoniques V2 (D1 empirique)

**Live actuellement** :
- `https://omk-nexus-landing-page.vercel.app` (FR, single-page focal, Pattern A)
- `https://omk-nexus-landing-en.vercel.app` (EN, single-page focal, Pattern A)

**Roadmap Pattern C (cible)** :
- Hub holding FR : `omk-nexus-hub-fr.vercel.app` (ou sub-path)
- Hub holding EN : `omk-nexus-hub-en.vercel.app`
- Landing Marcus FR/EN : `omk-nexus-marcus-{fr,en}.vercel.app`
- Landing Harrison FR/EN : `omk-nexus-harrison-{fr,en}.vercel.app`
- Landing David FR/EN : `omk-nexus-david-{fr,en}.vercel.app`
- About + Contact partagés (par langue)

→ **6+ URLs potentielles** en roadmap Pattern C, contre 2 actuellement en Pattern A.

## 3. Doctrine

### 3.1 Substance-first ordering (verrouillé)

```
SITEMAP  →  WIREFRAME  →  HIERARCHIE PAR PAGE  →  STYLE (palette / typo / motion)
   │              │                    │                       │
   │              │                    │                       └─ sister ADR-ANTI-TEMPLATE-001
   │              │                    └─ structure canon §2.3
   │              └─ 5 questions §4
   └─ 7 pages canon §2.2 + 3 patterns §2.4
```

Tout travail landing commence par le sitemap. Pas de pixel avant d'avoir répondu aux 5 questions wireframe (§4) sur **chaque page** du sitemap.

### 3.2 Information X-Ray

Chaque section d'une page = **UNE information claire**. Une section à moitié (module qui tente d'expliquer pricing ET méthode) = violation X-Ray → split en deux sections.

**Test X-Ray** : *"Si je screenshot cette section, peut-elle tenir seule avec son titre + 1 phrase + 1 visuel ?"*
- Oui → passe le test.
- Non → split ou refactor.

### 3.3 Cohérence cross-page (footer + nav)

Toute page du sitemap partage :
- **Nav bar** : brand left, manifest center, login/CTA right (cf. §2.3).
- **Footer** : manifest signature + liens vers sibling ships (autres pages du sitemap) + langues (FR/EN) si bi-langue.

Pas de footer ad-hoc par page. Pas de nav bar variant selon la page (sauf CTA contextualisé : "Prendre RDV" sur contact.html vs "Voir pricing" sur `<persona>.html`).

### 3.4 Sister-discipline

| Si tu touches à... | Tu lis d'abord... |
|---|---|
| Sitemap | ce ADR (ADR-MULTIPAGE-001) |
| Wireframe d'une page | ADR-LANDING-CRAFT-001 §4.2 |
| Build multi-page | ADR-LANDING-CRAFT-001 §4.5 |
| Modules / rails | ADR-NEXUS-EVOLUTION-IA-001 §5/§6 |
| Pattern single-file vanilla | ADR-NEXUS-LANDING-PERSONAS-001 §3.2 |
| Structure Holding→Filiales | plan-L2 §5.4 |
| Style (typo / palette / motion) | ADR-ANTI-TEMPLATE-001 |
| Page-unique sans sitemap | ADR-PAPERCLIP-002 |

## 4. Wireframe — 5 Questions Jack Roberts

Avant de wireframer **chaque page** du sitemap, répondre à ces 5 questions (méthodologie Jack Roberts appliquée) :

### Q1 — Qui est le visiteur ?

**PAS le business. LE VISITEUR.** Persona, contexte d'arrivée, intent.

> Exemple V2 — Marcus (ICP Conformité) :
> *"Coach / consultant indépendant qui cherche à formaliser sa pratique sans devenir une usine à gaz. Arrive via LinkedIn ou recherche Google 'coaching structuré'. Lit beaucoup, scroll peu."*

### Q2 — Quelle action unique veut-on qu'il prenne ?

**UNE seule action primaire par page.** Pas trois CTAs au même poids.

> Exemple V2 — Landing Marcus :
> *"Réserver un appel découverte de 20 minutes (CTA primaire). Téléchargement de la méthode en PDF (CTA secondaire, bas de page)."*

### Q3 — Quelles objections a-t-il ?

Lister 3-7 objections et y répondre **dans la page** (section FAQ ou inline).

> Exemple V2 — Objections Marcus :
> *"Je ne veux pas devenir dépendant d'une plateforme." · "C'est trop tôt pour formaliser." · "Et si mes clients ne suivent pas ?" · "Combien ça coûte vraiment ?" · "Je peux faire ça moi-même avec Notion."*

### Q4 — Quel est le vibe / ton ?

Cohérence cross-page : dark luxury sobre (`#0A0E16` + `#C8A55C`) sister canon. Pas de variation par page sauf intention éditoriale forte (et alors documentée dans cet ADR en amendement).

### Q5 — Brand assets existants à respecter ?

Inventaire des brand assets (logo, palette, typo, motion library, manifest signature) **avant** de wireframer. Si un asset manque, c'est une dette à remonter dans `_SPECS/ADR/` — pas une improvisation par page.

## 5. Anti-patterns

| # | Anti-pattern | Diagnostic | Remédiation |
|---|---|---|---|
| A1 | **Single-page monolithique sans sitemap** | Page > 7 sections, pas de route distincte, hero = 60% du viewport | Convertir en Pattern A borné (3-7 sections) ou Pattern B/C |
| A2 | **Page d'atterrissage = hero seul** | Pas de suite logique après le hero, scroll = rien | Ajouter Modules + Pricing + FAQ + CTA (cf. §2.3) |
| A3 | **Multi-page sans hiérarchie claire** | Chaque page = île, nav bar différente, footer incohérent | Imposer §2.3 sur toutes les pages, audit cross-page |
| A4 | **Pas de footer cohérent cross-page** | Footer ad-hoc par page, pas de liens sibling ships | Footer canon (§2.3 + §3.3) imposé |
| A5 | **Style d'abord, substance après** | Palette / typo travaillée avant sitemap + wireframe | Inverser l'ordre (§3.1) |
| A6 | **Section à moitié** (X-Ray fail) | Une section tente 2 informations | Split en 2 sections ou refactor |
| A7 | **Templates Inter/Roboto/Arial** | sister ADR-ANTI-TEMPLATE-001 violation | Typos canoniques premium (sister) |
| A8 | **Page-unique sans sister-ADR sitemap** | Aucun ADR n'a tracé le sitemap avant build | Cet ADR est la gate : pas de landing sans ADR sitemap ratifié |

## 6. Consequences

### 6.1 Positives

- **SEO** : chaque URL = entrée indépendante Google (Pattern B/C). Pattern A reste référençable mais avec une seule URL.
- **A/B testing** : variation 1 page sans toucher l'écosystème (Pattern B/C).
- **Partageabilité** : un persona = un URL partageable (`omk-nexus-marcus-fr.vercel.app`).
- **Itération rapide** : modifier 1 landing persona sans toucher sister (Pattern C).
- **Discipline cross-page** : nav + footer cohérents (§3.3) → cohérence de marque.
- **Évolutivité** : ajout d'un nouveau persona = 1 nouvelle URL + footer mis à jour (Pattern C extensible).

### 6.2 Negatives / Trade-offs

- **Coût initial sitemap + wireframe** : 1-2 jours de travail avant pixel (contre ~0 en single-page ad-hoc).
- **Maintenance cross-page** : footer / nav doivent rester synchro (sister-discipline §3.4).
- **Risque Pattern C over-engineered** : 12 URLs pour 3 personas peut sembler disproportionné — re-évaluer à 6 mois (Q3 2026 → Q4 2026).
- **Discipline substance-first** : résistances possibles (le style est plus "sexy" que la structure). ADR-PAPERCLIP-002 est la gate.

### 6.3 V1 lessons retenues

- 3 landing V2 actuellement single-page (Pattern A) — fonctionnent, mais bloquent l'évolution Pattern B/C sans refonte sitemap.
- Aucune n'a eu de sitemap tracé en amont → cette doctrine corrige.

## 7. Rollout

### Phase 1 — Immédiat (Sprint en cours)

- **Ratifier cet ADR** (status DRAFT → RATIFIED).
- **Mapper V2 actuel** : pour chaque landing `omk-nexus-landing-3-personas/v2/`, identifier le pattern (§2.4) et les 7 pages canon (§2.2) applicables.
- **Wireframer 5 questions** (§4) pour chaque landing existante.

### Phase 2 — Q3 2026 (12WY Cycle Q3 2026, en cours)

- Construire **Pattern C hybrid Holding→Filiales** (cf. `plan-L2 §5.4`) pour OMK Nexus :
  - 1 hub holding FR + 1 hub holding EN.
  - 3 landing personas FR (Marcus / Harrison / David).
  - 3 landing personas EN (sisters).
  - About + Contact partagés (×2 langues).
  - → 12 URLs roadmap cible.
- Sister-build avec `ADR-LANDING-CRAFT-001 §4.5` (Phase 5 Multi-Page Build).

### Phase 3 — Q4 2026 (post-12WY)

- Audit cross-page (footer / nav cohérence).
- A/B testing Pattern A vs Pattern C sur 1 persona pilote.
- Ré-évaluer la dette sitemap si de nouvelles pages sont ajoutées.

## 8. Sister ADRs & References

### 8.1 Sisters immédiates

- **ADR-LANDING-CRAFT-001 §4.2** — Phase 2 Wireframe (substance-first).
- **ADR-LANDING-CRAFT-001 §4.5** — Phase 5 Multi-Page Build (implémentation).
- **ADR-NEXUS-LANDING-PERSONAS-001 §3.2** — single-file vanilla canon (Pattern A sister).

### 8.2 Sisters ancre

- **ADR-NEXUS-EVOLUTION-IA-001 §5/§6** — modules + rails existants à câbler dans le sitemap.
- **plan-L2 §5.4** — Holding → Filiales VERSION FINALE (structure cible Pattern C).
- **ADR-ANTI-TEMPLATE-001** — pas Inter/Roboto/Arial (style discipline).
- **ADR-PAPERCLIP-002** — anti-page-unique sans sitemap (gate).

### 8.3 References empiriques V2

- `C:\Users\amado\omk-nexus-landing-3-personas\v2\` — 3 personas + index (single-page Pattern A, base de la roadmap multi-page).
- `https://omk-nexus-landing-page.vercel.app` (FR, LIVE, Pattern A).
- `https://omk-nexus-landing-en.vercel.app` (EN, LIVE, Pattern A).

### 8.4 Source doctrine

- **Jack Roberts methodology (video transcript)** — *"Maintenant nous avons besoin de penser à ce que veut le site web"* → *"page d'accueil, page contact, page services, etc."* — lesson substance-first (cf. frontmatter `sources_canons[0]`).

## 9. ADR Status & Ratification

- **Statut** : DRAFT (2026-07-06).
- **Prochaine étape** : ratification par A0-Jumeau-Numerique via skill `ratify-adr`.
- **Amendements attendus** : Phase 2 (Q3 2026) ajoutera les wireframes concrètes Pattern C (12 URLs OMK Nexus cibles).
- **Sunset clause** : si Pattern A tient > 12 mois sans besoin Pattern B/C, re-évaluer §2.5 roadmap.

---

**B1 E-Myth Gatekeeper — Substance first, then style. Le sitemap est la gate ; pas de pixel avant d'y avoir répondu.**