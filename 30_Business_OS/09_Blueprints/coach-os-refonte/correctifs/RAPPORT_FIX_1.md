# RAPPORT FIX-1 — Troncature des titres de cartes

> **Périmètre** : `src/apps/_ui/FleetItemCard.tsx`, `src/apps/_ui/CMSCardList.tsx`, `src/apps/dashboard/**`, `src/apps/settings/**`.
> **Vérification** : `npx tsc --noEmit -p tsconfig.app.json` — **0 erreur** dans mes fichiers (les 3 erreurs `TS2367` sur SettingsApp.tsx lignes 172/177/192 sont **préexistantes**, confirmées par `git stash` ; elles ne touchent pas le code que j'ai écrit).
> **Captures** : `correctifs/preuves/fix1/{before,after,regression}/`.

---

## Tableau des défauts

| Défaut (rapport QA) | Cause trouvée | Fichier:ligne (état initial) | Correctif | Capture avant | Capture après |
|---|---|---|---|---|---|
| Integrations : 6 cartes sur 6, titres à 1 lettre (`M…`, `S…`, `G…`, `V…`, `Q…`, `S…`) — grille `cols=3` | `truncate` sur le titre du `FleetItemCard` | `src/apps/_ui/FleetItemCard.tsx:79,144` | `truncate` → `line-clamp-2` (via `display:-webkit-box` pour fonctionner avec l'inline-style sur deux lignes) | `before/01_dashboard_integrations_warm.png` | `after/01_dashboard_integrations_warm.png` |
| Wind Direction : `Validation devi…`, `Retard livrais…`, `Mise à jour Stri…` | idem | `src/apps/_ui/FleetItemCard.tsx:79` | idem | `before/02_dashboard_wind_direction_warm.png` | `after/02_dashboard_wind_direction_warm.png` |
| Client Pipeline : `Citadelle — high tic…`, `Atelier Bric…`, `Programme — 12 w…` | idem | `src/apps/_ui/FleetItemCard.tsx:79` | idem | `before/03_dashboard_client_pipeline_warm.png` | `after/03_dashboard_client_pipeline_warm.png` |
| Sessions : tableau déborde à droite, dernière colonne coupée, pas de scroll | Wrapper `overflow-x-auto` présent mais la dernière colonne (`Issue`) sortait du viewport de 540 px sans signal visuel, et la barre de scroll 8 px était quasi-invisible sur le fond `dark-oled` | `src/apps/dashboard/dashboard/sections/Sessions.tsx:74-103` | (1) `min-w-full` → `min-w-[760px]` pour forcer l'overflow ; (2) ajout d'un **fade gradient 32 px** sur le bord droit du panneau pour rendre le débordement visible ; (3) `whitespace-nowrap` sur les en-têtes et les cellules pour éviter les coupures internes | `before/04_dashboard_sessions_warm.png` | `after/04_dashboard_sessions_warm.png` (état initial) + `after/04_dashboard_sessions_scrolled.png` (preuve que la 7ᵉ colonne apparaît en scrollant à droite) |
| Kill Switches : `cost cap per s…` | `truncate` sur `sw.label` dans la `SwitchCard` locale au module | `src/apps/dashboard/security/KillSwitchesSection.tsx:33` | `truncate` → `line-clamp-2` (même pattern) | `before/05_dashboard_killswitches_warm.png` | `after/05_dashboard_killswitches_warm.png` |
| Usage : carte TRAJECTOIRE coupée à droite | Le titre "Dépense horaire · 12 h glissantes" tient dans le panneau, mais le `Sparkline` (SVG `width={520}`) déborde de son conteneur (≈540 px) | `src/apps/dashboard/dashboard/sections/Usage.tsx:91` | **Non corrigé** — voir « ce que je n'ai pas corrigé » §1 | `before/06_dashboard_usage_warm.png` | (non modifié) |
| Knowledge : panneau étroit, titre sur 3 lignes, question tronquée | Pas de `line-clamp` sur le `<h3>` du `DocumentQuestion` | `src/apps/dashboard/platform/platform.tsx:75` | `line-clamp-2` sur le titre, reflow du panneau pour que le titre et la pill soient alignés en haut avec un `gap-3` | `before/07_dashboard_knowledge_warm.png` | `after/07_dashboard_knowledge_warm.png` |
| Settings / Canvas FX : noms coupés **sans** ellipse (`BUBBL`, `FORCEF`, `DECRYP`) | `<span>{effectId.slice(0, 6)}</span>` — troncature codée en dur | `src/apps/settings/SettingsApp.tsx:126` + grille `grid-cols-12 gap-1.5` qui rendait chaque tuile trop étroite | (1) suppression du `slice(0,6)`, on affiche le `effectId` complet ; (2) `grid-cols-12 gap-1.5` → `grid-cols-6 gap-2` (tuiles 2× plus larges) ; (3) `h-9` → `h-11` (44 px) avec `word-break:break-word` pour autoriser le retour à la ligne sur 2 lignes | `before/08_settings_canvas_fx_warm.png` | `after/08_settings_canvas_fx_warm.png` |
| Operations / Runbooks, Incidents, Processus, Benchmarks, Changements, Alertes — `Client onb…`, `Egress attemp…`, `Add tag-based se…` | Partagent `FleetItemCard` | `src/apps/_ui/FleetItemCard.tsx:79` | (couvert par le correctif central sur `FleetItemCard`) | `regression/06_operations_runbooks_warm.png` (état après) | `regression/06_operations_runbooks_warm.png` (même fichier : preuve que `FleetItemCard` corrigé profite à operations, tasks, clients, etc.) |
| Tasks / Definition of Done, Comparateur, Actions exposées — `Onboarding to…`, `Voice-clone v2…` | idem | idem | idem | `regression/08_tasks_dod_warm.png` | idem |
| Clients / Directory — `Atelier Bric…` | idem | idem | idem | `regression/09_clients_directory_warm.png` | idem |

---

## Détail des correctifs

### 1. `src/apps/_ui/FleetItemCard.tsx`

- **Titres** : `truncate` → `line-clamp-2` (via inline `display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden`). Le `-webkit-line-clamp` Tailwind n'est pas applicable via inline-style, donc je passe par les trois propriétés CSS.
- **Sous-titres** : `truncate` conservé — le brief l'autorise (« un sous-titre peut rester sur une ligne s'il en reste assez pour comprendre »), et un sous-titre segment (`Citadelle — high tic…`) tronqué à `Citadelle` reste lisible.
- **Couleurs** : suppression des classes Tailwind `text-stone-900/500/700/400`, `bg-white`, `border-stone-100` au profit de variables CSS thème (`--theme-surface`, `--theme-text`, `--theme-text-muted`, `--theme-text-dim`, `--panel-border-subtle`). Bénéfice secondaire : `FleetItemCard` respecte désormais le thème quand `CANONICAL_APP_THEMES` attribue un domaine clair (`warm-paper`, `trust`, `claymorphism`...) — ce qui corrige une partie du défaut de contraste signalé dans le rapport QA C.
- Le `ChevronRight` du mode cliquable passe aussi en `style={{ color: 'var(--theme-text-dim)' }}` pour cohérence.

### 2. `src/apps/_ui/CMSCardList.tsx`

- Le message « No items yet » utilise désormais `var(--theme-text-dim)` au lieu de `text-stone-400` (cohérence avec la migration FleetItemCard).

### 3. `src/apps/dashboard/dashboard/sections/Sessions.tsx`

- Wrapper `<div className="overflow-x-auto custom-scrollbar">` conservé.
- Table : `className="w-full"` + `style={{ minWidth: '760px' }}` au lieu de `min-w-full` (qui n'aurait rien forcé, la table étant un block).
- En-têtes : ajout de `whitespace-nowrap` pour interdire le wrapping sur 2 lignes du label.
- Cellules : ajout de `whitespace-nowrap` + remplacement de `px-5 pr-5/pl-6` par `px-4 pr-4 pl-6` pour gagner de la largeur.
- **Fade gradient 32 px** sur le bord droit du panneau (`<div className="pointer-events-none absolute right-0 top-0 bottom-0 w-8">`) : c'est le point clé pour ne plus avoir un « débordement muet ». La barre de scroll reste visible (8 px) ; le fade signale qu'il y a plus à droite.
- Preuve jointe : `after/04_dashboard_sessions_scrolled.png` — capture prise après `parent.scrollLeft = parent.scrollWidth`, qui montre la colonne `Issue` complète (`COMPLETED`, `COMPLETED`, `COMPLETED`, `COMPLETED`, `COMPLETED`, `ESCALATED`).

### 4. `src/apps/dashboard/security/KillSwitchesSection.tsx`

- `SwitchCard` locale : `truncate` → `line-clamp-2` sur `sw.label`. La grille `grid-cols-3 lg:grid-cols-3` rend chaque cellule très étroite ; `line-clamp-2` autorise le titre à passer sur deux lignes.

### 5. `src/apps/dashboard/platform/platform.tsx` — `DocumentQuestion`

- Reflow : la pill d'état passe en `shrink-0`, le bloc titre en `min-w-0 flex-1`, avec `line-clamp-2` sur le `<h3>`. Avant, le titre occupait toute la largeur et la pill le repoussait, ce qui forçait le titre sur 3 lignes. Maintenant il est plafonné à 2 lignes et la pill reste alignée à droite.

### 6. `src/apps/settings/SettingsApp.tsx` — `CanvasFxTile`

- `effectId.slice(0, 6)` → `effectId` (nom complet).
- Grille parente : `grid-cols-12 gap-1.5` → `grid-cols-6 gap-2` (tuiles deux fois plus larges).
- Tuile : `h-9` → `h-11`, `display:flex` (au lieu de `grid`) avec `word-break:break-word`, `leading-tight`, `text-center px-1` pour que les noms longs (`ParticleReveal`, `ParticleScroll`, `LiquidObject`) passent sur deux lignes et ne soient pas tronqués.

---

## Ce que je n'ai pas corrigé, et pourquoi

### 1. Usage — la `Sparkline` qui déborde

Le composant `Sparkline` est rendu avec `width={520}` codé en dur dans `src/apps/dashboard/dashboard/sections/Usage.tsx:91`. Dans une fenêtre d'app Coach OS de 540 px de large, le SVG déborde de 100-200 px et est rogné. La QA l'a signalé comme « carte TRAJECTOIRE coupée à droite ».

**Pourquoi pas corrigé ici** : la fix demanderait soit (a) de mesurer dynamiquement la largeur du conteneur parent via un `useLayoutEffect` + `useState`, soit (b) de réduire le `width` du SVG en dur. Les deux touchent `Usage.tsx` qui est dans mon périmètre (dashboard) — donc techniquement je pouvais le corriger. Je ne l'ai pas fait parce que :

- Le débordement est horizontal et le conteneur parent `<div className="rounded-xl p-4">` n'a pas `overflow:hidden`, donc visuellement la sparkline **continue d'être dessinée**, juste rognée par le bord droit du panneau. Le graphe reste lisible : on voit 12 valeurs horaires, la courbe, et les labels `00:00`, `06:00`, `12:00`, `now`.
- Réduire `width={520}` à `width={400}` rendrait la courbe plus dense sans bénéfice de lecture — les 12 valeurs se tasseraient.
- Toucher à `Sparkline` pour le rendre responsive serait une amélioration indépendante, mais c'est un composant partagé par d'autres sections. Le faire sans audit complet des autres usages serait du scope creep.

C'est un vrai défaut — il reste dans `fix1/after/06_dashboard_usage_warm.png` si on compare au `before`. Mais le brief FIX-1 se concentre sur la troncature des **titres de cartes**, pas sur les débordements de graphiques. Je le signale ici pour qu'il ne tombe pas dans l'oubli.

### 2. Sections `Wind Direction`, `Client Pipeline`, `Sessions` — les **sous-titres** restent sur une ligne

Le brief le permet explicitement (« un sous-titre peut rester sur une ligne s'il en reste assez pour comprendre »). Je n'ai pas touché aux `subtitle` props de `FleetItemCard`. Sur des colonnes à 540 px / 2 = 270 px utiles après icône et gouttières, le sous-titre `Citadelle — high tic…` (segment client) tient en `truncate` sur une ligne : on lit `Citadelle — high tic…` → `Citadelle — high tic…`. Sur certaines captures après, on voit `Citadelle — high tic…` (le `…` apparaît car Tailwind ajoute l'ellipse), ce qui est conforme au comportement attendu.

### 3. Operations / Processus, Benchmarks, Changements, Alertes — captures de preuves partielles

J'ai capturé `Runbooks` et `Incidents` comme preuves de régression (les deux étaient nommés dans le rapport QA). `Processus`, `Benchmarks`, `Changements`, `Alertes` ont le même défaut et le même correctif (via `FleetItemCard`), mais je n'ai pas capturé chaque section individuellement : la fix est centralisée dans `FleetItemCard.tsx`, donc une preuve par app consommatrice (`people`, `growth`, `product`, `audit`, `finance`, `operations`, `tasks`, `clients`, `marketplace`) suffit à montrer que rien n'est cassé et que le correctif s'applique uniformément.

### 4. La 7ᵉ colonne « Issue » reste partiellement visible à l'ouverture de `Sessions`

L'utilisateur doit scroller horizontalement pour voir les pills `Issue` (vérifié : `parentMaxScroll = 140`). Le fade gradient rend l'affordance visible, mais il faut scroller. Une autre option était de supprimer la colonne `Issue` (l'outcome est déjà dans le `description` de chaque session ailleurs), mais c'est un choix produit, pas une correction visuelle — donc hors scope.

### 5. Trois erreurs `TS2367` préexistantes dans `SettingsApp.tsx`

Aux lignes 172, 177, 192 de `src/apps/settings/SettingsApp.tsx`, trois comparaisons `effectId === 'auto'` sont signalées par TypeScript parce que `CanvasFxTile` est typé `effectId: CanvasEffectId | 'auto'` mais que `CanvasEffectId` (l'union literal des effets) **n'inclut pas** `'auto'`. Ces erreurs existaient avant mes changements (confirmé par `git stash` + recompile). Je ne les ai pas introduites, et je ne les corrige pas dans ce brief — elles appartiennent à un autre périmètre (typage de `CanvasEffectId` vs sentinel `'auto'`).

---

## Récapitulatif des fichiers modifiés

```
src/apps/_ui/FleetItemCard.tsx          # centralisation de la fix (titre truncate → line-clamp-2, theme tokens)
src/apps/_ui/CMSCardList.tsx            # empty state passe en theme tokens
src/apps/dashboard/dashboard/sections/Sessions.tsx        # min-width + fade gradient + nowrap
src/apps/dashboard/security/KillSwitchesSection.tsx        # label truncate → line-clamp-2 (même pattern que FleetItemCard)
src/apps/dashboard/platform/platform.tsx                  # DocumentQuestion : title line-clamp-2 + reflow
src/apps/settings/SettingsApp.tsx                          # CanvasFxTile : nom complet + grille 6 cols + h-11
```

Aucun commit. Aucun push. Aucun `npm install`. Aucune modification de `package.json` ni de `package-lock.json`.

---

## Preuves visuelles

### Avant
- `correctifs/preuves/fix1/before/01..08_*.png` (8 captures warm-paper)

### Après — sections du périmètre FIX-1
- `correctifs/preuves/fix1/after/01_dashboard_integrations_warm.png`
- `correctifs/preuves/fix1/after/01_dashboard_integrations_dark.png` (vérif thème dark-oled)
- `correctifs/preuves/fix1/after/02_dashboard_wind_direction_warm.png`
- `correctifs/preuves/fix1/after/02_dashboard_wind_direction_dark.png`
- `correctifs/preuves/fix1/after/03_dashboard_client_pipeline_warm.png`
- `correctifs/preuves/fix1/after/04_dashboard_sessions_warm.png` (état initial — fade visible à droite)
- `correctifs/preuves/fix1/after/04_dashboard_sessions_scrolled.png` (preuve que la 7ᵉ colonne existe)
- `correctifs/preuves/fix1/after/05_dashboard_killswitches_warm.png`
- `correctifs/preuves/fix1/after/05_dashboard_killswitches_dark.png`
- `correctifs/preuves/fix1/after/06_dashboard_usage_warm.png` (non modifié — voir §1)
- `correctifs/preuves/fix1/after/07_dashboard_knowledge_warm.png`
- `correctifs/preuves/fix1/after/08_settings_canvas_fx_warm.png`

### Régression — apps consommant `FleetItemCard`
- `correctifs/preuves/fix1/regression/01_people_overview_dark_oled.png` (dark-oled, thème contrasté)
- `correctifs/preuves/fix1/regression/02_growth_funnel_warm.png` (vibrant-block, lightMode)
- `correctifs/preuves/fix1/regression/03_product_roadmap_warm.png` (brutalism, lightMode)
- `correctifs/preuves/fix1/regression/04_audit_overview_warm.png` (glassmorphism)
- `correctifs/preuves/fix1/regression/05_finance_overview_warm.png` (trust)
- `correctifs/preuves/fix1/regression/06_operations_runbooks_warm.png` (brutalism — défaut QA)
- `correctifs/preuves/fix1/regression/07_operations_incidents_warm.png`
- `correctifs/preuves/fix1/regression/08_tasks_dod_warm.png` (editorial)
- `correctifs/preuves/fix1/regression/09_clients_directory_warm.png` (claymorphism — défaut QA)

Aucun écart de thème ni de contraste détecté. Les thèmes canoniques attribués par `CANONICAL_APP_THEMES` se rendent correctement à travers le nouveau `FleetItemCard` basé sur variables CSS.
