---
type: Playbook
title: primitives — ce que la session ontologie construit, ce que les boucles consomment
description: Verrou à jetons partagé entre toutes les boucles d'agents du poste, avec battement de cœur. Deux défauts reproduits puis corrigés, neuf tests au vert.
tags: [primitives, verrou, concurrence, agents, jetons, mkdir]
generated: { by: claude-opus-5, at: 2026-08-19T03:00:00Z }
verified:
  - { by: process:test-jetons-9-cas, at: 2026-08-19T03:00:00Z }
sources:
  - id: implementation
    resource: 60_Implementation_Méthodologiques/primitives/jetons.sh
    title: Le verrou à jetons
    last_modified: 2026-08-19
  - id: tests
    resource: 60_Implementation_Méthodologiques/primitives/test_jetons.sh — 9 cas, 9 au vert
    author: process:test-jetons-9-cas
    last_modified: 2026-08-19
  - id: origine
    resource: 60_Implementation_Méthodologiques/_loop/slots.sh — première version, écrite par la session Coach OS
    title: La version dont celle-ci part
    last_modified: 2026-08-19
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Chaque affirmation de cette
> page correspond à un cas de test exécuté, pas à une lecture du code.

# À quoi sert ce dossier

La session **ontologie** construit les primitives ; les boucles d'agents les
consomment. C'est le partage de corridor décidé le 2026-08-19.

Une primitive remise à une autre session sans avoir été testée est une
promesse, pas une primitive.

# Le verrou à jetons

## Le problème, bien posé dès la première version

`ps -W | grep -c node.exe` compte **déjà** tous les processus de la machine :
le compteur était partagé de fait. Ce qui manquait n'était pas un compteur,
c'était l'**exclusion mutuelle**.

Deux boucles peuvent compter au même instant, voir de la place, et lancer
toutes les deux. **Le compte était juste, la décision était fausse.**

## Le mécanisme

Un jeton est un répertoire. `mkdir` échoue si le répertoire existe, et
l'opération est atomique.

**Mesuré, pas supposé** : 25 `mkdir` simultanés sur le même chemin, exactement
un gagnant. C'est ce qu'aucune lecture de compteur ne garantit.

## Les deux défauts corrigés, tous deux reproduits avant correction

### 1. Le balayage volait les jetons vivants

L'âge d'un jeton était lu sur la `mtime` du répertoire, **qui ne bouge plus
après la création**. Un agent vivant depuis plus que le TTL perdait donc son
jeton, et un second le prenait : deux agents, une place, **en silence**.

Reproduit : jeton vieilli de 60 minutes, agent toujours vivant, jeton
supprimé, second `mkdir` réussi.

Ce n'était pas théorique — nos escouades tournent 20 à 40 minutes, et le TTL
d'origine était de 45.

**Correction : battement de cœur.** Le détenteur touche son jeton tant qu'il
vit. La `mtime` devient le **dernier signe de vie** au lieu de l'heure de
naissance. Le TTL veut alors dire *« aucun signe de vie depuis N minutes »* —
le sens qu'on voulait depuis le début.

### 2. Une lecture d'état mutait l'état

`slots_libres` et `etat_slots` appelaient le balayage. **Afficher le statut
pouvait supprimer le jeton d'un agent vivant.**

Une commande de diagnostic ne doit jamais changer ce qu'elle diagnostique.

**Correction :** le balayage n'a lieu qu'à l'acquisition. Les lectures sont
pures et **signalent** les jetons suspects sans y toucher.

### 3. Le trap différé — trouvé par le test, pas par la lecture

Un neuvième cas a échoué à la première exécution : le jeton n'était pas rendu
quand la commande était tuée.

Cause : **bash diffère un trap tant qu'une commande de premier plan
s'exécute.** Le `SIGTERM` n'était traité qu'à la fin de la commande.

Correction : la commande tourne en arrière-plan et on `wait` dessus — bash
redevient interruptible, le trap part immédiatement.

# Comment l'utiliser

```bash
source "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/primitives/jetons.sh"

jetons_avec "mon-agent" bash lance-quelque-chose.sh
```

`jetons_avec` est **correcte par construction** : elle prend un jeton, bat
pendant toute l'exécution, et le rend quoi qu'il arrive — sortie normale,
échec, ou interruption. Le code de sortie de la commande est propagé.

| Réglage | Défaut | Sens |
|---|---|---|
| `JETONS_MAX` | 8 | agents simultanés, **toutes boucles confondues** |
| `JETONS_TTL_MIN` | 6 | minutes sans battement avant péremption |
| `JETONS_BATTEMENT_S` | 60 | intervalle entre deux battements |

Le TTL passe de 45 à **6 minutes** : avec un battement, six minutes de silence
signifient vraiment que le détenteur est mort. Sans battement, il fallait
majorer la durée du plus long agent — et se tromper dès qu'un agent dépassait.

Lectures pures, sûres à tout moment : `jetons_pris`, `jetons_libres`,
`jetons_etat`.

# Ce que ce verrou ne garantit pas

Il borne le **nombre d'agents lancés**. Il ne dit rien de ce qu'ils
**écrivent** : deux agents dans des jetons différents peuvent parfaitement
écraser le même fichier.

Le cloisonnement des écritures reste affaire de **périmètre exclusif déclaré
dans le brief** — et c'est une discipline, pas un mécanisme.

# Files

- [jetons.sh](jetons.sh) - Le verrou. À sourcer.
- [test_jetons.sh](test_jetons.sh) - Neuf cas. Chacun reproduit un défaut réel avant de vérifier qu'il ne se produit plus.
