# BRIEF — resorber la dette de style de l'app `people`

Tu ne changes aucun comportement. Tu remplaces des couleurs codees en dur par les
variables du systeme de theme, pour que l'app suive enfin le theme choisi.

## Le probleme, mesure

L'app `people` porte **74 couleurs hexadecimales** et **124 classes de palette
Tailwind** ecrites en dur. Total : **198 points**.

Consequence visible : changer le theme d'une app ne change qu'une partie de son
apparence. Pire, les pages de detail semblent appartenir a une autre app que
leurs listes — c'est le constat du proprietaire du produit, et c'est ce qu'on
corrige.

Le depot : `C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os`
React 19 · TypeScript · Tailwind v4 · Zustand.

## Le systeme de theme

`src/lib/themes/store.ts` (`applyThemeTokens`) pose ces variables sur la racine
de chaque fenetre. Elles sont ta cible :

| role | variable |
|---|---|
| texte principal | `var(--theme-text)` |
| texte secondaire | `var(--theme-muted)` |
| texte tertiaire | `var(--theme-text-dim)` |
| fond de fenetre | `var(--theme-bg)` |
| fond exterieur | `var(--canvas)` |
| surface de carte | `var(--theme-surface)` · `var(--panel-solid)` |
| survol de surface | `var(--theme-surface-hover)` |
| bordure | `var(--panel-border)` · `var(--theme-border)` |
| bordure discrete | `var(--panel-border-subtle)` · `var(--hairline)` |
| ombre | `var(--shadow-panel)` · `var(--theme-shadow)` |
| accent | `var(--theme-accent)` |
| accent en rgb | `var(--theme-accent-rgb)` (pour `rgba(var(--theme-accent-rgb), .2)`) |

En Tailwind, la notation entre crochets accepte les variables :
`className="bg-[var(--theme-surface)] text-[var(--theme-text)]"`.

## Ce que tu NE dois PAS convertir

C'est la partie la plus importante du brief. Une couleur qui porte un **sens**
n'est pas un choix de style :

1. **Les etats semantiques** — vert = succes, rouge = erreur ou incident, orange
   = avertissement, bleu = information. Un badge « ONLINE » vert doit rester vert
   sur un theme qui n'a pas de vert.
2. **Les previsualisations de theme** — tout composant qui affiche les couleurs
   d'un AUTRE theme que le theme courant (`ThemePreview`, les vignettes de
   `settings`, les demonstrations de `design`). Les convertir casserait leur
   raison d'etre.
3. **Les identites de marque** — le logo, les couleurs propres a un partenaire
   ou a un outil tiers.
4. **Les accents par app** — la constante `ACCENT` en tete de chaque app est
   voulue : c'est l'identite de l'app. Tu ne la touches pas.

En cas de doute : **laisse la couleur et signale-la dans ton rapport.** Une
couleur laissee et signalee vaut mieux qu'un sens detruit.

## Le cas des degrades bâtis sur l'accent

Certains fichiers construisent leurs fonds ainsi :

```
background: `radial-gradient(60% 80% at 50% 0%, ${{accent}}26 0%, transparent 70%)`
```

Ce n'est pas a supprimer — c'est la signature visuelle de l'app. Mais le RESTE
de la page (surfaces, textes, bordures) doit suivre le theme, pour que le
degrade se pose SUR un fond correct au lieu de le remplacer. Verifie qu'une page
de detail et sa liste se ressemblent apres ton passage.


## Le modele de reference : l'app `clients`

Ouvre `src/apps/clients/ClientsApp.tsx` et `ClientsDetailPage.tsx` avant de
commencer. C'est le comportement que le proprietaire du produit veut partout, et
il decoule d'un mecanisme simple qu'il faut comprendre pour ne pas le casser :

- `AppFrame` ecrit les tokens du **theme de l'app** sur son propre `div`. Tout ce
  qu'il contient — la barre laterale et les sections — herite donc de l'identite
  de l'app (Claymorphism pour `clients`), quel que soit le theme global.
- `AppDetailOverlay` est monte **en frere** d'`AppFrame`, pas en enfant. Il ne
  voit pas ces variables et retombe sur `:root`, que `ThemeApplier` regle sur le
  **theme global** — celui de la barre du haut.

Resultat : barre laterale figee sur l'identite de l'app, page de detail qui suit
le theme choisi par l'utilisateur. C'est voulu, c'est bien, et **ta conversion
produit ce comportement automatiquement** : une couleur ecrite en dur ne suit ni
l'un ni l'autre, une variable suit celui de son contexte.

Tu n'as donc RIEN a changer a la structure. Tu remplaces des valeurs, et le bon
comportement apparait tout seul.

**Critere de reussite visuel** : apres ton passage, changer le theme dans la
barre du haut doit changer l'apparence des pages de detail de l'app, sans
toucher a sa barre laterale.

## Verification obligatoire

```
npx tsc --noEmit -p tsconfig.app.json 2>&1 | grep -c "error TS"
npm test
```

La reference est **75 erreurs TS**. Au-dela, tu as introduit une regression.

Puis compte ce qui reste :

```
grep -rEo "#[0-9a-fA-F]{{6}}" src/apps/people --include=*.tsx | wc -l
grep -rEo "\b(bg|text|border)-(white|black|stone|slate|zinc|gray|neutral)(-[0-9]+)?\b" src/apps/people --include=*.tsx | wc -l
```

Rapporte les deux chiffres avant et apres.

## Interdits

0. **N'invoque AUCUN workflow BMAD** (`bmad-spec`, `bmad-build-auto`,
   `bmad-advanced-elicitation`...). Ils ouvrent une porte « [A] Approve » que
   personne ne peut franchir — la session est non interactive. Tu implementes
   directement.
1. Tu ne touches qu'a `src/apps/people/`. Aucune autre app, aucun composant
   partage, aucun fichier de `src/lib/` ou `src/components/`.
2. Tu ne changes **aucun comportement** : pas de logique, pas de structure JSX,
   pas de props. Seulement des valeurs de couleur.
3. N'ajoute aucune dependance. Pas de `git commit`.
4. Ne supprime aucune section, aucune donnee de demonstration.

## Rapport attendu

Les deux comptes avant/apres, la liste des couleurs que tu as **volontairement
laissees** avec la raison de chacune, et tout point non fait avec sa raison.
Un point non fait et signale vaut mieux qu'un point bacle en silence.
