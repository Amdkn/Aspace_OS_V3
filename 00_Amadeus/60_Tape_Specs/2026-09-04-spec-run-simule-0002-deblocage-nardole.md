---
id: spec-run-simule-0002-deblocage-nardole
date: 2026-09-04
layer: L2
status: active
type: ruban-phi
target: 10_Tech_OS/kernel
work: 9
framework: kernel uc.db (gate.py / review.py / dlq.py / uc.py)
pattern_source:
  - 10_Tech_OS/kernel/mandat_nardole_w15.txt
  - 00_Amadeus/60_Tape_Specs/2026-09-01-spec-d4-cold-start-reap.md
  - 00_Amadeus/60_Tape_Specs/2026-09-03-spec-dlq-qualification-works-morts.md
version: v1
title: run-simule-0002 deblocage agent Nardole (work 9)
---

# Ruban φ — run-simule-0002 : déblocage de l'agent Nardole (work 9)

## Diagnostic (mesuré, 2026-09-04)

Enquête directe sur `10_Tech_OS/kernel/uc.db` (python sqlite3, lecture seule) :

- `work` id=9 : `pc:run-simule-0002 agent Nardole bloque`, layer L2,
  tape_id NULL, status `failed`, attempts=1, créé 2026-08-02 14:18:08.
- Aucune trace de `run-simule-0002` hors de uc.db : grep -ril sur
  `10_Tech_OS/` et `00_Summers_Verse/` retourne uniquement `10_Tech_OS/kernel/uc.db`.
  Aucun artefact de simulation n'a jamais été bâti.
- Aucune ligne `claim` pour work_id=9. Aucune ligne `prediction` pour work_id=9.
- Historique d'événements de work 9 :
  - event 450 (2026-09-03 07:12:03, controleur) : `failed` —
    « qualifie mort par review: pending depuis 2026-08-02, sans ruban
    (tape_id NULL) ni critere execute — escalade Donna ».
  - event 456 (2026-09-03 07:17:05, doctor11_review_l1) : `qualification_mort` —
    « pc:run-simule-0002 agent Nardole bloque: idem 8. Verdict: mort definitive
    (epreuve passee) ».
  - event 460 (2026-09-03 07:17:45, controleur) : `requeue` — relance.
  - event 546 (2026-09-03 18:28:07) : `failed` — `{"reason": "ruban incomplet"}`.

Cause racine : l'item a été soumis sans ruban (tape_id NULL). Le work est
l'épreuve DLQ elle-même : simuler un agent Nardole bloqué (mort sans libérer
son claim) pour prouver que la loi du bail rend le travail à la file tout
seul. La reprise échoue à chaque tentative parce que le constructeur n'a
jamais reçu de description complète — c'est exactement le cas où le test du
ruban (AGENTS.md racine, §3) refuse. Ce document est le ruban manquant.

Contre-mesure : re-scope work 9 en un livrable exécutable — un script de
simulation + son vérificateur — et refaire le cycle kernel complet
(claim/predict/build/review/done), bail 3600, sur ce work.

## Objectif

Produire dans `10_Tech_OS/kernel/` deux fichiers nouveaux (stdlib uniquement,
français ASCII sans accents, style `verify_gtd.py`) :

1. `run_simule_0002.py` — simulation de l'épreuve : un worker fantôme
   (`nardole_sim_l2`) claim un work de test dédié créé par le script lui-même
   via `python uc.py submit`, avec un bail court (120 s), puis le worker
   meurt sans jamais rendre le travail (aucun done, aucun abandon explicite).
2. `verify_run_simule_0002.py` — vérificateur qui prouve la loi du bail :
   après expiration du bail, le reap (`python uc.py reap` ou l'équivalent
   exposé par `uc.py`) rend le work à la file (`status` revient a `pending`),
   et la table `event` porte bien un événement de type `reap` pour ce work.

## Critère d'acceptation

1. `C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel/run_simule_0002.py`
   existe, s'execute avec python 3 stdlib uniquement (imports limites a
   json/os/subprocess/sys/time), et cree lui-meme son work de test par
   `python uc.py submit --layer L2 --title "pc:run-simule-0002 nardole sim epreuve bail" --parent 9`
   (si le CLI `uc.py` attend d'autres noms d'options, c'est la sortie reelle
   de `python uc.py submit --help` qui fait foi — mesurer, ne pas deviner).
2. La simulation claim le work de test avec le harness exact
   `nardole_sim_l2` et un bail de 120 secondes, puis exit sans rendre le
   travail (simulation de mort).
3. `C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel/verify_run_simule_0002.py`
   existe (stdlib uniquement, meme style) et verifie, dans l'ordre numerote :
   [1] le work de test est de retour en `pending` (ou `claimed` avec
       expires_at passee si le reap n'a pas encore tourne) apres attente
       d'expiration — c'est l'etat pre-reap admissible ;
   [2] apres reap, `status` = `pending` et aucune ligne `claim` active
       (expires_at future) ne subsiste pour ce work_id ;
   [3] la table `event` contient au moins un evenement de kind `reap`
       pour ce work_id, horodate.
4. Le work de test est ensuite rendu proprement a l'etat neutre via
   `python dlq.py rendre --work <id_test>` (Donna), pour ne pas polluer la file :
   le verifier accepte aussi bien `pending` que `failed` en etat final, mais
   journalise l'etat final mesure dans sa sortie.
5. `python verify_run_simule_0002.py` affiche `SIM0002_OK` et retourne rc=0
   quand tout passe, `SIM0002_KO` avec la liste des erreurs et rc=1 sinon.
6. Aucun fichier existant du kernel n'est modifie (git status --porcelain sur
   `10_Tech_OS/kernel/` ne montre que les deux fichiers nouveaux).

## Criteres de done pour le work 9 lui-meme (cycle kernel)

Le constructeur execute le cycle complet sur le work 9, dans cet ordre,
toutes les etapes horodatees dans uc.db :

1. `cd C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel`
2. CLAIM — loi du bail, bail 3600 s :
   `python uc.py claim --harness yaz_spec_l2 --work 9 --lease 3600`
3. PREDICTION ANTERIEURE — obligatoirement avant tout build (loi de prédiction) :
   `python uc.py predict --work 9 --claim <claim_id> --confidence 0.8`
   avec le claim : "run_simule_0002.py + verify_run_simule_0002.py produits,
   SIM0002_OK rc=0 au premier tir, aucun fichier existant modifie".
4. BUILD : produire les deux fichiers du présent ruban.
5. EVIDENCE : attacher un event `evidence` par critere (1 a 6) avec la sortie
   reelle de chaque commande de preuve.
6. REVIEW : `python review.py run` — le done n'est jamais atteint que depuis
   review (loi de détachement). Scorer ensuite la prediction (outcome 0/1).
7. DONE : `python uc.py done --work 9` — refuse hors review.

## Commandes de preuve

```bash
cd C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel
python run_simule_0002.py            ; echo "rc=$?"
python verify_run_simule_0002.py     ; echo "rc=$?"
python -c "import sqlite3;c=sqlite3.connect('uc.db');print(list(c.execute(\"select status,tape_id from work where id=9\")))"
```

Preuve attendue : `SIM0002_OK`, rc=0, et work 9 avec tape_id non NULL et
status `review` ou `done`.

## Périmètre

Le présent ruban ne couvre que les deux fichiers ci-dessus dans
`10_Tech_OS/kernel/` ; le cycle kernel (claim/predict/build/review/done) du
work 9 est décrit dans la section Criteres de done.

## Interdits

- Ce ruban ne cree que les deux fichiers ci-dessus dans `10_Tech_OS/kernel/`.
  Aucun fichier existant n'est modifie. Aucune ecriture directe dans uc.db :
  tout passe par `uc.py` / `dlq.py` / `review.py`.
- Le work de test cree par la simulation est clos par `dlq.py rendre` apres
  preuve — la file ne doit pas accumuler d'item fantome.
- Pas de dependance hors stdlib. Pas d'accents ni de caracteres non ASCII
  dans les deux scripts.
- Si le work 9 est statue `failed` au moment du claim (cause mesuree :
  event 546), le claim passe par `python dlq.py rendre --work 9` d'abord —
  Rick a deja tranché la reprise (requeue event 460), donc c'est la voie
  canon, pas une exception.
- Test du ruban (AGENTS.md racine, §3) : un constructeur doit pouvoir
  executer sans poser une seule question a l'operateur.
