---
id: SIDEBAR_V2_OMK_SAAS_OS_NEXUS_FORK
title: Sidebar V2 — OMK SaaS OS Vercel.app — Reconstitution NEXUS fork
date: 2026-07-03T16:42 ET
author: Mavis/MC (A3 Book) sur instruction A+ Amadeus — analyse post-screenshots Mark (ClaudeClaw Enterprise) + Blueprint Kit + Solaris calque + NEXUS fork
status: DRAFT — await GO A0 (post-pricing + post-Go 3/4)
doctrine: D6 no-copy · D4 append-only · never break existing OMK template · Filiales → Domain Pages NOT sidebar
preserves: existing OMK Digital Garden Cultivate/Nurture/Bloom/Roots · 14 views · Sidebar.tsx · ORM/Pages.tsx
sister_canon:
  - plan-minimax-l1-book-lune/04_organigramme-doctrine/  (placeholder)
  - plan-L2-business-os.md §5.4 (Filiales architecture)
  - plan-L2-business-os.md §13.4 (Coach spearhead)
  - ADR-L2-AAAS-001 (3 variants AaaS canon)
  - ADR-CORE-006 RATIFIED 2026-07-03T14:38
  - _ROSTER.md canon 35 A3
---

# Sidebar V2 — OMK SaaS OS NEXUS fork — reconstitution

> **Sources analysées** :
> 1. **`Enterprise_OS_Blueprint_Kit`** (Mark Kashef + Early AI Dopters) — 15 fichiers racine, 8 specs, 11 prompts, 3 examples (northgate-law / riverside-clinic / solo-consultant). Doctrine AWS-vendor, mais structure inspiration.
> 2. **Mark's ClaudeClaw Enterprise** (9 screenshots ClaudeClaw Enterprise : Dashboard, Agents/Memories, Jarvis, Sessions, Audit Log, Kill Switches, Compliance SOC 2/HIPAA, ASCII architecture, Knowledge Base/Vectors) — sidebar CORE/OPS/SECURITY/ADVANCED/COLLABORATION/TEAM/ACCOUNT, plus arborescences d'intégrations (Memory DB / Slack Tools / Salesforce / Bedrock Image/Doc Gen / Hive Mind).
> 3. **`Solaris`** (`30_Business_OS/10_Projects/solaris/apps/dashboard/`) — Sidebar.tsx 149 lignes avec sections Cultivate/Nurture/Bloom/Roots, 12 views dont AiPanel + Sales + Growth + Marketplace, repos clients/tasks/legal/growth, supabase migrations.
> 4. **OMK SaaS OS** (`30_Business_OS/10_Projects/omk/apps/dashboard/`) — Sidebar.tsx 204 lignes avec sections CULTIVATE/NURTURE/BLOOM/ROOTS, **14 views** (Dashboard/Finance/People/Clients/Documents/SOP Library/Tasks/AI Agents Network/Growth/Sales Sanctum/Marketplace/IT & Data/Legal/Settings + ClientDetailView), auth/, data/, lib/, Vite+React.
> 5. **`plan-L2-business-os.md §5.4 Filiales par ICP`** = topologie hybride Holding → Filiales, chaque Filiale = sous-ensemble Jerry lean (Cyborg+GreenLantern pour Coach, etc.)

---

## 1. Architecture d'ensemble (vue méta)

```
HOME (Holding OMK)                  SIDEBAR Settings (per-user)         FILIALES (per-ICP)
─────────────────────                ────────────────────────────         ───────────────────────
CULTIVATE/NURTURE/BLOOM/ROOTS        Mark-style arborescences      Coach / EC / Avocat / Médical
(pages existants OMK)               (CORE/OPS/SECURITY/...)        (deploys séparés,
14 views + Sidebar.tsx              activables par Settings)       matrice lean par domaine)
                                    + Sidebar customization
                                    + Filiales switcher
```

**Règle d'or V2** : **`Home` (Holding) ≠ `Settings` (per-user) ≠ `Filiales` (per-ICP deploy)**. Les 3 sont cloisonnés. Mark's sidebar vit dans **Settings** parce qu'il est personnel + arborescent. Filiales déploient des instances dédiées par ICP.

---

## 2. État actuel — OMK SaaS OS Sidebar (cultivate/Nurture/Bloom/Roots)

Source : `30_Business_OS/10_Projects/omk/apps/dashboard/src/components/Sidebar.tsx` (204 lignes).

| Groupe | Liens | Logique |
|---|---|---|
| **CULTIVATE** | Dashboard · Finance · People | "Ce que je cultive" |
| **NURTURE** | Clients · Knowledge · SOP Library · Tasks | "Ce que je nourris" |
| **BLOOM** | AI Agents Network · Growth · Sales Sanctum · Marketplace | "Ce qui fleurit" |
| **ROOTS** | Legal · IT & Data · Settings | "Ce qui ancre" |

➡️ **Verdict** : culture jardin digital bien établie, **14 views** déjà développées. OMK devance Solaris sur la richesse des views (14 vs 12). Ce qui manque : **(a)** la profondeur arborescente Mark-style, **(b)** le regroupement Triptyque 1/Triptyque 2/Duo canon, **(c)** le cloisonnement Home/Settings/Filiales.

---

## 3. État Mark — ClaudeClaw Enterprise (9 screenshots)

Source : 9 PNG `C:\Users\amado\.mavis\uploads\` (OMK dashboard + 8x ClaudeClaw Enterprise).

| Section | Items | Notes |
|---|---|---|
| **CORE** | Overview · Agents · Chat · Playground · Jarvis | Le "cerveau" agentique |
| **OPERATIONS** | Sessions · Usage · Cost · Audit Log | Runtime operations |
| **SECURITY** | Kill Switches · DLP & Exfil · Panic · Rate Limits · Security Posture · Compliance · Alerting + **Agent Behavior** (memory writes/ingest/consolidation/context v2 disabled · hooks · skills · sessions frozen · jarvis voice disabled) | Runtime guards, **clauses à revisiter** (cf. infra) |
| **ADVANCED** | Knowledge · Missions · Memories · Hive Mind · Scheduled · Integrations | Arborescences Mark (le plus profond) |
| **COLLABORATION** | War Room | Module humain |
| **TEAM** | Members | RH agentique |
| **ACCOUNT** | Settings | Per-user |

**Mark's diagram ASCII (screenshot #8)** montre la topologie runtime :
```
You (Telegram/Slack) → Orchestrator → main(me)/ops/research → Memory DB / Slack Tools / Salesforce / Bedrock Image/Doc Gen
                                                              ↘ Hive Mind (shared DB)
```
Cette topologie correspond exactement à mon A1/A2/A3 canon : A1 (Gatekeeper) → A2/A3 (symphony crews) → Hive Mind / Memory / Integrations.

**Compliance page (screenshot #7)** montre la granularité :
- SOC 2 72% (9 controls scored : 0 Gap, 5 Partial, 4 Met, 1 Unknown, 2 Manual)
- HIPAA 63%
- AICPA 2017 Trust Services Criteria (Security, Availability, Confidentiality) scoré contre live AWS posture
- Drill-down par sous-critère (CC6.1 data-at-rest, CC6.3 least-privilege IAM, CC7 network protection)

**ASCII reconstitué au-delà des screenshots (Mark-side logic + Blueprint Kit + Hermes)** :

| Sous-menu reconstitué | Sub-pages inférées | Sister canon |
|---|---|---|
| Agents | Main agent / Ops / Research + System Prompt · Chat · Sessions · Usage · Memories (B.1·B.2·B.3) · Connections · Settings | ASCII diagram screenshot #8 |
| Sessions | 50 conversations · Preview · Channel · Agent · Messages · Duration · Last Active · Model (filter/group) | screenshot #3 |
| Audit Log | 200 events / 7 days · Search by actor/action/agent · TIME · ACTOR · ACTION · AGENT · SURFACE · DETAILS · cost | screenshot #4 |
| Kill Switches | Block all tool dispatch · Granular alias for tool_use · Bypass Bedrock guard · PII redaction · Exfil guard · Custom patterns · Panic · Rate limits · Security posture · Compliance | screenshot #5+#6 |
| Compliance | SOC 2 · HIPAA · CC6.1 · CC6.3 · CC7 · Latest guidance · Fix recommendations | screenshot #7 |
| Knowledge Base | Default scope (0 docs, 0 chunks) · Test retrieval · Test with a model (multi-LLM : Claude Opus, GPT-OSS 120B, DeepSeek V3.2, Qwen3 32B, Kimi K2.5, Mistral, Llama 3 8B) · Drag & drop upload · Compare · Chat | screenshot #9 |
| Missions | Long-term memories · Mem 0 strategy · Hive Mind · Scheduled tasks · Integrations · War Room · Members | inféré |
| Memories | importance: 70 · ingest · chat/slack/salesforce/crm captures · date · 5-tuple hash · auto-ingest behavior | screenshot #2 |

---

## 4. Proposition Sidebar V2 — OMK SaaS OS NEXUS fork

### Vue d'ensemble — 3 couches cloisonnées

```
┌────────────────────────────────────────────────────────────────────────┐
│                    OMK SaaS OS Vercel — Home                          │
│         (Holding = pages existantes DIGITAL GARDEN)                   │
│  Sidebar Shell (Sidebar.tsx) → 4 sections canon CULTIVATE/NURTURE/    │
│  BLOOM/ROOTS + 14 views existantes                                  │
└────────────────────────────────────────────────────────────────────────┘
                                  ↓ clic "Settings" (route /settings)
┌────────────────────────────────────────────────────────────────────────┐
│                     OMK SaaS OS — Settings                           │
│      (per-user, Mark-style arborescences VIENTENT ici)            │
│  Tabs : Profile · Sidebar Custom · Integrations · Security ·       │
│         Compliance · Knowledge Base · Filiales · Workspace          │
└────────────────────────────────────────────────────────────────────────┘
                                  ↓ clic "Filiales" (route /filiales)
┌────────────────────────────────────────────────────────────────────────┐
│                  OMK SaaS OS — Filiales                              │
│     (per-ICP deploys §5.4 plan L2, pas dans Sidebar)             │
│  Coach · EC · Avocat · Médical · Family-Office = 5 templates        │
└────────────────────────────────────────────────────────────────────────┘
```

### Sidebar V2 — `Sidebar.tsx` Home (Holding) — restructuration en Triptyque 1+2+Duo **sans rien casser**

**CURRENT** = 14 vues sur 4 sections = CULTIVATE/NURTURE/BLOOM/ROOTS (Digital Garden metaphor conservé).

**PROPOSED V2** = **regroupement en Triptyque 1 / Triptyque 2 / Duo** dans **les mêmes 4 sections** du Digital Garden = **préserve l'esthétique Solaris + calque la doctrine B1/B2/B3 sans casser UI**.

| Section (Digital Garden) | Triptyque canon | Items | Justification |
|---|---|---|---|
| **🌱 CULTIVATE** (Triptyque 1 = fondation) | foundation | Dashboard · **People/Agents** · Operations/Knowledge · **IT Software Kernel** | Regroupe People + AI Agents Network → People/Agents ; Knowledge + SOP Library → Operations/Knowledge ; IT & Data → IT Software Kernel |
| **🌿 NURTURE** (care quotidien) | day-to-day | Clients · Tasks · Documents | Inchangés, courant Solaris |
| **🌸 BLOOM** (Triptyque 2 = GTM) | go-to-market | **Product** (NEW view) · Growth · Sales Sanctum | Ajoute **Product** manquant — c'est l'angle mort Triptyque 2 aujourd'hui |
| **🌳 ROOTS** (Duo = garde-fous) | guard-rails | **Finance** · **Legal** · Marketplace | Regroupe Finance + Legal = Duo canon ; Marketplace = Tier 3 multi-associés |

**4 nouveaux fichiers views à créer** (manquant actuellement) :
1. `src/components/views/PeopleAgentsView.tsx` — fusion People + AI Agents Network
2. `src/components/views/OperationsKnowledgeView.tsx` — fusion Knowledge + SOP Library
3. `src/components/views/ItSoftwareKernelView.tsx` — étendu IT & Data avec souveraineté local
4. `src/components/views/ProductView.tsx` — Triptyque 2 obligatoire

⚠️ **Aucune suppression** des 14 views actuelles — `FILIALES_LEGACY.md` archive pointe vers les views individuelles, la fusion est gérée au niveau Sidebar (routes canoniques vers la view fusionnée).

### Sidebar V2 — `Settings.tsx` — Mark's arborescences (la pièce attendue)

**Page /settings** passe d'un formulaire basique à un **hub de 7 tabs Mark-style** :

| Tab | Contenu | Routes additionnelles | Sister canon |
|---|---|---|---|
| **Profile** | User email · display name · avatar · role | `/settings/profile` | Sister canon `_auth/AuthProvider.tsx` |
| **Sidebar Custom** | Toggle sections visible/caché · ré-ordonner Triptyque 1/2/Duo · dark mode · collapse state · Filiales switcher | `/settings/sidebar` | NOUVEAU (la pièce attendue) |
| **Integrations** | Bedrock (image/doc gen) · Slack · Salesforce · Google Workspace · SendGrid · Airtable · Notion · MCP Servers | `/settings/integrations` | screenshot #7 Mark + Blueprint Kit §8 specs integrations |
| **Security** | Kill Switches · PII Redaction · DLP & Exfil · Panic · Rate Limits · Security Posture · Compliance · Agent Behavior toggles (memory writes / ingest / consolidation / context v2 / hooks / skills / sessions frozen / jarvis voice) | `/settings/security/*` | screenshot #5+#6 Mark — adapter à notre posture sovereign-local PAS AWS |
| **Compliance** | SOC 2 · HIPAA · AI-Act Art. 9/10/14 · RGPD · 5 mécanismes Zero-PII (ADR-ICP-NEXUS-001 Pilier 5) · Latest guidance · Fix recommendations | `/settings/compliance` | screenshot #7 Mark — doctrine canon §4 ADR-Nexus |
| **Knowledge Base** | Default scope (0 docs, 0 chunks) · Test retrieval · Test with a model (multi-LLM : Claude Opus/Sonnet/Haiku, GPT-OSS 120B, DeepSeek V3.2, Qwen3 32B, Kimi K2.5, Mistral, Llama 3 8B) · Drag & drop upload · Compare · Chat | `/settings/knowledge-base` | screenshot #9 Mark |
| **Filiales & Workspace** | Holding vs Filiales switcher · Coach · EC · Avocat · Médical · Family-Office · Lean matrix per Filiale | `/filiales` (sister route) | plan-L2-business-os.md §5.4 |

⚠️ Adapter pour **sovereign-local PAS AWS** — le scoring Mark est AWS posture, notre posture est Hermes-on-prem + Ollama 2-node air-gapped (T1 spec bundle ratifié 2026-07-03).

### Sidebar V2 — `Filiales` page — matrice lean par ICP (calque §5.4 plan L2)

| Filiale | Domaines Jerry activés (lean) | Sister canon |
|---|---|---|
| **Coach** (spearhead) | Cyborg (Workflows) + GreenLantern (SOP-Vault) | ADR-ICP-NEXUS-001 |
| **EC** | Flash (Reconciliations) + WonderWoman (Zero-PII-Facturation) | idem |
| **Avocat** | Aquaman (AI-Act, Conflict-Scanner) | idem |
| **Medical** | WonderWoman (Health-Vault) + Aquaman | idem |
| **Family-Office** | Mental Manhunter (Vault-Redactor) + Batman (Vault-Audit) | sanctuary |

**Pas une page Sidebar** — c'est une route /filiales dediée.

---

## 5. Plan d'implémentation — phase W3-W5

### Phase A — préservation template (W3 ✅)

- [x] Lire Sidebar.tsx existant (204 lignes, 14 views, 4 sections)
- [x] Mapper les 14 views actuelles vs Triptyque 1/2/Duo
- [x] Documenter cette spec comme DRAFT

### Phase B — restructuration Home (W3 ✅ exécuté 2026-07-03T16:50)

- [x] Créer 4 nouvelles views : **PeopleAgentsView** (8812 chars, fusion People + AI Agents), **OperationsKnowledgeView** (5646 chars, fusion Documents + SOP), **ItSoftwareKernelView** (7376 chars, étendu sovereignty Cyborg P10-P18), **ProductView** (6532 chars, nouveau Triptyque 2)
- [x] Bonus : **FilialesMatrixView** (7217 chars, route /filiales sister §5.4 plan L2) — référencée par ProductView
- [x] Ajouter routes `/people-agents`, `/operations-knowledge`, `/it-software-kernel`, `/product`, `/filiales` dans App.tsx (lignes 92-96)
- [x] Modifier `Sidebar.tsx` NAV_GROUPS pour pointer vers les routes fusionnées :
  - **CULTIVATE** : Dashboard / People-Agents / Operations-Knowledge / IT Software Kernel (Triptyque 1)
  - **NURTURE** : Clients / Tasks / Marketplace
  - **BLOOM** : Product / Growth / Sales Sanctum (Triptyque 2)
  - **ROOTS** : Finance / Legal (Duo) + Settings (Mark-style)
- [x] D4 append-only : legacy routes /people /agents /documents /sop /it-data restent live
- [ ] PR review + merge vers main (gated A0)

### Phase C — Settings Mark-style (W5 gated)

- [ ] Créer `src/components/settings/SettingsLayout.tsx` (tabs layout)
- [ ] 7 tabs components : `ProfileTab`, `SidebarCustomTab`, `IntegrationsTab`, `SecurityTab`, `ComplianceTab`, `KnowledgeBaseTab`, `FilialesTab`
- [ ] Wire routes `/settings/{tab}` dans router
- [ ] Adapter Compliance aux 5 mécanismes Zero-PII canon (ADR-ICP-NEXUS-001 Pilier 5) au lieu de SOC 2 live-AWS

### Phase D — Filiales matrix (W6 gated)

- [ ] Créer `src/components/filiales/FilialesMatrix.tsx`
- [ ] 5 templates par ICP avec leurs sous-domaines lean
- [ ] Switcher Holding ↔ Filiale dans contexte AuthProvider
- [ ] PR review pour les 5 templates

---

## 6. Doctrine ancrage

- **D2 research-first** : Blueprint Kit + Solaris + Mark + OMK existing = 4 sources comparées
- **D6 no-copy** : aucune ligne copiée de Mark directement — adoption de **patterns** (CORE/OPS/SECURITY/ADVANCED/COLLABORATION/TEAM/ACCOUNT), pas de CSS/HTML/marqueur spécifique
- **D4 append-only** : SettingsView.tsx actuel reste archive, nouveau layout tabs ajoute par-dessus
- **Calquer sur Solaris** (E-Myth cult UI), pas remplacer
- **Filiales → Domain Pages**, pas Settings → Filiales
- **Sovereign-local PAS AWS** : posture Hermes-on-prem + Ollama 2-node air-gapped T1

---

## 7. Hors périmètre (différé)

- 5 Templates Filiales complets deploy Vercel séparés (plan §5.4 roadmap)
- 8 B2 Agents runtime instanciés dans Settings → Integrations
- 35 A3 twins Les fictions dans un éditeur de Settings (cf. `_ROSTER.md`)
- Drill-down Compliance CC6.1/CC6.3/CC7 (Mark a 9 controls scorés — adapter aux 5 mécanismes Zero-PII)
- Audit log runtime événementiel (Mark a 200 events / 7 jours)
- Test retrieval / Test with a model multi-LLM (Mark a 7 modèles)

---

## 8. Sacred exclusions

- ❌ Ne PAS remplacer Cultivate/Nurture/Bloom/ROOTS (préserver métaphore jardin digital)
- ❌ Ne PAS merger Settings et Filiales (3 couches cloisonnées : Home / Settings / Filiales)
- ❌ Ne PAS adopter la posture AWS live-scoring (sovereign-local canon)
- ❌ Ne PAS coder les kill switches en dépendance AWS (canon Cyborg P10-P18 sovereign-local)
- ❌ Ne PAS toucher les 14 views actuelles en suppression (D4 append-only — routes archived)

---

*Spec DRAFT 2026-07-03T16:42 ET par Mavis/MC (A3 Book) suite instruction A+. Sister canon : 5 sources analysées (Blueprint Kit 15 fichiers, Mark 9 screenshots ClaudeClaw Enterprise, Solaris 12 views, OMK 14 views existantes, Filiales §5.4 plan L2). Doctrine D2 + D6 + D4 strict.*
