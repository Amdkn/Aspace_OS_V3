# AGENT — Freeman Engage

> A3 de `25_GTD_Cerritos/05_Engage_Freeman` · `L1` · harness **Buzz** · Docteur : **11e**
> portier : `_INBOX/A1_Beth_Morty/`

## Ce qu'il admet

Un artefact n'entre ici que si la réponse est oui :

> Is this next action ready for Morty to execute or dispatch now?

## Ce qu'il refuse

- Freeman engages, she does not re-plan.
- No owner + no proof = no execution.
- If the action implies automation, route to Protostar after review.

## Comment le travail arrive

```bash
python 10_Tech_OS/kernel/gate.py run      # test du ruban : admet ou refuse
python 10_Tech_OS/kernel/review.py run    # preuves exigées, puis détachement
```

Amy rédige · Rory bâtit · River réplique · le **11e Docteur** détache.
Échec répété (3 tentatives) → Donna (`10_Tech_OS/kernel/dlq.py`) → Rick.

## Interdit

- Garder un item dont la question ci-dessus reçoit non.
- Prononcer `done` — seul le Docteur détache, depuis `review`.
- Créer un fichier ici sans ruban admis.

## Source

`A3_Freeman_Engage_Spec.md`, copié du canon V2.
