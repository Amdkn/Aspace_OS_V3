---
type: Backend
title: A'Space Governance Dashboard — console unifiée VPS
description: Console canonique d'infrastructure (ADR-INFRA-001) : `https://aspace-dashboard.148.230.92.235.sslip.io/`. Plus de dashboards isolés — toute nouvelle gouvernance devient une app dans cette console (Caddy/Kong reverse-proxy + Dokploy).
tags: [governance, dashboard, vps, caddy, kong, dokploy, hermes, adr-infra-001]
generated: { by: minimax-m3, at: 2026-08-17T21:16:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T21:16:00Z }
sources:
  - id: concept-governance-dashboard
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/concepts/concept_aspace_governance_dashboard.md"
    title: "A'Space Governance Dashboard — console unifiée d'infrastructure"
    last_modified: 2026-06-05
  - id: shadow-reprise
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/concepts/concept_shadow_l0_l1_l2_reprise.md"
    title: "Concept — Reprise Shadow L0 → L1 → L2"
    last_modified: 2026-06-05
okf_version: "0.2"
---

# A'Space Governance Dashboard — console unifiée VPS

> **Doc-ownership (ADR-INFRA-001 D3)** : Codex documente **local Windows** (source) ;
> Hermes documente **dans le VPS** (`/srv/aspace/.../aspace-governance-dashboard.md`,
> déploiement) ; Claude Code (A2) maintient ce wiki local et réconcilie le drift.
> Cette page = la copie source locale.

## 1. URL canonique

`https://aspace-dashboard.148.230.92.235.sslip.io/`

App Next.js, service `aspace-dashboard.service` active/enabled, loopback `127.0.0.1:9119`,
exposé HTTPS via Caddy.

## 2. Structure

```
/srv/aspace/dashboard/app/
├── page.tsx              → Overview (/)
├── infrastructure/       → CPU, disque, mémoire (/infrastructure)
├── tokens/               → Token Governance (/tokens)
├── api/<domain>/         → endpoints (auth requise — 401 sans session)
└── components/Sidebar.tsx → navigation canonique
```

**Sidebar canonique** : Overview · Infrastructure · Tokens · + surfaces externes
(Hermes Agent Dashboard `:8642`, Hermes Workspace `:3001`, Dokploy `:3002`).

## 3. La règle canonique (le vrai livrable doctrinal)

> **Plus de dashboards isolés par réflexe.** Tout nouveau dashboard devient une
> « app de gouvernance » dans cette console unique :
>
> ```
> /srv/aspace/dashboard/app/<domain>/        # page.tsx
> /srv/aspace/dashboard/app/api/<domain>/    # route.ts
> + une entrée dans components/Sidebar.tsx
> npm run lint && npm run build
> ```

Provenance : SKILL VPS `aspace-governance-dashboard` (`~/.hermes/skills/`) + skills locaux
Codex `dashboard-builder` + `hermes-vps-runtime-ops`.

## 4. Validation (2026-06-05)

| Test | Résultat |
|---|---|
| lint | PASS |
| build | PASS |
| `/` `/infrastructure` `/tokens` | 200 |
| `/api/*` | 401 (auth) |
| service active/enabled | OK |
| secret-scan | PASS |

## 5. Token Governance (déjà déployé)

- 22 inventaire · 5 high-risk · 22 unknown-expiry · 0 broken
- Valeurs **jamais stockées/rendues** (empreintes SHA-256 seulement)
- À annoter : `API_SERVER_KEY`, `OPENROUTER_API_KEY` (Hermes) = `unknown-expiry/high`

## 6. Risque ouvert

**Disque Supabase à 79 %** (cible 25–50 %). À traiter par L0/13ᵉ Docteur.
Risque infra réel, non bloquant immédiat.

## 7. Token Governance — décision D3 (ADR-INFRA-001)

Ce que ce n'est PAS : un endroit pour stocker les secrets. Le token est hashé puis comparé.
La valeur ne quitte jamais le vault d'origine.

```sql
SELECT sha256(token) AS fingerprint, last_seen_at, expires_at
FROM vault.secrets_metadata
WHERE fingerprint = '<sha256>';
```

Le dashboard manipule `secrets_metadata`, jamais `secrets`.

## 8. Drift VPS ↔ local

Hermes (VPS, déploiement) ↔ Codex (local Windows, source). Claude Code maintient la page
wiki et réconcilie le drift. Toute évolution de la règle doit être re-synchronisée des deux côtés.

Prochaine app de gouvernance = **Supabase Health** (analytics/realtime/supavisor) ou
**Cleanup Approvals** (pas CPU/orchestration, déjà fait).

## Liens entrants

- `ntfs-junction-aliasing.md` — la couche filesystem ; le dashboard est une *vue*
- `shadow-l1-l2-homologie.md` — qui alimente (Hermes Workspace VPS) ?
- `geordi-junctions-map-159.md` — la frontière physique vs la vue logique
