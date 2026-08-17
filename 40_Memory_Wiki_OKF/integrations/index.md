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

- [Composio en gateway MCP cloud](composio-mcp-as-gateway.md) - L'endpoint For You est branché à la racine de `~/.mcp.json`, hors de l'agentgateway local, qui tombe dès qu'un seul MCP échoue au démarrage. Test Key Pragma passé : HTTP 200, 8 outils meta, 250+ outils d'apps joignables par recherche.
- [Les SaaS refusent l'embarquement en iframe](iframe-embedding-refuse.md) - Mesure directe des en-têtes sur 8 cibles : sept refusent. Le niveau « Easy » de l'App Store ne peut viser que de la documentation. Note aussi un chaînon manquant plus grave que l'iframe.
