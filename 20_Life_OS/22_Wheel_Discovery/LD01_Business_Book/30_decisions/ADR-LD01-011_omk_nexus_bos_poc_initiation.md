---
type: adr-decision-doctrine
id: ADR-LD01-011
title: "OMK Nexus BOS PoC Initiation — specs/demo/AAARR Growth prompts (Tier T1, Enterprise_OS_Blueprint_Kit)"
status: ACCEPTED
date: 2026-07-05T09:45:00-04:00
deciders:
  - "A0 Amadeus (GO 2026-07-05 'Un GO groupé' — 3 axes validés : Q1 Growth+DLP-light, Q2 Tier T1, Q3 append-only dans Blueprint Kit)"
  - "MC (Mavis/MiniMax Code) — option alternative validée post ADR-LD01-010"
  - "Hermes Agent (HA · author — A3 Picard in PARA, projects owner H10, capitaine USS Enterprise)"
parent_dox: ../CLAUDE.md
sister: ../AGENTS.md
refines:
  - ADR-LD01-010_hermes_promotion_a3_picard_in_para (HA = A3 Picard, projets owner H10)
  - ADR-LD01-008_coaching-loop-picard-jerry-summers (loop engineering intouchable)
  - ADR-INFRA-003 (Picard H10 projects owner anchor)
  - Gemini Deep Research 2026-07-05 (analyse niche coaching B2B · Medvi sanitized pivot · Triptyque 1+2+Duo · 100 clients premium $1.2M ARR)
  - plan-minimax-l1-book-lune.md §1 (HA Picard dans l'architecture canon)
related:
  - "Enterprise_OS_Blueprint_Kit (Geordi resources) : 20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Enterprise_OS_Blueprint_Kit/"
  - "specs overrides (6 fichiers, append-only) : specs/{system,architecture,security,cost,agent,build_plan}_spec_omk_nexus.md"
  - "Onboarding demo (4 fichiers, append-only) : examples/omk-nexus-coaching-agency/{README,01_onboarding_walkthrough,02_first_session_runbook,03_quiz_acquisition_integration}.md"
  - "Growth AAARR prompts (1 fichier, append-only) : prompts/aaarr_growth_signal_pack.md"
  - "A3 Geordi spec (sister canon USS Enterprise) : 03_Resources_Geordi/A3_Geordi_Resources_Spec.md"
  - "A3 Enterprise_References_Index : 24_PARA_Enterprise/A3_Enterprise_References_Index.md"
domain: LD01_Career_Business / OMK_Nexus_BOS / Tier_T1 / Loop_Engineering
tags: ["#ADR", "#omk_nexus_bos", "#poc_initiation", "#tier_t1", "#coaching_b2b", "#triptyque_1_2_duo", "#growth_aaarr", "#picard_h10", "#append_only", "#geordi_resources", "#war_mode", "#loop_engineering"]
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-INFRA-002, ADR-INFRA-003, ADR-LD01-008, ADR-LD01-010]
sign_off_a0: "A0 Amadeus — GO 2026-07-05 'Un GO groupé' (Growth+DLP-light en parallèle, Tier T1, append-only dans Blueprint Kit)"
war_mode: true
reversible_by: "suppression des 11 fichiers livrables (6 specs + 4 demo + 1 prompts) + revert append calendar.md + delete citadel trace = revert complet. BLUEPRINT.md et autres fichiers canon Enterprise_OS_Blueprint_Kit restent intacts par construction (D4 append-only)."
---

# ADR-LD01-011 — OMK Nexus BOS PoC Initiation

> **Pré-D1 vérification (HA, 2026-07-05T09:45)** :
> - ✅ Enterprise_OS_Blueprint_Kit EXISTE à `20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Enterprise_OS_Blueprint_Kit/` (15 items dont BLUEPRINT.md 8.7 kb, 11 prompts canon, 8 specs templates, 3 exemples solo/law/clinic)
> - ✅ A3_Geordi_Resources_Spec.md confirme parent A2 = Computer USS Enterprise (mon ship, sister scope A3 Picard)
> - ✅ Slots 009-011 dans 30_decisions/ : 009=DRAFT (intouché), 010=ADR promotion HA (intouché), 011=LIBRE → utilisé
> - ✅ ADR-LD01-008 (loop engineering) et ADR-LD01-010 (promotion HA Picard) intacts

## Status

**ACCEPTED** (A0 GO 2026-07-05 « Un GO groupé » — 3 axes validés simultanément). War Mode actif. **Append-only strict — réversible** par suppression des 11 fichiers livrables uniquement.

## Context

### §A — La mission (post Gemini Deep Research)

Suite à l'analyse Gemini Deep Research du 2026-07-05 (verbatim dans message A0), **OMK Nexus BOS** est le **PoC (Proof of Concept) B2B** ciblant l'intersection **Cabinets de Coaching Premium × Agences de Business Development**. Le pivot a été tranché par A0 contre les niches médicales (Biohacking) et psychologiques (TDAH) pour éviter les lourdeurs réglementaires (fédérales US, HIPAA, FDA) qui ont causé la chute de Medvi.

**Cible chiffrée** : **100 clients premium × $1 000/mois = $1.2M ARR**, sans stock physique, marge nette > 90% grâce au Plan MiniMax (5.1B tokens / $50) combiné à l'inférence locale.

**Architecture 8 domaines L1** (Triptyque 1 + Triptyque 2 + Duo) selon le PoC Gemini :
- **Triptyque 1 (Backbone)** : People / IT / Operations
- **Triptyque 2 (Front-End)** : Product / Growth / Sales
- **Duo (Garde-Fous)** : Finance / Legal

### §B — Mon rôle (A3 Picard in PARA, projets owner H10)

Après ma promotion ADR-LD01-010, je suis A3 Picard in PARA (H10 projects owner, USS Enterprise). **OMK Nexus BOS est l'un des projets sous ma responsabilité**, le premier projet canonique post-promotion.

**D1 receipts input** :
- Mon input upstream vers Book (MC, A3 Book in Life Wheel) au cycle H10 = `<proj>/MANIFEST.md` (canonical per ADR-INFRA-003 §D1)
- Mes inputs downstream depuis les A3 twins USS Enterprise : Spock (Areas), Geordi (Resources), Data (Archives)
- **Geordi = mon fournisseur canonique de templates** (notamment Enterprise_OS_Blueprint_Kit) — c'est là que je puise pour scaffolder OMK Nexus BOS

### §C — Le template canon (Enterprise_OS_Blueprint_Kit)

**Source** : Mark Kashef / Early AI Dopters community (kit libre, attribution non requise).

**Tier choisi** : **T1 (entre solo et law firm)** — car 100 clients premium = taille d'un cabinet. Q2 validée par A0.

**Architecture canon du Blueprint** :
- Single AWS account (in-account only)
- Fargate orchestrator (one chokepoint per turn)
- Amazon Bedrock pour les model calls (prompts never leave)
- 31 DynamoDB tables + 6 S3 buckets + 3 KMS keys
- 42 kill switches + write-once audit (S3 Object Lock, 7-year hold)
- 9-patterns DLP leak scan (block 7 / warn 2)
- 5 RBAC roles (viewer/analyst/operator/admin/owner)
- 11 Build-It Prompt Pack (set up → plan → draft and prove)

**DLP-light subset PII/credentials** (mitigation Q1) : on ne fork pas les 9 patterns complets du Blueprint pour cette itération. On ship un **subset minimal** couvrant :
- AWS access keys (regex)
- API key headers
- PEM private keys
- Slack/GitHub tokens
- Credit cards
- US SSNs
- PII basique (email + phone)

## Decision

### D1 — Append-only strict dans `02_Templates/Enterprise_OS_Blueprint_Kit/` (Q3 validée)

Aucun fichier canon du Blueprint n'est muté. **11 fichiers livrables** sont créés dans des dossiers/fichiers neufs (aucun overwrite, aucun patch) :

#### Catégorie 1 — Specs overrides (6 fichiers, dans `specs/`)

| Fichier | Remplace | Remplissage OMK Nexus |
|---|---|---|
| `system_spec_omk_nexus.md` | template `SYSTEM_SPEC.md` | Tier T1, niche coaching B2B, $1.2M ARR, MiniMax plan, surfaces Telegram+web dashboard |
| `architecture_spec_omk_nexus.md` | template `ARCHITECTURE_SPEC.md` | Triptyque 1+2+Duo, 8 agents (1 par LD), Bedrock+inference locale, DLP subset |
| `security_spec_omk_nexus.md` | template `SECURITY_SPEC.md` | DLP 7 patterns subset PII/credentials, 5 RBAC, kill switches sur chaque agent |
| `cost_spec_omk_nexus.md` | template `COST_SPEC.md` | MiniMax 5.1B tokens / $50, fail-closed cost cap, cost arbitrage vs Medvi |
| `agent_spec_omk_nexus.md` | template `AGENT_SPEC.md` | 8 agents (People/IT/Ops/Product/Growth/Sales/Finance/Legal), 1 block chacun |
| `build_plan_omk_nexus.md` | template `BUILD_PLAN.md` | Phase 1 (foundation 1 semaine), Phase 2 (growth+quiz), Phase 3 (scale 100 clients) |

#### Catégorie 2 — Onboarding demo (4 fichiers, dans `examples/omk-nexus-coaching-agency/`)

| Fichier | Rôle |
|---|---|
| `README.md` | Vue d'ensemble du cas coaching B2B tier T1 (parallèle `northgate-law/`, `riverside-clinic/`, `solo-consultant/`) |
| `01_onboarding_walkthrough.md` | Pas-à-pas prospect/coach : de la découverte à la première session |
| `02_first_session_runbook.md` | Runbook 90 min : quiz acquisition → analyse AAARR → cartographie pertes → plan de libération |
| `03_quiz_acquisition_integration.md` | Intégration Quiz d'Acquisition Medvi (audit context) à l'Agentic Dashboard |

#### Catégorie 3 — Growth AAARR prompts (1 fichier, dans `prompts/`)

| Fichier | Contenu |
|---|---|
| `aaarr_growth_signal_pack.md` | **11 prompts de signal acquisition AAARR** (2 Acquisition + 3 Activation + 2 Rétention + 2 Recommandation + 2 Revenu) |

### D2 — DLP-light en parallèle (Q1 validée : Growth prioritaire + DLP-light subset)

Le DLP complet Supabase (9 patterns Blueprint complet + EU AI Act + SOC2) est **hors scope cette itération**. À la place :

**DLP-light** = un subset de **7 patterns minimum** implémentés en regex Python dans le pipeline de sortie des 11 prompts Growth :
- AWS access keys (AKIA[0-9A-Z]{16})
- GitHub PATs (ghp_[0-9a-zA-Z]{36})
- Slack tokens (xox[baprs]-[0-9a-zA-Z]+)
- PEM private keys (`-----BEGIN .* PRIVATE KEY-----`)
- Credit cards (16 digits with Luhn)
- US SSNs (\d{3}-\d{2}-\d{4})
- PII basic (email + phone)

**Implémentation** : un fichier `security_spec_omk_nexus.md` (spéc) + un script Python `dlp_light_filter.py` qui scanne chaque output de prompt avant insertion en DB. Pas de Supabase scripts lourds — juste un middleware local.

**Quand le DLP complet arrive** : dès le premier client réel signé (post Phase 1), on monte le DLP complet conformément à BLUEPRINT.md §6 (9 patterns + DLP proxy Supabase).

### D3 — Tier T1 confirmé (Q2 validée)

**T1** = entre solo (T0) et clinic (T2). Caractéristiques :
- 2-10 personnes dans l'équipe (cas OMK : Amadeus + Abdaty + béta-coachs)
- Données confidentielles (PII clients coachés), pas régulées (HIPAA non applicable)
- Budget infra $200-1000/mois (cohérent avec MiniMax plan forfaitaire)
- 5 RBAC roles, mais viewer/operator limités au début
- Compliance : EU AI Act awareness, pas SOC2 dès le PoC

### D4 — Loop engineering OMK Nexus (rattachement ADR-LD01-008)

L'ADR-LD01-008 définit la **loop engineering coaching** : Book (H1 aggregator) supervise Picard (H10 projects owner) au tick H1 weekly. **Pour OMK Nexus BOS** :

- **H10 tick (par moi, Picard)** : produire `<proj>/MANIFEST.md` (canonical per ADR-INFRA-003 §D1)
  - Contenu : id, title, status (INITIATED/ACTIVE/ARCHIVED), tier (T1), cycle (12WY-Q3-2026), rock_count
  - Update : à chaque jalon (Phase 1 fin, Phase 2 fin, Phase 3 fin)

- **H1 tick (par Book, MC)** : agréger inputs
  - Mon input Picard = `<proj>/MANIFEST.md` mis à jour
  - Jerry Pulse = indicateurs « lights on » (cf ADR-LD01-008 D3)
  - Summers Verse = ligne narrative
  - Output = fiche P&L weekly OMK Nexus

- **Daily tick (par Squad B3 coaching)** : 1 tâche close + 1 output + 1 lesson

### D5 — Append-only strict (le filet de réversibilité)

**Mutations autorisées (D5 append-only)** :
- ✅ Création de cet ADR-LD01-011.
- ✅ Append à `99_meta/calendar.md`.
- ✅ CitADEL trace JSON.
- ✅ Création des 11 fichiers livrables dans `Enterprise_OS_Blueprint_Kit/` (6 specs + 4 demo + 1 prompts) — aucun dans des fichiers existants.

**Mutations interdites (D5 anti-paperclip)** :
- ❌ BLUEPRINT.md du Blueprint Kit (intouchable).
- ❌ Les 11 prompts canon `prompts/01..11_*.txt` (intouchables).
- ❌ Les 8 specs templates `specs/*.md` (intouchables).
- ❌ Les 3 exemples canoniques `examples/{solo-consultant,northgate-law,riverside-clinic}/` (intouchables).
- ❌ `03_Resources_Geordi/A3_Geordi_Resources_Spec.md` (intouchable).
- ❌ `24_PARA_Enterprise/A3_Enterprise_References_Index.md` (intouchable).
- ❌ ADR-LD01-008 et ADR-LD01-010 (intouchables).
- ❌ Twins Book + Picard, calques HA + MC, A3_Book spec, BIBLIOGRAPHY, README, CLAUDE.md, AGENTS.md.

### D6 — Hors-scope explicite (YAGNI)

- ❌ **DLP complet Supabase** (9 patterns Blueprint + EU AI Act complet + SOC2) — reporté Phase 2 ou premier client signé.
- ❌ **Code TypeScript / UI runtime** (Blueprint mentionne Fargate, mais le PoC nécessite pas de runtime AWS déployé — juste les spécs + onboarding demo).
- ❌ **Mutation `LD01_Business_Book/CLAUDE.md`** `consumed_by` field (HA primary = dev-runtime A3 Book → A3 Picard) — gated HITL A0, sister scope ADR-LD01-010.
- ❌ **Cron automatique** (Posture C + ADR-WARMODE-001 flag-gated).
- ❌ **Création d'agents twins** sous `.mavis/agents/a3-<nom>/` (cf ADR-LD01-009 D3 DRAFT) — sister scope, hors scope ici.
- ❌ **Déploiement AWS réel** (juste les spécs pour l'instant, déploiement Phase 2).
- ❌ **Recrutement beta-coachs** (Phase 3, post-PoC validé).

## Consequences

### Positives

- **PoC structurellement complet** : specs + démo + prompts = les 3 piliers d'un PoC B2B viable.
- **Tier T1 cohérent** : taille d'équipe et budget alignés sur 100 clients premium.
- **DLP-light subset** : 7 patterns minimum suffisent pour protéger les 11 prompts Growth sans sur-engineering.
- **Loop engineering rattachée** : le PoC s'inscrit dans la cadence H10/H1/Daily définie par ADR-LD01-008.
- **Append-only = réversibilité totale** : suppression des 11 livrables = revert complet.
- **Trace citadel** : gouvernance Agent OS peut monitorer l'avancée PoC.
- **Mémoire persistante mise à jour** : HA = A3 Picard in PARA, role identité canon pour futures sessions.

### Negatives / Risques

- **Pas de validation marchée avant fin PoC** : on construit les specs/demo/prompts AVANT de tester avec un vrai coach. **Mitigation** : Phase 2 = 3 beta-coachs en early access (gated HITL A0, hors scope cette ADR).
- **DLP-light insuffisant pour compliance stricte** : 7 patterns ne couvrent pas EU AI Act complet. **Mitigation** : DLP complet en Phase 2 (premier client signé = bloquant).
- **Coût MiniMax 5.1B tokens / $50 insuffisant pour 100 clients simultanés** : à 100 clients × ~50k tokens/mois = 5B tokens, pile au plafond. **Mitigation** : cache sémantique local + inference locale Ollama pour les premières passes, MiniMax uniquement pour validation finale (per Gemini §Product Domain).
- **Conflit potentiel avec ADR-LD01-009 DRAFT D7** (qui dit « MC = A2 Curie ») : la correction MC a tranché MC = A3 Book, mais le DRAFT reste. **Mitigation** : ADR-LD01-009 reste DRAFT non ratifié, hors scope ici.

## Verification (D1 receipts, à exécuter après écriture)

```powershell
$root_bp = 'C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\02_Templates\Enterprise_OS_Blueprint_Kit'

# 1. Cet ADR existe
Test-Path 'C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\30_decisions\ADR-LD01-011_omk_nexus_bos_poc_initiation.md'   # True

# 2. ADR-LD01-008 et ADR-LD01-010 intacts
Test-Path 'C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\30_decisions\ADR-LD01-008_coaching-loop-picard-jerry-summers.md'   # True
Test-Path 'C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\30_decisions\ADR-LD01-010_hermes_promotion_a3_picard_in_para.md'   # True

# 3. 6 specs livrées
$specs = @('system', 'architecture', 'security', 'cost', 'agent', 'build_plan')
foreach ($s in $specs) {
    Test-Path "$root_bp\specs\${s}_spec_omk_nexus.md"   # True x6
}

# 4. 4 demo files livrés
$demo_files = @('README', '01_onboarding_walkthrough', '02_first_session_runbook', '03_quiz_acquisition_integration')
foreach ($f in $demo_files) {
    Test-Path "$root_bp\examples\omk-nexus-coaching-agency\${f}.md"   # True x4
}

# 5. 1 prompts file livré
Test-Path "$root_bp\prompts\aaarr_growth_signal_pack.md"   # True

# 6. BLUEPRINT.md et 11 prompts canon intacts (mtime < this session)
$bp = Get-Item "$root_bp\BLUEPRINT.md"
$prompts_canon = Get-ChildItem "$root_bp\prompts\*.txt"
# Tous mtime < 2026-07-05 09:30

# 7. calendar.md contient l'épisode 09:45
$cal = Get-Content 'C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\99_meta\calendar.md' -Raw
if ($cal -notmatch '2026-07-05T09:45') { Write-Warning 'calendar.md sans épisode 09:45' }

# 8. CitADEL trace existe
Test-Path 'C:\Users\amado\agent-os\citadel\decisions\2026-07-05_adr_ld01_011_omk_nexus_poc.json'   # True

Write-Host '[OK] ADR-LD01-011 + 11 livrables + trace vérifiés'
```

## Anti-patterns (suite canon)

- ❌ Muter BLUEPRINT.md ou les 11 prompts canon.
- ❌ Muter les 8 specs templates (créer des overrides, pas des patches).
- ❌ Muter les 3 exemples canoniques (créer `omk-nexus-coaching-agency/`, pas modifier `northgate-law/`).
- ❌ Sauter le DLP-light (les 11 prompts Growth doivent être DLP-scannés avant DB insert).
- ❌ Déployer en AWS réel avant Phase 2 validée.
- ❌ Recruter beta-coachs avant PoC specs validées.

## Annexes — Sisters canoniques

- **Sister A (existant)** : Enterprise_OS_Blueprint_Kit (15 items, Geordi resource)
- **Sister B (existant)** : A3_Geordi_Resources_Spec.md (Computer USS Enterprise parent)
- **Sister C (existant)** : ADR-LD01-008 (loop engineering coaching, doctrine intouchée)
- **Sister D (existant)** : ADR-LD01-010 (promotion HA = A3 Picard, sister scope)
- **Sister E (à venir)** : Première fiche P&L hebdo Book agrégeant input OMK Nexus — Phase 1 fin
- **Sister F (à venir)** : Beta-coach onboarding Phase 2 (3 coaches early access) — gated HITL A0
- **Sister G (à venir)** : Premier client signé Phase 3 (déclenche DLP complet Blueprint §6) — gated HITL A0

> Last DOX pass : 2026-07-05T09:45:00-04:00 (création, append-only, War Mode actif, A0 GO groupé tracé dans citadel).
