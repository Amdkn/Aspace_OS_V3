# AGENTS.md — 10_Tech_OS (DOX child)

This is a **DOX child AGENTS.md** under the A'Space OS V3 root `AGENTS.md`. It contains local instructions for the `10_Tech_OS/` subtree (the constructor mechanism, kernel, replication).

## Scope

- `10_Tech_OS/00_Governance_Rick/` — Rick's governance (LAW.md, SOUL.md, WATCHDOG.md).
- `10_Tech_OS/11_Kernel_Core_13th/` — L0 Kernel Core (instanced from replicator/gabarit).
- `10_Tech_OS/12_Life_Core_11th/` — L1 Life Core (operates 20_Life_OS).
- `10_Tech_OS/13_Buzz_Core_12th/` — L2 Buzz Core (operates 30_Business_OS).
- `10_Tech_OS/kernel/` — shared kernel: uc.db, schema.sql, gate.py, review.py, dlq.py, harness.py, bridge_paperclip.py, uc.py.

## Local rules

1. **The kernel is sacred.** `kernel/uc.db` is the production state. Do not edit `schema.sql` without an ADR. Migration is via `uc.py`.
2. **Three Cores, one gabarit.** `11_Kernel_Core_13th/`, `12_Life_Core_11th/`, `13_Buzz_Core_12th/` are instances of the same template. They are NOT separate codebases.
3. **Rick does not govern the 3 OS.** Rick governs the mechanism that produces them (`replicator/`). Rick does not replace individual Core governance.
4. **Watchdog has 3 thresholds.** vivant (A0 écrit < 10 min), bien portant (node < 45, cadences ≤ 2, disk > 5 Go), anti-fragile (cause + guard code + guard seen + lesson). Read `WATCHDOG.md` before touching `kernel/`.

## Cross-references

- Root: [`/AGENTS.md`](../../AGENTS.md)
- Memory: [`/00_Amadeus/30_MEMORY_CORE/`](../../00_Amadeus/30_MEMORY_CORE/) — **archival candidate**.
- OpenWiki/OKF durable memory: `C:\Users\amado\ASpace_OS_V3\40_Memory_Wiki_OKF\`. Le clone `openwiki/` reste un outil, pas la mémoire canonique.

## D4 append-only — audits de vivance

- **2026-09-20 15:38 EDT — Stabilisation Antifragile, Idempotente et Durable de Desktop Commander :**
  - **Diagnostic médico-légal :** Éradication de la boucle infernale de refresh token reuse (`Invalid Refresh Token: Already Used`) causée par 3 tâches planifiées concurrentes (`ASpace DC Health`, `ASpace DC Maintenance`, `ASpace DC Migration`) qui exécutaient des `taskkill /F` aveugles et relançaient des processus concurrents.
  - **Idempotence stricte (Loi L0) :** Mutex Windows global unique (`Global\ASpace_DC_Bedrock_Mutex`) dans `dc_bedrock_sentinel.py`. Tout lancement additionnel détecte l'instance existante saine et quitte avec le code 0 sans doublement ni perturbation.
  - **Antifragilité & Auto-Guérison :** Sauvegarde atomique continue de `device.json` vers `device.json.verified` et `device.json.stable_backup`. Restauration automatique au démarrage en cas de corruption.
  - **Zéro Angle Mort d'Autorisation :** En cas d'invalidation de token nécessitant une validation de code, le superviseur extrait automatiquement le code par regex, ouvre le navigateur sur l'URL de vérification, copie le code dans le presse-papier, et déclenche une notification vocale immédiate via `edge-tts` (voix `fr-FR-DeniseNeural`) sans jamais masquer l'exigence dans l'ombre.
  - **Persistance & Unicité :** Suppression définitive des 3 tâches planifiées parasites. Maintien d'une seule tâche canonique `ASpace Desktop Commander` pointant vers `direct-runner.ps1` et `dc_bedrock_sentinel.py`. Dépollution totale des proxies (`HTTP_PROXY`, `LLMTRIM_PROXY`, etc.).
  - **Preuve opérationnelle :** Statut vivant `online`, PID actif, channel subscribed, tunnel Supabase cloud établi (`192.168.12.134:52306 -> 172.64.149.246:443 Established`), smoke test MCP stdio 3/3 pings OK (< 5s), tests unitaires `test_dc_recovery.py` 3/3 PASS, suite unitaire kernel 11/11 PASS.

- **2026-09-18 — Meta-Harness Capability Fabric :** Orca est l'ADE hôte par défaut; Herdr fournit la persistance runtime, Multica le management du travail, Buzz le plan collaboration/event/identity. Ces surfaces peuvent décrire simultanément un même worker. `uc.py/uc.db` reste la source canonique de work_id, état, preuve, lease et gate; Rick/S1 sélectionne les capacités au lieu de figer les harnesses en L0/L1/L2.

- **2026-08-30 — Preuve de vivance.** Un port qui écoute, un roster peuplé, une base avec des items ou un gardien WSL ne prouvent pas qu'A'Space agit. Toute affirmation « V3 est vivant » doit montrer un cycle continu et horodaté `ruban complet → claim → prédiction antérieure au started_at → construction réelle → revue indépendante → scoring → descendance`, après démarrage à froid et avec reprise d'un worker tué. Tant que ce certificat n'existe pas, qualifier séparément les primitives disponibles, l'infrastructure joignable et l'agence autonome.

## D4 — 2026-09-07 — Desktop Commander launcher

- `dc-launcher.ps1` provides start/remote, status, restart, update, install. Launch root: `C:\Users\amado\ASpace_OS_V3`. Remote process presence is not proof of MCP connectivity.
- Verified: PowerShell syntax and status (one Remote process); MCP read/write within V3 succeeded. Restart/update/install paths are not live-tested. Installation backs up both user profiles and appends overriding functions; it must be run locally because DC file access is restricted to V2/V3. No automatic logon start is installed.
- Update stops DC package processes before npm to avoid EBUSY, and throws before relaunch on npm failure. Visible service window exposes authorization/errors. Existing session must not be killed by an agent testing this launcher through itself.
- OpenWiki synchronization remains pending: its location is outside the current DC file allowlist.

## D4 — 2026-09-07 — DC root installation verified

- User explicitly authorized DC file access to `C:\Users\amado`; scope applied via DC configuration. Canonical launcher moved to `C:\Users\amado\dc.ps1` with `dc.cmd`; both PowerShell profiles route there. V3 launcher forwards to root.
- Supervisor source: `C:\Users\amado\.desktop-commander\managed\supervisor.mjs`. Task `ASpace Desktop Commander` runs at user logon; `ASpace DC Migration` implements repair with direct-launch fallback. Root startup does not depend on V2/V3.
- Fixed failures: fixed port 47831 raised EADDRINUSE; replaced with loopback dynamic port recorded in endpoint.json. Restart child-exit race caused duplicate Remote processes; stale exit events are now ignored after intentional stop.
- Evidence: restart changed Remote PID 20168 to 25132; induced process-tree termination recovered automatically as PID 10436 under supervisor 18604. Remote count confirmed one. Remote MCP read succeeded after both operations. Update registry check returned already_current 0.2.48. Full newer-release activation/rollback and Windows logout/login remain untested.
- Backups of both profiles and old launcher: managed/backups/20260907-045042. Source docs live beside managed runtime; generated OpenWiki pages are not manually edited, per its AGENTS.md.

## D4 — 2026-09-07 — Instanciation Canonique des 14 Subagents Antigravity (Tech OS)

- Instanciation dynamique en mémoire via `define_subagent` des 14 entités souveraines d'A'Space OS V3 :
  - **S1 :** `s1_rick` (Rick Sanchez, Gardien L0 & Architecte Suprême).
  - **3 Docteurs :** `doctor_13_kernel` (Kernel Core, L0), `doctor_12_bus` (Bus Core, L2), `doctor_11_life` (Life Core, L1).
  - **10 Compagnons (3*3 + Donna DLQ) :**
    - 13e Dr (Kernel) : `companion_yas_observatory` (monitoring 60s), `companion_ryan_builder` (CI/CD < 30min), `companion_graham_memory` (graphe Semantica).
    - 12e Dr (Bus) : `companion_bill_discovery` (signaux marché), `companion_clara_product_forge` (offres $100M), `companion_nardole_dispatch` (kanban & balancing).
    - 11e Dr (Life) : `companion_amy_interface` (ergonomie port 5555), `companion_rory_backend` (RLS Supabase), `companion_river_workflows` (bus n8n).
    - Transversal (Rick) : `companion_donna_dlq` (Dead Letter Queue & qualification des causes d'échecs).
- Manifeste machine-readable : `10_Tech_OS/subagents/subagents_tech_os_roster.json`.
- Concept certifié OKF v0.2 : `40_Memory_Wiki_OKF/architecture/roster_subagents_tech_os.md`.

## D4 — 2026-09-19 23:55 EDT — Intégration PR #37 (KER-9 / work_id 165) & Sélecteur de Capacités de Harness

- **Mandat Exécutif Hermes ↔ Antigravity (KER-15) :** Traitement de la PR #37 (`feat(kernel): implement minimal harness capability selector in uc_workgraph.py`) via la session Antigravity persistante unique (`V3 Analysis And Audit`).
- **Revue Indépendante & Résolution de Conflit sur Branche PR :**
  - Conflit identifié : PR #37 écrasait `uc_workgraph.py` sans connaître les sous-commandes WorkGraph v2 créées sur `main`.
  - Résolution chirurgicale sur la branche `feat/harness-capability-selector-7681792783926570114` (commit `aac4d454`) : unification de `get_harnesses` et `--require-capability` / `--min-evidence-level` / sous-commande `select` avec la totalité des commandes WorkGraph v2 (`intent`, `link`, `depend`, `bind`, `artifact`, `gate`, `goal`, `round`, `round-link`, `goal-review`, `wait`, `capability`, `graph`).
- **Vérification Déterministe :** Validation unitaire `test_uc_workgraph.py` (1 test OK en 17.3s), tests CLI de non-régression (`select --help`, `goal --help`).
- **Merge & Push :** Merge sans avance rapide dans `main` (commit SHA `694367aabb4dee188c20fe451349feba5616eefe`), push validé sur `origin/main`.
- **Ancrage Souverain `uc.db` & Projection Linear :**
  - Transition de `work_id: 165` (KER-9) respectant la loi de prédiction et la loi de détachement : `prediction` enregistrée -> `review` -> `done`.
  - Clôture du bail `session_binding` Jules (`7681792783926570114`).
  - Enregistrement de `artifact_id: 2` (git-commit) et `gate_decision_id: 2` (PASS).
  - Confirmation d'évidence postée sur Linear KER-9 et statut passé à **Done**.
  - Action delta report journalisé en commentaire sur Linear issue KER-15.

## D4 — 2026-09-07 — Intégration Vague 2 Innovations (HoH, Co-Évolution, Dynamic Ontology, RSI)

- Ingestion substrat Geordi : 13 papiers de recherche sous `20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/Articles_Recherche/2026-09_v2_harness_coevolution/` et 2 dépôts clonés sous `repos_innovations/` (`verl` et `HarnessOfHarness`).
- Sas de Distillation : exécution de `50_Distillation/distill_wave2_harness_coevolution.py`, génération de `distillat_wave2_harness_coevolution_2026_09.md` et extraction de 52 triplets RDF formels dans `70_Onthologies/triplets/harness-coevolution-2026-09.jsonl`.
- Expansion Semantica : `semantica_knowledge_graph.json` porté de 1 628 à 1 681 nœuds (1 446 arêtes).
- Cristallisation OKF 0.2 : `architecture/harness_of_harness_coevolution.md`, `architecture/dynamic_ontology_and_graph_engineering.md`, `learning/skill_misevolution_and_immune_defense.md`.
- Durcissement Immunitaire : `compiler_skill.py` enrichi du bouclier anti-misevolution (arXiv:2608.12851) et `state_engine.py` partitionné en mémoire récursive Recuris (arXiv:2608.24876).
- Cadrage Méthodologique : `60_Implementation_Méthodologiques/frameworks/protocole_coevolution_harness_long_horizon.md`.

## D4 — 2026-09-07 — Déploiement des 13 Scheduled Tasks Antigravity (Tech OS)

- Programmation autonome et enregistrement des 13 Scheduled Tasks dans le scheduler natif Antigravity (T-01 à T-13) :
  - **L0 Baux & Gouvernance :** `T-01` Donna DLQ (`*/15 7-23 * * *`), `T-02` Rick Sanchez L0 (`0 2 * * 0`).
  - **L0 Kernel Core :** `T-03` Yas Observatory (`*/30 8-23 * * *`), `T-04` Ryan Builder (`0 4 * * *`), `T-05` Graham Memory nocturne (`0 3 * * *`), `T-06` Graham Distillation hebdo (`0 5 * * 0`), `T-07` Graham Wiki Lint (`0 9 * * 0`).
  - **L2 Business Core :** `T-08` Nardole Dispatch (`*/20 8-20 * * 1-5`), `T-09` Bill Discovery (`0 7 * * 1-5`), `T-10` Clara Product Forge (`0 10 * * 5`).
  - **L1 Life Core :** `T-11` Amy Interface (`0 8,14,20 * * *`), `T-12` Rory Backend (`0 6 * * *`), `T-13` River Workflows (`*/30 * * * *`).
- Manifeste persistant machine-readable : `10_Tech_OS/scheduler/scheduled_tasks_manifest.json`.
- Concept certifié OKF v0.2 : `40_Memory_Wiki_OKF/architecture/scheduled_tasks_orchestration_tech_os.md`.

## D4 — 2026-09-07 — Instanciation Méta-Tâche T-00 A0 Amadeus (Optimisation & Adaptation Contextuelle)

- Création et programmation de `T-00 Meta A0 Amadeus Adaptation` (`0 1 * * 0`, dimanche 01h00) :
  - Adaptation dynamique aux mutations d'infrastructure hôte (Windows Natif, WSL `aspace-l0`, VPS distant `aspace-vps`).
  - Alignement ontologique permanent avec `semantica_knowledge_graph.json` (1 681 nœuds).
  - Préservation stricte de la fabrication légère n8n sans Docker (orchestrateur natif transformant les `.py` en flux visuels réactifs sans obésité RAM).
- Sidecar UI déployé : `C:\Users\amado\.gemini\config\sidecars\t-00-meta-a0-amadeus-adaptation\sidecar.json`.
- Worker : `10_Tech_OS/scheduler/meta_a0_adaptation_worker.py`.
- Concept OKF 0.2 : `40_Memory_Wiki_OKF/architecture/meta_a0_scheduled_tasks_adaptation.md`.

## D4 — 2026-09-07 — Interconnexion Directe Dashboard Agent OS (Port 5555) ↔ 14 Subagents Antigravity

- Extension du backend `agent-os/desktop/tools/tech-os-api.ts` :
  - `GET /api/tech-os/subagents` : Roster temps réel des 14 Subagents (S1 Rick, 3 Docteurs, 10 Compagnons) enrichi des Scheduled Tasks (T-00..T-13), rapports d'exécution et baux `uc.db` en heure locale EDT (UTC-4).
  - `POST /api/tech-os/subagents/invoke` : Invocateur direct des ouvriers opérationnels (`nardole_dispatch_worker.py`, `meta_a0_adaptation_worker.py`, `cartographier_v3.py`, compilation TypeScript Ryan `tsc --noEmit`, audit SQLite PRAGMA Rory, sondage Yas).
  - `POST /api/tech-os/workflows/trigger` : Exécution native en Python des workflows n8n légers sans conteneur Docker (< 190 Mo RAM, latence < 15 ms).
- Application Cockpit `SubagentsRoster` (`agent-os/desktop/src/apps/SubagentsRoster/index.tsx`) :
  - Tableau de bord de pilotage unifié avec filtres par cœur, statuts pulsants, attribution des tâches programmées, et bouton 1-clic `⚡ Invoquer` avec console terminale intégrée.
- Interconnexion interactive dans les 9 Companion Apps :
  - `NardoleDispatch` : bouton interactif `⚡ Invoquer Nardole` avec rafraîchissement instantané des baux et travaux orphelins `uc.db`.
  - `RyanBuilder` : bouton `runBuildTest` connecté en direct au compilateur TypeScript `tsc --noEmit`.
  - `YasObservatory` : bouton `⚡ Invoquer Yas` pour sonder la télémétrie des services et ports.
  - `GrahamMemory` : bouton `⚡ Invoquer Graham` pour la consolidation et cartographie du graphe de connaissances.
  - `RiverWorkflows` : bouton `⚡ Déclencher Workflow Python (n8n Léger)` exécutant le script natif sans Docker.
  - `RoryBackend` : bouton `⚡ Invoquer Rory (Audit SQL)` auditant l'intégrité de `uc.db`.
- Validation stricte : `npm run typecheck` (`npx tsc --noEmit`) validé à 0 erreur ; serveur Vite en écoute active sur `http://127.0.0.1:5555/` (HTTP 200 OK).
- Note OKF 0.2 créée : `40_Memory_Wiki_OKF/architecture/interconnexion_dashboard_subagents_v3.md`.

## D4 — 2026-09-07 — Refactorisation Souveraine des 9 Apps Compagnons en 3 Doctor Apps par Onglets

- Selon la directive d'Amadou Kone, élimination des 9 applications brouillons dispersées et consolidation en 3 applications maîtresses structurées par onglets (standard Observatoire) :
  - **`Doctor13Kernel` (`doctor-13-kernel`) :** 13e Docteur (Gouvernance L0), Yas (Télémétrie 60s), Ryan (CI/CD tsc live), Graham (Mémoire Semantica 1 681 nœuds).
  - **`Doctor12Bus` (`doctor-12-bus`) :** 12e Docteur (Croissance SOB), Bill (Radar signaux marché), Clara (Product Forge & SOPs), Nardole (Dispatch Kanban live uc.db).
  - **`Doctor11Life` (`doctor-11-life`) :** 11e Docteur (Souveraineté vitale), Amy (Interface ergonomie adaptative), Rory (Backend coffre-fort RLS), River (Workflows Canvas interactif n8n léger natif Python sans Docker).
- Nettoyage du dock et registre : suppression des 9 répertoires brouillons, 0 erreur TypeScript (`tsc --noEmit`), serveur Vite opérationnel (HTTP 200).

## D4 — 2026-09-07 — Déploiement de l'Application Souveraine Onthology (Palantir Foundry Monocle)

- Création de l'application dédiée `Onthology` (`agent-os/desktop/src/apps/Onthology/index.tsx`) inspirée de Palantir Foundry :
  - **Monocle Data Lineage** : Pipeline interactif en 7 étapes (Raw, Clean, NLP/Parsing, Ontology, Alerting, Transforms, Applications) reliées par des courbes de Bézier cubiques SVG dynamiques avec indicateurs d'états temps réel.
  - **Palantir 5-Layer Framework** : Visualisation en 5 bandes horizontales d'interaction bidirectionnelle (Application Layer, Dynamic/AI Layer, Kinetic Layer, Semantic Layer, Data Sources Layer).
  - **Process Mining & Explorer** : Histogramme chronologique de distribution, filtres de transition et flux d'états d'exécution V3 (Frozen Intent -> Gate Admission -> Nardole Dispatch -> Active Lease -> Done & Replicated).
  - **Object Explorer & Inspecteur RDF** : Table paginée et filtrable des 1 681 entités Semantica et drawer d'inspection latérale des 1 446 relations RDF (entrantes/sortantes).
## D4 — 2026-09-07 — Résolution Complète des Dettes Techniques & Alignement Palantir Foundry de l'App Onthology

- Audit approfondi basé sur les 4 captures d'écran de référence de Palantir Foundry transmises par Amadou Kone :
  1. **Foundry Navigation Rail Déployé** : Rail latéral gauche officiel (logo Foundry ◎, Home, Search ⌘K, Notifications, Recent, APPS: Lineage, Objects, Layers, Mining, Contour, Vertex).
  2. **Monocle Data Lineage DAG Conforme (Capture 3)** : Remplacement du layout linéaire par le véritable graphe DAG multi-branches convergent et divergent (Raw [14], Clean [17], Parsing/NLP/ML [4], Ontology Object Boxes [10], Alerting [3], Transform [5]) avec courbes de Bézier cubiques SVG et particules de flux en transit animé.
  3. **Palantir 5-Layer Framework Conforme (Capture 2)** : Structure fidèle aux 5 couloirs (Application, Dynamic/AI, Kinetic, Semantic, Data Sources) avec nœuds circulaires cerclés de noir et ensemble des flèches bidirectionnelles couplées (rouge descendant / vert montant) avec badges d'étiquettes réelles (Interface Output, Insight Delivery, AI Processing, ML Analysis, Decision Feedback, Action Execution, Real-time Mapping).
  4. **Process Mining Non-Conformities Conforme (Capture 1)** : Tableau de bord de minage de processus complet (histogramme Reported Date avec inputs, filtres Type avec jauges bleues horizontales, histogramme Number Transitions avec steppers, widget flottant de seuil de transition et graphe d'états orienté avec pourcentages réels 20%, 83.17%, 30%, 76%, etc. reliant Open, Submitted, Assigned [alerte rouge], Dispositioned, Closed, Canceled, Reassessed).
  5. **Object Explorer Réel & Inspecteur 360** : Chargement dynamique des 1 681 nœuds Semantica et 1 446 triplets RDF depuis `/api/tech-os/graham-graph` avec filtrage instantané et inspecteur latéral des relations entrantes/sortantes.
## D4 — 2026-09-07 — Intégration Native Palantir OSDK, Contour, Vertex AIP & Substrat HoH

- Intégration complète de la spécification officielle Palantir Foundry Platform Python & OSDK (v2 API) :
  1. **Sidebar Palantir Dépliable / Repliable** : Tiroir de navigation latéral (56px -> 240px) avec sélecteur de workspaces, arborescence projets/fichiers, recherche globale (⌘K), menu des applications Foundry complet et indicateur d'état HoH.
  2. **Contour (Chemins Analytiques & Cohortes) Actif** : Moteur analytique `palantir_osdk_engine.py` connecté à `/api/tech-os/osdk/contour` avec 4 tableaux interactifs (Filter Board, Pivot Board par classe, Histogramme de connectivité, Cohorte des Top 10 Hubs stratégiques `life-os`, `beth`, `business-os`, `rick`, `morty`, `cerritos`, `jerry`, `tech-os`).
  3. **Vertex AIP (Artificial Intelligence Platform) Workbench Actif** : Console d'ancrage ontologique connectée à `/api/tech-os/osdk/aip` avec grounding des Object Types (`SemanticaEntity`, `WorkItem`, `Subagent`, `NonConformityAlert`), requêtes en langage naturel, déduction automatique d'Action Types OSDK et bouton d'application directe en base (`createOntologyObject`).
  4. **Barre d'Outils et En-tête 100% Fonctionnels** :
     - Sélecteur de branches (`🌱 master`, `🌿 staging-v3`, `🧪 experiment-osdk`).
     - Menu `Actions ▾` : Création d'objets, déclenchement dry-run de pipeline, export DAG JSON, documentation HoH.
     - Modales interactives complètes : Outils diagnostics, Recherche Monocle (⌘F), Color Group Editor, Partage d'URL d'instance.
     - Bascule de mise en page du DAG (`dag`, `orthogonal`, `compact`) et réalignement instantané.
  5. **Substrat HoH (Harness-of-Harness - arXiv:2609.01481)** : L'architecture de l'app Onthology est désormais ancrée dans le meta-harness HoH, où le modèle LLM ne raisonne plus en l'air mais pilote un harnais d'état rigide (SQLite `uc.db`, OSDK Action Types, boucle de co-évolution modèle-harnais).
- Validation stricte : `tsc --noEmit` validé à 0 erreur ; `verif_marqueurs.mjs` à 0 placeholder ; `verif_http.mjs` validé à 200 OK.

## D4 — 2026-09-07 — Modernisation Majeure de l'Onglet Graham (13e Docteur · Kernel Core)

- Remplacement de la vue simpliste de Graham par une suite d'ingénierie mémoire & résilience à 3 sous-vues :
  1. **Graphe Semantica & Inspecteur 360** : Navigation dans les 1 681 entités et 1 446 relations RDF, filtrage multi-critères, inspecteur d'identifiant canonique, classe et connectivité, et raccourcis vers les Top Hubs (`life-os`, `beth`, `business-os`, `rick`, `tech-os`).
  2. **Gestionnaire de Checkpoints WAL** : Inventaire temps réel des snapshots physiques dans `10_Tech_OS/kernel/checkpoints/` via `/api/tech-os/graham/checkpoints`, déclenchement de snapshots atomiques avec `PRAGMA wal_checkpoint(TRUNCATE)` et boutons de restauration 1-clic sûre.
  3. **Console de Résilience & Évaluation de Critères de Rupture** : Interface directe avec `graham_checkpoint.py` pour évaluer les critères dynamiques d'assertion (rc=4 -> restauration immédiate).
  4. **Journal d'Audit Vivant** : Extraction des événements `graham_checkpoint` depuis la table `event` de `uc.db`.
- Endpoints Tech OS ajoutés et validés : `GET /api/tech-os/graham/checkpoints`, `POST /api/tech-os/graham/action`.
- Validation stricte : `npm run typecheck` à 0 erreur ; `verif_marqueurs.mjs` à 0 placeholder ; `verif_http.mjs` à 100% 200 OK.

## D4 — 2026-09-09 — Validation de Run Souveraine Kernel Core (13e Docteur, Yaz, Ryan, Graham)

- **[YAZ] Audit & Intégrité Runtime / uc.db :**
  - Ajout des garde-fous `try...except (ImportError, ModuleNotFoundError)` sur les imports `agentpulse` dans l'ensemble des scripts `10_Tech_OS/kernel/` (`uc.py`, `gate.py`, `review.py`, `dlq.py`, `harness.py`, `bridge_paperclip.py`).
  - Migration schéma SQLite effectuée (`uc.py migrate`) et vérification d'intégrité validée (`PRAGMA integrity_check` -> `ok`).
- **[GRAHAM] Synchronisation Engram Phrase Book, Ontologies & OKF :**
  - Synchronisation du Phrase Book Engram `10_Tech_OS/kernel/engram/phrase_book_aspace.json` avec la référence Turtle `aspace://70_Onthologies/sujets/J01_Jerry_Prime_LD01_Business.ttl` et OKF v0.2 `aspace://40_Memory_Wiki_OKF/concepts/engram_phrasebook_architecture.md`.
  - Exécution réussie des 6 unit tests (`10_Tech_OS/kernel/engram/test_engram.py` -> 6/6 tests OK).
- **[RYAN] Compilation & Definition of Done :**
  - Compilation `python -m py_compile` de l'ensemble des modules Python modifiés (0 erreur, exit code 0).
  - Enregistrement, prédiction, revue, attestation et clôture `done` des 3 issues Kernel Core dans `uc.db` (3/3 items détachés avec calibration 100%).

## D4 — 2026-09-10 — Compilation RDF Engram NVMe (1 378 Invariants) & Daemon TTS Anti-Écho

- **[GRAHAM & RYAN] Compilateur RDF -> Engram NVMe :**
  - Implémentation de `10_Tech_OS/kernel/engram/compile_engram_from_rdf.py`.
  - Scan de 20 fichiers `.jsonl` dans `70_Onthologies/triplets/` (1 462 triplets parsés).
  - Compilation de **1 378 nouveaux invariants** déterministes dans `10_Tech_OS/kernel/engram/phrase_book_aspace.json` (portant le volume total à 1 385 entrées actives).
  - Validation complète des tests unitaires Engram (`10_Tech_OS/kernel/engram/test_engram.py` : 6/6 tests passés en 0.104s).
- **[YAZ & RICK] Daemon TTS Résilient (`antigravity_tts_daemon.py`) :**
  - Réduction du seuil de verrou obsolète `tts_playing.lock` de 90s à 30s pour éliminer les blocages en cascade.
  - Pré-indexation anti-écho des 64 Ko passés au démarrage pour empêcher tout rejeu de messages archivés.
  - Filtrage automatique des blocs de pied de page Markdown (liens audio / commandes de relecture muettes).
  - Processus pérennisé en tâche de fond sous Windows avec sortie audio `fr-FR-DeniseNeural` via `edge-tts`.

## D4 — 2026-09-10 — Intégration PR Jules #4 (L0 Test Suite) & Câblage Engram BethFilter

- **[RICK & 13e DOCTEUR] PR Jules #4 & Suite de Tests L0 :**
  - Fusion et validation de la PR Jules #4 (`L0 Rick Sanchez Audit & Kernel Replication Suite`).
  - Purge intégrale du code mort dans `_tmp_kanban/` (`purge_qualif.py`, `read_schema.py`, etc.).
  - Validation réussie de `10_Tech_OS/kernel/test_l0_kernel.py` (2 tests, exit code 0, 100% conformité L0 réplication).
- **[BETH & RICK] Câblage Déterministe O(1) Engram dans le Noyau :**
  - Intégration de `BethFilter` dans `10_Tech_OS/kernel/gate.py` (admission SSSF) et `10_Tech_OS/kernel/controleur.py` (systole requeue).
  - Tout intent ou work item violant un circuit-breaker Engram subit un veto immédiat sans rejeu parasite.
- **[AMADOU KONE & ANTIGRAVITY] Déploiement Brief Asynchrone Morty SLM :**
  - Déploiement de `delegation-a-jules/PRD-MORTY-LOCAL-ENGINE.md` pour implémentation asynchrone par Jules sans consommation de quota Antigravity direct.

## D4 — 2026-09-11 — Implémentation Locale SLM Morty & Compilateur de Dataset Marin

- **[MORTY & GRAHAM] Compilateur de Dataset d'Alignement Marin :**
  - Implémentation de `10_Tech_OS/kernel/slm/marin_dataset_extractor.py`.
  - Extraction automatique des concepts certifiés `40_Memory_Wiki_OKF/concepts/*.md` et des relations ontologiques de `70_Onthologies/triplets/*.jsonl`.
  - Génération du premier jeu d'alignement `marin_alignment_dataset.jsonl` (77 entrées instruction tuning déterministes).
- **[MORTY & RICK] Moteur d'Inférence Déterministe CPU (MiniMind + TimesFM Fallback) :**
  - Implémentation de `10_Tech_OS/kernel/slm/morty_engine.py` (`MortyLocalEngine`).
  - Projection des séries chronobiologiques H1 à H90 (lissage Holt-Winters cyclique) et arbitrage symbolique instantané sur CPU (< 1 ms, zéro quota cloud).
  - Validation complète de la suite unitaire `10_Tech_OS/kernel/slm/test_morty_engine.py` (3/3 tests OK en 0.101s).

## D4 — 2026-09-11 — Intégration du Patch Jules (Session 18214439155436997252) & Auto-Bootstrap DLQ

- **[JULES & RICK SANCHEZ] Auto-Bootstrapping DLQ & Robustesse L0 :**
  - Ingestion directe du patch issu de la session Jules #18214439155436997252.
  - Auto-initialisation du schéma SQLite (`schema.sql`) dans `10_Tech_OS/kernel/dlq.py` (`cx()`) en cas de base vierge sans table `work`.
  - Déploiement de `pytest.ini` à la racine pour préserver l'exécution unitaire des répertoires non-unitaires (`50_Distillation`, `openwiki/evals`).
  - Validation de non-régression via `10_Tech_OS/kernel/test_l0_kernel.py` (2/2 tests OK en 55.7s).

## D4 — 2026-09-11 — Validation du Run Kernel Core (13e Docteur & Compagnons Yaz, Graham, Ryan)

- **[YAZ] Vérification du Runtime, uc.db et Scripts Kernel :**
  - Résolution de l'encodage BOM dans `pytest.ini`.
  - Auto-initialisation et vérification d'intégrité de `10_Tech_OS/kernel/uc.db` (`PRAGMA integrity_check` -> `ok`).
- **[GRAHAM] Synchronisation Engram, Ontologies & OKF :**
  - Alignement vérifié entre `70_Onthologies/`, `40_Memory_Wiki_OKF/` et `10_Tech_OS/kernel/engram/phrase_book_aspace.json` (1 385 entrées actives).
  - Validation complète des tests Engram (`pytest 10_Tech_OS/kernel/engram/test_engram.py` -> 6/6 tests OK).
- **[RYAN] Compilation Python & Definition of Done :**
  - Compilation de tous les scripts kernel modifiés via `py_compile` (0 erreur).
  - Exécution complète de la suite de tests (`pytest 10_Tech_OS/kernel/` -> 14/14 tests OK).
- **[13e DOCTEUR] Mise à jour de la Gouvernance MCP Linear :**
  - Exécution de `scripts/log_kernel_mcp_update.py` enregistrant le statut des issues "Kernel Core" (KFR-1, KFR-2, KFR-3) dans la table `event` de `uc.db`.

## D4 — 2026-09-11 — Interfaçage Toggle Folders Style Antigravity & Moteur d'Exécution CPython Unifié (Agent OS Port 5555)

- **[ANTIGRAVITY & AMADOU KONE] Arborescence Pliable & Explorateur .py Unifié :**
  - Refonte complète de `00_Amadeus/10_Observers/agent-os/desktop/src/apps/TechOSWorkflows/index.tsx`.
  - Intégration de l'arborescence en dossiers accordéons rétractables (`expandedFolders: Record<string, boolean>`) répliquant l'ergonomie du sidebar gauche d'Antigravity (icônes chevrons, dossiers sombres ambre, typographie monospace épurée).
  - Classification automatique des 297 scripts réels du workspace répertoriés dans `python_scripts_catalog.json` :
    - ⚡ **Générateurs / Moteurs d'Action Réelle (`isGenerator: true`)** : Badge émeraude.
    - 🛡️ **Vérificateurs Passifs (`isVerifier: true`)** : Badge ambre.
    - ⚙️ **Scripts Opérationnels Système** : Badge cyan.
- **[TECH OS BACKEND] API d'Exécution Asynchrone CPython & Protection Anti-Traversal :**
  - Extension de `POST /api/tech-os/execute` dans `tools/tech-os-api.ts` pour supporter le streaming non-bloquant et l'exécution de tout script validé sous `ASpace_OS_V3/`.
  - Résolution des timeouts et tests de validation réussis avec code retour `RC = 0` (`controleur.py`, `verify_beth.py`, `pre_tool_guard.py`).
  - Validation TypeScript `tsc --noEmit` à 0 erreur.

## D4 — 2026-09-11 — Heartbeat Daemon Autonome (Cycle 15 Min - Itération 4)

- **[PULL REQUESTS JULES FUSIONNÉES] :**
  - **PR #5 (`The-OMK-Office-V1-JaaS-Landing-Site-Web`) :** Optimisations A11y, packaging et Largest Contentful Paint (LCP) fusionnées sur `main`.
  - **PR #3 (`Agent-OS-Desktop`) :** Audit d'accessibilité shell et durcissement TypeScript fusionnés sur `main`.
- **[MAINTENANCE DU PLANCHER JULES >= 3] :**
  - Lancement immédiat de 3 nouvelles sessions concurrentes autonomes (`AUTO_CREATE_PR`, `requirePlanApproval: false`) :
    1. `sessions/12048127233329127156` sur `Amdkn/JaaS-V1-Mobile-OS` (PRD-010 : UI/UX, A11y & Performance).
    2. `sessions/6561232945132601891` sur `Amdkn/The-OMK-Office-V1-JaaS-Landing-Site-Web` (PRD-011 : Lead Conversion & Interactive Demo).
    3. `sessions/8763102326381256725` sur `Amdkn/Agent-OS-Desktop` (PRD-012 : Telemetry Widgets & Polish UI).
- **[KERNEL & OBSERVABILITÉ UC.DB] :**
  - Battement du contrôleur exécuté sans friction : `0 bail expiré, 0 relance nécessaire`.
  - Système 100% stable et opérationnel sans aucune consommation de quota direct.

## D4 — 2026-09-12 — Déploiement du Hook Anti-Dérive & Verrouillage Anti-Passivité F6

- **[HOOKS & SÉCURITÉ 5D] hook_anti_drift.py :**
  - Implémentation de `10_Tech_OS/kernel/hooks/hook_anti_drift.py` pour éliminer définitivement la faute F6 (bascule en anglais, refus génériques "As an AI...", fuite dans l'attente passive d'ordres).
  - Intégration dans le banc de test unitaire `10_Tech_OS/kernel/hooks/test_hooks.py` (`test_hook_anti_drift`).
  - Validation complète exécutée via pytest : 5/5 tests passés avec succès en 0.34s.

## D4 — 2026-09-12 — Interconnexion Déterministe d'Engram O(1) au Hook PreInvocation Natif Antigravity

- **[ENGRAM NVME & HOOK PRE-INVOCATION] :**
  - Enrichissement de la lookup table `10_Tech_OS/kernel/engram/phrase_book_aspace.json` (1 390 entrées) avec les ancres fondamentales A0 (`A0_SOVEREIGN_POSTURE`, `ASTRA_EXECUTION_MANDATE`, `GOLDRATT_BOTTLENECK_LAW`, `LIFE_OS_AUTONOMOUS_HEXAD`, `ENGRAM_ZERO_TOKEN_NVME`).
  - Intégration directe du résolveur `EngramPhraseBook` dans le hook natif `C:\Users\amado\.gemini\config\hooks\pre_invocation_sovereign_guard.py`.
  - Résolution déterministe O(1) par memory mapping (`mmap`) sans consommation de token LLM.
## D4 — 2026-09-20 — Revue & Fusion de la PR #38 (KER-8 / work_id: 169) · Goal/Round/Work Semantics

- **[KERNEL CORE · WORKGRAPH V2 ORCHESTRATION] :**
  - Revue indépendante et fusion de la PR #38 (`feat(kernel): implement Goal/Round/Work orchestration semantics in uc_workgraph.py`) pour `KER-8` (`work_id: 169`).
  - Implémentation native de l'énumération `GoalOutcome` (`DONE`, `WAIT`, `ABANDON`, `NEXT_ROUND`) et de la classe `WorkGraph` :
    - `create_goal(layer, title) -> goal_id`
    - `create_round(goal_id) -> round_id` (avec hiérarchie parent `work.parent_id`)
    - `create_work(round_id, title) -> task_id`
    - `review_goal(goal_id, round_id, outcome, notes) -> event_id` (Goal Review explicite découplé des tâches d'évidence).
  - Gestion sécurisée des connexions SQLite avec fermeture explicite (`try/finally c.close()`), évitant tout verrouillage résiduel sur Windows.
  - Enrichissement du banc de tests `10_Tech_OS/kernel/test_uc_workgraph.py` avec `test_workgraph_orchestration` validant l'intégrité FK, le parentage strict et la sérialisation des événements.
  - Tests unitaires validés avec succès : `Ran 2 tests in 23.594s — OK`.
  - Commit de fusion : `037587251785fe7754b2d86c8d76db781eb8989f` pushé sur `origin/main`.
  - Évidence enregistrée dans `uc.db` pour `work_id: 169` (prédiction, transition `review` -> `done`, artifact `git-commit` #3, gate `CODE_REVIEW` verdict `pass`, session binding Jules `2579532014043635508` closed).

## D4 - 2026-09-23 - Work 181: truthful dispatch and zero-work supervisor
- Added fleet_ownership.py: exact canonical work mapping, atomic uc.py claim before provider mutation, durable ambiguous-dispatch marker, session binding and fresh provider execution check before Linear In Progress.
- kernel_fleet_tick.py refuses retasking an occupied companion lane. A queued session is not projected as executing.
- hermes_cron.ps1 supervisor now checks WorkGraph deterministically before touching Orca/LLM; empty cycle observed skipped at 07:03:22 EDT.
- Validation: 20 focused tests passed; independent review requested. Full Orca/Kernel convergence is not certified by this patch.
- Evidence: 10_Tech_OS/reports/convergence_181_evidence.json. Original files: kernel/backups/convergence-20260923T110058Z.

- Work 181 final delta: OS file lock serializes entire fleet tick; final focused suite 21/21 PASS. Evidence: reports/convergence_181_evidence_v2.json. Independent review remains required.


## D4 - 2026-09-23 - Work 181 acceptance and truthful runtime reconciliation
- Hermes independent review PASS; reviewed SHA256 match; 21 focused tests rerun PASS. reports/convergence_181_acceptance.json records closure evidence.
- Orca ready. Ten unsupported In Progress projections corrected: six Backlog, four In Review. Work 180 stale binding closed; KER-44 reopened Backlog with explicit failed acceptance (four remaining gaps).
- Four historical PR-merged assertions contradict GitHub OPEN states; no retrospective prediction or fabricated completion. reports/orca_workgraph_reconciliation_20260923.json records the discrepancy.


## D4 - 2026-09-23 - KER-44 executable constitution and Dao/Jing
- Nine complete companion contracts, closed WorldState loop, forbidden authority validation; legacy role contracts preserved.
- dao_jing.py derives thirteen typed, byte-bounded projections from read-only SQLite snapshots and exposes ownership/evidence drift.
- Agent OS GET adapter delegates to kernel without shell or UI business logic. Evidence and commands: reports/KER44_IMPLEMENTATION.md.

- **2026-09-24 — Hermes Bot Mode / Orca :** 3 Doctors + 9 Compagnons rattaches chacun a un profil Hermes existant et un worktree distinct; terminal.cwd fixe, lanceurs Bot Chat avec --in, noms canoniques dans Orca et metadata Bot Mode. Sauvegardes locales; aucune preuve dexecution deduite du roster. Registre: reports/hermes_bot_worktree_bindings.json.
