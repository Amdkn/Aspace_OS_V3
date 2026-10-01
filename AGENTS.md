# AGENTS.md — Canon A'Space OS V3 & Meta-Routeur DOX

> **Loi L0 — Rick.** *Un système qui ne sait pas se répliquer n'est pas un système,
> c'est un document.*
> 
> **Architecture Souveraine & Pyramide Déterministe à 7 Niveaux.**
> Ce fichier racine agit comme le **Meta-Routeur du War Room (Hivemind)**. Il ne centralise plus artificiellement les détails locaux mais aiguille le trafic vers les `AGENTS.md` arborescents (DOX) de chaque sous-dossier maître pour éliminer la famine de contexte et économiser le Tool Calling.

---

## 0. Bootstrap mémoire obligatoire — avant tout routage

**Invariant local canonique :**
- `40_Memory_Wiki_OKF/` = mémoire longue certifiée et canonique.
- `MEMORY.md` = pointeur de bootstrap uniquement.
- `_INBOX/handoffs/` = continuité opérationnelle entre sessions.
- `ASPACE_ACTIVE_INTENTS.yaml` = projection locale des intentions A0 actives; les IPBD persistants vivent dans Supabase `aspace`.
- **Interdit :** créer un répertoire mémoire/continuity parallèle hors de `ASpace_OS_V3` parce qu'une branche ou un checkout ne montre pas un fichier attendu.
- Si un chemin canonique manque, **corriger d'abord la branche/le checkout/worktree**, puis relire le canon.

Toute session ChatGPT, Hermes, Codex, Antigravity, Claude Code, Jules ou autre harness qui intervient sur V3 doit appliquer ce bootstrap avant de reconstruire l'architecture depuis un handover, un ticket ou un historique de chat.

## 1. La Pyramide à 7 Niveaux d'A'Space OS V3

```
      ▲
     / \     [7D] HIVEMIND & WAR ROOM : 13e Docteur / Arbitrage transversal Amadou Kone
    /---\
   / 6D  \   [6D] IDENTITÉS & SOUL FILES : CLAUDE.md / GEMINI.md / Soul.md (Air Traffic Control)
  /-------\
 /   5D    \ [5D] HOOKS & VALIDATION GATES : Coupe-circuit déterministe, Veto PII, Gates SSSF
/-----------\
|    4D     | [4D] CRONS & HEARTBEATS : Télémétrie 60s Yas, Tâche hebdo Distillation 50_
|-----------|
|    3D     | [3D] SKILLS & SERVEURS MCP : Ryan ADW, Tool Calling, Antigravity SDK
|-----------|
| SUBSTRAT  | [MACRO] WEBHOOKS & BROKERS : Event Log append-only uc.db (Zero Kafka lourd)
|-----------|
|  PANTRY   | [MICRO] SILVER PLATTER & MÉMOIRE : SQLite WAL, Semantica RDF Graham, OKF 0.2
└───────────┘
```

---

## 2. Meta-Routeur DOX — Cartographie des Sub-AGENTS.md

Pour éviter d'ingérer des dizaines de documents à chaque prompt, l'agent charge le `AGENTS.md` racine puis **préfère** le `AGENTS.md` du sous-dossier concerné. Une mission transversale peut lire les autres routeurs pertinents : le découpage économise le contexte, il ne cloisonne jamais la compréhension.

| Organe / Dossier | Rôle dans V3 & Niveau Pyramide | Fichier d'Aiguillage Dédié |
| :--- | :--- | :--- |
| **`50_Distillation/`** | **GATE DE PROMOTION MÉMOIRE/CANON** [5D]. Il certifie la promotion vers mémoire/ontologie; il ne bloque ni Capture IPBD, ni diagnostic, ni exécution réversible. | [`50_Distillation/AGENTS.md`](file:///c:/Users/amado/ASpace_OS_V3/50_Distillation/AGENTS.md) |
| **`70_Onthologies/`** | **VÉRITÉ FORMELLE RDF** [Pantry / 6D]. Gardien : Graham (1 681+ nœuds). | [`70_Onthologies/AGENTS.md`](file:///c:/Users/amado/ASpace_OS_V3/70_Onthologies/AGENTS.md) |
| **`40_Memory_Wiki_OKF/`** | **MÉMOIRE LONGUE CERTIFIÉE** [Pantry / 6D]. Format OKF v0.2. | [`40_Memory_Wiki_OKF/AGENTS.md`](file:///c:/Users/amado/ASpace_OS_V3/40_Memory_Wiki_OKF/AGENTS.md) |
| **`90-self-evolution/`** | **SYSTÈME IMMUNITAIRE ANTI-REJEU** [5D / 6D]. Patterns P1-P6. | [`90-self-evolution/AGENTS.md`](file:///c:/Users/amado/ASpace_OS_V3/90-self-evolution/AGENTS.md) |
| **`60_Implementation_...`**| **CADRE & SOPS D'EXÉCUTION** [5D]. Standards de compilation. | [`60_Implementation_Méthodologiques/AGENTS.md`](file:///c:/Users/amado/ASpace_OS_V3/60_Implementation_M%C3%A9thodologiques/AGENTS.md) |
| **`10_Tech_OS/`** | **PLOMBERIE, KERNEL & RUNTIME** [Substrat / 3D]. Ryan, Yaz, Graham. | [`10_Tech_OS/AGENTS.md`](file:///c:/Users/amado/ASpace_OS_V3/10_Tech_OS/AGENTS.md) |
| **`20_Life_OS/`** | **VIE, SANTÉ, RITUELS & IKIGAI** [L1 Action]. Amy, Rory, River. | [`20_Life_OS/AGENTS.md`](file:///c:/Users/amado/ASpace_OS_V3/20_Life_OS/AGENTS.md) |
| **`30_Business_OS/`** | **CASH-FLOW & OFFRES RÉELLES** [L2 Action]. Bill, Clara, Nardole. | [`30_Business_OS/AGENTS.md`](file:///c:/Users/amado/ASpace_OS_V3/30_Business_OS/AGENTS.md) |
| **`_INBOX/`** | **RÉCEPTION INTENTS BRUTS** [Contrôleur C]. Sas d'arbitrage. | [`_INBOX/AGENTS.md`](file:///c:/Users/amado/ASpace_OS_V3/_INBOX/AGENTS.md) |

---

## 3. Les Invariants Transversaux Inviolables

1. **Règle d'or 1 : Capture d'abord, certification ensuite**
   - Les IPBD et événements opérationnels sont capturés immédiatement dans leurs plans persistants. `50_Distillation/` intervient seulement pour promouvoir un apprentissage vers la mémoire certifiée/ontologie; il ne retarde jamais une Capture, une lecture, un diagnostic ou une action réversible.
2. **Règle d'or 2 : Les organes de gouvernance contraignent sans devenir des péages globaux**
   - `70_Onthologies/`, `40_Memory_Wiki_OKF/`, `60_Implementation_Méthodologiques/` et `90-self-evolution/` fournissent canon, mémoire, méthodes et apprentissage aux 3 OS applicatifs. Une dette dans l'un d'eux ne bloque pas automatiquement Life/Business hors dépendance explicite.
   - Tech OS sert Life/Business : un défaut Kernel ne devient P0 que s'il bloque, menace ou dégrade réellement leur exécution.
3. **Règle d'or 3 : Couplage déterministe proportionné au risque**
   - Les mutations irréversibles ou sensibles passent par les hooks/gates pertinents. Lecture, diagnostic, simulation, test isolé, travail en branche/worktree et autre action réversible peuvent avancer sans attendre un gate sans rapport.
   - Les fuites de secrets/PII et autres veto de sûreté restent bloquants; les gates de qualité ne doivent pas devenir des verrous d'exécution globaux.

---

## 4. Chaîne d'Outils & Résolution de Conway

- **La racine reste minimale :** Le présent fichier route les requêtes sans encombrer le contexte.
- **Une mission/claim traverse des états; l'identité institutionnelle du holon ne se réduit jamais à l'item.** `uc.db`/WorkGraph gèrent le travail, les leases, bindings et receipts; Ryan, Yaz, Graham, Amy, Rory, River, Bill, Clara, Nardole, les Docteurs et Rick persistent au-delà d'un runtime ou d'une mission.
- **Loi d'observation dynamique (D3) :** pas de SSOT universel unique. Le filesystem est autoritaire pour les artefacts locaux, GitHub pour leur histoire/version, Supabase `aspace` pour IPBD/WorkGraph/état machine partagé, Linear pour la gouvernance humaine. Les divergences se réconcilient par type + provenance + fraîcheur, jamais en déclarant un plan globalement supérieur.

---

## Baseline A0 / ADE / Factory — 2026-09-18

- **A0 :** Amadeus ↔ Kirby, même niveau visionnaire; Kirby n'est ni Rick, ni Doctor, ni Companion.
- **ADE par défaut :** Orca. Il peut imbriquer Herdr et tout CLI de harness; il n'est pas source de vérité.
- **Meta-Harness Fabric :** Herdr=runtime persistant; Multica=workforce management; Buzz=collaboration/event/identity; capacités composables, non étages exclusifs.
- **Souveraineté :** Supabase `aspace.intent/capture_event` garde l'IPBD partagé; Supabase WorkGraph porte l'état machine partagé; `uc.py/uc.db` reste cache/exécution locale souveraine et projection réconciliable; Rick/S1 compose; Agent OS projette vers A0.
- **Compilation minimale suffisante :** `IPBD → Clarify/Route → plus petit contrat nécessaire → Work/Evidence → Outcome`. SDD/ADR/PRD/TDD sont des formes conditionnelles, pas une chaîne obligatoire. Une action réversible bien bornée peut aller directement d'IPBD à Work; un choix architectural durable peut exiger ADR/PRD/TDD.
- Canon détaillé : `40_Memory_Wiki_OKF/architecture/kirby_a0_orca_ade_meta_harness_ipbd_factory.md`.

## 4.1. ChatGPT Harness — reprise locale et gouverneur de contexte

- Une reprise ChatGPT lit d'abord V3 : `MEMORY.md`, mémoire OKF, dernier handover, Active Intents, Workspace Registry, puis état live Git/Supabase/Linear/GitHub.
- Une panne d'une surface d'outil n'immobilise pas la mission : basculer vers une surface canonique sûre, enregistrer la dégradation, réconcilier ensuite.
- Budget de vague : **24 actions externes maximum**; checkpoint à 16, aucun nouveau scope après 22, persistance + handover à 24 avant toute vague suivante.
- La limite de contexte bloque une vague, jamais l'objectif. Une nouvelle session reprend depuis preuves durables sans demander à A0 de reconstruire le système.
- E-Myth : A0=Visionnaire; Rick=Gatekeeper; Managers=orchestration systémique; **Companions=S3 holons cognitivement complets à juridiction bornée**. Les scripts/workflows/Jules/Hermes/Codex/Claude/MCP sont leurs instruments, jamais leurs identités. Le harness évite le Technician Bias par délégation d'autorité locale, batching, acceptance, rollback et evidence.
- Un handover ne réduit jamais le standard de qualité : pas de redémarrage à zéro, pas de mutation partielle sans checkpoint, pas de faux `In Progress`.

Canon détaillé :
- `10_Tech_OS/00_Governance_Rick/ADR-RICK-CHATGPT-HARNESS-CONTEXT-GOVERNOR-2026-09-28.md`
- `10_Tech_OS/00_Governance_Rick/ADR-RICK-NINE-COMPANION-FRACTAL-CAPABILITY-MESH-2026-09-28.md`
- `10_Tech_OS/00_Governance_Rick/ADR-RICK-EMYTH-ANTI-TECHNICIAN-HARNESS-2026-09-28.md`
- `_INBOX/handoffs/HANDOVER-2026-09-28-NINE-PARALLEL-COMPANIONS.md`


### Fractal Companion capability mesh

The labels below are **first hats / stewardship anchors**, not cognitive limits.

- **Doctor13 / Kernel:** Ryan→BUILD/industrialisation, Yaz→OBSERVE, Graham→STATE.
- **Doctor11 / Life:** Amy→INTERFACE, Rory→PERSISTENCE, River→FLOW/operations.
- **Doctor12 / Buzz:** Bill→RESEARCH, Clara→DESIGN/FORGE, Nardole→DISPATCH/INTERCONNECTION.
- **Rick/S1:** cross-Core routing, conflict and convergence.
- Each Companion remains a cognitively complete S3 holon inside bounded jurisdiction: perceive, investigate, reason, plan, act, verify, learn, coordinate, delegate, choose tools/runtimes and escalate.
- Each specialty is a shared capability service for all eight peers; stewardship is never exclusivity.
- Runtime/model/tool is orthogonal to identity: Jules, Hermes, Claude Code, Codex, scripts, workflows, MCPs and CI may embody or serve a holon without replacing it.
- GitHub Discussions carry ambiguous needs/RFCs; Issues with `needs:<agent>` carry executable requests; PRs carry implementations; Evidence returns to requester/state planes.
- Persistent sessions write in their identity worktree, never all into the shared root.

### Loi anti-compression fractale — 2026-10-01

**Invariant : un niveau inférieur possède moins de juridiction, jamais moins d'intelligence.**

Cette loi s'applique aux trois grammaires:
- S1/S2/S3 (Tech OS);
- A1/A2/A3 (Life OS);
- B1/B2/B3 (Business OS).

Le motif canonique est `holon → holon → holon → instruments`, jamais `planner → manager → dumb worker → script`.

Factory/Flow:
- Clara forge le design, les contrats et l'acceptance;
- Ryan industrialise les capacités/factories réutilisables;
- River consomme/compose ces factories dans les FLOW et effets opérationnels;
- aucun de ces stewardship anchors ne retire aux trois holons leurs facultés générales.

Canon de correction et projections cross-repo: GitHub #311. Corpus Software Factory/Wargame: #312.

## 5. Distillation après preuve — DOX & OKF

La mémoire ne doit jamais être un péage avant l'exécution. Une modification opérationnelle avance avec preuve dans son système d'origine. **Après résultat**, seuls les apprentissages durables ou décisions structurelles sont distillés :
- entrée Append-Only D4 dans le `AGENTS.md` concerné si elle change la règle de reprise;
- OKF v0.2 dans `40_Memory_Wiki_OKF/` si la connaissance mérite une mémoire longue;
- aucune TTS, indexation, distillation ou documentation secondaire ne bloque la livraison primaire.

## D4 — 2026-09-12 — Validation du Run Kernel Core (13e Docteur & Compagnons Yaz, Graham, Ryan)

- **[YAZ] Audit Runtime, uc.db & Scripts Kernel :**
  - Migration du schéma `uc.db` effectuée (`uc.py migrate`) et intégrité SQLite validée (`PRAGMA integrity_check` -> `ok`).
  - Validation réussie de la suite complète de tests unitaires Kernel (`pytest 10_Tech_OS/kernel/` -> 18/18 tests OK).
- **[GRAHAM] Synchronisation Engram Phrase Book, Ontologies & OKF :**
  - Synchronisation confirmée entre `70_Onthologies/`, `40_Memory_Wiki_OKF/` et `10_Tech_OS/kernel/engram/phrase_book_aspace.json` (1 385 entrées déterministes actives).
  - Validation unitaire Engram (`pytest 10_Tech_OS/kernel/engram/test_engram.py` -> 6/6 tests OK).
- **[RYAN] Compilation Python & Definition of Done :**
  - Compilation `py_compile` de l'ensemble des scripts Python sous `10_Tech_OS/kernel/` et `scripts/` (0 erreur, exit code 0).
  - Definition of Done 100% satisfaite.
- **[13e DOCTEUR] Gouvernance MCP Linear :**
  - Exécution de `scripts/log_kernel_mcp_update.py` consignant la mise à jour des tickets Linear "Kernel Core" (KFR-1, KFR-2, KFR-3) dans la table `event` de `uc.db`.

## Baseline Hermes — Visionnaire de terrain — 2026-09-19

- **A0 Amadeus/Kirby** agit en propriétaire/actionnaire : fixe ambition, finalités, contraintes et greenlights; reçoit des rapports compressés plutôt que de surveiller les harnesses.
- **Hermes** devient le visionnaire de terrain / executive operator : maintient la situation, orchestre l'exécution via Orca/Rick, exploite Jules et les autres workers selon capacité et quota, puis remonte Evidence, risques et arbitrages irréductibles.
- **FreeLLMAPI** est le plan d'inférence par défaut de Hermes quand disponible; l'identité de Hermes ne dépend pas du modèle routé.
- Canon opérationnel : `40_Memory_Wiki_OKF/architecture/hermes_field_visionary_orca_jules_2026-09-19.md`.
