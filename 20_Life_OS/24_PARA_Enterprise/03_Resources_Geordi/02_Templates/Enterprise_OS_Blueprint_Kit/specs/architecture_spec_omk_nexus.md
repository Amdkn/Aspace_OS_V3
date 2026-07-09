---
type: spec-override
id: SPEC_OMK_ARCHITECTURE
title: "ARCHITECTURE_SPEC OMK Nexus BOS - Triptyque 1+2+Duo, 8 agents (1 par LD)"
status: RATIFIED
date: 2026-07-05T09:45:00-04:00
author: HA (A3 Picard in PARA)
refines: specs/ARCHITECTURE_SPEC.md (template canon)
sister: ADR-LD01-011
---

# ARCHITECTURE_SPEC - OMK Nexus BOS (override Tier T1)

> Override du template canon. Architecture 8 agents = 1 par LD (Triptyque 1 + Triptyque 2 + Duo).

## Design principles (from Blueprint + Triptyque PoC)
- One AWS account holds everything (per Blueprint section 2).
- One orchestrator runs every agent = **HA Picard (H10) orchestre, A3 Book (H1) supervise** per ADR-LD01-008.
- Every model call goes through Bedrock, so prompts never leave your walls.
- All data in DynamoDB + S3, encrypted with KMS.
- One chokepoint per turn: rate limit + kill switches + fail-closed cost cap.
- Write-once (WORM) audit trail 7 ans.
- Only chosen surfaces reach in (Telegram + Slack + Web dashboard), through one gated front door.
- **Extra layer (PoC specifique OMK)** : cache semantique local SQLite/OPFS (per Gemini T1 IT) pour les prompts AAARR rejoues sur signaux similaires -> 0 token cloud.

## Secure-substitute map (fill from OMK current tools)
| Your current tool | Secure in-account substitute | Why |
|---|---|---|
| Otter.ai / Gong (manual transcript) | Bedrock Claude + Whisper | transcripts never leave account |
| Notion SOPs (static) | DynamoDB Skills table + S3 markdown | executable, versioned, auditable |
| Lemlist / Instantly (email blast) | Local AAARR scrapers + AAARR prompts (this PoC) | signal-based, not spam |
| HubSpot CRM | DynamoDB L1 cognition table | own keys, own schema |
| Calendly | Telegram bot scheduling | one surface to audit |
| Managed LLM API (OpenAI/Anthropic direct) | Bedrock in-account | prompts never leave |
| Zapier automations | DynamoDB Streams + Lambda | auditable, reversible |

## Data flow (one account, OMK Nexus specifique)
```
beta-coach / prospect signal (LinkedIn Apollo / Reddit / Gong transcript)
  -> AAARR Growth scraper (local, no token cloud)
  -> Bedrock Claude (Haiku tier, signal qualification)
  -> DynamoDB swarm_pulses (L2 mesh per ADR-L2-MESH-001)
  -> if signal scored >= 0.7: Bedrock Sonnet (Quiz d'Acquisition draft)
  -> Quiz d'Acquisition Medvi audit (in Agentic Dashboard web)
  -> if prospect accepts: Telegram bot takes over (HA Picard H10 tier, MANIFEST.md write)
  -> if signed: A3 Book H1 aggregator (MC) appends to weekly P&L
  -> if retainer active: DLP-light subset PII/credentials filter before every external write
  -> write-once audit log (S3 Object Lock, 7-year hold)
```

## 8 Agents = Triptyque 1+2+Duo

### Triptyque 1 - Backbone (3 agents)
| LD | Agent A3 | Role | Surface | Modele | Outils |
|---|---|---|---|---|---|
| LD06 (People) | A3 Burnham Family | Human/agent partition - SOPs, contrats types, onboarding technique | Telegram + dashboard | Sonnet | Read/Write DynamoDB SOPs |
| LD07 (IT) | A3 Stamets Social | Cache semantique local + KV cache management | n/a (infra) | Haiku | Bash, OPFS |
| LD01 (Ops) | A3 Book (MC canon) | Maintenance Skills - SOPs -> .md executables | dashboard | Sonnet | Read/Write S3 + DynamoDB |

### Triptyque 2 - Front-End (3 agents)
| LD | Agent A3 | Role | Surface | Modele | Outils |
|---|---|---|---|---|---|
| LD04 (Product) | A3 Tilly Cognition | Creation assistee - segmentation Haiku/Sonnet (premier jet local + validation cloud) | web dashboard | Haiku -> Sonnet | Read/Write DynamoDB content |
| LD08 (Growth) | A3 Saru Finance | **AAARR scrapers + signal qualification** (11 prompts per ADR-LD01-011) | Telegram + dashboard | Haiku | Bash scraping + Read Apollo/Reddit |
| LD05 (Sales) | A3 Ortegas SNW | **Quiz d'Acquisition Medvi + closing par preuve ROI** | web dashboard | Sonnet | Read/Write DynamoDB prospects |

### Duo - Garde-Fous (2 agents)
| LD | Agent A3 | Role | Surface | Modele | Outils |
|---|---|---|---|---|---|
| LD02 (Finance) | A3 Spock Areas | **MiniMax plan forfaitaire** = cost cap fail-closed | n/a (monitoring) | n/a (script) | Bash AWS Budget + kill switch |
| LD03 (Legal) | A3 Data Archives | **DLP-light 7 patterns** (PII/credentials subset, Phase 2 = 9 patterns Blueprint) | n/a (middleware) | n/a (regex Python) | Read/Write middleware |

## Key decisions and tradeoffs
- Deploy tier: **T1 standard** (per ADR-LD01-011 D3)
- VPC interface endpoints: **OFF** par defaut (~$175/mois saved), ON seulement si PrivateLink isolation requise Phase 2
- Audit Object Lock mode: **governance**, retention: **7 ans** (per Blueprint section 6 + ADR-LD01-011)
- Model mix: **Haiku pour les 11 prompts AAARR (signal qualification), Sonnet pour le Quiz d'Acquisition et l'output final, Opus hardcode aucun usage PoC** (cout trop eleve vs. value-add incertain)
- **Cache semantique local SQLite/OPFS** : specifique OMK, pas dans Blueprint par defaut. Mitige le Jevons paradox (cout token -> quand usage monte)
