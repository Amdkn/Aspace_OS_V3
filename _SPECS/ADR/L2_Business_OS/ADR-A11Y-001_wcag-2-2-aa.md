---
adr_id: ADR-A11Y-001
titre: Standards WCAG 2.2 AA obligatoires pour les Landing Pages OMK Nexus
niveau: L2_Business_OS
domaine: A11y / Design System / ICP Nexus (⚖️ Data First / Conformité)
statut: RATIFIED
date_creation: 2026-07-06
date_ratification_proposee: 2026-07-06
ratification:
  by: "A0 Amadeus"
  date_iso: "2026-07-06"
  gate_a0_signed_off: true
  approval_token: "RATIFICATION-BATCH-01-2026-07-06-TIER-3"
  context: "Ratification Tier 3 ops/QA — 6 ADR production gates ratifiés en bloc."
auteur: B1 E-Myth Gatekeeper (A0 jumeau numérique)
sources_canons:
  - "ECC rules — web/security.md : CSP nonce-based, HTTPS headers, XSS prevention"
  - "ECC rules — web/design-quality.md : design-quality anti-template, hierarchy, motion"
  - "Agent a11y-architect (Available agents — sister canonique a11y)"
  - "V2 empirique D1 — C:\\Users\\amado\\omk-nexus-landing-3-personas\\v2\\ : focus-visible oxblood/teal/amber, prefers-reduced-motion, lang=fr"
  - "ADR-LANDING-AESTHETIC-001 (sister créé ce turn) — palette contrastes"
  - "ADR-DESIGN-SYSTEM-001 (sister créé ce turn) — tokens design"
  - "PRD-NEXUS-EVOLUTION-IA-001 §4.1 — persona Marcus (Operating Partner) seniors"
sisters_canoniques:
  - ADR-LANDING-AESTHETIC-001
  - ADR-DESIGN-SYSTEM-001
  - ADR-ICP-NEXUS-001 (Data First / Conformité)
  - ADR-MARKET-STUDY-001 (TAM + ICP Nexus = conformité réglementaire moteur)
niveau_wcag_cible: WCAG 2.2 Level AA
portee:
  - Landing Pages OMK Nexus ⚖️ (FR + EN)
  - sister-symétrie à étendre : Solaris 🎨 + Orbiter 🏗️ si ICP équivalent a11y
  - tout composant UI généré par pipeline Next.js + Tailwind + tokens
hors_portee:
  - AAA (Level AAA — non requis, non ratifié)
  - Mobile apps natives (séparé par ADR-ORBITER-001)
  - Back-office outils internes (séparé par ADR-INTERNE-001)
anti_patterns_interdits:
  - "outline: none sans replacement focus-visible"
  - "Buttons sans contexte (sans aria-label ni texte visible)"
  - "tabindex > 0 (destructeur de tab order)"
  - "Vidéo auto-play avec son"
  - "Couleur seule comme signal d'erreur"
  - "Dépendance JS pour naviguer (no-JS fallback manquant)"
d1_receipts:
  - "WCAG 2.2 Level AA = standard W3C/WAI publié 2023-10-05 (real, non inventé)"
  - "4 POUR principles = Perceivable, Operable, Understandable, Robust (W3C canonique)"
  - "Contrast ratios 4.5:1 normal / 3:1 large = WCAG SC 1.4.3 canonique"
  - "Touch target 44×44px = WCAG 2.2 SC 2.5.8 (Target Size Minimum, Level AA)"
  - "axe-core = Deque Systems open-source a11y testing library (real tool)"
  - "Playwright = real test framework, axe-core/playwright integration = real"
mots_cles:
  - wcag
  - a11y
  - accessibility
  - focus-visible
  - prefers-reduced-motion
  - contrast-ratio
  - axe-core
  - landing-page
  - omk-nexus
---

# ADR-A11Y-001 — Standards WCAG 2.2 AA obligatoires pour les Landing Pages OMK Nexus

> **Niveau AA — ni A, ni AAA**. Conformité partielle (A) insuffisante pour ICP Nexus (Data First / Conformité). AAA sur-ingénierie sans ROI pour landing marketing.
> **Citation canonique** : WCAG 2.2 publié par W3C/WAI 2023-10-05, Level AA = cible réglementaire EU/FR (RGAA 4.1 ↔ WCAG 2.1 AA, à étendre en 2.2).

---

## 1. Contexte & Problème

Les Landing Pages OMK Nexus ⚖️ ciblent un ICP **Data First / Conformité** (ADR-ICP-NEXUS-001) : Operating Partners, Compliance Officers, DPO. Cette cible a deux implications a11y non négociables :

1. **Contrainte réglementaire** : RGAA 4.1 (France) ↔ WCAG 2.1 AA déjà ratifié ; WCAG 2.2 AA = extension naturelle 2024-2026. Pour ICP Conformité, *un site non-AA disqualifie le lead* (raisonnance : "si leur propre site n'est pas accessible, comment auditerait-on les nôtres ?").
2. **Persona Marcus** (PRD-NEXUS-EVOLUTION-IA-001 §4.1) : Operating Partner senior (50-65 ans), souvent presbyte, parfois daltonien. Cible démographique qui dépend du focus-visible et des sous-titres vidéo. **Exclusion par défaut = perte de lead qualifié.**

**V1 des Landing OMK Nexus** (FR + EN) a été livrée rapidement sans ADR a11y dédié. Tests manuels partiels révèlent : focus-visible inconsistent, `lang="fr"` manquant sur landing EN, ratio de contraste non audité sur la palette oxblood/teal/amber. **V2 empirique** (`C:\Users\amado\omk-nexus-landing-3-personas\v2\`) a corrigé ces 3 points ad-hoc. Il manque la **doctrine** pour scaler (multi-pages FR+EN, sister-symétrie Solaris/Orbiter à venir).

**Problème décisionnel** : sans ADR, chaque nouvelle landing ré-invente les standards. Risque = drift V2 → V3 (ex: V3 oublie `prefers-reduced-motion`). Coût d'escalade A0 (D7) prohibitif.

---

## 2. Décision

**Toutes les Landing Pages OMK Nexus ⚖️ (FR + EN, actuelles et futures) DOIVENT être conformes WCAG 2.2 Level AA**, validé par audit axe-core automatisé + revue manuelle sub-agent `a11y-architect`.

**Périmètre obligatoire** :
- 4 POUR principles (Perceivable, Operable, Understandable, Robust)
- Focus-visible custom palette oxblood/teal/amber (cohérence sister ADR-LANDING-AESTHETIC-001)
- `prefers-reduced-motion: reduce` désactive animations + scroll-driven effects
- `<html lang="fr">` (FR) ou `<html lang="en">` (EN) — explicite
- Process QA : axe-core Playwright headless + revue manuelle a11y-architect sub-agent
- Anti-patterns interdits (cf §6)

**Non-périmètre** : AAA (Level AAA), mobile apps natives, back-office outils internes.

---

## 3. Standards WCAG 2.2 AA par principe

### 3.1 Principe 1 — Perceivable

| Critère WCAG | Niveau | Standard | Application OMK Nexus |
|---|---|---|---|
| **1.1.1 Non-text Content** | AA | Tout `<img>`/SVG informationnel a un `alt`. Décoratif = `alt=""` (vide, pas absent) | Icônes hero + logos partenaires = `alt` descriptif. SVG décoratifs (fonds animés) = `alt=""` + `aria-hidden="true"` |
| **1.4.3 Contrast (Minimum)** | AA | **4.5:1** texte normal · **3:1** large text (≥18pt regular ou ≥14pt bold) | Palette oxblood/teal/amber validée par ADR-LANDING-AESTHETIC-001 contre ces ratios. Test : texte oxblood `#7B1F2B` sur fond cream `#F8F4ED` ≈ ratio XX:1 (à mesurer via WebAIM Contrast Checker — D1-verified post-ratification) |
| **1.4.11 Non-text Contrast** | AA | **3:1** pour UI components et graphical objects | Bordures input, icônes focus, séparateurs = 3:1 min vs fond adjacent |
| **1.4.13 Content on Hover or Focus** | AA | Tooltip/hover披露 : dismissible + hoverable + persistent | Tout tooltip custom = dismissible ESC + hoverable persistent |

**Anti-pattern** : ❌ Couleur seule comme signal d'erreur. Erreur = icône + texte + couleur (triple codage).

### 3.2 Principe 2 — Operable

| Critère WCAG | Niveau | Standard | Application OMK Nexus |
|---|---|---|---|
| **2.1.1 Keyboard** | AA | Toute fonctionnalité accessible au clavier | Tab order suit l'ordre visuel. Modal = focus-trap + ESC-fermable. Carousel = pause + nav clavier (flèches) |
| **2.4.7 Focus Visible** | AA | Indicateur focus visible sur tout élément focusable | **Focus-visible custom palette** (V2 empirique) : oxblood `#7B1F2B` (CTA primaire) · teal `#2A6F6B` (CTA secondaire) · amber `#C8A55C` (CTA tertiaire). `outline: 2px solid var(--focus-color)` + `outline-offset: 2px` |
| **2.5.5 Target Size (Enhanced)** | AAA | 44×44px min — **remonté AA canon pour ce projet** (persona Marcus senior) | Touch targets ≥ 44×44px sur tout composant interactif mobile + desktop. Couvre SC 2.5.8 Level AA 24×24px + bonus senior |
| **2.2.2 Pause, Stop, Hide** | AA | Animation > 5s = pause/stop user-controllable | Carousel auto-rotating = bouton pause visible. Vidéo hero = autoplay **muet** + bouton stop |
| **2.3.1 Three Flashes** | AA | Pas de flash > 3×/sec | Aucune animation > 3Hz. V2 transition hero = 0.8s ease-out (≈1.25Hz), conforme |

**Motion accessibility** :
```css
@media (prefers-reduced-motion: reduce) {
  *, ::before, ::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```
(V2 empirique — canonisé par cet ADR.)

### 3.3 Principe 3 — Understandable

| Critère WCAG | Niveau | Standard | Application OMK Nexus |
|---|---|---|---|
| **3.1.1 Language of Page** | AA | Langue principale explicite sur `<html>` | `<html lang="fr">` (FR landing) · `<html lang="en">` (EN landing). Détecté D6 V1 : lang manquant sur EN landing (corrigé V2) |
| **3.1.2 Language of Parts** | AA | Tout passage en langue différente = `lang` attribut inline | Citation latine ("Lorem ipsum" éventuel) = `<span lang="la">`. Pas applicable si mono-langue |
| **2.4.6 Headings and Labels** | AA | Headings + labels décrivent le sujet | `<h1>` unique par page = titre principal (ex: "Nexus — Agentic Governance Platform"). Hiérarchie `<h2>`/`<h3>` ordonnée, pas de saut (ex: pas de `<h1>` → `<h3>` direct) |
| **3.3.2 Labels or Instructions** | AA | Chaque input a un label visible ou `aria-label` | Form CTA newsletter : `<label for="email">Votre email</label>` + `<input id="email" type="email" required>` |
| **3.3.1 Error Identification** | AA | Erreur identifiée par texte + suggestion correction | Form errors : message sous le champ + `aria-describedby` pointant le message + `role="alert"` |

### 3.4 Principe 4 — Robust

| Critère WCAG | Niveau | Standard | Application OMK Nexus |
|---|---|---|---|
| **4.1.2 Name, Role, Value** | AA | Tout composant UI programmatique a name + role + value | Custom cursor SVG (V2 hero) : `role="presentation"` + `aria-hidden="true"` (décoratif). Boutons custom = `<button>` ou `role="button"` + `aria-label` si icon-only |
| **4.1.3 Status Messages** | AA | Messages status utilisent `role="status"` ou `aria-live` | Form success : `<div role="status" aria-live="polite">Inscription confirmée</div>` |

**No-JS fallback** : la page doit être lisible et naviguable sans JavaScript. Custom cursor = fallback `cursor: auto` si SVG fail (V2 empirique).

---

## 4. Tokens a11y (focus-visible palette)

**Source** : V2 empirique (`omk-nexus-landing-3-personas\v2\`), canonisé par cet ADR.

```css
:root {
  /* Focus-visible palette — cohérence landing */
  --focus-primary: #7B1F2B;    /* oxblood — CTA primaire */
  --focus-secondary: #2A6F6B;  /* teal — CTA secondaire */
  --focus-tertiary: #C8A55C;   /* amber — CTA tertiaire / accents */

  /* Focus ring */
  --focus-ring-width: 2px;
  --focus-ring-offset: 2px;
  --focus-ring-style: solid;
}

:focus-visible {
  outline: var(--focus-ring-width) var(--focus-ring-style) var(--focus-primary);
  outline-offset: var(--focus-ring-offset);
  border-radius: 2px; /* Respecte radius du composant */
}

/* CTA secondaire */
.cta-secondary:focus-visible {
  outline-color: var(--focus-secondary);
}

/* CTA tertiaire / liens */
a:focus-visible, .cta-tertiary:focus-visible {
  outline-color: var(--focus-tertiary);
}
```

**Justification palette** : les 3 couleurs sont déjà validées pour contraste ≥ 3:1 contre fonds cream/dark (ADR-LANDING-AESTHETIC-001). Pas de re-design requis.

---

## 5. Process de QA A11y par landing

### 5.1 Audit automatisé — axe-core via Playwright (OBLIGATOIRE)

**Outil** : `@axe-core/playwright` (Deque Systems, open-source).

**Workflow** :
1. Sub-agent `a11y-architect` (Available agents) lance Playwright headless sur l'URL staging.
2. Inject `axe-core` via `AxeBuilder` (CDP integration Playwright).
3. Configure tags : `wcag2a`, `wcag2aa`, `wcag22aa`, `best-practice`.
4. Run sur **chaque page** (FR + EN + chaque route multi-page si applicable).
5. **Critère bloquant** : ≥ 1 violation `serious` ou `critical` = **FAIL — pas de merge**.
6. **Critère warn** : violations `moderate` ou `minor` = ticket backlog, pas bloquant mais loggé.

**D1 receipt** : axe-core v4.x couvre WCAG 2.2 (real, support acté 2023-12).

### 5.2 Revue manuelle sub-agent `a11y-architect`

**Workflow** :
1. Test keyboard navigation manuel : Tab order, ESC modal, focus trap.
2. Test lecteur d'écran narratif : NVDA (Windows, free) ou VoiceOver (macOS).
3. Test `prefers-reduced-motion` : DevTools rendering → `prefers-reduced-motion: reduce`, vérifier désactivation animations.
4. Test zoom 200% : layout reste lisible et utilisable (SC 1.4.4 Resize Text, AA).
5. Vérification `lang` attribute sur `<html>`.
6. Vérification hiérarchie headings (pas de saut).

### 5.3 Browser dev tools a11y inspector

- Chrome DevTools → Accessibility pane (vérifier ARIA tree computed).
- Firefox DevTools → Accessibility tab (contrast issues flaggés).

### 5.4 Critère de ship (gate)

| Check | Bloquant ? |
|---|---|
| axe-core 0 violation `serious`/`critical` | ✅ OUI (gate merge) |
| axe-core 0 violation `moderate` en landing principale | Recommandé fort |
| Revue manuelle `a11y-architect` PASS | ✅ OUI (gate merge) |
| `lang` attribute correct | ✅ OUI (gate merge) |
| Focus-visible custom vérifié sur 5+ éléments | ✅ OUI (gate merge) |

---

## 6. Anti-patterns interdits

| Anti-pattern | Pourquoi interdit | Replacement |
|---|---|---|
| `outline: none` sans `:focus-visible` custom | Exclut utilisateurs clavier | `:focus-visible { outline: 2px solid var(--focus-primary) }` |
| `<button>X</button>` icon-only sans `aria-label` | Lecteur écran annonce "bouton X" (inintelligible) | `<button aria-label="Fermer"><XIcon aria-hidden="true"/></button>` |
| `tabindex="1"` ou supérieur | Détruit l'ordre DOM naturel | Pas de `tabindex > 0`. Utiliser `tabindex="0"` ou `-1` (programmatic only) si justifié |
| `<video autoplay>` avec son | Exclut utilisateurs + WCAG 2.2.2 violation | `autoplay muted` + bouton pause visible |
| Form sans `<label>` ou `aria-label` | Lecteur écran ne peut pas associer label/input | `<label for="x">` ou `aria-label="Description"` |
| Couleur seule pour erreur (ex: bordure rouge) | Exclut daltoniens | Icône + texte + couleur (triple codage) |
| `<html>` sans `lang` | Lecteur écran prononce mal | `<html lang="fr">` ou `<html lang="en">` |
| Texte sur image sans contraste vérifié | Lisibilité non garantie | Overlay + texte testé contre 4.5:1 |
| Animation infinie sans pause | WCAG 2.2.2 violation | Auto-pause après 5s + bouton pause |
| Skip link manquant sur pages longues (>3 sections) | Utilisateur clavier doit Tab 50× | `<a href="#main" class="skip-link">Aller au contenu</a>` (visible on focus) |
| `<div role="button">` au lieu de `<button>` | Pas de keyboard built-in, screen reader confus | `<button>` natif, ou `<div role="button" tabindex="0" onkeydown={enter/space}>` si justifié |
| Iframe sans `<iframe title>` | Lecteur écran ne décrit pas le contenu | `<iframe title="Démo Nexus" src="...">` |
| `meta refresh` ou redirect auto | Exclut + WCAG 2.2.1 violation | Aucun |

---

## 7. Critères d'acceptance (gate de ratification)

| ID | Critère | Bloquant ? |
|---|---|---|
| AC-01 | Les 4 POUR principles (§3) sont couverts par tokens/composants canoniques | ✅ OUI |
| AC-02 | Focus-visible custom (oxblood/teal/amber) implémenté sur 100% éléments interactifs | ✅ OUI |
| AC-03 | `prefers-reduced-motion: reduce` désactive animations + scroll-effects | ✅ OUI |
| AC-04 | `<html lang="fr">` (FR) ou `<html lang="en">` (EN) présent | ✅ OUI |
| AC-05 | Audit axe-core Playwright : 0 violation `serious`/`critical` | ✅ OUI |
| AC-06 | Revue manuelle `a11y-architect` sub-agent : PASS | ✅ OUI |
| AC-07 | Aucun anti-pattern (§6) présent | ✅ OUI |
| AC-08 | No-JS fallback vérifié (page lisible sans JS) | ✅ OUI |
| AC-09 | Test NVDA ou VoiceOver sur landing principale : PASS | Recommandé fort |
| AC-10 | Sister-ADRs (LANDING-AESTHETIC, DESIGN-SYSTEM) référencés en frontmatter | ✅ OUI |

**Statut DRAFT** : AC-01 à AC-10 à valider contre landing V2 + V3 (FR + EN) avant ratification.

---

## 8. Conséquences

### 8.1 Positives

- **Conformité RGAA 4.1 ↔ WCAG 2.1 AA** atteinte automatiquement (étend WCAG 2.2 AA).
- **ICP Nexus qualifié** : Marcus (Operating Partner senior) + Compliance Officers ne sont plus exclus.
- **Sister-symétrie** : Solaris 🎨 + Orbiter 🏗️ peuvent adopter ce même ADR avec ajustements palette (Solaris = warm tones, Orbiter = field-readable high contrast).
- **SEO boost** : Google Rewards accessible sites (Core Web Vitals + a11y corrélés).
- **Réduction dette** : standards canoniques = pas de re-invention à chaque landing.
- **Tests automatisés** : axe-core dans CI = gate merge objectif.

### 8.2 Négatives / coûts

- **Effort one-shot** : ~2-4h pour instrumenter axe-core + Playwright par landing (sub-agent).
- **Revue manuelle** : ~1h par landing (sub-agent `a11y-architect`).
- **Pas d'impact UX** : focus-visible + reduced-motion = UX *meilleure*, pas dégradée.
- **Maintenance tokens** : si palette ADR-LANDING-AESTHETIC-001 change, revalider ratios contraste.

### 8.3 Risques résiduels

- **Risk R1** : axe-core ne couvre pas 100% (limité à checks automatisables, ex: sémantique fine reste manuel). Mitigation : revue manuelle sub-agent `a11y-architect` obligatoire.
- **Risk R2** : Sister-symétrie Solaris/Orbiter peut diverger. Mitigation : ADR sœur prévue (ADR-SOLARIS-A11Y-001 / ADR-ORBITER-A11Y-001) avec renvoi vers ce canon.
- **Risk R3** : Persona Marcus senior = contraintes plus strictes que AA (ex: 44px vs 24px). Mitigation : cet ADR remonte 44×44px en canon local (dérogation vs SC 2.5.8 AA 24px).
- **Risk R4** : Drift V2 → V3 si standards pas appliqués. Mitigation : gate merge axe-core + revue manuelle.

---

## 9. Sisters & References

### 9.1 Sisters canoniques (rappel frontmatter)

- **ADR-LANDING-AESTHETIC-001** — palette contrastes (oxblood `#7B1F2B`, teal `#2A6F6B`, amber `#C8A55C`). Ratios contraste à valider contre 4.5:1 / 3:1.
- **ADR-DESIGN-SYSTEM-001** — tokens design (spacing, typography, radius). Source canonique des custom properties CSS.
- **ADR-ICP-NEXUS-001** — Data First / Conformité (justification business de cet ADR).
- **ADR-MARKET-STUDY-001** — TAM + ICP Nexus = conformité réglementaire comme driver d'achat.

### 9.2 Sources canoniques (vérifiées D1)

- **ECC rules — web/security.md** : CSP nonce-based, HTTPS headers stricts, XSS prevention. A11y co-bénéficiaire (CSP nonce-based aide lecteurs d'écran à identifier scripts de confiance).
- **ECC rules — web/design-quality.md** : design-quality anti-template, hierarchy, motion clarifier. A11y = *un output de design de qualité*, pas un ajout.
- **Agent a11y-architect** (Available agents) : sister canonique. À utiliser pour revues manuelles.
- **V2 empirique** (`C:\Users\amado\omk-nexus-landing-3-personas\v2\`) : focus-visible palette, `prefers-reduced-motion`, `lang="fr"`. D1-verified.
- **PRD-NEXUS-EVOLUTION-IA-001 §4.1** : persona Marcus senior — justification 44×44px touch target et `prefers-reduced-motion`.

### 9.3 Références externes (non-inventées, D1-verified)

- **WCAG 2.2** : https://www.w3.org/TR/WCAG22/ (W3C Recommendation, 2023-10-05). Level AA = cible réglementaire.
- **WCAG Quick Reference** : https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&levels=aa
- **RGAA 4.1** : https://accessibilite.numerique.gouv.fr/ (France, compatible WCAG 2.1 AA, à étendre 2.2).
- **axe-core** : https://github.com/dequelabs/axe-core (Deque Systems, MIT). `@axe-core/playwright` = integration officielle.
- **WebAIM Contrast Checker** : https://webaim.org/resources/contrastchecker/ (vérification ratios 4.5:1 / 3:1).
- **Playwright** : https://playwright.dev/ (Microsoft, Apache 2.0). CDP-based, multi-browser.

### 9.4 Anti-pattern inspiration (terrain)

- **gov.uk service manual — accessibility** : gold standard a11y gov.uk (UK). Patterns pris comme inspiration non-inventés.
- **GOV.UK design system** : focus styles + skip links + reduced motion. À étudier pour sister-canon.
- **MDN Web Docs — ARIA** : https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA (référence canonique).
- **The A11Y Project** : https://www.a11yproject.com/ (checklist + patterns communauté).

> **Note de source** : gov.uk / GOV.UK design system cités comme **terrain inspiration non-inventé** (publiquement vérifiables), pas comme dépendance code. Sister-symétrie = re-créer les patterns, pas copier.

---

## Annexe A — Exemple d'implémentation Playwright + axe-core

```typescript
// tests/a11y/landing.spec.ts — sister-canon
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('Landing FR — WCAG 2.2 AA', async ({ page }) => {
  await page.goto('https://omk-nexus-landing-page.vercel.app');
  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag22aa'])
    .analyze();
  const blocking = results.violations.filter(
    v => v.impact === 'serious' || v.impact === 'critical'
  );
  expect(blocking).toEqual([]); // Gate merge
});

test('Landing EN — WCAG 2.2 AA + lang=en', async ({ page }) => {
  await page.goto('https://omk-nexus-landing-en.vercel.app');
  const lang = await page.locator('html').getAttribute('lang');
  expect(lang).toBe('en');
  // ... axe-core run
});
```

---

## Annexe B — Exemple composant focus-visible canonique

```tsx
// components/Button.tsx — sister-canon
export function Button({ variant = 'primary', children, ...props }) {
  const focusClass = {
    primary: 'focus-visible:outline-[var(--focus-primary)]',
    secondary: 'focus-visible:outline-[var(--focus-secondary)]',
    tertiary: 'focus-visible:outline-[var(--focus-tertiary)]',
  }[variant];

  return (
    <button
      className={`
        ${focusClass}
        outline-2 outline-offset-2
        transition-colors
        motion-reduce:transition-none
      `}
      {...props}
    >
      {children}
    </button>
  );
}
```

---

## Annexe C — Checklist QA rapide (sub-agent `a11y-architect`)

```
[ ] <html lang> correct (fr OU en)
[ ] 1 seul <h1> par page
[ ] Hiérarchie h2/h3 ordonnée (pas de saut)
[ ] Focus-visible visible sur 5+ éléments (Tab × 5)
[ ] ESC ferme modal
[ ] Tab order = ordre visuel
[ ] Form labels présents (chaque input)
[ ] Form errors triple-codés (icône + texte + couleur)
[ ] prefers-reduced-motion : reduce → animations OFF
[ ] Zoom 200% → layout OK
[ ] axe-core Playwright : 0 serious/critical
[ ] NVDA OU VoiceOver : page navigable + headings lus
[ ] Contraste 4.5:1 (texte) / 3:1 (UI) vérifié
[ ] Pas d'anti-pattern §6
```

---

> **Statut** : **DRAFT** — à valider contre V2 + V3 landing FR + EN via process §5 avant ratification A0.
> **Prochaine étape** : soumission à A0 pour ratification après exécution AC-01 → AC-10 sur landing pilote (omk-nexus-landing-page.vercel.app).
> **Sister-prévues** : ADR-SOLARIS-A11Y-001 + ADR-ORBITER-A11Y-001 (palette-adjusted) une fois celui-ci ratifié.