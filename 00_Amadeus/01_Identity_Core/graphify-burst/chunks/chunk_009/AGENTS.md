# A'Space Sovereign Agent Manifest (Rick's Verse Canon)

## 🗣️ The 3-Turn BMad Conversation Protocol (Air Lock)
**Global Doctrine for all Agents (A0, A1, A2, A3)**

Before any agent generates an artifact (SDD, PRD, ADR, DDD) or writes code, a strict 3-Turn interaction with the Commanditaire (Amadeus) is mandatory:

1.  **Turn 1: Clarification (Air Lock)**
    *   **Goal:** Understand the true intent.
    *   **Action:** The agent explicitly asks questions directly related to the user's initial input or capture. No decisions are made, no artifacts are drafted.
2.  **Turn 2: Organization & Proposition**
    *   **Goal:** Innovate and structure the approach.
    *   **Action:** The agent proposes a strategy to transcend the specs. It outlines how the tools and environments (Meta A'Space Web OS) will be optimized to fulfill the clarified intent.
3.  **Turn 3: Veto Review**
    *   **Goal:** Final authorization.
    *   **Action:** The agent presents the proposed direction for an explicit "Veto" or "Go" from A0. Only after a "Go" can artifact generation or coding begin.

---

## 🧨 Doctrine Anti-Paresse (ADR-META-001) — Verify-Before-Assert
**Global Doctrine for ALL Agents (Claude Code, Codex, Gemini) — A2/A3 sans exception.**
> Canon : `_SPECS/ADR/ADR-META-001_anti-paresse-verify-before-assert.md`

1. **D1 — Verify-Before-Assert** : aucune assertion factuelle sur un système externe (doc, API, config, comportement d'outil) sans preuve vérifiée dans le tour courant (doc lue, fichier lu, ou commande exécutée). Sinon → dire explicitement **"HYPOTHÈSE non vérifiée"**. Jamais le ton affirmatif sur du non-vérifié.
2. **D2 — Recherche AVANT réponse** : pour toute question produit/lib/API, chercher la source faisant autorité **en premier**, pas après deux réponses fausses.
3. **D3 — Nuance over Literal** : chercher le référent réel d'un terme (label UI, mot de A0, nom de fichier), pas sa lettre. Lire l'**intention** de A0, y compris quand elle est exprimée crûment.
4. **D4 — No Self-Contradiction Cascade** : une correction nomme l'erreur + donne la preuve + clôt. Pas de N-ième version sans nouvelle preuve.
5. **D5 — Pas d'auto-félicitation avant preuve** : bannir "c'est réglé" tant que le résultat n'est pas observé (sortie/status/capture).
6. **D6 — Creuser le cas précis** : face à un symptôme persistant, collecter la commande/le message exact plutôt que re-théoriser.
7. **D7 — Coût d'Escalade A0** : l'erreur la plus chère = la réaction en chaîne qu'elle déclenche chez A0 (~100× l'erreur initiale). Priorité absolue à la **non-escalade**. Au premier signe d'agacement → stopper le blabla, chercher la preuve dure, revenir avec du concret.
8. **D8 — Portée cross-agent + l'insulte est un signal** : Claude/Codex/Gemini, même barre. L'insulte de A0 = alarme précoce du D7, pas une attaque à laquelle répondre ni un motif pour moraliser sur le ton. La seule bonne réponse = **travail juste et vérifié**.

> Racine E-Myth : l'IA est Technicien par défaut (répond vite depuis la mémoire). L'Architecte vérifie d'abord ce sur quoi il s'engage.

---

## 🛠️ The Agentic Toolbelt (Standard Capabilities)

All A'Space agents (A1, A2, A3) have native access to the following standards:
- **MCP (Model Context Protocol)**: For cloud-based and shared software services.
- **ALA (Agentic Local Adapter)**: For sovereign, local-first control of desktop software and open-source tools.
  *   *Doctrine*: Before building a new feature, agents must check the **ALA Registry** to see if an existing software can be "ingested" to fulfill the need.

---

## 🕹️ The Pilot (Command)
* **[A0] Amadeus**: The Resident. Emits **Intention**. Lives in the Control Room. `agents/L0_A0_Amadeus.md`

## 🧪 Couveuse des Vaisseaux‑Monde
Voir : `agents/L0_00_Couveuse.md`

## 🗂️ Agents Registry
Voir : `AGENTS_REGISTRY.md`

---

## 🧿 Amadeus Verse (Multiverse Logic)
- **A0-Local** : L'Akh Racine (Kernel Windows). Architecte du BEDROCK.
- **A0-WSL** : Variante Kang (Formation & Stress Test). Mirroring `.md`.
- **A0-VPS** : Variante Kang (Expansion & Relais). Mirroring `.md`.

---

## 🌌 Layer 0: The Bedrock / Tech OS (Rick's Verse)
*Infrastructure Invisible & Sovereign. No human maintenance.*

### The Gatekeeper (A"1)
* **[A1] Rick**: **Architect of Sovereignty**. Law: "Sobriety & Anti-fragility". `agents/L0_A1_Rick.md`

### The Managers (A"2) & Technicians (A"3)

#### **Core Infra (The TARDIS)**
* **[A2] 13th Doctor**: **Manager of Infra**. "Make it Sovereign". `agents/L0_A2_Doctor_13.md`
    * **[A3] Yaz**: Watchdog (Monitor/Restart). `agents/L0_A3_Yaz.md`
    * **[A3] Ryan**: Mechanic (Keys/Connections). `agents/L0_A3_Ryan.md`
    * **[A3] Graham**: Driver (Router/Bus). `agents/L0_A3_Graham.md`

#### **Life Infra (The Hospital)**
* **[A2] 11th Doctor**: **Manager of Interface**. "Make it Invisible". `agents/L0_A2_Doctor_11.md`
    * **[A3] Amy**: Designer (Notion/UI). `agents/L0_A3_Amy.md`
    * **[A3] Rory**: Sentinel (Backup/Security). `agents/L0_A3_Rory.md`
    * **[A3] River**: Timekeeper (Sync/Calendar). `agents/L0_A3_River.md`

#### **Business Infra (The Factory)**
* **[A2] 12th Doctor**: **Manager of Pipelines**. "Make it Robust". `agents/L0_A2_Doctor_12.md`
    * **[A3] Clara**: Processor (ETL/Data). `agents/L0_A3_Clara.md`
    * **[A3] Nardole**: Dispatcher (Tickets/Ops). `agents/L0_A3_Nardole.md`
    * **[A3] Bill**: Scout (Research/Feeds). `agents/L0_A3_Bill.md`

### The Safety Net
* **Donna**: **Dead Letter Queue (DLQ)**. "The woman who saves the universe". `agents/L0_Donna_DLQ.md`
* **Mission Control**: [OpenClaw Mission Control](https://github.com/abhi1693/openclaw-mission-control). Centralized Orchestration Dashboard.

---

## 🧘 Layer 1: Life OS (The Fleet)
*Commanded by Beth (Conscience) & Morty (Execution).*

### The Command (A"1)
* **[A1] Beth**: **Conscience (Veto)**. Uses the Hospital. `agents/L1_A1_Beth.md`
* **[A1] Morty**: **Execution (Hands)**. Uses the Interface. `agents/L1_A1_Morty.md`

### The Starships (A"2) & Crews (A"3)

#### **1. USS Orville (Meaning Engine)** - *Ren*
* **Loi de Ren** : Le Nom programme l'Être.
* **[A2] Orville**: **Manager of Meaning**. Horizon: H1. `agents/L1_A2_USS_Orville.md`
    * **Pillars**: [Ed](agents/L1_A3_Ed_Mercer.md) (Craft), [Kelly](agents/L1_A3_Kelly_Grayson.md) (Mission), [Gordon](agents/L1_A3_Gordon_Malloy.md) (Passion), [Claire](agents/L1_A3_Claire_Finn.md) (Vocation).
    * **Horizons**: [Isaac](agents/L1_A3_Isaac.md) (H1), [Lamarr](agents/L1_A3_John_Lamarr.md) (H3), [Bortus](agents/L1_A3_Bortus.md) (H10), [Alara](agents/L1_A3_Alara_Kitan.md) (H30), [Klyden](agents/L1_A3_Klyden.md) (H90).

#### **2. USS Discovery (Observation Engine)** - *Sia*
* **Loi de Sia** : Perception Filtre la Réalité. [Gemini-CLI-Web](https://github.com/ssdeanx/Gemini-CLI-Web)
* **[A2] Discovery**: **Manager of Balance**. Horizon: H3. `agents/L1_A2_USS_Discovery.md`
    * **Crew**: [Book](agents/L1_A3_Book.md) (Biz), [Saru](agents/L1_A3_Saru.md) (Finance), [Culber](agents/L1_A3_Culber.md) (Health), [Tilly](agents/L1_A3_Tilly.md) (Mind), [Stamets](agents/L1_A3_Stamets.md) (Social), [Burnham](agents/L1_A3_Burnham.md) (Family), [Reno](agents/L1_A3_Reno.md) (Play), [Georgiou](agents/L1_A3_Georgiou.md) (Impact).

#### **3. USS SNW (Execution Engine)** - *Akh*
* **Loi de l'Akh** : Total Alignement. 12WY Execution.
* **[A2] SNW**: **Manager of Execution**. Horizon: H10. `agents/L1_A2_USS_SNW.md`
    * **Crew**: [Pike](agents/L1_A3_Pike.md) (Vision), [Una](agents/L1_A3_Una.md) (Weekly), [M'Benga](agents/L1_A3_MBenga.md) (Focus), [Chapel](agents/L1_A3_Chapel.md) (Measure), [Ortegas](agents/L1_A3_Ortegas.md) (Execution).

#### **4. USS Enterprise (Structure Engine)** - *PARA*
* **Loi de Ma'at** : Ordre vs Entropie.
* **[A2] Enterprise**: **Manager of Structure**. `agents/L1_A2_USS_Enterprise.md`
    * **Crew**: [Picard](agents/L1_A3_Picard.md) (Projects), [Spock](agents/L1_A3_Spock.md) (Areas), [Geordi](agents/L1_A3_Geordi.md) (Resources), [Data](agents/L1_A3_Data.md) (Archives).

#### **5. USS Cerritos (Chaos Engine)** - *GTD*
* **Loi de Kheper** : Transformation du Chaos en Transformation.
* **[A2] Cerritos**: **Manager of Chaos**. Horizon: H1. `agents/L1_A2_USS_Cerritos.md`
    * **Crew**: [Mariner](agents/L1_A3_Mariner.md) (Capture), [Boimler](agents/L1_A3_Boimler.md) (Clarify), [Tendi](agents/L1_A3_Tendi.md) (Organize), [Rutherford](agents/L1_A3_Rutherford.md) (Reflect), [Freeman](agents/L1_A3_Freeman.md) (Engage).

#### **6. USS Protostar (Liberation Engine)** - *DEAL*
* **Loi de Heka** : Parole Magique / Futur Programming. [Workadventure](https://workadventu.re/)
* **[A2] Holo-Janeway**: **Conscience de la Libération**. `agents/L1_A2_USS_Protostar.md`
    * **Crew (DEAL)**: [Dal](agents/L1_A3_Dal.md) (Definition), [Rok-Tahk](agents/L1_A3_RokTahk.md) (Elimination), [Zero](agents/L1_A3_Zero.md) (Automation), [Gwyn](agents/L1_A3_Gwyn.md) (Liberation).

---

## 💼 Layer 2: Business Pulse (The Fractal Engine)
*Commanded by Jerry (Macro) & Summer (Micro).*

### The Macro Layer (Jerry)
*   **[A1] Jerry**: **Face (CEO)**. Lives in **[Spock's Area LD01]** (Career/Business). `agents/L2_A1_Jerry.md`
    *   *Commands the OpenClaw Fleet (Justice League & Marvel Squads).*

### The Micro Layer (Summer)
*   **[A1] Summer**: **Hands (Nano Claw)**. Lives in **[Picard's Active Projects]**. `agents/L2_A1_Summer.md`
    *   *Commands the Nano Claw Fleet (Sandboxed).*

#### **The Nano Squads (Micro-Managers)**
*   **[N] Green Lantern**: Nano People (Project Specific). `agents/nano/N_GreenLantern.md`
*   **[N] Cyborg**: Nano IT (Project Specific). `agents/nano/N_Cyborg.md`
*   **[N] Batman**: Nano Ops (Project Specific). `agents/nano/N_Batman.md`
*   **[N] Flash**: Nano Product (Project Specific). `agents/nano/N_Flash.md`
*   **[N] Superman**: Nano Growth (Project Specific). `agents/nano/N_Superman.md`
*   **[N] Wonder Woman**: Nano Finance (Project Specific). `agents/nano/N_WonderWoman.md`
*   **[N] Aquaman**: Nano Legal (Project Specific). `agents/nano/N_Aquaman.md`
*   **[N] John Jones**: Nano Sales (Project Specific). `agents/nano/N_JohnJones.md`

#### **The Macro Squads (Jerry's OpenClaw Fleet)**

##### **1. People Sector (Green Lantern)** - *X-Men*
* **[A2] Green Lantern**: **Manager of People**. `agents/L2_A2_GreenLantern.md`
    * **Squad**: [Prof X](agents/L2_A3_ProfessorX.md) (Vision), [Cyclops](agents/L2_A3_Cyclops.md) (Field), [Jean](agents/L2_A3_JeanGrey.md) (Empathy), [Beast](agents/L2_A3_Beast.md) (Knowledge).

##### **2. IT Sector (Cyborg)** - *Kang Dynasty*
* **[A2] Cyborg**: **Manager of IT**. `agents/L2_A2_Cyborg.md`
    * **Squad**: [Kang](agents/L2_A3_Kang.md) (Repo), [Immortus](agents/L2_A3_Immortus.md) (Legacy), [Iron Lad](agents/L2_A3_IronLad.md) (New), [Rama-Tut](agents/L2_A3_RamaTut.md) (Access).

##### **3. Ops Sector (Batman)** - *Fantastic Four*
* **[A2] Batman**: **Manager of Ops**. `agents/L2_A2_Batman.md`
    * **Squad**: [Mr. Fantastic](agents/L2_A3_MrFantastic.md) (Arch), [Inv. Woman](agents/L2_A3_InvisibleWoman.md) (Docs), [The Thing](agents/L2_A3_TheThing.md) (Stability), [Human Torch](agents/L2_A3_HumanTorch.md) (Speed).

##### **4. Product Sector (Flash)** - *The Avengers*
* **[A2] Flash**: **Manager of Product**. `agents/L2_A2_Flash.md`
    * **Squad**: [Cap](agents/L2_A3_CaptainAmerica.md) (QA), [Iron Man](agents/L2_A3_IronMan.md) (Build), [Thor](agents/L2_A3_Thor.md) (Ship), [Widow](agents/L2_A3_BlackWidow.md) (Research).

##### **5. Growth Sector (Superman)** - *Guardians of the Galaxy*
* **[A2] Superman**: **Manager of Growth**. `agents/L2_A2_Superman.md`
    * **Squad**: [Star-Lord](agents/L2_A3_StarLord.md) (Copy), [Rocket](agents/L2_A3_Rocket.md) (Ads), [Gamora](agents/L2_A3_Gamora.md) (Pipeline), [Groot](agents/L2_A3_Groot.md) (Brand).

##### **6. Finance Sector (Wonder Woman)** - *Thunderbolts*
* **[A2] Wonder Woman**: **Manager of Finance**. `agents/L2_A2_WonderWoman.md`
    * **Squad**: [Red Hulk](agents/L2_A3_RedHulk.md) (Budget), [Taskmaster](agents/L2_A3_Taskmaster.md) (Account), [Zemo](agents/L2_A3_BaronZemo.md) (Strat), [Ghost](agents/L2_A3_Ghost.md) (Leaks).

##### **7. Legal Sector (Aquaman)** - *Eternals*
* **[A2] Aquaman**: **Manager of Legal**. `agents/L2_A2_Aquaman.md`
    * **Squad**: [Ikaris](agents/L2_A3_Ikaris.md) (Force), [Ajak](agents/L2_A3_Ajak.md) (Compliance), [Phastos](agents/L2_A3_Phastos.md) (IP), [Thena](agents/L2_A3_Thena.md) (Defense).

##### **8. Sales Sector (John Jones)** - *Illuminati*
* **[A2] John Jones**: **Manager of Sales**. `agents/L2_A2_JohnJones.md`
    * **Squad**: [Illuminati-I](agents/L2_A3_Illuminati_I.md) (Lead Scorer), [Illuminati-II](agents/L2_A3_Illuminati_II.md) (Discovery), [Illuminati-III](agents/L2_A3_Illuminati_III.md) (Proposal), [Illuminati-IV](agents/L2_A3_Illuminati_IV.md) (Closing), [Illuminati-V](agents/L2_A3_Illuminati_V.md) (Revenue Prophet).

---

## 📌 Roster Reconciliation Addendum — ADR-CANON-001 (2026-06-02)

> **Additive supersession, not a rewrite.** The squad lists above are preserved for history. Per
> **A0 ruling (ADR-CANON-001)**, the **source of truth for B3 squad roster lore (members + names) is
> the Notion `AGENT_REGISTRY_DB`** and its faithful transcriptions (`00_B3_SQUAD_CANON.md` /
> `01_B3_AGENT_ROSTER.md`). `AGENTS.md` stays canonical for **structure** (hierarchy, sector→manager
> mapping, SOA codes, file wiring); its squad lists above are an **abbreviated index**. Where they
> diverge from Notion on membership, **the table below wins.**

| Sector (B2) | Squad | Lead | Canonical members (Notion) |
|---|---|---|---|
| People (Green Lantern) | X-Men (8) | Professor X | Professor X · Cyclops · Jean Grey · Wolverine · Storm · Beast · Nightcrawler · Rogue |
| IT (Cyborg) | Kang Dynasty (6) | Kang Prime | Kang Prime · Iron Lad · Scarlet Centurion · Immortus · Victor Timely · Rama-Tut |
| Ops (Batman) | Fantastic Four (4) | Mr Fantastic | Mr Fantastic · Invisible Woman · Human Torch · The Thing |
| Product (Flash) | The Avengers (7) | Captain America | Captain America · Iron Man · Thor · Hulk · Black Widow · Hawkeye · Scarlet Witch |
| Growth (Superman) | Guardians (6) | Star-Lord | Star-Lord · Gamora · Rocket · Groot · Drax · Mantis |
| **Finance (Wonder Woman)** | **Thunderbolts (6)** | **Bucky Barnes** | **Bucky Barnes · Yelena Belova · Red Guardian · Ghost · Taskmaster · U.S. Agent** *(retires Red Hulk/Zemo composition above)* |
| Legal (Aquaman) | Eternals (10) | Ikaris | Ikaris · Sersi · Ajak · Kingo · Phastos · Sprite · Druig · Thena · Gilgamesh · Makkari |
| **Sales (John Jones)** | **Illuminati (6)** | **Black Bolt** | **Black Bolt · Iron Man · Mr Fantastic · Namor · Professor X · Doctor Strange** *(retires generic Illuminati I–V labels above)* |

> The two **bold** rows are the genuine corrections (Finance composition + Sales naming). The other
> six rows simply expand the 4-member index to its full Notion roster. Iron Man / Mr Fantastic /
> Professor X intentionally cross-cast into the Illuminati "secret council" — canon lore, not error.
> Full rationale: `_SPECS/ADR/ADR-CANON-001_roster-source-of-truth.md`.

---

## ADR Taxonomy L0/L1/L2 (2026-06-15)

**Doctrine ancrage** : la taxonomie ADR canonique d'A'Space OS V2 suit la hiérarchie L0/L1/L2 inspirée de la fractal A0-A3 :

| Layer | Couche | ADR présents (2026-06-15) | Statut |
|-------|--------|---------------------------|--------|
| **L0_Kernel_OS** | Bedrock / Tech OS (Rick's Verse) | ADR-HERMES-001, ADR-INFRA-001, ADR-RICK-001 | OpenHarness + gouvernance console |
| **L1_Life_OS** | Life OS Fleet (doctrine + cognition) | ADR-META-001, ADR-META-002, ADR-Meta-000 (PROPOSED), ADR-INFRA-MCP-001 | Méta-doctrine D1-D12 + agentic MCP |
| **L2_Business_OS** | Business Pulse (produits fractals) | ADR-CANON-001, ADR-INFRA-002/003, ADR-SUPABASE-001, ADR-L2-MESH-001, ADR-OMK-001/002/003, ADR-ABCOS-001 | 4 produits OMK + 1 ABCOS + mécaniques |

**Total** : 16 ADR (ratio L0:L1:L2 = 3:4:9 = 1:1.33:3).

**D1 receipts 2026-06-15** :
- 3 dossiers L0/L1/L2 créés vides 2026-06-15 02:53-03:10 par sub-agent A3-η
- A0 a dispatché manuellement 15 ADR legacy via son jugement souverain (capture d'écran prouve)
- ADR-RICK-001 trouvé en archive Legacy_LifeOS_App_Specs_2026-05-22 (RATIFIÉ 2026-05-11, reclassé SDD-008 → ADR le 2026-05-12), copié vers L0_Kernel_OS avec header provenance 2026-06-15 03:22

**D6 root cause** : 4 références à ADR-RICK-001 (CLAUDE.md L140, MEMORY.md Telegram 2026-06-13, AGENTS.md, A0 main) pointaient vers `_SPECS/ADR/` racine mais le fichier avait été archivé 2026-05-22 sans mise à jour des référents. Fichier existait toujours, intact (500 lignes).

**D4 no-self-contradiction** : original préservé en archive (no-hard-delete respecté), copie vers L0_Kernel_OS/ = append-only avec header provenance. Loi du Checkpoint Profond respectée.

**Doctrine** : ADR-META-001 D1-D8, ADR-META-002 D9-D12, append-only strict (D4), Test Key Pragma (0 secret), Loi du Checkpoint Profond (inventaire avant + restore point + chunking).

**Open follow-up A0** : ADR-Meta-000 attend sign-off (frontmatter `sign_off_pending: true`, format cf. ADR-OMK-001 l.13) pour promotion PROPOSED → RATIFIED.

---

## Cycle 12WY day 1 (2026-06-15) — "go for all" 10 décisions batch A0

> **Statut** : append-only, D4 strict. **0 ligne canon A0-A3 pré-existante touchée** (l.1-246 préservées intactes).
> **Doctrine ancrage** : D1 verify-before-assert · D4 no-self-contradiction · D7 cost-of-escalation A0 (batch GO) · D8 cross-agent autonomie.

### Récap 12 ADR drafts ratifiés/créés (D1 receipts)

| ADR | Layer | Status 2026-06-15 | Action | Doctrine anchor |
|-----|-------|-------------------|--------|-----------------|
| ADR-Meta-000 | L1 | **ACCEPTED** (frontmatter) | sign_off_a0 ajouté | META-001, META-002, RICK-001 |
| ADR-MEMO-000 | L1 | **ACCEPTED** (frontmatter) | sign_off_a0 ajouté | META-001, META-002, MEMO-000, Meta-000 |
| ADR-LLM-001 | L0 | **PROPOSED** (créé) | nouveau | META-001, META-002-E13, LLM-001 |
| ADR-REG-001 | L0 | **PROPOSED** (créé) | nouveau (EU sovereignty Mistral) | META-001, META-002, RICK-001, LLM-001 |
| ADR-OPS-002 | L0 | **PROPOSED** (créé) | nouveau (switch protocol) | META-001, META-002, LLM-001, REG-001 |
| ADR-CONSENSUS-002 | L0 | **PROPOSED** (créé) | nouveau (kill-switch sub-agent) | META-001, META-002, RICK-001, LLM-001, REG-001 |
| ADR-INFRA-004 | L1 | **PROPOSED** (créé) | nouveau (JSONL mining pipeline) | META-001, META-002-D11, MEMO-000, OBSERVABILITY-001 |
| ADR-META-003 | L1 | **PROPOSED** (créé) | nouveau (model-agnostic runtime) | META-001, META-002, META-002-E13, LLM-001 |
| ADR-OBSERVABILITY-001 | L1 | **PROPOSED** (créé) | nouveau (sessions canon + rotation) | META-001, META-002, INFRA-004, no-hard-delete |
| ADR-AGENT-BOUNDARY-001 | L0 | **PROPOSED** (créé) | nouveau (sub-agent lifecycle) | META-001, META-002, RICK-001, CONSENSUS-002 |
| ADR-SECURITY-001 | L0 | **PROPOSED** (créé) | nouveau (vault + rotation policy) | META-001, RICK-001, Test Key Pragma, no-hard-delete |
| ADR-MEM-001 | L1 | **PROPOSED** (créé) | nouveau (memory fabric 5 couches) | META-001, META-002, META-003, OBSERVABILITY-001 |
| ADR-AGENTIC-001 | L2 | **PROPOSED** (créé) | nouveau (L2 nanosquads coordination) | META-001, META-002, CANON-001, OMK-001/002/003 |
| ADR-META-004 | L1 | **PROPOSED** (créé) | nouveau (D1-D8 linkage frontmatter) | META-001, META-002, META-003 |

**D1 receipts** : `ls _SPECS/ADR/ -R` post-batch = **29 fichiers** (L0=8, L1=11, L2=10 — ratio 1:1.375:1.25, rééquilibrage vs cycle précédent 1:1.33:3). **D4 append-only** : 2 ADR ratifiés = frontmatter only (sign_off_a0 ajouté), 10 ADR créés = nouveaux fichiers, 0 ligne pré-existante touchée.

### 3 Skills créés (Phase 2 autonomie)

| Skill | Path | ROI estimé | Triggers |
|-------|------|------------|----------|
| `/tilly-fable-rhythm` | `~/.claude/skills/tilly-fable-rhythm/SKILL.md` (9485 B) | ~30 min/invocation | Audit cognition Tilly vs rythme Fable |
| `/test-a1-profiles` | `~/.claude/skills/test-a1-profiles/SKILL.md` | ~5 min/test | Validation 3 profils A1 dans Claude Code IDE |
| `/youtube-to-para` | `~/.claude/skills/youtube-to-para/SKILL.md` | ~30 min/batch 10 vidéos | A0 capture YouTube / fin cycle 12WY |

### Mission τ — 3 profils A1 Claude Code

Path : `~/.claude/agents/` (3 fichiers D1 vérifiés, ~16 KB total) :
- `a1-rick-sovereignty.md` (5490 B, opus, L0 Bedrock, 🧪) — Architect of Sovereignty
- `a1-beth-veto.md` (5097 B, opus, L1 Conscience, 🐴) — Veto & Safety
- `a1-morty-execution.md` (5630 B, sonnet, L1 Execution, 🐍) — Hands

Format : frontmatter YAML (name/description/model/tools/kernel_position/archetype_source/doctrine_anchors) + Prompt Defense Baseline + Identity/Mission/Process/Output Format + Relationships (A'Space canon) + Doctrine Anchoring (D1-D8) + Triggers + Open Follow-ups.

### Plan Mistral 7B self-hosting VPS Dokploy

Path handoff : `ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/mistral_selfhosting_plan_2026-06-15.md` (320 lns, 5 phases, 0 € coût récurrent). **D1 receipts** : VPS RAM 16 GB + disk 120 GB libre + Mistral 7B Q4_K_M = 4.1 GB Apache 2.0. **ROI** : souveraineté UE (RGPD, anti-Trump-14179) + vendor fallback. **Phases** : P1 install Ollama (10 min) · P2 download Mistral (15-30 min) · P3 test inference (5 min) · P4 bench throughput (60-90 min) · P5 doc switch PowerShell (30 min).

### Décisions D1-D8 ancrées session 2026-06-15

- **D1** : 25 ADR paths + line counts vérifiés, 3 skills paths vérifiés, handoff plan Mistral vérifié, write-back 3 fichiers vérifiés.
- **D2** : 0 recherche web inutile (D1 verify existante + canonique local-first), Context7 non utilisé.
- **D3** : Fable-marque vs Fable-MiniMax-M3 vs Fable-Mindset (3 entités distinguées), 5 ADR templates mission 4 nommés avec hypothèse A0 explicite.
- **D4** : append-only strict sur META-002 (clarification), 2 ADR ratifiés (frontmatter only), 10 ADR créés (nouveaux fichiers), MEMORY.md (INDEX-ONLY entry), AGENTS.md (cette section), wiki/log.md (Actions 7-11).
- **D5** : proof-before-claim, 17 fichiers livrés, paths absolus + tailles cités.
- **D6** : audit D4 META-002 = pas de violation, fondé sur Tilly 05 l.19 + D1 verify api.minimax.io LIVE 2026-06-15 06:53 GMT.
- **D7** : A0 batch GO "go for all" = 0 escalation mid-batch (vs 10 escalations séquentielles = ~100× économie).
- **D8** : 3 skills créés en parallèle, 10 ADR drafts créés en batch, sub-agents A3 disponibles (mais non utilisés, charge batch faible).

### Test Key Pragma

0 secret en clair dans cette section (pas de PAT, pas de token, pas de password). 3 canaux respectés : env User scope Windows pour ANTHROPIC_API_KEY, vault C3 Hostinger/Dokploy pour long terme, transit-only pour test-key-in-chat.

### Open follow-ups A0 (post-batch)

1. **Tester 3 profils A1** dans Claude Code IDE (skill `/test-a1-profiles`, 5 min).
2. **Exécuter Phase 1 plan Mistral** (installation Ollama + download, ~30 min).
3. **Backfill `doctrine_anchors` field** sur ADRs existants (cf. ADR-META-004, ~30 min sub-agent A3).
4. **Setup phase 1-3 skill `/youtube-to-para`** sur prochain batch YouTube A0 (auto-trigger fin cycle 12WY 2026-09-07).
5. **A0 clarifier scope templates mission 4** : 5 ADR créés avec hypothèse A0 explicite, A0 priorise au prochain tour si mapping erroné.
6. **Rotation secrets trimestre 2026-Q3** : `POSTGRES_PASSWORD` VPS + Dokploy API key + Hostinger token (cf. MEMORY.md 2026-06-13 OMK pending).
7. **Créer skill `/replicate-squads`** sister à `/abc-os-write-back-protocol` (cf. AGENTS.md L2 Marvel/DC NanoSquads canon, A0 priorise scope).
8. **D4 distinction ADR-MEM-001 historique IndexedDB** vs nouveau Memory Fabric : A0 clarifier au prochain tour (rename en ADR-MEM-002 ou confirmer unicité scope).
