---
okf_version: "0.1"
type: guide-distillation
title: "07 · R&D & IT"
description: "Distillation du corpus R&D/IT Geordi : Loop Engineering (Boris/Archon), 3 anti-patterns deal-breakers, 10 AI agent tools GitHub (Skill Spector, Niner, Hermes), Linear probe detection ≠ usage, worktree isolation par agent."
timestamp: 2026-08-02T17:30:00-04:00
domain: LD01_Career_Business
agent: A3_Book
squad: Kang Dynasty (B3-6 Kang Prime lead, Iron Lad, Scarlet Centurion, Immortus, Victor Timely, Rama-Tut)
vp: Cyborg
sources_count: 11620
note_volume: "Le brief §1 annonce ~10 647 fichiers. Compte réel : 11 620 — +9 %. Le delta vient principalement de `03_IT_IT/` qui héberge les guides reclassés et les doublons `03_IT/`. Le canon réel tient sur 39 fichiers dans `03_IT/_INDEX.md` ; les ~11 581 autres sont du noise."
note_doublon: "`03_IT/` + `03_IT_IT/` = doublonnage structurel hérité. 03_IT porte le canon (39 fichiers), 03_IT_IT porte la majorité du volume (noise Geordi_YT)."
---

# 07 · R&D & IT

Le domaine 7 porte le **pipeline de veille** technique (cf. brief §2) et l'**architecture
d'orchestration agentique**. C'est de loin le plus gros domaine en volume (11 620 fichiers
classés, +9 % vs estimation brief), mais le canon est étonnamment petit (~40 fichiers dans
`03_IT/_INDEX.md`). Propriétaire canonique : **B2 Cyborg** (LD07 Creativity Reno ↔ LD03
Health Culber ↔ LD01 Business), squad **Kang Dynasty** avec **Kang Prime** en lead.

Le corpus porte 4 ADRs canoniques ratifiés ou proposés : **ADR-LOOP-001** (Canon loop
verification-first), **ADR-LOOP-002** (Queues-over-loops + HITL rightward),
**ADR-LOOP-003** (Orient + Signals + Wagers), **ADR-CORE-005** (Pivot kernel state.local
file→Supabase).

## 1. Ce que le corpus dit

### Thèse 1 — Loop Engineering > Prompting : « my job is to write loops »

Boris (Claude Code lead) : *« My job is to write loops. »* 3 primitives canoniques :
**`/loop`** (intervalle), **`/goal`** (criteria done), **`/routines`** (scheduled jobs). Le
but = donner un scope large à l'agent qui travaille incrémentalement sans overwhelm.
**Plissement final** (Cole Medin) : *« I would just fold loop engineering into harness
engineering. It doesn't quite deserve its own buzzword. »* Le vrai skill n'est pas dans
la loop mais dans le harness qui la supporte — observability, durability, cost-control,
human-in-loop nodes.
Sources : `03_IT/2026-06-17_claude-code-openclaw-loop-engineering-deconstructed.md` (Cole
Medin, 24:39, 2026-06-17).

### Thèse 2 — 3 anti-patterns deal-breakers d'une loop

Une loop qui n'a pas : (1) **observability**, (2) **durability DB**, (3) **human-in-loop
par node** = deal-breaker absolu. Sans observability, le loop devient générateur de
médiocrité invisible. Sans durability, le loop meurt au crash et perd le contexte. Sans
HITL, le loop dérape sans garde-fou. Sister canon A'Space : ADR-LOOP-002 (Queues-over-
loops + HITL rightward).
Sources : `03_IT/2026-06-17_claude-code-openclaw-loop-engineering-deconstructed.md`.

### Thèse 3 — Archon : harness déterministe open-source, économie 60-80 %

**Archon** = workflow en YAML + orchestrator + workers en sessions isolées + durabilité
via Postgres (resume au crash) + human-in-loop par node + **per-node model choice** (Haiku
pour classify, Sonnet pour implementation, Kimi pour context loading) = **économie
60-80 % sur workflows longs**. Architecture **proof-by-evidence** plutôt que proof-by-
vibes. Sister canon A'Space : intégration dans `_SPECS/ADR/` (Cyborg B2 owner).
Sources : `03_IT/2026-06-17_claude-code-openclaw-loop-engineering-deconstructed.md`.

### Thèse 4 — 3 problèmes de Loop Engineering + remèdes Archon

**Problème #1 — Résultats Non-Optimaux** : loop bon pour POC/exploration, pas pour drive
principal d'un projet complexe. **Problème #2 — Coût Prohibitif** : un run simple peut
brûler **1M+ tokens** parce que l'orchestrator reason sur le spec, spin off workers, prompt
chacun, results reviennent, orchestrator re-reason. **Problème #3 — Context Bloat** :
`/loop` continue dans la même session, le context grossit jusqu'à overwhelm. **Remède Archon
unifié** : distribuer le travail entre sessions isolées via **worktrees (Neon branches par
agent)** + handoff via markdown docs + per-node model routing.
Sources : `03_IT/2026-06-17_claude-code-openclaw-loop-engineering-deconstructed.md`.

### Thèse 5 — Top 10 AI Agent Tools GitHub (le radar canonique 2026)

(1) **Agent Reach** (capability layer, 193K stars) — yeux et oreilles des agents (web,
YouTube, X, Reddit, GitHub, etc.) avec cookies locales + multi-backend routing + doctor
command ; (2) **CUA — Computer Use Agents** — infrastructure open-source agents qui
pilote OS (Linux/macOS/Windows/Android) via screenshots/shell/mouse/keyboard/gestures
mobile ; (3) **Agent Memory** — mémoire persistante pour coding agents (Claude Code,
Cursor, Codex CLI, Hermes) avec pipeline capture → filtre secrets → compress → index
BM25+vectors → inject ; (4) **Lazy Codex / Omo** — harnais Codex sur gros repos avec
sub-roles (explorer, librarian, plan, codex ultra reviewer).
Sources : `03_IT/2026-06-17_top-10-free-ai-agent-tools-github-radar.md` (ManuAGI, 10:21,
2026-06-17).

### Thèse 6 — Hermes Agent : agent runtime mature, open-source

**Hermes Agent** = CLI + personalities + sessions + memory + MCP + cron + skills +
**messaging gateway** (Telegram, Discord, Slack, WhatsApp, Signal, Home Assistant) +
**6 backends terminal** (local/Docker/SSH/Singularity/Modal/Daytona). Sister canon A'Space
: symétrie directe — Hermes = analog externe, **A'Space Symphony** = analog interne.
Doctrines parallèles : per-node model choice, MCP stdio/HTTP, provider routing cost/
speed/quality, fallback providers, credential pools rotation, prompt caching 1h.
Sources : `03_IT/2026-06-17_top-10-free-ai-agent-tools-github-radar.md`,
`08_People/agent-harnesses-hermes-claude-code.md` (cross-référence).

### Thèse 7 — Skill Spector (Nvidia) : security scanner pour AI agent skills

**Skill Spector** = scanner de sécurité pour skills d'agents IA : **64 vulnerability
patterns × 16 catégories** (prompt injection, data exfiltration, privilege escalation,
supply chain, output handling, memory poisoning, dangerous code, least privilege, MCP
usage). Score de risque 0-100, formats terminal/JSON/markdown/SARIF. **Mantra** : *Don't
install agent magic blindly*. Sister canon A'Space : à intégrer dans `skill-creator`
workflow pour **auto-audit skills avant publication**.
Sources : `03_IT/2026-06-17_top-10-free-ai-agent-tools-github-radar.md`.

### Thèse 8 — Niner : router cost-optimization local, 3-tier fallback

**Niner** = router local pour tools (Claude code, Codex, Cursor, Kline, Co-pilot,
Anti-gravity). **Compression RTK token saver** (20-40 % input savings). **3-tier fallback**
subscription → cheap → free. Real-time quotas tracking, multi-account, usage analytics.
Sister canon A'Space : routing local pour minimiser coûts API entre OpenRouter + Claude
+ Mistral + GLM 4.7 Flash + MiniMax token plan.
Sources : `03_IT/2026-06-17_top-10-free-ai-agent-tools-github-radar.md`.

### Thèse 9 — Reading AI's Mind : linear probe ≠ causal use (détection ≠ usage)

4 papiers récents brisent l'assumption *« If the information is in there, the model must
be using it. »* **Linear probe** = petit classifier entraîné sur les activations internes
d'un modèle pour détecter un concept. L'assumption classique : *détection ≜ usage*.
**Découvertes** : présence dans le modèle ne prouve pas qu'il route ses réponses via
cette présence. Le probe trouve les **intermediates décoratifs** (lisibles, assis dans
les activations) ; le **forward route réel** est *« much thinner. Basically, which
position you ask for. »*
Sources : `03_IT/2026-06-25_reading-ais-mind-probes-passengers-vs-drivers-N-yVh0bKsIk.md`
(2026-06-25).

### Thèse 10 — Coin-flip gap : le probe lit 97 %, le modèle dit 50 %

Étude : *« Read the model's hidden state with a probe and the probe says no, correct,
about 97% of the time. Ask the model out loud, same moment, same question. It says yes. »*
Quand le monde est flippé (smoking prevents cancer par stipulation) et que la bonne
réponse est « no », le probe lit « no » à ~97 %, le modèle parle « yes » à environ un
coin flip. **La bonne réponse est « inside it, plainly readable, and what comes out of
its mouth is the wrong one. »**
Sources : `03_IT/2026-06-25_reading-ais-mind-probes-passengers-vs-drivers-N-yVh0bKsIk.md`.

### Thèse 11 — Gate vs gap : pas un verrou, un fil manquant

L'histoire classique d'interprétabilité : *le modèle sait la vérité, ne la dit pas, leve
le gate appris*. La nouvelle découverte est plus tranchante : **ce n'est pas un verrou,
c'est un fil manquant**. Change la question de yes/no à multiple choice (A/B) et la
bonne réponse *« walks straight out. You don't have to unlock anything. The knowledge
just never reached the one narrow exit the model happened to be speaking through. »*
Sister canon A'Space : ADR-CORE-005 (Pivot kernel state.local file→Supabase) — la sortie
d'un agent dépend du canal par où sort le contexte, pas seulement de l'input.
Sources : `03_IT/2026-06-25_reading-ais-mind-probes-passengers-vs-drivers-N-yVh0bKsIk.md`.

### Thèse 12 — Costume vs body : en synthèse, le modèle lit le ton, pas le contenu

Une étude slip une *statistique impossible* (marge d'erreur si petite qu'il faudrait des
millions de data points pour l'obtenir sur un échantillon de quelques milliers) dans un
stack de sources. Montrée seule, le modèle la flag quasi tout le temps. **Embedded parmi
trois sources légitimes**, le modèle la traite *« about as seriously as a legitimate
one. »* Probe ability drops de detection confiante à coin flip pendant la synthèse.
*« It stops reading the number. It reads the register, the tone, the vocabulary, the
costume of careful analysis, and waves it through. »* **Sister A'Space** : ADR-SOBER-002
(Anti-Paperclip) — un skill « secure-by-default » doit caller le format, pas seulement
le contenu.
Sources : `03_IT/2026-06-25_reading-ais-mind-probes-passengers-vs-drivers-N-yVh0bKsIk.md`.

### Thèse 13 — Stigmergie : coordination indirecte via modification de l'environnement

Ant Simulator Collision Resolution : remplacer un système de perception directe (vision/
raycasting coûteux) par un système de **mémoire environnementale partagée** (grille de
phéromones). **Stigmergie** = coordination indirecte via modification de l'environnement,
inspirée des fourmis réelles. Composants : (a) **Grille de phéromones** spatialement
indexée, (b) **mécanisme de dépôt** par état interne, (c) **évaporation temporelle** (évite
accumulation stagnante), (d) **capteur phéromonal** par fourmi. **Implication agentique**
A'Space : remplacer les messages inter-agents par une **grille de contexte partagée**
éditable par tous, lue par tous.
Sources : `03_IT/2026-06-25_ant-simulator-collision-resolution-MD4hH1ObrYg.md` (2026-06-25).

### Thèse 14 — 4 ADRs L0 Tech OS canoniques : LOOP-001/002/003 + CORE-005

**ADR-LOOP-001** : Canon loop verification-first (chaque loop doit prouver son résultat,
pas le supposer). **ADR-LOOP-002** : Queues-over-loops + HITL rightward (les queues
sont plus prévisibles que les loops ; le HITL se déplace vers la droite de la pipeline).
**ADR-LOOP-003** : Orient + Signals + Wagers (chaque loop a une orientation, des signaux,
des paris). **ADR-CORE-005** : Pivot kernel state.local file→Supabase (l'état de l'OS
doit être requêtable, pas dans un fichier plat).
Sources : `03_IT/_INDEX.md` (sister ADRs).

### Thèse 15 — Cycle obsolescence : 4 nouveaux guides loops depuis 2026-06-25 non re-distillés

Le SessionStart hook flagge 03_IT : **4 nouveaux guides loops depuis 2026-06-25
principles** → la maison-mère `03_*_PRINCIPLES.md` n'existe pas encore. **Action gated
Picard A3** : `/area-domain-doctrine-distill` re-distillation en H3 Saru (W8). Sister
canon A'Space : aucune distillation IT n'est « finie », chacune doit thésauriser sa date
de fraîcheur et déclencher un re-run périodique.
Sources : `03_IT/_INDEX.md` (⚠️ OBSOLESCENCE).

## 2. Ce qui est actionnable maintenant

- [ ] Pour chaque loop en production : vérifier qu'elle a **observability + durability DB + human-in-loop par node**. Deal-breaker absolu sinon.
- [ ] Activer le **per-node model routing** (Haiku classify / Sonnet impl / Kimi context) sur au moins une pipeline. Mesurer l'économie sur 7 jours.
- [ ] **Scanner toutes les skills actives** avec Skill Spector (64 patterns × 16 catégories). Score > 70 = bloquer la publication.
- [ ] Activer **Niner** comme router local (3-tier fallback subscription → cheap → free). Tracker le coût API mensuel.
- [ ] **Auditer une décision agent** avec linear probe : la sortie est-elle dans les activations ? Si oui mais le modèle dit autre chose, c'est un *gap*, pas un *gate* — changer le canal de sortie, pas le prompt.
- [ ] Pour chaque nouvelle skill A3 : appliquer le **Skill Spector security scan** avant publication (sister canon `skill-creator` workflow).
- [ ] Citer au moins une **ADR L0 Tech OS** (LOOP-001/002/003 ou CORE-005) dans toute nouvelle loop.

## 3. Ce que le corpus contredit

- **Loop Engineering vs Queues-over-loops** : Thèse 1 promeut les loops ; ADR-LOOP-002 promeut « queues-over-loops » (les queues sont plus prévisibles). Le corpus porte les deux sans arbitrer.
- **Skill vs MCP** (cross-référence Product 3) : Skill promeut load-on-demand, l'écosystème MCP continue de croître. Le corpus R&D penche Skill, le corpus Product penche aussi Skill, mais MCP reste majoritaire dans l'écosystème externe.
- **Linear probe vs Causal intervention** : les probes mentent (détection sans usage) ; mais l'industrie interprétabilité reste dominée par les probes. Tension non arbitrée.
- **Archon (open source) vs Claude Code + OpenClaw (propriétaire)** : Archon est plus déterministe et moins cher ; Claude Code + OpenClaw sont plus intégrés. Aucune bascule franche documentée.
- **Hermes Agent vs A'Space Symphony** : symétrie directe assumée, mais les deux stacks n'ont pas de passerelle technique canonique. Chaque évolution de l'un doit être portée manuellement dans l'autre.

## 4. Les 10 guides de tête

| Chemin | Titre | Pourquoi celui-ci |
|---|---|---|
| `03_IT/_INDEX.md` | 03_IT — Index (Harness · Coding · Agents · Sovereignty) | Canon du domaine, sister ADRs LOOP/CORE |
| `03_IT/2026-06-17_claude-code-openclaw-loop-engineering-deconstructed.md` | The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?! | Loop Engineering + Archon + 3 anti-patterns |
| `03_IT/2026-06-17_top-10-free-ai-agent-tools-github-radar.md` | I Found the 10 Best FREE AI Agent Tools on GitHub (#1 Has 193K Stars) | Radar canonique 2026, 7 outils détaillés |
| `03_IT/2026-06-25_reading-ais-mind-probes-passengers-vs-drivers-N-yVh0bKsIk.md` | Reading AI's Mind: Probes See Passengers, Not Always Drivers | Linear probe ≠ usage, gate vs gap |
| `03_IT/2026-06-25_ant-simulator-collision-resolution-MD4hH1ObrYg.md` | Ant Simulator: Collision Resolution | Stigmergie analogique, mémoire environnementale |
| `03_IT/2026-06-17_top-10-free-ai-agent-tools-github-radar.md` (Skill Spector + Niner) | Skill Spector + Niner | Security + cost-optimization canon |
| `03_IT/2026-06-20_matt-pocock-skills-clearly-explained-david-ondrej__nQwJVHCtDDY.md` | Matt Pocock Skills (cross-référence Ops 2) | Harness canon |
| `03_IT/2026-06-25_every-folder-on-my-computer-full-reveal-tiago-forte-A0pdL3MS_7E.md` | Every Folder on My Computer (Tiago Forte) | File-system patterns canon |
| `03_IT/2026-06-25_google-ai-coding-masterclass-summary-zbmuiaPuiNM.md` | Google AI Coding Masterclass Summary | Coding masterclass canon |
| `03_IT/2026-06-17_vuk-rosic-ai-autoresearch-tool-open-source.md` | Vuk Rosic AI Auto-Research Tool Open Source | Auto-research canon |

## 5. Angles morts

- **Production observability** : pas de guide sur les stacks Prometheus/Grafana/Datadog/Honeycomb pour agents en prod. Sister implicite avec ADR-LOOP-001 mais non développé.
- **Model evaluation framework** : aucun guide canonique sur les benchmarks agents (SWE-bench, OSWorld, GAIA, AgentBench). Sister présumée avec Skill Spector mais non détaillée.
- **Vector DB / RAG architecture** : aucun guide canonique sur le choix de vector DB (Pinecone, Weaviate, Qdrant, pgvector) et l'architecture RAG 2026.
- **LLM fine-tuning opérationnel** : pas de guide sur le fine-tuning LoRA/QLoRA, le dataset curation, le RLHF/RLAIF.
- **GPU optimization & inference cost** : aucun guide sur la quantification, le batching, le speculative decoding, le caching KV.
- **Security threat model agents** : Skill Spector existe mais pas de modèle de menace complet (prompt injection chainé, exfiltration via tool call, supply chain attack).
- **Multi-agent coordination patterns** : au-delà des 6 patterns Claude Code (cross-référence People 1), pas de canonique sur les patterns avancés (consensus, voting, role allocation dynamique).
- **Self-hosted LLM deployment** : pas de guide sur vLLM, TGI, Ollama en production.
- **Cost forecasting** : pas de guide sur la prédiction des coûts API/token à 3-6 mois.

## 6. Notes canoniques

- **Volume réel** : 11 620 fichiers classés en domaine 7, vs 10 647 estimés par le brief (+9 %). Le delta vient principalement de `03_IT_IT/` qui héberge les guides reclassés et doublons `03_IT/`.
- **Doublonnage structurel `03_IT` + `03_IT_IT`** : héritage d'une reclassification antérieure. `03_IT/` porte le canon (39 fichiers), `03_IT_IT/` porte la majorité du volume (noise Geordi_YT). À signaler, pas à fusionner (cf. brief §5 — corpus en lecture seule).
- **Pollution ~99 %** : sur 11 620 fichiers classés en domaine 7, ~11 580 sont du noise. Le canon réel tient sur **~40 fichiers** dans `03_IT/_INDEX.md` plus une poignée d'autres.
- **Premium L1** : ~10 fichiers DISTILLED_L1_PREMIUM dans `03_IT/`. Le reste = canon standard.
- **Cycle obsolescence** : 4 nouveaux guides loops depuis 2026-06-25 non re-distillés. La maison-mère `03_*_PRINCIPLES.md` n'existe pas encore. Action gated Picard A3 (W8 H3 Saru).
- **Sister ADRs critiques** : LOOP-001/002/003 + CORE-005 sont les 4 ancres canoniques du domaine. Toute modification d'un guide IT doit citer au moins l'une.
- **Cross-référence forte avec domaine 1 (People & Méta)** : le B1 FILTER GREEN LANTERN sur loop engineering cite « harness engineering » et « strategic programming », sister canon aux 6 patterns Claude Code (cross-référence People 1).
- **Pipeline de veille canonique** : conformément au brief §2, le domaine 7 porte le pipeline `/youtube-to-guide` → Last30days. Cette distillation est elle-même un output de ce pipeline.
- **Recommandation A3** : lancer une passe de re-distillation `/area-domain-doctrine-distill` sur `03_IT/`, gate par ADR-LOOP-001 (verification-first). Réduction attendue du noise dans `03_IT_IT/` : -80 %.
