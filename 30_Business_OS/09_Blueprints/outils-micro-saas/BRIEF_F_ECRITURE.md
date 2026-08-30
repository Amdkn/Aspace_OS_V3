# BRIEF-F — La couche d'écriture, et la fin d'un mensonge

Lis `ANALYSE.md` dans ce dossier. Il fait partie de ce brief.
Lis `GARDE_FOU.md` dans `coach-os-refonte/correctifs/`.

Ton rapport : `RAPPORT_F_ECRITURE.md`, à côté.

---

## Le fait qui déclenche ce chantier

Un agent a prétendu ajouter une tâche. Il n'en avait aucun moyen. Mesuré :

```
src/apps/tasks/TasksApp.tsx   0 affordance de creation
src/lib/cms/cms.store.ts      updateItem seul — pas d'addItem, pas de deleteItem
src/agent/tools.ts            5 outils, 1 seul ecrit (changerTheme)
```

**Coach OS est une vitrine.** Dix-neuf apps qui affichent des données de démonstration, sans
une seule surface où l'on crée. Ni pour un humain, ni pour un agent.

Tant que la couche d'écriture n'existe pas, tout agent à qui l'on demande d'agir **mentira**,
parce que c'est la seule réponse qu'il peut produire.

## Regarde d'abord

`hermes-gratuit/planches/` — les planches-contact. Tu y verras l'anatomie d'un outil, écrite
noir sur blanc dans l'interface :

> « L'onglet existe, Frida est né — il reste à brancher la machinerie : **la table de données,
> le pipeline et la lecture en chat**. »

Et le résultat : « Frida peut maintenant créer ses scènes, les enregistrer, les afficher dans
une galerie. » Trois verbes : créer, enregistrer, afficher.

## Ce qu'on construit

### 1 · Le magasin sait écrire

`src/lib/cms/cms.store.ts` n'a que `updateItem`. Il lui faut `addItem` et `removeItem`, avec
la même rigueur :

- un identifiant généré, pas deviné ;
- les champs obligatoires de la collection respectés — chaque collection déclare déjà son
  `titleField`, son `subtitleField`, son `badgeField` ; sers-t'en plutôt que d'inventer une
  forme par app ;
- l'écriture persiste, comme le reste du magasin.

Regarde comment `updateItem` s'y prend et **suis la même voie**. N'invente pas un second
mécanisme à côté.

### 2 · Tasks sait créer

C'est là que le mensonge s'est produit ; c'est là qu'on commence.

Un bouton d'ajout dans `Today`, un formulaire minimal — titre, échéance — et l'item apparaît
dans la liste. Puis cocher une tâche la marque faite, et l'on peut la supprimer.

**Rien de spectaculaire. Quelque chose qui marche.** Une app qui sait créer une ligne vaut
mieux que dix qui l'annoncent.

Respecte le thème de l'app (`editorial` pour Tasks) et les composants existants — `kit.tsx`,
`widgets.tsx`. Ne fabrique pas un formulaire qui jure avec le reste.

### 3 · L'agent sait écrire — mais il propose

AGENT-D pose en ce moment la couche de scénarios : les outils qui écrivent **déposent une
proposition** au lieu d'agir, et l'utilisateur tranche dans une file d'approbation.

Tes nouveaux outils suivent cette règle. Deux, nommés ainsi :

| outil | ce qu'il fait |
|---|---|
| `creerItem` | dépose la création d'un item dans une collection |
| `modifierItem` | dépose une modification d'un item existant |

Pas de `supprimerItem` dans cette vague : la suppression proposée par un agent demande une
réflexion que ce brief ne porte pas. Dis-le dans ton rapport plutôt que de l'ajouter.

**Coordonne-toi avec ce qui existe.** Si AGENT-D a déjà livré la couche de scénarios, branche
tes outils dessus. Sinon, écris-les de façon à ce que le branchement soit une ligne, et
signale-le. **Ne réécris pas sa couche.**

### 4 · L'agent ne ment plus

Ajoute à l'invite système (`api/_agent/prompt.ts`) une règle explicite, dans ses mots :

> Tu n'annonces jamais une action que tu n'as pas réellement effectuée. Si aucun outil ne te
> permet de faire ce qu'on te demande, tu le dis en une phrase — ce que tu ne peux pas faire,
> et ce que tu peux faire à la place. Une action inventée coûte plus cher qu'un refus.

C'est la correction la plus importante de ce brief, et la moins visible. **Prouve-la** : une
capture où l'on demande à l'agent quelque chose qu'il ne peut pas faire, et où il le dit.

Attention : `api/_agent/prompt.ts` est peut-être en cours de modification par AGENT-D. Si tu
constates un conflit, ajoute ta règle sans écraser la sienne, et dis-le.

## Ton périmètre

```
src/lib/cms/cms.store.ts
src/apps/tasks/**
src/agent/tools.ts
api/_agent/prompt.ts      (ajout seulement, pas de reecriture)
api/_agent/tools.ts       (declaration des deux nouveaux outils)
```

Rien d'autre. **Pas les autres apps** : on prouve le patron sur Tasks, on le généralise
ensuite. Pas de `npm install`.

## Les pièges de cette base, tous payés

- **Un sélecteur Zustand ne rend qu'un scalaire ou une référence déjà stable.** Un tableau
  construit à chaque appel fait boucler React jusqu'à la page blanche. Quatre fois ici.
- **L'état persisté est une entrée non fiable** — répare à la lecture, ne crois pas.
- **`api/` a son propre tsconfig** : `npm run typecheck:api`. Il n'en avait aucun, et `tsc -b`
  rendait « propre » sans rien vérifier.
- **Le serveur ne doit pas croire ce que le client lui renvoie.** L'audit a montré qu'un
  résultat d'outil forgé passe tel quel. N'aggrave pas en donnant des pouvoirs d'écriture sans
  vérification.

## Preuve attendue

Dans `preuves/F/` :

1. Tasks avant — aucun bouton de création ;
2. le formulaire ouvert ;
3. la tâche créée, visible dans la liste ;
4. après rechargement — elle est toujours là ;
5. l'agent à qui l'on demande de créer une tâche : **une proposition apparaît**, la liste n'a
   pas changé ;
6. après approbation : la tâche est là ;
7. **l'agent à qui l'on demande quelque chose d'impossible, et qui le dit.**

La septième est celle qui compte le plus. C'est le défaut d'origine.

`npx vitest run` vert, `npm run typecheck:api` vert, aucune erreur de console.

## Rapport

Fichiers créés, captures, et **« ce que je n'ai pas fait, et pourquoi »**. En particulier :
ce que tu as trouvé de la couche de scénarios d'AGENT-D, et comment tu t'y es branché.
