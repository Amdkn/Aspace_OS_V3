# BRIEF-D — Les scénarios : l'agent propose, il n'agit plus

Lis `ANALYSE_PALANTIR.md` dans ce dossier. Il fait partie de ce brief.
Lis `GARDE_FOU.md` dans `coach-os-refonte/correctifs/`.

Ton rapport : `RAPPORT_D_SCENARIOS.md`, à côté.

---

## Regarde d'abord, lis ensuite

`palantir-ontologie/planches/` — six planches-contact de la démo. **Ouvre-les.** Une démo
produit se lit à l'écran, pas dans les mots ; trois fois cette semaine un chantier a été mené
à l'aveugle faute de le faire.

Ce que tu y verras, et qui est le modèle à transposer :

- le tableau de programmation, avec les créneaux déplacés en couleur ;
- **trois cartes d'options comparées** côte à côte — « Best Surgeon Match », « Balanced for
  Fit & Flow », « Least Schedule Impact » — chacune avec ses métriques et son coût en
  changements ;
- l'onde vocale à droite pendant que l'agent écoute ;
- le bouton **Submit for Approval** ;
- puis la vue administrateur : une file **Scenario Requests**, un scénario nommé « Patricia
  Emergency case », et **Approve & Merge**.

La transcription intégrale est dans `transcription-palantir.md`.

## Le problème qu'on corrige

Les cinq outils de Coach OS **agissent immédiatement**. `changerTheme` change le thème,
`ouvrirApp` ouvre l'app. Un agent qui se trompe a déjà agi.

Et l'audit de sécurité vient d'établir deux choses qui rendent ça intenable :

- un contenu du CMS peut donner des instructions à l'agent (injection par le contenu) ;
- un client peut **forger un résultat d'outil** que le serveur relaie tel quel au modèle.
  Vérifié : un faux `lireCollection` annonçant 1 client au lieu de 6 a fait répondre « Tu as
  1 client ».

Un agent détourné qui travaille dans un bac à sable ne casse rien. C'est la vraie raison
d'être de ce chantier — pas l'élégance.

## Ce qu'on construit

### 1 · Le scénario

Un **bac à sable persistant** : un jeu de modifications proposées, nommé, qui survit à la
fermeture, et qui n'écrit pas dans les données réelles.

> « Ces scénarios ne sont pas éphémères. Je peux faire le tour des urgences et revenir les
> modifier. Et ils ne touchent pas les données de production. »

Concrètement pour Coach OS : les outils qui **écrivent** cessent d'écrire directement. Ils
déposent une **proposition** dans le scénario courant. Les outils qui **lisent** continuent de
lire les données réelles.

Aujourd'hui seul `changerTheme` écrit. Mais l'architecture doit accueillir les écritures à
venir — créer une tâche, modifier un client — sans être rouverte. Conçois la couche, ne
l'invente pas app par app.

`ouvrirApp` et `allerASection` ne sont pas des écritures : ce sont des gestes de navigation,
ils restent immédiats. Sépare clairement les deux natures et dis pourquoi dans le code.

### 2 · La comparaison

Quand l'agent propose plusieurs voies, il les montre **côte à côte**, avec ce qui les
distingue — pas un paragraphe de prose.

C'est ce que fait la démo : trois cartes, et une phrase qui tranche (« B convient le mieux,
trois déplacements de moins »). Puis l'infirmière demande *« quelle est la différence entre A
et B ? »* et obtient une réponse comparative, pas une redite.

### 3 · La file d'approbation

Celui qui propose n'est pas celui qui engage.

> « Je ne veux pas être celle qui fusionne en production, parce que mon rôle est d'être sur le
> terrain. »

Une file où chaque scénario en attente se voit, s'ouvre, **s'édite encore**, et se fusionne ou
se rejette. L'administrateur de la démo ne valide pas en bloc : il déplace un patient de plus
avant de fusionner.

Coach OS **annonce déjà ce geste** dans People / Agents : « You approve in 10 min · Yes or no
on the queue. Ship or kill. Move on. » La page le raconte, elle ne le fait pas. Fais-le.

Place la file là où elle a du sens — la section Agents de People, ou une section dédiée. Juge,
et justifie.

### 4 · Tout ou rien

> « J'annule l'infirmière, j'annule la préparation de salle, mais l'appel qui annule le
> médecin échoue. Maintenant j'ai un médecin affecté à un rendez-vous qui n'existe plus. »

La fusion d'un scénario est **atomique** : toutes les modifications passent, ou aucune. Un
échec au milieu ne laisse pas un état que personne n'a voulu.

Coach OS a déjà ce défaut en germe : `allerASection` ouvre l'app **puis** clique la section ;
si le clic échoue, l'app reste ouverte sur autre chose. Corrige-le au passage, ou explique
pourquoi tu ne le fais pas.

## Ton périmètre

```
src/agent/**
src/stores/**            (nouveau magasin de scénarios)
src/apps/people/**       (la file d'approbation, si tu la places là)
api/_agent/**
```

Pas de `npm install`, pas de verrou touché. Le déploiement Vercel a déjà été cassé deux fois
cette semaine par des changements de configuration.

## Les pièges de cette base, tous payés

- **Un sélecteur Zustand ne rend qu'un scalaire ou une référence déjà stable.** Un tableau
  construit à chaque appel fait boucler React jusqu'à la page blanche. Quatre fois ici.
- **L'état persisté est une entrée non fiable.** Une valeur forgée dans `localStorage` doit
  être réparée à la lecture, pas crue.
- **Borne toute position contre la fenêtre**, au montage et au redimensionnement.
- **`api/` a son propre tsconfig** (`npm run typecheck:api`). Il n'en avait aucun, et
  `tsc -b` rendait « propre » sans rien vérifier.

## Preuve attendue

Des captures, dans `preuves/D/` :

1. l'agent propose une modification — **rien n'a changé** dans les données ;
2. deux options comparées côte à côte ;
3. la file d'approbation avec un scénario en attente ;
4. le scénario édité par l'approbateur **avant** fusion ;
5. après fusion : la modification est appliquée ;
6. une fusion dont une étape échoue : **aucune** modification n'est appliquée.

La sixième est la plus importante et la plus facile à escamoter. Provoque l'échec, ne le
simule pas dans un commentaire.

`npx vitest run` reste vert, `npm run typecheck:api` reste vert, aucune erreur de console.

## Rapport

Fichiers créés, captures, et **« ce que je n'ai pas fait, et pourquoi »**. Si tu juges qu'une
des quatre idées ne se transpose pas à Coach OS, dis-le et argumente — c'est une réponse
recevable, l'imitation aveugle ne l'est pas.
