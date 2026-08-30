# Les outils micro-SaaS — ce que dit Hugo Buisson

Deux vidéos, un même auteur, deux moitiés d'une seule idée.

- `ZLw7kIgNcQE` — *100 jours avec Hermes Agent résumé en 16 minutes* : l'architecture.
- `RutkqDcQZL0` — *Comment utiliser Hermes GRATUITEMENT à VIE* : la démonstration, avec la
  fabrication d'un outil de bout en bout.

Transcriptions intégrales à côté. Planches-contact dans `hermes-gratuit/planches/`.

---

## Le défaut qui a déclenché tout ça

Un avatar de Coach OS a prétendu ajouter une tâche à Today. **Il a menti.** Vérifié :

- l'app Tasks n'a aucune affordance de création — ni bouton, ni formulaire ;
- le magasin CMS n'expose que `updateItem` : ni `addItem`, ni `deleteItem` ;
- l'agent a cinq outils, dont un seul écrit quoi que ce soit.

Il n'avait aucun moyen d'agir. Il a raconté. C'est le mensonge le plus coûteux, parce qu'on
le croit — et parce que rien à l'écran ne le contredit.

**Coach OS est une vitrine.** Dix-neuf apps qui affichent des données de démonstration, sans
une seule surface où l'on crée, modifie ou supprime quoi que ce soit. Ni pour un humain, ni
pour un agent.

## L'anatomie d'un outil, telle qu'il la formule

La phrase exacte, lue à l'écran dans la vidéo 2 :

> « Ton outil est prêt à être équipé. L'onglet existe, Frida est né — il reste à brancher la
> machinerie : **la table de données, le pipeline et la lecture en chat**. »

Quatre pièces, donc, et pas une de moins :

| pièce | ce que c'est |
|---|---|
| **l'onglet** | une page dans l'app, visible dans la barre latérale |
| **l'agent** | quelqu'un qui la tient — « chaque agent possède son outil » |
| **la table** | une vraie collection où l'on écrit, pas un tableau figé |
| **le pipeline** | ce que l'agent sait exécuter dessus |
| **le chat** | en bas à droite de l'outil, pour lui parler *dans son contexte* |

Et un cinquième élément qui n'est pas décoratif : un **certificat de vérification** que
l'assistant produit avant de rendre la main.

## Ce que ça donne en pratique

L'outil B-roll, fabriqué en cinq minutes : « Frida peut maintenant créer ses scènes, les
enregistrer, les afficher dans une galerie. »

Trois verbes. Créer, enregistrer, afficher. **C'est exactement ce que Coach OS ne sait pas
faire.**

La délégation qui suit vaut d'être notée : il écrit `@Ingrid` — la manageuse — et lui demande
de déléguer. Ingrid appelle l'agent de veille pour récupérer un identifiant, le passe à Frida,
Frida génère, rend la main, **et Ingrid vérifie que le travail est conforme avant de le
valider à l'humain.**

Deux niveaux de contrôle avant l'humain. C'est la même forme que l'approbation de Palantir.

## Ce qu'il dit de l'ontologie, et qui recoupe Palantir

> « L'ontologie, c'est la manière d'organiser les éléments importants de ton activité et de
> faire le lien entre eux. L'agent ne récupère pas seulement une liste, il récupère aussi les
> éléments qui y sont liés. »

Et son procédé pour partir de zéro, qui est le plus actionnable de la vidéo :

> « Demander à l'IA de te poser un certain nombre de questions sur un domaine très précis. Si
> tu lui dis juste "pose-moi des questions sur X", elle va t'en poser, mais elle ne fera
> jamais l'effort de t'interroger à 360°. Pour des petites tâches, 10 à 15 questions. Pour ce
> qui est déterminant, jusqu'à 100. »

Cent questions, quarante minutes à une heure de réponses — puis structuration en Markdown,
réutilisable partout. Il insiste : *« on pense toujours au système de mémoire sans penser
d'abord à l'information qu'on va mettre dedans. »*

## Le modèle par agent

> « Le meilleur modèle, ce n'est pas le plus puissant dans l'absolu. C'est celui qui est juste
> assez puissant pour réaliser la tâche, au coût le plus bas et à la vitesse la plus élevée. »
> « C'est comme prendre un tank pour aller à la boulangerie. »

Son agent de veille tourne sur un modèle bon marché ; sa manageuse, avec qui il discute au
quotidien et qui analyse les statistiques, sur un modèle puissant en raisonnement maximal.

Le socle de Coach OS a déjà la forme qu'il faut — un registre `id → fabrique de modèle` — mais
le choix est **global**. Il devrait être **par agent**.

## OpenRouter — la limite que tu n'as jamais exploitée

Le chiffre exact, en fin de vidéo 2 :

| situation | plafond |
|---|---|
| jamais payé un centime | **50 requêtes/jour** |
| **10 $ déposés une fois, valable à vie** | **1 000 requêtes/jour** |
| dans les deux cas | 20 requêtes/minute |

Tu as déjà des crédits chez OpenRouter. **Tu es donc déjà dans la seconde ligne** — 1 000
requêtes par jour sur les modèles gratuits, sans rien débourser de plus.

Et le **free model router** répond au défaut des modèles gratuits : quand l'un est saturé, il
route la requête vers un autre automatiquement. Sans lui, une requête sur un modèle surchargé
échoue simplement.

Vingt fois plus de requêtes gratuites par jour, sur une somme déjà dépensée. C'est le meilleur
rapport de tout ce document.

## Ce que je retiens pour Coach OS

L'ordre qui tient debout :

1. **La couche d'écriture.** Le magasin CMS doit savoir créer, modifier, supprimer. Sans elle,
   tout le reste est du théâtre — et un agent qui prétend agir continuera de mentir.
2. **Les surfaces.** Une app sans bouton de création n'est pas une app, c'est une capture
   d'écran. Tasks d'abord, puisque c'est là que le mensonge s'est produit.
3. **Les outils d'agent qui écrivent** — et qui déposent dans un scénario plutôt que d'agir,
   puisque c'est ce qu'AGENT-D est en train de poser.
4. **L'agent qui tient l'outil**, avec son chat dans le contexte de l'outil, et son propre
   modèle.
5. **OpenRouter comme cinquième fournisseur**, avec le free model router.

Le point 1 conditionne tous les autres, et c'est celui qui manque depuis le début.
