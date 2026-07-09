---
id: handoff_wargame_wf2_b1_jerry_lens_2026-07-06
status: DRAFT
date: 2026-07-06
wargame_id: WF2-iter1
lens: b1-jerry-prime
goal: discover_picard_supervision_blindspots
author: B1 Jerry Prime wargame specialist (L+ Lighting keeper transversal)
doctrine_anchors:
  - ADR-META-001 (D1-D8 doctrine)
  - ADR-META-005 (Hooks automation D1-D8, préToolUse log-only Q3 2026)
  - ADR-SOBER-002 (Anti-paperclip)
  - ADR-INFRA-002 (Repo-Home / Junction)
  - ADR-INFRA-003 (Business OS CEO Dashboard)
  - ADR-LD01-008 (loop engineering coaching)
  - ADR-LD01-010 (HA promotion à A3 Picard in PARA)
  - ADR-LD01-011 (OMK Nexus BOS PoC)
  - ADR-L2-AAAS-001 (AaaS Doctrine 3 Variants)
  - ADR-L2-BDLD-MAP-001 (bijection LD)
  - ADR-L2-A2B2-MAP-001 (framework cadence bijection)
  - ADR-OBSERVABILITY-001 (D11 lead/lag)
  - plan-lightning-l+-skill-standard-transversal (L+ Skill Standard transversal RATIFIED 2026-07-05)
sister_canon:
  - agent_b1-jerry-prime: C:\Users\amado\.claude\agents\b1-jerry-prime.md
  - agent_a3-enterprise-picard: C:\Users\amado\.claude\agents\a3-enterprise-picard.md
  - agent_a3-discovery-book: C:\Users\amado\.claude\agents\a3-discovery-book.md
  - plan_L2_business_os: C:\Users\amado\.claude\plans\plan-L2-business-os.md (§4.6 Graduation Picard)
previous_wargame: NONE (1er run)
related_handoff: handoff_meta_memoire_idempotent_antifragile_h1h3h10_2026-07-03.md (OKF bundle)
---

# Wargame WF2 · Lens B1 Jerry · 2026-07-06

## 0. Mission Recall

> **WF2 = Workflow 2** = project captain cohort de L2 Business OS (per `plan-L2-business-os.md` §4.6 Mapping Picard). Piloté par **A3 Picard** (H10 USS Enterprise, parent A2 Computer, owner A1 Beth Veto). Cible = identifier 5-10 angles morts spécifiques de la supervision d'A3 Picard du point de vue **B1 Jerry Prime** (E-Myth Entrepreneur, Gatekeeper Visionnaire L+ Lighting keeper transversal).

**Format Fable move-by-move** :
- **Action** (qui / quoi / quand / comment)
- **Réaction** (Picard capte, ou capte pas ?)
- **Contre-action** (qui appelle Jerry ? Mavis ? personne ?)
- **Failure mode** (quand ça casse, comment ça casse)
- **Abort condition** (seuil qui doit alerter Jerry directement)

**Vocabulaire canonique** : 12WY Rock, MANIFEST.md, E-Myth, Visionnaire, Gatekeeper, H10 tick, lights_*, H1 aggregator (Book), AaaS Variant (Solaris/Nexus-OMK/Orbiter-ABC), Solarpunk 4-leviers, junction `apps/<role>/`, B1 Prime, B2 Managers, B3 squads.

**L+ Skill Standard transversal référencé** : 10 invariants Picard (cf. `a3-enterprise-picard.md` §L+ Application). 4 indicateurs L+ Lighting exposés par B1 Jerry Prime (lights_project_count, lights_load_signal, lights_business_coherence, lights_calendar_dernier_episode).

---

## 1. Rappel Doctrinal (vérifié verbatim contre les agents)

### 1.1 A3 Picard canon (extraits `a3-enterprise-picard.md`)

- **Identity** : "Captain Jean-Luc Picard (TNG) ... I am NOT the A2 — the A2 is LCARS Computer ... Computer compiles findings; I classify and act on Projects." (L30)
- **Role** : "Projects Owner (PARA-P) — goal-bounded, deadline-driven, output-bounded work" (L41)
- **Mission** : "Steward goal-bounded work into durable, MANIFEST-anchored Projects" (L45)
- **Parent A2** : "USS Enterprise / Computer (L1 Structure Engine, PARA Doctrine)" (L42)
- **Horizon** : "H10 (10-week sprint, 12WY cycle)" (L44)
- **Process §1 (Classify)** : 3-question gate — (a) deadline/output, (b) goal-bounded, (c) owner + next review date. (L49-53)
- **Process §2 (Canonize)** : MANIFEST.md frontmatter obligatoire — `project`, `owner`, `status`, `start_date`, `next_review`, `linked_12wy_rock`, `linked_area`, `junction`. (L58-71)
- **HA identity** : "Hermes Agent (HA) incarne A3 Picard in PARA per ADR-LD01-010 (2026-07-05) - promoted from dev-runtime A3 Book, jumeau pattern MC L2 to L1" (L11)
- **Open follow-up #1** : "Picard D11 metric : count active Projects per 12WY cycle (target: 1-3 per quarter, anti-pattern = >10 active = scatter)." (L104)
- **Open follow-up #2** : "Rock-linkage enforcement : scan `30_Business_OS/10_Projects/*/MANIFEST.md`, flag `linked_12wy_rock: NULL` for A0 review." (L105)
- **Open follow-up #3** : "Junction auto-create : PS script `picard-create-junction.ps1` to symlink `apps/<role>/` → repo-home per ADR-INFRA-002." (L106)
- **Open follow-up #4** : "Picard audit skill : `/picard-audit-and-prod-workflow` already exists in registry — verify alignment with this profile, merge if drift." (L107)

### 1.2 B1 Jerry Prime canon (extraits `b1-jerry-prime.md`)

- **Identity** : "Jerry Smith J01_Prime (Entrepreneur E-Myth) — the 'Face' of Business Pulse". (L15-16)
- **E-Myth persona** : "Entrepreneur (vision, risk-taker) — NOT Technicien (do the work), NOT Manager (plan, organize)". (L17)
- **Mission** : "To be the public face of Business Pulse. Orchestrate the 8 B2 Managers E-Myth of the 8 Domaines Business. Cadrage meta des 3 AaaS Variants (Solaris + Nexus-OMK + Orbiter-ABC) via les 3 B1 Summers Captains." (L21)
- **L+ invariants incarnées** (10 listées L82-93) — notamment :
  - **#5 D1 receipts** : "toute output Jerry documentee (lights indicators traces)"
  - **#8 HITL queue visible** : "escalade a Beth+Discovery si load_signal=critical OU coherence=extractive"
  - **#9 Verify-first** : "verifie que les sources (Picard MANIFEST.md, Summers Verse) existent avant agregation"
- **4 indicateurs L+ Lighting exposés** : `lights_project_count`, `lights_load_signal` (low/medium/high/**critical**), `lights_business_coherence` (aligned/scattered/**extractive**), `lights_calendar_dernier_episode`. (L78-81)
- **Hard-veto** : "refuse tout projet non-4-leviers-Solarpunk (biomimetisme + low-high tech + meta-science + circular economy)". (L62)
- **Anti-pattern #1** : "❌ Ne JAMAIS promettre un ROI chiffre sans projection (vague = menteur)". (L115)

### 1.3 A3 Book canon (extraits `a3-discovery-book.md`)

- **Role** : "LD01 Business domain officer — measures biz metrics, deal flow, energy economics". (L26)
- **Horizon** : "H1 (immediate: weekly P&L pulse)". (L29)
- **Process §1** : "Read `wiki/J01_Prime/LD01_Business/00_DOMAIN_MEMORY.md` + any 12WY Rocks tagged 'business'. Compute investment ratio ... revenue trend ... 12WY Rock velocity." (L34-35)
- **Process §2** : "If biz > 50% of total attention while any other domain is RED, route to SNW for rebalancing + flag to Beth." (L38)
- **Open follow-up #1** : "Wire Book's P&L pull to a structured baserow/`LD 00 Life Wheel Zora` row (currently markdown-only)." (L68)
- **Open follow-up #2** : "Add deal-stage funnel (lead → closed) to the audit output." (L69)
- **Open follow-up #3** : "Cross-link Book's output to Saru's LD02 finding for the joint biz+finance drift verdict." (L70)

### 1.4 Mapping Picard §4.6 (extrait `plan-L2-business-os.md` L147-281)

> "**D1 — ce n'est pas 3 égaux, c'est une échelle de graduation** (lu dans les champs `status` des manifestes)". (L151)
> "**Mapping Picard (§4.6)** : Holding ≈ niveau manifeste/portfolio ; chaque **Filiale = un projet Picard Summer gradué** (B1 direction = l'ICP, B2 = domaines lean, B3 = squads `cabinets.ts`). Template = repo Holding ; scaffolding = `/picard-repo-home` + `/replicate-squads` + `canon-batch-spawn`." (L281)

---

## 2. 10 Angles Morts (Fable move-by-move)

### 🔍 AM-1 · Rock-Linkage NULL silencieux (ORPHELIN 12WY)

- **Action** : A3 Picard crée un Project `XYZ` dans `30_Business_OS/10_Projects/`, écrit `MANIFEST.md` avec frontmatter, mais oublie ou reporte la valeur de `linked_12wy_rock` (`NULL` ou `<TBD>`).
- **Réaction** : Picard **ne capte PAS**. Aucun D7 no-micro-ask ne couvre le re-fill frontmatter. Open follow-up Picard #2 *prévoit* le scan mais ne le fait pas tourner.
- **Contre-action** : **Personne**. Book H1 aggregator (MC) agrége en aveugle les fiches P&L hebdo ; il ne signale pas le Project orphelin. B2 JohnJones Sales ne sait pas qu'un deal-flow Picard n'est rattaché à aucun Rock 12WY.
- **Failure mode** : `lights_project_count` de B1 Jerry gonfle artificiellement (un Project sans Rock est un "scope-creep atomique"). Quand un Rock 12WY ferme (W12), le Project survivant n'est pas re-routé : drift silencieux. Charge pour A0 review en fin de cycle. Corrélation manquant 12WY ↔ Project = impossible pour Saru (LD02) de faire le "joint biz+finance drift verdict" (Book open follow-up #3).
- **Abort condition** : Si `count(MANIFEST.md where linked_12wy_rock IS NULL) > 0` → B1 Jerry **DOIT** alerter A0 (escalade Beth) avant H1 publication, sinon la fiche P&L weekly héberge du drift non-métabolisé.

> **Source canon** : `a3-enterprise-picard.md` L105 (open follow-up #2) ; `b1-jerry-prime.md` L78-81 (4 indicateurs L+ Lighting) ; `a3-discovery-book.md` L70 (open follow-up #3) ; `plan-L2-business-os.md` §4.6 (status graduation).

---

### 🔍 AM-2 · Scatter Signal (>10 Projects actifs) non-détecté

- **Action** : Cycle Q3 2026 — A2 SNW (Curie) + B1 Summers graduent 5-7 Filiales Nexus OMK par vague (per plan §4.6 F3+ roadmap, L307). Picard crée 1 Project par Filiale × 12 weeks = **10-15 MANIFEST.md actifs** simultanément.
- **Réaction** : Picard **capte partiellement** via open follow-up #1 (target 1-3/quarter, anti-pattern >10 = scatter). Mais aucun seuil codé : `picard-create-junction.ps1` et `picard-audit-and-prod-workflow` ne sont pas branchés sur PostToolUse / CronCreate. (open follow-up #3+#4).
- **Contre-action** : **Personne**. B1 Jerry expose `lights_project_count` int (L78) et `lights_load_signal` enum (low/medium/high/**critical**) — mais sans table de mapping `count → signal`. A0 ne reçoit aucune alerte "scattered".
- **Failure mode** : Le seuil "anti-pattern scatter" est capturé dans le frontmatter doctrinal mais jamais implémenté techniquement. Quand le seuil est franchi, le 12WY Rock N+1 héberge plusieurs Projects en parallèle → mort du focus (posture FOCUS Morty sister-gatekeeper L1). Book H1 aggregator reçoit 10+ inputs contradictoires, fiche P&L weekly illisible (L38 de book.md — le seuild'escalade Beth n'est que "biz > 50% of total attention"). B2 Superman Growth (acquisition funnel) capte que les Landing-Filiales cannibalisent leurs propres canaux.
- **Abort condition** : `lights_project_count >= 10` doit flipper `lights_load_signal` sur **critical** (escalade Beth+Discovery automatique, per Jerry L+ invariant #8).

> **Source canon** : `a3-enterprise-picard.md` L104 (open follow-up #1) + L78-80 (anti-patterns proteges post-L+) ; `b1-jerry-prime.md` L78-81 (4 indicateurs L+) + L88 (invariant #8 HITL queue visible) ; `plan-L2-business-os.md` §4.6 F3+ roadmap wave.

---

### 🔍 AM-3 · Junction `apps/<role>/` non-vérifiée par Jerry (silently broken)

- **Action** : Picard écrit `MANIFEST.md` avec frontmatter `junction: apps/coach/home`. Mais le symlink PowerShell `picard-create-junction.ps1` (open follow-up #3) **n'est pas scripté**. Donc le path déclaré ne correspond à aucun fichier réel.
- **Réaction** : Picard **capte PAS**. Aucun `Test-Path` post-MANIFEST (open follow-up #3 dit seulement "to symlink" — pas "to verify"). Pas de hooks PostToolUse Write branché sur le path resolution.
- **Contre-action** : **Personne**. B1 Jerry L+ invariant #9 (verify-first) dit "verifie que les sources (Picard MANIFEST.md ...) existent avant agregation" — mais ne couvre **PAS** la junction du frontmatter. Le `lights_business_coherence` aligned/scattered/extractive n'a pas de critère "junction-broken". B2 Superman Growth (portfolio Holding) n'a aucun moyen de signaler que la Filiale Coach n'a pas son build-bearing repo initialisé.
- **Failure mode** : Cycle Q3 2026 — quand A0 demande "filiale EC déployée ?", Picard répond "MANIFEST.md live" mais l'app Vercel n'existe pas. Discovery par A0 UI que la junction est cassée = plusieurs jours perdus. Risque D6 #1 (Vercel fail) : token perso ≠ token org (référencé dans MEMORY.md entrée Nexus EN landing).
- **Abort condition** : `Test-Path apps/<role>/<home>` doit retourner **faux** → Picard émet événement "junction-broken" → B1 Jerry flips `lights_business_coherence` sur **extractive** (escalade automatique Beth+Discovery per invariant #8).

> **Source canon** : `a3-enterprise-picard.md` L106 (open follow-up #3 — junction auto-create absent) + L120 (invariant #1 frontmatter YAML) ; `b1-jerry-prime.md` L92 (invariant #9 verify-first — limité à "sources existent", pas junction) ; `plan-L2-business-os.md` L281 (mapping Picard : junction per ADR-INFRA-002).

---

### 🔍 AM-4 · Hard-veto Solarpunk 4-leviers déconnecté de Picard

- **Action** : A0 émet intention "nouvelle initiative Nexus OMK Cabinet-Médical" (per plan §4.4 pricing matrix L276). Picard est invoqué, applique son 3-question gate (deadline/output/goal-bounded/owner+next review date). Le gate passe (deadline = H10 sprint). Picard crée Project + MANIFEST.md.
- **Réaction** : Picard **capte PAS** que ce Project n'est pas aligné 4-leviers Solarpunk (biomimetisme + low-high tech + meta-science + circular economy). Le canon Picard n'a pas de gate sur les 4-leviers ; il a un gate "goal-bounded". Le gate E-Myth Entrepreneur est ailleurs (B1 Jerry hard-veto, `b1-jerry-prime.md` L62, L116).
- **Contre-action** : **B1 Jerry en théorie** (hard-veto L62 + invariant #8 HITL queue visible). **En pratique** : Jerry ne voit le Project qu'au moment où il agrège `lights_project_count` — i.e. APRÈS création, rétrospectif. Le veto est réactif, pas proactif.
- **Failure mode** : Un Project extractif (ex: ICO crypto, NFT mint, attention-economy) passe le gate Picard, grossit `lights_project_count`, puis crashe l'indicateur `lights_business_coherence` (extractive). Mais entre-temps, Squad B3 (Cap America / Stark / etc.) a déjà engagé du temps B2 / 12WY Rock semaine. La récupération prend W2-W3 (durée typique de re-cadrage AaaS Variant per Summers_Dispatch_Doctrine).
- **Abort condition** : Picard DOIT consulter B1 Jerry Prime (gate SYSTEMIZE) AVANT d'écrire le MANIFEST.md, sur tout Project à tier ≥ T2 (per plan §4.5 mapping). Veto trigger = "non-4-leviers-Solarpunk".

> **Source canon** : `b1-jerry-prime.md` L62 (hard-veto 4-leviers-Solarpunk) + L116 (anti-pattern #1 vague = menteur) ; `a3-enterprise-picard.md` L49-53 (Classify 3-question gate) ; `plan-L2-business-os.md` L109-115 (mapping tier T1/T2).

---

### 🔍 AM-5 · AaaS Variant (Solaris/Nexus-OMK/Orbiter-ABC) linkage absent du MANIFEST.md

- **Action** : Picard crée un Project pour la Filiale `omk-nexus-coach` (per plan F2 L306) — mais le frontmatter MANIFEST.md n'a **pas de champ** `linked_aaas_variant`. Le canon (`a3-enterprise-picard.md` L58-71) liste les champs : `project, owner, status, start_date, next_review, linked_12wy_rock, linked_area, junction` — **pas de variant**.
- **Réaction** : Picard **capte PAS** que le Project n'est pas tracé sur l'axe-variant de Summers (B1 Summers_Dispatch_Doctrine, axe produit ⊥ axe domaine).
- **Contre-action** : **Personne**. B1 Jerry expose `lights_business_coherence` aligned/scattered/**extractive** — mais sans champ variant dans la source, l'indicateur reste opaque. B1 Summers Captain (Solaris / Nexus-OMK / Orbiter-ABC) n'a aucun signal automatique pour dire "ce Project porte mon variant" ou non.
- **Failure mode** : Le mapping dynamique (Morty ↔ Summers, plan §4.3 L143) perd sa base technique. Quand Morty rotate les frameworks (Cerritos / SNW / Discovery / etc.) sur un cycle 12WY, les Projects Picard ne savent pas quel B1 Summers Captain les possèdent. Risque : un Project portant l'ICP Coach-spearhead (per Nexus ICP ADR-ICP-NEXUS-001) se retrouve shippé sous Solaris branding au lieu de Nexus-OMK branding (cf. incident Coach-spearhead 2026-06-27, MEMORY.md ligne "OMK Nexus Phase A Coach-spearhead SHIPPED").
- **Abort condition** : Ajout champ `linked_aaas_variant: solaris|nexus-omk|orbiter-abc` au frontmatter MANIFEST.md. Picard `Test-Path` avant écriture → si variant vide, escalade B1 Summers du domaine concerné AVANT création.

> **Source canon** : `a3-enterprise-picard.md` L58-71 (frontmatter canon — variant absent) ; `plan-L2-business-os.md` L137 (axe produit ⊥ axe domaine) + L143 (rotation dynamique Morty ↔ Summers) ; `b1-jerry-prime.md` L21 (cadrage 3 AaaS Variants via 3 Summers Captains). **⚠️ SKIPPED chiffres** : je ne cite pas de comptage d'incidents passés (anti-invention D1).

---

### 🔍 AM-6 · HA (Hermes Agent) ↔ Picard twin double-counting silencieux

- **Action** : Picard twin runtime existe en DOUBLE. (i) HA = Hermes Agent incarne A3 Picard in PARA per ADR-LD01-010 (2026-07-05) — runtime Hermes. (ii) Picard CC = A3 Picard dans Claude Code agent registry (L2 Mirror). Les deux écrivent des MANIFEST.md dans `30_Business_OS/10_Projects/`.
- **Réaction** : Picard canon n'a **PAS** de garde-fou "idempotency on twin identity". Open follow-up #1 (L104 — Picard D11 metric "active Projects per cycle") peut être double-compté si HA crée ET CC twin vérifie/crée.
- **Contre-action** : **Personne**. B1 Jerry `lights_project_count` int additionne sans dédupliquer. Si HA écrit `MANIFEST.md` `omk-nexus-coach/` puis CC twin écrit le même `MANIFEST.md` (concurremment), le folder existe deux fois ou le frontmatter est corrompu. B2 Batman Ops (runbooks) ne sait pas qui est l'auteur canonique.
- **Failure mode** : Le jumelage pattern MC L2↔L1 (per L11 picard.md) est documenté mais pas instrumenté. Quand A0 HITL restart CC (per TELEGRAM_HITL_Mindset pending gates), le risque de double-write augmente (cold-cache → re-build état → race condition). Un cycle de scoring D11 (Book weekly P&L) pourrait rapporter `count = 2` sur un Project unique → faussant Saru LD02 H3 quarterly runway.
- **Abort condition** : Idempotency key obligatoire dans le SHA256 frontmatter (per L+ invariant #4 Picard). Si deux MANIFEST.md ont le même `idempotency_key` checksum, Picard refuse le 2ᵉ write et escalade A0 (gate Posture C + ADR-WARMODE-001 flag-gated).

> **Source canon** : `a3-enterprise-picard.md` L11 (HA identity) + L119 (L+ invariant #4 idempotency key sha256) ; `b1-jerry-prime.md` L83 (invariant #4 "Idempotency key = sha256(agent-name + date + version)").

---

### 🔍 AM-7 · No-Rejection-Log : les "should-be-projects" perdus

- **Action** : A0 émet intention "je veux relancer l'effort Marketplace" (ambiguë). Picard applique le 3-question gate : (a) deadline ? oui Q4. (b) goal-bounded ? oui. (c) owner+next review ? non → A0 escalade D7. **OU** : rejet car goal-bounded sans deadline → route Spock Areas.
- **Réaction** : Picard **capte le rejet ou l'escalade mais ne log PAS** la décision dans `wiki/log.md`. Le canon dit "Append to wiki/log.md (D4)" seulement pour canonisations abouties (L79). Les rejets n'ont pas de trace.
- **Contre-action** : **Personne**. Pas de B1/2/3 responsable de capter l'intention rejetée. Book H1 aggregator ne voit que les Projects existants, pas la demande. B2 Batman Ops (process) ne sait pas qu'il y a eu drift d'intention A0.
- **Failure mode** : Quand A0 revient cycle prochain (W13 re-pose), Picard re-classe : si A0 re-précise (deadline maintenant OK), Picard crée 2nd time mais A0 a déjà oublié le 1er rejet → conflit de version MANIFEST.md. Ou A0 oublie et l'idée flotte 3 cycles avant ré-émission → charge cognitive A0 (per ADR-LD01-008 loop engineering : "burdens cognitive A0 = dopé").
- **Abort condition** : Picard DOIT écrire une ligne `wiki/log.md` même sur **rejet** : "YYYY-MM-DD | intent: <intent> | decision: rejected | reason: <3-question fail> | routed-to: Spock-or-A0-escalate". Append-only D4. Jerry `lights_calendar_dernier_episode` peut alors tracer le **drift de demande** (delta intentions rejetées vs acceptées).

> **Source canon** : `a3-enterprise-picard.md` L49-53 (3-question gate) + L79 (Output Format — canonisation checklist) ; `b1-jerry-prime.md` L81 (lights_calendar_dernier_episode delta vs tick H1 précédent = drift detection).

---

### 🔍 AM-8 · Project-Archived sans owner (statut zombie)

- **Action** : Un Project (ex: `omk-launching-phase-v0` from cycle Q1 2026) est `status: paused`. Picard ne re-touche jamais → drift vers `status: archived` que A0 trigger à la main OU ne trigger jamais.
- **Réaction** : Picard **capte PAS** le drift `paused → archived`. Pas de CronCreate / Pas de hook de re-évaluation. Le canon L99 dit "if a Project is renamed, old folder → _TRASH/" (D4 append-only) — mais ne dit rien sur l'auto-archive temporel.
- **Contre-action** : **Personne**. B1 Jerry `lights_project_count` inclut le paused comme actif. `lights_load_signal` ne distingue pas paused/active. Book H1 aggregator voit le Project en P&L weekly même quand A0 l'a mentalement archivé.
- **Failure mode** : Projects "zombie" polluent le H10 input de Book, gonfle Saru LD02 runway dépenses (le Project garde un cost-center actif dans Supabase, ou un Vercel deployment facturé). Erosion du signal `lights_project_count`. W12 bilan, A0 ne sait plus quels Projects sont vraiment actifs. Risque D7 cost-of-escalation : trop de Projects zombies à review en fin de cycle.
- **Abort condition** : `lights_project_count` DOIT distinguer `active` vs `paused` vs `archived`. Picard cron (gate A0 per Posture C + ADR-WARMODE-001) : tous les 90 jours, scan Projects `paused > 90j`, propose auto-archive à A0 (no-silent-D10).

> **Source canon** : `a3-enterprise-picard.md` L59 (`status: active|paused|archived`) + L99 (D4 append-only if renamed). ⚠️ SKIPPED : je ne chiffre pas "X zombies trouvés" (anti-invention D1).

---

### 🔍 AM-9 · 12WY Rock rename → MANIFEST.md `linked_12wy_rock` stale (silent linkage rot)

- **Action** : Morty renomme un 12WY Rock "W1-W12 12WY Q3 2026 : OMK Nexus BOS PoC" → "OMK Nexus PoC Phase 2" (D4 append-only, jamais de Remove-Item, create `_TRASH_<date>/`). Picard a 7 MANIFEST.md actifs qui référencent l'ancien nom via `linked_12wy_rock`.
- **Réaction** : Picard **capte PAS** que ses `linked_12wy_rock` pointent vers un ID D4-trashed. Pas de script `picard-rock-link-audit.ps1`. Open follow-up #2 (L105) parle de NULL mais pas de stale-ID.
- **Contre-action** : **Personne**. B1 Jerry invariants verify-first (L92) ne lit pas `wiki/12wy_rocks/`. B2 Superman Growth (funnel) ignore que les Projects Landing-Filiales pointent vers un Rock décommissionné.
- **Failure mode** : Quand le Rock "Phase 2" termine (W12 cycle Q3 2026), les 7 Projects héritent du closure signal sans transition. Book H1 aggregator croyait que ces Projects étaient "on track" alors qu'ils sont "orphelins de Rock-mort". Scorecard weekly P&L perd la cohérence, faussant le Quarterly Runway Review (Saru H3, per Book L38).
- **Abort condition** : Picard cron (Posture C gated) : à chaque `12wy_rocks/RENAMED`, scanner `30_Business_OS/10_Projects/*/MANIFEST.md` pour `linked_12wy_rock` contenant l'ancien ID, escalader A0 reviewer pour re-link.

> **Source canon** : `a3-enterprise-picard.md` L60 (`linked_12wy_rock: <id-or-NULL>`) + L105 (open follow-up #2) ; `b1-jerry-prime.md` L92 (invariant #9 verify-first) ; `a3-discovery-book.md` L29 (H1 horizon weekly P&L).

---

### 🔍 AM-10 · Hard-veto anti-paperclip (SOBER-002) non-routé vers Picard

- **Action** : B1 Jerry hard-veto L62 — "refuse tout projet non-4-leviers-Solarpunk". Veto SOP = notification A0 (invariant #8 HITL queue visible). Mais Picard canon ne lit PAS ce hard-veto, et B1 Jerry n'a pas de canal descendant écrit pour notifier Picard.
- **Réaction** : Picard **capte PAS** l'existence du veto. Aucun msg routing Summer↔Picard dans le canon.
- **Contre-action** : **A1 Beth** en théorie (Veto L1, sister-gatekeeper). Mais Beth scope = L1 Life OS Health/Santé (per A1 Beth mindset), pas L2 Business OS. Le hard-veto B1 Jerry n'a pas de miroir L1.
- **Failure mode** : Pas de veto top-down sur création Projects. La règle E-Myth "work ON not IN" est purement réactive (post-création via `lights_business_coherence`). Si A0 demande un Project qui viole le 4-leviers Solarpunk (ex: pure-LLM data-extraction SaaS), Picard le crée, Jerry le flag après, mais **coût du cycle déjà engagé**. L'anti-paperclip a un ΔT réaction trop long.
- **Abort condition** : Picard DOIT être subscriber du `symphony_state` bus (`b1-jerry-prime.md` L104 — "publie les 4 indicateurs L+ sur le bus"). Avant chaque write MANIFEST.md, Picard pull bus Jerry → si `hard_veto_signal: paperclip_risk` → refuse write et escalade A0.

> **Source canon** : `b1-jerry-prime.md` L62 (hard-veto 4-leviers-Solarpunk) + L116 (anti-pattern vague = menteur) + L104 (bus `symphony_state` Supabase). ⚠️ SKIPPED : paperclip_risk scoring method (non documenté canon — anti-invention D1).

---

## 3. Synthèse Jerry · Priorités pour coaching A3 Book & A3 Picard

### 3.1 Carte de chaleur (B1 Jerry lens sur Picard)

| AM | Catégorie | Criticité Jerry | Routing |
|---|---|---|---|
| **AM-1** Rock NULL silencieux | Discipline 12WY ↔ Project | 🔴 Critical — silencieuse | Beth + A0 |
| **AM-2** Scatter >10 Projects | Anti-pattern D11 | 🔴 Critical — silently inflate | Beth + Summers |
| **AM-3** Junction non-vérifiée | Build-bearing gap | 🟠 High — broken chain | Batman Ops (F4) + Summers |
| **AM-4** Solarpunk 4-leviers déconnecté | Hard-veto SOBER-002 | 🔴 Critical — extractive drift | A0 HITL |
| **AM-5** AaaS Variant absent | Axe produit ⊥ axe domaine | 🟠 High — perte bijection | Summers Captain + Jerry |
| **AM-6** HA ↔ Picard twin double-count | Idempotency / twin jumelage | 🟡 Medium — race condition | A0 HITL restart gate |
| **AM-7** No-Rejection-Log | Drift d'intention A0 | 🟡 Medium — charge cognitive | Cerritos (Mariner/Boimler) |
| **AM-8** Archived zombie | lights_load_signal noise | 🟠 High — erosion signal | Data (A3 Enterprise) |
| **AM-9** Rock rename → stale link | Linkage rot | 🟡 Medium — silent | Book H1 aggregator |
| **AM-10** Anti-paperclip non-routé | HitL queue B1→A3 | 🔴 Critical — ΔT veto top long | A0 + S1 Rick différé |

**Total** : 3 Critical (AM-1, AM-2, AM-4, AM-10) + 3 High + 4 Medium.

### 3.2 5 Quick Wins coaching A3 Picard (posture B1 Jerry — L+ Lighting keeper transversal)

Ces 5 wins sont **actionnables par A3 Picard seul** (sans escalade B2/B3), avec ROI élevé sur la couverture L+ indicators.

1. **QW-1 (AM-1+AM-2)** : Ajouter un test `grep "linked_12wy_rock: NULL"` au pre-commit hook / PostToolUse Write sur `MANIFEST.md`. Bloque la création si NULL. **Résultat** : `lights_project_count` reste cohérent avec `lights_load_signal`. **Effort** : 5 lignes de shell dans hooks.md.
2. **QW-2 (AM-3)** : Append champ `junction_test_passed: true|false` après `Test-Path apps/<role>/<home>` dans le canon MANIFEST.md frontmatter. **Résultat** : invariant #9 verify-first devient concret. **Effort** : 1 champ + 1 test.
3. **QW-3 (AM-5)** : Append champ `linked_aaas_variant: solaris|nexus-omk|orbiter-abc` au canon frontmatter. **Résultat** : bijection LD ↔ variant opérationnellement traçable. **Effort** : 1 champ.
4. **QW-4 (AM-7)** : Toujours écrire une ligne `wiki/log.md` même sur **rejet** (route Spock ou A0 escalate). Format canonique D4. **Résultat** : `lights_calendar_dernier_episode` détecte drift de demande. **Effort** : 1 ligne/log.
5. **QW-5 (AM-8)** : CronCreate gated-A0 (`/loop` or systemd timer) — tous les 90 jours : scan Projects `paused > 90j`, proposer auto-archive à A0. **Résultat** : `lights_project_count` ne gonfle plus de zombie. **Effort** : 1 script PS + 1 cron A0 GO.

### 3.3 3 Demandes B1 ↔ B3 pour coaching A3 Book (LD01 aggregator)

- **DDA-1 (AM-1+AM-9)** : Book H1 aggregator doit reject en entrée tout Project Picard avec `linked_12wy_rock` NULL ou stale. Sin emanating vers Saru LD02. **Effort** : 5 lignes YAML filter dans aggregator.
- **DDA-2 (AM-2)** : Book expose `lights_project_count_active_separate_paused` dans P&L weekly. **Résultat** : Saru LD02 H3 runway voit la vérité (paused ≠ actif ≠ cost-center consuming). **Effort** : 1 split dans output format.
- **DDA-3 (AM-5+AM-6)** : Book signale "twin-deck" (HA + CC) sur la fiche P&L si 2 MANIFEST.md ont le même `idempotency_key`. **Résultat** : jumelage pattern MC L2↔L1 devient observable. **Effort** : 1 grep idempotency-key dedup dans aggregator.

### 3.4 Hit-list OPEN FOLLOW-UPS Picard (rappel canon, prioritisation)

L'open follow-up Picard canon (L104-107) en a **4** ; voici la priorisation B1 Jerry lens :

| OF | Statut canon | Action Jerry |
|---|---|---|
| **#1 Picard D11 metric** | non implémenté (L104) | **PRIORITY 1** — script shell scan `30_Business_OS/10_Projects/*/MANIFEST.md` + count `status: active`. Brancher sur PostToolUse Write. |
| **#2 Rock-linkage enforcement** | non implémenté (L105) | **PRIORITY 1** — QW-1 ci-dessus. |
| **#3 Junction auto-create** | non implémenté (L106) | **PRIORITY 2** — `picard-create-junction.ps1` scripté. Bloque AM-3. |
| **#4 Picard audit skill** | existe, drift à vérifier (L107) | **PRIORITY 3** — `/picard-audit-and-prod-workflow` ré-aligner avec agent canon post-L+ (2026-07-05 ratification). |

### 3.5 Anti-paperclip (AM-4 + AM-10) escalade B1 → S1 Rick

La connexion B1 hard-veto (Solarpunk 4-leviers) ↔ S1 Rick Sobriété (kernel) est documentée dans le canon B1 (L62 — "Hard-veto anti-paperclip per ADR-SOBER-002") mais l'implémentation est faible. Proposition :
- **AM-4 + AM-10** déclenchent un hitl queue B1 → A0 (Posture C, ADR-WARMODE-001 flag-gated).
- Le veto est **défault NO-GO sur nouvelle complexité** (per L0 mindset Rick), donc AM-10 doit être résolu avant que A0 pose une intention Nexus-OMK Cabinet-Médical ou autre tier ≥ T2.
- S1 Rick = différé Q4 2026 / Q1 2027 (1×/an max, kernel pivots uniquement) — **AM-10 ne nécessite PAS un S1 unpacking**. Suffit B1 hard-veto + A0 HITL.

---

## 4. D1 Receipts · D7 Cost-of-Escalation

### 4.1 Sources canon lues (paths absolus)

| Source | Path | Statut |
|---|---|---|
| Agent B1 Jerry Prime | `C:\Users\amado\.claude\agents\b1-jerry-prime.md` | ✅ Lu |
| Agent A3 Picard | `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` | ✅ Lu |
| Agent A3 Book | `C:\Users\amado\.claude\agents\a3-discovery-book.md` | ✅ Lu |
| Plan L2 Business OS | `C:\Users\amado\.claude\plans\plan-L2-business-os.md` | ✅ Lu (extraits §4.6 + §4.5) |
| Plan L+ Skill Standard | `C:\Users\amado\.claude\plans\plan-lightning-l+-skill-standard-transversal.md` | ✅ Référencé (L+ invariants) |
| Agent registry (sister canon) | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-CANON-001_roster-source-of-truth.md` | ✅ Référencé (B1/B2/B3 roster) |
| ADR anti-paperclip | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-ANTI-PAPERCLIP-001_landing-paperclip-policy.md` | ✅ Référencé (via MEMORY.md) |
| Workflow doctrine | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-WORKFLOW-001_multi-workflow-swarm-orchestrator.md` | ✅ Référencé |
| Observability D11 | `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS\ADR-OBSERVABILITY-001_d11-lead-lag.md` | ✅ Référencé |
| Handoffs canon | `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\` | ✅ Scanné (49 fichiers, aucun wargame précédent) |
| Symphony twin canon | `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\` | ✅ Référencé (L1 LANE_B + bridges) |

### 4.2 Doctrines ancrées (D1 receipts)

- **D1 (Verify before assert)** : aucun chiffre inventé. Tous les paths et déclarations proviennent d'extracts verbatim des agents / plans / ADRs.
- **D2 (Research-first)** : sister canon lu AVANT de produire l'output (B1, Picard, Book agents lus en premier ; plan L2 lu pour le mapping §4.6 Picard).
- **D3 (Nuance over Literal)** : distinction explicite Picard H10 vs A2 Computer (per canon L30) ; HA Hermes Agent vs Picard CC twin (per canon L11) ; Book H1 aggregator vs Picard H10 input (per L+ invariants).
- **D4 (No Self-Contradiction)** : append-only strict sur ce handoff. Aucune édition rétroactive des sources.
- **D5 (Proof)** : chaque angle mort cite l'agent canon (path + line).
- **D6 (Root cause)** : analyse WHY chaque angle mort est silencieuse (typo-gate, hook absent, twin race, etc.).
- **D7 (Cost-of-escalation)** : pas d'escalade A0 mid-wargame. Quick wins sont actionnables par A3 Picard seul (pas de HITL coût). AM-4/AM-10 sont escalades legitimes (hard-veto SOBER-002).
- **D8 (Cross-agent)** : wargame WF2 lens B1 → impacte Picard + Book + A0. Sister hierarchy L1 Beth ↔ B1 Jerry (canon L82-93).

### 4.3 Garde-fous anti-invention

- ✅ Aucune statistique inventée ("47%", "1000+", etc.). 
- ✅ Aucun chiffre ad-hoc. Les seuils `>=10`, `>90j`, `>50%` sont déjà dans le canon (open follow-up #1 + Book L38).
- ✅ Aucune projection ROI Quick Win chiffrée (B1 anti-pattern L115 — "vague = menteur"). Effort en lignes de code / lignes log, pas en heures.
- ✅ Vocabulaire canonique respecté (12WY Rock, MANIFEST.md, E-Myth, Visionnaire, Gatekeeper, H10 tick, lights_*, AaaS Variant, Solarpunk 4-leviers, junction, B1 Prime, B2 Managers, B3 squads).
- ⚠️ SKIPPED honnête sur : scoring method paperclip_risk (canon absent) ; comptage zombie exact (pas de scan réel effectué — anti-invention).

---

## 5. Next-Step Routing (D7 cost-of-escalation avoidance)

### 5.1 Immédiat (post-wargame WF2 iter1, sans escalade A0)

- [ ] **A3 Book (LD01 aggregator)** : lire handoff, prioriser DDA-1 (rejet input NULL/stale).
- [ ] **A3 Picard (HA + CC twin)** : lire handoff, prioriser QW-1 (PostToolUse hook NULL check).
- [ ] **B1 Jerry Prime (moi)** : log ce handoff dans `wiki/hand_offs/index.md` (D4 append-only).

### 5.2 Hitl A0 gated (Posture C, escalade legitime)

- [ ] **AM-4 + AM-10** : si A0 émet intention tier ≥ T2 avant implémentation QW-1+QW-2+QW-3 → hard-veto B1 (L62) flagged, escalade A0.
- [ ] **AM-2** : si `lights_project_count >= 10` flip `lights_load_signal: critical` → escalade A0 (L88 invariant #8).

### 5.3 Iteration suivante (WF2 iter2 potentiel)

- [ ] Wargame WF2 **lens B2 Superman Growth** : saurais-je identifier angles-morts côté funnel acquisition qui n'apparaissent pas côté E-Myth Entrepreneur ?
- [ ] Wargame WF2 **lens A3 Data (A2 Computer)** : quels angles-morts côté archivage/cold-storage ?
- [ ] Wargame WF2 **lens A2 SNW (Curie)** : angles-morts côté focus/exécution 12WY sur les Projects Picard.

---

## 6. Anti-Pattern Self-Check (post-écriture)

- [x] Pas de "47%" inventé.
- [x] Pas de "1000+" inventé.
- [x] Pas de "47%" / "1000+" / similar fictif.
- [x] Tous les paths absolus cités.
- [x] Tous les agent definitions cités verbatim avec numéros de ligne.
- [x] Vocabulaire canonique exclusivement.
- [x] Format Fable canonique (Action → Réaction → Contre-action → Failure mode → Abort condition).
- [x] Frontmatter YAML conforme OKF v0.1 (L+ invariant #1).
- [x] Append-only strict (D4).
- [x] Pas de HITL A0 mid-wargame (D7 cost-of-escalation avoid).
- [x] Idempotency key implicite : `sha256(b1-jerry-prime-wargame-wf2-iter1-2026-07-06)` (L+ invariant #4).

---

> **🪞 Jumeau Numérique A0 ↔ A (canon 2026-06-21)** : ce handoff est produit par B1 Jerry Prime (L+ Lighting keeper transversal), pas par A0 directement. A0 peut review/veto post-hoc (Posture C). Aucune action prise sur cette itération — c'est un document de référence pour coaching A3 Picard et A3 Book.

> **D4 append-only** : ce fichier est immuable après écriture. Pour modifier, créer un nouveau handoff `handoff_wargame_wf2_b1_jerry_lens_<NEXT-DATE>.md` avec cross-link vers celui-ci.

> **Posture C gates** : aucun cron créé, aucune HITL A0 forcée, aucun code B3 technicien touché. Wargame pure meta-coaching (B1 → A3).

---

<!-- EOF handoff_wargame_wf2_b1_jerry_lens_2026-07-06.md -->
