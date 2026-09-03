# INTENT: rescope-cascade-verify
**Layer:** L1
**Originator:** Amadou (mandat KANBAN t_06c75ff0, GO permanent)
**Date:** 2026-09-02
**Statut:** FROZEN

## 1. Irritant réel

Le work 19 (« Verification etat cascade A1/A2/A3 materialise (ASP-890 suite) »,
uc.db, ruban `10_Tech_OS/12_Life_Core_11th/tapes/02_Rory_Health/Cascade_Verify_Spec.md`)
a atteint `done` le 2026-09-01 20:14:20, mais sa chaîne de preuve est cassée :

1. **Famille d'échec « ruban sans critère lisible »** : le review.py n'accepte
   que le titre exact `## Critere d'acceptation` — le ruban portait
   `Critere d'acceptation` en prose, donc 3 tentatives ont échoué
   (events 153/182, work 10 event 199 « escalade vers rick, 4 tentatives »).
2. **Le ruban de vérification exigeait un état dérivé d'un build jamais
   passé par la chaîne** : le work 10 (tape 3, `Cascade_Build_Spec.md`)
   n'a été `done` que le 2026-09-02 01:24:54 — APRÈS la vérification
   (20:14). La vérification a donc attesté un état construit par un
   rattrapage hors-ruban (agent restore x16 + squads + projets), dont la
   seule preuve est rétrospective.
3. **Critères auto-référentiels non exécutables** : les critères 10-11 du
   ruban exigeaient que le work lui-même soit en `review`/critères prouvés
   au moment de la preuve — un cercle qui a coûté 2 cycles de review
   (events 188-196).

Le goulot n'est pas la cascade (elle est matérialisée : 16 agents, 3 squads,
3 projets, preuves du 2026-09-01 20:08) — c'est la **chaîne de preuve** :
vérifier un work dont le pré-requis n'est pas `done` n'est pas une preuve,
c'est une anticipation. Approche force-brute (re-exécuter apply_life_os_cascade.sh)
a échoué réellement : conflits de noms, script consommé, WinError 193 au review
(events 143/188/259).

## 2. Résultat visé (mesurable)

Le re-scopage du work 19 : sa preuve ne repose plus sur un snapshot du
2026-09-01 mais sur **l'état actuel mesuré**, contradictoire avec le work 10
`done` daté 2026-09-02 01:24:54. L'état final vérifiable :

- L'intent de re-scopage existe, FROZEN, critères exécutables.
- Un work re-scope est soumis, claimé, prédit (antérieur), construit
  (re-mesure multica de l'état cascade AUJOURD'HUI), attesté, review,
  done dans uc.db — sans toucher à `apply_life_os_cascade.sh`.

## 3. Contraintes non-négociables

- **Budget** : ≤ 50k tokens pour le cycle complet.
- **Blast radius** : lecture seule sur A'Space Core (`multica agent/squad/project
  list/get`). Interdits : mutation multica (create/restore/delete), modification
  de `apply_life_os_cascade.sh`, écriture directe dans uc.db hors uc.py.
- **Garde-fous souverains** : aucune action irréversible. Lecture seule = rien
  à valider humainement si impact $ = 0.
- **Lois kernel** : prédiction enregistrée AVANT tout started_at (lois SQL),
  transitions via uc.py uniquement.

## Critere d'acceptation (Definition of Done)

- [ ] `multica agent list` retourne les 16 agents cibles : A1-Beth, A1-Morty,
      A2-Orville, A2-Discovery, A2-SNW, A2-Enterprise, A2-Cerritos,
      A2-Protostar, A3-Pike, A3-Dal, A3-Mercer, A3-Mariner, A3-Picard,
      A3-Spock, A3-Geordi, A3-Data — mesure du jour, pas le snapshot du
      2026-09-01
- [ ] `multica squad list` retourne les 3 squads cibles
      (Squad-A1-Beth-Morty 2 membres leader ba488363, Squad-A2-Frameworks
      6 membres leader 4b9489db, Squad-A3-Officiers 8 membres leader
      ea5784f0)
- [ ] `multica project list` retourne les 3 projets cibles
      (321de019 A1-Vision, 9dc2df84 A2-Frameworks, e13a4401 A3-Officiers)
      actifs
- [ ] `git -C C:/Users/amado/ASpace_OS_V3 status --porcelain --
      10_Tech_OS/12_Life_Core_11th/tapes/02_Rory_Health/apply_life_os_cascade.sh`
      retourne vide (script non modifié), rc 0
- [ ] Le work re-scope est `done` dans uc.db avec une prediction anterieure a
      la premiere evidence (loi de prediction) — commande executable :
      `python -c "import sqlite3;c=sqlite3.connect('10_Tech_OS/kernel/uc.db');p=c.execute('SELECT predicted_at FROM prediction WHERE work_id=? ORDER BY predicted_at LIMIT 1',(<N>,)).fetchone();e=c.execute(\"SELECT MIN(at) FROM event WHERE work_id=? AND kind='evidence'\",(<N>,)).fetchone();print(1 if p and e and p[0]<e[0] else 0)"`
      doit retourner `1` (<N> = id du work re-scope ; schema verifie :
      prediction.predicted_at, event.at/kind/work_id)