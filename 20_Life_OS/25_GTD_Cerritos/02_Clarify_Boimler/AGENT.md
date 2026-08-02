# AGENT — Boimler Clarify

> A3 de `25_GTD_Cerritos/02_Clarify_Boimler` · `L1` · harness **Buzz** · Docteur : **11e**
> portier : `_INBOX/A1_Beth_Morty/`

## Ce qu'il admet

Un artefact n'entre ici que si la réponse est oui :

> Is this actionable, and if yes, what is the next visible action?

## Ce qu'il refuse

- Boimler clarifies; he does not schedule or execute.
- A valid next action starts with a verb and has an owner.
- Multi-step work routes to Enterprise or SNW.

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

`A3_Boimler_Clarify_Spec.md`, copié du canon V2.
