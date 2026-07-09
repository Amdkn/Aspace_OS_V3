---
source: A0 Amadeus (intention stratégique, 2026-06-05) + governance dashboard live + MiniMax Plus plan
date: 2026-06-05
type: concept
domain: L0/L1/L2 orchestration — plan de reprise (Shadow → autonome)
status: ACTIVE (forward plan — précède activation Open Hermes ÉTAT 3)
tags: [#shadow_l0 #shadow_l1 #shadow_l2 #hermes_desktop #hermes_workspace #telegram #minimax #caddy #13th_doctor #governance_dashboard #reprise]
---

# 🔭 Concept — Reprise Shadow L0 → L1 → L2 (le terrain est prêt)

> Capté de l'intention A0 du 2026-06-05. Décrit **qui reprend quoi** maintenant que les 3 Shadow L0
> (Codex / Gemini / Claude Code) ont préparé le terrain. Aligné ADR-RICK-002 (Hermes promotion),
> ADR-INFRA-001 (console unifiée), `05_OSS_Twin/symphony/L0/open-hermes-runtime.md` (ÉTAT 3).

## 1. Le mouvement
Les **3 opérateurs Shadow L0** (Codex infra Windows · Gemini long-context · Claude Code reasoning) ont
**préparé le terrain**. La reprise s'organise par couche, chacune incarnée par une instance Hermes :

| Couche | Incarnation | Lieu | Connexion | Rôle |
|---|---|---|---|---|
| **Shadow L1** | **Hermes Desktop** (Nous Research) | **Local Windows** | **Telegram** (canal A0 async) | back-office Life OS, présence A0 sleep-safe |
| **Shadow L2** | **Hermes Workspace** | **VPS** (148.230.92.235) | Dashboard gouvernance + Caddy | Business Pulse, exécution, infra |

> Distinction canon (ADR-HERMES-001) : **Hermes Desktop = Nous Research natif Windows** (≠ fathah/hermes-desktop, purgé).
> Hermes Workspace = remote VPS. Ils ne se télescopent plus.

## 2. Shadow L2 — Hermes Workspace VPS (déjà debout)
- **Dashboard de gouvernance d'infrastructure** : `aspace-dashboard.148.230.92.235.sslip.io` (ADR-INFRA-001).
  - Surfaces vues live (2026-06-06) : **Hermes Agent** (Dashboard+Kanban), **Workspace** (remote agent UI),
    **Dokploy** (déploiements), **Supabase Studio**, **Infrastructure** (CPU/disk/mem), **Tokens**, **Supabase health**.
  - **Token Governance** : 22 inventaire · 5 high-risk · 22 unknown-expiry · 0 broken. Valeurs **jamais stockées/rendues**
    (empreintes SHA-256 seulement). À annoter : `API_SERVER_KEY`, `OPENROUTER_API_KEY` (Hermes), etc. = `unknown-expiry/high`.
- **Surfaces Caddy** = les liens HTTPS des interfaces du **13ème Docteur** (infra) exposées via Caddy reverse-proxy + sslip.io.
- **Doc-ownership** (ADR-INFRA-001 D3) : Codex documente **local Windows** ; Hermes documente **dans le VPS** ; Claude Code réconcilie.

## 3. Le moteur LLM — MiniMax Plus (frugalité ADR-RICK-002)
- **Plan repris** : MiniMax **Monthly Plus $20/mois** (Stripe, order 2062860963412980668, expire 2026-07-05, auto-renewal OFF).
- **Specs Plus** : famille M3/M2.7/image/speech/music · **3–4 agents concurrents** · **fenêtre 1M contexte** · ~1.7B tokens M3/mois.
- **Quota** : ~**4500 requêtes / 5h**. **API Anthropic-compatible** → branché comme backend **Claude Code CLI**
  (et Hermes Agents A3). Premium Anthropic-cloud réservé arbitrages Rick A1 critiques.
- Doctrine : *les couches sont souveraines, les modèles sont des véhicules* — MiniMax/GLM par défaut, ~100× moins cher.

## 4. Schéma de reprise
```
A0 (Telegram async + dashboard)
   │
   ├── Shadow L1  = Hermes Desktop (Nous, Windows local) ──Telegram──> A0
   │        backend : MiniMax Plus (z-ai/glm-4.7-flash default, cf. ~/.hermes/memories/config.yaml)
   │
   └── Shadow L2  = Hermes Workspace (VPS)
            ├── Dashboard gouvernance (Caddy/sslip.io) : Hermes Agent · Workspace · Dokploy · Supabase · Tokens
            ├── 13ème Docteur interfaces (surfaces Caddy)
            └── Claude Code CLI ← API Anthropic-compatible MiniMax ($20/mo, 4500 req/5h)
```

## 5. Lien avec la supervision orchestration
Ce plan de reprise est l'**ÉTAT cible** que le plan de supervision
(`05_OSS_Twin/symphony/SUPERVISION.symphony-hermes.draft.md`) doit encadrer :
Symphony (B1 router) + Hermes Agent (:3101) tournent en L2 VPS ; Yaz les veille ; Donna escalade vers
A0 par **Telegram** (le canal Shadow L1) ; le dashboard les surface. Veto 90j toujours actif → activation phasée.

## 6. Prochains crochets (quand A0 autorise)
1. Annoter les 22 tokens `unknown-expiry` du Token Governance (People/X-Men + Yaz scan secrets).
2. Câbler le panneau `/orchestration` (queue depth, runs, coût, DLQ) — Hermes documente dans le VPS.
3. Brancher Donna DLQ → Telegram MCP (escalade A0 sleep-safe).
4. Confirmer `~/.hermes/memories/config.yaml` `model.default` vs MiniMax Plus (cohérence backend).

*Concept forward — capté 2026-06-05. Le terrain Shadow L0 est prêt ; L1 (Hermes Desktop/Telegram) + L2 (Hermes Workspace/VPS) reprennent.*
