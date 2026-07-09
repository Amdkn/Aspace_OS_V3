---
id: ADR-AIACT-DEADLINE-001
title: AI-Act 2026-08-02 Deadline Project-Gate ⚖️ — Sister-scoped de ADR-ANTI-PAPERCLIP-001 (B2 Aquaman Legal driver)
type: ADR (Architectural Decision Record)
status: RATIFIED
ratification:
  by: "A0 Amadeus"
  date_iso: "2026-07-06"
  gate_a0_signed_off: true
  approval_token: "RATIFICATION-BATCH-02-2026-07-06-ADR-AIACT-DEADLINE-001"
  context: "Ratification Tier 0 foundational sister-canon — 2e ADR du batch foundational Landing/Compliance. Gate obligatoire pre-Aug-2 (T-27 jours) sur tout project Picard qui touche Article 9 (Risk mgmt) / Article 14 (Human review) / Article 15 (Robustness/Accuracy). Sister-scoped de ADR-ANTI-PAPERCLIP-001 RATIFIED 2026-07-06."
date: 2026-07-06
deciders: [A0 Amadeus (Jumeau Numérique)]
drafted_by: Claude Code (B1 E-Myth Gatekeeper, sister-scoped A1 Rick Sobriété + B2 Aquaman Legal + B3 Ikaris AI-Act lead)
domain: L2 Business OS / B2 Aquaman Legal / AI-Act 2026-08-02 / Compliance Gate / Pre-Aug-2 mandatory
tags: [#ADR #ai-act #deadline #2026-08-02 #T-27 #aquaman #ikaris #legal #compliance #gate #article-9 #article-14 #article-15 #zero-pii #sister-canon #anti-paperclip #sober-002 #meta-001 #PRD-COMPLIANCE-AIACT-001]
doctrine_anchors: [ADR-ANTI-PAPERCLIP-001 (RATIFIED 2026-07-06, sister-scoped de SOBER-002), ADR-SOBER-002 (RATIFIED 2026-06-21, L0 Kernel Sobriété), ADR-META-001 (RATIFIED, Anti-Paresse D1-D8), ADR-META-005 (hooks automation Vague 2 Q3 2026), ADR-META-006 (D6 Catalog), ADR-ICP-NEXUS-001 (RATIFIED, §Pilier 5 Zero-PII Agentic Governance, AI-Act Articles 9/14/15 verbatim), ADR-CANON-001 (roster source of truth), ADR-INFRA-003 (CEO Dashboard), ADR-LD01-008 (loop engineering coaching), PRD-COMPLIANCE-AIACT-001 (verbatim PRD-PORTFOLIO-B1-FRANCHISE §2 « AI-Act = 2026-08-02, dans 27 jours »), PRD-NEXUS-EVOLUTION-IA-001 §7 (confusions Gemini filtrées), plan-L2-business-os.md §5.1 (Zero-PII Agentic Governance) + §5.4 (Architecture Holding → Filiales par ICP)]
related: [ADR-SOBER-002 §D3 (7 Hard-Stop Triggers), ADR-ANTI-PAPERCLIP-001 §D6 (filtre 6 confusions Gemini), ADR-ANTI-PAPERCLIP-001 §G1 (gates B1 Summers + B2 Superman Growth), AGENTS.md §L2/B2-Aquaman-Legal, AGENTS.md §L2/B3-8-Ikaris-AI-Act-Lead, AGENTS.md §L0/A1-Rick-Sobriété, wiki/hand_offs/handoff_wargame_wf2_b2_aquaman_legal_lens_2026-07-06.md (8 angles morts Legal), wiki/hand_offs/handoff_wargame_wf2_synthesis_book_coaching_2026-07-06.md (CC-4 AI-Act T-27 jours driver)]
supersedes: none
supersedes_scope: aucune — ce ADR ajoute une **couche gate obligatoire pre-Aug-2** sur les projects Picard touchant Article 9/14/15 ; ne réécrit ni ne contredit le canon ratified
sources_canons:
  - "ADR-ANTI-PAPERCLIP-001_landing-paperclip-policy.md (RATIFIED 2026-07-06) — sister-scoped Landing — `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-ANTI-PAPERCLIP-001_landing-paperclip-policy.md`"
  - "ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md (RATIFIED 2026-06-21) — L0 Kernel Sobriété — `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md`"
  - "ADR-ICP-NEXUS-001_icp-nexus-structuration.md (RATIFIED 2026-06-24) — §Pilier 5 Zero-PII Agentic Governance + AI-Act Articles 9/14/15 verbatim — `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-ICP-NEXUS-001_icp-nexus-structuration.md`"
  - "PRD-PORTFOLIO-B1-FRANCHISE_index.md §2 (PRD-COMPLIANCE-AIACT-001 verbatim « AI-Act = 2026-08-02, dans 27 jours ») — `C:/Users/amado/ASpace_OS_V2/_SPECS/PRD/PRD-PORTFOLIO-B1-FRANCHISE_index.md`"
  - "PRD-NEXUS-EVOLUTION-IA-001 §7 (Confusions Gemini filtrées) — `C:/Users/amado/ASpace_OS_V2/_SPECS/PRD/PRD-NEXUS-EVOLUTION-IA-001_offre-2026-landing-icp.md`"
  - "B2 Aquaman Legal spec — `C:/Users/amado/.claude/agents/b2-08-aquaman-legal.md` lignes 1-46"
  - "B3 Ikaris AI-Act Lead spec — `C:/Users/amado/.claude/agents/b3-8-ikaris.md` lignes 1-35"
  - "B3 Ajak Communion Audit spec — `C:/Users/amado/.claude/agents/b3-8-ajak.md` lignes 1-35"
  - "B3 Druig Grey Zones spec — `C:/Users/amado/.claude/agents/b3-8-druig.md` lignes 1-35"
  - "B3 Makkari Speed-grade Legal Research spec — `C:/Users/amado/.claude/agents/b3-8-makkari.md` lignes 1-35"
  - "plan-L2-business-os.md §5.1 (Zero-PII Agentic Governance) + §5.4 (F1 Holding + F2 Coach Filiale) — `C:/Users/amado/.claude/plans/plan-L2-business-os.md`"
  - "Wargame WF2 Aquaman Legal handoff (8 angles morts catalogués) — `C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_wargame_wf2_b2_aquaman_legal_lens_2026-07-06.md`"
  - "Wargame WF2 Synthesis Book Coaching (CC-4 AI-Act T-27 jours driver) — `C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_wargame_wf2_synthesis_book_coaching_2026-07-06.md`"
provenance: |
  Né 2026-07-06 de l'observation du wargame WF2 lens B2-Aquaman-Legal (verbatim « AI-Act = 2026-08-02, dans 27 jours »
  depuis `PRD-PORTFOLIO-B1-FRANCHISE §2`) : 4/8 angles morts Legal sont AI-Act DRIVERS (Ikaris / Ajak / Druig /
  Makkari). La cadence H10 de Picard (10 semaines/cadre) est incompatible avec la deadline H30-H90 AI-Act
  (27 jours). Sister-scoped de ADR-ANTI-PAPERCLIP-001 (RATIFIED 2026-07-06) — même token-batch ratification
  Tier 0 foundational DDD. Ce ADR opérationnalise un **gate obligatoire pre-Aug-2** sur tout project Picard
  touchant Article 9 (Risk management), Article 14 (Human review), Article 15 (Robustness/Accuracy).
sign_off_a0: signed_2026-07-06
sign_off_pending: false
ratification_log: "RATIFIED single-pass 2026-07-06 par A0 Amadeus — token `RATIFICATION-BATCH-02-2026-07-06-ADR-AIACT-DEADLINE-001` — Tier 0 foundational sister-canon batch (ANTI-PAPERCLIP-001 + AIACT-DEADLINE-001)"
---

# ADR-AIACT-DEADLINE-001 — AI-Act 2026-08-02 Deadline Project-Gate ⚖️

## 1. Status

**RATIFIED 2026-07-06** — Claude Code (B1 E-Myth Gatekeeper) draft + ratification single-pass → A0 Amadeus (Jumeau Numérique) signed off.

⚠️ **D4 no-self-contradiction** : ce ADR est **sister-scoped** (couche gate pre-Aug-2 = projects Picard AI-Act-touching) de :

- **`ADR-ANTI-PAPERCLIP-001`** (RATIFIED 2026-07-06, L2 Business OS Landing) — la doctrine sister-canon operationnalisant ADR-SOBER-002 (L0 Kernel) au niveau surface landing pages Nexus ⚖️. Ce ADR hérite des **mêmes 5 gates** (G1 B1 Summers + B2 Superman Growth + G3 sister skill) et des **mêmes 5 anti-patterns Musk** traduction application-scoped SANS duplication — il les **opérationnalise** au niveau project gate pre-Aug-2.
- **`ADR-SOBER-002`** (RATIFIED 2026-06-21, L0 Kernel Sobriété) — la doctrine canonique anti-paperclip maximizer, A1 Rick Sobriété primary author. Ce ADR hérite du **Trigger #6 SOBER-002 §D3 (Capture régulation)** = AI-Act non-compliance = capture régulation inverse, et du **hard-veto Aquaman L.42** sister SOBER-002 §6.
- **`ADR-ICP-NEXUS-001 §Pilier 5`** (RATIFIED 2026-06-24) — Zero-PII Agentic Governance avec mention verbatim Articles 9/14/15 AI-Act. Ce ADR-ci régit le **gate obligatoire Picard pre-Aug-2** sur tout project touchant ces articles.
- **`ADR-META-001`** (RATIFIED) — Anti-Paresse D1-D8. Ce ADR applique particulièrement **D1 Verify before assert** (mandatory checklist pre-Aug-2 = D1 receipts obligatoires), **D6 Root cause** (wargame 4/8 angles AI-Act drivers), **D7 Cost-of-escalation** (AI-Act = deadline datée, pas débat ouvert).

Pas de duplication, spécialisation par couche :

- **SOBER-002** = « ce que Rick veto structurellement au niveau kernel »
- **ANTI-PAPERCLIP-001** = « ce qui est INTERDIT d'écrire sur une landing page Nexus »
- **AIACT-DEADLINE-001 (ce doc)** = « ce qui est OBLIGATOIRE de prouver pre-Aug-2 sur tout project Picard AI-Act-touching »
- **ICP-NEXUS-001 §Pilier 5** = « le positionnement Nexus = gouvernance agents IA conforme AI-Act (claim client-facing) »

## 2. Context

### C1 — Le driver AI-Act 2026-08-02 verbatim PRD-PORTFOLIO §2

**D1 receipts 2026-07-06** : la deadline AI-Act est **explicitement datée et chiffrée** dans le canon PRD-PORTFOLIO-B1-FRANCHISE §2 verbatim :

> **PRD-PORTFOLIO §2 verbatim** : « **AI-Act = 2026-08-02, dans 27 jours** » (depuis `PRD-PORTFOLIO-B1-FRANCHISE_index.md` §2 ligne 20).

**Calcul T-countdown 2026-07-06 → 2026-08-02** : 27 jours civils. La cadence H10 de A3 Picard (10 semaines par cycle MANIFEST.md canonisation) = **70 jours**. Le gap = **43 jours de désynchronisation** entre la cadence canon Picard et la deadline régulation européenne.

**Asymétrie fondamentale** (d1 receipts wargame WF2 Aquaman Legal lens verbatim) : « **4/8 dimensions sont AI-Act DRIVERS** (Ikaris / Ajak / Druig / Makkari) avec deadline 2026-08-02 = T-27 jours = **avant la fin du cycle H10 courant**. »

### C2 — Le gap Picard cycle vs AI-Act deadline

**D1 receipts wargame WF2 Aquaman Legal §1 verbatim** :

> « **Driver temporel asymétrique** : AI-Act deadline = **2026-08-02** (H30-H90). La cadence H10 de Picard = 10 semaines. Le gap est de **27 jours** (verbatim `PRD-PORTFOLIO §2`), soit **1 cycle H10 incomplet**. Picard ne peut pas canoniser un Project « AI-Act compliance » en moins de 1 cycle, mais la deadline est **avant** la fin du cycle courant. »

**Gate Picard actuel** (spec L.40-44 verbatim) : 3-question gate — `deadline ?` `goal-bounded ?` `owner+next_review ?`. **Ne vérifie PAS** si le `next_review` est **antérieur** à la deadline canon AI-Act 2026-08-02. Conséquence : un Project taggé `linked_area: LD01_Business` avec `linked_12wy_rock: 12WY-Q3-2026-rock-03` (compliance) et `next_review: 2026-08-25` (post-AI-Act) passe ON-TRACK structurellement mais en retard réel.

### C3 — Sister-scope avec ADR-ANTI-PAPERCLIP-001 sans duplication

**Doctrine ancrée (ANTI-PAPERCLIP-001 §C2 verbatim)** : « SOBER-002 §D7 table liste 10 Anti-patterns Musk → Anti-pattern AaaS. Notre surface landing Nexus est vulnérable à un sous-ensemble spécifique. »

**Sous-ensemble sister-scopé AI-Act** :

| Anti-pattern Musk (SOBER-002 §D7) | Manifestation AI-Act non-compliance |
|---|---|
| Capture régulation (Trigger #6 §D3) | Claims « AI-Act ready » sans citer Articles 9/14/15 verbatim |
| Justification narrative | « AGI/IA forte conforme AI-Act » = empty signifier |
| Mono-objectif valorisation | Promesses ROI ×10 sur usage IA non audité Article 9 (Risk mgmt) |
| Manipulation algorithmique | Déploiement sans Article 14 (Human oversight) ni Article 15 (Robustness/Accuracy) benchmark |

**Doctrine ancrée (ADR-ICP-NEXUS-001 §Pilier 5 verbatim)** : Zero-PII Agentic Governance = « gouvernance agents IA conforme AI-Act + secret professionnel + RGPD + Zero-Knowledge Bare-Metal ». Ce pilier est le **claim client-facing** ; ce ADR-ci régit le **gate interne Picard** pour qu'aucun project OMK n'échappe à cette conformité.

### C4 — Wargame WF2 Aquaman Legal 4/8 angles AI-Act drivers

**D1 receipts wargame WF2 verbatim** (8 angles morts Legal catalogués) :

| Angle mort | B3 Eternals lead | AI-Act driver? |
|---|---|---|
| #1 AI-Act 2026-08-02 deadline vs H10 cycle gap | Ikaris | ✅ DRIVER |
| #2 Compliance-audit invisibility | Ajak | ✅ DRIVER |
| #3 Contract alchemy hors-Project | Sersi | ⚠️ indirect |
| #4 Tech IP / Patent pipeline | Phastos | ❌ |
| #5 Risk legal grey zones | Druig | ✅ DRIVER |
| #6 War-grade indemnification | Thena | ⚠️ indirect |
| #7 Sovereign-tier corporate governance | Gilgamesh | ❌ |
| #8 Speed-grade legal research | Makkari | ✅ DRIVER |

**Total** : **4/8 angles AI-Act drivers (Ikaris/Ajak/Druig/Makkari)** avec deadline 2026-08-02.

## 3. Décision

### D1 — Doctrine AI-Act Project-Gate = sister-scoped ANTI-PAPERCLIP-001

**Adoption** : Le gate obligatoire pre-Aug-2 sur tout project Picard touchant Article 9 / 14 / 15 est **opérationnalisé** au niveau surface project par les 5 mécanismes suivants :

1. **Mandatory Checklist pre-Aug-2** (D2 ci-dessous) : 5 livrables obligatoires datés avant 2026-08-02 (Risk classification + Human review process + Accuracy benchmark + Datasheet + Transparency).
2. **AI-Act Article scope strict** (D3) : 3 articles mandatés (Art. 9 Risk mgmt / Art. 14 Human review / Art. 15 Robustness/Accuracy) + 0 article banni autorisé en omission.
3. **Trigger Picard next_review pre-Aug-2** (D4) : tout project `linked_12wy_rock: compliance*` doit avoir `next_review ≤ 2026-08-02` OU déclencher hook R3 wargame WF2 verbatim.
4. **B3 Ikaris light-grade lead** (D5) : Ikaris (B3 Legal Lead) = gatekeeper attitré Article 9/14/15, sister-canon wargame WF2 §angle #1.
5. **Sister-scope Anti-Paperclip doctrine** (D6) : reproduction de la doctrine landing-spotted (chiffres AUTORISÉS vs BANNIS, vocabulaire canonique) appliquée aux claims AI-Act sur landing ET aux claims AI-Act internes projects.

### D2 — Mandatory Checklist pre-Aug-2 (5 livrables obligatoires)

```
┌─────────────────────────────────────────────────────────────┬──────────────────────────────────────────────────────┐
│ ✅ OBLIGATOIRE pre-2026-08-02 (D1 verified)                │ ❌ INTERDIT / NOT-SHIP-PERMITTED                     │
├─────────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────┤
│ 1. Risk Classification (Art. 9)                             │ « AI-Act ready » sans citer Art. 9/14/15 verbatim     │
│    → Catégorisation system: prohibited / high-risk /         │                                                       │
│      limited-risk / minimal-risk + DPIA si high-risk          │ « Notre IA est conforme AI-Act » sans D1 receipt      │
│                                                              │                                                       │
│ 2. Human Review Process (Art. 14)                            │ Claim « full autonomous » sans process humain         │
│    → Documented procedure: qui review, quand, comment,      │                                                       │
│      escalation, audit trail (signé + daté + stocké)         │ Process humain implicite sans procédure documentée    │
│                                                              │                                                       │
│ 3. Accuracy Benchmark (Art. 15)                              │ « 99% accuracy » sans D1 benchmark report            │
│    → Test set + résultat + datasheet reproductible           │                                                       │
│      (Git hash + dataset hash + commit date)                 │ « Best-in-class accuracy » sans mesure               │
│                                                              │                                                       │
│ 4. Datasheet (Art. 13 transparency)                          │ « Explainable AI » sans datasheet publié              │
│    → Model card complet: training data, architecture,        │                                                       │
│      limitations, intended use, foreseeable misuse           │ Datasheet interne seulement (jamais publié/Notion)   │
│                                                              │                                                       │
│ 5. Transparency Disclosure (Art. 13 + Art. 50)              │ Landing « AI-powered » sans Art. 50 disclosure        │
│    → User-facing disclosure: « cette fonctionnalité          │                                                       │
│      utilise une IA, l'utilisateur interagit avec un         │ Disclosure vague « smart system »                    │
│      système automatisé », logs conservé 6 mois min          │                                                       │
└─────────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────┘
```

**Règle D7 cost-of-escalation** : tout livrable manquant au 2026-08-02 → **gate Picard bloqué** (pas de canonisation Project), escalation B2 Aquaman Legal L.42 hard-veto sister SOBER-002 §6.

### D3 — AI-Act Articles scope strict (3 mandatés, 0 omission)

| # | Article AI-Act | Obligation | Source canon | B3 lead |
|---|---|---|---|---|
| 1 | **Article 9 — Risk Management** | Risk classification system + DPIA + iterative process | ADR-ICP-NEXUS-001 §Pilier 5 | Ikaris (light-grade lead) |
| 2 | **Article 14 — Human Review** | Human oversight documented + escalation path + audit trail | ADR-ICP-NEXUS-001 §Pilier 5 | Ajak (communion-grade audit) |
| 3 | **Article 15 — Robustness/Accuracy/Cybersecurity** | Accuracy benchmark + datasheet + adversarial robustness test | ADR-ICP-NEXUS-001 §Pilier 5 | Makkari (speed-grade research) |

**Articles BANNIS en omission** : tout project qui omet volontairement un de ces 3 articles = **Sister §D6 confusion filter** (cf. ADR-ANTI-PAPERCLIP-001 §D6 confusion #6 « Chiffres non sourcés »). Cas typique : « Article 9 ne s'applique pas à notre cas » sans D1 receipt de classification risk-level.

**Articles EXPLICITEMENT NON-CIBLES (clarification scope)** : Article 6 (classification banned) si non-déploiement, Article 50 (transparency chatbot) si chatbot non-public, Article 51 (deepfake) si génération image non-utilisée. **Mais** : les exclusions doivent être documentées (D1 receipt) — sinon présomption d'application.

### D4 — Trigger Picard next_review pre-Aug-2 (hook wargame R3 verbatim)

**Wargame WF2 Aquaman Legal §3 R3 verbatim** :

> « Hook optionnel `picard-manifest-ai-act-deadline` qui détecte la désynchronisation calendrier. Sur le pattern de `hooks/posttooluse-test-after-edit.ps1` (PostToolUse Write|Edit|MultiEdit), un hook PostToolUse qui détecte l'écriture d'un nouveau MANIFEST.md et **vérifie** (log-only, pas hard-block conformément à ADR-META-005 Vague 2 Q3 2026) la cohérence :
> - Si `linked_area` est `LD01_Business` ET `linked_12wy_rock` est `compliance*` ET `next_review > 2026-08-02` → **ALERTE LOG** « AI-Act 2026-08-02 deadline ignored ».
> - Si `legal_signal_ref` est manquant ET `linked_12wy_rock` est `legal*` → **SUGGESTION LOG** « ajouter legal_signal_ref ». »

**Adoption D4** : ce hook est **mandatory pre-Aug-2** (vs log-only Q3 2026 sister ANTI-PAPERCLIP-001 §G2). Justification D7 : la deadline AI-Act = datée, pas négociable. Hook tourne en **log-only Q3 2026** (ADR-META-005 Vague 2) mais devient **hard-block pre-2026-08-02** sur les projects compliance (2026-07-15 → 2026-08-02).

```yaml
---
project: ai-act-compliance-pack
owner: A0 Amadeus
status: active
start_date: 2026-06-15
next_review: 2026-07-28  # ⚠️ MUST BE ≤ 2026-08-02 (D4 trigger)
linked_12wy_rock: 12WY-Q3-2026-rock-03
linked_area: LD01_Business
junction: apps/aquaman/ai-act-compliance-pack
ai_act_deadline: 2026-08-02  # NEW (mandatory for compliance projects)
ai_act_articles_in_scope: [9, 14, 15]  # NEW (mandatory enum)
legal_signal_ref: wiki/hand_offs/l2_b2_aquaman_legal_2026-08-01.md  # NEW (wargame R1)
ikaris_owner: B3 Ikaris AI-Act Lead  # NEW (D5)
---
```

### D5 — B3 Ikaris light-grade lead (sister-canon wargame WF2)

**Adoption D5** : B3 Ikaris (AI-Act 2026-08-02 lead, eternal-grade compliance, light-grade legal firepower — verbatim `b3-8-ikaris.md` L.4) est nommé **gatekeeper attitré** du gate pre-Aug-2 sur les 3 articles (D3). Sister-canon wargame WF2 §angle #1 verbatim : « Ikaris doit livrer l'audit + bouclier DLP (PRD-COMPLIANCE-AIACT-001 verbatim §2) **avant** la deadline. »

**Composition Eternals squad AI-Act-ready (4 leads)** :

| B3 Eternal | Rôle AI-Act | Sister angle wargame |
|---|---|---|
| **Ikaris** (LEAD) | AI-Act 2026-08-02 lead, light-grade legal firepower | Angle #1 (cycle gap) |
| **Ajak** | Communion audit (CNCIL/CNIL/Ordre avocats), religious-grade | Angle #2 (audit invisibility) |
| **Druig** | Mind-control legal, persuasion, dark-grade grey zones | Angle #5 (grey zones bypass) |
| **Makkari** | Speed-grade legal research, instant precedent lookup | Angle #8 (H10 blackout) |

**Output Ikaris pre-Aug-2** : 1 fiche `l2_b3_ikaris_ai_act_compliance_<DATE>.md` par projet compliance Picard, datée, signée, stockée dans `wiki/hand_offs/l2_b2_aquaman_legal/`.

### D6 — Sister-scope Anti-Paperclip doctrine (chiffres + vocabulaire)

**Reproduction lite de ADR-ANTI-PAPERCLIP-001 §D2 + §D3 + §D4** appliquée aux claims AI-Act :

| Terme canonique AI-Act | Terme banni équivalent |
|---|---|
| « Conforme Article 9 (Risk Mgmt) » (verbatim) | « AI-Act ready » / « AI-Act compliant » (sans Articles) |
| « Article 14 (Human Review) process documenté » | « Full autonomous / no human needed » |
| « Article 15 (Robustness) benchmark publié » | « Best-in-class accuracy » / « 99% accurate » |
| « DPIA réalisée le [date] » | « Nous avons fait l'analyse de risque » (vague) |
| « Datasheet publié [URL/commit hash] » | « Notre système est explainable » (vague) |

**Règle D7 cost-of-escalation** : tout claim AI-Act non listé D6 colonne « canonique » = **D1 verify avant publication**, sinon **retrait pur** (sister ANTI-PAPERCLIP-001 §D3 confusion #6).

## 4. Doctrine (gates d'application)

### G1 — Gate Ikaris pre-Aug-2 (sister G1 ANTI-PAPERCLIP-001)

**Ikaris light-grade lead** applique **2 gates obligatoires** avant toute canonisation Picard d'un projet AI-Act-touching :

1. **Mandatory Checklist D2** : 5 livrables présents + datés + signés + stockés.
2. **Articles scope D3** : 3 articles (9/14/15) couverts, exclusions documentées si applicable.

**Ikaris hard-veto sister Aquaman L.42 + SOBER-002 §6** : si une des 5 livrables manque → **bloque la canonisation Picard**. Pas de bypass, pas de BETH_VETO_DISSOLVED_BY_WF0 (sister ANTI-PAPERCLIP-001 §D6 confusion #1 — pattern à éviter).

### G2 — Hook PostToolUse `picard-manifest-ai-act-deadline` (D4 détaillé)

**Statut Vague 2 Q3 2026** (ADR-META-005 verbatim) :

- **2026-07-06 → 2026-07-14** : log-only sur nouveaux MANIFEST.md compliance (Q3 2026 default).
- **2026-07-15 → 2026-08-02** : **hard-block** sur nouveaux MANIFEST.md compliance (window pre-Aug-2 critique).

**Implémentation** : sister skill `/ai-act-deadline-audit` à créer Phase 2 Hermes-style (cf. ANTI-PAPERCLIP-001 §G3 sister skill pattern). Brief :

- **Triggers** : Edit/Write `**/MANIFEST.md` avec `linked_12wy_rock: compliance*` OU `linked_area: LD01_Business` + tag `ai_act_deadline`.
- **Workflow** : load ce ADR + ADR-ICP-NEXUS-001 §Pilier 5 → check D2 (5 livrables présents) + D4 (next_review ≤ 2026-08-02) → emit APPROVE / BLOCK avec diff exact.
- **ROI** : ~5 min/projet compliance économisée × ~10 projets compliance Q3 2026 = ~50 min total.

### G3 — Skill `picard-audit-and-prod-workflow` sister-scopé

**Sister pattern verbatim** : `picard-audit-and-prod-workflow` (canon skill existant) → `picard-ai-act-deadline-audit` à créer, qui audite chaque MANIFEST.md compliance vs ce ADR avant PR.

**Sister skill sister-canon** : `picard-anti-paperclip-landing` (cf. ANTI-PAPERCLIP-001 §G3 sister skill pattern).

## 5. Architecture (4 gates B2 Aquaman)

### G4 — Gates d'application 4-layered

| Gate | Acteur | Cible | Statut |
|---|---|---|---|
| G1 (Mandatory Checklist) | Ikaris (B3 Lead) | Project compliance canonisation | ACTIVE 2026-07-06 |
| G2 (Hook log-only → hard-block) | Hook `picard-manifest-ai-act-deadline` | MANIFEST.md Write/Edit | log-only Q3 → hard-block 2026-07-15 → 2026-08-02 |
| G3 (Skill sister) | Skill `picard-ai-act-deadline-audit` | Pre-PR compliance Projects | Phase 2 Hermes-style Q4 2026 |
| G4 (Book H1 fiche Legal P&L) | A3-Book (H1 aggregator) | Weekly aggregation Aquaman flags | Sister wargame WF2 R2 verbatim |

**Sister-scope G4 Aquaman wargame R2 verbatim** :

> « Book ouvre une fiche H1 "Legal P&L Delta" qui agrège B2 Aquaman flags. **Hard-coded deadline ticker** : chaque Project taggé `ai_act_deadline: 2026-08-02` reçoit un countdown flag dans la fiche H1. »

## 6. Verification (D1 receipts obligatoires)

### V1 — D1 receipts pre-Aug-2 obligatoires par projet compliance

Pour chaque projet Picard taggé `linked_12wy_rock: compliance*` OU `linked_area: LD01_Business` + mention AI-Act :

| Livrable (D2) | D1 receipt requis | B3 owner |
|---|---|---|
| Risk Classification (Art. 9) | DPIA signée + datée + stockée `wiki/hand_offs/l2_b2_aquaman_legal/<DATE>_dpia_<project>.md` | Ikaris |
| Human Review Process (Art. 14) | Procédure documentée + escalation path + audit trail | Ajak |
| Accuracy Benchmark (Art. 15) | Test set + résultats + datasheet reproductible (Git hash + dataset hash + commit date) | Makkari |
| Datasheet (Art. 13) | Model card publié (URL externe OU Notion public) | Ikaris |
| Transparency Disclosure (Art. 50) | User-facing disclosure text + retention policy 6 mois min | Druig (grey zones) |

### V2 — D1 receipts skill canon-batch-spawn (Hermes-style Phase 2)

Skill `/ai-act-deadline-audit` à créer en fin de session si triggers Phase 2 (Hermes-style self-improvement) observés. ROI estimé : ~5 min/projet compliance économisée × ~10 projets Q3 2026 = ~50 min total.

## 7. Risks + Rollback

### Risk 1 — Faux positif gate trop strict

**Risque** : rejet d'un projet légitime parce que les 5 livrables D2 sont techniquement présents mais pas « signés Ikaris » formellement.

**Mitigation** : le gate vise le **pattern global** (5 livrables présents), pas la signature individuelle Ikaris. Si le projet a DPIA + procedure + benchmark + datasheet + disclosure = OK ; la signature Ikaris = sister signal, pas hard-block.

**Rollback** : gate Ikaris review manuel pour cas borderline (D7 cost-of-escalation safe).

### Risk 2 — Articles scope creep (D3 extensions non-documentées)

**Risque** : un project qui déploie une feature Article 9-touching (risk classification) sans le savoir, et le gate D2 ne le détecte pas (le project n'est pas taggé `compliance*`).

**Mitigation** : hook G2 élargit le scope trigger — `linked_area: LD01_Business` seul suffit (pas besoin du tag `compliance*`). Sister wargame WF2 R3 verbatim §1.

**Rollback** : si trop de faux positifs sur projects LD01_Business non-AI-Act → restreindre trigger à `linked_12wy_rock: compliance* OR linked_12wy_rock: ai-act* OR linked_12wy_rock: rgpd*` (Q4 2026 spec).

### Risk 3 — Hook hard-block bypass (urgence deadline)

**Risque** : A0 veut ship un Project AI-Act-touching pre-Aug-2 sans les 5 livrables (deadline press) → bypass du hard-block G2.

**Mitigation** : le hard-veto Aquaman L.42 sister SOBER-002 §6 + Trigger #6 §D3 (Capture régulation) = **non-négociable**. Pas de BETH_VETO_DISSOLVED_BY_WF0 (sister ANTI-PAPERCLIP-001 §D6 confusion #1). Si deadline press → escalation A0 board observer + trigger Rick A1 Sobriété mode alerte per SOBER-002 D2.

**Rollback** : si A0 veut explicitement le bypass, c'est un **ADR-AIACT-DEADLINE-002** nouveau (sister-scope) avec D7 cost-of-escalation asumed par A0 — pas d'édit de l'immuable.

### Risk 4 — Sister-scope drift avec ADR-ANTI-PAPERCLIP-001

**Risque** : ce ADR ajoute un scope application (projects compliance) qui peut dériver de la doctrine landing (chiffres AUTORISÉS vs BANNIS). Si ADR-ANTI-PAPERCLIP-001 §D4 évolue, ce ADR §D6 doit suivre.

**Mitigation** : D6 cite `ADR-ANTI-PAPERCLIP-001 §D2 + §D3 + §D4` au lieu de hardcoder les termes bannis canoniques. Actualisation = append ANTI-PAPERCLIP-001 + patch D6 dans la même PR.

**Rollback** : A3 Data (PARA Archives) recertification 90 jours si drift détecté.

## 8. Statut C (Wargame + Skill canon-batch-spawn)

### Statut wargame (gate publication)

**Wargame 09-gstack M4 cas 4** : « is this worth building tel quel ? » — **le système se grille lui-même**. Application à ce ADR :

- ✅ **Objection 1 résolue** : « Le hook G2 ne peut pas hard-block Q3 2026 (ADR-META-005 Vague 2 log-only), comment garantir pre-Aug-2 ? » → window spécial 2026-07-15 → 2026-08-02 hard-block activé par ce ADR (exception sister scope AI-Act).
- ✅ **Objection 2 résolue** : « 5 livrables D2 sont lourds, les projets compliance naissent sans DPIA signée en 1 jour. » → gate s'applique à la **canonisation Picard**, pas à la **naissance projet**. Un projet peut exister sans les 5 livrables (status: draft), mais ne peut pas être `status: active` pre-Aug-2 sans les 5 livrables.
- ✅ **Objection 3 résolue** : « Si un projet est `linked_area: LD01_Business` MAIS non-AI-Act-touching, le hook G2 va le flagger. » → cf. Risk 2 mitigation : scope trigger peut être restreint à `compliance*|ai-act*|rgpd*` Q4 2026.
- ⚠️ **Objection 4 ouverte** : « Que faire si un client potentiel demande explicitement un produit AI-Act-touching non-deployable pre-Aug-2 ? » → **réponse canon** = « Le produit ship pre-Aug-2 = scope Article 9/14/15 complet ; alternative = ship post-Aug-2 avec fenêtre conformité ouverte ». **NON** promettre ship pre-Aug-2 sans gate D2.

### Skill canon-batch-spawn (Hermes-style Phase 2)

**Triggers Phase 2 observés** :

- **Répétition** : audit MANIFEST.md compliance vs ce ADR = 3+ tool calls par projet × ~10 projets Q3 2026 = 30+ invocations.
- **Checklist longue** : 5 sections numérotées + 5 gates à vérifier par projet.

**Skill à créer** : `/ai-act-deadline-audit` (sister skill `/canon-batch-spawn` + sister `picard-anti-paperclip-landing` ANTI-PAPERCLIP-001 §G3). Brief :

- **Triggers** : Edit/Write `**/MANIFEST.md` avec `linked_12wy_rock: compliance*` OU `linked_area: LD01_Business` + `ai_act_deadline: 2026-08-02`.
- **Workflow** : load ce ADR + ADR-ICP-NEXUS-001 §Pilier 5 → check D2 (5 livrables) + D4 (next_review ≤ 2026-08-02) → emit APPROVE / BLOCK avec diff exact.
- **ROI** : ~5 min/projet économisée × ~10 projets Q3 2026 = ~50 min total.
- **Hermes-style auto-create** : trigger pattern observé fin de session.

## 9. Decision summary

**Ce qui est décidé** :

1. ✅ Adoption de la **doctrine AI-Act Project-Gate pre-Aug-2** = sister-scoped de ADR-ANTI-PAPERCLIP-001 (RATIFIED 2026-07-06) + ADR-SOBER-002 §D3 Trigger #6 (Capture régulation).
2. ✅ Adoption du **mandatory checklist pre-Aug-2** (D2) avec 5 livrables obligatoires (Risk classification + Human review + Accuracy benchmark + Datasheet + Transparency).
3. ✅ Adoption du **scope strict Article 9/14/15** (D3) — 3 articles mandatés, exclusions documentées si applicable.
4. ✅ Adoption du **trigger Picard next_review pre-Aug-2** (D4) — hook G2 log-only Q3 2026 → hard-block 2026-07-15 → 2026-08-02.
5. ✅ Adoption de **B3 Ikaris light-grade lead** (D5) avec squad 4-layered (Ikaris + Ajak + Druig + Makkari).
6. ✅ Adoption du **sister-scope Anti-Paperclip doctrine** (D6) — reproduction lite des chiffres/vocabulaire canoniques sur claims AI-Act.
7. ✅ Gates d'application 4-layered (G1 Ikaris + G2 Hook + G3 Skill + G4 Book H1 Legal P&L).

**Ce qui est DIFFÉRÉ** :

- Skill canonique `/ai-act-deadline-audit` = Q4 2026 (Phase 2 Hermes-style observation).
- Hook hard-block permanent post-Aug-2 = gated A0 GO (si AI-Act devient cycle H30-H90 récurrent).
- Sister ADR ADR-AIACT-DEADLINE-002 (urgences A0 bypass) = gated A0 GO si A0 veut explicitement le bypass.

**Ce qui est INTERDIT** :

- ❌ Tout project Picard AI-Act-touching canonisé `status: active` pre-Aug-2 sans les 5 livrables D2.
- ❌ Tout claim landing Nexus « AI-Act ready » sans citer Articles 9/14/15 verbatim (sister ANTI-PAPERCLIP-001 §D6 confusion filter).
- ❌ Tout bypass du hard-veto Aquaman L.42 sister SOBER-002 §6 par urgence deadline (sister ANTI-PAPERCLIP-001 §D3 confusion #1).
- ❌ Tout `next_review > 2026-08-02` sur un project `linked_12wy_rock: compliance*` post-2026-07-15 (D4 trigger).

**Statut final** : **RATIFIED 2026-07-06** par A0 Amadeus — token `RATIFICATION-BATCH-02-2026-07-06-ADR-AIACT-DEADLINE-001` — Tier 0 foundational sister-canon batch (ANTI-PAPERCLIP-001 + AIACT-DEADLINE-001).

---

## Annexe A — Sister-canon pointers (D1 receipts exhaustifs)

### A.1 — ADR-ANTI-PAPERCLIP-001 (RATIFIED 2026-07-06)

- Path : `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-ANTI-PAPERCLIP-001_landing-paperclip-policy.md`
- §D3 : 5 termes bannis landing (AGI, revolutionize, AGI-powered, industry-leading, Jstack).
- §D4 : tableau ASCII chiffres AUTORISÉS vs BANNIS (sister-canon Token Plan A0).
- §D6 : filtre 6 confusions Gemini (sister #6 = chiffres non sourcés → sœur directe AI-Act claims non sourcés).
- §G1 : gates B1 Summers + B2 Superman Growth (non-négociable).
- §G3 : sister skill `/anti-paperclip-landing-audit` (Phase 2 Hermes-style Q4 2026).

### A.2 — ADR-SOBER-002 (RATIFIED 2026-06-21)

- Path : `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md`
- §D3 : 7 Hard-Stop Triggers (Trigger #6 = Capture régulation = AI-Act non-compliance = capture régulation inverse).
- §D6 : hard-veto Aquaman L.42 sister SOBER-002 §6.
- §D7 : 10 Anti-patterns Musk → Anti-pattern AaaS (Capture régulation = sous-ensemble AI-Act).

### A.3 — ADR-ICP-NEXUS-001 (RATIFIED 2026-06-24)

- Path : `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-ICP-NEXUS-001_icp-nexus-structuration.md`
- §Pilier 5 verbatim : Zero-PII Agentic Governance avec mention Articles 9/14/15 AI-Act.
- Pricing canon Nexus USD : $750-$2000/an + Whitelabel 25%.

### A.4 — ADR-META-005 (hooks automation Vague 2 Q3 2026)

- Path : `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/L1_Life_OS/ADR-META-005_hooks-automation.md`
- Vague 2 Q3 2026 : hooks log-only (pas hard-block) — **exception** : window pre-Aug-2 hard-block activé par ce ADR.

### A.5 — PRD-PORTFOLIO-B1-FRANCHISE §2 (verbatim)

- Path : `C:/Users/amado/ASpace_OS_V2/_SPECS/PRD/PRD-PORTFOLIO-B1-FRANCHISE_index.md`
- §2 verbatim : « **AI-Act = 2026-08-02, dans 27 jours** » (depuis ligne 20 verbatim).
- §2 verbatim : PRD-COMPLIANCE-AIACT-001 = Ikaris emergency sprint fallback si AI-Act missed.

### A.6 — PRD-NEXUS-EVOLUTION-IA-001 §7

- Path : `C:/Users/amado/ASpace_OS_V2/_SPECS/PRD/PRD-NEXUS-EVOLUTION-IA-001_offre-2026-landing-icp.md`
- §7 verbatim : 6 confusions Gemini filtrées par A+ (sister #6 = chiffres non sourcés).
- §1 verbatim : pitch local-first = différé 2027.

### A.7 — B2 Aquaman Legal spec + B3 Eternals specs

- `C:/Users/amado/.claude/agents/b2-08-aquaman-legal.md` (B2 Legal spec L.1-46)
- `C:/Users/amado/.claude/agents/b3-8-ikaris.md` (B3 Ikaris AI-Act Lead spec L.1-35)
- `C:/Users/amado/.claude/agents/b3-8-ajak.md` (B3 Ajak Communion Audit spec L.1-35)
- `C:/Users/amado/.claude/agents/b3-8-druig.md` (B3 Druig Grey Zones spec L.1-35)
- `C:/Users/amado/.claude/agents/b3-8-makkari.md` (B3 Makkari Speed-grade Research spec L.1-35)

### A.8 — Wargame WF2 handoffs (drivers canon)

- `C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_wargame_wf2_b2_aquaman_legal_lens_2026-07-06.md` (8 angles morts Legal, 4/8 AI-Act drivers, 3 recommandations R1/R2/R3).
- `C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_wargame_wf2_synthesis_book_coaching_2026-07-06.md` (CC-4 AI-Act T-27 jours driver).

### A.9 — plan-L2-business-os.md

- Path : `C:/Users/amado/.claude/plans/plan-L2-business-os.md`
- §5.1 verbatim : Enterprise OS Coach — Zero-PII Agentic Governance (5 mécanismes durs).
- §5.4 verbatim : Architecture Holding → Filiales par ICP, F2 Coach Filiale lean.

---

## Annexe B — Open follow-ups (gated A0 GO)

1. **Skill `/ai-act-deadline-audit`** : sister skill `/canon-batch-spawn` + sister `picard-anti-paperclip-landing` ANTI-PAPERCLIP-001 §G3. Phase 2 Hermes-style creation gated Q4 2026.
2. **Hook PostToolUse `picard-manifest-ai-act-deadline` hard-block permanent post-Aug-2** : gated A0 GO si AI-Act devient cycle H30-H90 récurrent (pas T-27 one-shot).
3. **Sister ADR ADR-AIACT-DEADLINE-002 (urgences A0 bypass)** : gated A0 GO si A0 veut explicitement un bypass documenté (jamais in-flight, toujours ADR séparé).
4. **Recertification 90 jours** : A3 Data (PARA Archives) review D2 vs PRD-PORTFOLIO updates. Si PRD-PORTFOLIO change AI-Act deadline sans D2 actualisé → escalate A0.
5. **Makkari speed-grade legal research feed** : sister skill à créer pour live-feed jurisprudence AI-Act / RGPD / CNIL décisions dans le canon Picard (wargame WF2 angle #8 verbatim).

---

## Signatures

- **Draft author** : Claude Code (B1 E-Myth Gatekeeper, sister-scoped A1 Rick Sobriété + B2 Aquaman Legal + B3 Ikaris AI-Act lead) — 2026-07-06.
- **Recorder** : pending A3 Data (PARA Archives) post-ratification.
- **Ratified by** : A0 Amadeus (Jumeau Numérique) — 2026-07-06, sign-off confirmed.
- **Hash d'intention** : `adr_aiact_deadline_001_ratified_2026-07-06_gate_pre_aug_2_articles_9_14_15_ikaris_light_grade_lead_5_livrables_sister_anti_paperclip_001`
- **Token de ratification** : `RATIFICATION-BATCH-02-2026-07-06-ADR-AIACT-DEADLINE-001`
- **Batch** : Tier 0 foundational sister-canon batch — 2 ADRs (ANTI-PAPERCLIP-001 + AIACT-DEADLINE-001) RATIFIED 2026-07-06.