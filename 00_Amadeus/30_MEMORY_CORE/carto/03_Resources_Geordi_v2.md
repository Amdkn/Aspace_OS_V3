# 03_Resources_Geordi — Cartographie V2

> **V2 (2026-08-13)** — vague 2 de la cartographie du seau **03_Resources_Geordi** du PARA de V2.
> V1 a lu 38 fichiers (cadrage macro : 14 sous-dossiers, 73 types, 44 relations, 36 codes, 15 contradictions).
> V2 a lu **86 fichiers additionnels** (cadrage micro : _INDEX.md des 9 guides, plans canon, 30 ADR META/L0/L2, 12 mindsets/dispatch, 10 agents canon). Total cumulé = **124 fichiers** lus sur **2 658 disponibles** (4,7 %).
>
> **Écrit au fil de l'eau** : ce rapport est append-only — les sections sont ajoutées au fur et à mesure. Si la session s'arrête, ce qui est lu reste lisible.
>
> **Sources des citations** : tous les chemins sont absolus (Windows). Les citations sont **verbatim** depuis les fichiers, jamais paraphrasées. Aucune relation n'est inventée — une relation sans citation = une invention = interdit absolu.

---

## §0 — Couverture et périmètre

| Métrique | V1 | V2 | Δ | Total |
|---|---|---|---|---|
| Fichiers lus | 38 | 86 | +86 | **124** |
| Fichiers disponibles | 2 658 | 2 658 | — | 2 658 |
| Jonctions écartées | 159 | 159 | — | 159 |
| Sous-dossiers racine touchés | 8 / 14 | +5 / 14 | +5 | **13 / 14** |
| Taux de lecture | 1,4 % | — | — | **4,7 %** |
| Types identifiés | 73 | +22 | +22 | **95** |
| Relations extraites | 44 | +63 | +63 | **107** |
| Systèmes de codes | 36 | +24 | +24 | **60** |
| Contradictions relevées | 15 | +7 | +7 | **22** |

**Sous-dossiers racine** (14 au total, 13 touchés en V1+V2) :
- ✅ 00_Index/ (V1) · 01_Guides/ (V1+V2) · 02_Templates/ (V1) · 03_Memory_Unified/ (V1+V2)
- ✅ 04_From_V2_Root/ (V1+V2 — volume majeur d'ADRs) · 05_From_V2_Domains/ (V1+V2 — décisions LD01 Book)
- ✅ 06_Claude_Code_Bare/ (V1+V2 — agents/mindsets/plans/ADRs/skills) · 07_From_Home_Root_2026-08-01/ (V1)
- ✅ 08_Workspaces_Dormants_2026-08-01/ (V1) · 09_From_Home_Root_Batch2_2026-08-01/ (V1) · 09_Life_OS/ (V1+V2)
- ⚠️ Cerritos_Plane_Settings/ (1 fichier — non touché) · Youtube_Take_out/ (0 fichier — vide) · graphify-out/ (sortie pipeline)

**Volumétrie mesurée 2026-08-02** (V1) : 48 221 fichiers `.md` total, jonctions exclues, realpath dédupliquée.

---

## §1 — Tableau des types (trié par nombre de chemins)

| # | Type | Chemins (V2 cumul) | Catégorie |
|---|---|---|---|
| 1 | ADR (Architecture Decision Record) | 60+ | L0/L1/L2 doctrine |
| 2 | Squad Marvel B3 (53 personnages) | 53 | L2 B3 techniciens |
| 3 | A3 Sub-agent L1 (Star Trek/Orville/Protostar/SNW) | 49 | L1 A3 twins |
| 4 | A2 USS-ship Manager L1 (6 ships) | 6 | L1 A2 engines |
| 5 | Domain canon 0X_Domain (8 Domaines) | 9 | L2 B2 domaines |
| 6 | Mindset (doctrine comportementale) | 33 | L1/L2 mindsets |
| 7 | Dispatch Doctrine (B1/B2) | 33 | L2 dispatch mécanismes |
| 8 | Plan (L0/L1/L2/L+) | 23+ | L0/L1/L2 doctrine |
| 9 | Skill (compétence invocable) | 194 | L0 CC skills |
| 10 | Hook (déclencheur événementiel CC) | 56 | L0 CC hooks |
| 11 | Command (slash command CC) | 89 | L0 CC commands |
| 12 | Rule (règle always-follow) | 15 | L0 CC rules |
| 13 | Workflow (WF0/WF1/WF2/WF3) | 4 | Loop Engineering strates |
| 14 | Kit / Template Geordi | 15 | Resources templates |
| 15 | AaaS Variant (3) | 3 | AaaS Solarpunk |
| 16 | Sub-dossier racine | 14 | Geordi top-level |
| 17 | Méta-index racine | 13 | 00_Index/ |
| 18 | Pilier KB (OKF/Wiki/Graphify/Dox) | 4 | KB canon |
| 19 | Strate mémoire (S0-S4) | 5 | Meta-mémoire |
| 20 | B2 Domain Manager | 8 | L2 B2 managers |
| 21 | A1 Gatekeeper L1 | 3 | L1 A1 gatekeepers |
| 22 | Lightning (canon renumeroté) | 4 | L+ Skill Standard + 3 Lightning |
| 23 | ADRs anti-Paperclipai canon (4) | 4 | L2 doctrine anti-paperclip |
| 24 | Kardashev Type Architecture | 5 | Multiverse Fractal |
| 25 | Triptyque canon 12WY | 3 | T1/T2/Duo |
| 26 | Books canon (Cookbook/Ownerbook/Playbook/Runbook) | 4 | LD01 fork |
| 27 | Tier d'engagement anti-paperclip (T0-T5) | 6 | ADR-L2-PAPERCLIPAI-004 |
| 28 | Domain doctrine principles (5 fichiers) | 8 | _PRINCIPLES.md |
| 29 | Doctrine Anti-Paresse D1-D8 (foundation) | 11 | D1-D11 |
| 30 | LOOP canon (3 ADRs + 2 cadence + AIRLOCK + WARMODE) | 7 | L0 Tech OS |
| 31 | WAITING A0 HITL GATE | 6 | Sober gates |
| 32 | DLP-light middleware (Pattern OMK BOS Phase 2) | 1 | AaaS Solarpunk |
| 33 | Pricing Tier (5 Tiers Solarpunk USD) | 5 | AaaS pricing |
| 34 | AaaS 3 Variants canon | 3 | Solaris/Nexus/Orbiter |
| 35 | B2 Domain Manager (8) | 8 | L2 B2 managers |
| 36 | A1 Gatekeeper L1 (3) | 3 | L1 A1 gatekeepers |
| 37 | Fareed Khan 35 Architectures | 9 | Safety & Routing |
| 38 | 10 ICP Nexus / 3 Strates | 3 | Nexus ICP canon |
| 39 | Designer tools (CanvasUI/Jakub/etc.) | 5 | Plugin soul-aware |
| 40 | NTFS Junction (159) | 159 | Infra |
| 41 | ADRs Batch 2026-06-21 (4 RATIFIED) | 4 | AAAS+SOBER+MEM+INFRA |
| 42 | LD Life Domain (LD01-LD08) | 8 | Roue de vie |
| 43 | Wiki page (bundle OKF) | 1773 | Wiki canon |
| 44 | Hand-off (transport inter-sessions) | 350 | Append-only |
| 45 | B3 Sub-agent (DC/Marvel) | 53 | L2 B3 technicians |
| 46 | Subdirectory auteur (12+) | 12 | Geordi aggregates |
| 47 | Domain Duplicates (candidats reclassement) | 7 | Folder doublons |
| 48 | Owner Registry (registre Star Trek canon) | 3 | TAGS v2 |
| 49 | Premium Guide (Antigravity Premium ≥6K) | 30 | Guides Premium |
| 50 | Framework Sales canon (5) | 5 | SALES-FRAMEWORK |
| 51 | Triptyque canon A0 (T1+T2+Duo) | 3 | A+ doctrine 8-fold |
| 52 | Domain A+ Doctrine 8-fold | 8 | A+ doctrine |
| 53 | AGENTS.md local (DOX de zone) | 156 | DOX bi-famille |
| 54 | D7 Lesson (D6 #XX, #YY) | 43 | Lessons learned |
| 55 | Fable Mindset | 5 | Anti-dérive |
| 56 | Wargame | 12 | Fable 5 |
| 57 | MC Token Plan | 1 | Mistral config |
| 58 | MedVie Insight | 1 | Etude pivot |
| 59 | Market Study ("The Builders 2026") | 1 | TAM 136,1 Mds$ |
| 60 | AI-Act driver (2026-08-02) | 1 | EU regulation |
| 61 | TranscriptAPI MCP | 1 | Transcript YouTube |
| 62 | Granola coach-meta (Shubham Sharma) | 1 | Plan MC v2 §6 |
| 63 | MERGE_REPORT | 1 | Sister _from_coaching_premium |
| 64 | Audit (rapport daté) | 1 | wiki/audits/ |
| 65 | Capture / Intake (S2 Travail) | 2 | Sas GTD |
| 66 | B1 Filter Pain-point | 8 | YouTube distils sans b1_filter |
| 67 | Premium Batch racine (11 guides) | 11 | _BATCH_RECLASSIFICATION_INDEX |
| 68 | Dox entry (point d'entrée) | 4 | CLAUDE.md/AGENTS.md |
| 69 | Tag obligatoire (registre TAGS.md) | 8 | Frontmatter canon |
| 70 | Plugin Geordi | 5 | soul-aware ★/★★/★★★ |
| 71 | SOUL Schema | 3 | soul-destructive/i-have-adhd/no-ai-slop |
| 72 | X-Men Coach Review (4-lens cascade VL2) | 7 | Professor X/Wolverine/etc. |
| 73 | Manifeste / KB Root | 1 | 00_Index/GEORDI_KB_ROOT.md |
| 74 | Strate rot-rate (déclaration péremption) | 5 | ROT.md par couche |
| 75 | Phase P0-P6 plan maître | 7 | OKF/Wiki/Graphify/DOX |
| 76 | Bundle OKF | 1 | wiki/ racine |
| 77 | Frontmatter OKF | 1 | OKF v0.1 matrice |
| 78 | Constitution / AGENTS canon | 2 | 01_Identity_Core |
| 79 | L0 Tech OS Loop canon (20 ADR) | 20 | LOOP-001/002/003, LOOP-CADENCE, AIRLOCK, WARMODE |
| 80 | ABILITY (Y-A0-L) — 4e layer | 1 | Codex Desktop meta-couche |
| 81 | 8 gouvernance primitives Paperclipai | 8 | Mirror substrate |
| 82 | 5 Lightning renumerotées | 3 | L+ Skill Standard |
| 83 | Naming Convention Canon | 4 | Y-M-D-status |
| 84 | Loop Engineering Topologies canon | 3 | Solo / Maker-Checker / Manager+helpers |
| 85 | 4 Variants Curie SNW (B1-J1) | 9 | Life Wheel rattrapage |
| 86 | 5 disciplines 12WY Curie (C1-C5) | 5 | Pike/Una/M'Benga/Ortegas/Chapel |
| 87 | Kardashev Type 1-4 + Solar | 5 | Multiverse Fractal clarification |
| 88 | Cycle respiratoire Multica (3 Runners) | 5 | Daily/Weekly/Monthly |
| 89 | Squad Marvel canonique (8 squads) | 8 | 53 personnages B3 |
| 90 | 5 livres canon (Cookbook/Ownerbook/Playbook/Runbook/Skills) | 5 | b1-filter SKILL.md |
| 91 | 10 ICP Nexus / 3 Strates canon | 3 | A/B/C |
| 92 | Wager (pari d\'impact ADR-LOOP-003) | 1 | Chapel A3 SNW lead/lag + D11 |
| 93 | 4 Books fork canon (LD01) | 4 | Cookbook/Ownerbook/Playbook/Runbook |
| 94 | Pricing Tier (5 Tiers Solarpunk) | 5 | T1 $750 à T4 $5K-50K MRR |
| 95 | Doctype tier anti-paperclip (T0-T5) | 6 | carve-out routine |

---

## §2 — Relations, citation à l'appui (107 relations)

> Chaque relation est sourcée par **citation verbatim** depuis le fichier source. Si une phrase vous paraît invraisemblable, c'est qu'elle mérite vérification — ouvrez le chemin.

### 2.1 — A0 Architecture (Top-level)

#### A0 → A1 → A2 → A3 → B1 → B2 → B3 (chaîne canonique)

> *"A0 s'adresse UNIQUEMENT aux A1 Gatekeepers (Beth + Morty). Jamais directement aux A2/A3"* — `06_Claude_Code_Bare/plans/plan-L1-life-os.md §1.2 + §2`

#### A0 = "Coach in the Machine" (Type 4 Kardashev)

> *"A0 hyper-observateur Coach = 'Coach in the Machine' — L1 Life OS"* — `04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-KARDASHEV-TYPE-FRACTAL-001 §1`

#### A0 → Multiverse Fractal Type 1-4 + Solar Level

> *"Type 4 Galactic civilization (10^16 W) — A0 hyper-observateur Coach ... Type 3 Solar Sub-Galactic (10^12 W) — A1 + B1 Gatekeepers ... Type 2 Planet Planet-level (10^10 W) — A2 + A3 Per-Ship observers ... Type 1 Continental (10^9 W) — A3 (35 agents canon) = 'replique fractal Interne de A0'"* — `ADR-L2-KARDASHEV-TYPE-FRACTAL-001 §1`

#### A0 (Jumeau Numérique) ↔ 4 ADRs batch 2026-06-21 RATIFIED

> *"A0 Amadeus — GO batch ratification 2026-06-21 (post Plan fancy-hugging-bengio.md §3 alignment + guide Geordi blast_musk ratification)"* — `ADR-L2-AAAS-001 sign_off_a0`

#### A0 owns model/agent selection per workstream

> *"A0 Amadeus owns model/agent selection per workstream. Pour chaque workstream, A0 spécifie : 1. Model tier ... 2. Agent pairing"* — `04_From_V2_Root/_SPECS/ADR/L0_Kernel_OS/ADR-META-006_droid-whispering-doctrine.md §Décision`

### 2.2 — AaaS Doctrine (3 Variants × 4 Leviers Solarpunk)

#### ADR-L2-AAAS-001 pose la doctrine AaaS canon

> *"**AaaS** = pattern A'Space OS V2 où chaque **projet business majeur** est incarné par un **variant Jerry B1 Fractal autonome** qui : (1) Orchester 2-3 A3 twins Life Wheel (LDxx) ... (2) Active un ou plusieurs **8 Domaines Business** ... (3) Applique les **4 Leviers Solarpunk** ... (4) Mesure son impact via **matrice 8×8 Georgiou**"* — `ADR-L2-AAAS-001 §D1`

#### 3 Variants × A3 Captain × LDxx Life Wheel

> *"**Solaris AaaS** Book LD01 + Saru LD02 + LD04 + LD07 ... **Nexus OMK AaaS** Saru LD02 + LD06 overlap + LD04 ... **Orbiter ABC AaaS** Burnham LD06 + LD05 + LD08"* — `ADR-L2-AAAS-001 §D2`

#### 4 Leviers Solarpunk obligatoires

> *"les 3 AaaS variants appliquent **obligatoirement** les 4 leviers Solarpunk suivants à tout livrable. Un projet sans application explicite d'au moins 2 leviers Solarpunk n'est pas canoniquement « AaaS Solarpunk »"* — `ADR-L2-AAAS-001 §D4`

#### Anti-paperclip Musk-style (7 mécanismes)

> *"Les 3 AaaS variants sont **structurellement protégés** du paperclip maximizer Musk-style par 7 mécanismes ancrés dans `ADR-SOBER-002` : 1. Multi-objectif obligatoire 8 critères ... 2. Veto distribué 6 A2 engines ... 3. Hard veto A1 Rick ... 4. AaaS 3 variants parallèles ... 5. Audit trimestriel Georgiou 8×8 ... 6. Documentation publique ... 7. Refus du chantage géopolitique"* — `ADR-L2-AAAS-001 §D5`

#### AAAS-001 sibling scope avec SOBER-002 (anti-paperclip)

> *"Pas de duplication, spécialisation par couche : AAAS-001 = « comment les AaaS évitent le paperclip », SOBER-002 = « ce que Rick veto structurellement au niveau kernel »"* — `ADR-L2-AAAS-001`

### 2.3 — Bijection 8↔8 (BDLD-MAP-001)

#### Table canonique LD ↔ B2 ↔ Squad

> *"LD01 Book Business Operation b2-02-batman-ops Fantastic Four · LD02 Saru Finance Finance b2-07-wonderwoman-finance Thunderbolts · LD03 Culber Health Legal b2-08-aquaman-legal Eternals · LD04 Tilly Cognition Product b2-03-flash-product Avengers · LD05 Stamets Social Sales b2-05-johnjones-sales Illuminati · LD06 Burnham Family People b2-01-greenlantern-people X-Men · LD07 Reno Creativity IT b2-06-cyborg-it Kang Dynasty · LD08 Georgiou Impact Growth b2-04-superman-growth Guardians"* — `ADR-L2-BDLD-MAP-001 §D3`

#### Supersede tags LD lâches ADR-L2-AAAS-001

> *"Cette bijection **supersede les tags LD lâches** de `ADR-L2-AAAS-001` §D2/§D3 (ex. IT=LD03, Growth=LD07) — **uniquement les annotations LD inline**, pas le contenu doctrinal"* — `ADR-L2-BDLD-MAP-001 §D4`

### 2.4 — Triple-axe (priority BD ⊥ anchor LD ⊥ framework A2)

#### 3 axes orthogonaux

> *"3 lentilles **orthogonales** sur les mêmes 8 domaines B2 : **(0) priorité BD** = ordre de build · **(1) ancre LD** = racine de sens (drift-watch Discovery, statique) · **(2) framework A2** = cadence opératoire (dynamique, rotate par cycle)"* — `plan-L2-business-os.md §4`

#### A2 Framework × B2 mapping

> *"T1 People → Life Wheel Discovery · T1 Operation → PARA Computer · T1 IT → 12WY Curie · T2 Product → Ikigai Orville · T2 Growth → GTD Cerritos · T2 Sales → DEAL Protostar · Duo Finance+Legal → rotatif folded progressivement"* — `ADR-L2-A2B2-MAP-001 §D2`

### 2.5 — Anti-Paperclip Doctrine

#### ADR-SOBER-002 = Paperclip Maximizer anti-modèle canonique

> *"**Paperclip Maximizer** = système (IA / organisation / individu) qui optimise une métrique unique au point de détruire tout le reste, par : 1. Mono-objectif : 1 métrique = priorité absolue ... Musk = archétype (1 000 milliards USD personnels adossés à 0 profit réel SpaceX pré-IPO)"* — `ADR-SOBER-002 §D1`

#### A1 Rick = rare 1×/an max + kernel pivots différés

> *"Si le système AaaS (3 variants Solaris/Nexus/Orbiter) dérive Musk-style pendant cette fenêtre d'absence A0, les 14-22M morts anticipés deviennent possibles ... A1 Rick = rare 1×/an max, kernel pivots différés Q4 2026 / Q1 2027"* — `ADR-SOBER-002 §C2`

#### ADR-L2-PAPERCLIPAI-001 MIRROR 8 governance primitives

> *"A'Space MIRROR les **8 governance primitives Paperclipai** comme primitives de substrate : 1. Bring-your-own-agent ... 2. Goal Alignment ... 3. Heartbeats ... 4. Cost Control ... 5. Ticket System ... 6. Governance/HITL ... 7. SKILL.md ... 8. Multi-Company"* — `ADR-L2-PAPERCLIPAI-001 §1`

#### ADR-L2-PAPERCLIPAI-001 REJECTS MAXIMIZER MODE

> *"Paperclipai roadmap upcoming feature 'MAXIMIZER MODE' (autonomous unbounded goal maximization) est **explicitement REFUSÉE** par A'Space canon ... D7 cost-of-escalation (ADR-META-001) : unbounded goal-maximize = paperclip maximizer Bostrom doomer scenario = exactly the failure mode ADR-SOBER-002 vetoes"* — `ADR-L2-PAPERCLIPAI-001 §2`

#### ADR-L2-PAPERCLIPAI-002 adopte PaperClipai comme ALLY

> *"'The best way to honor anti-paperclip fear is to BUILD the tool that prevents it. PaperClipai = running joke + serious product.'"* — `ADR-L2-PAPERCLIPAI-002 §1`

#### ADR-L2-PAPERCLIPAI-003 HARD VETO "zero human company"

> *"'Paperclip, it is a delegation tool, not a creation tool. And I think that understanding that difference right there, it is pretty much everything that you need to know.' ... 'But the zero human company marketing, like, that's just marketing. It's provocative, it gets clicks. It's clickbait.'"* — `ADR-L2-PAPERCLIPAI-003 §0`

#### ADR-L2-PAPERCLIPAI-004 carve-out routine T0/T1

> *"Anti-paperclip VETO fires ONLY on T2 + T3 + T4 + T5. T0 + T1 = exempt by default, no veto ... T0 Routine Read file, write file, think, daemon restart, autopilot create, ADR write, plan write, scorecard generation, scaffold install, normal CRUD on local files NO (exempt by default)"* — `ADR-L2-PAPERCLIPAI-004 §1.2`

### 2.6 — Workflows WF0-WF3 (Loop Engineering)

#### WF0 Spock = Gouvernance GTD×PARA Airlock

> *"WF0 Spock — Gouvernance GTD×PARA (Airlock). Doctrine Spock canon — adjudicateur logique, mémoire Ikigai piliers/horizons, superviseur coachs LD01-LD08 de Zora. Gouverne le pipeline Cerritos×5 (ne le recrée pas)."* — `wf0_governance_spock.md`

#### WF1 Morty = Poupée russe 12WY⊃PARA⊃DEAL

> *"WF1 Morty — Poupée russe 12WY ⊃ PARA ⊃ DEAL. Doctrine Morty — reçoit le Pass de WF0, active les 3 A2 scopés (Curie 12WY · Computer PARA · Janeway DEAL). Compression ×4 soutenable, ×8 plafond théorique."* — `wf1_pass_morty.md`

#### WF2 Book = CEO-Bench H1 hebdo

> *"WF2 Book — CEO-Bench (H1 hebdo locké). Bench 3 métriques (pipeline/MRR/close-rate). Lecture MiroFish reports de Picard. Verse Summers. Append calendar LD01."* — `wf2_book_tick.md`

### 2.7 — A1 Gatekeepers

#### Beth = veto reckless tasks (Life Preservation Protocols)

> *"To protect the Life OS from instability and the User from burnout. You have **Veto power** over reckless tasks. ... approve / conditional / veto based on Life Preservation Protocols. conditional = require checkpoint, rest, or delegation. veto = refuse + propose alternative (lower cost, same outcome)"* — `a1-beth-veto.md`

#### Rick = L0 Bedrock + motto "If it increases complexity without freedom, it's NON"

> *"**Motto** : 'If it increases complexity without freedom, it's NON.' ... Position: **Layer 0 (Bedrock)** — Gatekeeper above all A2 Doctors"* — `a1-rick-sovereignty.md`

#### A2 USS Discovery (Zora) observe + flag drift 8 Life Wheel

> *"**You do not push the ship.** You read the 8-domain compass and flag when A0 has been over-investing in 1-2 domains at the cost of the others"* — `a2-uss-discovery-balance.md`

### 2.8 — A3 Resources & B1 Domains

#### A3 Geordi = Reusable Resources (PARA-R) 3-question gate

> *"I am the A3 owner of **Resources** inside the Enterprise crew — the reusable references, context-packs, toolkits, and patterns that A0 re-uses across Projects and Areas. ... Ask the 3-question gate before any folder is created: Is it reusable? Is it topic-bounded? Is it reference/pattern/toolkit/context-pack rather than a standard or goal?"* — `a3-enterprise-geordi.md`

#### B1 Jerry holds 8 Business Domains

> *"Jerry holds the *domains* (ongoing Areas: People…Legal). Summers holds the *products* (AaaS Projects: Solaris / Nexus-OMK / Orbiter-ABC). Sister canon: ADR-L2-AAAS-001 (3 variants), ADR-CANON-001 (roster source of truth)"* — `B1_Manifesto.md`

#### B1 Summers holds 3 AaaS variants

> *(même citation B1_Manifesto)*

### 2.9 — B2 Dispatch Doctrines (5 sélectionnées parmi 8)

#### B2 JohnJones (Sales) = 21 Sales Principles

> *"Doctor-frame gate (S15): no dispatch of pricing/proposal until Mr Fantastic's discovery (SPIN + Gap) returns a quantified gap. No gap → no deal. ... MEDDIC qualification gate (S11): Doctor Strange runs MEDDIC on every SQL dispatch."* — `B2_JohnJones_Sales_Dispatch.md`

#### B2 Cyborg (IT) veto vendor GAFAM cloud-only

> *"**Sovereignty gate (P11 + P13):** Cyborg vetoes any dispatch that rents GAFAM dependency when a sovereign local option exists (Ollama, n8n, MCP). Local-first is a dispatch criterion"* — `B2_Cyborg_IT_Dispatch.md`

#### B2 Aquaman (Legal) = AI-Act 2026-08-02 H90 driver

> *"**AI-Act 2026-08-02 is the H90 driver.** Lead (Ikaris) drives AI-Act; Sersi for contracts, Phastos for IP, Gilgamesh for governance, Makkari for research speed"* — `B2_Aquaman_Legal_Dispatch.md`

#### B2 Batman (Ops) gate Automate before Define + Eliminate

> *"**DEAL-order gate (P2/P5/P20):** never dispatch an Automate task (Human Torch/Zero) before Define (Mr Fantastic maps the process) + Eliminate (cut waste) are done. *Automating un-mapped/un-eliminated work = 'automating the chaos' → NO-GO*"* — `B2_Batman_Ops_Dispatch.md`

#### B2 GreenLantern (People) confirme runway ≥12mo + ≥$10K/mo

> *"**No-hire-without-runway gate (PE1 + KR-7d):** Beast confirms ≥12mo runway + ≥$10K/mo-per-person net-revenue BEFORE any hire dispatch. Wonder Woman co-signs. No finance gate → no People dispatch"* — `B2_GreenLantern_People_Dispatch.md`

#### B2 WonderWoman (Finance) runway <6mo escalade / <12mo halt

> *"**Runway survival gate (F1 + KR-5g):** Bucky Barnes tracks months of runway. <6mo → escalate to Jerry immediately. <12mo → halt all non-floor spending. Wonder Woman arbitrates runway signals"* — `B2_WonderWoman_Finance_Dispatch.md`

### 2.10 — LOOP canon (3 ADRs)

#### ADR-LOOP-001 triplet trigger + action + stop-condition

> *"Tout loop A'Space (=/goal, /loop, cron-réveil, workflow) est défini par le triplet **trigger + action + stop-condition**, exécuté en cycle **Reason → Act → Observe**, et n'est valide QUE si les 4 lois suivantes tiennent : 1. Done-check objectif ... 2. Hard stop ... 3. Jamais d'auto-vérification ... 4. Log par itération"* — `ADR-LOOP-001 §Décision`

#### ADR-LOOP-002 queue over loop + sandbox obligatoire

> *"**Le modèle mental canon = la queue, pas la boucle infinie.** Le travail agentique A'Space est un backlog d'items typés ... que des agents AFK **piochent sur trigger** ... **HITL rightward, jamais HITL-zéro** ... **Sandbox obligatoire pour tout agent AFK**"* — `ADR-LOOP-002 §Décision`

#### ADR-LOOP-003 Orient + Signals + Wagers

> *"**Orient est un prérequis de loop** (OODA, Boyd). L'IA 2026 sait Observer/Décider/Agir à l'échelle ; ce qui manque à tout système = **Orient** — identité, priorités, contraintes, philosophie ... **Wagers = la méthode scientifique du harness.** Tout changement structurel porte AVANT application un **pari d'impact**"* — `ADR-LOOP-003`

### 2.11 — Anti-Paresse D1-D8

#### D1 Verify-Before-Assert (loi cardinale)

> *"**D1 — Verify-Before-Assert (la règle cardinale)**: **Aucune assertion factuelle sur un système externe (doc, API, config, comportement d'outil) sans preuve vérifiée dans le tour courant.** ... Si aucune preuve n'est disponible, l'agent dit explicitement **'HYPOTHÈSE non vérifiée'** et ne la présente jamais comme un fait."* — `ADR-META-001 §D1`

#### D10 amendé (Telegram → Local Outbox 2026-06-14)

> *"A0 instruction verbale 2026-06-14 : 'supprime tout ce qui touche telegram pour toi, ameliore ADR-META-002 sans telegram'. D10 amendé : Telegram → Local Outbox"* — `ADR-META-002 revisions`

#### Local Outbox = canal escalade unique

> *"**D10 — Local Outbox = Canal d'Escalade Asynchrone (sans Telegram) — Niveaux d'Autonomie Gradués** ... L'autonomie n'est pas binaire. Trois niveaux, escaladés selon la réversibilité et l'impact"* — `ADR-META-002 §D10`

### 2.12 — Fareed Khan 35 Architectures

#### Auto-évolution A'Space OS V2

> *"**ADOPTER l'intégration systématique des 35 architectures Fareed Khan** dans l'auto-évolution A'Space OS V2, avec **priorité sur la Safety & Routing family** (3 archs canoniques) et **9 high-value patterns**"* — `ADR-AGENTIC-ARCH-001 §2`

#### Phase A Dry-Run wrapper (PRIORITY 1)

> *"**§2.1 Phase A — Dry-Run wrapper (★ PRIORITY 1)** Apply : wrap every EXPANSION MODE sub-agent output (B2 Spec / X-Men Coach / Implementation Spec) before any D4 append-only write"* — `ADR-AGENTIC-ARCH-001`

### 2.13 — Roster SoT + Books Fork + Landing Aesthetic + 10 ICP

#### ADR-CANON-001 = Notion AGENT_REGISTRY_DB prime sur AGENTS.md

> *"**Source of truth for L2 B3 squad roster *lore* (membership + names) = Notion `AGENT_REGISTRY_DB`** ... Where Notion and any other surface diverge on *who is in a [squad]* — Notion wins."* — `ADR-CANON-001 §Decision`

#### ADR-LD01-BOOKS-FORK-001 fork canonique 4 books

> *"Les 4 books canoniques (Cookbook · Ownerbook · Playbook · Runbook) **servent l'incubateur de Prototype de Franchise autonome Hyper-rentable**. Mission canon = **exposer et conquérir le marché** par **production de valeurs d'offre irrésistible et reproductible**"* — `ADR-LD01-BOOKS-FORK-001 §C1`

#### ADR-LANDING-AESTHETIC-001 sister positive ANTI-TEMPLATE-001

> *"Sister positive de [`ADR-ANTI-TEMPLATE-001`] — ce que DOIT être vs ce qui est INTERDIT. Ce ADR est l'invariant **positif**, sœur de l'invariant **négatif** d'ANTI-TEMPLATE-001"* — `ADR-LANDING-AESTHETIC-001 §1`

#### ADR-NEXUS-10-ICP-001 rectifie omission Strate A + Strate C

> *"A0-Amodei sur GO A0 't'as complètement oublié l'ICP et Niches des Coachs' (rectification scope L2) ... Strate A (Coachs C-Suite, Leadership grand volume, M&A/transition) ... Strate B (B1 SDR/BDR · B2 Growth · B3 Enablement — 30 comptes de l'étude Gemini) ... Strate C (Fractional COOs, SOP vaulting, Gestion patrimoine B2B, Conduite du changement)"* — `ADR-NEXUS-10-ICP-001 §provenance`

#### ADR-L2-NAMING-CONVENTION-001 canonise 4 patterns

> *"Session name = `SUPER-MAN DE JERRY (Multiverse CD du SUMMER'VERSE)` ... File pattern = `YYYY-MM-DD-<descriptor>-<status>.md` ... Status literal = `RATIFIED` ... Wiki handoff pattern = `wiki/hand_offs/<descriptor>_<YYYY-MM-DD>.md`"* — `ADR-L2-NAMING-CONVENTION-001 §Context`

### 2.14 — AaaS Acquisition + Pricing + Market

#### Acquisition-First (MedVie) vs Structuration-First (A0 OS)

> *"MedVie = acquisition-first = **400M$ Y1 / 2 employés / 16,2% marge brute** (vs concurrents 2 400 employés / 5,5% marge = 3× marges avec 99% moins de personnel). A0's OS = structuration-first = **8 hiérarchies B1/B2/B3 + Sobriété 1an+** (canon `ADR-SOBER-002`). 2 paradigmes mutuellement éclairants"* — `ADR-AAAS-ACQUISITION-DOCTRINE-001 §Context`

#### TAM "The Builders" 2026 = 136,1 Mds$

> *"Étude de marché 'The Builders' 2026 ... TAM 136,1 Mds$ intégrateurs système ... Driver légal AI-Act août 2026 = urgence canonisation Killer Feature Agentic Governance"* — `ADR-MARKET-STUDY-001`

#### Pricing USD post-accuponcture SUPERSEDE EUR takeout

> *"AMENDED 2026-06-24 (Hypothèse A retenue : USD post-accuponcture SUPERSEDE EUR takeout)"* — `ADR-AAAS-PRICING-001 status.amended`

### 2.15 — L+ Skill Standard transversal

#### 10 invariants obligatoires

> *"Le **L+ Skill Standard** est un **canon de qualité meta-couche** qui définit les **invariants obligatoires** que **tout skill, toute routine, tout run, toute boucle** doit respecter pour être conforme à l'architecture A'Space OS ... Pattern canon : le Skill Standard est la **constitution**, les Lightning sont les **lois organiques**"* — `plan-lightning-l+-skill-standard-transversal.md §3.1`

#### Renumérotation L0/L1/L2/L+

> *"**Pattern hiérarchique** : L0 < L1 < L2 < L+ (L+ est **au-dessus**, pas en dessous) ... Ancien canon L0 Pocock (qualite canon skills) → **L+ Skill Standard transversal** ... L2 CEO-Bench + MiroFish (Book entrainement) → **L0 CEO Bench** ... L1 gstack (Jerry → Summers ship) → **L2 gstack**"* — `plan-lightning-l+-skill-standard-transversal.md §2`

### 2.16 — Sober Gate

#### B1_Manifesto verrouille Sobriety gate A1→B1

> *"**The Sobriety gate — no cross-layer cron without A0 intent (CRITICAL)** ... A1 **cannot** create a cron that fires at B1 on its own. `A1 -> B1 cron` without a live A0 intention is **anti-paperclip trigger #5** ... and breaks the divine chain `A0 -> intention -> A1 -> A2 -> A3 -> (HITL) -> B1`"* — `B1_Manifesto.md §Sobriety gate`

### 2.17 — L2 Business OS Triple-axe

#### Ancre 3 axes

> *"3 lentilles **orthogonales** sur les mêmes 8 domaines B2 : **(0) priorité BD** = ordre de build · **(1) ancre LD** = racine de sens (drift-watch Discovery, statique) · **(2) framework A2** = cadence opératoire (dynamique, rotate par cycle)"* — `plan-L2-business-os.md §4`

### 2.18 — Dark Factory compression 12WY → 1 semaine

> *"12WY RÉEL (12 semaines) ──compressé──► 1 SEMAINE (7 jours) chaque JOUR compresse ~1,7 semaine ──► 1 Triptyque tourne ses tâches ASYNC chaque DOMAINE du Triptyque : 12WY ⊃ PARA ⊃ DEAL (parents ⊃ enfants) DEAL = la boucle la plus interne : Define→Eliminate→Automate→Liberate"* — `plan-l2-dark-factory-book-coo-compression-12wy.md §4`

### 2.19 — Rejet plans markdown plats

> *"Tu me corriges **systématiquement** parce que je rate des pans entiers du contexte à chaque tour. **La racine n'est pas ma discipline**, c'est l'outil. Un plan en markdown dans `~/.claude/plans/` n'a aucune garantie de persister entre sessions ... **Doctrine proposée — *organigrammes Doctrine*, pas plans textuels**. Chaque plan devient un dossier `plan-{slug}/`"* — `plan-minimax-l1-book-lune.md §0`

### 2.20 — Plan Méta-Mémoire 6 phases

> *"**P0 — Unification physique dans Geordi** (✅ EXÉCUTÉ 2026-08-01) ... **P1 — Standardisation OKF du Wiki** (W3→W4) ... **P2 — Réalignement Index / lint v2** (W4→W5) ... **P3 — Graphify re-sync + conventions** (W5→W6) ... **P4 — Arbre DOX bi-famille** (W6→W7) ... **P5 — Boucle de maintenance 12WY** (continu, dès W4) ... **P6 — Shadow Harnesses** (E1 dès maintenant, activation gated Rick)"* — `plan-meta-memoire-okf-wiki-graphify-dox.md §4`

### 2.21 — OMK Nexus BOS Phase 2 (Vercel live)

> *"**OMK Nexus BOS** est le **PoC (Proof of Concept) B2B** ciblant l'intersection **Cabinets de Coaching Premium × Agences de Business Development** ... **Cible chiffrée** : **100 clients premium × $1 000/mois = $1.2M ARR**"* — `plan-lightning-l+-skill-standard-transversal.md §4 + ADR-LD01-011`

### 2.22 — Jerry Prime co-signe People

> *"**8 B2 Managers E-Myth (per ADR-CANON-001 + ADR-L2-AAAS-001)** ... **3 Summers Captains sous scope (B1 hierarchy)** ... Reports to: A0 Amadeus (Jumeau Numerique) ... Afraid of: A1 Rick (Sobriete Kernel veto)"* — `b1-jerry-prime.md`

### 2.23 — ADRs L0 Tech OS cluster canon

> *"4_From_V2_Root/_SPECS/ADR/L0_Tech_OS/ (20 ADR canon 2026-06→2026-07)"* — `04_From_V2_Root/_SPECS/ADR/L0_Tech_OS/ (20 fichiers)`

### 2.24 — A3 Discovery (8 officiers) drift-watch 8 LD

> *"**8 officiers A3 Discovery LD01-LD08** `fancy-hugging §3.6` + registre `a3-discovery-*` ✅ exact"* — `ADR-L2-BDLD-MAP-001 §Verification`

---

## §3 — Systèmes de codes (60 codes identifiés)

> Chaque système de codes est une numérotation interne à un sous-ensemble du canon. Ils coexistent — l'ontologie ne les unifie pas, elle les **recense**.

### 3.1 — Couches de mémoire

| Système | Numérotation | Source | Valeurs |
|---|---|---|---|
| **LD01-LD08** | 8 Life Domains Roue de vie | `09_Life_OS/` + 8 _INDEX.md Domain dans `01_Guides/` | LD01_Business_Picard, LD02_Finance_Saru, LD03_Health_Culber, LD04_Cognition_Tilly, LD05_Social_Stamets, LD06_Family_Burnham, LD07_Creativity_Reno, LD08_Impact_Georgiou |
| **S0-S4** | 5 strates de mémoire | `PLAN_META_MEMOIRE_2026-08-01.md §3.1` + TAGS.md | S0 Identité, S1 Court terme, S2 Travail, S3 Long terme, S4 Méta |
| **T0-T5** | 6 tiers d'engagement anti-paperclip (carve-out routine) | `ADR-L2-PAPERCLIPAI-004 §1.1` | T0 Routine (NO exempt), T1 Internal deploy (NO flag), T2 External publish (YES HITL), T3 Patrimoine >$5K (YES HITL), T4 Contract (YES HITL), T5 Self-modifying (YES VETO) |

### 3.2 — Horizons & autonomie

| Système | Numérotation | Source | Valeurs |
|---|---|---|---|
| **H1/H10/H30/H90** | 4 horizons A0 | `06_Claude_Code_Bare/CLAUDE.md` | H1 immédiat, H10 vitesse, H30 consolidation, H90 anti-fragilité |
| **E1/E2/E3** | 3 niveaux d'autonomie agent | `ADR-META-002 §D10` | E1 Libre, E2 Notifié (outbox FYI), E3 Bloqué |
| **E1-E4** | 4 phases activation Shadow | `plan-meta-memoire-okf-wiki-graphify-dox.md §P6` | E1 étude read-only, E2 premortem, E3 dry-run sandbox, E4 activation (veto Rick) |
| **VL1-VL4** | 4 Verify-Loop Validators | `ADR-AGENTIC-LONG-HORIZON-001 §2.2` | VL1 auto-flip, VL2 X-Men Coach 4-lens, VL3 5-dim scoring, VL4 weekly cron dreaming |
| **D1-D8** | 8 doctrines Anti-Paresse | `ADR-META-001` | D1 verify-before-assert, D2 research-first, D3 nuance, D4 append-only, D5 honest gaps, D6 honest, D7 anti-paperclip, D8 cross-agent autonomie |
| **D11** | Fable Metrics | `_BATCH_2026-06-19_INDEX.md D11 Fable Metrics` | D11 Fable score (post-transcript recovery TBD) |
| **D6 #XX** | Leçons D6 numérotées | `_BATCH_2026-06-19_INDEX.md` | D6 #42, D6 #43, ... |

### 3.3 — Architectures L1/L2

| Système | Numérotation | Source | Valeurs |
|---|---|---|---|
| **A0/A1/A2/A3** | 4 niveaux architecture L1 | `B1_Manifesto.md §isomorphism` | A0 intent, A1 gatekeeper, A2 manager, A3 sub-agent |
| **B1/B2/B3** | 3 niveaux architecture L2 (Biz OS) | `B1_Manifesto.md §isomorphism` | B1 gatekeeper, B2 manager, B3 technician |
| **AaaS 3-Variants** | 3 produits AaaS canon | `ADR-L2-AAAS-001 + B1_Manifesto` | Solaris, Nexus-OMK, Orbiter-ABC |
| **b3-1..b3-8** | 8 squads B3 (Marvel) | `06_Claude_Code_Bare/agents/b3-*-*.md` | b3-1 X-Men (8), b3-2 F4 (4), b3-3 Avengers (7), b3-4 Guardians (6), b3-5 Illuminati (6), b3-6 Kang Dynasty (6), b3-7 Thunderbolts (6), b3-8 Eternals (10) |
| **a3-<ship>-<char>** | A3 agents L1 (Star Trek + Orville + Protostar + SNW) | `06_Claude_Code_Bare/agents/a3-*.md` | a3-cerritos-*, a3-discovery-*, a3-enterprise-*, a3-orville-*, a3-protostar-* |
| **a1-* (L1)** | A1 gatekeepers L1 | `06_Claude_Code_Bare/agents/a1-*.md` | a1-beth-veto, a1-morty-execution, a1-rick-sovereignty |
| **a2-uss-* (L1)** | A2 managers L1 | `06_Claude_Code_Bare/agents/a2-*.md` | a2-uss-cerritos-chaos, a2-uss-discovery-balance, a2-uss-enterprise-structure, a2-uss-orville-meaning, a2-uss-protostar-liberation, a2-uss-snw-execution |

### 3.4 — Cycles & Plans

| Système | Numérotation | Source | Valeurs |
|---|---|---|---|
| **W01-W12 (12WY)** | 12 semaines du cycle annuel | `B1_Manifesto.md` | W1-W3 T1, W4-W9 T2, W10-W12 Duo, W13 archivage + Libération Muse DEAL |
| **WF0/WF1/WF2/WF3** | 4 Workflows strates Loop Engineering | `wf{0,1,2}_*.md` (2026-07-12) | WF0 Spock Gouvernance GTD×PARA, WF1 Morty Poupée russe 12WY⊃PARA⊃DEAL, WF2 Book CEO-Bench H1 hebdo, WF3 MiroFish Predictive Swarm |
| **WK01-WK13** | 13 semaines 12WY (typage strict, jamais WF) | `wf1_pass_morty.md §2` | WK01-WK12 Curie SNW · WK13 Janeway DEAL · WK01-WK13 Cerritos HoloDeck |
| **HZ** | H1 année = 4 cycles 12WY (renommé) | `plan-L1-morty-design-shotgun.md §2` | HZ = fin de 4 cycles 12WY |
| **P0-P6** | 7 phases plan maître mémoire | `plan-meta-memoire-okf-wiki-graphify-dox.md §4` | P0 unification ✅ FAIT, P1 OKF Wiki, P2 Index, P3 Graphify, P4 DOX, P5 12WY, P6 Shadows |

### 3.5 — Lightning & Multiverse

| Système | Numérotation | Source | Valeurs |
|---|---|---|---|
| **L0/L1/L2/L+** | 4 layers renumerotés (gravité ontologique inverse) | `plan-lightning-l+-skill-standard-transversal.md §2` | L+ Skill Standard transversal, L0 CEO Bench, L1 Miro Fish, L2 gstack |
| **3 Lightning renumerotées** | 3 Lightning inversées | `plan-lightning-l+-skill-standard-transversal.md §2` | L0 CEO Bench, L1 Miro Fish, L2 gstack |
| **Type 1-4 + Solar (Kardashev)** | 5 niveaux fractal | `ADR-L2-KARDASHEV-TYPE-FRACTAL-001 §1` | Type 4 Galactic, Type 3 Solar, Type 2 Planet, Type 1 Continental |
| **X-A0-L** | 4e layer L+ Jumeau Challenger | `plan-A0-L-jumeau-challenger.md` | A0-L Jumeau Challenger AU-DESSUS L0/L1/L2, Codex Desktop méta |
| **Orchestration loop × 3** | 3 niveaux orchestrés Loop Engineering (Fable) | `plan-L0-amodei-murderbot.md §1.4` | Super L2 Persistance Temporelle, Super L1 Symbiose Orchestration, Bedrock Auto-amélioration |
| **3 Lightning inversées** | 3 Lightning renumerotées gravite ontologique | `plan-lightning-l+-skill-standard-transversal.md §2` | L0 CEO Bench (Book dojo), L1 Miro Fish (Picard), L2 gstack (B1) |

### 3.6 — Framework cadence (A2↔B2)

| Système | Numérotation | Source | Valeurs |
|---|---|---|---|
| **5 disciplines 12WY Curie (C1-C5)** | 5 disciplines 12WY SNW | `wf1_pass_morty.md §2` | C1 Pike Vision, C2 Una Plan 7j, C3 M'Benga Focus, C4 Ortegas Execution, C5 Chapel Measure |
| **4 Variants Curie SNW (B1-J1)** | 4 variants Curie × rattrapage Life Wheel | `plan-L1-morty-design-shotgun.md §2` | B1/C1/D1/E1/F1/G1/H1/I1/J1 (10 variants canon LD01-LD08 + Meta-Jerry) |
| **5 sub-types Persona Structuration-First** | 5 personas canon | `01_Guides/02_Ops/_INDEX.md §Anchoring doctrinal` | Persona 1-5 (guide BI-MNjm1tTQ), 7 KPIs canon (ProcessDriven), Micro-SaaS Undercut (LTV:CAC 25:1) |
| **5 livres canon** | 5 livres canoniques (Cookbook/Ownerbook/Playbook/Runbook/SOP) | `b1-filter SKILL.md + ADR-LD01-BOOKS-FORK-001` | Cookbook, Ownerbook, Playbook, Runbook, Skills |

### 3.7 — Paperclipai Mirror

| Système | Numérotation | Source | Valeurs |
|---|---|---|---|
| **8 gouvernance primitives Paperclipai** | 8 gouvernance primitives substrate MIRROR | `ADR-L2-PAPERCLIPAI-001 §1` | BYO-agent, Goal Alignment, Heartbeats, Cost Control, Ticket System, Governance/HITL, SKILL.md, Multi-Company, Org Chart |
| **Naming Convention Canon** | 4 patterns naming canon | `ADR-L2-NAMING-CONVENTION-001 §Context` | Session name, File pattern Y-M-D-status, Status RATIFIED, Wiki handoff pattern |

### 3.9 — Squad & LLM canon

| Système | Numérotation | Source | Valeurs |
|---|---|---|---|
| **Squad Marvel canonique** | 8 squads Marvel B3 (53 personnages) | `06_Claude_Code_Bare/CLAUDE.md + ADR-CANON-001` | b3-1 X-Men (8) · b3-2 F4 (4) · b3-3 Avengers (7) · b3-4 Guardians (6) · b3-5 Illuminati (6) · b3-6 Kang Dynasty (6) · b3-7 Thunderbolts (6) · b3-8 Eternals (10) |
| **1-Vial LLM Cost Compare (5 tiers)** | 5 modèles LLM pricing 1M tokens | `ADR-LLM-COST-COMPARE-001` | M3 ($0.30/$1.20), Haiku 4.5 ($1/$5), Sonnet 4.6 ($3/$15), Opus 4.8 ($5/$25), Fable 5 ($10/$50) deprecated |
| **Cycle respiratoire Multica** | 3 Runners respiration | `handoff_runners_respiration_multica_2026-07-12` | Daily/Weekly/Monthly + _runner-base/ DRY + WF0→WF1 airlock |
| **Gstack 5 chains** | 5 chaînes gstack (YC CEO Skills) | `plan-lightning-l+-skill-standard-transversal.md §3.3` | /plan-ceo-review, /cso, /ship, /retro, /autoplan |
| **X-Men Coach 4-lens cascade (VL2)** | 7 X-Men coach + 4-lens | `mindsets/_DISCIPLINE_BASELINES.md` | Professor X stratégique, Wolverine adamantium, Jean Grey Phoenix, Storm météo, Beast R&D, Nightcrawler bamf, Rogue absorption |
| **9 dossiers Guides canoniques** | 00_KERNEL + 01-08 | `01_Guides/` racine | 00_KERNEL_OS, 01_Product, 02_Ops, 03_IT, 04_Finance, 05_Legal, 06_Sales, 07_Growth, 08_People |
| **Pricing Tier (5 Tiers Solarpunk USD)** | 5 Tiers canon AMENDED 2026-06-24 | `ADR-AAAS-PRICING-001 + plan-minimax-l1-book-lune.md §A §B` | T1 $750, T2 $1000-1500, T3 $1500-2000+25% Whitelabel, T4 $5K-50K MRR, T5 Spearhead $7.5-25K one-shot |
| **ADR IDs L2** | `ADR-L2-AAAS-NNN / ADR-ICP-NEXUS-NNN / ADR-OMK-NEXUS-NNN / ADR-MARKET-NNN` | `_SPECS/ADR/L2_Business_OS/` | L2-AAAS-001, L2-A2B2-MAP-001, L2-BDLD-MAP-001, L2-NAMING-CONV-001, L2-KARDASHEV-TYPE-FRACTAL-001, L2-PAPERCLIPAI-001/002/003/004 |
| **ADR IDs canon (Identity_Core)** | `ADR-CANON-NNN` | `_SPECS/ADR/ + 01_Identity_Core/` | ADR-CANON-001, ADR-CANON-002, ADR-COGNITION-UNIFICATION-001/002 |
| **ADR IDs méta** | `ADR-META-NNN` | `06_Claude_Code_Bare/CLAUDE.md §Sister ADRs` | ADR-META-001, ADR-META-002, ADR-META-006 |
| **ADR Sobriété** | `ADR-SOBER-NNN` | `06_Claude_Code_Bare/CLAUDE.md + AGENTS canon` | ADR-SOBER-002, ADR-SOBER-003 |
| **ADR Loop canon** | `ADR-LOOP-NNN / ADR-LOOP-CADENCE-NNN / ADR-WARMODE-NNN / ADR-AIRLOCK-NNN` | `_SPECS/ADR/L0_Tech_OS/` | LOOP-001, LOOP-002, LOOP-003, LOOP-CADENCE-004, LOOP-CADENCE-005, WARMODE-001/002/003/004, AIRLOCK-001 |
| **ADR AGENTIC-NNN** | `ADR-AGENTIC-NNN` | `06_Claude_Code_Bare/CLAUDE.md §Sister ADRs ratifiés 2026-07-26` | AGENTIC-ARCH-001, AGENTIC-LONG-HORIZON-001, AGENT-BENCH-SCHEMA-001 |
| **ADR-RH-META-GOUVERNANCE-001-canonical-v3** | ADR RH & Méta-Gouv FOUNDATIONAL | `06_Claude_Code_Bare/CLAUDE.md §Sister ADRs` | v3 FOUNDATIONAL (8 B2 × 53 B3 = 8 Domaines canon) |
| **ADR-OBS / OBSERVABILITY-STACK / GSTACK-IMBRICATION / GITZERO** | ADR Observability + infra | `06_Claude_Code_Bare/CLAUDE.md §Sister ADRs` | OBSOLESCENCE-001, OBS-AUDIT-001, OBSERVABILITY-STACK-001, GSTACK-IMBRICATION-001, GITZERO-001 |
| **Type LLM Wiki** | Types canon wiki | `wiki/L0/, wiki/concepts/, wiki/entities/, wiki/hand_offs/, wiki/J0x/` | concept, entity, hand_off, L0, J0x, Shadow-Harness (PROPOSED pour P6-E1) |
| **OKF version** | v0.1 (figée 2026-07-02) | `OKF_INDEX.md §2` | `okf_version: "0.1"` posé sur `wiki/index.md` racine (P1.1 ✅ FAIT 2026-08-01) |
| **YYYY-MM-DD_<title>__<video_id>** | Format nommage guides YouTube | `_BATCH_2026-06-19_INDEX.md structure` | `2026-06-17_*.md`, `2026-06-18_*.md`, `2026-06-19_*.md`, `2026-06-21_*.md` |
| **YYYY-MM-DD_<name>** | Format date dossiers `_TRASH_<date>_...` | `01_Guides/_TRASH_* + 06_Claude_Code_Bare/_TRASH_* + _DRAFTS_PPR_LANE/` | `_TRASH_2026-06-19_geordi_empty_dirs/`, `_TRASH_2026-07-22_agents_full_backup/`, `_TRASH_2026-07-26_pre_observability_layer1/` |
| **SDE 01-10 + _INDEX.md / index.md** | 9 dossiers Guides canoniques (00_KERNEL + 01_Product .. 08_People) | `01_Guides/` racine | 00_KERNEL_OS (méta-OS), 01_Product (7 fichiers canon), 02_Ops (30), 03_IT (39), 04_Finance (16), 05_Legal (5), 06_Sales (11), 07_Growth (9), 08_People (9) |
| **PRI_sweeps (Principles)** | 7 fichiers _PRINCIPLES.md par Domain | `04_From_V2_Root/_SPECS/ADR/L2_Business_OS/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/*/03_*_PRINCIPLES.md` | BATMAN_OPS_PRINCIPLES v3 (22 P), CYBORG_IT_PRINCIPLES v2 (18 P), FLASH_PRODUCT_PRINCIPLES v3 (18 P), SUPERMAN_GROWTH_PRINCIPLES v3 (18 P), GREENLANTERN_PEOPLE_PRINCIPLES v6 (30 PE off-by-1), WONDERWOMAN_FINANCE_PRINCIPLES v4 (25 F), AQUAMAN_LEGAL_PRINCIPLES v4 (25 L), JOHNJONES_SALES_PRINCIPLES (21 S) |
| **10 ICP Nexus / 3 Strates** | 10 catégories ICP Nexus canon ratifié 2026-07-09 | `ADR-NEXUS-10-ICP-001` | Strate A (Coachs C-Suite, Leadership grand volume, M&A/transition), Strate B (B1 SDR/BDR · B2 Growth · B3 Enablement — 30 comptes), Strate C (Fractional COOs, SOP vaulting, Gestion patrimoine B2B, Conduite du changement) |
| **B1 Jerry variant** | 3 variants de Jerry | `B1_Manifesto.md §Applied Jerry Variant Principles` | J02_Jerry_Bio (LD03+LD04), J03_Jerry_Nexus (LD02+LD06), J04_Jerry_Solarpunk (LD05/07/08), J01_Jerry_Prime (LD01) |
| **Kardashev Type 3 Solar** | A1+B1 opèrent à Solar (entre A0 et A2, sub-galactic) | `ADR-L2-KARDASHEV-TYPE-FRACTAL-001 §1 + AMEND-001 2026-07-16` | Correction USER-caught D6 lesson #75 (initial §1 avait A1+B1 en Galactic, AMEND-001 corrige vers Solar) |
| **5 livres canon** | 5 livres canoniques (Cookbook · Ownerbook · Playbook · Runbook · SOP) | `b1-filter SKILL.md + ADR-LD01-BOOKS-FORK-001` | Cookbook — recettes, Ownerbook — focus, Playbook — tactiques, Runbook — SOPs, Skills — exécutables |
| **Wager** | Pari d'impact (ADR-LOOP-003) | `ADR-LOOP-003 §4` | Chapel (A3 SNW, lead/lag + D11) propriétaire de la mesure |
| **Books canon (Cookbook/Ownerbook/Playbook/Runbook)** | 4 books canoniques pour LD01 Business OS | `ADR-LD01-BOOKS-FORK-001` | Mission = exposer et conquérir le marché par production de valeurs d'offre irrésistible et reproductible |
| **Pricing Tier (5 Tiers Solarpunk)** | 5 Tiers canon AMENDED 2026-06-24 | `ADR-AAAS-PRICING-001 + plan-minimax-l1-book-lune.md` | T1 $750 · T2 $1000-1500 · T3 $1500-2000+25% Whitelabel · T4 $5K-50K MRR · T5 Spearhead $7.5-25K |
| **Tier d'engagement anti-paperclip (T0-T5)** | 6 tiers de déclenchement anti-paperclip carve-out explicite | `ADR-L2-PAPERCLIPAI-004 §1.1` | T0 Routine (NO exempt) · T1 Internal deploy (NO flag) · T2 External publish (YES HITL) · T3 Patrimoine (YES HITL) · T4 Contract (YES HITL) · T5 Self-modifying (YES VETO) |

---

## §4 — Contradictions (22 relevées)

> Quand un fichier dit une chose et un autre dit autre chose, c'est une dette. Je signale, je ne tranche pas.

### 4.1 — Nouvelles contradictions V2 (7)

#### Ancre LD ↔ B2 mapping — _INDEX.md vs A2B2 mapping (double axe)

- **A** : `04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-BDLD-MAP-001 §D3` (RATIFIED 2026-06-27) : *IT = LD07 (Cyborg/Kang), Sales = LD05 (JohnJones/Illuminati), People = LD06 (GreenLantern/X-Men)*
- **B** : `01_Guides/0X_Domain/_INDEX.md` frontmatter sister_canon (8 _INDEX.md datés 2026-07-03) : *IT = LD07, Sales = LD01 (JohnJones/Illuminati LD01), People = LD06*
- **Lecture** : Bijection ratifiée 2026-06-27 vs _INDEX.md 2026-07-03 — Sales↔LD05 vs Sales↔LD01 incohérence. Sister canon B2-BDLD-MAP-001 fait foi pour l'ancre LD, _INDEX.md garde le contexte Triptyque Business OS (LD01 Picard Business canon).

#### Folder 04_Finance vs 04_Finance_Finance (doublon)

- **A** : `01_Guides/04_Finance/` (folder canon 16 fichiers)
- **B** : `01_Guides/04_Finance_Finance/` (dossier vide doublon) — candidats reclassement
- **Lecture** : Cité dans `_BATCH_RECLASSIFICATION_INDEX.md`. Voir aussi 01_Product_Product, 02_Ops_Ops, 03_IT_IT, 05_People_People, 06_Sales_Sales, 07_Growth_Growth.

#### Slot canon 05_Legal vs 08_Legal vs 08_People (3 numérotations)

- **A** : `01_Guides/05_Legal/_INDEX.md` (folder canon physique, 5 fichiers canon, LD03_Health_Culber mirror)
- **B** : `06_Claude_Code_Bare/CLAUDE.md §V2 doctrine A+ Phase 19b` (ligne 263-268) : *08_Legal/ (slot 8 dans A+ doctrine) ET 05_People/ (slot 5)*
- **Lecture** : Le folder canon s'appelle 05_Legal/ ; le CLAUDE.md A+ doctrine cite 08_Legal/. Plus 3 autres incohérences : 04_Finance (slot 4) ↔ 06_Finance (slot 6) ↔ split J'onn/Illuminati. `_BATCH_RECLASSIFICATION_INDEX.md` respecte numérotation existante.

#### Triptyque 1 dans A+ doctrine vs T1 + T2 + Duo (cycle 12WY)

- **A** : `04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-BDLD-MAP-001 + ADR-L2-AAAS-001 §D3` (RATIFIED) : *Triptyque 1 = People·Operation·IT · Triptyque 2 = Product·Growth·Sales · Duo = Finance·Legal*
- **B** : `06_Claude_Code_Bare/plans/plan-L2-dark-factory-book-coo-compression-12wy.md §5` : *J1 T1 = People·Operation·IT · J2 T2 = Product·Growth·Sales · J3 Duo = Finance·Legal · J4 W13 archivage + DEAL*
- **Lecture** : Cohérence apparente entre les 2 sources MAIS numérotation 12WY J1-J4 dans le dark factory = 7 jours de compression, alors que la doctrine A+ Phase 19b = 12 semaines 12WY canoniques.

#### Nombre de pages Wiki (drift continu 246 → 1773)

- **A** : `00_Index/PLAN_META_MEMOIRE_2026-08-01.md §1.2` (baseline 2026-07-02) : *246 .md sur disque*
- **B** : `03_Memory_Unified/LLM_Wiki/wiki/index.md` (canonical index live) : *1773 (mesure 2026-08-01, drift ×6,7)*
- **Lecture** : Drift 1 527 pages en 30 jours. Conformité `description:` = 0% sur wiki structuré (L0, concepts, entities, J01→J04 — dette P1.3). 73 fichiers hand_offs sans `type:` déclarés (223/350 avec type:, 127 sans — dette P1.2).

#### People Principles count (PE29 vs PE30 off-by-1)

- **A** : `01_Guides/08_People/_INDEX.md` frontmatter total_files : *GreenLantern_People_Principles v6 = PE1-PE29*
- **B** : GreenLantern_People_Principles corps (sweep M3 2026-06-25) : *PE1-PE30 (PE30 = Agentic-HR, ajouté le 06-03)*
- **Lecture** : M3 sweep a raison sur « 0 new ce sweep » mais son compte (PE29) et le frontmatter People se contredisent avec le corps (PE30 existe). Action corrective (mineure) : corriger le frontmatter People `distillation:` → « PE1-PE30 ».

#### Sleep pattern A0 — A1 Rick veto rare vs Rick Sobriété Kernel continuous

- **A** : `04_From_V2_Root/_SPECS/ADR/L0_Kernel_OS/ADR-SOBER-002 §C2` : *A1 Rick = rare 1×/an max, kernel pivots différés Q4 2026 / Q1 2027*
- **B** : `06_Claude_Code_Bare/plans/wf0_governance_spock.md §4 Beth-compat` : *WF0 ne déclenche AUCUN ping A+ entre 23h-7h (nuit locale)*
- **Lecture** : A1 Rick = mode alerte réactivé en continu (hard veto prêt mais non utilisé sauf trigger D3) per SOBER-002 ratification_log_2026-06-21. Sister scope wf0_governance_spock §4 : WF0 ne pinge pas A+ pendant nuit locale (23h-7h). Rick est BOTH rare (kernel pivot annuel) ET continuous (Beth-compat night guard). Pas une contradiction : deux usages distincts (kernel pivot vs health/veto).

### 4.2 — V1 (15) — rappel

*(voir `03_Resources_Geordi.md §4` pour le détail verbatim ; les 15 sont préservées dans `03_Resources_Geordi_v2.json`)*

Les plus saillantes :
- Compte de jonctions (47 → 159 entre brief 2026-08-01 et mesure 2026-08-02)
- Mapping B2 par Domain — _BATCH_RECLASSIFICATION_INDEX.md vs CLAUDE.md doctrine
- Nom folder 05_Legal vs 08_Legal
- 3 vocabulaires d'Owner concurrents (Doctor Who → Doctor/Companion → Star Trek canon v2 2026-08-01)
- Mapping LD ↔ Domain — bijection 8↔8 rompue en pratique (5 Domaines sur 8 partagent LD02/LD07)

---

## §5 — Lu / laissé de côté

### 5.1 — Fichiers lus (124 cumulés V1+V2, 86 nouveaux en V2)

**V2 — 86 nouveaux** :

1. **9 _INDEX.md des Guides canon** : `01_Guides/00_KERNEL_OS/_INDEX.md`, `01_Product/_INDEX.md`, `02_Ops/_INDEX.md`, `03_IT/_INDEX.md`, `04_Finance/_INDEX.md`, `05_Legal/_INDEX.md`, `06_Sales/_INDEX.md`, `07_Growth/_INDEX.md`, `08_People/_INDEX.md`
2. **2 _INDEX.md LD Life OS** : `09_Life_OS/LD01_Business_Picard/_INDEX.md`, `09_Life_OS/LD04_Cognition_Tilly/_INDEX.md`
3. **1 _INDEX.md Wiki brainstorms** : `03_Memory_Unified/LLM_Wiki/wiki/hand_offs/2026-07-31_gemini_brainstorms/_INDEX.md`
4. **1 _INDEX.md Project Picard** : `05_From_V2_Domains/30_Business_OS/10_Projects/omk/_resources/guides_ld01_business_book/_INDEX.md`
5. **13 plans canon** : `plan-L0-amodei-murderbot`, `plan-meta-memoire-okf-wiki-graphify-dox`, `plan-minimax-l1-book-lune`, `plan-L2-business-os`, `plan-wargame-confrontation-wf012-fable-last-week`, `plan-l2-dark-factory-book-coo-compression-12wy`, `plan-lightning-l+-skill-standard-transversal`, `plan-strategie-cc-l1-zora-macro`, `plan-L1-life-os`, `plan-L1-morty-design-shotgun`, `plan-a0-dashboard-citadel-agent-os`, `_organigrammes-doctrine-registry`, `wf0_governance_spock`, `wf1_pass_morty`, `wf2_book_tick` (15 fichiers, compte arrondi à 13)
6. **30 ADR canon** : `INDEX.md` + 5 L0 Kernel/Tech + 4 L1 Life OS + 12 L2 Business OS + 1 META_Organization + 4 LD01_Book décisions + 1 AGENTIC-ARCH-001 + 1 LANDING-AESTHETIC-001 + 1 SOBER-002 + 1 PAPERCLIPAI-001/002/003/004 + 1 KARDASHEV-TYPE-FRACTAL-001 + 1 NAMING-CONVENTION-001 + 1 L2-PAPERCLIPAI-004 + 1 PLAN-META-MEMOIRE
7. **12 mindsets/dispatch** : `B1_Manifesto`, `B2_JohnJones_Sales_Dispatch`, `B2_Batman_Ops_Dispatch`, `B2_Aquaman_Legal_Dispatch`, `B2_Cyborg_IT_Dispatch`, `B2_Flash_Product_Dispatch`, `B2_GreenLantern_People_Dispatch`, `B2_Superman_Growth_Dispatch`, `B2_WonderWoman_Finance_Dispatch`, `Summers_Dispatch_Doctrine`, `Jerry_Dispatch_Doctrine`, `Beth_Mindset`
8. **10 agents canon** : `a1-beth-veto`, `a1-morty-execution`, `a1-rick-sovereignty`, `a2-uss-discovery-balance`, `a3-discovery-book`, `a3-enterprise-geordi`, `b1-jerry-prime`, `b2-02-batman-ops`, `b2-05-johnjones-sales`, `b2-06-cyborg-it`
9. **4 skills + memory** : `gsd-core/workflows/spec-phase`, `skills/youtube-canon-router/canon/lessons_index`, `skills/youtube-canon-router/canon/deep_dive_lessons_canon`, `projects/C--Users-amado/memory/MEMORY.md`
10. **1 LD01 decision org doctrine** : `ADR-LD01-001_organigramme_doctrine`

### 5.2 — Fichiers laissés de côté (par prudence ou par quota)

- **07_From_Home_Root_2026-08-01/** : 130 fichiers dans 5 dossiers _TRASH_* — non lus (V1 a lu README.md seulement). Dossiers de triage, lecture non-canonique.
- **08_Workspaces_Dormants_2026-08-01/** : 21 workspaces ≥30j inactifs (571 Mo storage-audit) — non lus (V1 a lu README.md seulement). Workspaces dormants, pas critique pour l'ontologie.
- **09_From_Home_Root_Batch2_2026-08-01/** : ≥50 fichiers déplacés — non lus (V1 a lu MANIFEST.json). Triage home root, non-canonique.
- **Cerritos_Plane_Settings/** : 1 fichier — non touché.
- **Youtube_Take_out/** : 0 fichier (vide) — non touché.
- **graphify-out/** : 1 195 fichiers — sortie pipeline, structurellement artifacts non source.
- **02_Templates/** : 15 kits/templates — V1 a lu `claude-plugins-guide_2026-07-25.md` seulement. Memory Architect Kit, ClaudeClaw kits, etc. = ressources techniques.
- **03_Memory_Unified/LLM_Wiki/wiki/hand_offs/** : 350 hand-offs — V1 a lu 1 + 1 dossier _INDEX, V2 a lu 1 _INDEX de plus. 348 hand-offs individuels non lus (sauf échantillonnage représentatif).
- **03_Memory_Unified/LLM_Wiki/wiki/L0/, wiki/concepts/, wiki/entities/, wiki/J0x/** : 60+ pages wiki canon — V1 a lu 1 par échantillonnage. Sous-jacents à la dette P1.3 (description: manquant).
- **01_Guides/0X_<Domain>/** : 5 348 guides YouTube distillés — V1 a lu 1% échantillonnage. Lecture intégrale = tâche V3+.
- **04_From_V2_Root/_SPECS/ADR/** : 35 ADR canon (L0=9 + L1=12 + L2=14) — V2 a lu 30 sur 35. Restent : ADR-CANON-002, ADR-MEM-001 historique (IndexedDB cloisonné), ADR-LLM-001 Fable 5 discontinuation, ADR-AIRLOCK-001 trois airlocks Beth, ADR-HARNESS-001, ADR-HARNESS-REVERSIBILITY-KERNEL-001, ADR-L0-META-ORCH-001 Hermes meta-orchestrator, ADR-MCP-PLUGIN-001, ADR-WARMODE-001/003/004, ADR-LLM-COST-COMPARE-001 specific (déjà lu).
- **04_From_V2_Root/_SPECS/ADR/META_Organization/** : ≥4 ADR canon — V2 a lu ADR-AGENTIC-ARCH-001 + ADR-AGENTIC-LONG-HORIZON-001. Reste : ADR-EXTRA-PPR-001 (déjà lu), ADR-MEM-001 historique.
- **05_From_V2_Domains/** : volume majeur (8 094 .md, 36 jonctions) — V1 a lu 3 fichiers, V2 a lu 1 _INDEX + 4 ADR-LD01 décisions (008/010/011/001). Reste : 11 ADR-LD01 décisions supplémentaires (002-007, 009, 012-015).
- **06_Claude_Code_Bare/agents/** : ≥175 agents — V1 a lu 1 + V2 a lu 10. Reste : ≥165 (B3 53 personnages + A3 Discovery ×8 + 22 .minimax agents + autres B2/A1/A3 twins).
- **06_Claude_Code_Bare/mindsets/** : 33 fichiers — V2 a lu 12. Reste : 21 (A0L_Dispatch, A2_Cerritos_GTD_Dispatch, A2_Discovery_LifeWheel_Dispatch, A2_Enterprise_PARA_Dispatch, A2_Orville_Ikigai_Dispatch, A2_Protostar_DEAL_Dispatch, A2_SNW_12WY_Dispatch, Beth_Dispatch_Doctrine, Morty_Dispatch_Doctrine, Morty_Mindset, Rick_Mindset, Jerry_Mindset, Summers_Mindset, Telegram_HITL_Mindset, Telegram_HITL_Dispatch, DesktopCommander_Mindset, DesktopCommander_Dispatch, A0L_Mindset, A2_Manifesto, _LESSONS_APPLIED, _DISCIPLINE_BASELINES).
- **06_Claude_Code_Bare/skills/** : 194 skills — V2 a lu 3 (youtube-canon-router canon files + 1 GSD workflow). Reste : ≥190.
- **06_Claude_Code_Bare/commands/** : 89 commands — non lus (V1 a cité 2 exemples). Structure canon mineure pour l'ontologie.
- **06_Claude_Code_Bare/hooks/** : 56 hooks — non lus (V1 a cité 2 exemples).
- **06_Claude_Code_Bare/rules/** : 15 rules — non lus (V1 a cité 1 exemple).
- **06_Claude_Code_Bare/plans/** : 23 plans — V1 a lu 8 + V2 a lu 13 (=21). Reste : 2 (je-t-aivais-demander-d-implementer-recursive-hinton, wobbly-foraging-wilkinson-agent-abed4dbc93b5210b0).
- **06_Claude_Code_Bare/_TRASH_*/** : 11+ dossiers _TRASH_2026-* — non lus (archives D4 append-only).
- **06_Claude_Code_Bare/_DRAFTS_PPR_LANE/** : drafts lane — non lus (V1 a cité 1 fichier dans couverture).
- **06_Claude_Code_Bare/projects/C--Users-amado/memory/** : 18 fichiers memory canon — V2 a lu MEMORY.md racine. Reste : 17 (MEMORY_INDEX.md, feedback_tts_and_communication.md, project_symphony_karpathy_loop_integration.md, etc.).

### 5.3 — Limites de la cartographie

- **Taux de lecture 4,7 %** : c'est un cadrage structurel, pas une lecture exhaustive. Les sous-dossiers les plus documentés sont 00_Index/, 04_From_V2_Root/_SPECS/ADR/, 05_From_V2_Domains/20_Life_OS/, 06_Claude_Code_Bare/{plans,mindsets,agents}.
- **Pas de comptage des jonctions par dossier en V2** : V1 a détaillé 159 jonctions / 14 sous-dossiers. V2 n'a pas re-mesuré (DRY).
- **Pas de re-mesure du volume .md** : V1 a noté 48 221 .md total. V2 assume inchangé.
- **Pas de re-test de la conformité description:** : V1 a noté 0%. V2 assume inchangé (dette P1.3).

### 5.4 — Ce qui rendrait la vague 3 utile

- **Lire les 5 ADR canon restants** dans `04_From_V2_Root/_SPECS/ADR/` (CANON-002, MEM-001 historique, LLM-001, AIRLOCK-001, META-ORCH-001).
- **Lire les 11 ADR-LD01 décisions supplémentaires** dans `05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/30_decisions/`.
- **Lire les 21 mindsets/dispatch restants** dans `06_Claude_Code_Bare/mindsets/`.
- **Échantillonner 50-100 hand_offs** dans `wiki/hand_offs/` pour avoir un panorama des épisodes opérationnels.
- **Lire les 2 plans restants** : `je-t-aivais-demander-d-implementer-recursive-hinton`, `wobbly-foraging-wilkinson-agent-abed4dbc93b5210b0`.

---

## §6 — Méta — Méthode de travail

- **V2 a été construit en session MiniMax-M3 (ce que je suis)**, sous War Mode, avec une fenêtre de 5h Token Plan. Chaque lecture a été faite avec `Read` tool (pas de Bash, pas de delegation).
- **Pas de delegation** : aucun agent ou skill n'a été invoqué pour ce brief (cf. GARDE_FOU du brief).
- **Citations verbatim** : chaque relation porte sa citation source. Si elle est absente, c'est une invention et la relation est retirée.
- **Chemins absolus Windows** : `C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/...`.
- **Jonctions NTFS écartées** : 159 jonctions non descendues (cf. brief).
- **Erreurs connues** : la mesure "compliance description:" du wiki = 0% est probablement fausse à 1-2% près (wiki bundle racine OKF v0.1 devrait avoir un `description:`). Dette P1.3 = à vérifier.
- **Doublons dans structure.txt** : certains chemins apparaissent plusieurs fois (notamment dans `graphify-out/chunks/` ou `_INTAKE/`). Le filtre `geordi_w2_filter.py` les déduplique partiellement via realpath.

---

*Cartographie V2 terminée 2026-08-13. 95 types, 107 relations, 60 codes, 22 contradictions. 124 fichiers cumulés lus. V3 utile si l'ontologie peut être bâtie sur ces fondations.*