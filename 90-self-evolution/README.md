# 90-self-evolution — les problématiques mesurées, converties en skills

> **Ce dossier ne contient aucune idée neuve.** Chaque skill répond à une
> problématique **mesurée** dans
> [`50_Distillation/RAPPORT_INTENTIONS_V3.md`](../50_Distillation/RAPPORT_INTENTIONS_V3.md)
> sur 2 307 sessions de mars à août 2026. Une skill sans repère `D`/`B`/`P`/`I`
> n'a pas sa place ici.

## Pourquoi ce dossier existe

Le rapport a établi une chose que rien n'exploitait :

> **Deux sessions d'août sur trois rejouent une intention déjà formulée.**
> L'unicité passe de **80,5 % en juillet à 32,3 % en août**. `GARDE-FOU` est
> relancé 96 fois, `LES SEPT CADENCES` 69 fois, `MODE FABLE` 60 fois.

Un système qui se relance au lieu de produire n'a pas un problème de capacité,
il a un problème de **mémoire procédurale**. C'est exactement ce que les cinq
sources ci-dessous résolvent — et la raison d'être de ce dossier :
**convertir un brief rejoué en skill qui tient.**

## Les cinq sources, et ce qu'on prend de chacune

| Source | Ce qu'on en tire |
|---|---|
| [Hermes Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) | Le **format** : `SKILL.md` + frontmatter, `references/`, `scripts/`, divulgation progressive à trois niveaux |
| [hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | La **boucle** : GEPA lit les traces d'exécution pour comprendre *pourquoi* ça échoue, puis fait passer les candidats par des portes |
| [Prime Agent (arXiv 2608.23552)](https://arxiv.org/html/2608.23552) | La **récursion** : primitive `rlm`, sous-agents concurrents, et surtout le *Continual Harness* — l'état persistant qui se modifie lui-même |
| [Recuris (arXiv 2608.24876)](https://arxiv.org/abs/2608.24876) | La **mémoire de travail** : un état vérifié remplace l'historique, et un vérificateur juge l'environnement — jamais la déclaration du modèle. **+15,6 pts sur Claude Opus 5**, échecs long-horizon **−80 %** |
| Forum d'agents (tests OpenAI, 1 200 agents / 70 000 messages) | La **collaboration** : espace partagé asynchrone plutôt que chaînes séquentielles, avec réservation de tâche |

**Ce qui n'est pas repris, et pourquoi.** Prime Agent annonce 95,5 % sur
ARC-AGI-3 ; ce chiffre concerne son harnais, pas ce dossier, et le citer comme
une promesse serait exactement la confusion mesuré/supposé que **D2** interdit.
De même, GEPA suppose un jeu d'évaluation : tant que `datasets/` est vide,
**aucune skill d'ici n'est optimisée** — elles sont écrites à la main.

## La structure

```
90-self-evolution/
├── skills/                    une skill par problématique mesurée
│   └── <p#-nom>/
│       ├── SKILL.md           frontmatter Hermes + Quand / Procédure / Pièges / Vérification
│       ├── references/        chargé à la demande (niveau 2), jamais au démarrage
│       └── scripts/           ce qui est exécutable — la vérification est scriptée (B3)
├── evolution/                 la boucle : proposer, évaluer, promouvoir
├── datasets/                  jeux d'évaluation — VIDE, donc aucune optimisation
└── reports/                   état de travail courant, fils du forum
```

## Les huit skills, et leur ancrage

| Skill | Répond à | Mesure qui la justifie |
|---|---|---|
| [`p1-anti-rejeu`](skills/p1-anti-rejeu/SKILL.md) | **P1**, B4 | 978 / 2 307 sessions rejouent un brief |
| [`p2-mandat-persistant`](skills/p2-mandat-persistant/SKILL.md) | **P2**, B1, D1 | `GARDE-FOU` 96×, `SEPT CADENCES` 69×, `MODE FABLE` 60× |
| [`p3-point-entree`](skills/p3-point-entree/SKILL.md) | **P3**, B2 | 11,2 % des documents atteignables ; bundle OKF = 0,6 % du corpus |
| [`p4-instrument-honnete`](skills/p4-instrument-honnete/SKILL.md) | **P4**, D2, B3 | jonctions NTFS ; `isDirectory()` faux sur lien ; total de tokens gonflé ×3,5 |
| [`p5-plancher-contexte`](skills/p5-plancher-contexte/SKILL.md) | **P5** | ~96k tokens d'outillage avant le premier mot |
| [`p6-verification-goulot`](skills/p6-verification-goulot/SKILL.md) | **P6**, D2 | 423 fichiers produits, 0 relu par un humain |
| [`p7-memoire-travail`](skills/p7-memoire-travail/SKILL.md) | **P2**, P4, B3 | Recuris : +15,6 pts Opus 5, −80 % d'échecs long-horizon |
| [`p8-forum-agents`](skills/p8-forum-agents/SKILL.md) | **P1**, P5, B4 | 103 `node.exe` le 12 août ; 4 tranches en double le 30 août |

## L'ordre de lecture

**Par le bas**, comme ARMS et comme Hermes : `p4` et `p2` d'abord — un
instrument honnête et un mandat qui tient — puis `p7` (l'état vérifié qui les
rend durables), puis `p1`, `p3`, `p5`, `p6`, et `p8` en dernier parce que
faire collaborer plusieurs agents suppose que chacun tient seul.

Une skill anti-rejeu posée sur un instrument qui ment produit des verdicts faux
avec conviction.

## Le verrou

**Rien ne passe de `confiance: machine` à `confiance: humain` sans le
propriétaire.** Hermes le pose par `skills.write_approval: true`, qui met les
écritures en attente sous `~/.hermes/pending/skills/` ; le dépôt
self-evolution le pose par revue de PR humaine ; ici c'est
[`evolution/PORTES.md`](evolution/PORTES.md). C'est le seul verrou qu'aucun
script ne peut poser à la place de quelqu'un.
