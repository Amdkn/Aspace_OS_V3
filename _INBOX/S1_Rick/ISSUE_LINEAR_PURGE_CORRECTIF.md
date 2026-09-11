# ISSUE LINEAR: [Kernel Core] Purge Code Mort & Couverture Tests Auto-Réplication L0 Kernel

* **Title:** `[Kernel Core] Purge du code mort _tmp_kanban et couverture de tests déterministes sur 10_Tech_OS/kernel`
* **Team:** `Kernel Core` (KFR / KC)
* **Assignee:** `Rick Sanchez / 13e Docteur`
* **Priority:** `Urgent (P1)`
* **Labels:** `role:manager`, `role:dlq`, `layer:5D-Gate`, `status:verified-canon`

---

## Context & Irritant Real (L0 Law)
Selon la Loi L0 (*"Un système qui ne sait pas se répliquer n'est pas un système, c'est un document"*), le noyau `10_Tech_OS/kernel/` présentait des vulnérabilités d'auto-réplication :
1. Présence de scripts de debug temporaires et orphelins dans `_tmp_kanban/`.
2. Absence de tests unitaires couvrant les primitives fondamentales du noyau (`uc.py`, `dlq.py`, `gate.py`).
3. Risque de requeue silencieux en cas d'échecs récurrents qualifiés par Donna DLQ.

## Plan d'Action & Directives Sans Concession (Rick Sanchez)
1. **Purge :** Supprimer l'intégralité des fichiers de debug morts dans `_tmp_kanban/`.
2. **Couverture de Tests L0 :** Implémenter la suite de tests automatisée `10_Tech_OS/kernel/test_l0_kernel.py` couvrant :
   - L'initialisation du schéma `uc.db` et les soumissions/claims/attestations d'items de travail (`uc.py`).
   - L'escalade des échecs récurrents (`attempts >= 3`) et l'arbitrage terminal/requeue contrôlé via Donna DLQ (`dlq.py`).
   - Le passage des portes de validation SSSF (`gate.py`).
3. **Servitude Silencieuse :** Garantir que `10_Tech_OS` demeure une couche de plomberie agnostique.

## Definition of Done
- [x] Fichiers morts de `_tmp_kanban/` purgés.
- [x] Script `10_Tech_OS/kernel/test_l0_kernel.py` créé et passant à 100% sans régression.
- [x] Télémétrie et journalisation des événements d'escalade DLQ vérifiées.
