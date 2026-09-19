# ISSUE LINEAR: [Kernel Core] Audit L0 Rick Sanchez - Purge Code Mort & Servitude Silencieuse

* **Title:** `[Kernel Core] Audit L0 Rick Sanchez - Purge Code Mort, Servitude Silencieuse & Contrôle DLQ`
* **Team:** `Kernel Core` (KFR / KC)
* **Assignee:** `Rick Sanchez - Visionnaire L0`
* **Priority:** `Urgent (P1)`
* **Labels:** `role:manager`, `role:dlq`, `layer:5D-Gate`, `status:verified-canon`

---

## 1. Diagnostic L0 (Rick Sanchez - Garant de la Loi L0)

> *"Un système qui ne sait pas se répliquer n'est pas un système, c'est un document."*

### A. Code Mort & Fonctions Orphelines
- **Fichier orphelin non-portable :** `10_Tech_OS/kernel/antigravity_tts_daemon.py` présentait des chemins Windows utilisateur en dur (`C:\Users\amado`) avec dépendances Windows-only (`win32com.client`). Purgé définitivement.
- **Fichier d'état résiduel :** `10_Tech_OS/kernel/run_simule_0002_state.json` resté en résidu de simulation. Purgé définitivement.
- **Chemins d'exécutable en dur :** `dark_factory.py` et `bridge_paperclip.py` contenaient des chemins Windows fixes. Portabilisés avec `sys.executable` et `shutil.which`.

### B. Servitude Silencieuse de Tech OS
- Aucun processus fantôme ou démon consommateur de CPU/RAM à l'insu de l'hôte.
- Le moteur SLM local Morty (`morty_engine.py`) opère en mode CPU déterministe (Holt-Winters) de manière totalement passive.

### C. État de la Dead Letter Queue (`dlq.py`)
- Analyse de `10_Tech_OS/kernel/uc.db` via `dlq.py rapport` : 0 dossier en attente sur le bureau de Rick (`bureau_de_rick: []`, verdict `"rien a arbitrer"`).
- Comportement d'escalade et d'arbitrage terminal vérifié par la suite de tests `test_l0_kernel.py`.

---

## 2. Actions Correctives & Plan de Purge Exécuté
1. **Purge du code mort :** Supprimé `antigravity_tts_daemon.py` et `run_simule_0002_state.json`.
2. **Portabilisation :** Refactorisé `dark_factory.py` et `bridge_paperclip.py`.
3. **Extension de couverture de tests :** Couverture de `controleur.py`, `mandat_docteur.py`, `beth_consumer.py`, et `wheel_consumer.py` ajoutée à `test_l0_kernel.py`.
4. **Validation des tests :** 100% des tests unitaires exécutés via `pytest` (21/21 passed).

---

## 3. Definition of Done
- [x] Code mort et fichiers non-portables purgés sans concession.
- [x] Chemins exécutables refactorisés en mode portable multi-OS.
- [x] Suite de tests `10_Tech_OS/kernel/test_l0_kernel.py` étendue à 100% de succès.
- [x] Événement d'arbitrage et gouvernance Linear MCP inscrit dans `uc.db`.
