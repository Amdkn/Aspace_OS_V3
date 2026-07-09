---
id: AAAS_SOL_B3_KANGDYNASTY_SQUAD_CANON
layer: B3_SWARM_EXECUTION
scope: Summer Project
project: 00_Agency_aaS
mode: Solaris (visual-first / brand-led)
domain: IT
b2_owner: Cyborg
squad: Kang Dynasty
lead_character: Kang Prime
canon_source: Notion AGENT_REGISTRY_DB — "Kang Dynasty"
doctrine_source: J01_Jerry_Prime_LD01_Business (Area — perpetual doctrine)
principles_status: PENDING (no extracted reference principles yet — only Growth/Superman has Yann Leonardi corpus)
status: SHADOW_ACTIVE
updated: 2026-05-29
---

# 🟣 Kang Dynasty — IT Squad (Picard / AaaS Solaris instance)

> **Project instance** du canon Kang Dynasty. Doctrine perpétuelle dans l'Area Jerry `05_IT_Cyborg_KangDynasty/B3_Squad_KangDynasty/`. Lore → Notion `AGENT_REGISTRY_DB`. **Principes de référence : PENDING.**

**Lore Marvel** : variants de Kang, maîtres du temps et de la technologie, coordonnés depuis une chronologie centrale. **Analogie business** : infra team qui provisionne, sécurise et maintient le socle technique multi-tenant.

**Specialty** : Infra VPS/DNS/Dokploy + provisioning + sécurité réseau + CI/CD.

## Membres canoniques (6 sub-agents)
- **Kang Prime** — Infra core : VPS, DNS, Dokploy, orchestration
- **Iron Lad** — Provisioning automatisé (Hostinger API)
- **Scarlet Centurion** — Sécurité réseau, SSL/TLS
- **Immortus** — Capacity planning, scaling anticipé
- **Victor Timely** — CI/CD pipelines
- **Rama-Tut** — Backup / Disaster Recovery

## Stack canonique
Hostinger Ubuntu 24.04 · Dokploy · Supabase (self-host) · Uptime Kuma + PM2.

## Calibrage Solaris (delta projet)
- Tier **Solaris** = multi-tenant managed sur infra mutualisée → provisioning tenant < 5min.
- Isolation tenant + SSL auto pour chaque instance Solaris.

## Build Gates types (canon)
- Provisioning < 5min → green
- Uptime > 99.5% → green
- Zero leaked secret (scan continu)

## Anti-patterns interdits (canon)
- ❌ Secret en clair dans repo / .md / .json
- ❌ Déploiement sans backup pré-deploy
- ❌ Changement infra sans rollback documenté

## Owner B2 & escalation
**Cyborg** (IT VP). Escalade vers Summer puis Jerry si uptime < 99% ou MTTR infra > 1h.

## Doctrine & miroirs
- **Crosslink** : `00_CROSSLINK.md` · **Principes** : *PENDING*.

*B3 instance Solaris under Cyborg (B2). Doctrine inherited from Jerry Area. Last sync: 2026-05-29*
