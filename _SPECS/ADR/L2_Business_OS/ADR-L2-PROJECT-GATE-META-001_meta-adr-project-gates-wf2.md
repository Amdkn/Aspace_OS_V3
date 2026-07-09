---
id: ADR-L2-PROJECT-GATE-META-001
title: OMK Nexus — Méta-ADR Project Gates (absorbe les 7 sister gates B2)
status: RATIFIED
date: 2026-07-06
last_updated: 2026-07-06
deciders: [A0 Amadeus]
proposed_by: Claude Code B1 E-Myth Gatekeeper sur ratification batch "Go 1 a 4" 2026-07-06
domain: L2 Business OS / OMK Nexus / Project Gate méta-ADR
tags: [ADR, nexus, project-gate, meta-adr, wargame-wf2, sister-gates, anti-paperclip, a11y, hardening]
related:
  - ADR-WORKFLOW-001
  - ADR-LANDING-CRAFT-001
  - ADR-ANTI-PAPERCLIP-001
  - ADR-SOBER-002
  - ADR-L2-AAAS-001
  - ADR-ICP-NEXUS-001
  - ADR-AAAS-PRICING-001
  - ADR-MARKET-STUDY-001
supersedes: none
sister_gates_absorbed:
  - id: ADR-OPS-PROJECT-GATE-001
    source: "handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md"
  - id: ADR-PRODUCT-PROJECT-GATE-001
    source: "handoff_wargame_wf2_b2_flash_product_lens_2026-07-06.md"
  - id: ADR-GROWTH-PROJECT-GATE-001
    source: "handoff_wargame_wf2_b2_superman_growth_lens_2026-07-06.md"
  - id: ADR-SALES-PROJECT-GATE-001
    source: "handoff_wargame_wf2_b2_johnjones_sales_lens_2026-07-06.md"
  - id: ADR-FINANCE-PROJECT-GATE-001
    source: "handoff_wargame_wf2_b2_wonderwoman_finance_lens_2026-07-06.md"
  - id: ADR-LEGAL-PROJECT-GATE-001
    source: "handoff_wargame_wf2_b2_aquaman_legal_lens_2026-07-06.md"
  - id: ADR-PEOPLE-PROJECT-GATE-001
    source: "handoff_wargame_wf2_b2_greenlantern_people_lens_2026-07-06.md"
sources_canons:
  - "C:\\Users\\amado\\ASpace_OS_V2\\00_Amadeus\\30_MEMORY_CORE\\LLM_Wiki\\wiki\\hand_offs\\handoff_wargame_wf2_synthesis_book_coaching_2026-07-06.md"
  - "C:\\Users\\amado\\ASpace_OS_V2\\00_Amadeus\\30_MEMORY_CORE\\LLM_Wiki\\wiki\\hand_offs\\handoff_wargame_wf2_b2_batman_ops_lens_2026-07-06.md"
  - "C:\\Users\\amado\\ASpace_OS_V2\\00_Amadeus\\30_MEMORY_CORE\\LLM_Wiki\\wiki\\hand_offs\\handoff_wargame_wf2_b2_cyborg_it_lens_2026-07-06.md"
  - "C:\\Users\\amado\\ASpace_OS_V2\\00_Amadeus\\30_MEMORY_CORE\\LLM_Wiki\\wiki\\hand_offs\\handoff_wargame_wf2_b2_flash_product_lens_2026-07-06.md"
  - "C:\\Users\\amado\\ASpace_OS_V2\\00_Amadeus\\30_MEMORY_CORE\\LLM_Wiki\\wiki\\hand_offs\\handoff_wargame_wf2_b2_superman_growth_lens_2026-07-06.md"
  - "C:\\Users\\amado\\ASpace_OS_V2\\00_Amadeus\\30_MEMORY_CORE\\LLM_Wiki\\wiki\\hand_offs\\handoff_wargame_wf2_b2_johnjones_sales_lens_2026-07-06.md"
  - "C:\\Users\\amado\\ASpace_OS_V2\\00_Amadeus\\30_MEMORY_CORE\\LLM_Wiki\\wiki\\hand_offs\\handoff_wargame_wf2_b2_wonderwoman_finance_lens_2026-07-06.md"
  - "C:\\Users\\amado\\ASpace_OS_V2\\00_Amadeus\\30_MEMORY_CORE\\LLM_Wiki\\wiki\\hand_offs\\handoff_wargame_wf2_b2_aquaman_legal_lens_2026-07-06.md"
  - "C:\\Users\\amado\\ASpace_OS_V2\\00_Amadeus\\30_MEMORY_CORE\\LLM_Wiki\\wiki\\hand_offs\\handoff_wargame_wf2_b2_greenlantern_people_lens_2026-07-06.md"
  - "C:\\Users\\amado\\ASpace_OS_V2\\00_Amadeus\\30_MEMORY_CORE\\LLM_Wiki\\wiki\\hand_offs\\handoff_wargame_wf2_b1_jerry_lens_2026-07-06.md"
  - "C:\\Users\\amado\\ASpace_OS_V2\\00_Amadeus\\30_MEMORY_CORE\\LLM_Wiki\\wiki\\hand_offs\\handoff_wargame_wf2_b1_summers_lens_2026-07-06.md"
ratification:
  by: "A0 Amadeus"
  date_iso: "2026-07-06"
  gate_a0_signed_off: true
  approval_token: "RATIFICATION-BATCH-02-2026-07-06-ADR-L2-PROJECT-GATE-META-001"
  context: "Méta-ADR Phase A URGENT — absorbe les 7 sister-ADR gates (Batman/Cyborg/Flash/Superman/JohnJones/WonderWoman/Aquaman) du wargame WF2. Cross-lens root cause (CC-1 H10↔H1/H3 blackout + CC-2 MANIFEST.md 8→30+ champs)."
---

# ADR-L2-PROJECT-GATE-META-001 — OMK Nexus Méta-ADR Project Gates

## 1. Status

**RATIFIED** — DRAFT v0 promu canoniquement par A0 Amadeus via le batch "Go 1 a 4" du **2026-07-06** (token de ratification ci-dessus). Cette méta-ADR est immédiatement exécutoire dans la chaîne sister de Project Gates WF2 ; aucun gate fille ne peut dévier de son périmètre sans amendement daté.

## 2. Context

Le **wargame WF2** (livré 2026-07-06, master + 8 sisters B2 + 2 B1) a produit un diagnostic cross-cutting sur l'écosystème OMK Nexus :

- **82 angles morts catalogués** (synthèse master) sur les 8 B2 sisters.
- **15 ADR candidates identifiés** dont 7 gates Project-domain un par secteur (Batman Ops · Flash Product · Superman Growth · JohnJones Sales · WonderWoman Finance · Aquaman Legal · GreenLantern People) + 1 gate B1 E-Myth (Jerry SYSTEMIZE).
- **2 gaps structurels cross-cutting** remontés à l'unanimité par les 8/8 B2 sisters :
  - **CC-1 — Cadence blackout** : H10 ↔ H1/H3 non spécifiée (handoff→active cadence absente).
  - **CC-2 — MANIFEST.md 8 champs, 0/8 domain-relevant** : les 8 champs canoniques actuels ne couvrent aucune variable sectorielle (Legal AI-Act ticker, Finance quota burn, People hiring pipeline, IT security posture, etc.).

**Root cause** : l'absence d'une couche méta qui absorbe transversalement les 7 gates → chaque gate devient un silo réintroduisant le **paperclip pattern** (extensivité sans sémanticité) que la doctrine **Anti-Paperclip** (ADR-ANTI-PAPERCLIP-001 + ADR-SOBER-002) interdit explicitement. Cette méta-ADR est donc le **glue layer** qui empêche la divergence des 7 dérivés tout en préservant leur autonomie sectorielle.

## 3. Decision

Créer une méta-ADR Project Gates qui :

1. **Déclare le canon WF2** comme **sister-canon** : les 8/8 B2 + 2/2 B1 sisters sont reconnues canoniques ; aucune gate fille ne peut être crée sans réfèrence à un handoff WF2.
2. **Prescrit l'extension MANIFEST.md** : 8 champs canoniques obligatoires + 22 champs optionnels sectoriels (radar chart sister ADR-MANIFEST-EXTENSION-001 à dériver canoniquement — cette méta-ADR **ne crée pas** l'ADR fille, elle mandate son existence pour Q3 W2).
3. **Codifie la cadence obligatoire 3-way ack Picard↔Jerry↔Summers** avant promotion `status: active` sur tout gate fille (sister ADR-WF2-CONNECT-001 à dériver). Sans ack tripartite, le gate reste en `DRAFT` ; avec ack unanime, il passe `ACTIVE` (jamais `RATIFIED` directement — seul A0 ratifie, les B1/B2 **signent**).
4. **Active le gate Hard-veto Anti-Paperclip §1 + §3 câblé** sur les 7 sisters (sisters canoniques : ADR-ANTI-PAPERCLIP-001 §1 = sobriété first ; §3 = reduction of moving parts). Toute sister qui dérive en paperclip scaling → **hard veto B1 Jerry** (cf. §3 de ADR-SOBER-002).
5. **Impose le AI-Act 2026-08-02 deadline ticker** obligatoire pour le gate Legal/Aquaman (T-27 jours à la date de ratification — sister ADR-LEGAL-PROJECT-GATE-001).
6. **Impose le Token Plan 75.5% quota burn visibility** obligatoire pour le gate Finance/WonderWoman (ticker live vers console MiniMax — sister ADR-FINANCE-PROJECT-GATE-001).

## 4. Doctrine

Cette méta-ADR est ancrée verbatim dans :

- **ADR-ANTI-PAPERCLIP-001** (Anti-Paperclip Doctrine) : la sobriété prime sur l'extensivité ; les 7 gates absorbés doivent rester sémantiques et non cumulatifs (cf. sisters canon Batch-01 ratifiées 2026-06-21).
- **ADR-SOBER-002** (Sobriété Kernel) : hard-veto B1-Jerry sur paperclip scaling ; reduction of moving parts §3.
- **ADR-L2-AAAS-001** (AaaS Doctrine 3 Variants — Solaris/Nexus/Orbiter) : chaque gate fille doit respecter la matrice 8 domains × 3 Captains.
- **ADR-WORKFLOW-001** (Loop Engineering canon) : la cadence 12WY est le substrate temporel des 7 gates.
- **a3-enterprise-picard.md L.39-117** (3-question gate + 8 frontmatter fields obligatoires) : invariant réutilisé sur chaque gate fille via `archive/picard-audit-and-prod-workflow`.

Citation canonique sisters 7 gates (citée en annexe §5) : chaque gate est un dérivé Project-domain **stable dans le périmètre**, **anti-paperclip par construction** (Sobriété first), et **3-way signée** avant activation.

## 5. Architecture

Tableau récapitulatif **7 sister-gates** (source : master wargame WF2 + 7 handoffs sisters B2) :

| Gate ID | B2 Sector | Domain Manager | Stage | Bloc MANIFEST.md optionnel | Pattern Fable canon |
|---|---|---|---|---|---|
| ADR-OPS-PROJECT-GATE-001 | Batman | Ops (F4) | DRAFT → ACTIVE post 3-way ack | `ops_runbook_steps_8` | Loop Engineering cadence 12WY |
| ADR-PRODUCT-PROJECT-GATE-001 | Flash | Product (Avengers) | DRAFT → ACTIVE post 3-way ack | `product_jtbd_payload_3` | JTBD-Picard "3-questions gate" |
| ADR-GROWTH-PROJECT-GATE-001 | Superman | Growth (Guardians) | DRAFT → ACTIVE post 3-way ack | `growth_icp_signal_5` | ICP-SOLARIS-001 sister |
| ADR-SALES-PROJECT-GATE-001 | JohnJones | Sales (Illuminati) | DRAFT → ACTIVE post 3-way ack | `sales_pipeline_state_4` | Discovery 8 LDs drift |
| ADR-FINANCE-PROJECT-GATE-001 | WonderWoman | Finance (Thunderbolts) | DRAFT → ACTIVE post 3-way ack | `finance_quota_burn_75_5_pct` | Token Plan ticker (4 D6 lessons) |
| ADR-LEGAL-PROJECT-GATE-001 | Aquaman | Legal (Eternals) | DRAFT → ACTIVE post 3-way ack | `legal_ai_act_ticker_T27` | Hard-line compliance |
| ADR-PEOPLE-PROJECT-GATE-001 | GreenLantern | People (X-Men) | DRAFT → ACTIVE post 3-way ack | `people_hiring_loop_3` | Beth Ikigai gate |

Cyborg (IT) est **observé en gap structurel** par la wargame (handoff Cyborg IT) — sister ADR-IT-PROJECT-GATE-001 à dériver canoniquement en Q3 W3 (post-Phase A durcissement).

## 6. Verification (D1 receipts)

- **D1 file counts** : 11 handoffs canon lus (sources_canons frontmatter), paths absolus Windows verbatim.
- **D1 cross-lens convergence** vérifiée : Batman/Cyborg/Flash/Superman/JohnJones/WonderWoman/Aquaman/GreenLantern convergent toutes sur CC-1 (cadence H10↔H1/H3) et CC-2 (MANIFEST.md 8 champs 0/8 domain-relevant).
- **D2 research-first** : aucune sœur créée ex-nihilo ; toutes référencent un handoff WF2 daté 2026-07-06.
- **D4 append-only** : ce fichier est nouveau ; aucun canon existant n'a été modifié.
- **D6 lessons shipped** : cette méta-ADR absorbe 4 D6 lessons identifiées dans WonderWoman Finance (handoff) — burner rate, EVA churn, quota dashboard, batch vs per-token.
- **D7 cost-of-escalation** : ratifiée en création par batch "Go 1 a 4" ; aucun escalate additionnel.
- **D8 cross-agent** : la chaîne Picard↔Jerry↔Summers (3-way ack) est l'agent-spine canonique applicable à Codex/Gemini equally.

## 7. Risks + Rollback

- **Risque #1 — Sur-coupling** : si un gate fille dérive, la méta peut casser en cascade. *Mitigation* : chaque gate fille reste sémantiquement autonome dans son périmètre sectoriel ; la méta ne pilote que la cadence, les champs MANIFEST.md optionnels, et le 3-way ack — pas le contenu sectoriel.
- **Risque #2 — Drift Cyborg IT** : si Cyborg rate la fenêtre Q3 W3, IT reste sans gate ; mitigation = sentinel Cyber-arch (sister ADR-IT-PROJECT-GATE-001 à dériver).
- **Risque #3 — Token Plan 75.5%** : si MiniMax révoque l'accès console ; rollback = se rabattre sur agrégation logs Symphony (proxy).
- **Risque #4 — AI-Act T-27** : si A0 rate la deadline du 2026-08-02 ; rollback = HALT tous les gates Legal/Aquaman, escalade Beth Sobriété.
- **Rollback global** : si la méta-ADR elle-même devient inutile, déplacer cette ADR dans `_TRASH_<date>_meta-gate-not-needed/` (no hard-delete, D4 append-only respecté).
- **Posture C** strictement respectée : artefact créé, **0 cron activé**, sister chain ouverte (B1 Jerry Prime → B1 Summers → B2 8 sisters → A3 Picard signing) en attente d'activation Phase A.

## 8. Statut C (Activation Status)

- ✅ Artefact **créé** canoniquement (cette ADR, 2026-07-06).
- ⏸ **0 cron** activé (Posture C respectée — activation Phase A Q3 W2 conditionnée par les 3-way acks sisters).
- ⏸ Sister chain **OUVERTE** : B1 Jerry SYSTEMIZE → B1 Summers SHIP → B2 8 sisters → A3 Picard `picard-audit-and-prod-workflow` signing.
- ⏸ 7 gates filles en `DRAFT` ; passage `ACTIVE` conditionné par 3-way ack.
- ⏸ Cyborg IT sister (8e gate) à dériver en Q3 W3.

## 9. Decision Summary

**1 table, 7 gates absorbés, 1 méta-ADR canonique.** Spec cross-cutting root-cause cover pour CC-1 (cadence H10↔H1/H3 blackout 8/8) et CC-2 (MANIFEST.md 8→22+ champs optionnels sectoriels). Prête pour Phase A **Q3 W2 ratification window** (deadline AI-Act 2026-08-02 = T-27 jours driver).

**Token de ratification** : `RATIFICATION-BATCH-02-2026-07-06-ADR-L2-PROJECT-GATE-META-001`
**Source canon master** : `handoff_wargame_wf2_synthesis_book_coaching_2026-07-06.md`
**Sisters canoniques** : 7 sisters gates listées en frontmatter (sources verbatim).
**Doctrine** : Anti-Paperclip (ADR-ANTI-PAPERCLIP-001) + Sobriété (ADR-SOBER-002) + AaaS 3 Variants (ADR-L2-AAAS-001) + Workflow Loop Engineering (ADR-WORKFLOW-001).
