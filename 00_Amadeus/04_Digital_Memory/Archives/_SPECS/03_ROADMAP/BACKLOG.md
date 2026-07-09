# BACKLOG A'Space — V0 → Antifragile

**Dernière mise à jour** : 2026-02-28
**Instance** : V0 Windows

> Priorisé par impact sur la souveraineté et l'antifragilité du système.
> Chaque item est ancré sur un ADR ou une décision Amadeus (A0).
> Exécution : tâches L0/Rick via Claude Code ou Gemini CLI (pas Amadeus).

---

## LÉGENDE PRIORITÉ

| Priorité | Signification |
|----------|---------------|
| 🔴 P0 | Bloquant — anomalie critique ou sécurité |
| 🟠 P1 | Important — corriger avant d'avancer |
| 🟡 P2 | Amélioration — impact fort, non bloquant |
| 🟢 P3 | Backlog — utile mais pas urgent |

---

## SPRINT 1 — Fondations ✅ EXÉCUTÉ (2026-02-28)

> **Tous les items ci-dessous ont été exécutés par Claude Code (Sprint 1).**
> Commit git : `d52f86c` dans `aspace_a0_amadeus`

### ✅ P0 — Fix doctrine_sync.sh → vrai Canon (ADR-004)

**Quoi** : Changer `REPO_DIR` dans `doctrine_sync.sh` pour pointer vers `C:/Aspace00/aspace_a0_amadeus` au lieu de la copie stale `workspace/aspace_a0_amadeus/`
**Pourquoi** : Chaque nuit, le Runtime se synchronise depuis une copie figée — le Canon réel n'est jamais propagé
**Fichier** : `openclaw/.openclaw/workspace/sync/doctrine_sync.sh`
**ADR** : ADR-004
**Effort** : 5 min

---

### ✅ P0 — Supprimer workspace/aspace_a0_amadeus/ (copie stale)

**Quoi** : `rm -rf C:/Aspace00/openclaw/.openclaw/workspace/aspace_a0_amadeus/`
**Pourquoi** : Source de confusion sur quelle est l'autorité canonique
**Prérequis** : P0 doctrine_sync.sh corrigé en premier
**Effort** : 1 min

---

### ✅ P1 — Cleanup 03_OpenClaw_Body → config-only (PRD-001)

**Quoi** : Supprimer le clone OpenClaw de `03_OpenClaw_Body/`, créer les 4 fichiers cibles (agents_registry.json, bootstrap.sh, .env.template, openclaw.json.template)
**Pourquoi** : Non-conforme ADR-001, pollue le Canon git avec 60+ items inutiles
**Fichier spec** : `_SPECS/02_V1_PRD/PRD-001_03_OpenClaw_Body_Cleanup.md`
**ADR** : ADR-001 + ADR-002
**Effort** : 20-30 min

---

### ✅ P1 — Créer agents_registry.json (ADR-003)

**Quoi** : Créer `03_OpenClaw_Body/agents_registry.json` avec mapping complet des 103 agents Canon (Canon ↔ Runtime ↔ Config)
**Pourquoi** : Source Unique de Vérité pour le mapping — prérequis pour tout audit automatique
**Prérequis** : P1 03_OpenClaw_Body cleanup (le dossier doit être propre d'abord)
**ADR** : ADR-003
**Effort** : 1-2h (génération via script Node.js)

---

### ✅ P1 — Fix cron delivery WhatsApp (4 erreurs consécutives)

**Quoi** : Corriger ou désactiver le mode delivery WhatsApp du job `Nightly doctrine sync`
**Pourquoi** : 4 erreurs consécutives — le cron échoue à la livraison même si le script s'exécute bien
**Fichier** : `openclaw/.openclaw/cron/jobs.json` — job `64b9a890-...`
**Options** :
  - Option A : Supprimer le bloc `delivery` (pas de notification)
  - Option B : Changer `delivery.mode` en `"silent"` ou `"log"`
  - Option C : Configurer WhatsApp correctement (hors scope V0)
**Effort** : 5 min (décision Amadeus sur option)

---

### 🟡 P2 — Instancier Donna_DLQ dans le Runtime

**Quoi** : Créer le dossier Runtime `donna_dlq/` dans `agents_runtime/` avec les 6 fichiers standards (AGENTS.md, HEARTBEAT.md, IDENTITY.md, SOUL.md, TOOLS.md, USER.md)
**Pourquoi** : Donna = Dead Letter Queue — agent critique pour la résilience, doit exister en Runtime
**ADR** : ADR-003 (gaps identifiés)
**Effort** : 15 min

---

### 🟡 P2 — Créer .env.template à la racine de aspace_a0_amadeus

**Quoi** : Créer `aspace_a0_amadeus/.env.template` (variables V0/V1/V2)
**Pourquoi** : Prérequis pour la portabilité Multiverse (ADR-002)
**ADR** : ADR-002
**Effort** : 5 min

---

### 🟡 P2 — Décider deal_* vs protostar_* (doublons)

**Quoi** : 4 paires de doublons dans le Runtime — même vaisseau (USS Protostar = DEAL Engine)
**Pourquoi** : Ambiguïté dans l'adressage des agents DEAL
**Décision Amadeus** : Garder `protostar_*` (nom canon) ou `deal_*` (nom fonctionnel) ?
**Effort** : 10 min (décision) + 15 min (nettoyage)

---

### 🟡 P2 — Ajouter 52 agents inactifs à openclaw.json

**Quoi** : 52 agents présents dans `agents_runtime/` mais absents de `openclaw.json`
**Pourquoi** : Ces agents ne peuvent pas être adressés via OpenClaw tant qu'ils ne sont pas dans la config
**Prérequis** : agents_registry.json créé (pour avoir le mapping exact)
**Effort** : 1h (génération via script)

---

### 🟢 P3 — Supprimer A0_OSS_Twin/ (ghost folder)

**Quoi** : `rm -rf C:/Aspace00/A0_OSS_Twin/`
**Pourquoi** : Dossier vide, reste d'une ancienne architecture
**Effort** : 1 min

---

### 🟢 P3 — Auditer amadeus_ultimate_dna/ + .tar.gz

**Quoi** : Inspecter le contenu du backup 50MB
**Pourquoi** : Comprendre si c'est un backup VPS utile ou une archive redondante
**Effort** : 30 min

---

### 🟢 P3 — Instancier Summer + 7x Nano DC dans le Runtime

**Quoi** : Créer les dossiers Runtime pour les 8 agents Canon sans Runtime
**Pourquoi** : Compléter le mapping Canon ↔ Runtime
**Prérequis** : agents_registry.json (ADR-003)
**Effort** : 1h

---

---

## SPRINT 2 — Migrations Container ✅ TERMINÉ (2026-02-28)

> **Commit** : `a3bb781` — "Sprint 2: Container migration ADR-005 + _SPECS intégrés"
> Étapes 1-7 exécutées (Gemini étape 1, Claude Code étapes 2-7 après récupération)
> openclaw.json + 16 fichiers config patchés (anciens chemins → aspace_a0_amadeus/openclaw/)

## SPRINT 2b — Restructuration 00_Amadeus — PRD-004 (Gemini CLI) — EN COURS

> **Exécutant** : Gemini CLI
> **Spec complète** : [`PRD-003`](../02_V1_PRD/PRD-003_Container-Migration.md) + [`PRD-004`](../02_V1_PRD/PRD-004_00_Amadeus-Restructuration.md)
> **Décision architecturale** : ADR-005 (OpenClaw inside Container)

### ✅ P0 — Créer aspace_a0_amadeus/.gitignore

**Quoi** : Créer le `.gitignore` excluant `openclaw/.openclaw/`, `openclaw/node_modules/`, `.env`
**Pourquoi** : Prérequis obligatoire avant de déplacer OpenClaw inside le container
**ADR** : ADR-005
**Effort** : 2 min

---

### ✅ P0 — Déplacer openclaw/ → aspace_a0_amadeus/openclaw/ (ADR-005)

**Quoi** :
```powershell
robocopy "C:\Aspace00\openclaw" "C:\Aspace00\aspace_a0_amadeus\openclaw" /E /MOVE /XD node_modules
```
**Pourquoi** : Portabilité Multiverse — un seul `git clone` pour V0/V1/V2 (ADR-005)
**Prérequis** : `.gitignore` créé en premier
**ADR** : ADR-005 (supersède ADR-001 position)
**Effort** : 5-10 min (29MB + node_modules exclus)

---

### ✅ P0 — Déplacer _SPECS/ → aspace_a0_amadeus/_SPECS/

**Quoi** :
```powershell
robocopy "C:\Aspace00\_SPECS" "C:\Aspace00\aspace_a0_amadeus\_SPECS" /E /MOVE
```
**Pourquoi** : La spec architecturale fait partie du Container Souverain
**ADR** : ADR-005 (structure cible)
**Effort** : 2 min

---

### ✅ P1 — Archiver A0_Memory/ → PARA Archives

**Quoi** :
```powershell
robocopy "C:\Aspace00\A0_Memory" "C:\Aspace00\aspace_a0_amadeus\20_Life_OS\24_PARA_Enterprise\04_Archives_Data\A0_Memory" /E /MOVE
```
**Pourquoi** : Nettoyage racine C:\Aspace00 — mémoire va dans PARA (ADR-005 structure cible)
**Effort** : 5 min

---

### ✅ P1 — Mettre à jour doctrine_sync.sh + openclaw.json (nouveau chemin .openclaw)

**Quoi** : Changer `OPENCLAW_STATE` dans `doctrine_sync.sh` pour pointer vers le nouveau chemin :
```bash
OPENCLAW_STATE="${OPENCLAW_STATE_DIR:-$REPO_DIR/openclaw/.openclaw}"
```
**Pourquoi** : Après la migration ADR-005, `.openclaw/` sera dans `aspace_a0_amadeus/openclaw/`
**Prérequis** : P0 déplacement openclaw/ terminé
**ADR** : ADR-004 + ADR-005
**Effort** : 5 min

---

### 🔴 P0 — Restructurer 00_Amadeus (5 couches + Bio_Metrics 3 instances) — SPRINT 2b EN COURS

**Spec complète** : [`PRD-004`](../02_V1_PRD/PRD-004_00_Amadeus-Restructuration.md)
**Quoi** :
- Migrer `Vision_System/` → `01_Identity_Core/Vision_System/`
- Créer `02_Bio_Metrics/V0_Personal/` (Life Wheel + KPIs)
- Créer `02_Bio_Metrics/V1_SolarpunkKernel/` (TARDIS Protocol)
- Créer `02_Bio_Metrics/V2_BusinessPulse/` (DC/Marvel metrics)
- Créer `05_OSS_Twin/` (V0_Windows.md, V1_WSL.md, V2_OSS_Twin.md)
- Migrer `Drivers/` + `Scripts_Python/` → `10_Tech_OS/`
**Effort** : 30-60 min

---

### ✅ P2 — Supprimer A0_OSS_Twin/ (ghost folder)

**Résultat** : N'existait pas — déjà propre.

---

### ✅ P2 — Commit git Sprint 2

**Résultat** : Commit `a3bb781` (2026-02-28)

---

## HORIZON SUIVANT — Outillage Stratégique

Ces items débloquent la vision E-myth (Amadeus = Visionnaire, pas Technicien) :

| Item | Description | Prérequis |
|------|-------------|-----------|
| **Open Code install** | Installer et configurer Open Code | Sprint 2 terminé |
| **ADR-006 Tool Ecosystem** | Documenter Claude Code → Gemini CLI → Open Code | Open Code installé |
| **V1 WSL bootstrap** | Premier déploiement WSL via bootstrap.sh | Sprint 2 terminé + ADR-002 |
| **doctrine_sync V2** | Ajouter validation agents_registry.json | ADR-003 + ADR-004 |
| **Instancier Donna_DLQ** | Agent Dead Letter Queue critique dans Runtime | Post-migration |
| **52 agents inactifs** | Activer dans openclaw.json selon agents_registry | Post-migration |

---

## DÉCISIONS AMADEUS EN ATTENTE

| Décision | Impact | Urgence |
|----------|--------|---------|
| amadeus_ultimate_dna/ + .tar.gz | Archiver dans PARA ou supprimer ? (50MB) | 🟠 P1 Sprint 2 |
| deal_* vs protostar_* | Naming Runtime agents DEAL | 🟡 P2 |
| 52 agents inactifs | Activer tous ou sélectionner ? | 🟡 P2 |
| Contenu Bio_Metrics | Rédiger les .md identitaires (V0/V1/V2) | 🟡 P2 (Claude Code, pas Gemini) |
