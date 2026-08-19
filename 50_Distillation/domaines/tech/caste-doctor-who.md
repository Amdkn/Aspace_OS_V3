---
type: Concept
title: Caste Doctor Who — A1 Rick / A2 Doctors / A3 Companions
description: Hiérarchie des agents Tech OS dérivée du lore Doctor Who : un Visionnaire, trois Managers, neuf Compagnons spécialisés.
tags: [tech, gouvernance, agents, hierarchie]
generated: { by: minimax-m3, at: 2026-08-19T12:00:00Z }
verified:
  - { by: process:read, at: 2026-08-19T12:00:00Z }
sources:
  - id: rick-a1
    resource: 05_From_V2_Domains/10_Tech_OS/00_Governance_Rick/Drivers/A1 - Rick Sanchez (Visionnaire & Gatekeeper Absolu).md
    title: A1 Rick Sanchez — ADR-000
    last_modified: 2026-01-01
  - id: d11
    resource: 05_From_V2_Domains/10_Tech_OS/00_Governance_Rick/Drivers/A2 - 11ème Docteur (Manager du Life Core).md
    title: A2 11ème Docteur (Life Core / Product)
    last_modified: 2026-01-01
  - id: d12
    resource: 05_From_V2_Domains/10_Tech_OS/00_Governance_Rick/Drivers/A2 - 12ème Docteur (Manager du Buz Core  Business Pulse).md
    title: A2 12ème Docteur (Forge Core / Data)
    last_modified: 2026-01-01
  - id: d13
    resource: 05_From_V2_Domains/10_Tech_OS/00_Governance_Rick/Drivers/A2 - 13ème Docteur (Manager du Solarpunk Kernel).md
    title: A2 13ème Docteur (Kernel Core / Infra)
    last_modified: 2026-01-01
  - id: governance-readme
    resource: 05_From_V2_Domains/10_Tech_OS/00_Governance_Rick/README.md
    title: 00_Governance_Rick (The Citadel)
    last_modified: 2026-01-01
okf_version: "0.2"
---

Le Tech OS reprend la métaphore **Doctor Who** pour distribuer les rôles entre agents :

| Niveau | Nom | Couche OS | Mission |
|--------|-----|-----------|---------|
| A1 | Rick Sanchez (Visionnaire, Gatekeeper Absolu) | Métacouche | Émettre la Loi L0, ratifier les ADR, déclencher l'Apoptose |
| A2 | 11ème Docteur | L0.1 Life Core | Manager UX/AG-UI, supervise Amy / Rory / River Song |
| A2 | 12ème Docteur | L0.2 Forge Core | Manager Skills/MCP, supervise Bill / Clara / Nardol |
| A2 | 13ème Docteur | L0.3 Kernel Core | Manager Infra/VPS, supervise Yaz / Ryan / Graham |
| A3 | 9 Companions | L0.1 / L0.2 / L0.3 | Exécutants spécialisés dans leurs domaines |

## Règles de délégation (TARDIS §2 SDD-003)

```
A1 Rick → A2 Doctor → A3 Compagnon   ✅ chaîne correcte
A1 Rick → A3 Compagnon               ❌ court-circuit interdit
A0 Amiral → A3 Compagnon             ❌ violation de souveraineté
A2 Doctor → autre A2 Doctor          ⚠️ via Rick uniquement
```

Rick ne connaît que 3 interlocuteurs (11D, 12D, 13D). Chaque Doctor ne connaît que ses 3 Companions. Pas de cross-team sans Rick.

## Loi TARDIS : Who Not How

- A1 Rick définit **QUI** (quel A2 Doctor).
- A2 Doctors définissent **QUI** (quel A3 Companion) et **POURQUOI**.
- A3 Companions définissent **COMMENT** — exécution pure, scoped, sandboxée.

L'Amiral (A0) ne touche jamais le **HOW** — uniquement le **WHAT** stratégique.

Voir aussi : [[tardis-inverse]], [[capabilities-doctors-13-12-11]], [[agents-doctor-data-12th]].