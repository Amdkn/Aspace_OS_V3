---
id: B3_AGENT_ROSTER_04_Alikaly_IT
layer: B3_SWARM_EXECUTION
surface: 04_Alikaly
scope: Summer Project
domain: IT
squad: KangDynasty
status: SHADOW_ACTIVE
updated: 2026-05-27
source: Notion AGENT_REGISTRY_DB
source_url: https://www.notion.so/36c7e9e2658c81aa91b5e9be3cedcb52
---

# Agent Roster - IT / KangDynasty

## Notion Canon Lore

- **Notion page**: [Kang Dynasty](https://www.notion.so/36c7e9e2658c81aa91b5e9be3cedcb52)
- **B2 gatekeeper**: Cyborg
- **Lead character**: Kang Prime
- **Specialty**: Infrastructure VPS, Dokploy, Hostinger API et DNS
- **Lore**: Variants temporels de Kang : maitrise du temps, deploiement multi-dimensionnel, infrastructure conquerante. Business: IT scalable, deploiements paralleles, controle temporel des releases.

## Canonical Members

- Kang Prime - Lead infra, architecture VPS + DNS + Dokploy
- Iron Lad - Provisioning rapide, scripts bootstrap Hostinger API
- Scarlet Centurion - Securite reseau, firewall, SSL/TLS
- Immortus - Long-term planning, capacity planning, scaling
- Victor Timely - Time-boxing deploiements, CI/CD discipline
- Rama-Tut - Backup and disaster recovery

## Canonical Task Surface

- VPS Hostinger Ubuntu/KVM
- Dokploy Docker orchestration
- Hostinger DNS API
- GitHub Actions -> Dokploy webhook
- Monitoring Uptime Kuma + PM2 health endpoints
- Supabase managed Postgres boundaries

## Build Gates

- VPS provisioning < 5 min payment-to-active
- Uptime Solaris cloud > 99.5% mensuel
- Zero leaked secret dans logs via Yaz Watchdog scan

## Anti-Patterns Interdits

- SSH manuel sur VPS prod sans ticket trace
- Deploy sans CI/CD ou scp direct
- Modifier DNS sans propagation check post-change

## Escalation Rule

Escalade vers Jerry si uptime mensuel < 99% ou MTTR infra > 1h.

## Machine Roster

``yaml
domain: IT
b2_gatekeeper: Cyborg
squad: KangDynasty
lead_character: Kang Prime
notion_source: https://www.notion.so/36c7e9e2658c81aa91b5e9be3cedcb52
members:
  - "Kang Prime - Lead infra, architecture VPS + DNS + Dokploy"
  - "Iron Lad - Provisioning rapide, scripts bootstrap Hostinger API"
  - "Scarlet Centurion - Securite reseau, firewall, SSL/TLS"
  - "Immortus - Long-term planning, capacity planning, scaling"
  - "Victor Timely - Time-boxing deploiements, CI/CD discipline"
  - "Rama-Tut - Backup and disaster recovery"
``

## Collaboration Defaults

- First agent to understand the JTBD creates a short working note.
- Second agent attacks assumptions and missing evidence.
- Third agent builds or gathers the main artifact.
- Fourth agent reviews proof, edge cases, and handoff quality.
- The exact order may change when the task demands it.

## Peer Unlock Rule

Before escalating to B2, a blocked B3 must ask one peer from the same squad to challenge the blocker and propose one workaround.

## Proof Rule

Every claim in this roster is either from Notion AGENT_REGISTRY_DB or from the local Business Pulse swarm doctrine. If Notion and local doctrine diverge, Notion wins for lore and local doctrine wins for filesystem path conventions.