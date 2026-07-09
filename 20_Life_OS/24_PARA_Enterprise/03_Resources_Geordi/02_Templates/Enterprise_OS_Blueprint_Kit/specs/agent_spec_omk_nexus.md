---
type: spec-override
id: SPEC_OMK_AGENT
title: "AGENT_SPEC OMK Nexus BOS - 8 agents (1 par LD du Triptyque 1+2+Duo)"
status: RATIFIED
date: 2026-07-05T09:45:00-04:00
author: HA
refines: specs/AGENT_SPEC.md (template canon)
sister: ADR-LD01-011
---

# AGENT_SPEC - OMK Nexus BOS (override 8 agents)

> Override du template canon. 8 agents = 1 par LD (Triptyque 1 + Triptyque 2 + Duo).

## Agent: AAARR_Growth_Scraper (LD08 Growth)
- Purpose: Scraper signaux publics AAARR (Apollo, Reddit, LinkedIn Sales Navigator)
- Model and effort: Haiku (cheap, signal qualification tier)
- Tools it can use: Bash (scraping Apollo/Reddit APIs), Read (signal corpus)
- Surfaces it answers on: Telegram (alertes daily), dashboard (cumul hebdo)
- Data it can touch: DynamoDB swarm_pulses (own table only), local SQLite cache
- Who can invoke it: operator, admin (A0 + Abdaty)
- Kill switch: kill switch #1 (Blueprint section 6) = stop scraping if abuse detected
- Cost note: ~$5/mois (Haiku, ~100k tokens/mois, cache semantique local)

## Agent: Quiz_Acquisition_Conductor (LD05 Sales)
- Purpose: Conduire le Quiz d'Acquisition Medvi, generer cartographie pertes + plan liberation
- Model and effort: Sonnet (qualitative, high-stakes)
- Tools it can use: Read (DynamoDB prospects), Write (prospect scoring), Web dashboard
- Surfaces it answers on: web dashboard (Agentic Dashboard simulation)
- Data it can touch: DynamoDB prospects (own table), DLP-light filter middleware
- Who can invoke it: prospect self-serve (pas d'auth requise pour le quiz public), analyst (coachs)
- Kill switch: kill switch #2 (Blueprint section 6) = stop Quiz if defect
- Cost note: ~$80/mois (Sonnet, 100 clients x 1 quiz/mois x 5k tokens)

## Agent: DLP_Light_Filter (LD03 Legal)
- Purpose: Middleware regex Python, scanner outputs avant DB insert
- Model and effort: n/a (regex, no LLM)
- Tools it can use: Read (input strings), Write (audit log)
- Surfaces it answers on: n/a (middleware)
- Data it can touch: audit log only (S3 Object Lock)
- Who can invoke it: n/a (autonomous middleware)
- Kill switch: kill switch #5 = block ALL outputs until restored
- Cost note: ~$0 (Python regex)

## Agent: Cost_Cap_FailClosed (LD02 Finance)
- Purpose: Monitor AWS Budget + MiniMax plan, kill Bedrock on cap
- Model and effort: n/a (bash script)
- Tools it can use: Bash (AWS Budget API, MiniMax usage API)
- Surfaces it answers on: n/a (background daemon)
- Data it can touch: AWS Budget, MiniMax usage log
- Who can invoke it: n/a (autonomous daemon)
- Kill switch: kill switch #4 = kill Bedrock calls
- Cost note: ~$0

## Agent: SOP_Skill_Translator (LD01 Ops)
- Purpose: Convertir SOPs Notion textuelles en .md Skills executables
- Model and effort: Sonnet (medium)
- Tools it can use: Read (Notion export), Write (S3 Skills bucket), Bash (git commit)
- Surfaces it answers on: dashboard
- Data it can touch: DynamoDB skills (own table), S3 markdown bucket
- Who can invoke it: operator, admin
- Kill switch: standard SOP kill (kills SOP pipeline)
- Cost note: ~$20/mois (Sonnet, ~50 SOPs convertis/mois x 3k tokens)

## Agent: Onboarding_Conductor (LD06 People)
- Purpose: Premier contact Telegram, generation contrats types, onboarding technique beta-coachs
- Model and effort: Sonnet
- Tools it can use: Telegram bot API, Read/Write DynamoDB onboarding
- Surfaces it answers on: Telegram bot
- Data it can touch: DynamoDB onboarding (own table)
- Who can invoke it: any (Telegram users self-serve after BotFather auth)
- Kill switch: kill switch #3 = stop Telegram bot
- Cost note: ~$30/mois (Sonnet, 10 onboardings/mois x 10k tokens)

## Agent: Cache_Semantic_IT (LD07 IT)
- Purpose: Maintenir cache semantique local SQLite/OPFS, servir prompts rejoues a 0 token cloud
- Model and effort: Haiku (matching + indexing)
- Tools it can use: Bash (SQLite ops), Read (cache entries)
- Surfaces it answers on: n/a (infra)
- Data it can touch: SQLite cache (local), OPFS
- Who can invoke it: AAARR_Growth_Scraper, Quiz_Acquisition_Conductor (read-only via API)
- Kill switch: n/a (infra, no surface)
- Cost note: ~$10/mois (Haiku indexing, ~500k cache entries/mois)

## Agent: Content_Generator (LD04 Product)
- Purpose: Generation livrables coaching (syntheses strategiques, roadmaps croissance)
- Model and effort: Haiku (premier jet) -> Sonnet (validation finale)
- Tools it can use: Read (DynamoDB clients), Write (S3 livrables), Web dashboard
- Surfaces it answers on: web dashboard
- Data it can touch: DynamoDB livrables (own table), S3 content bucket
- Who can invoke it: analyst (coachs), admin
- Kill switch: standard content kill
- Cost note: ~$40/mois (Haiku bulk + Sonnet validation, ~200 livrables/mois)
