# BRIEF — l'app Legal, refaite autour de la souverainete

Tu es developpeur front. Ton perimetre exclusif : `src/apps/legal/`.

## Deux choses a faire

**1. Les anciennes pages de detail sont a refaire, pas a retoucher.** Elles
suivent deja le theme de la barre du haut — c'est le seul point acquis. Le
proprietaire les qualifie de « mega basiques ». Applique les cinq points de la
section « Ce qu'est une bonne page de detail ».

**2. Ajoute la couche souverainete.** Elle vient d'une conference d'IndyDevDan,
« Is Anthropic STEALING Your Data? ». La these, resumee sans la trahir :

> Les laboratoires de modeles ne volent pas vos donnees — leurs conditions
> l'interdisent et leurs incitations les en dissuadent. Mais ils les utilisent
> **agregees et anonymisees**, et cet agregat est une **carte du marche**. Quand
> un domaine devient rentable, ils y entrent. Vous payez deux fois : en argent,
> et en savoir-faire.

Le test qu'il propose, et qui doit apparaitre tel quel dans l'app :
**« si un concurrent pouvait lire la trace complete de mon agent, est-ce que ca
changerait quelque chose ? »**

Ajoute ces sections, en gardant les existantes :

- **Echelle de souverainete** — les six niveaux, du moins au plus souverain :
  *Niveau 0* abonnement grand public (Claude, ChatGPT) ;
  *Niveau 1* API commerciale (moins de collecte, agregat seulement) ;
  *Niveau 2* nuage de modeles (Bedrock, Vertex, Foundry — le fournisseur
  s'interpose, plus d'echantillonnage) ;
  *Niveau 3* plan de controle possede (petite machine, passerelle LLM, on possede
  toutes les traces et on change de modele a volonte) ;
  *Niveau 4* hybride prive (poids ouverts sur des GPU loues, on possede le
  modele) ; *Niveau 5* materiel possede.
  Chaque niveau : ce qu'on gagne, ce qu'on garde, ce que ca coute, et pour quelle
  taille d'organisation. **Marque le niveau ou se trouve Coach OS aujourd'hui.**
  L'auteur note lui-meme qu'il hesite sur l'ordre 2 / 3 ; garde son ordre et
  signale l'hesitation plutot que de trancher a sa place.

- **Commodite ou propriete intellectuelle** — un classement des travaux. Le
  travail de commodite (prototypes, CRUD, glue) n'a pas besoin d'etre defendu.
  Le travail d'IP — invites, traces, logique metier, evaluations construites a la
  main, donnees d'usage — est rare, asymetrique, et se cumule. Chaque entree
  porte le verdict du test de la trace.

- **Registre des dependances** — de quels modeles, fournisseurs et services
  depend l'activite, et ce qui tombe si l'un disparait. C'est du risque
  d'homme-cle, applique a la technologie.

- **Clauses et retention** — ce que disent reellement les conditions de service
  qu'on a acceptees : ce qui est conserve, combien de temps, ce qui est exclu de
  l'entrainement, et quelles classes de compte ont quelles protections. L'auteur
  insiste : les classes de clients ne sont pas egales, le commercial est mieux
  protege que le grand public.

**Ne transforme pas ceci en pamphlet.** Le ton de la source est explicitement
non alarmiste : les faits, leurs sources, et la decision laissee au lecteur.
Rends visible ce qui est **verifie** (conditions de service) et ce qui est
**speculation** — l'auteur separe les deux avec soin, fais-en autant.

## Le depot

`C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os`

React 19 - TypeScript - Tailwind v4 - Zustand - Vite.
**Reference TS : 71 erreurs. Ne la depasse pas.** `npm test` : 60 verts.

## La regle de theme — c'est le coeur de cette vague

Un seul motif est correct dans ce depot, celui de `src/apps/clients/ClientsApp.tsx` :

- La **barre laterale** porte l'identite de l'app : theme fige, choisi par l'app.
- La **page de detail** suit le theme de la **barre du haut**, celui que
  l'utilisateur change globalement.

Le mecanisme, a comprendre avant de toucher quoi que ce soit :

`AppFrame` ecrit les jetons du theme de l'app sur **son propre `div`**. Tout ce
qu'il contient en herite. `AppDetailOverlay` est monte **en frere** d'`AppFrame`,
pas dedans : il ne voit pas ces variables, retombe sur `:root`, que
`ThemeApplier` regle sur le theme global. C'est exactement ce qu'on veut.

**Consequence directe : un detail rendu dans le corps d'une section herite du
theme de l'app et ne suivra JAMAIS la barre du haut.** C'est le defaut a
corriger. Il a deja ete corrige deux fois sur d'autres apps ; le motif est connu.

La structure de retour attendue :

```tsx
return (
  <>
    <AppFrame ... sections={sections} />
    {detail ? (
      <AppDetailOverlay appId="<app>" accent={ACCENT} onBack={...}>
        <...DetailPage item={detail} onBack={...} />
      </AppDetailOverlay>
    ) : null}
  </>
);
```

Lis `ClientsApp.tsx` en entier avant d'ecrire une ligne.

## Ce qu'est une bonne page de detail

Le proprietaire du produit est explicite : les anciennes pages de detail sont
**trop basiques pour rester en l'etat**. On ne les met pas a jour, on les
**refait**. Une page de detail digne de ce nom, pour un element d'une collection :

1. **Un en-tete qui situe** — le nom, son etat, son fil d'Ariane, et la date de
   derniere mise a jour. On doit savoir *ou on est* sans lire le corps.
2. **Les attributs structures**, pas un bloc de texte : des paires
   libelle/valeur groupees par sens, lisibles en diagonale.
3. **L'historique** — ce qui s'est passe sur cet element, date par date. Un
   element sans histoire est une fiche morte.
4. **Les relations** — a quoi il est lie, et un lien pour y aller. C'est ce qui
   transforme une collection en systeme.
5. **Ce qu'on peut en faire** — les actions possibles, meme si elles ne sont pas
   toutes cablees. Une page qui ne mene nulle part est une image.

`src/apps/clients/ClientsDetailPage.tsx` est la reference vivante.

## Les deux chiffres durs

1. `node tools/shot.mjs --app <app> --out /tmp/x.png` ne remonte **aucune erreur
   de console**. Le script ouvre l'app, pose le theme, capture, et liste les
   erreurs. Le selecteur `--section` fonctionne sur le **libelle** affiche.
   **Regarde tes captures.** Le typage vert et les tests verts ne prouvent rien
   sur ce qui s'affiche : trois fois cette semaine du code casse a ete valide
   pour cette raison exacte.
2. **Zero classe de palette Tailwind en dur** dans ton perimetre :
   `bg-white`, `text-stone-900`... Uniquement `var(--theme-text)`,
   `var(--theme-surface)`, `var(--panel-border)`, `var(--theme-muted)`.
   Exception : une couleur qui porte un **sens** (vert = ok, rouge = incident,
   orange = avertissement).

## Interdits

0. **N'invoque AUCUN workflow BMAD** (`bmad-spec`, `bmad-build-auto`...). Le
   depot en contient 51 ; ils ouvrent une porte « [A] Approve » que personne ne
   peut franchir — la session est non interactive et tu resterais bloque.
1. **Ne modifie AUCUN fichier sous un dossier `_TRASH_*`.** Ce sont des archives,
   c'est le chemin de retour arriere. Un agent a vide l'une d'elles pour faire
   tomber un compteur a zero : la mesure est devenue verte parce que la preuve
   avait disparu. Les comptages excluent ces dossiers, tu n'as rien a y gagner.
2. **N'ecris jamais dans le magasin de themes** (`setAppTheme`, `setGlobalTheme`).
   Cela ecrase le choix de l'utilisateur dans Settings. Le defaut d'une app se
   declare dans `CANONICAL_APP_THEMES` (`src/lib/themes/tokens.ts`), et un choix
   explicite de l'utilisateur doit toujours gagner.
3. Tu ne touches pas a `src/components/AppFrame.tsx`, ni a
   `src/components/cms/AppDetailOverlay.tsx`, ni a `tools/shot.mjs`.
4. Aucune dependance nouvelle. Pas de `git commit`, pas de `git push`.
5. Tu ne supprimes aucune section existante.
6. Chemins **absolus** pour tout fichier ecrit hors du depot.

## Verification obligatoire

```
npx tsc --noEmit -p tsconfig.app.json 2>&1 | grep -c "error TS"
npm test
grep -rEo "\b(bg|text|border)-(white|black|stone|slate|zinc|gray|neutral)(-[0-9]+)?\b" src/apps/<app> --include=*.tsx | grep -v _TRASH | wc -l
```

Attendu : **au plus 71**, tests verts, **0 erreur de console**, **0 classe de
palette hors corbeille**.

## Rapport attendu

Dans `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/RAPPORT_LEGAL.md`.

Par app : la structure de retour finale, les pages de detail refaites, les
captures que tu as prises et ce que tu y as vu, les chiffres de verification, et
**tout point non fait avec sa raison**. Un point non fait et signale vaut mieux
qu'un point bacle en silence.

Si tu dois t'arreter avant la fin, ecris quand meme ce rapport avec l'etat exact.
