# BRIEF — enrichir l'app `finance`

Tu es un developpeur front. Tu ajoutes des sections a UNE app existante,
avec du contenu structure et une page de detail par element.

**Ton fichier principal** : `src/apps/finance/FinanceApp.tsx`
**Etat actuel** : (lire le fichier pour l'etat exact)
**Accent de l'app** : `#0d9488`

## Ce qu'on corrige

Coach OS a 19 apps qui sont des **coquilles** : trois sections au nom vague, du
contenu de demonstration, aucun modele derriere. Le proprietaire du produit l'a
dit sans detour : « arreter d'avoir des apps basiques dans le projet le plus
ambitieux ».

Soixante-seize conferences ont ete analysees par dix-huit agents pour en tirer
la structure ci-dessous. Ce n'est pas une liste d'idees : c'est ce qui a survecu
a trois filtres — la primitive doit appauvrir les sections existantes si on la
retire, etre portee par au moins deux grappes d'analyse independantes, et
fonctionner pour un expert-comptable comme pour un coach.

**Ton travail : transformer cette structure en sections reelles.**

## Le depot

`C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os`

React 19 · TypeScript · Tailwind v4 · Zustand · Vite. Tests : `npm test`
(vitest + jsdom). Type-check : `npx tsc --noEmit -p tsconfig.app.json` — la
reference est **79 erreurs preexistantes**, ne la depasse pas.

## Le motif d'une app — a suivre exactement

Lis `src/apps/operations/OperationsApp.tsx` en entier avant d'ecrire une ligne.
Tu y verras :

- `const sections: AppSection[] = [{ id, label, icon, render }, ...]` passe a
  `<AppFrame title=... subtitle=... icon=... accent=... sections={sections} />` ;
- des composants de rendu locaux (`Runbooks`, `Knowledge`, `Incidents`) ;
- `CMSCardList` (`src/apps/_ui/CMSCardList.tsx`) pour les grilles de cartes ;
- `registerItemDetail('<appId>', <Composant>)` pour les pages de detail ;
- `useCmsStore` (`src/lib/cms/cms.store.ts`) pour les collections de contenu.

Un exemple de section moderne, deja branchee sur un registre reel :
`src/apps/_ui/ontology/OntologySection.tsx`, utilisee par `it-rd` et
`operations`. Elle montre comment lire une source unique plutot que de recopier
des donnees.

## Regles de contenu — c'est ici que tout se joue

1. **Aucune section vide.** Chaque section rend quelque chose de structure : une
   grille de cartes, un tableau, une liste d'etats. Une section qui affiche
   « bientot disponible » est un echec de cette tache.
2. **Des donnees de demonstration credibles et coherentes**, posees dans un
   fichier `<app>/seed.ts` a part — jamais melangees au composant. Entre 4 et 8
   entrees par section. Elles doivent raconter un metier plausible, pas
   `Lorem ipsum` ni `Item 1 / Item 2`.
3. **Chaque carte ouvre un detail.** Une grille qui ne mene nulle part est une
   image. Utilise le motif `registerItemDetail` deja en place dans l'app.
4. **Variables de theme, jamais de palette Tailwind en dur.** Utilise
   `var(--theme-text)`, `var(--theme-muted)`, `var(--panel-border)`,
   `var(--theme-surface)`, `var(--theme-surface-hover)`. Un epic precedent vient
   de corriger 385 usages ; ne reintroduis pas le defaut. Exception admise : une
   couleur qui porte un SENS (vert = succes, rouge = incident).
5. **Reutilise ce qui existe** — `CMSCardList`, `SectionHead`, les composants de
   `src/apps/_ui/`. N'invente pas un second systeme de cartes.

## Interdits

0. **N'invoque AUCUN workflow BMAD** (`bmad-spec`, `bmad-build-auto`,
   `bmad-advanced-elicitation`, `bmad-party-mode`...). Le depot en contient 46 ;
   ils ouvrent une porte d'approbation « [A] Approve / [E] Edit » que personne ne
   peut franchir ici — la session est non interactive. Tu **implementes
   directement** : tu edites les fichiers, tu verifies, tu rends. N'ecris aucun
   document de specification ; ecris du code.

1. Ne modifie **aucune autre app** que la tienne, ni `src/lib/ontology/`, ni
   `src/components/AppFrame.tsx`, ni `src/lib/app-discovery.ts` (sauf si ta
   tache le dit explicitement).
2. N'ajoute **aucune dependance**.
3. Ne supprime aucune section existante. Tu ajoutes.
4. Pas de `git commit`, pas de `git push`.
5. Ne touche pas a `src/components/canvasui/`.

## Verification obligatoire avant de rendre

```
npx tsc --noEmit -p tsconfig.app.json 2>&1 | grep -c "error TS"
npm test
```

Rapporte les deux chiffres. Si le compte TS depasse **79**, tu as introduit une
regression : corrige-la avant de rendre.

## Rapport attendu

En fin de session, liste : les sections ajoutees, les fichiers crees, les deux
chiffres de verification, et tout point que tu n'as pas pu faire avec la raison.
Un point non fait et signale vaut mieux qu'un point bacle en silence.

## Les sections a ajouter

Ajoute ces **quatre** sections, en gardant toutes les existantes :

- **Plancher de marge** — pas une marge cible, un PLANCHER : le seuil sous lequel
  une prestation ne se vend pas. Chaque offre : son cout reel, son plancher, son
  prix pratique, et l'ecart. Rends visible ce qui passe sous le plancher.

- **Courbe de demande** — des scenarios de prix et leur volume estime. Montre au
  moins trois points par offre pour qu'on voie la pente, pas un chiffre isole.

- **Budget de tokens** — la depense en modeles, comparee au cout des personnes
  qu'elle evite d'embaucher. C'est la metrique qui justifie l'automatisation :
  presente-la comme un rapport, pas comme une facture.

- **Formes de prix** — les differentes manieres de facturer une meme prestation :
  frais d'installation, abonnement, a l'evenement, gratuit en accroche. Chaque
  forme avec ce qu'elle implique en tresorerie et en engagement client.
