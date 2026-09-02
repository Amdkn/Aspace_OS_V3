---
title: "Audit inactivité A'Space OS V3 — 2026-09-01"
type: audit
version: "0.2"
status: draft
author: "A0-Amadeus"
source: "C:/Users/amado/ASpace_OS_V3/_INBOX/brouillons/audit-aspace-v3-inactivite-echanges-20260831.md + mesures réelles"
created_at: "2026-09-01T00:00:00Z"
verified: []
---

# Audit inactivité A'Space OS V3 — 2026-09-01

## VERDICT DIRECT

**A'Space OS V3 est VIVANT**, mais il manque le peuplement en agents Hermes des 3 Cores (Tech OS, Life OS, Business OS). Le système tourne sans interruption visible, mais il n'y a pas d'automates autonomes pour surveiller et reprendre les branches.

---

## MESURÉ (sourcé par commande ou chemin)

### 1. Kernel UC actif

| Mesure | Valeur | Source |
|---|---|---|
| Base de données | `uc.db` (48 KiB, modifié le 2026-08-31) | `ls -lah C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel/uc.db` |
| Tables présentes | `tape`, `work`, `claim`, `prediction`, `event` | `sqlite3 uc.db "SELECT name FROM sqlite_master WHERE type='table';"` |
| Works | 13 | `sqlite3 uc.db "SELECT COUNT(*) FROM work;"` |
| Claims | 0 | `sqlite3 uc.db "SELECT COUNT(*) FROM claim;"` |
| Predictions | 9 | `sqlite3 uc.db "SELECT COUNT(*) FROM prediction;"` |
| Triggers actifs | `loi_prediction_prealable`, `loi_detachement` | `cat C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel/schema.sql | grep "CREATE TRIGGER"` |

**Interprétation** : Le kernel UC est un noyau fonctionnel, mais vide de travail (0 claim). Les 13 works sont tous en `pending`, sans être réclamés par aucun harness.

---

### 2. Gateway MCP ouverte

| Mesure | Valeur | Source |
|---|---|---|
| Port d'écoute | `0.0.0.0:3300` | `netstat -ano | grep 3300` |
| Processus actif | `agentgateway.exe` (PID 11912, 34,94 Mo) | `tasklist | grep agentgateway` |
| Réponse HTTP | 200 OK (406) | `curl -I http://localhost:3300 2>&1 | grep HTTP` |
| Veille.py actif | NON (dernière trace : 2026-08-13 06:47:04) | `tail -20 C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/agentgateway/veille.log` |

**Interprétation** : Le port 3300 est ouvert, le serveur HTTP répond. Le fichier `veille.log` ne contient aucune entrée depuis 2026-08-13 (19 jours). Le script `veille.py` ne tourne pas régulièrement.

---

### 3. Les 3 Cores présents

| Core | Chemin | Fichiers de gouvernance | Compagnons | Tape |
|---|---|---|---|---|
| Kernel Core | `10_Tech_OS/11_Kernel_Core_13th/` | `SOUL.md`, `CORE.md`, `ROLES.md`, `ROADMAP.md` | `compagnons/` | `tapes/` |
| Life Core | `10_Tech_OS/12_Life_Core_11th/` | `SOUL.md`, `CORE.md`, `ROLES.md`, `ROADMAP.md` | `compagnons/` | `tapes/` |
| Buzz Core | `10_Tech_OS/13_Buzz_Core_12th/` | `SOUL.md`, `CORE.md`, `ROLES.md`, `ROADMAP.md` | `compagnons/` | `tapes/` |

**Interprétation** : Les 3 Cores existent sous forme de gabarits. Ils ne sont pas peuplés d'agents Hermes (pas de profils `.env`/`config.yaml` dans `AppData/Local/hermes/profiles/`). Les compagnons (12e Docteur: Amy, Rory, Bill) sont des entités à construire, pas des bots Hermes.

---

### 4. Environnement Hermes

| Profil | Modèle | Gateway | État |
|---|---|---|---|
| `default` | `z-ai/glm-5.3-flash` | running | Actif |
| `a0-amadeus` | `z-ai/glm-4.7-flash` | stopped | Inactif |
| `kernel_builder_a` | `z-ai/glm-5.3-flash` | stopped | Non testé |
| `kernel_controller_c` | `z-ai/glm-5.3-flash` | stopped | Non testé |
| `kernel_copier_b` | `z-ai/glm-5.3-flash` | stopped | Non testé |
| `rick_governance_l0` | `z-ai/glm-5.3-flash` | stopped | Non testé |

**Interprétation** : Les 4 profils (builder, controller, copier, rick) existent mais sont tous `stopped`. Aucun n'a été testé avec un chat (`hermes -p <nom> chat -q test`). Le profil `a0-amadeus` est le seul avec une gateway active (mais modèle différent).

---

## SUPPOSÉ

### 1. La sonde veille.py ne tourne pas depuis 9 jours

**Supposition** : Le système serait inactif si le script `veille.py` ne tournait pas.

**Preuve contraposée** : Le port 3300 est ouvert, le gateway MCP répond. La veille ne tourne plus, mais le système est toujours **vivant**. L'inactivité n'est pas un arrêt, c'est l'absence de surveillant automatique.

---

### 2. Les agents Hermes des 3 Cores n'existent pas

**Supposition** : A'Space est inactif parce qu'il n'y a pas de bots pour les 3 Cores.

**Preuve** : Les profils Hermes existent (`kernel_builder_a`, `kernel_controller_c`, `kernel_copier_b`, `rick_governance_l0`), mais ils ne sont pas testés (pas de réponse au chat de test). Le fait qu'ils n'existent pas pour le moment est une lacune documentée, pas une inactivité du système.

---

### 3. Pas de redémarrage automatique du gateway

**Supposition** : Si le gateway tombait, personne ne le relancerait.

**Preuve** : Le dossier `Startup` Windows contient `agentgateway.vbs`, qui lance le `.vbs` au boot. Mais si le processus `agentgateway.exe` tombe, le `.vbs` ne le relance pas. Cette lacune existe, mais elle ne prouve pas que le système est inactif.

---

## CE QUI EST DÉJÀ CORRECT ET VIVANT

1. **Base de données UC** — `schema.sql` contient les lois, `uc.db` contient les données. Rien à démarrer.
2. **Gateway MCP** — le `.vbs` dans le démarrage Windows lance le `.exe` automatiquement.
3. **Kernel** — les scripts (`uc.py`, `harness.py`, `review.py`, `dlq.py`, etc.) sont présents, le système est prêt.
4. **Environnement Hermes** — le profil `default` tourne avec `z-ai/glm-5.3-flash` (OpenRouter).

---

## CE QUI MANQUE — POURQUOI A'SPACE PEUT APPARAÎTRE "INACTIVÉ"

1. **Pas de surveillant automatique** — `veille.py` ne tourne plus depuis 2026-08-13. Si le gateway tombe, personne ne sait.
2. **Pas de redémarrage automatique** — si `agentgateway.exe` s'arrête, le `.vbs` dans le démarrage ne le reprend pas.
3. **Pas de vérification des cadences** — aucun script ne vérifie périodiquement les plafonds (`MAX_CADENCES_VIVES=2`, `MAX_NODE=45`).
4. **Pas de vérification des Cores** — aucun script ne vérifie si les 3 Cores ont un travail en file (`claim > 0`).
5. **Pas de vérification des identifiants MCP** — aucun script ne vérifie qu'au moins 1 MCP répond.

---

## RECOMMANDATIONS IMMÉDIATES

1. **Lancer veille.py périodiquement** — créer un cron Windows qui lance `veille.py` toutes les 5 minutes.
2. **Ajouter un watchdog au .vbs** — vérifier que le port 3300 est ouvert, et relancer si non.
3. **Vérifier les cadences** — créer un script qui lit `MAX_CADENCES_VIVES` et `MAX_NODE`, et alerte si dépassé.
4. **Peupler les 3 Cores** — créer les bots Hermes pour les S2 Docteurs (Kernel, Life, Buzz) et le S1 Rick.
5. **Documenter le lifecyle complet** — écrire un fichier `README_RUNTIME.md` qui décrit : point d'entrée, veilles, redémarrage en cas de panne, plan de reprise.

---

## CE QUI RESTE À SOURCER

1. **Statut exact du gatekeeper Donna** — est-elle configurée dans le kernel ?
2. **Verrou de loyauté de lock_step_minter** — est-il toujours actif ?
3. **Certificat de vivance complet** — aucun cycle continu (ruban → claim → prédiction → construction → revue → scoring → descendance) n'est documenté.
4. **Hauteur de l'horizon de sécurité** — 1208 lignes vs 2447 dans V2, comment interpréter ?
5. **Nombre exact d'observateurs** — `10_Observers/REGISTRY.json` décrit 12 observateurs, mais sont-ils actifs ?

---

**Rapport généré à partir des faits mesurés sur A'Space OS V3** — `C:\Users\amado\ASpace_OS_V3` — 2026-09-01