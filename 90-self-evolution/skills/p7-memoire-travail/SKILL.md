---
name: p7-memoire-travail
description: Tient un état de travail vérifié qui remplace l'historique comme source de vérité, et n'avance un objectif que sur preuve d'environnement. Applique Recuris (arXiv 2608.24876) à la boucle P1/P2 mesurée du poste.
version: 1.0.0
platforms: [windows, linux, macos]
author: amadou-kone
metadata:
  hermes:
    tags: [memoire-travail, recuris, etat-verifie, long-horizon, rsi]
    category: self-evolution
    requires_tools: [terminal]
    ancrage:
      problematiques: [P2, P1, P4]
      besoins: [B1, B3]
      desirs: [D1, D2]
      mesure: "Recuris : +15,6 pts sur Claude Opus 5 (τ²-bench), +32,2 pts sur les tâches les plus longues, échecs long-horizon −80 %"
      source: "50_Distillation/RAPPORT_INTENTIONS_V3.md §3 P2"
---

# Quand l'utiliser

**Dès qu'une tâche dépasse une dizaine d'étapes** ou franchit une compaction.
C'est la skill qui rend les autres durables : sans état vérifié, un agent
relit un historique qui grossit, perd l'objectif non résolu, et redemande.

# Pourquoi elle existe

Recuris nomme précisément la panne du poste :

> *« Prior harnesses retrieve against a growing chat history and lose track of
> unresolved goals. »*

C'est **P2** décrit de l'extérieur : l'historique conserve les faits et perd
ce qui reste à faire. Le remède mesuré : **+15,6 points sur Claude Opus 5**,
**+32,2 sur les tâches les plus longues**, et les échecs long-horizon qui
tombent **de 80 %**.

Deux principes s'appliquent directement ici :

1. **L'état, pas l'historique.** Chaque objectif porte un statut —
   `pending`, `done`, `blocked` — sa preuve, et son bloqueur éventuel.
2. **Le vérificateur juge l'environnement, jamais la déclaration.**
   *« It evaluates the tool or environment result rather than the model's own
   claim that the action succeeded. Invoking a skill or attempting a tool call
   is not completion evidence. »* C'est **P4** formulé comme une règle
   d'architecture, et c'est exactement le `exit 0` qui ne prouve rien.

# Procédure

1. **Ouvrir l'état au début de la tâche**, un objectif par ligne :

   ```bash
   python 90-self-evolution/skills/p7-memoire-travail/scripts/etat.py ouvrir "<tâche>" "<but 1>" "<but 2>"
   ```

2. **Avancer un objectif uniquement contre une preuve d'environnement** —
   un chemin de fichier, un code HTTP, une sortie de commande :

   ```bash
   python .../etat.py fait <n> --preuve "portee.py --auto-test → rc=0, 140/140"
   ```

   Sans `--preuve`, le script **refuse**. Une intention d'avoir fait n'est pas
   une preuve d'avoir fait.

3. **Déclarer un blocage plutôt que de le contourner en silence** :

   ```bash
   python .../etat.py bloque <n> --raison "aucun connecteur e-mail câblé"
   ```

4. **Relire l'état après compaction, pas l'historique** :

   ```bash
   python .../etat.py voir
   ```

# Ce que cette skill remplace

- **La relecture de l'historique** comme source de vérité en fin de tâche.
  L'état vérifié la remplace : il est court, il est à jour, il survit à la
  compaction.
- **Le récapitulatif de fin de tour** reconstruit de mémoire, qui réaffirme
  parfois des objectifs jamais atteints.
- **La déclaration « c'est fait »** sans preuve attachée.

# Pièges

- **Un objectif marqué `done` sans preuve est pire que non suivi** : il
  éteint la vigilance sur ce qui n'est pas fini. Le script l'interdit plutôt
  que de le déconseiller.

- **L'état n'est pas un journal.** Il porte ce qui reste à faire, pas ce qui
  s'est passé. S'il grossit, il redevient l'historique qu'il remplace.

- **Un vérificateur trop strict crée un `false-pending`.** Recuris le
  reconnaît comme cible de réparation à part entière : si un objectif atteint
  reste `pending`, le défaut est dans le vérificateur, pas dans la tâche.

- **Ne pas confondre avec les cadences.** Cet état vit le temps d'une tâche.
  Le mandat, lui, vit dans les fichiers de démarrage — voir
  [`p2-mandat-persistant`](../p2-mandat-persistant/SKILL.md).

# Vérification

```bash
python 90-self-evolution/skills/p7-memoire-travail/scripts/etat.py --auto-test
```

Le test vérifie qu'un `done` **sans preuve est rejeté**, qu'un `done` avec
preuve est accepté, et que l'état survit à une relecture. Il échoue si la
règle de preuve peut être contournée — c'est le seul comportement qui rendrait
cette skill nuisible.
