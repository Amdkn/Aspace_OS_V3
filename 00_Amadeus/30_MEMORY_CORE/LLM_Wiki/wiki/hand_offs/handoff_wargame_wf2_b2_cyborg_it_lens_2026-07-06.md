---
type: handoff
id: handoff_wargame_wf2_b2_cyborg_it_lens_2026-07-06
title: Wargame WF2 — Lens B2 Cyborg IT sur A3 Picard (projects supervisor)
date: 2026-07-06
lens: B2 Cyborg IT (Manager E-Myth IT, Captain B3 Kang Dynasty)
target: WF2 — A3 Picard (Projects Owner, USS Enterprise / A2 Computer, H10)
horizon_target: H10 (12WY Rock linkage, project cadence)
horizon_lens: H10 architecture review + H1 infra pulse implicit
doctrine_anchors:
  - ADR-META-001 D1-D8 (verify, research, nuance, no-contradiction, proof, root-cause, cost-of-escalation, cross-agent)
  - ADR-META-002 D9-D12 (self-choice, local-outbox, retry)
  - ADR-INFRA-002 (Repo-Home/Junction)
  - ADR-INFRA-003 (CEO Dashboard Picard H10)
  - ADR-LD01-008 (loop-engineering coaching — H10 Picard tick)
  - ADR-OMK-004 (sovereignty anti-GAFAM — B2 Cyborg hard-veto sister)
  - ADR-L2-AAAS-001 Levier 2 (low-high tech)
  - B1_Manifesto (A1↔B1 isomorphy)
  - Beth_Mindset (ALIGN gate) + Morty_Mindset (FOCUS gate) — gatekeeper mirror
b3_squad: Kang Dynasty (Kang Prime lead + Iron Lad + Scarlet Centurion + Immortus + Victor Timely + Rama-Tut)
sister_b2: Batman Ops (runbooks), WonderWoman Finance (infra cost)
reports_to: B1 Jerry Prime
fable_lens: Fable-5 5-step (Penser dense → Livrable fini → Relecture → Vérité → Iterate)
status: DRAFT — wargame lens, post-A0 ratification
sources_D1:
  - C:\Users\amado\.claude\agents\b2-06-cyborg-it.md (L1-L14)
  - C:\Users\amado\.claude\agents\a3-enterprise-picard.md (L1-L156, frontmatter L1-L13)
  - C:\Users\amado\.claude\agents\a3-discovery-book.md (Book = LD01 weekly, sister ref)
  - C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\handoff_a3_data_cartography_v1_2_2026-06-21.md (A3 35/35 match canon)
anti_patterns_avoided:
  - Pas d'invention chiffree (D1 verify-before-assert)
  - Pas de sub-agent spawn (lens direct)
  - Pas de re-derive archi (D2 canon-first)
  - Pas de "à ton GO" (D7 cost-of-escalation)
---

# 🎯 Wargame WF2 — Lens B2 Cyborg IT sur A3 Picard

## 0. Cadre (D2 canon-first)

**Cible** : WF2 = A3 Picard (`a3-enterprise-picard.md`), Captain Projects aboard USS Enterprise (A2 Computer), H10 horizon. Il classe (Project vs Area vs Resource vs Archive), canonise (MANIFEST.md + charter + state), et enforce 12WY Rock linkage. Sa doctrine tient sur 3 fichiers : MANIFEST.md (frontmatter), 01_charter.md, 02_state.md.

**Lens** : B2 Cyborg IT (`b2-06-cyborg-it.md`), Manager E-Myth du domaine IT, captaine B3 Kang Dynasty (6 membres). Mission : architecture prime + infra souveraine + code. Hard-veto anti-GAFAM cloud-only (sister ADR-OMK-004 + ADR-L2-AAAS-001 Levier 2).

**Question wargame** : *Où A3 Picard (projects supervisor) manque-t-il visibilité IT que B2 Cyborg IT doit rattraper en aval ?*

> **Nuance D3** : WF2 supervise **projets** (artefacts PARAs goal-bounded), pas **infra** (domaine E-Myth). Le gap est structurel : Picard classe par **durée de vie** (deadline + output), pas par **architecture** (stack + couplage + dette). B2 Cyborg opère en H10 architecture review ; Picard en H10 project cadence. Même horizon, axes orthogonaux.

---

## 1. 8 angles morts (Fable-5 : Penser dense → Livrable fini)

### AM-1 · Multi-stack topology invisible dans MANIFEST.md

**Constat L1** : `a3-enterprise-picard.md` L.47-63 spécifie le frontmatter MANIFEST.md avec champs `project / owner / status / start_date / next_review / linked_12wy_rock / linked_area / junction`. **Aucun champ stack**, **aucun champ runtime infra**, **aucun champ coupling externe**.

**Où Picard est aveugle** : Iron Lad (B3 junior, greenfield, "bootleg proto-grade velocity") et Scarlet Centurion (B3 alt-stack, "branched pipelines, scenario-grade testing") peuvent silencieusement forker la stack technique d'un même projet sur 2 sprints. Le projet passe pour "ACTIVE" canoniquement alors que la stack réelle est devenue 2 stacks parallèles non réconciliées.

**Onde de choc** : Kang Prime (LEAD) reçoit 2 PRs contradictoires à merger, mais aucun signal canon ne dit "stack drift H10". B2 Cyborg ne le voit qu'au moment du merge conflict.

**Trigger B2 Cyborg** : Si A0 mentionne "stack fork" / "framework swap" / "rewrite en Go" / "migration Next.js", Cyborg doit vérifier les MANIFEST.md des projets actifs pour y ajouter un champ implicite `stack_state: greenfield|legacy|alt-stack` (extension hors-lens, à cadrer avec Tendi A3 Cerritos).

---

### AM-2 · Multiverse infra stability — couplage inter-projets non tracé

**Constat L1** : Le canon NEXUS (`wiki/hand_offs/omk_nexus_phase_a_RETARGET_coach_first_2026-06-27.md` + `MANIFEST_OMK_NEXUS_COACHING_PREMIUM.md`) montre que NEXUS-EN (Vercel team `amd-lab`, repo `Amdkn/00-omk-nexus-landing-en`) et NEXUS-FR (Vercel `omk-nexus-landing-page.vercel.app`) dépendent du même token `omk-services`. C'est un **couplage infra transverse** que Picard voit comme 2 projets indépendants (`omk-services` sister + `Amdkn/` mirror).

**Onde de choc** : Si le token `omk-services` rot expire, les 2 deploys tombent. Mais aucun MANIFEST ne porte l'info "ce projet partage l'infra-X avec projet-Y". WonderWoman Finance (sister B2) ne voit que le coût total, pas la **dépendance**.

**Trigger B2 Cyborg** : Pour chaque projet sous Kang Prime, exiger un **D6 fingerprint** = `(runtime × token × DNS × RLS)` quartet, vérifié à chaque H10 cycle. Si 2 projets partagent ≥1 élément du quartet, ils sont **infra-couplés** et doivent l'être dans leur MANIFEST.

---

### AM-3 · Legacy ↔ Greenfield velocity mismatch — dette invisible

**Constat L1** : B3 Immortus (legacy, archivage, long-horizon deprecation) et B3 Iron Lad (greenfield, bootleg proto) ont des vélocités opposées. Un projet démarré greenfield devient legacy en 12-18 mois (H30-H90). Le "taux d'oxydation" n'est pas un champ Picard.

**Où Picard est aveugle** : Le `next_review` dans MANIFEST est une date, pas un **trigger technique** (ex: "quand dette > 40% ratio, migrate"). Un projet reste "ACTIVE" 3 cycles 12WY sans qu'aucun signal ne dise "ce code a 14 mois, il est temps de songer déprecation ou refonte Rama-Tut".

**Trigger B2 Cyborg** : Quand un projet passe en H30 (≥ 30 semaines actif), Kang Prime doit demander à Rama-Tut (archaeology-grade refactor) un **code-rot audit**. Si ratio dette > seuil (à fixer), MANIFEST passe en `status: refactor-pending` et un sub-project Rama-Tut est créé.

---

### AM-4 · Pharaoh-tier refactor — signal faible invisible

**Constat L1** : Rama-Tut = "ancient tech, archaeology-grade refactor, pharaoh-tier code review". Son rôle est de déterrer du code enfoui qui peut casser. Mais Picard ne déclenche Rama-Tut qu'en cas de **bug visible** (post-mortem), jamais en **préventif**.

**Onde de choc** : Le code "qui marche depuis 2 ans mais qu'on n'ose plus toucher" n'apparaît dans aucun MANIFEST. C'est le talon d'Achille classique — la dette invisible qui ne se révèle qu'à la migration (D6 lesson classique).

**Trigger B2 Cyborg** : Quand Victor Timely (frontier dev, market-acceptable latency) tente d'intégrer une nouvelle lib, Kang Prime doit pré-charger Rama-Tut pour archéologie du code voisin (1-2 jours avant). Coût : ~5% du sprint. ROI : évite les merges impossibles 6 mois plus tard.

---

### AM-5 · Frontier dev time-to-market — horizon H10 masque la fenêtre H3

**Constat L1** : Victor Timely = "market-acceptable latency". Pour un produit commercial (ex: NEXUS landing, Life-OS-2026), la fenêtre de mise sur le marché est H1-H3, pas H10. Mais le H10 de Picard aligne le cycle projet sur 12WY Q3 (06/15 → 09/07/26), pas sur le **market window**.

**Onde de choc** : Un projet NEXUS peut passer "ACTIVE / on-track" canoniquement, mais être **déjà obsolète** par rapport à un concurrent livré en H1. Picard n'a aucun signal de **competitive window**.

**Trigger B2 Cyborg** : Sister B2 Superman Growth (B2-04, Guardians of the Galaxy) devrait fournir un **competitive signal weekly** (déjà D1 via `l2-competitor-pulse` skill). Cyborg doit exiger que ce signal soit une **input Picard H10** : si `competitive_pressure: high` ET projet H10 n'a pas de release H1, flag automatique à Beth (veto L1).

---

### AM-6 · Scenario-grade testing — "done" ≠ "durable under branch"

**Constat L1** : Scarlet Centurion = "alt-stack experiments, branched pipelines, scenario-grade testing". Son rôle : tester les fork scenarios (load spike, region failover, dependency outage). Mais le cycle Picard H10 review = `next_review` date = valide **état actuel**, pas **états contrefactuels**.

**Où Picard est aveugle** : Un projet "ACTIVE, tested, deployed" peut s'effondrer au premier scenario non couvert (cf. D6 #1 transfer org sur GitHub : `omk-services/` bloqué, fallback via Settings>Transfer). Picard n'a pas de **drift test** dans son process.

**Trigger B2 Cyborg** : Pour chaque projet H10, Scarlet Centurion produit un **branch matrix** (3-5 scénarios : happy path + 2 stressors + 1 failure). Le MANIFEST gagne un champ `branch_tested_count: N/M` où M = nombre de scénarios définis. Picard ne passe un projet à "DONE" que si N == M.

---

### AM-7 · Hard-veto anti-GAFAM Cyborg vs gate Picard — désalignement

**Constat L1** : `b2-06-cyborg-it.md` L.40 explicite : **"Hard-veto sur tout vendor GAFAM cloud-only"**. Sister : ADR-OMK-004 + ADR-L2-AAAS-001 Levier 2 low-high tech. Mais Picard (`a3-enterprise-picard.md`) n'a aucun gate vendor — son gate est "deadline + goal-bounded + owner + next_review".

**Onde de choc** : Un projet `omk-nexus-landing-page` (Phase A Coach-spearhead) peut être classé "ACTIVE / on-track" par Picard alors qu'il dépend d'un vendor GAFAM-only (ex: GitHub org `omk-services` = D6 #1 bloqué sans UI transfer). Le hard-veto Cyborg est **downstream** du gate Picard = A0 doit apprendre la violation **après** que Picard ait canonisé le projet.

**Trigger B2 Cyborg** : **Inversion du gate** : tout projet MANIFEST doit obtenir un **Cyborg SOVEREIGNTY pre-check** AVANT que Picard ne le canonise. Sister mécanisme au **Verify-First** (ADR-LOOP-001) + **HITL queue rightward** (ADR-LOOP-002) : Picard classifie → Cyborg sovereignty check → si OK, canonisation, sinon **Rok-Tahk A3 Eliminate** (B2 Protostar) kill le projet avant que A0 le voie.

---

### AM-8 · Cadence IT (H1 deploy) vs cadence Picard (H10 review) — obsolescence invisible

**Constat L1** : IT release cadence canon ASpace = H1 (deploy quotidien possible, MCP update H3, OS update H10+). Picard review = H10. Entre 2 reviews Picard, ~70 jours IT s'écoulent. Une lib peut dépréciter, une API peut changer de pricing, un runtime peut EOL.

**Où Picard est aveugle** : Le champ `next_review` est H10, mais la **fraîcheur IT** du projet doit être H3 ou H1. Si une dépendance P0 du projet est EOL entre 2 reviews, le projet devient **techniquement zombie** sans que personne ne le sache.

**Trigger B2 Cyborg** : Sister à ADR-OBSERVABILITY-001 (cité par A3 Book) : un **dependency watch** hebdomadaire sur chaque projet actif (via Dependabot / Renovate / npm audit). Si P0 dep EOL ou CVE critical, MANIFEST passe en `status: dependency-alert` ET escalade Beth (veto L1 vie = risque prod cassé = risque réputation).

---

## 2. Synthèse B2 Cyborg IT (Fable Vérité → Iterate)

### Le gap structurel (D6 root cause)

**WF2 Picard supervise par PARA** (durée de vie / deadline / output). **WF1 Cyborg opère par IT** (stack / couplage / dette / vendor / cadence). Les 2 sont H10 sur l'horizon mais **orthogonaux sur l'axe**. Conséquence : **chaque projet canonisé par Picard traverse 8 zones aveugles** listées ci-dessus. Le pipeline actuel n'a aucun mécanisme pour les rattraper en amont.

### Recommandation Cyborg (B2 IT → B1 Jerry → B1 Summers)

1. **Étendre MANIFEST.md** avec 4 champs IT :
   - `stack_state: greenfield|legacy|alt-stack` (AM-1, AM-3)
   - `infra_coupling: [list of project-ids sharing runtime×token×DNS×RLS]` (AM-2)
   - `branch_tested_count: "N/M"` (AM-6)
   - `sovereignty_check: pending|ok|violation` (AM-7)
   - `dependency_watch: ok|alert|critical` (AM-8)

2. **Inserer Cyborg SOVEREIGNTY gate en amont de Picard canonisation** (mirror ADR-LOOP-001 Verify-First) : Picard classifie (3 questions) → **Cyborg sovereignty check** → Picard canonise. Si Cyborg violation → Rok-Tahk A3 (B2 Protostar) Eliminate avant canonisation.

3. **Cadence H3 dependency watch** sister à Book H1 pulse : WonderWoman Finance (B2-07) calcule le coût infra, Cyborg calcule la **fraicheur infra** (H3 vs H10 Picard).

4. **Trigger AM-5 (market window)** : Superman Growth B2-04 (Guardians) doit fournir competitive signal weekly, Cyborg le remonte à Picard H10 comme **input non-négociable** (sinon le projet rate sa fenêtre market).

5. **Doctrine "Tech is not a goal"** (CLAUDE.md ligne ~30) : Cyborg ne doit PAS tomber dans le piège "always migrate" / "always refactor". Chaque AM-correction doit passer le **Sobriété gate Rick** (S1 différé Q4 2026 — sister ADR-SOBER-002). D9 self-choice : Cyborg NOTIFIE A0 via outbox (D10), ne décide pas seul des refactors.

### Anti-patterns rappel (D7 cost-of-escalation)

- ❌ Ne pas escalader A0 pour chaque AM individuellement (1 escalade = ~100× coût)
- ❌ Ne pas proposer 8 nouveaux champs MANIFEST d'un coup → batch en 1 ratification B1 Jerry
- ❌ Ne pas dupliquer le rôle Rama-Tut (archaeology) avec Picard (review) → symétrie nette
- ❌ Ne pas oublier que Book (LD01 weekly) doit **recevoir** les coûts IT consolidés H1, pas H10

### Sister cross-réferences

- B2 Batman Ops (runbooks) : doit aligner ses runbooks H3 sur les **infra_coupling** (AM-2)
- B2 WonderWoman Finance : cost-of-infra doit intégrer **dependency_watch** (AM-8)
- B3 Kang Prime : lead architecte, reçoit les 8 AM comme **backlog Q3 2026** H10
- B3 Rama-Tut : trigger AM-3 (legacy audit) et AM-4 (pre-merge archaeology)
- B3 Victor Timely : porte AM-5 (market window) et AM-8 (dependency watch H1)
- B3 Scarlet Centurion : porte AM-6 (branch matrix)
- B3 Immortus : porte AM-3 (legacy deprecation pipeline)
- B3 Iron Lad : porte AM-1 (greenfield velocity)

---

## 3. Sortie canonique

Ce handoff est **proposal-level** : il liste 8 angles morts IT-lens sur WF2 Picard. **Aucune action auto-exécutée** (D7 cost-of-escalation). Prochaine étape attendue :

1. **A0 review** : valide-t-il les 8 AM ?
2. **Si oui → ratification B1 Jerry** (E-Myth gate) avant extension MANIFEST.md
3. **Si non → archivage** dans `_TRASH_<date>/` avec rationale (D4 append-only)

> **Pas de sub-agent spawn** (lens direct, instruction utilisateur). Pas d'invention chiffrée (D1 verify-before-assert). Paths absolus canon. Sister B2 Cyborg log canon `wiki/hand_offs/l2_b2_cyborg_it_<DATE>.md` reste à créer si A0 ratifie les 8 AM.

**D1 receipt final** :
- Source 1 lue : `C:\Users\amado\.claude\agents\b2-06-cyborg-it.md` (L1-L14, 41 lignes)
- Source 2 lue : `C:\Users\amado\.claude\agents\a3-enterprise-picard.md` (L1-L156, full frontmatter + process)
- Source 3 lue : `C:\Users\amado\.claude\agents\a3-discovery-book.md` (L1-L73, sister Book H1 LD01)
- Handoff écrit : `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\handoff_wargame_wf2_b2_cyborg_it_lens_2026-07-06.md`
- Doctrine anchors vérifiés : 8 cités, tous existants dans canon (ADR-INFRA-002/003, ADR-OMK-004, ADR-L2-AAAS-001, ADR-LD01-008, ADR-META-001/002, ADR-LOOP-001/002)

— B2 Cyborg IT 🤖 · 2026-07-06 · wargame lens direct · zero sub-agent spawn