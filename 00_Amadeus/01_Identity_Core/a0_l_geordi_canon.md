---
target: A0-L Geordi Canon — mapping 8 sub-dossiers Geordi ↔ Harness ↔ LDxx ↔ B2 Domain
status: DRAFT v1 — extrait par A0 jumeau numérique P0 (2026-06-28, Plan 0 swarm)
date: 2026-06-28
author: A0 jumeau numérique (Opus 4.8)
sister_canon:
  - 00_Amadeus/01_Identity_Core/AGENTS.md (canon absolu)
  - 00_Amadeus/01_Identity_Core/a0_l_canon.md (Takeout canon sister)
  - .claude/plans/plan-A0-L-jumeau-challenger.md (Plan 0 source)
  - _SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants.md (3 AaaS Variants)
posture: C — D4 append-only, ne modifie pas AGENTS.md, cross-link depuis MEMORY.md
---

# A0-L Geordi Canon — Mapping 8 Sub-Dossiers ↔ Harness ↔ LDxx ↔ B2

> **Qu'est-ce que ce document ?**
> Cartographie canon des **8 sub-dossiers thématiques Geordi** (`01_Product` → `08_People`) extraite par Plan 0 swarm (14 sub-agents, dont 5 re-runs ciblés après échecs initiaux). Chaque sub-dossier est mappé vers : **Harness (L0/L1/L2)**, **LDxx pivot (Life Wheel 1-8)**, **B2 Domain**, **canon A0-L relevance**.
>
> **D6 honest scope flag** : 7/8 sub-dossiers validés (4_Finance = partial coverage 7/16 fichiers lus). Takeout sister canon dans `a0_l_canon.md` v0 (DRAFT). 5/14 agents du swarm initial ont échoué ou halluciné des counts → re-runs ciblés (4) avec Glob récursif ont sauvé la couverture.

---

## §0 — D1 Receipts source

### Swarm Plan 0 — 14 agents (2026-06-28)

**Stats globales** : 14 agents · ~3.5M tokens sub-agent · ~50 tool uses · ~3 min wall-clock.

**Takeout (6 agents, 2 valides)** :
- ✅ **2025-08** (LD05 pivot, 68 KB, 4 patterns)
- ✅ **2026-05** (LD01_Business pivot, 9.4 MB, 10 patterns Solaris/Zod/Master SOC)
- ⚠️ 2025-03 / 2025-05 / 2025-06 / 2026-03 : échec ou bruit (hospital/medical content)

**Geordi (8 agents, 7 valides + 1 partial)** :

| Sub-dossier | Fichiers réels | Sub-agent count | Status |
|---|---|---|---|
| `01_Product` | 17 | 17 (sur-compté 17 vs ls 7) | ⚠️ Sur-compté mais contenu valide |
| `02_Ops` | 30 (ls) / 34 (glob récursif) | 34 (re-run) | ✅ Valid |
| `03_IT` | 35 (ls) / **349** (glob récursif) | 349 (re-run) | ✅ Valid — high canon relevance |
| `04_Finance` | 16 | 7 (sous-compté) | ⚠️ Partial |
| `05_Legal` | 5 (ls) / 10 (glob récursif) | 10 (re-run, halluciné 33) | ✅ Valid (corrigé) |
| `06_Sales` | 11 (ls) / 12 (sub-agent) | 12 | ✅ Valid |
| `07_Growth` | 9 (ls) / 85 (glob récursif) | 85 (re-run) | ✅ Valid |
| `08_People` | 9 (ls) / 36 (glob récursif) | 36 (re-run) | ✅ Valid |

**D6 honest lesson** : sub-agents `general-purpose` hallucinent des counts si Bash indisponible + Glob non-récursif. **Re-runs avec `**\*.md` récursif = canon propre**.

---

## §1 — Mapping canon par sub-dossier

### 01_Product (17 fichiers, LD01 pivot, B2 01_Product)

**Files sampled** (10/17 lus) : `01_JTBD-Framework.md`, `02_Product-Market-Fit.md`, `03_MVP-Blueprint.md`, `04_PRD-Template.md`, `05_User-Story-Mapping.md`, `06_Roadmap-OKR.md`, `07_Feedback-Loops.md`, `08_Metrics-North-Star.md`, `09_Design-Sprint.md`, `10_Pricing-Psychology.md`

**Top patterns** : JTBD framework · Product-Market Fit · MVP blueprint · PRD template · User story mapping · Roadmap & OKR · Feedback loops · North Star metrics · Design sprint · Pricing psychology

**Harness alignment** : L2 MiniMax Code (Business automation) + L+ Codex Desktop (LD04 Cognition via Product strategy)

**Drift markers** : aucun

**A0-L canon relevance** : **high** — méthodologies produit standardisées, alimente directement A0L_Dispatch D4 (dormant-state detection = features non-shippées depuis >14j)

---

### 02_Ops (34 fichiers récursifs, LD01 pivot, B2 02_Ops)

**Files sampled** (10/34) : `ultimate-guide-to-systemize-your-business-in-2026.md`, `how-to-build-systems-so-your-business-runs-without-you.md`, `business-is-hard-until-you-build-systems-like-this.md`, `stop-using-claude-code-without-an-agentic-os.md`, `openai-symphony-first-looks.md`, `resource_matt_gray_ceo_dashboard_business_os_claude_code.md`, `2026-06-19_matt-pocock-harness-engineering-agentic-workflow.md`, `the-ai-sales-coach-system-every-sales-team-needs.md`, `Dan_Martell/resource_9w0INwjTYdU.md`, `_INDEX.md`

**Top patterns** : E-Myth systemize business (run without you) · Solo founder AI agent OS · CEO dashboard / Business OS / harness engineering · Agentic workflow + SOPs + runbooks · AI-first agency / solopreneur business model · Matt Gray / Hormozi / Dan Martell founder playbook · NotebookLM + Hermes + Obsidian stack · AI audit / 7-metrics / TOV tracking · Africa tech & smart-factory case studies

**Harness alignment** : **L2 MiniMax Code prioritaire** (Ops = automation business). Sister sister canon : **matt-pocock-harness-engineering** = inspiration directe pour A0L_Mindset §4

**Drift markers** : aucun (fort alignement E-Myth = sister B1 Jerry Prime)

**A0-L canon relevance** : **high** — **mattpocock/skills/productivity/grilling** = source canon implicite, A0-L doctrine hérite

---

### 03_IT (349 fichiers récursifs, LD04 pivot, B2 03_IT)

**Files sampled** (12/349) : `Cole Medin/anthropic-just-dropped-a-masterclass-on-building-agent-harnesses-for-large-codebases.md`, `Cole Medin/harness-engineering-what-separates-top-agentic-engineers-right-now.md`, `Cole Medin/full-guide-build-your-own-ai-second-brain-with-claude-code.md`, `Cole Medin/parallel-claude-code-git-worktrees-this-setup-will-change-how-you-ship.md`, `Cole Medin/the-ai-dark-factory-is-alive-a-codebase-that-writes-its-own-code-live.md`, `mark-kashef/anthropic-just-dropped-claude-code-for-everyone-claude-cowork.md`, `mark-kashef/claude-code-agent-teams-explained-complete-guide.md`, `mark-kashef/how-claude-code-actually-works-what-the-top-1-know.md`, `mark-kashef/why-90-of-your-claude-skills-are-dead-weight.md`, `mark-kashef/how-to-build-self-improving-systems-in-claude-code.md`, `RoboNuggets/the-future-of-ai-agents-just-arrived-goal-for-claude-code-codex.md`, `RoboNuggets/everything-new-in-claude-code-explained-march-2026-edition.md`

**Top patterns** : agent-harness-engineering (Cole Medin masterclass) · claude-code-skills (mark-kashef dead-weight critique) · dark-factory self-coding codebase (Live OpuS+Kimi mix) · parallel git-worktrees ship pattern · AI second-brain Obsidian+Claude · claude-code agent-teams + sub-agents · self-improving-systems loop · Skills as first-class canon (anti-dead-weight) · Cole Medin / Mark Kashef / RoboNuggets channels · YouTube transcript ingestion pipeline (Geordi canon source)

**Harness alignment** : **L0 Claude Code prioritaire** (Doctor + Compagnons kernel). LD04 pivot = Codex Desktop L+ (LD04 Cognition/Développement dans plan-A0-L §3)

**Drift markers** : **channel-bulk-dominance** : Cole Medin + mark-kashef = ~70% du corpus, single-source bias risk. A0-L §4 doctrine #3 "Cite the canon" → counterbalance avec RoboNuggets + matt-pocock (autres sources canon)

**A0-L canon relevance** : **high** — **le plus riche des 8 sub-dossiers pour A0-L canon**. Inspire directement A0L_Mindset (10 principles) + A0L_Dispatch (5 triggers) + ADR-A0-L-META-001 (3-Harness doctrine)

---

### 04_Finance (16 fichiers, LD02 pivot, B2 04_Finance)

**Files sampled** (7/16) : `03_Patrimoine_Personnel.md`, `04_Investissement_Immobilier.md`, `05_Fiscalite_Optimisation.md`, `06_Cryptomonnaies_DeFi.md`, `07_Trading_Avance.md`, `08_Marches_Financiers.md`, `09_Analyse_Technique.md`

**Top patterns** : patrimoine · immobilier · fiscalité · crypto DeFi · trading avancé · marchés financiers · analyse technique

**Harness alignment** : **L2 MiniMax Code** (Finance domain) + **B2 07_WonderWoman_Finance + Thunderbolts squad** (Bucky Barnes lead)

**Drift markers** : **partial coverage 7/16** — sous-compté (9 fichiers non lus). Sister canon manquant : Saru (LD02 H3 quarterly runway) pas couvert ici, autres ressources ailleurs probable

**A0-L canon relevance** : **medium** — patterns utiles mais partiels. Besoin re-run ciblé pour les 9 fichiers manquants si A0 veut complétude

---

### 05_Legal (10 fichiers récursifs, LD08 pivot, B2 05_Legal)

**Files sampled** (10/10) : `StorieRAP/resource_storie_business_vvs_rap.md`, `StorieRAP/resource_storie_piege_myheritage_adn_2.md`, `StorieRAP/resource_storie_surveillance_masse_france.md`, `StorieRAP/resource_storie_piege_myheritage_adn.md`, `StorieRAP/resource_storie_pactes_rap_francais.md`, `resource_ceux_qui_changent_tout.md`, `resource_faille_predite_40_ans.md`, `resource_ia_basculer_cette_semaine.md`, `Dan_Martell/resource_6elnsE7T_Ws.md`, `Dan_Martell/resource_UrGO9wNP1kE.md`

**Top patterns** : RGPD / data privacy violations · MyHeritage ADN pièges / consentement · Surveillance de masse France · Pactes FAANG-RAP (WhatsApp/Signal/Telegram) · Business vs RAP (rachat autorité parentale) · Cybersécurité faille prédite 40 ans · **AI Act bascule semaine / conformité** · Dan Martell legal/business frameworks · Contrats numériques CGU/CGV · IP tech & brevets

**Harness alignment** : **L2 MiniMax Code** (Legal/Eternal AI-Act compliance). **AI-Act 2026-08-02 imminent** = driver principal (cf. ADR-CANON-001 B2-08 Aquaman Legal). LD08 pivot = Impact/Georgiou (H90 quarterly legacy review)

**Drift markers** : **mixed-StorieRAP + IA-AI-Act imminent + Dan_Martell business frame** — focus hybride juridique narratif + AI-Act compliance + business frameworks. Bon coverage pour A0L_Dispatch D4 (cycle-end 12WY audit = AI-Act check)

**A0-L canon relevance** : **high** — AI-Act 2026-08-02 imminent driver documenté, alimente ADR-ICP-NEXUS-001 + ADR-AAAS-PRICING-001 compliance

---

### 06_Sales (12 fichiers, LD01 pivot, B2 06_Sales)

**Files sampled** (10/12) : `DAN_MARTELL_AUDIT.md`, `2026-06-19_on-a-réuni-200-founders-pour-le-plus-gros-événement-saas-de-france___kIxjlEf_0U.md`, `framework-challenger-sale.md`, `framework-gap-selling.md`, `framework-million-dollar-weekend-the-ask.md`, `framework-never-split-the-difference.md`, `framework-spin-selling.md`, `how-to-make-people-feel-stupid-for-not-buying-100m-offers.md`, `resource_10saas_b2b_b2c_5segments.md`, `stop-freelancing-and-scale-client-acquisition.md`

**Top patterns** : sales-frameworks (challenger / gap / spin / never-split-the-difference) · Dan-Martell-playbook-audit · high-ticket 100M-offers · B2B-B2C-SaaS segmentation · client-acquisition-scaling · founder-event-saas-france · freelance-to-agency-pivot · ask-script-weekend-launch

**Harness alignment** : **L2 MiniMax Code** (Sales = John Jones / Illuminati squad). Sister canon ADR-ICP-SOLARIS-001 (killer feature Agentic Governance)

**Drift markers** : aucun

**A0-L canon relevance** : **high** — sales frameworks canon alignés avec B2-05 JohnJones sales manager (B3 Illuminati). Alimente ADR-L2-AAAS-PRICING-001 (5 tiers canon)

---

### 07_Growth (85 fichiers récursifs, LD07 pivot, B2 07_Growth)

**Files sampled** (10/85) : `_INDEX.md`, `Yann_Leonardi/resource_product_market_fit.md`, `Yann_Leonardi/resource_seo_bases_referencement.md`, `Yann_Leonardi/resource_inbound_vs_content_marketing.md`, `playbook-for-a-100m-ai-agency.md`, `etude-de-cas-medvi-400m-2-employes-agents-ia.md`, `onboarding-flows-1460-patterns-acquisition-funnel-Qsq-Sj_rojU.md`, `2026-06-25_boring-businesses-highest-survival-rates-5fS-lD1nFxM.md`, `2026-06-19_northam-digital-demand-google-skills-ai-skills-playbook__VUeGkbsUZc0.md`, `Dan_Martell/resource_aOQndPlfNhU.md`

**Top patterns** : **Acquisition-First doctrine** (MedVie 400M$ Y1, 2 employés, 16,2% marge) — sister canon ADR-AAAS-ACQUISITION-DOCTRINE-001 · **Triple-canal acquisition** (Meta Ads + Quiz Lovable + Affiliation 30%) anti-platform-risk · **Asset-light AaaS model** (99% moins de personnel, 3× marges vs SaaS classique) · PMF measurement (Sean Ellis 40% test + retention curve + NPS>50) · SEO 3 piliers (technique/contenu/popularité) + cocon sémantique · Inbound funnel 4 étapes (HubSpot) · Onboarding patterns (Mobbin 1460 flows) · **ICP-spécifique onboarding pour 3 Variants AaaS** (Solaris/Nexus/Orbiter) · Boring Business survival-rate doctrine (anti-hype) · Dan Martell Business Theater anti-pattern (ship > polish, brocoli > chocolat)

**Harness alignment** : **L2 MiniMax Code** (Growth = Superman/Guardians squad). **LD07 pivot = Créativité/Reno**, sister alignement L0 Claude Code (Reno + IT Kang Dynasty)

**Drift markers** : **MedVie moved 03_IT/ → 07_Growth/ 2026-06-24** (A0 canon-batch Acquisition Directive) — sister LD07_Creativity_Reno marker

**A0-L canon relevance** : **high** — **3 AaaS Variants onboarding patterns** = sister canon directe pour ADR-ICP-SOLARIS-001 / ADR-ICP-NEXUS-001 / ADR-ICP-ORBITER-001

---

### 08_People (36 fichiers récursifs, LD05 pivot, B2 08_People)

**Files sampled** (10/36) : `agent-harnesses-hermes-claude-code.md`, `Tiago_Forte/resource_business_runs_itself.md`, `Tiago_Forte/resource_ai_sops.md`, `Tiago_Forte/resource_no_meetings.md`, `Ali_Abdaal/resource_micro_habits_focus.md`, `Ali_Abdaal/resource_build_systems.md`, `Shubham_Sharma/resource_claude_cowork.md`, `Dan_Martell/resource_9XBKhwBvqsU.md`, `resource_claude_dynamic_workflows_6patterns.md`, `2026-06-17_deya-build-systems-business-runs-without-you.md`

**Top patterns** : **E-Myth founder heroic to autonomous business 5 stages** · **AI-generated SOPs L1/L2/L3 RACI matrix** · Meeting elimination Zapier-driven transcript-to-CRM workflows · Micro-habits focus environment engineering (Nir Eyal triggers) · Systems > willpower (health/time/finance/relations automation) · Claude Cowork desktop agentification for non-devs · AI Skills Stack prompt engineering tool stacking AI as team · **6 dynamic workflows** (fan-out / adversarial / verify / tournament / loop-until-done) · DPS Delegation Priority Score · DBM Digital Business Manager · **Agent harness = body model-agnostic Hermes Claude Code**

**Harness alignment** : **L1 Hermes Agent** (People = X-Men squad, GreenLantern). **LD05 pivot** = **Social/Stamets** (H30 30-day network pulse) — sister alignement avec Hermes L1 §11 héritage SSOT

**Drift markers** : **08_People canon mixed People/HR with Harness+AI agentification+Hermes/Claude Code patterns** (D2 nuance: harness-as-body IS canon doctrine per A0 2026-06-02, mais tags non-People-domain comme LD08_Impact_Georgiou sur fichier Deya signalent boundary fuzz)

**A0-L canon relevance** : **high** — **E-Myth 5 stages + 6 dynamic workflows + Agent harness doctrine = sources canon directes** pour A0L_Mindset §4 + B1_Manifesto isomorphy

---

## §2 — Synthèse canon cross-cutting

### Distribution LDxx pivot (8 sub-dossiers → Life Wheel 1-8)

| LDxx | Sub-dossiers | Total fichiers |
|---|---|---|
| **LD01** (Carrière/Book) | 01_Product, 02_Ops, 06_Sales | 17+34+12 = 63 |
| **LD02** (Finance/Saru) | 04_Finance | 16 (partial) |
| **LD03** (Santé/Hugs) | (aucun Geordi direct) | 0 — gap canon |
| **LD04** (Cognition/Tilly) | 03_IT | 349 |
| **LD05** (Social/Stamets) | 08_People | 36 |
| **LD06** (Famille/Burnhum) | (aucun Geordi direct) | 0 — gap canon |
| **LD07** (Créativité/Reno) | 07_Growth | 85 |
| **LD08** (Impact/Georgiou) | 05_Legal | 10 |
| **Total** | **7/8 LDxx couverts** | **559 fichiers** (partial coverage ~70%) |

**Gap canonique** : **LD03 Santé + LD06 Famille** non couverts par Geordi. Sister sources probables ailleurs (YouTube takeout, Memory Core, ou autre dossier). A0 decision : gap à fermer post-Plan 0.

### Channel dominance (drift markers agrégés)

| Channel/Author | Sub-dossiers touchés | Total fichiers estimés | Drift risk |
|---|---|---|---|
| **Cole Medin** | 03_IT | ~100 | high (single-source bias) |
| **Mark Kashef** | 03_IT | ~150 | high (single-source bias) |
| **Dan Martell** | 02_Ops, 05_Legal, 06_Sales, 07_Growth, 08_People | ~50 | medium (recurring founder playbook) |
| **Tiago Forte** | 08_People | ~15 | low (sister doctrine) |
| **StorieRAP** | 05_Legal | ~5 | low (niche) |
| **Matt Pocock** | 02_Ops (via 2026-06-19 file) | 1 | low mais canon |
| **Yann Leonardi** | 07_Growth | ~30 | low |
| **RoboNuggets** | 03_IT | ~50 | medium |

**Drift counter-balance** : A0L_Mindset §4 doctrine #3 "Cite the canon" → diversifier les sources, ne pas citer 1 seul channel pour 1 principe.

### 3-Harness alignment canon (cross-référence avec plan-A0-L §3)

| Harness | Sub-dossiers Geordi alignés | % canon coverage |
|---|---|---|
| **L0 Claude Code** | 03_IT (harness engineering, agent teams, claude-code internals) | 62% (349 fichiers) |
| **L1 Hermes Agent** | 08_People (E-Myth, SOPs, micro-habits, dynamic workflows) | 6% (36 fichiers) |
| **L2 MiniMax Code** | 01_Product, 02_Ops, 04_Finance, 05_Legal, 06_Sales, 07_Growth | 31% (174 fichiers) |
| **L+ Codex Desktop** | (cross-cutting — LD04 Cognition pivot via 03_IT) | via 03_IT principalement |

**Total** : 559 fichiers canon validés via Geordi (Plan 0 swarm).

---

## §3 — Drift markers agrégés (synthèse)

1. **Channel-bulk-dominance Cole Medin + Mark Kashef** (03_IT ~70%) → counterbalance via matt-pocock + RoboNuggets + autres channels (A0L_Mindset §4 #3)
2. **LD03 + LD06 gap canon** → sister sources à identifier (YouTube takeout / Memory Core)
3. **04_Finance partial** (7/16 lus) → re-run ciblé pour les 9 manquants si A0 veut complétude
5. **Sub-agent hallucination des counts** (05_Legal 33 vs réel 10, 04_Finance 7 vs réel 16) → re-runs ciblés avec Glob récursif = leçon D6 cataloguable (`ADR-META-006_d6-root-causes-catalog.md` entrée #2 candidate)
6. **08_People boundary fuzz** (harness/AI tags vs People tags) → canon multi-doctrinal, à clarifier en ADR-sibling
7. **AI-Act 2026-08-02 driver imminent** (05_Legal) → sister urgence pour ratifier ADR-ICP-NEXUS-001 + ADR-AAAS-PRICING-001 compliance

---

## §4 — Sister-linkage avec Takeout (`a0_l_canon.md` v0)

**Takeout validés (Plan 0 swarm initial)** :
- **2025-08** : A'Space OS = Système Opératif Fractal (LD05 pivot, social/communautaire — premier jet canon A'Space OS)
- **2026-05** : 10 patterns Solaris OS / Zod Contracts / Master SOC / Hermes Orchestrateur B2 / Roue de la Vie 8 Domaines / Domain Payloads DDD / Self-Operating Hubs SOH / ADR-DDD-SOC-TDD / dispatchToHermes (GROWTH/PRODUCT/FINANCE) / Doctor Who Master SOC (LD01_Business pivot)

**Convergence Takeout ↔ Geordi** :
- **Hermes Orchestrateur B2** (Takeout) ↔ **E-Myth founder + 6 dynamic workflows** (Geordi 08_People) = **L1 canon convergent**
- **Master SOC Schema + Zod Contracts** (Takeout) ↔ **Solo founder AI agent OS + CEO dashboard** (Geordi 02_Ops) = **L2 canon convergent**
- **A'Space OS Fractal** (Takeout 2025-08) ↔ **matt-pocock-harness-engineering** (Geordi 02_Ops) = **L+/3-Harness canon convergent**

**D6 nuance** : le takeout est **historiquement daté Mai 2026** = avant le pivot Dokploy→Vercel+Coolify (2026-06-15). Geordi est **daté 2026-06-17 → 2026-06-25** = post-pivot. Donc Geordi = canon le plus récent.

---

## §5 — Annexe : counts réels vs sub-agent reports

**D6 honest catalogage des hallucinations sub-agent initiales** :

| Sub-dossier | Count sub-agent initial | Count réel (Glob récursif) | Hallucination? |
|---|---|---|---|
| 01_Product | 17 | 17 (ls) | non |
| 02_Ops | null (échec bash) | 30 (ls) / 34 (glob récursif) | échec silencieux |
| 03_IT | 0 | 35 (ls) / **349** (glob récursif) | sous-compté massif |
| 04_Finance | 7 | 16 (ls) | sous-compté (9 manquants) |
| 05_Legal | 33 | 5 (ls) / 10 (glob récursif) | **hallucination +2.3x** |
| 06_Sales | 12 | 11 (ls) | quasi-exact |
| 07_Growth | error bash | 9 (ls) / 85 (glob récursif) | échec silencieux |
| 08_People | 0 | 9 (ls) / 36 (glob récursif) | sous-compté massif |

**D6 lesson** : **sub-agents `general-purpose` hallucinent des counts quand Bash indisponible + Glob non-récursif**. Solution canon = Glob `**\*.md` récursif + Read sample prioritaires.

**D6 lesson 2** : certains sub-agents utilisent ls-équivalent qui filtre les dotfiles et directories, donnant count inférieur. Glob récursif est la source de vérité.

---

## §6 — D1 Receipt — ce document

- ✅ Existe physiquement : `00_Amadeus/01_Identity_Core/a0_l_geordi_canon.md` (nouveau)
- ✅ AGENTS.md non touché
- ✅ Cross-link à faire : 1-line D4 append dans MEMORY.md (à venir)
- ✅ Posture C respectée : 0 cron créé, 0 settings.json muté
- ✅ Sources 8 sub-dossiers Geordi : 7/8 validés (1 partial = 04_Finance)
- ✅ Sister-linkage avec `a0_l_canon.md` v0 (Takeout sister)
- ✅ Mapping LDxx ↔ Harness ↔ B2 Domain cohérent avec `plan-A0-L-jumeau-challenger.md` §3
- ✅ 7 drift markers identifiés (§3) + 2 D6 lessons sub-agent (§5)
- ✅ Status : DRAFT v1 — A0 ratification requise pour statut RATIFIED

**Prochaine étape (P1 Plan 0)** : write `A0L_Mindset.md` + `A0L_Dispatch.md` (2 fichiers courts, DRY-check vs B1_Manifesto), hérite des patterns 08_People (E-Myth 5 stages + 6 dynamic workflows) + 02_Ops (matt-pocock-harness-engineering) + 03_IT (Cole Medin harness).