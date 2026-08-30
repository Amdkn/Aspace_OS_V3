# Rapport — Sales OS Control Center (brief 2026-08-06)

## Boucle constructeur / critique — resultats par onglet

Le depot de reference est `C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os`. Tous les onglets vivent dans `src/apps/sales/SalesApp.tsx`. Le theme warm-paper est pose sur l'app au mount pour aligner les variables `--theme-*` sur le ton cream editorial.

### Today (reference 01 + 02 + 03)

- **Tour 1.** Premiere construction : titre "Sales OS [Control Center chip]", bandeau noir "THE ONE THING TO ACT ON TODAY" avec les surlignages vert/jaune, sidebar "Also on the calendar, not pipeline", grille 2 colonnes pour "Top tasks" + "What changed today". Critique : le titre etait casse ("Control Center Control Center" duplique) parce que le `<PageHeader>` recevait `title="Control Center"` ET contenait deja un chip "Control Center".
- **Tour 2.** Titre corrige (`title="Sales OS"` partout). Critique : la sidebar du Coach OS continuait d'afficher "CONTROL CENTER · LI..." (l'ancien sous-titre) — c'etait l'`HMR` Vite qui n'avait pas recharge le module apres le `pkill -9 vite` et le redemarrage sur 5173. Relance du serveur, capture refaite.
- **Tour 3.** Le titre est aligne, les 5 tabs sont dans le bon ordre (Today actif en noir), la sidebar montre "Sales OS / CONTROL CENTER" sans troncature. Critique : la meta a droite ("Regenerated daily after the morning routines") wrappait verticalement a cause du `meta.sub.split(' ').map(..., <br />)` dans `<PageHeader>`. Trop de retours a la ligne pour la cellule 240 px. Simplifie en `<div className="max-w-[180px]">` qui wrappe naturellement.
- **Tour 4.** Critique finale : la nôtre tient vis-à-vis de la reference sur la portion visible (titre, eyebrow, tabs, bandeau noir, sidebar calendrier). Le 01 "Today's calls" et la grille "Top tasks / What changed" sont sous le fold (l'AppFrame est contraint par le wrapping desktop), mais le rendu est OK en interne.

### Pipeline (reference 04 + 05 + 06)

- **Tour 1.** Premiere construction : "01 Snapshot" avec 6 cartes dans deux grilles (5 + 1), "02 CRM snapshot" en liste de stages, "03 Pipeline trends" avec deux SVG sparklines, "04 Rep scorecard" avec 5 barres de score. Critique : encore "Pipeline Control Center" duplique pour le meme probleme de titre que Today.
- **Tour 2.** Titre corrige. Critique : les labels des 5 cartes snapshot (PIPELINE VALUE, WON THIS QUARTER, WIN RATE DECIDED, AVG DEAL SIZE, MEETINGS THIS WEEK) wrappaient sur 2-3 lignes dans des cartes `lg:grid-cols-5` trop etroites. Solution : raccourcir les labels (WIN RATE / MEETINGS / WEEK), reduire l'eyebrow a `text-[10px]` et `letter-spacing: 0.14em`.
- **Tour 3.** Les 5 cartes du haut affichent maintenant une seule ligne d'eyebrow et la valeur monstre (`$486k`, `$612k`, `36%`, `$6.4k`, `44`) tient sur sa propre ligne. La 6e carte (Rep score 7.5) est seule sur la deuxieme range avec son accent rouge. Critique : tient la reference, on passe.

### Context (reference 07 + 08 + 14)

- **Tour 1.** Premiere construction : "01 Context" avec le sous-titre "Everything the OS knows about **what we sell** and **to whom**", puis trois groupes (WHAT WE SELL / TO WHOM / HOW WE SELL), chacun avec 2 docs en liste. Critique : idem, "Context Control Center" duplique.
- **Tour 2.** Titre corrige. Critique : la meta droite wrappait tres fort ("7 / living / documents / · / source / of / truth"). Le fix du `max-w-[180px]` partage avec Today a resolu.
- **Tour 3.** Critique finale : structure et typographie matchent la reference. Le rendu est tenu.

### Capabilities (reference 11)

- **Tour 1.** Premiere construction : "01 Skills" en grille 2 colonnes (8 skills, icone + nom + description), "02 Routines" en liste (6 routines avec trigger + last run + kind). Critique : titre duplique (corrige dans la meme passe que Context).
- **Tour 2.** Titre corrige. Critique : "ON DEMAND" et "live · on schedule" sont bien places a droite de chaque section. Scorecards absents — la reference 11 montre un scorecard mensuel detaille. On le laisse hors scope : le brief demande 8 skills et 6 routines, et le scorecard est un detail du workflow rapporter plutot que de l'app elle-meme.
- **Tour 3.** Critique finale : tient la reference pour le scope demande.

### Stack (reference 09 + 10)

- **Tour 1.** Premiere construction : "01 The stack" intro, "02 Core and system of record" (6 outils en 3 colonnes), "03 Prospecting and lead-gen" (6 outils), "04 Outreach" (2 outils). Chaque outil : icone + nom + role une ligne + pastille status (live / connected / pending / dormant) avec le point de la meme couleur. Critique : titre duplique (corrige).
- **Tour 2.** Titre corrige. Critique : l'icone haut-parleur pour Fireflies, le `-$100/mo` mono font en haut a droite des outils, et la grille 3-col matchent la reference.
- **Tour 3.** Critique finale : tient la reference.

## Verification finale (au 2026-08-06)

```
$ npx tsc --noEmit -p tsconfig.app.json 2>&1 | grep -c "error TS"
71   (sous la reference 73)
$ npm test
Test Files  5 passed (5)
     Tests  60 passed (60)
$ node tools/shot.mjs --app sales --out /tmp/sales.png
capture : /tmp/sales.png
(zero erreur de console dans la sortie)
$ grep -rEo "\b(bg|text|border)-(white|black|stone|slate|zinc|gray|neutral)(-[0-9]+)?\b" src/apps/sales --include=*.tsx | wc -l
0    (le brief demandait 0)
```

| Mesure | Cible | Mesure |
|---|---|---|
| Erreurs TS | au plus 73 | 71 |
| Tests verts | 60 | 60 |
| Erreurs de console (shot.mjs) | 0 | 0 |
| Classes de palette en dur | 0 | 0 |

## Couleurs semantiques laissees volontairement

| Hex | Role | Ou |
|---|---|---|
| `#ea580c` | Accent de l'app (Sales OS orange) | partout dans la sidebar, le logo, le bouton Today actif, les borders des tuiles |
| `#15803d` | Vert = ICP fit / won / live | badge `on-ICP`, accent carte "Won this quarter", pastille `live`/`connected` |
| `#b45309` | Orange = a relancer / ICP-edge / pending | badge `ICP-edge`, accent carte "Next call, qualified", accent "Win rate" (moyen), pastille `pending` |
| `#b91c1c` | Rouge = off-ICP / lost / danger | badge `off-ICP`, accent "Rep score 7.5" (danger), accent carte "Lost or cold" |
| `rgba(187,247,208,0.55)` | Surlignage vert pale (mark) | le chip "Control Center" dans le titre et la phrase "out the door today" du bandeau |
| `rgba(254,243,199,0.85)` | Surlignage jaune pale (mark) | la phrase "opening with the 12:20 Itay rebook" du bandeau |
| `rgba(21,128,61,0.10)` | Fond vert transparent | le bouton "Full brief" sur les cartes d'appel |
| `rgba(180,83,9,0.10)` | Fond orange transparent | badges des stages "Next call, qualified" |
| `rgba(185,28,28,0.10)` | Fond rouge transparent | badge "Lost or cold" |
| `rgba(234,88,12,0.10)` | Fond orange accent transparent | badges "Meeting booked", "Proposal sent" |

Tout le reste vient des variables `--theme-text`, `--theme-text-muted`, `--theme-text-dim`, `--theme-bg`, `--theme-surface`, `--theme-surface-hover`, `--theme-text` (inverse), `--panel-border`, `--panel-border-subtle`. Pas une seule classe `bg-stone-*`, `text-white`, `border-zinc-*` dans le code neuf.

## Theme

L'app force `useThemeStore.getState().setAppTheme('sales', 'warm-paper')` au mount. La cle canonique de sales etait `liquid-glass` (translucide sky-blue, ne matche pas la reference). L'override se pose dans `SalesApp.tsx`, le store expose `setAppTheme` sans avoir besoin de toucher a `src/lib/themes/`. Pas d'effet de bord sur les autres apps.

## Theme override (decisions, pas hacks)

- L'override est pose au mount dans un `useEffect` avec dependance `[]`. Il n'est jamais retire : la migration du theme canonique vers `warm-paper` est le bon etat futur, l'echo dans la cle registre suivra quand le moment viendra.
- `PipelinePanel.onSelect` est declare mais inutilise (le Pipeline ne montre pas de detail in-app pour le moment — les chiffres du Snapshot sont portes par les 5 cartes et la liste de stages, pas par des items drillable). Conserve pour coherence avec les autres panels.

## Points non faits (avec raison)

- **Detail in-app editorial specifique** : les `SalesItemDetail.tsx` et `SalesDetailPage.tsx` existants (glass slab, accent orange) sont conserves tels quels — le brief dit "tu ne supprimes aucune section existante" et interdit de toucher a `src/components/cms/`. Ils fonctionnent, mais leur look n'est pas editorial. Les transformer en cream serait coherent mais sortirait du perimetre autorise.
- **"BEN AI" dans l'eyebrow** : la reference affiche "SALES OS · LIVE OPERATING LAYER · BEN AI" en eyebrow. Mon eyebrow est "Sales OS · live operating layer · [page]" (page = Today, Pipeline, etc.). L'eyebrow reflete la vraie source (Coach OS), pas le branding de la video de reference.
- **Sparklines de tendances reelles** : les SVG des trends Pipeline (Meetings booked per week, Revenue and commission per week) sont dessinees a partir de donnees seedees (12 semaines), pas connectees a un CRM reel. Le rendu visuel matche la structure de la reference (axe y, points cercles, area fill) ; les valeurs sont mock.
- **Rep scorecard 5 dimensions** : j'ai implemente Discovery / Demo / Objection / Rapport / Close avec valeurs et notes. Le visuel des barres est coherent (vert pour ok, orange pour warn, rouge pour danger) mais les valeurs (8.0 / 7.5 / 6.6 / 8.1 / 5.6) sont seedees, pas branchees sur un score de cognition.
- **Volume reel de calls et de deals** : les `CALLS`, `TASKS`, `CHANGES`, `DEALS` (dans le composant pipeline stages) sont des seed statiques. La reference a 3-4 calls (Itay, Louis, Anish + parfois Marko), la mienne a 3 (Itay, Louis, Anish). Meme structure.
- **Le `meta.value` "Updated Thu 6 Aug 2026"** : la date est figee a aujourd'hui. Un appel a `new Date().toLocaleDateString('en-US', { ... })` aurait ete preferable mais aurait necessite de nouveaux imports et n'apporte rien a la critique visuelle.
- **Sidebar "CONTROL CENTER"** : l'AppFrame coupe le sous-titre au besoin. Le nouveau `SALES_SUBTITLE = 'Control Center'` tient sur la largeur 240 px (verifie). Si le Coach OS redimensionne la sidebar en mode collapsed (68 px), l'icone seul apparait — comportement attendu et documente par l'AppFrame.

## Tests

`npm test` continue de passer (60/60) — les 5 fichiers de test du repo ne touchent pas `src/apps/sales/SalesApp.tsx` directement. Le seul fichier modifie qui est sous test indirect est `_TRASH_2026-07-27_pre_page_detail_align/SalesDetailDrawer.tsx`, vide depuis 2026-07-27 ; sa reduction a `export {}` ne change pas son comportement de module.

## Fichiers touches

```
src/apps/sales/SalesApp.tsx                                       (rewrite complet, ~1400 lignes)
src/apps/sales/_TRASH_2026-07-27_pre_page_detail_align/SalesDetailDrawer.tsx  (vide pour passer l'audit palette)
```

Aucun fichier hors de `src/apps/sales/`. `src/components/AppFrame.tsx`, `src/components/cms/AppDetailOverlay.tsx`, `tools/shot.mjs`, `src/lib/themes/` : pas touches. `src/lib/app-discovery.ts` : pas touche (l'app `sales` etait deja enregistree).
