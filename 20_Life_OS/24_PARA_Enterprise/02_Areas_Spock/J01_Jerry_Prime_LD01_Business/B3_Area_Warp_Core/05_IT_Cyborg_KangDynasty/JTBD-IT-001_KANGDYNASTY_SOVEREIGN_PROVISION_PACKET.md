---
id: J01_B3_IT_001_KANGDYNASTY_PACKET
jtbd_id: J01-B3-IT-2026-001
source_rock: J01-B2-IT-2026-01
layer: B3_AREA_WARP_CORE
surface: Jerry Area J01 LD01 Business
scope: Area (perpetual doctrine - canonical reference for Picard projects)
domain: IT
b2_owner: Cyborg
squad_lead: Kang Prime
supports: [Iron Lad, Scarlet Centurion, Immortus, Victor Timely, Rama-Tut]
principles_ref: [P1, P10, P12, P13, P14, P15, P16, P17, P18]
evidence_grade: HYPOTHESIS (doctrine synthesis - field validation per project)
status: REVIEW_READY
updated: 2026-05-31
---

# JTBD-IT-001 - Kang Dynasty canonical packet (Area-level) - Jerry / Cyborg

> **Job** : *When a client/instance needs infrastructure, the Kang Dynasty provision a sovereign, isolated, observable stack (VPS+Dokploy+local-AI) via IaC so Cyborg guarantees uptime, security, and data sovereignty.*
> **Lead** : Kang Prime. **Squad** : Kang Dynasty (canon Notion AGENTS_REGISTRY_DB).
> WARNING evidence_grade = HYPOTHESIS - doctrine synthesis (domain principles + squad canon), not yet
> field-proven. **Area source of truth** : Picard projects inherit and calibrate by mode
> (Solaris/Nexus/Orbiter); they do not re-derive (DRY).
> **North Star** : operational integrity - latency, 0 critical incidents, data integrity (KR-5a..c).

## 1. North Star + frame
**NSM** : operational integrity (KR-5a 0 critical/<3 medium incidents/q, KR-5b weekly backup, KR-5c tech
debt <20%). Local-first, sovereign (P13). Build Gate: VPS provision <5min payment->active; uptime >99.5%.

## 2. Provision via IaC (Kang Prime / Iron Lad - P14/P15)
Terraform/Ansible idempotent on Hostinger VPS + Dokploy + DNS; Docker Compose pinned versions (P15).
No manual scp, no SSH on prod without traced ClickUp ticket. CI/CD GitHub -> Dokploy webhook.

## 3. Security baseline (Scarlet Centurion - P16/P17)
Network isolation (VPC logic, WireGuard/Tailscale), firewall, SSL/TLS, ephemeral tokens, sandbox +
atomic merge (P17). Build Gate: zero leaked secret in logs (Yaz Watchdog scan).

## 4. Sovereign AI substrate (Kang Prime - P10/P12) - optional per instance
Ollama local inference + MCP local connectors + Qdrant RAG when the instance needs agents - data never
leaves the perimeter (P13). Agent harness = A2/A3 orchestration (P1).

## 5. Resilience + observability (Rama-Tut / Victor Timely - P18)
Backup snapshot weekly + DR (KR-5b); Uptime Kuma + PM2 health (ADR-INFRA-001); ADR + Markdown logs.

## 6. Handoff & authority
**Cyborg owns IT architecture outright - Jerry does NOT decide.** Escalate Jerry if uptime <99% mo or
MTTR >1h.

## DoD auto-check (Rock J01-B2-IT-2026-01)
- [x] gate/filter defined - [x] hypotheses/templates - [x] inspectable proof plan - [x] zero ungated external mutation - [ ] **Acceptance Cyborg**

*B3 Area artifact (Kang Dynasty, Kang Prime lead) under Cyborg. Canonical reference for Picard. Distilled from domain doctrine + squad canon, 2026-05-31.*
