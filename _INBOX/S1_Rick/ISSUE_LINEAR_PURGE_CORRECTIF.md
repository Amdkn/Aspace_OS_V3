# ISSUE LINEAR: [Kernel Core] Audit L0 Rick Sanchez - Purge Code Mort, Servitude Tech OS & Donna DLQ

* **Title:** `[Kernel Core] Audit L0 Rick Sanchez - Purge Code Mort, Verification Servitude Silencieuse Tech OS & DLQ`
* **Team:** `Kernel Core` (KFR / KC)
* **Assignee:** `Rick Sanchez - Visionnaire L0`
* **Priority:** `Urgent (P1)`
* **Labels:** `role:manager`, `governance`, `kernel-l0`, `audit-purge`, `status:verified-canon`

---

## Context & Loi L0
Selon la Loi L0 (*"Un système qui ne sait pas se répliquer n'est pas un système, c'est un document"*), l'inspection de Rick Sanchez a évalué la capacité d'auto-réplication, de propreté et de servitude silencieuse de la couche noyau `10_Tech_OS/kernel/`.

## Constats & Directives Sans Concession (Rick Sanchez)
1. **Code Mort & Fichiers Sans Tests :**
   - Purge appliquée des scripts orphelins avec dépendances système Windows obsolètes (`or_preset_check.py`, `or_preset_create.py`, `ryan_factory_engine.py`).
   - Maintien du répertoire `_tmp_kanban/` sous contrôle `.gitkeep`.
   - Suppression du BOM UTF-8 corruptif dans `pytest.ini`.

2. **Servitude Silencieuse de Tech OS :**
   - Validation du statut de serviteur silencieux de `10_Tech_OS`. Aucun daemon pirate ou surconsommation CPU/GPU.
   - Morty SLM s'exécute de façon déterministe en CPU passif (Holt-Winters).

3. **Etat de la DLQ & Donna DLQ :**
   - État DLQ : 0 item en échec récurrent dans `uc.db` (`bureau_de_rick`: []).
   - Cause racine qualifiée pour tout échec récurrent (>3) : Absence d'attestation ou preuve cryptographique manquante lors des complétions de tâche.

## Definition of Done
- [x] Fichiers orphelins purgés et `pytest.ini` propre.
- [x] Suite de tests déterministe L0 validée (18/18 tests pytest PASS).
- [x] Rapport DLQ Donna vérifié sans anomalie.
- [x] Événement de gouvernance `role:manager` journalisé dans `10_Tech_OS/kernel/uc.db`.
