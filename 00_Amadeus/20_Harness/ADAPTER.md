# Contrat d'adaptateur de harness

Dix harnesses ne sont un avantage que si l'observateur les voit de la même façon. Sinon ce
sont dix intégrations, donc dix goulots — et A0 redevient ce que tu étais dans V2.

Ce document est le **contrat unique**. Un harness conforme peut réclamer du travail, quel que
soit son langage.

---

## Le fil de communication est la CLI, pas une bibliothèque

Le protocole est `10_Tech_OS/kernel/uc.py`. Chaque verbe écrit un objet JSON sur la sortie
standard. Un harness en Python, Node, Rust ou bash implémente le même contrat en appelant les
mêmes verbes.

`harness.py` est **une** implémentation de référence, pas le contrat. Ne pas la porter :
la réimplémenter.

## Les cinq verbes

| Verbe | Quand | Retour |
|---|---|---|
| `claim --harness NOM [--layer L] --lease S` | tirer du travail | `{"work": {...}}` ou `{"work": null}` |
| `predict --work N --claim "..." --confidence 0.7` | **avant** d'agir | `{"prediction_id": N}` |
| `beat --work N --harness NOM --lease S` | pendant le travail | `{"ok": true}` |
| `review --work N` \| `fail --work N --reason "..."` | verdict | `{"status": "..."}` |
| `reap` | avant chaque `claim` | `{"reclames": [...]}` |

## Machine à états

```
pending ──claim──> claimed ──review──> review ──done──> done
   ^                   │                                  
   └──── reap ─────────┘                        fail ──> failed
      (bail expiré)
```

`done` n'est pas prononcé par le harness : c'est le contrôleur qui détache, après revue.

## Les quatre obligations

**1. Prédire avant d'agir.** `predict` doit précéder l'exécution, pas la conclure. La base
refuse `review` sans prédiction — ce n'est pas une convention, c'est un trigger SQL.

**2. Battre pendant le travail.** Appeler `beat` au moins toutes les `lease / 3` secondes.
Sans battement, `reap` reprend le travail et un autre harness le refait.

**3. Ne jamais retenir un bail sur plantage.** Si le harness lève une exception, il appelle
`fail` avant de mourir. Un travail retenu jusqu'à expiration coûte le bail entier à la file.

**4. Ne pas poser de question.** Si le ruban (`tape_path`) est incomplet, le harness rend
`fail` avec la raison. Il ne s'adresse pas à l'opérateur. C'est le test du ruban
(`AGENTS.md` §3).

## Squelette minimal, tout langage

```
boucle:
  exec  uc.py reap
  r  <- exec uc.py claim --harness NOM --layer L --lease 300
  si r.work est nul: dormir 5s; continuer

  exec uc.py predict --work r.work.id --claim "<attendu>" --confidence 0.6

  demarrer un fil qui appelle beat toutes les 100s

  essayer:
      batir depuis r.work.tape_path
      exec uc.py review --work r.work.id
  attraper e:
      exec uc.py fail --work r.work.id --reason e
  enfin:
      arreter le fil de battement
```

## Base de données

Par défaut `10_Tech_OS/kernel/uc.db`. Redirigeable par la variable d'environnement
`ASPACE_DB` — utile pour un harness distant travaillant sur une copie, ou pour les tests.

## Conformité vérifiée le 2026-08-02

L'implémentation de référence a passé ces trois épreuves :

| Épreuve | Attendu | Observé |
|---|---|---|
| `cc` et `hermes` réclament en parallèle | items distincts | items 1 et 2, aucun doublon |
| `review` sans `predict` | rejet | rejeté par le trigger SQL |
| harness qui lève une exception en plein travail | travail rendu tout de suite | passé en `failed`, bail libéré |

Un harness qui ne passe pas ces trois épreuves n'est pas conforme.

## Enregistrement

`REGISTRY.json` de ce dossier liste les harnesses connus, avec leur présence réelle sur
disque — sondée, jamais déclarée. Un harness absent y figure avec `present: false` plutôt que
d'être passé sous silence.
