# BRIEF — les pages de detail de `finance` et `operations` ne s'ouvrent jamais

Le diagnostic est fait. Tu n'as pas a le refaire : tu appliques la correction et
tu la verifies.

## Le depot

`C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os`

React 19 · TypeScript · Tailwind v4 · Zustand · Vite.
Tests : `npm test`. Typage : `npx tsc --noEmit -p tsconfig.app.json` — la
**reference est 75 erreurs preexistantes**, ne la depasse pas.

## Le defaut, precisement

`useCollectionDrill` (`src/hooks/useCollectionDrill.ts`) ne rend **rien**. Il
retourne seulement `{ openId, open, close }` et pose un fil d'Ariane dans le
contexte de fenetre. C'est a l'app de rendre le detail quand `openId` est
renseigne.

Mesure sur les cinq apps :

| app | drills declares | lectures de `.openId` |
|---|---:|---:|
| `it-rd` | 7 | 8 |
| `growth` | 6 | 8 |
| `product` | 6 | 8 |
| **`operations`** | **7** | **0** |
| **`finance`** | **5** | **0** |

`finance` et `operations` montent leur `AppDetailOverlay` sur un etat **local**
`detail`, herite du flux d'origine, que les drills ne renseignent jamais. Le clic
ouvre le drill, le fil d'Ariane apparait, et aucun contenu ne s'affiche.

C'est pour cela que dans `finance` seule la section `Invoices` fonctionne : elle
passe par l'ancien chemin. Les quatre nouvelles — Planchers, Courbes, Tokens,
Formes — sont mortes. Idem dans `operations` pour Processus, Benchmarks,
Changements et Alertes.

## Ce qui existe deja et qu'il ne faut PAS recreer

- `FinanceItemDetail` (`src/apps/finance/FinanceItemDetail.tsx`) route deja
  correctement : `plancher_marges` -> `PlancherDetail`, `courbe_demande` ->
  `CourbeDetail`, `budget_tokens` -> `BudgetTokensDetail`, `formes_prix` ->
  `FormesPrixDetail`, `invoices` -> `InvoiceDetail`.
- `OperationsItemDetail` joue le meme role pour `operations`.
- Les deux sont enregistres via `registerItemDetail('<appId>', ...)`.
- Les collections sont bien enregistrees dans le magasin CMS
  (`seedFinanceCms()`, `seedOperationsCms()`), avec les bons identifiants.

**Le code de destination existe. Seul le declencheur manque.**

## Ta tache

Dans `src/apps/finance/FinanceApp.tsx` et
`src/apps/operations/OperationsApp.tsx` : rendre le detail quand un drill est
ouvert.

**Prends modele sur `src/apps/it-rd/ItRdApp.tsx`**, qui le fait deja
correctement — lis-le en entier avant d'ecrire une ligne, et reproduis son
motif. Ne l'invente pas, ne le modifie pas.

Contraintes :

1. **Ne casse pas `Invoices`** dans `finance`, ni `Runbooks` / `Knowledge Base` /
   `Incidents` dans `operations`. Ces sections fonctionnent aujourd'hui ; elles
   doivent fonctionner apres. C'est le principal risque de cette tache.
2. Le detail doit s'afficher dans `AppDetailOverlay`, comme partout ailleurs.
3. Le bouton retour doit ramener a la liste, et le fil d'Ariane suivre.
4. **Variables de theme uniquement** — `var(--theme-text)`, `var(--theme-muted)`,
   `var(--panel-border)`, `var(--theme-surface)`. **Aucune classe de palette
   Tailwind en dur** (`bg-white`, `text-stone-900`, `border-stone-100`...). Un
   agent precedent en a introduit 13 et elles etaient illisibles sur les themes
   sombres.
5. Ne touche a **aucune autre app**, ni a `src/hooks/useCollectionDrill.ts`, ni a
   `src/components/AppFrame.tsx`, ni a `src/components/cms/AppDetailOverlay.tsx`.

## Interdits

0. **N'invoque AUCUN workflow BMAD** (`bmad-spec`, `bmad-build-auto`,
   `bmad-advanced-elicitation`...). Le depot en contient 46 ; ils ouvrent une
   porte « [A] Approve / [E] Edit » que personne ne peut franchir — la session
   est non interactive. Tu **implementes directement** : tu edites, tu verifies,
   tu rends. N'ecris aucun document de specification.
1. N'ajoute aucune dependance.
2. Ne supprime aucune section.
3. Pas de `git commit`, pas de `git push`.

## Verification obligatoire

```
npx tsc --noEmit -p tsconfig.app.json 2>&1 | grep -c "error TS"
npm test
```

Rapporte les deux chiffres. Au-dela de **75** erreurs TS, tu as introduit une
regression : corrige-la avant de rendre.

## Rapport attendu

Le motif que tu as repris de `it-rd`, les lignes modifiees dans chaque app, les
deux chiffres de verification, et la liste des sections que tu as testees comme
fonctionnant encore (`Invoices`, `Runbooks`, `Knowledge Base`, `Incidents`).
Un point non fait et signale vaut mieux qu'un point bacle en silence.
