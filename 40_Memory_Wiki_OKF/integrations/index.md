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
- [Herdr et Ori, le substrat d'orchestration](herdr-ori-substrat-orchestration.md) - Herdr emet 25 evenements runtime (3 seulement abonnables) et offre un `agent wait --status` bloquant : la condition d'arret qu'un `sleep` ne donne jamais. Sa doc de config n'existe pas sur disque — c'est un gabarit commente embarque dans le binaire. Ori n'est pas qu'un lanceur : c'est un **pont OpenRouter natif**, et `ori claude --model <id OpenRouter>` fait nativement ce que le relais maison fait pour Windows. Audit du 2026-08-29 : `mcp.json` absent (Ori refuse le stdio, tout doit etre `http`, et `ORI_MCP_CONFIG` est indispensable hors workspace), persona restee au gabarit de scaffolding avec Opus par defaut. Contient le piege `&&` interprete par cmd.exe a l'interieur de guillemets simples destines a `sh -c`.
- [Relais OpenRouter pour modèles custom](relais-openrouter-modeles-custom.md) - Claude Code CLI valide le nom du modèle localement et rejette tout id non-Anthropic avant le moindre appel réseau : router vers GLM 5.3 Flash ou Qwen 3.8 Flash exige un relais qui réécrit le champ `model` en vol, pas une ligne de configuration. La clé OpenRouter cherchée en vain dans OmniRoute, sur le disque et dans Hermes WSL était dans Hermes **Windows** — deux états indépendants pour un même outil des deux côtés de la frontière WSL. Persistance par tâche planifiée + gardien à sonde de port : relais tué, revenu seul en 54 s. Le mutex essayé n'exclut pas et le doublon de gardien diagnostiqué n'existait pas — la requête de comptage se comptait elle-même. Voir [[herdr-ori-substrat-orchestration]] : Ori rend ce service nativement côté WSL.
- [barehands, piloter le tableau à la main sans forker](barehands-instrument-de-revue.md) - Un `server.py` stdlib et un `stage.html` de 155 Ko. La licence AGPL interdit de le fondre dans Coach OS, mais son protocole HTTP le rend pilotable sans le modifier — et un orbe « notes » accepte n'importe quel dossier de markdown, donc le bundle OKF tel quel. Le tableau ne sait pas écrire : c'est le trou à combler pour tamponner un verdict de revue.
