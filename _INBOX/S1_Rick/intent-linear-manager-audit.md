# INTENT: linear-manager-l0-audit-and-purge
**Layer:** L0 (Kernel Core)
**Originator:** Rick Sanchez — Visionnaire L0
**Date:** 2026-09-11
**Labels:** `role:manager`, `governance`, `kernel-l0`, `audit-purge`
**Statut:** ADMIS / FROZEN

## 1. Contexte & Diagnostique L0

Dans le cadre de la vérification sans concession de la Loi L0 ("Un système qui ne sait pas se répliquer n'est pas un système, c'est un document"), un audit complet du repository `Amdkn/Aspace_OS_V3` a été réalisé.

### Constats :
1. **Code mort / Fichiers orphelins :**
   - Présence de scripts orphelins contenant des chemins utilisateurs Windows en dur (`C:\Users\amado\...`) sans aucun test ni dépendance : `or_preset_check.py`, `or_preset_create.py`, `ryan_factory_engine.py`.
   - Présence d'un octet BOM UTF-8 corruptif à la racine du fichier `pytest.ini` bloquant le lancement standard de `pytest`.
   - Absence de suite de tests unitaires formelle pour les hooks déterministes 5D (`pre_tool_guard.py`, `post_build_validator.py`) et le webhook `yas_alert_sink.py`.

2. **Ressources Tech OS (Serviteur Silencieux) :**
   - Aucune tâche de fond / démon pirate ne consomme de mémoire ou CPU à l'insu de l'hôte.
   - Le moteur SLM local Morty (`morty_engine.py`) fonctionne en mode CPU déterministe (Holt-Winters) de manière totalement passive et silencieuse.

3. **DLQ & Triage Donna :**
   - La Dead Letter Queue (`10_Tech_OS/kernel/dlq.py`) affiche 0 échec récurrent supérieur au seuil de 3 (`bureau_de_rick`: []).

## 2. Actions Correctives & Purge Exécutée

1. **Purge du code mort :**
   - Suppression définitive de `10_Tech_OS/kernel/or_preset_check.py`.
   - Suppression définitive de `10_Tech_OS/kernel/or_preset_create.py`.
   - Suppression définitive de `10_Tech_OS/kernel/ryan_factory_engine.py`.
   - Nettoyage du BOM UTF-8 sur `pytest.ini`.
   - Portabilisation de `10_Tech_OS/kernel/hooks/post_build_validator.py` pour éliminer le fallback de chemin Windows au profit de `Path.cwd()`.

2. **Couverture de tests 100% Déterministe :**
   - Création de `10_Tech_OS/kernel/hooks/test_hooks.py` pour valider la détection de fuite de secrets PII (VETO), la détection TypeScript et l'enregistrement webhook DLQ.

3. **Gouvernance & Enregistrement uc.db :**
   - Mise à jour de la table d'événements `uc.db` via le script `log_kernel_mcp_update.py` attribuant le mandat et la validation au Kernel Core.

## 3. Definition of Done (Vérifiée)

- [x] Tous les fichiers orphelins à chemins en dur sont purgés.
- [x] `pytest` s'exécute sur l'ensemble du projet sans erreur de configuration.
- [x] `10_Tech_OS/kernel/hooks/test_hooks.py` passe avec succès (100%).
- [x] La DLQ reste propre et vérifiée par Donna (`dlq.py rapport`).
- [x] La table `event` de `uc.db` conserve la trace déterministe de la mise à jour Linear MCP avec le label `role:manager`.
