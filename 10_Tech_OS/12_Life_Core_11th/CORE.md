# Life Core — 11e Docteur

> Couche `L1` · **réside dans** `10_Tech_OS/` · **maître de** `20_Life_OS`
> · mission : tenir l'identite, l'observation et la vie.

**Ce fichier est engendré**, pas écrit. Source : `10_Tech_OS/00_Governance_Rick/replicator/core.template/`.
Toute modification directe sera écrasée au prochain `spawn.py --force`. Pour changer un Core,
on change le gabarit et on ré-engendre les trois.

## Ce que ce Core possède

| | |
|---|---|
| `ROLES.md` | les quatre titulaires |
| `tapes/` | les rubans admis pour cette couche |

Le Core ne possède **aucun organe**. La file, l'adaptateur, le portier et le reviewer vivent
dans `10_Tech_OS/kernel/` et servent les trois couches à l'identique.

## Comment ce Core travaille

```bash
# 1. une intention entre par le portier de la couche
python 10_Tech_OS/kernel/gate.py run

# 2. un harness réclame, prédit, bâtit, atteste
python 10_Tech_OS/kernel/worker_example.py --harness cc --layer L1 --max 1

# 3. le reviewer exige les preuves et détache
python 10_Tech_OS/kernel/review.py run
```

## Pourquoi ce Core vit dans le Tech OS et non dans la couche qu'il maîtrise

Le Tech OS de Rick **contient le mécanisme de reproduction des trois OS**. Les trois
Cores y résident donc ensemble, engendrés du même gabarit. Un Core est *maître de* sa
couche, il n'y *habite* pas — sinon il n'y aurait pas un réplicateur mais trois, et le
constructeur cesserait d'être universel.

## Frontière

Ce Core ne lit ni n'écrit dans les deux autres couches. S'il a besoin d'un travail hors de
`20_Life_OS`, il dépose une note dans `_INBOX/` du portier concerné — il ne franchit pas la
frontière lui-même.
