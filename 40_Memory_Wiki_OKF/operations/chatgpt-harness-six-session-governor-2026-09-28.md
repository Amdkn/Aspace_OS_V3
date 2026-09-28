---
type: Operations memory
title: ChatGPT Harness — six-session context governor
date: 2026-09-28
tags: [chatgpt, harness, context, tool-calls, handover, emyth, multisession]
okf_version: "0.2"
confidence: A0-accepted-design
---

# ChatGPT Harness — six-session context governor

A'Space ne doit plus dépendre d'une session ChatGPT géante pour conserver sa cohérence.

## Décisions durables

- reprise depuis V3 et ses sources persistantes, jamais depuis la mémoire conversationnelle seule;
- budget volontaire de 24 actions externes par vague;
- checkpoint à 16, aucun nouveau scope après 22, handover obligatoire à 24;
- une panne de surface n'est pas un gate global;
- handover = continuité de qualité, pas baisse d'ambition;
- A0 ne répète pas un contexte déjà enregistré;
- E-Myth appliqué au harness : Visionnaire → Gatekeeper → Managers → techniciens/effecteurs.

## Six lanes parallèles

- Ryan→Clara / GitHub Forge
- Rory / Linear Life Space
- River / Google Workspace Business Plane
- Graham / Supabase IPBD + WorkGraph
- River / Jev Reflex Fabric
- Yaz / LiDAR + Tinybird Observability

Rick garde l'arbitrage transversal. Amy/Herdr est le plan d'interface/persistance commun.

## Canon

- `10_Tech_OS/00_Governance_Rick/ADR-RICK-CHATGPT-HARNESS-CONTEXT-GOVERNOR-2026-09-28.md`
- `10_Tech_OS/00_Governance_Rick/ADR-RICK-SIX-PARALLEL-SESSIONS-2026-09-28.md`
- `10_Tech_OS/00_Governance_Rick/ADR-RICK-EMYTH-ANTI-TECHNICIAN-HARNESS-2026-09-28.md`
- `_INBOX/handoffs/HANDOVER-2026-09-28-SIX-PARALLEL-SESSIONS.md`
