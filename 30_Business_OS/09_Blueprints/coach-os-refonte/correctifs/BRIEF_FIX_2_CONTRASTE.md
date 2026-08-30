# FIX-2 — Les titres illisibles

Lis d'abord `COMMUN.md`, dans ce même dossier. Il fait partie de ce brief. **Sa section sur
l'erreur de diagnostic du rapport QA C te concerne directement** : ne va pas déterrer les
thèmes par app.

Ton rapport : `correctifs/RAPPORT_FIX_2.md`

---

## Ce que la QA a trouvé

Vingt-cinq défauts, tous de la même forme : un texte rendu dans une couleur trop proche de son
fond. Sombre sur sombre le plus souvent.

### it-rd — 14 défauts, les deux thèmes

Les sept sections (`Kernel`, `Experiments`, `Deploys`, `Journal`, `Boucles`, `Drift`, `Evals`)
ont leur titre « quasi invisible », sous `warm-paper` **et** sous `dark-oled`.

C'est le cas le plus net : `it-rd` porte le thème `cyberpunk`, qui est un thème sombre. Le
titre est illisible **dans son propre thème**, indépendamment du réglage global. Rien à voir
avec une cascade de thème — la palette cyberpunk pose un titre sombre sur un fond sombre.

À noter : la section `Ontology` de la même app a été jugée saine, « titre rouge lisible sur
fond sombre ». Elle te donne la couleur qui marche dans ce thème.

### ontology — 4 défauts, thème sombre

`Entities`, `Relations`, `Contracts`, `Versions` : titres, sous-titres, libellés de listes
déroulantes et descriptions de cartes en teal sombre sur fond noir. Les badges et les
compteurs restent lisibles — ils utilisent des variables de thème plus claires. **Ta réponse
est là** : aligne ce qui est illisible sur ce qui l'est déjà.

`ontology` n'a pas d'entrée dans `CANONICAL_APP_THEMES`, elle hérite donc du thème global.
Sous `dark-oled`, tout doit être lisible.

### onboarding — 1 défaut, thème sombre

Le citadel (étape 1/4) : titre `STEP 1 OF 4 · CAPTURE`, question, sous-titre, options radio,
lien `← Back`, barres de progression — tout en teal sombre sur fond quasi noir. Le panneau
droit `YOUR FUTURE DEMO INSTANCE` et ses quatre tuiles sont dans le même état.

### dashboard — hors périmètre

Wind Direction, Client Pipeline et CEO Cockpit ont aussi des titres peu contrastés. **Ils
appartiennent à FIX-1**, qui possède `src/apps/dashboard/`. N'y touche pas.

## La méthode

Regarde d'abord **comment le thème définit ses couleurs de texte** dans
`src/lib/themes/tokens.ts` : il y a un jeu de variables (`--theme-text`, `--theme-text-dim`,
et d'autres — lis le fichier, ne devine pas les noms). Un titre de section doit prendre la
variable la plus contrastée du thème, pas une couleur Tailwind figée.

La question à poser devant chaque défaut : *est-ce que ce texte utilise une variable de thème,
ou une couleur en dur ?*

- **Couleur en dur** (`text-stone-400`, `text-teal-800`…) → remplace-la par la variable.
  C'est la cause la plus probable et le correctif le plus propre.
- **Variable de thème, mais la variable elle-même est trop sombre** → là tu touches à la
  palette. Prudence : `tokens.ts` sert toutes les apps. Un test de garde existe
  (`src/lib/themes/orphan-css-vars.test.ts`) et doit rester vert. Si tu dois modifier une
  valeur de palette, dis-le explicitement dans ton rapport avec la valeur avant et après.

Un critère chiffré vaut mieux qu'un jugement à l'œil : vise **4,5:1** de rapport de contraste
pour le corps de texte, **3:1** pour les gros titres (WCAG AA). Tu peux extraire les paires
couleur/fond depuis le DOM avec `page.evaluate` plutôt que de juger sur un PNG — c'est
exactement ce que le testeur QA a dit ne pas avoir pu faire.

## Ton périmètre exclusif

```
src/apps/it-rd/**
src/apps/ontology/**
src/apps/_ui/ontology/**
src/apps/onboarding/**
src/lib/themes/tokens.ts          (palette uniquement, PAS CANONICAL_APP_THEMES)
```

Rien d'autre. Pas `src/apps/dashboard/`, pas `src/apps/_ui/FleetItemCard.tsx`, pas
`src/components/`.

`tokens.ts` est partagé et personne d'autre n'y écrit dans cette vague — mais chaque valeur
que tu y changes se propage à dix-neuf apps. Touche-y en dernier recours, et prouve par
captures que les apps voisines n'ont pas bougé.

## Preuve attendue

Une capture avant / après par section listée, sous le thème où le défaut apparaît, dans
`correctifs/preuves/fix2/`. Pour `it-rd`, les deux thèmes, puisque le défaut est présent sur
les deux.

Si tu as modifié `tokens.ts`, ajoute une capture de contrôle pour `people`, `sales`, `clients`
et `legal` — quatre thèmes différents — sous `warm-paper` et `dark-oled`.

Et lance `npx vitest run src/lib/themes/` : le test de garde des variables CSS orphelines doit
rester vert.
