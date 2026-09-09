# SPEC-003 : Structuration Autonome de Linear par Jules (BedRock Solarpunk)

* **Version :** 1.0.0-CANON
* **Date :** 2026-09-09
* **Architecte Souverain :** Amadou Kone (`amdkn`)
* **Agent Exécutant :** Jules (Google Labs) via MCP Linear
* **Standard :** OKF v0.2 / Hiérarchie Déterministe 7D

---

## 1. Mandat pour Jules (MCP Linear)

Jules, tu disposes de la connexion active au serveur **Linear MCP**.
Ton objectif est de structurer et d'administrer en autonomie l'espace Linear `kernel-core` selon la cosmologie A'Space OS V3 et la doctrine E-Myth.

### Les 3 Équipes / Projets Canoniques à structurer dans Linear :
1. **Équipe `Kernel Core` (KFR / KC) :**
   - **Gouverneur :** 13e Docteur (Manager Tech) + Rick Sanchez (L0).
   - **Techniciens :** Yaz (Télémétrie), Ryan (Build/Engine), Graham (Mémoire/Ontologie RDF).
   - **Périmètre :** `10_Tech_OS`, `70_Onthologies`, `40_Memory_Wiki_OKF`.
2. **Équipe `Life Core` (LC) :**
   - **Gouverneur :** 11e Docteur (Manager Life).
   - **Techniciens :** Amy (Vision), Rory (Grounding/Physiologie), River (Chronobiologie/12WY).
   - **Périmètre :** `20_Life_OS` (Gatekeepers Beth & Morty, 8 Domaines LD01-LD08).
3. **Équipe `Forge Core / Buzz Core` (FOR / BC) :**
   - **Gouverneur :** 12e Docteur (Manager Business).
   - **Techniciens :** Clara (Produit/Recherche), Bill (Forge/Code), Nardole (Dispatch/Logistique).
   - **Périmètre :** `30_Business_OS`, The OMK Office JaaS, Landing Web, SOB.

---

## 2. Labels Déterministes à Créer sur Linear
Jules doit créer les labels suivants via son outil Linear :
* `layer:5D-Gate` (Sécurité, Veto, PII, Circuit Breaker)
* `layer:4D-Cron` (Heartbeats 60s, Tâches récurrentes)
* `role:manager` (13e, 11e, 12e Docteurs)
* `role:technician` (Yaz, Ryan, Graham, Amy, Rory, River, Clara, Bill, Nardole)
* `role:dlq` (Donna Noble - Triage d'erreurs critiques)
* `status:verified-canon` (Vérifié par Amadou Kone)

---

## 3. Première Issue Canonique à Créer Immédiatement par Jules
* **Titre :** `[Kernel Core] Implémentation du compilateur RDF vers Engram Phrase Book (O(1) NVMe)`
* **Description :** Relier le graphe `70_Onthologies/onto_gate.py` à `10_Tech_OS/kernel/engram/phrase_book_aspace.json` pour automatiser l'indexation sans token.
* **Assignee :** Bill Potts / Ryan Sinclair (Jules)
* **Team :** Kernel Core
* **Priority :** Urgent (P1)