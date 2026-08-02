# Noyau — constructeur universel

Le contrôleur de V3. File de travail durable, réclamation atomique, bail expirant,
registre de prédictions. C'est le plus petit organe qui permet à un agent d'en détacher un
autre **sans passer par l'opérateur**.

```
schema.sql   les tables et les lois
uc.py        la CLI
uc.db        la base (locale, jamais commitée — voir .gitignore)
```

## Cycle de vie

```
pending ──claim──> claimed ──review──> review ──done──> done
   ^                   │                                  
   └──── reap ─────────┘                        fail ──> failed
      (bail expiré)
```

## Usage

```bash
python uc.py init
python uc.py submit --layer L2 --title "landing OMK" --tape spec.md --priority 5
python uc.py claim --harness cc --layer L2 --lease 900
python uc.py predict --work 1 --claim "lighthouse > 90" --confidence 0.7
python uc.py review --work 1
python uc.py done --work 1
python uc.py score --prediction 1 --outcome 1
python uc.py reap
python uc.py status
```

Un agent long appelle `beat --work N --harness X` périodiquement pour prolonger son bail.

## Les trois lois, tenues par la base

Elles sont dans `schema.sql` sous forme de triggers. La base **refuse** la transaction qui
les viole — aucune discipline d'agent n'est requise.

| Loi | Effet |
|---|---|
| `loi_prediction_prealable` | pas de `review`/`done` sans prédiction enregistrée avant |
| `loi_detachement` | `done` seulement depuis `review` |
| bail + `reap` | un agent mort rend son travail à la file |

## Vérifié le 2026-08-02

- deux harnesses (`cc`, `hermes`) réclament simultanément → **items distincts**, pas de double prise
- `review` sans prédiction → **rejeté** par la base
- bail d'une seconde, agent mort → `reap` remet en file, un autre harness reprend
- calibration lisible via `v_calibration`

## Concurrence

`claim` ouvre une transaction `BEGIN IMMEDIATE` : SQLite sérialise les prétendants, un seul
gagne. Mode WAL, `busy_timeout` à 5 s. Suffisant jusqu'à quelques dizaines de harnesses en
parallèle sur un disque local.

Base ailleurs que par défaut : variable `ASPACE_DB`.
