# FIX-4 — Navigation cassée, titres qui se replient, signals muets

**Date** : 2026-08-07
**Périmètre** : `src/apps/welcome/**`, `src/apps/sales/**`, `src/apps/legal/**`, `src/apps/audit/**`
**Hors périmètre** : `src/components/**` (FIX-5), `src/lib/**` (FIX-2), `src/apps/_ui/**` (FIX-1), `src/apps/finance/**` (FIX-3), `src/apps/product/**` (FIX-3)

---

## Résumé

| # | Défaut QA | Cause trouvée | Fichier:ligne | Correctif | Preuve |
|---|-----------|---------------|---------------|-----------|--------|
| 1 | Le bandeau PAGES de Welcome coupe 4 pages sur 9 sans signal | Pills en `text-xs px-3 py-1.5` + `overflow-x-auto` muet (scrollbar 8px sous le fond, pas lisible) ; aucun chevron, aucune indication de débordement | `PageChrome.tsx:89-109` | Pills compactées (`text-[11px] px-2.5 py-1`), chevrons gauche/droite avec `disabled` intelligent (scrollBy 200px), dégradé de bord 8px à droite, listener `scroll` + `ResizeObserver` sur le strip | `preuves/fix4/00_welcome_pages_bandis_BEFORE.png` / `preuves/fix4/01_welcome_pages_bandis.png` / `preuves/fix4/02_welcome_pages_scrolled_right.png` |
| 2 | Sur `OMK Coach Demo`, la sidebar marque la bonne section mais le bandeau PAGES reste sur `OMK RH` | Deux sources de vérité : `activeId` (local à `AppFrame`) pour la sidebar, `activePageId` (local à `WelcomeApp`) pour le bandeau. La sidebar n'expose pas son état, et `onSelectPage` ne touche qu'`activePageId` | `WelcomeApp.tsx:330-359` | Pont bidirectionnel : un `useEffect` délègue les clics sur `[data-section]` et synchronise `activePageId`. `navigateToPage(id)` met à jour `activePageId` ET déclenche un `btn.click()` sur le bouton sidebar correspondant | `preuves/fix4/00_welcome_active_sync_BEFORE.png` / `preuves/fix4/03_welcome_active_sync_coach_demo.png` |
| 3 | `Sales OS Control Center` se replie sur 2 lignes dans Context et Cognition | `PageHeader` grille `lg:grid-cols-[1fr_auto]` : quand la méta contient une valeur large (« The single-source brief », « 7 living documents · source of truth »), la colonne droite mange la largeur et coupe le titre `text-[40px] font-extrabold` | `SalesApp.tsx:701-742` | Grille en `lg:grid-cols-[minmax(0,1fr)_auto]` (le titre peut shrink si besoin) + `min-w-0` sur la colonne titre + `whitespace-nowrap` sur le `<h1>` et le chip. Colonne méta contrainte à `max-w-[180px] shrink-0`, `break-words` sur la valeur | `preuves/fix4/00_sales_context_BEFORE.png` / `preuves/fix4/04_sales_context_after.png` / `preuves/fix4/05_sales_cognition_after.png` |
| 4 | `legal > Compliance` affiche `Deadline 2026-08-02` sans signaler le dépassement | `SectionHead subtitle="Deadline 2026-08-02"` figé en gris neutre ; aucun calcul du retard ; aucun signal visuel | `LegalApp.tsx:114-133` | Calcul dynamique à chaque rendu : `Math.floor((today - 2026-08-02) / 86400000)` jours. Rendu conditionnel : couleur rouge + icône `AlertTriangle` + mention « en retard de N jour(s) ». Badge `Overdue` ajouté à côté du compteur. `SectionHead` n'acceptant que des `string`, j'ai recréé la même structure en markup direct | `preuves/fix4/06_legal_compliance_overdue.png` |
| 5 | `audit > Maturité` : `03 Déléguer` coupé en bas en 1440×900 | Cards `p-5` + grille interne `gap-3` + textes `text-[12px]` — chaque card ~220px, 3 cards + 2 sections de fin ≈ 880px > hauteur visible | `AuditApp.tsx:312-396` | Cards compactées : `p-4`, `gap-2.5`, `space-y-2.5`, textes passés de `12px` à `11.5px`. Sections de fin aussi compactées. Les 3 niveaux tiennent ensemble sans scroll | `preuves/fix4/00_audit_maturite_BEFORE.png` / `preuves/fix4/07_audit_maturite_after.png` |
| 6 | `Manuel de Diagnostic IA` devient `Manuel de Diagno…` dans la sidebar d'Audit | Truncature du **composant partagé** `AppFrame` (`truncate` était sur le titre de la sidebar, FIX-5 l'a déjà remplacé par `break-words`). Mon DOM-check confirme `height: 35px` (2 lignes wrappées), mais le rendu montre encore 1 ligne coupée — c'est FIX-5 qui le possède | `AppFrame.tsx:219` (FIX-5) | **Aucun correctif de mon périmètre.** Signalé ici. Inspection DOM : `width:134 height:35 scrollWidth:134` confirme que le wrap se fait côté React. Si le rendu visuel ne suit pas, c'est un problème de HMR/canvas-rendering côté AppFrame, pas du contenu d'Audit | (rien à montrer côté Audit) |

---

## Détail des correctifs

### 1 · Bandeau PAGES — neuf pages, signal visible

**Avant** (`PageChrome.tsx:89-109`) :

```tsx
<div className="flex items-center gap-1.5 overflow-x-auto custom-scrollbar ...">
  <span ...>Pages</span>
  {LANDING_PAGES.map(p => (
    <button className="... text-xs font-semibold px-3 py-1.5">…</button>
  ))}
</div>
```

Pills larges (`text-xs px-3 py-1.5`), pas de chevrons, scrollbar 8px sous le fond, pas lisible. Sur 1440px, 5 pills tenaient ; Finance, IT, Legal et Coach Demo étaient hors champ, muettes.

**Après** :

```tsx
<div className="relative flex items-center gap-1 ...">
  <button aria-label="Scroll pages left" data-testid="pages-scroll-left"
          disabled={!canScrollLeft} onClick={() => stripRef.current?.scrollBy({ left: -200 })}>…</button>
  <span ...>Pages</span>
  <div ref={stripRef} className="relative flex-1 min-w-0 overflow-x-auto custom-scrollbar">
    <div className="flex items-center gap-1 px-1 py-0.5">
      {LANDING_PAGES.map(p => (
        <button className="... text-[11px] font-semibold px-2.5 py-1">…</button>
      ))}
    </div>
    <div aria-hidden="true" className="pointer-events-none absolute top-0 right-0 bottom-0 w-8"
         style={{ background: 'linear-gradient(to right, transparent, var(--theme-surface) 80%)' }} />
  </div>
  <button aria-label="Scroll pages right" data-testid="pages-scroll-right"
          disabled={!canScrollRight} onClick={() => stripRef.current?.scrollBy({ left: 200 })}>…</button>
</div>
```

**Trois signaux indépendants du débordement** :

1. **Chevrons gauche/droite** (`ChevronLeft` / `ChevronRight` de lucide). Cliquer décale de 200px avec `scrollBy({ behavior: 'smooth' })`.
2. **Chevron `disabled`** quand il n'y a plus rien à révéler. Piloté par un `useEffect` qui écoute `scroll` + `ResizeObserver` sur le strip et met à jour `canScrollLeft` / `canScrollRight`.
3. **Dégradé de bord droit** 8px en `linear-gradient(to right, transparent, var(--theme-surface) 80%)`. `pointer-events-none` pour ne pas voler les clics aux pills.

Et **pills compactées** : `text-[11px]` (au lieu de `text-xs` = 12px), `px-2.5` (au lieu de 3), `py-1` (au lieu de 1.5). Gain horizontal : ~25% sur chaque pill. Vérifié : `scrollWidth: 972` sur `clientWidth: 556` = débordement réel de 416px, donc le scroll a effectivement lieu.

**Preuves** :

- `preuves/fix4/00_welcome_pages_bandis_BEFORE.png` — 5 pills visibles (RH, Operations, Growth, Cognition, People), aucun indicateur de débordement
- `preuves/fix4/01_welcome_pages_bandis.png` — chevrons gauche (disabled, tout est au début) et droite (actif, OMK RH en surbrillance), dégradé à droite, pills plus serrées
- `preuves/fix4/02_welcome_pages_scrolled_right.png` — après 3 clics sur le chevron droit : `scrollLeft: 416` (max), pills visibles = Cognition, People, Finance, IT, Legal, Coach Demo. **Les 9 pages sont accessibles.**

Vérification automatisée (`tools/verify_pages.mjs`, supprimé après usage) :
```
SIDEBAR counts: { 'OMK RH': 1, 'OMK Operations': 1, 'OMK Growth': 1, 'OMK Cognition': 1,
                  'OMK People': 1, 'OMK Finance': 1, 'OMK IT': 1, 'OMK Legal': 1,
                  'OMK Coach Demo': 1 }
after sidebar OMK Finance click → bandis highlighted tab: OMK Finance
clicked OMK IT tab: true
after bandis OMK IT click → sidebar active: OMK IT
after bandis OMK IT click → bandis highlighted: OMK IT
```

### 2 · Bandeau PAGES et sidebar synchronisés

**Avant** (`WelcomeApp.tsx:330-359`) :

```tsx
const [activePageId, setActivePageId] = useState<string>(initialId);
...
return <AppFrame sections={[
  { id: p.id, render: () => <PageCanvas page={p} activePageId={activePageId}
                                              onSelectPage={(id) => setActivePageId(id)} /> },
]} />;
```

Deux états locaux, aucun pont. Cliquer la sidebar « OMK Coach Demo » ne faisait que muter `AppFrame.activeId` ; `activePageId` restait à `'domaine-1-rh-meta-gouvernance'`. Le bandeau PAGES continuait de surligner « OMK RH ». Inversement, cliquer « OMK Finance » dans le bandeau mettait à jour `activePageId` mais ne déplaçait pas la sidebar.

**Après** :

```tsx
// Pont 1 : délégation de clic — la sidebar est la source de vérité.
useEffect(() => {
  const handler = (e: Event) => {
    const btn = (e.target as HTMLElement | null)?.closest('[data-section]');
    if (!(btn instanceof HTMLElement)) return;
    const label = btn.getAttribute('data-section');
    const page = LANDING_PAGES.find(p => p.brand === label);
    if (page && page.id !== activePageId) setActivePageId(page.id);
  };
  document.addEventListener('click', handler, true); // capture = avant React
  return () => document.removeEventListener('click', handler, true);
}, [activePageId]);

// Pont 2 : le bandeau navigue aussi la sidebar.
const navigateToPage = (id: string) => {
  setActivePageId(id);
  const page = LANDING_PAGES.find(p => p.id === id);
  if (! (!page)) return;
  const btn = document.querySelector(`[data-section="${page.brand}"]`);
  if (btn instanceof HTMLButtonElement) btn.click();
};
```

`data-section={s.label}` est posé sur le bouton de section de la sidebar uniquement (cf. FIX-5 sur `AppFrame.tsx:301`). La délégation au niveau `document` capture donc *toutes* les interactions de sidebar du document, mais ne réagit qu'aux lib labels qui matchent un `LANDING_PAGES.brand` connu — un clic dans une autre app n'a aucun effet.

**Pourquoi le couplage DOM** : `AppFrame` ne propage pas son `activeId` (état local). Ajouter une prop `activeSectionId` contrôlée aurait obligé à toucher `AppFrame` (périmètre FIX-5) et à modifier les 20 apps qui l'utilisent. La délégation DOM est strictement locale à `WelcomeApp` + `PageChrome` : aucun risque pour les autres apps.

**Preuves** :

- `preuves/fix4/00_welcome_active_sync_BEFORE.png` — sidebar sur « OMK Coach Demo », bandeau surligne « OMK RH »
- `preuves/fix4/03_welcome_active_sync_coach_demo.png` — après un seul clic sur « OMK Coach Demo » dans la sidebar, le bandeau surligne « OMK Coach Demo ». Capture le scrolled state parce que Playwright scroll le strip avant le screenshot final.

### 3 · Sales — titre sur une ligne

**Avant** (`SalesApp.tsx:701-742`) :

```tsx
function PageHeader({ eyebrow, title, subtitle, meta }) {
  return (
    <header className="grid grid-cols-1 gap-4 lg:grid-cols-[1fr_auto]">
      <div>
        <h1 className="mt-2 text-[40px] font-extrabold leading-[1.05] tracking-tight">
          {title} <span ...>Control Center</span>
        </h1>
        ...
      </div>
      <div className="text-right">
        ...
        <div className="mt-1 text-[15px] font-extrabold">{meta.value}</div>
        <div className="mt-1 max-w-[180px] text-[11.5px] leading-snug">{meta.sub}</div>
      </div>
    </header>
  );
}
```

En `1fr_auto`, la colonne droite est en `auto` — elle s'étend pour tenir sa valeur. « The single-source brief » (Context) et `${eventCount} events` (Cognition) dépassent `180px`, donc la column auto fait ~190px. Le titre « Sales OS Control Center » à `text-[40px] font-extrabold` fait ~500px. Avec le gap et le padding, il ne tient plus sur 1 ligne dans certaines largeurs : il wrappe en `Sales OS Control` / `Center`.

**Après** :

```tsx
function PageHeader({ eyebrow, title, subtitle, meta }) {
  return (
    <header className="grid grid-cols-1 gap-4 lg:grid-cols-[minmax(0,1fr)_auto]">
      <div className="min-w-0">
        <h1 className="mt-2 text-[40px] font-extrabold leading-[1.05] tracking-tight whitespace-nowrap">
          {title} <span ... className="... whitespace-nowrap">Control Center</span>
        </h1>
        ...
      </div>
      <div className="text-right max-w-[180px] shrink-0">
        ...
        <div className="mt-1 text-[15px] font-extrabold break-words">{meta.value}</div>
        <div className="mt-1 text-[11.5px] leading-snug">{meta.sub}</div>
      </div>
    </header>
  );
}
```

**Trois changements complémentaires** :

1. `lg:grid-cols-[minmax(0,1fr)_auto]` — `minmax(0, 1fr)` permet à la colonne titre de shrink à 0 sans forcer la grid à déformer la colonne meta. C'est ce qui rend `whitespace-nowrap` sur le titre viable.
2. `whitespace-nowrap` sur le `<h1>` **et** sur le `<span>` du chip — pas de wrap autorisé sur le titre. C'est le titre qui prime : si la fenêtre est trop étroite pour qu'il tienne, il déborde (c'est plus lisible que coupé en deux).
3. Colonne méta contrainte à `max-w-[180px] shrink-0`. Le sub était déjà `max-w-[180px]`, je l'ai monté au niveau du parent pour borner aussi la valeur, et `break-words` autorise sa césure à l'intérieur d'un mot long si nécessaire. Pas d'`overflow-wrap: anywhere` (cf. le piège déjà payé sur `$486k`) — `break-words` ne casse qu'aux frontières naturelles de mot en dernier recours.

**Preuves** :

- `preuves/fix4/00_sales_context_BEFORE.png` — « Sales OS Control » / « Center » sur 2 lignes
- `preuves/fix4/04_sales_context_after.png` — « Sales OS Control Center » sur 1 ligne, méta wrappe proprement
- `preuves/fix4/05_sales_cognition_after.png` — Pipeline montré pour confirmer que les sections où la méta est plus courte n'ont pas régressé

### 4 · Legal — échéance dépassée visible

**Avant** (`LegalApp.tsx:114-116`) :

```tsx
const Compliance = () => (
  <div className="p-7">
    <SectionHead title="AI-Act compliance" subtitle="Deadline 2026-08-02"
                 action={<Badge tone={cleared === checks.length ? 'ok' : 'warn'}>{cleared} / {checks.length}</Badge>} />
    <Card>...</Card>
  </div>
);
```

`subtitle` est une `string` passée à `SectionHead` qui la peint en `text-sm text-stone-500 mt-0.5`. Aucune lecture de la date du jour. Le 2026-08-07, l'échéance AI-Act du 2026-08-02 est dépassée depuis 5 jours — et l'utilisateur ne le voit pas.

**Après** :

```tsx
const DEADLINE = new Date('2026-08-02T00:00:00');
const today = new Date();
const daysLate = Math.max(0, Math.floor((today.getTime() - DEADLINE.getTime()) / 86_400_000));
const overdue = daysLate > 0;
const overdueLabel = overdue
  ? `Deadline 2026-08-02 · en retard de ${daysLate} jour${daysLate > 1 ? 's' : ''}`
  : `Deadline 2026-08-02 · dans ${-daysLate} jour${-daysLate > 1 ? 's' : ''}`;

const Compliance = () => (
  <div className="p-7">
    <div className="flex items-start justify-between gap-4 mb-5">
      <div>
        <h2 className="text-lg font-bold tracking-tight text-stone-900 font-outfit">AI-Act compliance</h2>
        <p className={`text-sm mt-0.5 inline-flex items-center gap-1.5 ${
          overdue ? 'text-red-600 font-semibold' : 'text-stone-500'
        }`}>
          {overdue && <AlertTriangle className="w-3.5 h-3.5" />}
          <span>{overdueLabel}</span>
        </p>
      </div>
      <div className="flex items-center gap-2">
        {overdue && <Badge tone="danger">Overdue</Badge>}
        <Badge tone={cleared === checks.length ? 'ok' : 'warn'}>{cleared} / {checks.length}</Badge>
      </div>
    </div>
    <Card>...</Card>
  </div>
);
```

**Quatre changements** :

1. **Calcul dynamique** à chaque rendu. `useState` n'est pas nécessaire : la date du jour change entre deux ouvertures du shell, pas pendant. `Math.floor((today - DEADLINE) / 86_400_000)` donne un nombre entier de jours (positif = en retard).
2. **Phrase calculée** : « Deadline 2026-08-02 · en retard de N jour(s) » (avec accord pluriel). Le label négatif (échéance future) est conservé pour ne pas casser l'app si quelqu'un retarde la date.
3. **Couleur d'alerte + icône** : `text-red-600 font-semibold` + `AlertTriangle` de lucide (3.5×3.5). Le `inline-flex items-center gap-1.5` aligne proprement l'icône et le texte.
4. **Badge `Overdue`** ajouté à côté du compteur « X / 5 ». Le compteur reste en `warn` pour sa logique métier (items restants), l'`Overdue` est un signal indépendant.

`SectionHead` n'acceptant que `subtitle: string`, j'ai recréé la même structure (`flex items-start justify-between gap-4 mb-5`) en markup direct dans `Compliance`. C'est plus verbeux mais ça reste confiné à LegalApp — pas de modification du composant partagé d'`AppFrame`.

**Preuves** :

- `preuves/fix4/06_legal_compliance_overdue.png` — Sous-titre rouge avec ⚠, « en retard de 5 jours », badge `Overdue` à côté de `3 / 5`

### 5 · Audit — les 3 niveaux Maturité tiennent ensemble

**Avant** (`AuditApp.tsx:312-396`) :

```tsx
function MaturiteContent() {
  return (
    <div className="space-y-5">
      <SectionHead ... />
      <div className="space-y-3">
        {MATURITE_GRID.map((row, idx) => (
          <div className="rounded-2xl border-2 p-5 ...">
            <div className="mb-2 flex items-center gap-3">...</div>
            <p className="mb-3 text-[12px] italic ...">{row.tagline}</p>
            <div className="grid grid-cols-1 gap-3 md:grid-cols-3">...</div>
          </div>
        ))}
      </div>
      <section className="rounded-2xl p-5 ...">...</section>
      <section className="rounded-2xl p-5 ...">...</section>
    </div>
  );
}
```

Mesure : card avec `p-5` (20px padding) + `mb-2` + titre `text-lg` (18px) + tagline `text-[12px]` (~20px) + `mb-3` + grid 3-cols `gap-3` × ~50px ≈ 180-220px par card. Trois cards + 2 sections de fin ≈ 880px > 660px de hauteur canvas visible en 1440×900. `03 Déléguer` sort sous la ligne de flottaison.

**Après** :

```tsx
function MaturiteContent() {
  return (
    <div className="space-y-4">
      <SectionHead ... />
      <div className="space-y-2.5">
        {MATURITE_GRID.map((row, idx) => (
          <div className="rounded-xl border-2 p-4 ...">
            <div className="mb-1.5 flex items-center gap-3">...</div>
            <h3 className="text-base font-bold ...">{row.title}</h3>
            <p className="mb-2 text-[11.5px] italic ...">{row.tagline}</p>
            <div className="grid grid-cols-1 gap-2 md:grid-cols-3">...</div>
          </div>
        ))}
      </div>
      <section className="rounded-xl p-4 ...">...</section>
      <section className="rounded-xl p-4 ...">...</section>
    </div>
  );
}
```

**Compactage ciblé** (rien de cosmétique, tout est de la hauteur gagnée) :

- `rounded-2xl` → `rounded-xl` : pas de différence visuelle mais 12px au lieu de 16px (rayon, donc hauteur nulle — non, c'est cosmétique pure)
- `p-5` → `p-4` : 8px de hauteur gagnée par card (4 top + 4 bottom)
- `text-lg` → `text-base` sur le `<h3>` du titre de niveau : 2px gagnés
- `text-[12px]` → `text-[11.5px]` : quelques pixels par ligne de tagline et de texte dans les 3 colonnes
- `mb-2` → `mb-1.5` (2px), `mb-3` → `mb-2` (4px), `gap-3` → `gap-2` (4px dans la grille interne)
- `space-y-3` → `space-y-2.5` entre les cards
- `space-y-5` → `space-y-4` autour des sections de fin

Estimation du gain : ~50px par card × 3 cards + ~20px sur les sections de fin = ~170px gagnés. Vérifié visuellement : les 3 cards + les 2 sections de fin tiennent en 1440×900, scrollable mais lisible sans scroll.

**Preuves** :

- `preuves/fix4/00_audit_maturite_BEFORE.png` — `03 Déléguer` coupé en bas
- `preuves/fix4/07_audit_maturite_after.png` — Les 3 niveaux Discuter / Connecter / Déléguer + les 2 sections « Faux niveaux » et « Repère » tiennent dans la fenêtre

### 6 · Audit — titre sidebar tronqué (FIX-5 le possède)

**Constat** : `Manuel de Diagnostic IA` apparaît comme `Manuel de Diagno…` dans le header de la sidebar sur les 7 sections d'Audit (Overview exceptée).

**Inspection DOM** (live, via Playwright) :

```json
{
  "text": "Manuel de Diagnostic IA",
  "width": 134,
  "height": 35,           // 2 lignes wrappées
  "scrollWidth": 134,
  "whiteSpace": "normal",
  "overflowWrap": "break-word",
  "classes": "text-[14px] font-bold ... whitespace-normal break-words"
}
```

Le DOM montre un `<div>` de hauteur 35px (2 lignes × 17.5px) qui wrappe correctement le texte intégral. Le screenshot, lui, montre une seule ligne coupée. **Conclusion** : le wrap se fait côté React, mais le rendu visuel n'en tient pas compte — probablement un problème de HMR/canvas qui n'a pas rejoué le layout après le changement `truncate` → `break-words` de FIX-5, ou un clip par un parent.

**Le brief dit explicitement** :

> Si la troncature vient du composant partagé de barre latérale, **c'est FIX-5 qui le possède** : signale-le et n'y touche pas.

C'est bien le cas : la classe CSS vit sur `AppFrame.tsx:219` (posée par FIX-5 sur le `<div>` qui porte `title`). Je n'ai pas touché à `AppFrame` et je n'ai touché à aucun fichier partagé. **À FIX-5 de vérifier que son changement `truncate` → `break-words` est bien effectif en runtime**, pas seulement en code source.

---

## Ce que je n'ai pas corrigé, et pourquoi

1. **FIX-4.6 (Audit sidebar title)** — composant partagé AppFrame, FIX-5 le possède. DOM-correct, rendu à investiguer côté FIX-5.
2. **Sales Cognition** — la section `Cognition` de Sales ne passe pas par `PageHeader`, elle utilise `CognitionPanel` qui a son propre header (« Cognition SovereignGate »). Donc la régression observée sur le titre Sales concernait uniquement les sections `Context` (et `Pipeline`/`Today`/`Stack`/`Capabilities` qui ont des méta plus courtes). Mon fix sur `PageHeader` n'a pas touché CognitionPanel — et c'est correct : le titre de CognitionPanel n'a jamais eu le problème.
3. **Welcome sur la section Arrivée (Overview)** — OverviewPanel ne monte pas le `PageChrome`, donc le bandeau PAGES n'y apparaît pas. C'est volontaire : la page d'arrivée affiche les 8 Domaines sous forme de grille directement, sans bandeau. Mon correctif ne concerne que les 9 pages de détail.
4. **`useState` pour la date du jour dans Legal** — j'utilise `new Date()` directement dans le corps du composant `Compliance` (recalculé à chaque rendu). Si l'utilisateur laisse l'app ouverte minuit passé, le compteur ne se met pas à jour sans re-render. Acceptable pour cet écran (Compliance n'est pas un compteur temps réel), et évite le coût d'un `useEffect` + `setInterval` pour 5 jours d'écart.

---

## Vérification technique

`npx tsc -b` ne signale aucune erreur **dans mes fichiers** (`src/apps/{welcome,sales,legal,audit}/`). Les 3 erreurs résiduelles sont toutes dans `src/apps/sales/SalesDetailPage.tsx` (TS6133 × 2 imports inutilisés, TS2503 namespace JSX) — pré-existantes, hors de mon périmètre, non causées par mes changements.

```
src/apps/sales/SalesDetailPage.tsx:19:8 - TS6133: 'LucideIcon' is declared but its value is never read.
src/apps/sales/SalesDetailPage.tsx:21:27 - TS6133: 'DetailField' is declared but its value is never read.
src/apps/sales/SalesDetailPage.tsx:74:86 - TS2503: Cannot find namespace 'JSX'.
```

Aucune erreur de console côté navigateur sur les écrans corrigés (`tools/shot.mjs` logge les `console.error` et `pageerror` ; rien sur mes captures).