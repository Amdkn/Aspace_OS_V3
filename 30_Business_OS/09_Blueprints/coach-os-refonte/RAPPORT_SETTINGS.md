# RAPPORT — Settings : themes de barre latérale et fond d'écran

**Date** : 2026-08-06
**Branche** : main
**Périmètre touché** : `src/apps/settings/` (SettingsApp.tsx, theme-details.tsx), `src/lib/wallpaper.ts` (nouveau), `src/components/Desktop.tsx` (lecture seule + overlay wallpaper).

---

## Tâche 1 — Per-app override gouverne la barre latérale

### Observation AVANT correction

J'ai d'abord vérifié que le mécanisme d'override fonctionnait réellement, comme demandé. Capture comparative de IT/R&D :

- **Capture 1 — `appThemes['it-rd'] = 'editorial'`** : la barre latérale passe en rose Editorial, le chip de thème affiche `Editorial · CUSTOM`, l'identité de l'app suit bien la surcharge.
- **Capture 2 — `appThemes['it-rd'] = undefined`** (override effacé) : la barre latérale revient au cyberpunk par défaut, le chip affiche `Cyberpunk · DEFAULT`.

**Conclusion de l'observation** : la résolution (`resolveTheme(appId)` dans `src/lib/themes/store.ts`) est correcte. Un choix explicite gagne sur le défaut canonique. La cause du « ça ne marche pas » du propriétaire était dans l'interface, pas dans le magasin.

Causes réelles du malaise côté UI :

1. **Le label mentait.** La section s'intitulait « Per-app override » sans expliquer sa portée ; on pouvait croire qu'elle repeint toute l'app.
2. **La rangée de sélection était illisible.** Carrousel de pastilles miniatures (9 px de hauteur), pas de nom de thème visible sans survol, distinction actif/inactif quasi impossible.
3. **Le défaut canonique était invisible.** Aucune indication quand on s'écartait du thème canonique, donc impossible de savoir si on était sur une surcharge ou sur le défaut.
4. **Le reset n'apparaissait que dans un état.** Pas de chip « default » quand l'app suivait le canonique.

### Ce que j'ai construit (T1)

Dans `src/apps/settings/SettingsApp.tsx` :

- **Titre de la section modifié** : « Themes · 12 styles from the UI UX Pro Max catalogue · per-app override governs the sidebar » — la portée est dans le sous-titre.
- **Carte « Global default » enrichie** : « Drives the top bar and every detail page. Per-app overrides only repaint the sidebar. » — la règle est rendue explicite.
- **Carte « Per-app sidebar theme »** (renommage + sous-titre deux phrases) :
  > « The override paints the left sidebar and section surfaces of that app. Detail pages always follow the global theme on the top bar — that's by design. »
- **Range de sélection refondue** : 12 cartes par app (grille 3/4/6 colonnes responsive). Chaque carte montre le nom du thème en clair, un aperçu miniature de ses accents, et un check visible sur le thème actif. La carte active a une bordure épaisse + ring + icône Check côté label.
- **État en clair sous le titre de chaque app** : `Sidebar now: <Nom> · default · <Nom canonique>` ou `Sidebar now: <Nom custom> · default · <Nom canonique>` — l'utilisateur voit immédiatement s'il est sur une surcharge ou sur le canonique.
- **Bouton Reset par app** : chip « default » quand l'app suit le canonique, bouton « Reset » explicite (icône + texte) dès qu'il y a une surcharge.
- **Magasin intact** : `setAppTheme` / `resetAppTheme` du store de thèmes ne sont pas réécrits, jamais appelés depuis un `useEffect` (rappel de la directive « pas d'écriture hors action utilisateur »).

### Captures

- `tmp/settings-themes.png` : Themes — header + Global default card avec la nouvelle explication de portée.
- `tmp/per-app-overrides.png` : Per-app overrides scrollé en bas — on voit « Growth » et « Sales Sanctum » avec leurs 12 cartes, le thème actif en évidence, le canonique en sous-titre. Toutes les apps de la liste portent la même structure.

---

## Tâche 2 — Section Wallpaper

### Architecture

- **Nouveau fichier `src/lib/wallpaper.ts`** (helper autonome). Trois clés localStorage dédiées (`coach-os-wallpaper-data-v1`, `coach-os-wallpaper-fit-v1`). Comme `demoShell.ts` pour `hasSeenCitadel`, c'est volontairement séparé du store Zustand des thèmes : une data URL de plusieurs Mo ferait exploser le blob persisté à chaque toggle de thème (re-sérialisation complète à chaque mutation), et un `QuotaExceededError` du navigateur effacerait silencieusement toutes les surcharges de thèmes de l'utilisateur.
- **Pas de dépendance ajoutée** : `createImageBitmap` + `<canvas>` (OffscreenCanvas où disponible, fallback DOM `<canvas>`), `convertToBlob` / `toDataURL` à `image/jpeg` qualité 0.85. Une photo 12 MP atterrit typiquement < 1 MB après redimension à 2560 px de côté long.
- **Échecs explicites** : `QuotaExceededError` est détecté et transformé en message utilisateur (« Browser storage is full. Clear some site data, then try a smaller image. »). Idem pour fichier non-image et erreur de décodage. L'image n'est jamais perdue en silence.
- **`src/components/Desktop.tsx`** modifié minimalement : import de `getWallpaper`, overlay d'un `<div fixed inset-0 z-[-9]>` au-dessus du `<Wallpaper>` original (qui reste rendu comme scène de fond). Quand `dataUrl` est null, l'overlay ne s'affiche pas et le papier-jardin canonique reprend ses droits. Aucun autre fichier de `Desktop.tsx` n'a été touché.

### Ce que j'ai construit (T2)

Nouvelle section dans la barre latérale de Settings, après Themes et avant Canvas FX : **Wallpaper** (icône `ImageIcon`).

L'écran propose :
- **Aperçu live** dans un cadre 192×112 px — l'image redimensionnée s'affiche avec le fit sélectionné, ou une icône image vide si rien n'est défini.
- **Bouton Upload image** (primary) + **Remove** (secondaire, seulement quand une image est définie).
- **Sélecteur de fit** : cover / contain / repeat (cover par défaut). Chips avec icône Check sur le fit actif, désactivés tant qu'aucune image n'est chargée.
- **Texte d'aide** sur la résidence locale et le budget ~1 MB.
- **Bouton Restore default** dans le `SectionHead` — remet le fond d'origine, désactivé tant qu'aucune image n'est définie.

`Restore default` est disponible **deux endroits** (le bouton d'en-tête + le bouton Remove inline) parce que les deux répondent au même contrat « défaire ce que j'ai fait » — c'est le pattern `Cancel` × `Revert` que d'autres shells utilisent.

### Captures

- `tmp/settings-wallpaper.png` : Wallpaper — état initial, « No custom wallpaper », bouton Upload image, fit `cover` actif, autres fits grisés.
- `tmp/settings-wallpaper-with-image.png` : après upload d'un dégradé bleu/violet/rose généré à la volée par le browser — preview rendu, header bascule à « Custom wallpaper set », le bouton Remove apparaît, fit reste à cover.
- `tmp/desktop-with-wallpaper.png` : bureau après fermeture de la fenêtre Settings — l'image de dégradé couvre l'arrière-plan, le papier-jardin a disparu, les icônes d'apps restent au-dessus.

---

## Vérifications chiffrées

| Contrôle | Attendu | Observé |
|----------|---------|---------|
| `npx tsc --noEmit -p tsconfig.app.json` erreurs | ≤ 67 | **67** |
| `npm test` tests verts | 60 | **60 passed (5 files)** |
| `node tools/shot.mjs --app settings --out /tmp/settings.png` erreurs console | 0 | **0** (le script termine sans lister d'ERREURS CONSOLE) |
| `grep palette classes src/apps/settings` | 0 | **0** |
| Fichiers `_TRASH_*` touchés | non | non |
| Magasin `src/lib/themes/store.ts` touché | non | non |
| `AppFrame.tsx` / `AppDetailOverlay.tsx` touchés | non | non |
| `tools/shot.mjs` touché | non | non |
| `git commit` / `git push` | non | non |

Note : le run `npm test` affiche 60 tests verts (brief = 60 verts) ; un warning `Unhandled Error` pré-existant sur `src/lib/ontology/ontology.test.ts` (timeout d'un worker forks) est visible mais n'a pas empêché le passage — non causé par cette tâche (le test incriminé n'a jamais été modifié).

---

## Fichiers modifiés / créés

| Fichier | Nature |
|---------|--------|
| `src/lib/wallpaper.ts` | créé |
| `src/apps/settings/SettingsApp.tsx` | réécrit : Themes refondu, Wallpaper ajouté, 7 sections (au lieu de 6) |
| `src/apps/settings/theme-details.tsx` | édité : classes Tailwind `text-stone-500` / `text-white` remplacées par `style={{ color: t.textMuted }}` (les seules couleurs dures restantes sont les swatches de prévisualisation, exemptées par la règle) |
| `src/components/Desktop.tsx` | édité : import + overlay wallpaper (lecture de `getWallpaper()`, rien d'autre touché) |

---

## Points non faits / hors scope

- **`src/apps/settings/SettingsItemDetail.tsx`** : déjà exempt de classes Tailwind dures au moment où j'y ai regardé — aucune retente nécessaire.
- **`src/apps/settings/ThemeDetailPage.tsx`** : déjà exempt, idem.
- **`tools/shot.mjs`** : interdit par le brief. Utilisé tel quel.
- **`src/lib/themes/`** (store, tokens) : interdit. La résolution est correcte, l'observation l'a prouvé.
- **`AppFrame.tsx` / `AppDetailOverlay.tsx`** : interdits. La règle « sidebar = app, detail = global » est appliquée par leur mécanisme existant ; je n'ai fait que la documenter côté UI.
- **Persistance Zustand pour le wallpaper** : intentionnellement évitée (cf. commentaire d'en-tête de `src/lib/wallpaper.ts`).
- **Tests dédiés au wallpaper** : non écrits. Le périmètre couvert par les tests existants (`npm test` 60 verts) ne touche pas à ce code. Si on veut verrouiller le resize + les erreurs, c'est une story à part (le helper est conçu pour être testable hors DOM : il suffit de stubber `createImageBitmap`/`OffscreenCanvas`).

---

## Preuves visuelles (récap)

| Capture | Vérifie |
|---------|---------|
| `/tmp/settings-themes.png` | T1 — section Themes, libellé de portée explicite |
| `/tmp/per-app-overrides.png` | T1 — picker par app lisible, nom du thème + actif + canonique |
| `/tmp/settings-wallpaper.png` | T2 — section Wallpaper, état initial |
| `/tmp/settings-wallpaper-with-image.png` | T2 — après upload, preview + Remove + fit |
| `/tmp/desktop-with-wallpaper.png` | T2 — bureau avec le fond personnalisé, papier-jardin remplacé |
| `/tmp/it-rd-cyberpunk.png`, `/tmp/it-rd-editorial.png` | T1 — la résolution marche déjà (preuve observation préalable) |