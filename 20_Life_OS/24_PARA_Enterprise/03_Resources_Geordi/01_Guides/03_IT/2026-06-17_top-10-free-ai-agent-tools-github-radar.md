---
id: YT-hu4-UzmDFRY
title: "I Found the 10 Best FREE AI Agent Tools on GitHub (#1 Has 193K Stars)"
channel: "ManuAGI - AutoGPT Tutorials"
duration: "10:21"
date: "2026-06-17"
category: "AI Agent Tooling / Open Source Radar / ASpace Stack Mapping"
status: DISTILLED_L1_PREMIUM
domain: "03_IT"
ld: LD07_Creativity_Reno  # E1 fix (était: LD03_Health_Culber) — bijection D3
ld_owner: "Culber"
video_id: hu4-UzmDFRY
url: https://www.youtube.com/watch?v=hu4-UzmDFRY
transcript_source: TranscriptAPI.com MCP (D6 #43)
b2_owner: cyborg-it
sister_b1: jerry-prime
---

# 📖 I Found the 10 Best FREE AI Agent Tools on GitHub (#1 Has 193K Stars)

> [!NOTE]
> Fiche de clarification d'excellence sémantique pour le Domaine 03_IT — AI Agent Tooling / Open Source Radar / ASpace Stack Mapping. Standard Antigravity Premium (D6 #48).

---

## 🧠 Concepts Clés à Haute Densité Sémantique

- **<Agent Reach — Capability Layer>** : Couche de capabilities qui donne aux agents 'yeux et oreilles' : lecture de pages web, recherche, sous-titres YouTube, RSS, intégration GitHub/X/Reddit/Bilibili/Xiaohongshu/LinkedIn/V2EX/WeChat. Cookies locales + multi-backend routing (swap broken integration) + doctor command pour diagnostics. Le problème résolu = agents qui hallucinent au lieu de chercher.
- **<CUA — Computer Use Agents>** : Infrastructure open-source pour agents qui pilotent OS complet (Linux/macOS/Windows/Android) via screenshots, shell, mouse, keyboard, gestures mobile. CUA-bench pour évaluation (OSWorld, ScreenSpot). Loom pour virtualization Mac Apple Silicon. Upgrade 'mon agent peut lire' vers 'mon agent peut agir'.
- **<Agent Memory — Mémoire Persistante>** : Mémoire persistante pour coding agents (Claude Code, GitHub Copilot CLI, Cursor, Gemini CLI, Codex CLI, Hermes, OpenClaw, OpenCode). Pipeline : capture tool use → filtre secrets → compress → index BM25+vectors → inject relevant. Réduit drastiquement token cost vs built-in memory files qui dumpent tout le contexte.
- **<Lazy Codex — Harnais Codex sur Gros Repos>** : Packages Omo comme harnais Codex. Workflow installé : /deep crée mémoire projet, /plan écrit avant code, /work exécute, /loop vérifie par evidence (pas vibes). Sub-roles : explorer, librarian, plan, codex ultra reviewer. Réduit chaos dans agentic coding.
- **<Hermes Agent — Agent qui Grandit avec Toi>** : CLI + personalities + sessions + memory + MCP + cron + skills + messaging gateway (Telegram, Discord, Slack, WhatsApp, Signal, Home Assistant). 6 backends terminal (local/Docker/SSH/Singularity/Modal/Daytona). Open-source agent runtime mature.
- **<Skill Spector — Security Scanner>** : Nvidia security scanner pour AI agent skills : 64 vulnerability patterns × 16 catégories (prompt injection, data exfiltration, privilege escalation, supply chain, output handling, memory poisoning, dangerous code, least privilege, MCP usage). 0-100 risk score, formats terminal/JSON/markdown/SARIF. Don't install agent magic blindly.
- **<Niner — Smart Router>** : Router local pour tools (Claude code, Codex, Cursor, Kline, Co-pilot, Anti-gravity). Compression RTK token saver (20-40% input savings). 3-tier fallback subscription → cheap → free. Real-time quotas tracking, multi-account, usage analytics. Keep experimenting without token burn punishment.

---

## 🛠️ Outillage Stratégique & Matrice d'Alignement

| Outil / Technologie / Approche | Rôle Stratégique | Alignement Souverain A'Space |
| :--- | :--- | :--- |
| **<Agent Reach (capability layer)>** | Donne accès web/YouTube/X aux agents. Multi-backend + doctor cmd. | A'Space : MCP `mcp-symphony-supabase` + Bright Data MCP + Mercury web fetcher. |
| **<CUA (Computer Use)>** | Agents qui pilotent OS via screenshots/clicks/keys. Cross-platform. | A'Space : alignement avec A3 twins qui pilotent des outils souverains (n8n UI, Obsidian vault, Postgres). |
| **<agent memory>** | Mémoire persistante pour coding agents. BM25+vectors index. | A'Space : intégration dans `wiki/` Memory Core canonique (cf. `wiki/index.md`). |
| **<Hermes agent>** | Agent runtime mature : CLI + personalities + MCP + cron + messaging. | A'Space : symétrie directe avec le runtime A'Space (Hermes = analog externe, A'Space Symphony = analog interne). |
| **<Skill Spector>** | Security scanner pour skills : 64 patterns × 16 catégories. | A'Space : à intégrer dans `skill-creator` workflow pour auto-audit skills avant publication. |
| **<Niner>** | Router cost-optimization : 3-tier fallback subscription → cheap → free. | A'Space : routing local pour minimiser coûts API entre OpenRouter + Claude + Mistral. |

---

## 🪐 Perspective Souveraine A'Space 03_IT

Ce radar ManuAGI est un inventaire tactique qui cartographie 1:1 avec l'architecture A'Space Symphony. Les 10 outils répondent à des pains réels que nos agents A3 rencontrent quotidiennement : (a) **Accès au monde externe** (Agent Reach ≡ Bright Data MCP + Mercury) — Spock (H30) doit orchestrer les agents qui requêtent le web pour la recherche concurrentielle et la veille marché. (b) **Action sur OS** (CUA) — utile pour OpenClaw et agents Desktop Commander MCP. (c) **Mémoire long-terme** (agent memory) — déjà partiellement implémenté dans `wiki/index.md` mais pourrait être renforcé via BM25+vectors sur Supabase Cloud. (d) **Harnais Codex** (lazy codex) — applicable directement au pipeline Symphony. (e) **Hermes agent** est l'open-source le plus proche de notre runtime A'Space — symétrie directe avec `00_Amadeus/05_OSS_Twin/symphony/`. (f) **Skill Spector** — devrait être intégré comme pre-publish hook du skill `/skill-creator`. (g) **Niner** — à prototyper comme routeur local entre OpenRouter + Anthropic + Mistral pour réduire coûts API. Action A0 (H3 Saru) : (1) skill `/symphony-fabuleux-discipline` invoqué pour orchestrer A3 sur le radar, (2) Skill Spector comme gate pré-publication, (3) benchmark Niner vs setup actuel sur 1 verticale.

---

## 🕹️ Protocole d'Exécution D.E.A.L

| Phase | Action Concrète | Objectif A'Space OS |
| :--- | :--- | :--- |
| **Définir** | Cartographier 1:1 les 10 outils radar avec les composants A'Space existants (Hermes ↔ Symphony, Agent Reach ↔ Bright Data MCP, etc.). | Identifier gaps fonctionnels + overlaps + dépendances. |
| **Éliminer** | Supprimer les outils redondants ou non-souverains déjà remplacés par A'Space (ex: pas besoin de Niner si OpenRouter offre déjà fallback). | Réduire surface d'attaque + complexité stack. |
| **Automatiser** | Intégrer Skill Spector dans workflow `/skill-creator` comme pre-publish hook (auto-audit des skills avant publication). | Sécurité skills par défaut — D7 cost-of-escalation = skill malicieux = D7 immédiat. |
| **Libérer** | Benchmark Niner vs setup actuel sur 1 verticale (OMK Tax Service) — mesurer économie réelle. | Réduction burn rate API + autonomie face aux rate-limits providers. |

---

## 🔬 Annexes Détaillées de l'Audit Sémantique & Technique

### Note Note A3-01 : Comparaison Hermes (open-source) vs A'Space Symphony (canonique)

Hermes est mature (CLI + personalities + sessions + memory + MCP + cron + skills + messaging + 6 backends terminal). A'Space Symphony a les mêmes primitives mais avec couche canonique 35 A3 twins + OpenSpec governance. Pas de duplication — plutôt : importer les patterns d'Hermes qui manquent à Symphony (ex: personnalités configurables, sessions persistantes inter-agents).

### Note Note A3-02 : Skill Spector — Intégration workflow skill-creator

Pre-publish hook : à chaque création de skill via `/skill-creator`, scanner avec Skill Spector les 64 vulnerability patterns. Si score > 30 → bloquer la publication + retourner le rapport à l'auteur. Si score < 30 → publish. Cela garantit que le canon A'Space reste secure-by-default.

### Note Note A3-03 : Niner vs OpenRouter fallback — Test A/B

Niner compression RTK = 20-40% tokens saved sur tool outputs. OpenRouter a déjà un fallback multi-provider mais sans compression. Hypothèse : Niner + OpenRouter = optimal (Niner compresse AVANT d'envoyer à OpenRouter qui route au provider optimal). Test sur 1000 requêtes Symphony en production pour mesurer économie réelle.

---

*Fiche de connaissances souveraine d'03_IT générée sous A'Space OS V2 — Standard Antigravity Premium (D6 #48).*
