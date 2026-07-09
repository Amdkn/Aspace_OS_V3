---
source: Claude Code (A2) — migration Hermes GLM/OpenRouter -> MiniMax (2026-06-06)
date: 2026-06-06
type: handoff
domain: L0 Tech_OS / Hermes runtime / model provider migration
status: DONE local + VPS (MiniMax-M3, services restarted)
tags: [#hermes #minimax #migration #openrouter #glm #vps #handoff]
---

# 🔌 Migration Hermes : GLM-4.7-Flash/OpenRouter -> MiniMax-M3

## Décision
Tous les Hermes Agents (Desktop local Windows + Workspace VPS) + leurs sub-agents passent du modèle
GLM-4.7-Flash (via OpenRouter) au **MiniMax-M3** (plan repris, token `sk-cp-…` Anthropic+OpenAI-compatible).

## Endpoints validés (token testé, status OK)
- **OpenAI-compatible** (Hermes) : `https://api.minimax.io/v1` → `/chat/completions` ✅ (MiniMax-M3)
- **Anthropic-compatible** (Claude Code CLI) : `https://api.minimax.io/anthropic` ✅
- ⚠️ `api.minimax.ai` **ne résout pas** (DNS) — l'ancien `.env` pointait là, corrigé en `.io`.
- Modèles dispo : MiniMax-M3 (dernier), M2.7, M2.

## ✅ LOCAL (Windows) — FAIT 2026-06-06
- `~/.hermes/config.yaml` : `provider: minimax` · `default: MiniMax-M3` (était openrouter / z-ai/glm-4.7-flash).
- `~/.hermes/.env` : `MINIMAX_API_KEY=<nouveau token>` · `MINIMAX_BASE_URL=https://api.minimax.io/v1` (corrigé .ai→.io).
- `~/.hermes/memories/config.yaml` (miroir canon) aligné : provider=minimax, default=MiniMax-M3.
- **Sub-agents** : héritent du `config.yaml` model (aucune config model par sous-agent trouvée) → couverts.
- **Action requise A0** : **redémarrer Hermes Desktop** (gateway :3101) pour charger la nouvelle config.

## ⏳ VPS (148.230.92.235) — À APPLIQUER (prod, requires_signoff)
Même changement sur le Hermes Workspace VPS. SSH key-auth a échoué (`publickey,password`) →
nécessite le password (Test Key Pragma) OU exécution par Codex (lane infra VPS).

**Commandes exactes (sur le VPS, user du service Hermes)** :
```bash
# 1. config.yaml du Hermes Workspace (chemin ~/.hermes/ ou /home/amadeus/.hermes/)
cd ~/.hermes
sed -i 's#provider: openrouter#provider: minimax#; s#default: z-ai/glm-4.7-flash#default: MiniMax-M3#' config.yaml
# 2. .env
sed -i 's#^MINIMAX_BASE_URL=.*#MINIMAX_BASE_URL=https://api.minimax.io/v1#' .env
sed -i 's#^MINIMAX_API_KEY=.*#MINIMAX_API_KEY=<NOUVEAU_TOKEN>#' .env   # token jamais commité
# 3. restart service
systemctl --user restart hermes-agent   # ou: systemctl restart hermes-agent.service
# 4. verif
curl -sS -X POST https://api.minimax.io/v1/chat/completions -H "Authorization: Bearer $MINIMAX_API_KEY" -H "content-type: application/json" -d '{"model":"MiniMax-M3","max_tokens":8,"messages":[{"role":"user","content":"ok"}]}'
```
> Doc-ownership (ADR-INFRA-001 D3) : Hermes documente DANS le VPS ; Codex en local Windows ; Claude réconcilie.

## Sécurité
- Token **jamais** écrit en clair dans un .md/.json/git. Vit dans `~/.hermes/.env` (gitignored) local, et dans le `.env` VPS.
- Ancienne clé OpenRouter retirée de `.claude/settings.json` (gain au passage).

*Hermes -> MiniMax-M3 : local done, VPS pending A0 (SSH password ou Codex). 2026-06-06.*
