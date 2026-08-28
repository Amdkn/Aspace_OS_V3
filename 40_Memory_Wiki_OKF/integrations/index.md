---
type: Bundle index
title: integrations — ce qui est branché à quoi
description: Câblages entre le poste et les services externes, avec le chemin pour les défaire et les confusions déjà payées.
tags: [okf, integrations, index]
generated: { by: claude-opus-5, at: 2026-08-17T15:10:00Z }
okf_version: "0.2"
---

Ce sous-bundle décrit **ce qui est branché à quoi** : gateways, endpoints,
clés (par leur préfixe seulement), et surtout ce qu'il a fallu comprendre pour
y arriver.

Chaque page doit répondre à trois questions : comment ça marche, comment on
vérifie que ça marche, comment on le retire.

# Files

- [9Router et OmniRoute au démarrage de Windows](routeurs-llm-locaux-autostart.md) - Les deux routeurs partagent le port 20128 par défaut et ne peuvent pas coexister ; 9Router se lie à `0.0.0.0` et s'arrête sur un menu interactif sans `--tray` ; OmniRoute lit `HOSTNAME`, pas `HOST`. Distingue les sources de quota (OpenRouter, AgentRouter, Ollama, NVIDIA) des couches de routage (OrcaRouter, OmniRoute, 9Router), qui n'en fournissent aucun. Mesure : zéro fournisseur connecté à ce jour.
- [Composio en gateway MCP cloud](composio-mcp-as-gateway.md) - L'endpoint For You est branché à la racine de `~/.mcp.json`, hors de l'agentgateway local, qui tombe dès qu'un seul MCP échoue au démarrage. Test Key Pragma passé : HTTP 200, 8 outils meta, 250+ outils d'apps joignables par recherche.
- [Les SaaS refusent l'embarquement en iframe](iframe-embedding-refuse.md) - Mesure directe des en-têtes sur 8 cibles : sept refusent. Le niveau « Easy » de l'App Store ne peut viser que de la documentation. Note aussi un chaînon manquant plus grave que l'iframe.
- [Herdr et Ori, le substrat d'orchestration](herdr-ori-substrat-orchestration.md) - Herdr émet 25 événements runtime (3 seulement abonnables) et offre un `agent wait --status` bloquant : la condition d'arrêt qu'un `sleep` ne donne jamais. Il détecte l'état par regex sur le terminal tant qu'aucun hook d'intégration n'est posé — et aucun ne l'est. Ori est un agent déclaratif à features TypeScript (35 événements runtime, schedules, skills). Il déclarait `codex`, `dsh` et `grok` non installés alors qu'ils sont bel et bien dans `~/.local/bin` : `ori.cmd` lançait WSL en shell non-login, donc sans ce répertoire au PATH — le même piège que les scripts de rotation de clés. Son `--help` cache six commandes hors workspace.
- [barehands, piloter le tableau à la main sans forker](barehands-instrument-de-revue.md) - Un `server.py` stdlib et un `stage.html` de 155 Ko. La licence AGPL interdit de le fondre dans Coach OS, mais son protocole HTTP le rend pilotable sans le modifier — et un orbe « notes » accepte n'importe quel dossier de markdown, donc le bundle OKF tel quel. Le tableau ne sait pas écrire : c'est le trou à combler pour tamponner un verdict de revue.
