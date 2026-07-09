# Loop Engineering — Architecture (citadel/loops/)

> Canon : ADR-L1-WF-001 · ADR-LOOP-002 (queue > loop) · plan noble-swimming-spindle.
> **Loi** : le travail agentique est une QUEUE d'items typés piochés sur trigger — jamais une boucle qui tourne pour tourner.

## Structure

```
loops/
├── ARCHITECTURE.md          ← ce fichier (conventions)
├── artifacts/               ← la connaissance PARTAGÉE entre loops (le cerveau commun)
│   ├── signals/             ← frictions, idées, opportunités observées par N'IMPORTE quelle loop
│   ├── tasks/               ← LA QUEUE : items actionnables typés (pioche sur trigger)
│   ├── tickets/             ← items client/support traités (WF2/W*)
│   └── docs/                ← livrables finis
├── logs/worklog.md          ← global append-only : 1 ligne par bloc de travail fini
└── domains/                 ← 1 contrat par loop : wf0-spock · wf1-morty · wf2-book · wf3-mirofish · w-star
```

## Conventions (liantes)

1. **Avant d'agir** : toute loop lit (a) son contrat `domains/<loop>/README.md`, (b) les **10 dernières lignes** de `logs/worklog.md`, (c) les signals non-traités qui matchent ses triggers.
2. **Après avoir agi** : append 1 ligne worklog `[ISO] [loop] verbe + objet + preuve (exit/path)`. Écriture SANS preuve = interdit (l'item retourne en queue tag `unverified`).
3. **Le composé** : chaque loop LIT et ÉCRIT `artifacts/signals/` — c'est le partage de cerveau qui fait composer les boucles. Un signal = 1 fichier `signals/<slug>.md`, frontmatter OKF, append des occurrences dans le MÊME fichier (jamais de doublon de slug).
4. **Queue** : un item `tasks/` sort quand livré+vérifié, ou part en **Donna DLQ** (`tasks/_dlq/`) après 2 WK sans pioche ou 3 échecs — avec raison. Rien ne disparaît (D4).
5. **Typage** : `WF` = strates d'orchestration · `WK01-13` = semaines 12WY. `W#` nu = interdit.
6. **Flags** : une loop ne tourne que si son flag `citadel/decisions/enable_<loop>.flag` existe. Cascade posée par WF0 sur GO_SPOCK_UNIQUE (révocation = suppression du GO).
7. **Airlock** : invariant Beth RED (data/15_airlock.json) → le scope concerné se gèle au tick suivant. Les loops continuent ; l'interpellation d'A+ se gèle.
8. **Zones** : Book n'écrit que LD01+loops · Picard écrit 10_Projects/ · personne ne réécrit un RATIFIED ni un intouchable.
