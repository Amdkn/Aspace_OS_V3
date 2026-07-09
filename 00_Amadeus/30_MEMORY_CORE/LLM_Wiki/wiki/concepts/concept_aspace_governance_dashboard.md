---
source: Codex (VPS SSH work) + Hermes validation, relayed by A0
date: 2026-06-03
type: concept
domain: L0 Tech_OS / Infrastructure Governance / VPS
tags: [#governance #dashboard #vps #hermes #codex #infrastructure #canonical_rule #aspace_dashboard]
status: CANONICAL_RULE
---

# A'Space Governance Dashboard — console unifiée d'infrastructure

> **Doc-ownership (ADR-INFRA-001 D3)** : **Codex documente en LOCAL (Windows)** = la source · **Hermes (dans
> le VPS) documente DANS le serveur** (`/srv/aspace/.../aspace-governance-dashboard.md`) = le déploiement ·
> **Claude Code (A2)** maintient ce wiki local et réconcilie le drift. Cette page = la copie source locale.

## Quoi
Codex a **structuré Hermes sur le VPS (par SSH)** et **fusionné les surfaces de gouvernance en une seule console** :
**URL canonique** : `https://aspace-dashboard.148.230.92.235.sslip.io/` (app Next.js, `aspace-dashboard.service` active/enabled, loopback `127.0.0.1:9119`, exposé HTTPS via Caddy).

## Structure
```
/srv/aspace/dashboard/app/
├── page.tsx              → Overview (/)
├── infrastructure/       → CPU, disque, mémoire, politique monitoring (/infrastructure)
├── tokens/               → Token Governance (/tokens)
├── api/<domain>/         → endpoints (auth requise — 401 sans session)
└── components/Sidebar.tsx → navigation canonique (point d'entrée)
```
**Sidebar** : Overview · Infrastructure · Tokens · + surfaces externes (Hermes Agent Dashboard `:8642`, Hermes Workspace `:3001`, Dokploy `:3002`).

## 🔑 La règle canonique (le vrai livrable doctrinal)
> **Plus de dashboards isolés par réflexe.** Tout nouveau dashboard devient une **"app de gouvernance"** dans
> cette console unique :
> ```
> /srv/aspace/dashboard/app/<domain>/        # page.tsx
> /srv/aspace/dashboard/app/api/<domain>/    # route.ts
> + une entrée dans components/Sidebar.tsx
> npm run lint && npm run build
> ```
Provenance : SKILL VPS `aspace-governance-dashboard` (`~/.hermes/skills/`) + skills locaux Codex `dashboard-builder` + `hermes-vps-runtime-ops`.

## Validation (Codex/Hermes)
lint PASS · build PASS · `/` `/infrastructure` `/tokens` = 200 · `/api/*` = 401 (auth) · service active/enabled · secret-scan PASS.

## ⚠️ Risque ouvert
- **Disque Supabase à 79%** (cible 25-50%) → à traiter (L0/13th Doctor). Risque infra réel, non bloquant immédiat.

## Drift VPS ↔ local (ADR-INFRA-001 D3)
- **Hermes** écrit la doc dans `/srv/aspace/...` (VPS = déploiement). **Codex** écrit en local Windows (source).
  Cette page = la copie source locale, réconciliée par Claude Code. Toute évolution de la règle doit être
  re-synchronisée des deux côtés.
- **Risque disque** : Codex travaille **actuellement** sur la réduction du disk usage du VPS ; prochaine app de
  gouvernance = **Supabase Health** (analytics/realtime/supavisor) ou **Cleanup Approvals** (pas CPU/orchestration, déjà fait).

## Liens
- [[concept_shadow_l1_l2_heartbeat_symphony]] · ADR-HERMES-001 (topologie Hermes Desktop/Workspace) · ADR-RICK-001.
- Echo doctrine : IT runtime fiche AaaS (souveraineté, loopback+Caddy), People PE17 (Hermes), Finance (token governance).
