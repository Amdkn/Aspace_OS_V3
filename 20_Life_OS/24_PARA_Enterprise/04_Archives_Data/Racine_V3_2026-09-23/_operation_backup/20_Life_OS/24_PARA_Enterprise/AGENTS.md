# AGENTS — 24_PARA_Enterprise

> Officier **Enterprise** · `L1` · Life Core (11e Docteur) · harness **Buzz**

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

`A2_Computer_Enterprise_Spec.md` fait foi. `SOUL.md` en donne l'intention.

## D4 append-only — journal

- **2026-09-04 — Reparation pulse PARA (Doctor 11, cron).** `verify_para.py` crashait (`TypeError: '<' not supported between dict and dict`) : `registre_para.json` avait ete pollue par des entrees dict de migration Gate 2 au lieu des noms de fichiers mesures sur le disque (criteres [1]/[3] du ruban 2026-09-04-spec-para-enterprise-pulse-v0.md). Corrections : (1) verifier durci — entree non string = erreur nommee au lieu de crash ; (2) registre restaure a la verite du disque (projects=[], areas=[], archives=[], resources=16 entrees 03_Resources_Geordi hors exclusions). Les 9 entrees de migration preservees dans `registre_migration_preserve_2026-09-04.json`. Preuve : `PARA_OK rc=0`.
- **2026-09-04 — PARA Enterprise pulse v0 détaché (work 63, Doctor 11 cron).** Cycle complet sur ruban gate-compliant tape 37 (`2026-09-04-spec-para-enterprise-pulse-v0.md`, corrigé: `title:` + `## Critère d'acceptation` + `## Périmètre`/`## Interdits` — gate.py complet=true, leçon work 49 appliquée). rory_build_l1: claim → prédiction #82 (outcome=1, scorée) → 6/6 attest → review → done. Preuve: `python verify_para.py` → PARA_OK rc=0 (re-exécuté par Doctor 11). Registre collé au disque (projects=[Rock_00_Business_Pulse_12WY]). Les 6 modules A2 ont désormais tous leur pulse + verify.
