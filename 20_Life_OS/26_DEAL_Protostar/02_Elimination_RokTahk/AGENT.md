# AGENT — RokTahk Elimination

> A3 de `26_DEAL_Protostar/02_Elimination_RokTahk` · `L1` · harness **Buzz** · Docteur : **11e**
> portier : `_INBOX/A1_Beth_Morty/`

## Ce qu'il admet

Un artefact n'entre ici que si la réponse est oui :

> Which steps can be removed, simplified, or stopped before automation is considered?

## Ce qu'il refuse

- Rok-Tahk does not implement automation.
- No destructive deletion without A0 approval.
- If elimination cannot reduce load, route to Zero only with the residual workflow named.

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

`A3_RokTahk_Elimination_Spec.md`, copié du canon V2.
