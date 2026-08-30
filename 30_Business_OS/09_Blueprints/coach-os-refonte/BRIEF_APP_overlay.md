# BRIEF — les pages de detail doivent suivre le theme de la barre du haut

Le diagnostic est fait. Tu appliques la correction et tu la verifies.

## Le depot

`C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os`

React 19 · TypeScript · Tailwind v4 · Zustand.
Reference TS : **75 erreurs preexistantes**. Ne la depasse pas.

## Le mecanisme, a comprendre avant de toucher quoi que ce soit

Deux emplacements possibles pour une page de detail, et ils n'heritent pas du
meme theme :

- **Dans `AppFrame`** — `AppFrame` ecrit les tokens du **theme de l'app** sur son
  propre `div`. Tout ce qu'il contient herite donc de Editorial, Claymorphism,
  Cyberpunk… selon l'app.
- **En frere d'`AppFrame`** — `AppDetailOverlay` est monte a cote, pas dedans. Il
  ne voit pas ces variables et retombe sur `:root`, que `ThemeApplier` regle sur
  le **theme global**, celui de la barre du haut.

Le comportement voulu par le proprietaire du produit, et deja obtenu par
`clients` : **barre laterale figee sur l'identite de l'app, page de detail qui
suit le theme de la barre du haut.**

## Le defaut

`people` et `finance` rendent leurs details via `DynamicPageView` **dans le corps
d'une section**, donc a l'interieur d'`AppFrame`. Leurs details heritent du theme
de l'app — Editorial pour `people`, Trust and Authority pour `finance`, tous deux
clairs. Resultat : en theme global Cyberpunk (sombre), ces deux apps restent
blanches alors que `clients` et `growth` suivent.

Compte actuel de `DynamicPageView` rendus dans une section :
`people` **6**, `finance` **5**. `clients` en a **0** — c'est le modele.

## Ta tache

Dans `src/apps/people/PeopleApp.tsx` et `src/apps/finance/FinanceApp.tsx` :
faire passer ces details par `AppDetailOverlay`, monte **en frere** d'`AppFrame`,
au lieu de les rendre dans le corps des sections.

**Prends modele sur `src/apps/clients/ClientsApp.tsx`** — lis-le en entier avant
d'ecrire une ligne. Sa structure de retour est :

```
return (
  <>
    <AppFrame ... sections={sections} />
    {detail ? (
      <AppDetailOverlay appId="clients" accent={ACCENT} onBack={...} motion={...}>
        <ClientsDetailPage item={detail} onBack={...} />
      </AppDetailOverlay>
    ) : null}
  </>
);
```

Les deux apps ont **deja** un `AppDetailOverlay` monte de cette facon pour leur
flux d'origine (`Invoices` dans finance, `Squads` dans people). Tu dois faire
converger les drills des nouvelles sections vers ce meme calque, pas en creer un
second.

Le composant a rendre dans le calque reste le meme : `DynamicPageView` avec son
`collectionId`, son `itemId`, son `onBack` et son `onNavigate`. Seul son
EMPLACEMENT dans l'arbre change.

## Contraintes

1. **Ne casse rien de ce qui marche.** Dans `finance` : `Invoices`. Dans
   `people` : les sept sections d'origine, et surtout `Squads`, dont le detail
   passe par `selectedCode` et `FleetDetail` — un mecanisme different, a ne pas
   toucher.
2. La barre laterale doit rester interactive quand un detail est ouvert. Elle
   l'est deja : `AppDetailOverlay` demarre a `left: var(--sidebar-w, 0px)`.
3. Le fil d'Ariane doit continuer de refleter la section et l'element ouvert.
4. **Aucune classe de palette Tailwind en dur** (`bg-white`, `text-stone-900`…).
   Une campagne vient d'en retirer 437 ; ne les reintroduis pas.
5. Ne touche a **aucune autre app**, ni a `src/components/AppFrame.tsx`, ni a
   `src/components/cms/AppDetailOverlay.tsx`, ni a `src/hooks/useCollectionDrill.ts`.

## Interdits

0. **N'invoque AUCUN workflow BMAD** (`bmad-spec`, `bmad-build-auto`…). Ils
   ouvrent une porte « [A] Approve » que personne ne peut franchir — la session
   est non interactive. Tu implementes directement.
1. N'ajoute aucune dependance. Pas de `git commit`.
2. Ne supprime aucune section, aucune donnee de demonstration.

## Verification obligatoire

```
npx tsc --noEmit -p tsconfig.app.json 2>&1 | grep -c "error TS"
npm test
grep -c "DynamicPageView" src/apps/people/PeopleApp.tsx
grep -c "DynamicPageView" src/apps/finance/FinanceApp.tsx
```

Les deux derniers comptes doivent avoir baisse : les `DynamicPageView` ne sont
plus dans le corps des sections mais dans le calque.

## Rapport attendu

La structure de retour finale de chaque app, les sections dont tu as verifie
qu'elles fonctionnent encore, les chiffres de verification, et tout point non
fait avec sa raison.
