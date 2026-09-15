# ISSUE LINEAR: [Kernel Core] Audit L0 Rick Sanchez - Purge & Portabilité Kernel OS

* **Title:** `[Kernel Core] Audit L0 Rick Sanchez - Portabilité Hooks, Servitude Silencieuse & Couverture de Tests`
* **Team:** `Kernel Core`
* **Assignee:** `Rick Sanchez / Visionnaire L0`
* **Priority:** `Urgent (P1)`
* **Labels:** `role:manager`, `governance`, `kernel-l0`, `audit-purge`, `role:dlq`
* **Status:** `Verified Canon`

---

## Contexte & Non-Négociable L0
Selon la Loi L0 (*"Un système qui ne sait pas se répliquer n'est pas un système, c'est un document"*), l'inspection du noyau `10_Tech_OS/kernel/` a établi les constats et correctifs suivants :

1. **Portabilité et Elimination des Chemins Hardcodés :**
   - Refactorisation de `10_Tech_OS/kernel/hooks/silver_platter.py` pour éliminer la dépendance fixe sur `C:/Users/amado/...` au profit de la variable d'environnement `SSSF_DB_PATH` avec un fallback inter-plateforme.
   - Elimination des chemins absolus Windows dans `dark_factory.py` (remplacés par `sys.executable` / `PYTHON_EXE`) et dans `bridge_paperclip.py` (utilisant `shutil.which("paperclipai")`).

2. **Couverture de Tests Hooks & Reproductibilité :**
   - Ajout de la suite de tests unitaires `test_silver_platter` dans `10_Tech_OS/kernel/hooks/test_hooks.py` (100% de réussite sur les hooks).

3. **Servitude Silencieuse de 10_Tech_OS :**
   - Aucune tâche ou démon d'arrière-plan résiduel ne consomme de CPU/Mémoire (`pgrep -af python` vérifié).
   - `10_Tech_OS` demeure une plomberie déterministe et agnostique.

4. **Qualification DLQ (Donna) :**
   - Vérification de `10_Tech_OS/kernel/uc.db` via `dlq.py rapport` : 0 échec récurrent (`bureau_de_rick: []`).
   - Diagnostic cause racine : Bloquage légitime lors d'absences d'attestations ou de preuves cryptographiques des harnesses.

---

## Definition of Done (Vérifiée)
- [x] Correctifs de portabilité appliqués à `silver_platter.py`, `dark_factory.py` et `bridge_paperclip.py`.
- [x] Suite de tests `10_Tech_OS/kernel/hooks/test_hooks.py` étendue et validée à 100%.
- [x] Aucun processus parasite en toile de fond (serviteur silencieux vérifié).
- [x] Rapport DLQ propre et événement enregistré dans la table `event` de `uc.db` avec le label `role:manager`.
