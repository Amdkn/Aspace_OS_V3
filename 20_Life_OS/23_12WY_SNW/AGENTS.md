# AGENTS — 23_12WY_SNW

> Officier **SNW** · `L1` · Life Core (11e Docteur) · harness **Buzz**

## Qui travaille ici

| Rôle | Agent | Fait |
|---|---|---|
| Review | **11e Docteur** | exige les preuves, score la prédiction, **détache** |
| Spec | **Amy** (Social) | rédige le ruban, le dépose au portier |
| Build | **Rory** (Health) | `claim` → `predict` → bâtit → `attest` → `review` |
| Spawn | **River** (Knowledge) | duplique un ruban éprouvé en aveugle |

Échec répété (3 tentatives) → **Donna** (`10_Tech_OS/kernel/dlq.py`) → **Rick**.

## Comment le travail entre

Aucun agent ne crée de fichier ici de sa propre initiative. Toute intention passe par :

```bash
# 1. déposer une note dans _INBOX/A1_Beth_Morty/
python 10_Tech_OS/kernel/gate.py run     # test du ruban : admet ou refuse
python 10_Tech_OS/kernel/review.py run   # exige les preuves, détache
```

Le portier refuse tout ruban dont le critère d'acceptation n'est pas vérifiable. C'est le
test du ruban (`AGENTS.md` racine, §3) : si un constructeur doit poser une question, la
note repart avec le motif.

## Rangement PARA

Chaque sous-discipline porte les quatre officiers A3 :
`01_Projects_Picard` · `02_Areas_Spock` · `03_Resources_Geordi` · `04_Archives_Data`.

Un artefact vivant va chez Picard, une responsabilité continue chez Spock, un savoir
réutilisable chez Geordi, un état révolu chez Data.

## Interdits

- Créer un fichier à la racine de ce framework sans qu'il vienne d'un ruban admis.
- Écrire dans un autre framework — passer par son portier.
- Prononcer `done` : seul le 11e Docteur détache, et seulement depuis `review`.

## Source

`A2_Curie_SNW_Spec.md` fait foi. `SOUL.md` en donne l'intention.
