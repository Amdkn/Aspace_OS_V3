# INTENT: diagnostic-work6
**Layer:** L0
**Originator:** Donna (dlq.py) — maintenance autonome
**Date:** 2026-09-02
**Statut:** DRAFT

## 1. Irritant réel

Échec répété (famille : preuve manquante) sur le work 6 « tache qui resiste »,
1 tentative(s). Le work est en attente d'arbitrage Rick ; sans
tranche, il bloque la branche et l'opérateur redevient le superviseur.

Motif enregistré : critere 0 sans preuve : build non atteste par le compagnon

## 2. Résultat visé (mesurable)

Le work 6 ressort de l'arbitrage avec un statut terminal vérifiable :
soit `pending` (rendre) soit `done`, et plus aucun échec de la famille
« preuve manquante » n'atteint 3 tentatives au prochain passage de `dlq.py run`.

## 3. Contraintes non-négociables

- Blast radius : dossiers touchés : aucun au-delà du work cité ; interdits : kernel/uc.db en écriture directe, 00_Amadeus/
- Aucun contournement de la preuve : les critères restent exécutables.
- La tranche appartient à Rick ; Donna ne modifie pas le statut elle-même.

## 4. Definition of Done

- [ ] `python 10_Tech_OS/kernel/dlq.py rapport` ne liste plus le work 6
- [ ] `python 10_Tech_OS/kernel/uc.py status` rend `L0` done/pending sans `blocked`
