# BRIEF — Settings : themes de barre laterale et fond d'ecran

Tu es developpeur front. **Perimetre exclusif : `src/apps/settings/`**, plus
`src/components/Desktop.tsx` uniquement pour la lecture du fond (tache 2).
Tu ne touches a aucune autre app.

## Le depot

`C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os`

React 19 · TypeScript · Tailwind v4 · Zustand · Vite.
**Reference TS : 67 erreurs. Ne la depasse pas.** `npm test` : 60 verts.

---

# Tache 1 — la surcharge par app gouverne la BARRE LATERALE

## Ce qui a change hier, et qu'il faut refleter

Une regle de theme vient d'etre etablie dans tout le depot :

- la **barre laterale** d'une app porte l'identite de cette app ;
- la **page de detail** suit le theme **global**, celui de la barre du haut.

Le mecanisme : `AppFrame` ecrit les jetons du theme de l'app sur son propre
`div` — barre laterale et sections en heritent. `AppDetailOverlay` est monte en
**frere** d'`AppFrame` : il ne voit pas ces variables, retombe sur `:root`, que
`ThemeApplier` regle sur le theme global.

**Consequence : la section « Per-app override » de Settings ne gouverne plus
qu'une seule chose, la barre laterale.** L'interface ne le dit pas. Elle annonce
« Pick a theme per business-domain app », ce qui laisse croire qu'elle change
toute l'app.

## Le probleme concret du proprietaire

Il veut pouvoir **changer manuellement le theme de la barre laterale d'IT / R&D**,
aujourd'hui figee sur Cyberpunk, sans toucher au reste.

La resolution est deja correcte dans `src/lib/themes/store.ts` :

```
resolveTheme(appId) = appThemes[appId] ?? CANONICAL_APP_THEMES[appId] ?? globalTheme
```

Un choix explicite **gagne** sur le defaut canonique. Donc si changer IT ne
fonctionne pas, la cause est dans l'interface ou dans la propagation, **pas dans
la resolution**. Trouve-la, ne reecris pas le magasin.

## Ce que tu fais

1. **Verifie d'abord que ca marche.** Serveur de dev, Settings > Themes, change
   IT / R&D pour autre chose que Cyberpunk, ouvre IT / R&D, et **regarde**.
   Rapporte ce que tu observes **avant** de corriger quoi que ce soit. Le defaut
   est peut-etre ailleurs que la ou tu l'attends.

2. **Rends la portee explicite.** Le libelle doit dire ce que la surcharge fait
   vraiment : elle habille **la barre laterale et les sections de l'app**. Et
   rappeler en une ligne que **les pages de detail suivent la barre du haut** —
   c'est voulu, et un utilisateur qui l'ignore croira le reglage casse.

3. **Rends la selection utilisable.** La rangee actuelle est un carrousel de
   pastilles minuscules avec des fleches : on ne distingue ni le nom du theme ni
   sa couleur. Chaque app doit permettre de choisir de facon lisible, avec le
   theme **actif** visible sans survol et le **defaut canonique** indique — pour
   qu'on sache quand on s'en ecarte.

4. **Un retour au defaut** par app. `resetAppTheme(appId)` existe deja dans le
   magasin. Ne le reecris pas.

5. **N'ecris jamais dans le magasin en dehors d'une action utilisateur.** Pas
   d'`useEffect` qui appelle `setAppTheme` au montage : un agent l'a fait hier
   dans une autre app, cela ecrasait le choix de l'utilisateur a chaque
   ouverture, il a fallu l'annuler.

---

# Tache 2 — une page « Fond d'ecran » dans Settings

Ajoute une **nouvelle section** a la barre laterale de Settings. Les six
actuelles — General, Themes, Canvas FX, Privacy, Integrations, Help — restent
toutes. Elle permet de **televerser une image qui devient le fond du bureau**.

## Contraintes reelles

1. **Aucun serveur, aucun stockage distant.** L'image vit dans le navigateur.
   Le chemin le plus simple qui tienne : `FileReader`, conversion en `data:` URL,
   persistance dans `localStorage`.

2. **`localStorage` plafonne autour de 5 Mo, et une photo le depasse.** C'est le
   vrai risque de cette tache. **Redimensionne avant de stocker** : passe l'image
   dans un `<canvas>`, borne sa plus grande dimension (2560 px suffit largement
   pour un fond), reexporte en `image/jpeg` a une qualite raisonnable. Et **gere
   l'echec explicitement** : si l'ecriture leve `QuotaExceededError`, dis-le en
   clair a l'utilisateur — ne perds pas son image en silence.

3. **Ne mets pas l'image dans le magasin de themes.** Il est persiste avec un
   `partialize` ; y injecter une data URL de plusieurs mega-octets casserait la
   rehydratation de tous les themes. Utilise une cle `localStorage` dediee et un
   petit helper autonome. `src/lib/demoShell.ts` montre deja ce motif avec son
   drapeau `hasSeenCitadel`, et son commentaire d'en-tete explique pourquoi cette
   separation existe.

4. **`src/components/Desktop.tsx` rend le fond.** Tu peux l'editer, mais
   **au minimum** : lis la cle, applique l'image si elle existe, garde le fond
   actuel sinon. Ne touche a rien d'autre dans ce fichier.

5. La page doit permettre : **televerser**, **previsualiser**, choisir le
   **cadrage** (couvrir / contenir / repeter), et **revenir au fond d'origine**.
   Le retour en arriere n'est pas optionnel : sans lui, une image ratee est
   definitive.

---

## Les deux chiffres durs

1. `node tools/shot.mjs --app settings --out /tmp/s.png` ne remonte **aucune
   erreur de console**. Le selecteur `--section` fonctionne sur le **libelle**.
   **Regarde tes captures.** Le typage vert et les tests verts ne prouvent rien
   sur ce qui s'affiche : trois fois cette semaine du code casse a ete valide
   pour cette raison exacte.
2. **Zero classe de palette Tailwind en dur** dans `src/apps/settings`.
   Uniquement `var(--theme-text)`, `var(--theme-surface)`, `var(--panel-border)`,
   `var(--theme-muted)`. Exception : une couleur qui porte un **sens**, et les
   pastilles de previsualisation, qui doivent evidemment afficher les couleurs
   d'AUTRES themes que le theme courant.

## Interdits

0. **Aucun workflow BMAD.** Ils ouvrent une porte « [A] Approve » infranchissable
   en session non interactive.
1. **Ne modifie aucun fichier sous un dossier `_TRASH_*`.** Ce sont des archives.
   Un agent en a vide une pour faire tomber un compteur ; la mesure est devenue
   verte parce que la preuve avait disparu.
2. Tu ne touches pas a `src/lib/themes/` (ni `store.ts`, ni `tokens.ts`), ni a
   `src/components/AppFrame.tsx`, ni a `AppDetailOverlay.tsx`, ni a
   `tools/shot.mjs`.
3. Aucune dependance nouvelle — ni bibliotheque de recadrage, ni de televersement.
   Le navigateur sait tout faire ici.
4. Pas de `git commit`, pas de `git push`. Chemins absolus hors depot.

## Verification obligatoire

```
npx tsc --noEmit -p tsconfig.app.json 2>&1 | grep -c "error TS"
npm test
node tools/shot.mjs --app settings --out /tmp/settings.png
grep -rEo "\b(bg|text|border)-(white|black|stone|slate|zinc|gray|neutral)(-[0-9]+)?\b" src/apps/settings --include=*.tsx | grep -v _TRASH | wc -l
```

Attendu : **au plus 67**, tests verts, **0 erreur de console**, **0 classe de
palette hors corbeille**.

**Et la verification qui compte vraiment** : change le theme d'IT / R&D depuis
Settings, ouvre IT / R&D, capture. Puis televerse une image, capture le bureau.
Deux preuves visuelles, pas deux affirmations.

## Rapport

`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/RAPPORT_SETTINGS.md`

Ce que tu as observe **avant** de corriger (tache 1, point 1), la cause reelle si
elle differait de l'hypothese, ce que tu as construit, tes captures et ce que tu
y as vu, les chiffres, et **tout point non fait avec sa raison**.

Si tu dois t'arreter avant la fin, ecris quand meme ce rapport.
