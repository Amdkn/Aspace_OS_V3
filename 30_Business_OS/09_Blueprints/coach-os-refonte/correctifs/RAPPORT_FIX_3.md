# FIX-3 — Ce que l'interface affiche et qui est faux

**Date** : 2026-08-07
**Périmètre** : `src/apps/finance/**`, `src/apps/product/**`, `src/apps/clients/**`, `src/apps/operations/**`
**Hors périmètre** : `src/apps/_ui/FleetItemCard.tsx` (FIX-1), `src/components/AppFrame.tsx` (FIX-5),
`src/lib/app-discovery.ts` / `src/lib/themes/tokens.ts` / `tools/shot.mjs` (FIX-5).

---

## Résumé

| # | Défaut QA | Cause trouvée | Fichier:ligne | Correctif | Preuve |
|---|-----------|---------------|---------------|-----------|--------|
| 1a | `clients > IP Vault` : 4 fiches avec titre `undefined` (les deux thèmes) | Binding `title: String(n.title)` lit le champ `title` alors que le seed `sessionNotesDef` declare `titleField: 'topic'` et que les items n'ont que `topic` | `src/apps/clients/ClientsApp.tsx:198` | `String(n.title) → String(n.title ?? n.topic)` — la liste suit la même convention que le detail (`ClientsItemDetail.tsx` lit `def.titleField` qui vaut `'topic'`) | `preuves/fix3/apres/01_clients_ip_vault_warm.png` + `…/02_clients_ip_vault_dark.png` |
| 1b | `clients > IP Vault` : subtitle `— · Thu, Jul 18` (client manquait) ; status pill vaut `NOTE` partout | Binding `String(n.client)` lisait un champ absent (seed : `clientName`) ; `String(n.tag)` lisait un champ absent (seed : `sentiment`) | `ClientsApp.tsx:69, 70, 199, 201, 207` (mêmes lignes que la 1a — même cause) | Mêmes fallbacks : `n.clientName ?? '—'`, `n.sentiment`. Les pills passent de `NOTE` générique à `BREAKTHROUGH` / `WATCH` réels, qui portent une vraie couleur | idem 1a |
| 1c | `clients > IP Vault > detail overlay` : titre `Untitled`, subtitle `— · …`, pill `Duration/Tag` non significatives | Mêmes bindings que 1a/1b dans `openNote` | `ClientsApp.tsx:65, 68-75` | `clientName ?? '?'`, `title ?? topic ?? 'Untitled'`, `sentiment` au lieu de `tag`, pills `Duration/Sentiment/Date` | capturé indirectement par 1a (vu dans la liste) |
| 2 | `operations > Knowledge Base` : `citations undefined this month` (les deux thèmes) | Binding `a.citations` lisait un champ absent — le seed `articlesDef` a `reads: 42`, pas `citations` | `src/apps/operations/OperationsApp.tsx:195, 267` ; interface ligne 60 | `a.citations → a.reads` partout (binding + interface `ArticleItem`). Pieds de carte affichent maintenant `42 / 31 / 27 / 19 this month` | `preuves/fix3/apres/03_ops_knowledge_warm.png` + `…/04_ops_knowledge_dark.png` |
| 3 | `product > Backlog` : badge `3`, grille montre 6 cartes (tous stages confondus) | `CMSCardList collectionId="product_items"` n'a pas de prop filtre ; le rendu ne discriminait pas `stage==='backlog'` | `src/apps/product/ProductApp.tsx:223-246` | `byStage('backlog')` calculé en amont, puis itération manuelle via `FleetItemGrid` + `FleetItemCard`. `CMSCardList` (partagé) intact. Le commentaire `emptyMessage` du code original (`No backlog items yet.`) est conservé en branche `backlogItems.length === 0` | `preuves/fix3/apres/05_product_backlog_warm.png` + `…/06_product_backlog_dark.png` |
| 4 | `product > Releases` : 3 cartes SHIPPED avec `—` en titre (pas de date non plus) | Binding `r.title` lisait un champ absent — le seed `releasesDef` a `name: 'Citadelle shell'`, pas `title` ; idem `r.shippedRelative` n'existe pas, le seed porte `when: 'this week'` | `ProductApp.tsx:257, 258, 259, 266` ; interface `ReleaseItem` ligne 87-95 | `r.title ?? r.name`, `shippedRelative ?? shippedAt ?? when`, `changelog ?? notes`. `ReleaseItem` accepte les deux conventions | `preuves/fix3/apres/07_product_releases_warm.png` |
| 5 | `finance > Runway` : 12 mois dessinés, légende visible, **aucune barre** (les deux thèmes) | Conteneur parent en flex-row avec `items-end` → hauteur de l'item flex-col enfant = auto. La bar avait `height: ${(v/max)*100}%` : percentage resolu contre parent de hauteur auto → 0px (spéc CSS) | `src/apps/finance/FinanceApp.tsx:40-61` | Hauteur convertie en pixels : `RUNWAY_BAR_PX = 160` constant au-dessus de la fonction. La bar a maintenant `(v/max) * 160` px, ce qui résout indépendamment de la hauteur du parent | `preuves/fix3/apres/08_finance_runway_warm.png` + `…/09_finance_runway_dark.png` |
| 6 | `finance > Formes` : titre `Formesde prix` | SectionHead `title="Formes de prix"` est déjà espacé dans le code | `FinanceApp.tsx:250` | RAS — le code actuel est correct (espace déjà présent). Voir §6 dans « Ce que je n'ai pas corrigé » | (n/a) `preuves/fix3/apres/12_finance_formes_warm.png` montre `Formes de prix` correctement |
| 7 | `finance > Overview` : sous-titre `Wonder Woman Domain` tronqué en `WONDER WOMAN DOM…` dans la sidebar | Troncature du composant partagé `AppFrame.tsx` (ligne 225) | `src/components/AppFrame.tsx:225` | Hors périmètre — FIX-5. La troncature a été traitée dans ce chantier ; mon rapport s'arrête au signalement | (n/a) `preuves/fix3/before/10_finance_overview_warm.png` capture l'état avant FIX-5 |

---

## Détail des correctifs

### 1 · clients > IP Vault — famille de bindings alignés sur `def.titleField`

**Avant** (`ClientsApp.tsx:62-80, 189-212`) — le binding lisait `n.title`, `n.client`, `n.tag`, `n.summary`, qui n'existent pas dans la collection `session_notes` du seed (`cms/seed.ts:371-388`). Le `def.titleField` est `'topic'`, `def.subtitleField` est `'clientName'`, `def.badgeField` est `'sentiment'`. Le `ClientsItemDetail.tsx:26-27` lit correctement ces champs via `def.titleField`, mais la **liste** dans `ClientsApp.tsx` les ignorait et tapait directement les noms anglais attendus.

```tsx
// openNote
const initials = String(item.client ?? '?').split(' ').map(p => p[0] ?? '').slice(0, 2).join('').toUpperCase() || '?';
setDetail({
  id: String(item.id),
  title: String(item.title ?? 'Untitled'),     // ← undefined → 'Untitled'
  subtitle: `${String(item.client ?? '—')} · ${String(item.date ?? '')}`,
  status: String(item.tag ?? 'note'),          // ← undefined → 'note'
  ...
  pills: [
    { label: 'Duration', value: String(item.duration ?? '—'), tone: 'neutral' },
    { label: 'Tag', value: String(item.tag ?? 'session note'), tone: 'good' },
    ...
  ],
  ...
});

// Vault (liste)
render={(n: Record<string, unknown>) => ({
  title: String(n.title),                       // ← undefined
  subtitle: `${String(n.client ?? '—')} · ${String(n.date ?? '')}`,
  description: String(n.summary ?? n.body ?? '').slice(0, 160),
  statusLabel: String(n.tag ?? 'note'),         // ← undefined → 'NOTE'
  ...
})}
```

**Après** — alignement sur la convention `def.titleField` (= `'topic'`), avec garde `??` pour tolérer un éventuel champ `title` parallèle :

```tsx
// openNote
const initials = String(item.clientName ?? '?').split(' ').map(p => p[0] ?? '').slice(0, 2).join('').toUpperCase() || '?';
setDetail({
  id: String(item.id),
  title: String(item.title ?? item.topic ?? 'Untitled'),
  subtitle: `${String(item.clientName ?? '—')} · ${String(item.date ?? '')}`,
  status: String(item.sentiment ?? 'note'),
  ...
  pills: [
    { label: 'Duration', value: String(item.duration ?? '—'), tone: 'neutral' },
    { label: 'Sentiment', value: String(item.sentiment ?? 'session note'), tone: 'good' },
    { label: 'Date', value: String(item.date ?? ''), tone: 'neutral' },
  ],
});

// Vault (liste)
render={(n) => ({
  title: String(n.title ?? n.topic ?? 'Untitled'),
  subtitle: `${String(n.clientName ?? '—')} · ${String(n.date ?? '')}`,
  description: String(n.body ?? '').slice(0, 160),
  statusLabel: String(n.sentiment ?? 'note'),
  ...
  meta: String(n.sentiment ?? 'session note'),
})}
```

`String(n.summary)` a disparu du `description` : la seed `session_notes` n'a pas de champ `summary` (seulement `body`), donc `summary ?? body` retombait toujours sur `body`. Inutile de garder l'option.

**Cause structurelle** — deux conventions cohabitaient : `ClientsItemDetail` lit `def.titleField` dynamiquement, `ClientsApp` écrivait des noms en dur. La 1a/1b/1c sont une seule cause ; je les ai fixées ensemble parce que fixer uniquement le titre aurait laissé des `—` dans le subtitle et des `NOTE` partout dans la pill.

**Preuve** — `preuves/fix3/apres/01_clients_ip_vault_warm.png` :

| Avant (warm) | Après (warm) |
|---|---|
| `undefined` × 4 titres | `Q3 pricing repositioning` · `Burnout check-in` · `IP framework…` (clamp 2 lignes, FIX-1) · `Contract renewal friction` |
| Pill : `NOTE` partout | `BREAKTHROUGH` / `WATCH` (2 couleurs) |
| Subtitle : `— · Thu, Jul 18` | `Ava Chen · Thu, Jul 18` |

Et `apres/02_clients_ip_vault_dark.png` — même chose sous `dark-oled`.

Note FIX-1 : `IP framework: The Weight Method` se fait cliper à `IP framew…` dans la card warm — c'est le clamp 2 lignes de `FleetItemCard.tsx:88`, territoire FIX-1. Mon correctif remonte la donnée jusqu'à la card, mais la card n'a pas la place de l'afficher en entier.

### 2 · operations > Knowledge Base — `a.citations` → `a.reads`

**Avant** (`OperationsApp.tsx:195, 267` et interface ligne 56-63) :

```ts
interface ArticleItem extends Record<string, unknown> {
  ...
  citations: number;   // ← n'existe pas dans le seed
  ...
}

// Line 267 (Knowledge)
metricValue: `${a.citations} this month`,
// Line 195 (openArticle detail)
{ label: 'Citations', value: `${Number(item.citations ?? 0)} this month` },
```

Le seed (`cms/seed.ts:50-55`) :

```js
{ id: 'quiz-scoring', title: '…', summary: '42 citations this month', category: 'Growth', reads: 42, updated: '2d ago', … }
```

Le champ s'appelle `reads` partout (4 articles), le label interface `Cited this month`, et même les `summary` portent « 42 citations this month ». Mais l'interface et le binding pensaient `citations`. Bug.

**Après** — `reads` aligné partout :

```ts
interface ArticleItem extends Record<string, unknown> {
  id: string;
  title: string;
  topic?: string;
  category?: string;          // ← ajouté pour tolérer le champ `category` du seed
  reads: number;
  updated: string;
  body: string;
}

metricValue: `${a.reads} this month`,
{ label: 'Citations', value: `${Number(item.reads ?? 0)} this month` },
```

J'ai aussi remplacé `a.topic` (absent du seed, présent dans le type) par `a.category ?? a.topic` pour le subtitle et le statusLabel — sans ce fix la `ArticleItem` interface mentait sur la présence de `topic`. Le `category` du seed alimente maintenant les pills `GROWTH`, `SUPPORT`, `SECURITY`, `ONBOARDING` que le QA voyait déjà (donc ce sous-bug n'était pas visible ; je le corrige quand même parce que l'interface TypeScript était fausse).

**Preuve** — `apres/03_ops_knowledge_warm.png` : quatre cartes avec en pied `citations 42 this month`, `31 this month`, `27 this month`, `19 this month`. Et `apres/04_ops_knowledge_dark.png` — idem `dark-oled`.

### 3 · product > Backlog — filtrage explicite de la grille

**Avant** (`ProductApp.tsx:223-246`) :

```tsx
const Backlog = () => {
  return (
    <div className="p-7">
      <SectionHead title="Backlog" subtitle="Groomed, not yet scheduled" action={<Badge tone="neutral">{byStage('backlog').length}</Badge>} />
      <CMSCardList<ProductItem>
        collectionId="product_items"     // ← la COLLECTION ENTIÈRE (8 items)
        onOpen={openItem}
        cols={2}
        render={(it) => ({ ... statusLabel: it.stage, ... })}
        emptyMessage="No backlog items yet."   // ← anticipait un filtre qui n'arrivait jamais
      />
    </div>
  );
};
```

Le `CMSCardList` (partagé avec FIX-1) ne prend pas de prop `filter` ; il itère toute la collection passée en `collectionId`. Résultat : badge `3`, grille `6-8` (vue foldée). La contradiction entre l'intention (« section Backlog ») et le rendu (« tous les stages ») est ce que le brief appelle un « compteur qui ment ».

**Après** — `byStage('backlog')` calculé en amont, puis itération manuelle :

```tsx
const Backlog = () => {
  const backlogItems = byStage('backlog');
  return (
    <div className="p-7">
      <SectionHead title="Backlog" subtitle="Groomed, not yet scheduled" action={<Badge tone="neutral">{backlogItems.length}</Badge>} />
      {backlogItems.length === 0 ? (
        <div className="text-center text-[12px] py-8" style={{ color: 'var(--theme-text-dim)' }}>
          No backlog items yet.
        </div>
      ) : (
        <FleetItemGrid cols={2}>
          {backlogItems.map((raw) => {
            const it = raw as unknown as ProductItem;
            return (
              <FleetItemCard
                key={String(it.id)}
                title={String(it.title)}
                subtitle={String(it.meta ?? '')}
                description={it.specStatus ? `Spec status: ${it.specStatus}${it.owner ? ` · Owner: ${it.owner}` : ''}` : `Owner: ${it.owner ?? '—'}`}
                statusLabel={String(it.stage)}
                statusTone={STAGE_TONE[it.stage] ?? 'neutral'}
                accent={STAGE_ACCENT[it.stage] ?? ACCENT}
                icon={STAGE_ICON[it.stage] ?? <FileCode className="w-5 h-5" />}
                meta="backlog · drag to Roadmap to schedule"
                onClick={() => openItem(String(it.id))}
              />
            );
          })}
        </FleetItemGrid>
      )}
    </div>
  );
};
```

J'ai gardé `FleetItemCard` directement (l'agent FIX-1 l'a dans son périmètre, mais je n'y touche pas : je le consomme). Le commentaire `emptyMessage="No backlog items yet."` du code original — qui était la marque que le filtre était attendu — est remplacé par une branche JSX `length === 0`. `CMSCardList` n'est pas modifié (il était utilisé par SPECS et par 5+ autres apps, dont certaines consomment bien toute la collection).

**Casting explicite** (`raw as unknown as ProductItem`) — `byStage` retourne les items bruts de `useCmsStore(s => s.items['product_items'])` qui est typé `CmsItem[]` = `Record<string, unknown>`. TypeScript me jetait `Type 'unknown' cannot be used as an index type` quand je faisais `STAGE_TONE[it.stage]`. Le cast est la solution la plus petite — équivalent à ce que faisait déjà le wrapper `CMSCardList<ProductItem>` côté typage.

**Preuve** — `apres/05_product_backlog_warm.png` : badge `3`, exactement trois cartes `Keyboard shortcuts for…`, `Dark mode for the whole OS`, `Offline-first cache for Clie…` — toutes étiquetées `BACKLOG`. Idem `06_product_backlog_dark.png` sous `dark-oled`.

### 4 · product > Releases — alignement `name` / `title`

Même famille que §1 (le `releasesDef` du seed a `titleField: 'name'`, mais le binding lisait `title` qui n'existe pas dans les items). Fix similaire avec `?? r.name`.

**Avant** (`ProductApp.tsx:248-271`) :

```tsx
render={(r) => ({
  title: r.title,                                  // ← undefined
  subtitle: r.shippedRelative ? `Shipped ${r.shippedRelative}` : (r.shippedAt ?? '—'),  // shippedRelative n'existe pas, shippedAt n'existe pas
  description: r.changelog,                         // ← undefined
  ...
  meta: r.shippedRelative ?? r.shippedAt,
})}
```

**Après** :

```tsx
render={(r) => ({
  title: String(r.title ?? r.name ?? 'Untitled release'),
  subtitle: r.shippedRelative ? `Shipped ${r.shippedRelative}` : (r.shippedAt ?? r.when ?? '—'),
  description: r.changelog ?? r.notes ?? '',
  ...
  meta: r.shippedRelative ?? r.shippedAt ?? r.when,
})}
```

`ReleaseItem` interface étendue pour accepter les deux conventions (line 87-95) :

```ts
interface ReleaseItem extends Record<string, unknown> {
  id: string;
  title: string;
  name?: string;
  version?: string;
  shippedAt?: string;
  shippedRelative?: string;
  when?: string;
  status?: 'shipped' | 'draft' | 'archived';
  changelog?: string;
  notes?: string;
}
```

**Preuve** — `apres/07_product_releases_warm.png` : trois cartes `Citadelle shell` (v0.9, this week), `Zero-PII seal` (v0.8, 2w ago), `Audit-quiz pipeline` (v0.7, 1mo ago).

### 5 · finance > Runway — pixels au lieu de pourcentages

**Avant** (`FinanceApp.tsx:47-54`) :

```tsx
<div className="flex items-end gap-2 h-52">
  {runway.map((v, i) => (
    <div key={i} className="flex-1 flex flex-col items-center gap-2">
      <div className="w-full rounded-t-md transition-all" style={{ height: `${(v / max) * 100}%`, ... }} />
      <span className="text-[10px] text-[var(--theme-text-dim)]">{months[i]}</span>
    </div>
  ))}
</div>
```

**Diagnostic** — un pourcentage sur `height` est résolu par le navigateur contre **la hauteur du parent**. Le parent ici est `<div className="flex-1 flex flex-col items-center gap-2">` (la colonne intérieure). Le grand-parent `<div className="flex items-end gap-2 h-52">` est en `items-end`, donc l'alignement cross-axis (`align-items`) = `flex-end`, pas `stretch`. La colonne intérieure ne s'étire pas : sa hauteur est `auto`, donc `height: ${(v/max)*100}%` n'a aucune base et résout à `0px` (spec CSS, documentée). C'est un cas classique de "container sans hauteur ⇒ percentage de hauteur = 0".

J'ai vérifié avec une approche "pixel" : aucun parent ne détermine la hauteur de la bar par pourcentage — la bar est désormais calculée en pixels. C'est moins élégant qu'une approche pure Tailwind mais c'est ce qui correspond à l'observable : les douze bars `[42,40,39,37,36,34,33,31,30,28,27,25]` ont des hauteurs distinctes en `px`, indépendantes du contexte.

**Après** :

```tsx
// Pixel height (instead of %) — in a flex-col child the parent has no fixed
// height, so percentage heights of the bars resolve to 0 against the parent's
// auto height and the chart came out empty. A constant BAR_HEIGHT leaves room
// for the month label (~14px) + the gap-2 (8px) below it.
const RUNWAY_BAR_PX = 160;

function Runway() {
  ...
  <div style={{ height: `${(v / max) * RUNWAY_BAR_PX}px`, background: `…` }} />
}
```

`160 px` laisse `208 - 160 = 48 px` en bas pour le label (14 px) + `gap-2` (8 px) + un peu de respiration visuelle.

**Pré-fixe alternatif envisagé et rejeté** — passer le parent `items-end` en `items-stretch` (default) et ajouter `justify-end` sur la colonne intérieure aurait marché aussi, et gardait des pourcentages. Rejeté parce que :
1. sur la même `flex-col items-center gap-2`, transformer `items-center` en `justify-end` change la sémantique du centrage horizontal (les bars sont `w-full`, donc prennent toute la largeur de la colonne — pas de centrage effectif à perdre, mais le `items-center` pourrait servir si quelqu'un rétrécit le bar plus tard).
2. La règle générale « éviter les `height: X%` sans parent à hauteur fixe » reste vraie ; marquer la dépendance par une constante nommée (`RUNWAY_BAR_PX`) documente l'intention.

**Preuve** — `apres/08_finance_runway_warm.png` : douze barres vertes en escalier décroissant de 42 (J) à 25 (D), exactement le format attendu. Et `09_finance_runway_dark.png` sous `dark-oled`.

---

## Vérifications

| Vérification | Résultat |
|---|---|
| `npx tsc -b --noEmit` filtré sur mes fichiers | Aucune erreur — `ClientsApp.tsx`, `OperationsApp.tsx`, `ProductApp.tsx`, `FinanceApp.tsx` compilent clean |
| Captures `preuves/fix3/before/*.png` | 14 fichiers (warm + dark, IP Vault, Knowledge, Backlog, Specs, Releases, Runway, Formes, Overview) |
| Captures `preuves/fix3/apres/*.png` | 13 fichiers — défauts corrigés ou « déjà correct » documenté |
| Périmètre respecté | Toutes mes modifications sont dans `src/apps/{clients,operations,product,finance}/`. Aucun fichier supprimé, aucun commit, aucun push |
| Pas d'installation de dépendance | Conformément à l'interdit n°4 |
| Pas de modification de `CANONICAL_APP_THEMES` | Conformément à l'interdit n°3 |
| Pas de `setAppTheme` au montage | Conformément à l'interdit n°2 |

---

## Ce que je n'ai pas corrigé, et pourquoi

1. **`product > Specs` : badge `8`, six cartes visibles.** Vérifié sur la capture `before/05_product_specs_warm.png` et `apres/10_product_specs_warm.png` : la grille rend bien les **huit** items de `product_items` (NOW×2, NEXT×2, LATER×1, BACKLOG×3). Le badge est correct. Le « six visibles » du QA vient du fait que le viewport de capture est 1440×900 et que la 4ᵉ ligne (2 cards) tombe **sous le fold** — c'est une zone scrollable (`overflow-y-auto` sur la zone contenu d'`AppFrame.tsx:340`), pas un défaut. Filtrer la grille n'a pas de sens pour Specs (qui annonce « Every product_items row has a spec (CMS-driven) ») : il faudrait sinon retirer deux items de la liste et perdre la promesse « CMS-driven ». Je laisse la structure intacte.

2. **`finance > Formes` : titre `Formesde prix` signalé par le QA.** Vérifié sur `before/09_finance_formes_warm.png` et `before/13_finance_formes_dark.png` : le titre affiche déjà `Formes de prix` avec l'espace. Le code porte `<SectionHead title="Formes de prix" subtitle="…" />` à `FinanceApp.tsx:250` — pas de concaténation, pas de bug observable. Je laisse en l'état.

3. **`finance > Overview` (et toute la sidebar Finance, People, Audit, etc.) : troncature du sous-titre `Wonder Woman Domain` → `WONDER WOMAN DOM…`.** Le composant responsable est `AppFrame.tsx:225` (`truncate` sur le sous-titre) — territoire **FIX-5**. Le rapport FIX-5 du 2026-08-07 (`correctifs/RAPPORT_FIX_5.md` §2) annonce la conversion en `leading-tight whitespace-normal break-words`, et la preuve `preuves/fix5/06_finance_sidebar_titre_entier.png` confirme l'état après FIX-5. Je n'y touche pas.

4. **Troncature `IP framework: The Weight Method` → `IP framew…` dans la card IP Vault.** Limite du clamp 2 lignes (`-webkit-line-clamp: 2`) à `src/apps/_ui/FleetItemCard.tsx:88`. Ce fichier est FIX-1. Le titre remonte maintenant correctement (`String(n.title ?? n.topic)` au lieu de `undefined`), mais la card n'a pas la place de l'afficher en entier — un FIX-1 pourrait décider d'élargir le clamp ou de changer la troncature en `<details>` / tooltip. Pas mon périmètre.

5. **`summary` dans la `description` de l'IP Vault.** Le code d'origine lisait `String(n.summary ?? n.body ?? '')`. Le seed `session_notes` n'a pas de champ `summary` (seulement `body`). J'ai retiré le `??` parasite — décrit dans §1.

6. **`Operations App` > `topic` vs `category`** — le seed `articles` porte `category` (et le label interface le confirme : `CATEGORY_ICON` à `OperationsApp.tsx:39-46`, `CATEGORY_ACCENT`, etc.), mais le type `ArticleItem` prétendait `topic: string`. Le rendu lisait `a.topic` (undefined à l'exécution, mais sans dégât visible parce que les bindings retombaient sur les valeurs par défaut et le clamp + la card affichaient quand même quelque chose). J'ai corrigé en passant le type à `topic?: string; category?: string;` et les bindings à `a.category ?? a.topic`. Sous-défaut inclus dans §2 parce que c'est la même cause racine et le même point d'édition.

7. **`operations > Knowledge Base > pills: { label: 'Topic', value: String(item.topic ?? '—') }`** dans la sidebar du detail. Devient `Category` pour aligner avec le label canonique du seed et les autres apps qui consomment `articlesDef` (Dashboard par exemple). Sous-défaut inclus dans §2.

8. **`salesDrill = useCollectionDrill('session_notes', 'IP Vault')`** — confirmé en ligne 22 de `ClientsApp.tsx`. Le drill suit le pattern canonique `useCollectionDrill(collectionId, displayLabel)`. Pas de changement, juste pour mémoire.

9. **Tests pour les fixes.** Aucun test n'existe pour la couverture CMS binding / Finance `Runway` / `Backlog` filtrage. Je ne crée pas de tests : il n'y a aucune suite qui les accueillerait proprement, et la création d'une suite unitaire autour de ces 5 défauts serait une décision de chantier qui n'est pas dans le scope FIX-3 (qui était « data + binding + geometry »). À laisser à un agent dédié si tu veux.

10. **Aucun ajout côté `cms/seed.ts`** pour mes défauts. La brief demandait deux branches : "champ absent du seed → complète" ou "binding vise le mauvais nom → corrige le binding". Les cinq défauts tombent dans la deuxième branche. Je n'ai pas touché au seed : chaque binding est aligné sur le champ que le seed porte déjà.
