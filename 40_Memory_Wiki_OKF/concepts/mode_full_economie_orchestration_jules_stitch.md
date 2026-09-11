---
type: Concept
title: Mode Full Économie Antigravity — Orchestration Jules & Gatekeeper Stitch
description: Architecture d orchestration asynchrone déléguée utilisant Jules (Google Labs) comme ouvrier de code par repo et Stitch comme Gatekeeper UI/UX.
tags: [economy-mode, jules, stitch, mcp, orchestration, quotas, antigravity]
generated: { by: antigravity, at: 2026-09-09T02:57:00Z }
verified:
  - { by: human:amdkn, at: 2026-09-09T02:57:00Z }
sources:
  - id: jules-mcp-repo
    resource: "https://github.com/samihalawa/google-jules-mcp.git"
    author: samihalawa
    last_modified: 2026-09-09
  - id: stitch-mcp-endpoint
    resource: "https://stitch.googleapis.com/mcp"
    author: google-labs
    last_modified: 2026-09-09
okf_version: "0.2"
---

# Mode Full Économie Antigravity — Orchestration Jules & Gatekeeper Stitch

## 1. Principe Fondamental & Sauvegarde des Quotas
- **Rôle d Antigravity / Gemini** : Chef d orchestre stratégique minimaliste. Ne consomme quasiment aucun token en écriture de code lourd.
- **Rôle de Jules** : Ouvrier de production autonome recevant des spécifications complètes et ouvrant des PRs GitHub.
- **Rôle de Stitch** : Gatekeeper de conformité design system, composabilité et validation visuelle.

## 2. La Vraie Limite : Sessions par Dépôt GitHub
- La contrainte opérationnelle de Jules n est **pas** un nombre arbitraire de tâches de projet.
- La contrainte réelle est le **plafond de sessions concurrentes par repository GitHub** (ex: `Amdkn/Agent-OS-Desktop`, `Amdkn/Business-Office-3-OS`, `Amdkn/The-OMK-Mobile-Back-Office`).
- **Stratégie d arbitrage** : Répartir les missions de Jules sur des repos distincts pour paralléliser sans saturer les files d attente.

## 3. Protocole de Délégation par Dossiers Physiques Dédiés
- **Zéro prompt flou** : L agent Antigravity ne transmet jamais de consignes vagues ou partielles.
- **Emplacement canonique** : Chaque dépôt possède son dossier `delegation-a-jules/` (ex: `PRD-*.md`, `README.md`).
- **Déclenchement minimaliste** : Le prompt d amorçage pointe directement sur ce dossier : `Exécute rigoureusement les directives du dossier delegation-a-jules/`.

## 4. Configuration MCP Certifiée
- **Jules MCP** : `npx -y google-jules-mcp` (Clé configurée sous `JULES_API_KEY`).
- **Stitch MCP** : `https://stitch.googleapis.com/mcp` (Header `X-Goog-Api-Key`).