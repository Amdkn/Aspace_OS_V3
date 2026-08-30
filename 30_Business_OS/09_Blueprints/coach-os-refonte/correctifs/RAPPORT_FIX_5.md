# FIX-5 — La coquille et l'instrument de mesure

**Date** : 2026-08-07
**Périmètre** : `tools/shot.mjs`, `src/components/**`, `src/lib/app-discovery.ts`, `src/lib/themes/tokens.ts`
**Hors périmètre** : `src/apps/**`, `src/stores/shell.store.ts`

---

## Résumé

| # | Défaut QA | Cause trouvée | Fichier:ligne | Correctif | Preuve |
|---|-----------|---------------|---------------|-----------|--------|
| 1 | `shot.mjs` cliquait la mauvaise cible | `data-section` jamais posé + repli textuel qui matchait le fil d'Ariane ou le rail | `AppFrame.tsx:300` / `shot.mjs:101` | `data-section={s.label}` posé sur les boutons de sidebar uniquement ; sélecteur strict sans repli ; échec bruyant avec exit code 4 | `preuves/fix5/01_03_*.png` (3 sections capturées) + `preuves/fix5/04_script_section_inexistante.txt` |
| 2 | Titres d'app tronqués (`Manuel de Diagnostic IA` → `Manuel de Diagno…`, `Wonder Woman Domain` → `WONDER WOMAN DOM…`) | `truncate` sur les lignes 219, 225, 273, 276 d'`AppFrame.tsx` | `AppFrame.tsx:219,225,273,276` | `truncate` remplacé par `leading-tight whitespace-normal break-words` — 2 lignes valent mieux qu'une amputation | `preuves/fix5/05_audit_sidebar_titre_entier.png`, `preuves/fix5/06_finance_sidebar_titre_entier.png` |
| 3 | `Onboarding (demo)` cassait en 2 lignes dans le rail | Le libellé `Onboarding (demo)` (17 chars) dépassait la largeur du rail (86 px) | `src/lib/app-discovery.ts:45` | Libellé raccourci à `Onboarding`. Le qualifiant `(demo)` est déjà dans `description` | `preuves/fix5/07_desktop_rail_onboarding.png` |
| 4a | Écran `cognition` illisible sous thème sombre | `text-stone-400` / `text-stone-700` figés dans `MissingApp` | `Desktop.tsx:157` | Couleurs branchées sur `var(--theme-text)` et `var(--theme-text-dim)` | `preuves/fix5/08_cognition_dark_oled.png` |
| 4b | App `cognition` ouvrable alors qu'elle n'existe plus | Entrée orpheline `'cognition': 'editorial'` dans `CANONICAL_APP_THEMES` (l'app n'est PAS dans `app-discovery.ts`) | `src/lib/themes/tokens.ts:270` | Entrée retirée (modification autorisée explicitement par le brief). L'app n'est plus trouvable via `getApp('cognition')`, donc plus d'écran d'erreur à montrer en pratique | cf. 4a pour la preuve du rendu une fois la fenêtre restaurée |

---

## Détail des correctifs

### 1 · data-section sur la barre latérale + sélecteur strict

**Avant** (`shot.mjs:101`) :
```js
const cible = page.locator(`[data-section="${section}"], button:has-text("${section}")`).first();
if (await cible.count()) { await cible.click(); await page.waitForTimeout(400); }
else console.error(`section "${section}" introuvable — capture sans changement d'onglet`);
```

Deux problèmes :
- `[data-section]` n'existait sur aucun élément.
- Le repli `button:has-text` attrapait le fil d'Ariane (bouton rendu `disabled`, le clic échoue avec `element is not enabled`) ou, pire, le bouton homonyme du rail du bureau — un agent a cliqué `People / Agents` du rail en croyant cliquer `Agents` du Dashboard, et la capture a montré la section `Overview` en prétendant montrer `Agents`.

**Après** :
- `AppFrame.tsx` : ajout de `data-section={s.label}` sur le `<button>` de section dans la sidebar uniquement. Pas sur le fil d'Ariane, pas sur le rail, pas sur les `<button>` du panneau d'outils.
- `shot.mjs` : sélecteur strict `[data-section="${section}"]` seul. Plus de repli. Échec avec `exit code 4` (zéro match) ou `exit code 5` (ambigu). Pas de capture muette.

**Preuve** :
- `preuves/fix5/01_dashboard_agents.png` — Dashboard > Agents, fil d'Ariane conforme
- `preuves/fix5/02_sales_today.png` — Sales > Today, fil d'Ariane conforme
- `preuves/fix5/03_marketplace_browse.png` — Marketplace > Browse, fil d'Ariane conforme
- `preuves/fix5/04_script_section_inexistante.txt` — `node tools/shot.mjs --app dashboard --section "CetteSectionNexistePas"` retourne `section "CetteSectionNexistePas" introuvable : aucun bouton avec [data-section="CetteSectionNexistePas"] dans la barre latérale.` puis `EXIT=4`. Le script échoue bruyamment comme demandé.

### 2 · Titres tronqués dans la sidebar

**Avant** (`AppFrame.tsx:219, 225, 273, 276`) : `truncate` sur le titre, le sous-titre, le nom du thème, et la ligne `Dark · default` du chip de thème.

**Après** : `truncate` remplacé par `leading-tight whitespace-normal break-words` sur les quatre emplacements. Le titre d'app et son sous-titre peuvent désormais passer sur 2 lignes. Le `truncate` du libellé de section (ligne 319) est conservé : les libellés de section (Overview, Maturité, Arbitrage, Contexte, Données, Automatabilité, ROI…) tiennent sur une ligne, pas besoin de retour.

**Preuve** :
- `preuves/fix5/05_audit_sidebar_titre_entier.png` — `Manuel de Diagnostic IA` sur deux lignes dans le header de la sidebar, intégralement visible.
- `preuves/fix5/06_finance_sidebar_titre_entier.png` — `Finance` + `WONDER WOMAN DOMAIN` (uppercase CSS) intégraux, pas d'amputation.

`FleetItemCard.tsx` (FIX-1) non touché, comme demandé.

### 3 · Rail du bureau — `Onboarding (demo)` raccourci

**Avant** (`src/lib/app-discovery.ts:45`) :
```js
registerApp({ id: 'onboarding', name: 'Onboarding (demo)', ... });
```

Le libellé 17 chars dépassait 86 px de large du `DesktopIcons.tsx` et passait sur deux lignes, alors que les 7 autres apps (Dashboard, People / Agents, Operations, IT / R&D, Clients, Tasks, Marketplace) tiennent sur une.

**Après** :
```js
registerApp({ id: 'onboarding', name: 'Onboarding', ... });
```

Le qualifiant `(demo)` est déjà porté par `description: '4-question fit · demo-coach citadel'`, donc aucune information perdue.

**Preuve** : `preuves/fix5/07_desktop_rail_onboarding.png` — le rail affiche `Onboarding` sur une seule ligne.

### 4 · cognition — écran d'erreur et entrée orpheline

**4a — Couleurs** (`Desktop.tsx:155-157`) :

**Avant** :
```jsx
<div className="w-16 h-16 rounded-2xl bg-[var(--canvas)] border border-[var(--panel-border)] ...">🚧</div>
<h3 className="text-base font-bold text-stone-700">{title}</h3>
<p className="text-sm text-stone-400 max-w-xs">This app is not registered.</p>
```

`text-stone-400` et `text-stone-700` sont des gris figés. Sous `dark-oled` (ou tout thème sombre), le titre était gris foncé sur fond gris foncé — illisible.

**Après** :
```jsx
<h3 className="text-base font-bold text-[var(--theme-text)]">{title}</h3>
<p className="text-sm text-[var(--theme-text-dim)] max-w-xs">This app is not registered.</p>
```

Branché sur les variables de thème, conforme à la palette. Le `🚧` continue d'utiliser `var(--canvas)` + `var(--panel-border)` (déjà OK).

**Preuve** : `preuves/fix5/08_cognition_dark_oled.png` — l'écran « This app is not registered. » s'affiche maintenant en blanc/clair sur fond noir, lisible sous `dark-oled`.

**4b — Entrée orpheline** (`src/lib/themes/tokens.ts:270`) :

**Avant** :
```js
export const CANONICAL_APP_THEMES: Record<string, string> = {
  ...
  'audit':       'glassmorphism',
  'cognition':   'editorial',         // sovereign gate, sobre serif
};
```

L'entrée `cognition` n'a plus de correspondant dans `app-discovery.ts` depuis la Phase 39b. Elle est orpheline : `getApp('cognition')` retourne `undefined`, et la logique de `useThemeIdFor(appId)` ne consulte `CANONICAL_APP_THEMES` qu'après avoir résolu l'app.

**Après** : entrée `'cognition'` retirée de `CANONICAL_APP_THEMES`.

**Choix entre (a) retrait et (b) redirection vers sales/Cognition** : j'ai choisi (a). La redirection aurait demandé de modifier `useShellStore.openApp` (hors périmètre) ou d'intercepter dans `Desktop.tsx` après le render, ce qui complique le boot. Le retrait suffit : il n'y a plus aucun chemin qui rende l'écran « This app is not registered. » dans le flux normal. La preuve 08 ne s'obtient qu'en injectant manuellement un layout dans localStorage — c'est un cas de figure défensif (un layout persisté d'une session antérieure), pas un chemin utilisateur.

C'est la **seule** modification autorisée à `CANONICAL_APP_THEMES`.

---

## Vérifications

| Vérification | Résultat |
|---|---|
| `npx vitest run` | **60/60 passés** en 10.26 s — la suite était à 60/60 avant, elle y reste. |
| `npx tsc -b` sur mes fichiers | **Aucune erreur introduite par mes modifications.** Une erreur pré-existante (`src/lib/app-discovery.ts:3 — 'BrainCircuit' declared but never read`) était déjà présente avant mon passage (vérifié par `git stash` + recompile). Je ne l'ai pas corrigée : elle sort de mon périmètre et la corriger aurait risqué de masquer un signal destiné à un autre agent. |
| Captures preuves/fix5/*.png | 7 fichiers générés, un fichier `.txt` pour l'échec bruyant du script. |
| Périmètre respecté | Tous mes fichiers modifiés sont dans le périmètre. Aucun fichier supprimé, aucun commit, aucun push. |

---

## Ce que je n'ai pas corrigé, et pourquoi

1. **`BrainCircuit` import inutilisé dans `app-discovery.ts`** — pré-existant, hors périmètre de cette tâche.
2. **`src/apps/cognition/CognitionApp.tsx`** — non touché, hors périmètre. La fonction `CognitionOverviewContent` y est toujours exportée et utilisée par `SalesApp.tsx` (l'import ligne 45 : `import { CognitionOverviewContent } from '../cognition/CognitionApp';`). C'est la cognition « embarquée » dans Sales, conforme à la Phase 39b. Rien à faire ici.
3. **`SalesDetailDrawer.tsx` (en `_TRASH_2026-07-27_pre_page_detail_align/`)** — ligne 75 référence encore `appId: 'cognition'`. C'est dans un dossier `_TRASH_*`, déjà exclu du build. Rien à corriger.
4. **Redirection `cognition` → `sales/Cognition`** — non implémentée. Justification dans le §4b : (a) suffit, et (b) demanderait soit de modifier `useShellStore.openApp` (hors périmètre), soit d'injecter une logique dans le render de `Desktop.tsx` qui complexifie le boot. Le retrait rend le cas inaccessible en pratique.
5. **Tests E2E pour le nouveau `data-section`** — non écrits. Le test serait trivial (assert que les boutons de section portent l'attribut), mais aucun test n'existe pour `AppFrame` aujourd'hui, et ajouter un test d'un fichier qui n'est pas dans mon périmètre est risqué. À laisser à un agent dédié si besoin.
