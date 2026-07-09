---
id: YT-UztrFXaSWv0
title: "The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!"
channel: "Cole Medin"
duration: "24:39"
date: "2026-06-17"
category: "Loop Engineering / Harness Architecture / Agent Orchestration"
status: DISTILLED_L1_PREMIUM
domain: "03_IT"
ld: LD07_Creativity_Reno  # E1 fix (était: LD03_Health_Culber) — bijection D3
ld_owner: "Culber"
video_id: UztrFXaSWv0
url: https://www.youtube.com/watch?v=UztrFXaSWv0
transcript_source: TranscriptAPI.com MCP (D6 #43)
b2_owner: cyborg-it
sister_b1: jerry-prime
---

# 📖 The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore?!

> [!NOTE]
> Fiche de clarification d'excellence sémantique pour le Domaine 03_IT — Loop Engineering / Harness Architecture / Agent Orchestration. Standard Antigravity Premium (D6 #48).

---

## 🧠 Concepts Clés à Haute Densité Sémantique

- **<Loop Engineering — Définition>** : Écrire des loops qui pilotent tes agents 24/7 plutôt que de les prompter. Boris (Claude Code lead) : 'My job is to write loops.' 3 primitives : /loop (intervalle), /goal (criteria done), /routines (scheduled jobs). Le but = donner un scope large à l'agent qui travaille incrémentalement sans overwhelm.
- **<Problème #1 — Résultats Non-Optimaux>** : Boris prétend gérer des tens of thousands of AI agents/jour. Cole est sceptique : 'Is that going to scale ?' Loop engineering bon pour POC/exploration, pas pour drive principal d'un projet complexe. Le loop devient vite un générateur de médiocrité sans human-in-loop.
- **<Problème #2 — Coût Prohibitif>** : Run simple peut brûler 1M+ tokens parce que l'orchestrator reason sur le spec, spin off workers, prompt chacun, results reviennent, orchestrator re-reason. Solution Archon = per-node model choice (small model pour classify, big pour implementation). Klever routing = économie 60-80% sur workflows longs.
- **<Problème #3 — Context Bloat>** : /loop continue dans la même session, le context grossit jusqu'à overwhelm. Solution Archon = distribuer le travail entre sessions isolées via worktrees (Neon branches par agent) + handoff via markdown docs. Chaque agent a son context dédié, validé par evidence-based loop (/work jusqu'à completion).
- **<Archon — Harness Deterministe Open-Source>** : Workflow en YAML, orchestrator + workers dans sessions isolées, durabilité via Postgres (resume même si machine down), human-in-loop par node. Archon peut mixer providers par node (Haiku pour classify, Sonnet pour implementation, Kimi pour context loading). Architecture proof-by-evidence plutôt que proof-by-vibes.
- **<Loop Engineering = Harness Engineering>** : Cole termine : 'I would just fold loop engineering into harness engineering. It doesn't quite deserve its own buzzword.' Le vrai skill n'est pas dans la loop mais dans le harness qui la supporte — observability, durability, cost-control, human-in-loop nodes.

---

## 🛠️ Outillage Stratégique & Matrice d'Alignement

| Outil / Technologie / Approche | Rôle Stratégique | Alignement Souverain A'Space |
| :--- | :--- | :--- |
| **<Archon (open-source)>** | Harness deterministe pour orchestrating multi-agents avec durability Postgres et per-node model choice. | A'Space : symétrie avec Symphony runtime (ADR sur `00_Amadeus/05_OSS_Twin/symphony/`). |
| **<Worktrees + Neon branches>** | Isolation des agents via branches DB séparées. Évite les conflits cross-agent. | A'Space : Supabase Cloud branches par agent A3 (H3 Saru — gouvernance financière des coûts de branche). |
| **<Markdown docs as handoff>** | Format portable pour passer le contexte entre sessions agents. | A'Space : canonique dans `wiki/` Memory Core + format markdown strict. |
| **<Per-node model routing>** | Choisir le bon model par étape (classify=Haiku, code=Sonnet, review=Codex). | A'Space : router OpenRouter local + Niner smart router (D6 #48 priority). |

---

## 🪐 Perspective Souveraine A'Space 03_IT

Le loop engineering est au cœur de l'évolution agentique 2026 et aligne directement avec la doctrine A'Space Symphony. (1) **Niveau doctrine** : la thèse 'my job is to write loops' est l'extension naturelle de la doctrine D9 self-choice (ADR-META-002) — l'humain définit le 'quoi' et 'pourquoi', les agents définissent le 'comment'. (2) **Niveau architecture** : Archon open-source résout exactement les 3 problèmes (résultats/coût/context) via harness deterministe + per-node model routing + durability Postgres. A'Space doit importer ces patterns — Symphony Phase 3 pourrait ajouter un module 'harness-engineering' inspiré d'Archon. (3) **Niveau action A0 (H3 Saru)** : (a) skill `/symphony-fabuleux-discipline` invoqué pour orchestrer A3 sur benchmark Archon vs Symphony actuel, (b) expérimenter /loop + /routines sur 1 verticale OMK Tax Service pour valider le pattern. Doctrine Anti-Paresse : Archon a 0 marketing claim mais ses résultats sont open-source auditable — exactement le standard A'Space exige. Sister-skill `/symphony-fabuleux-discipline` recommandé.

---

## 🕹️ Protocole d'Exécution D.E.A.L

| Phase | Action Concrète | Objectif A'Space OS |
| :--- | :--- | :--- |
| **Définir** | Benchmark Archon (open-source) vs Symphony runtime actuel sur 1 verticale OMK Tax (10 workflows). | Identifier gaps et quick wins. |
| **Éliminer** | Pas applicable — Archon est compatible avec Symphony, pas concurrent. | N/A |
| **Automatiser** | Implémenter per-node model routing dans Symphony (Haiku classify + Sonnet implementation + Kimi context). | Économie 60-80% tokens + latence réduite. |
| **Libérer** | Documenter pattern harness-engineering comme canonique A'Space (wiki entry sur 'Loop Engineering & Harness Architecture'). | Doctrine canonique + référence pour futurs A3 twins. |

---

## 🔬 Annexes Détaillées de l'Audit Sémantique & Technique

### Note Note A3-01 : Comparaison Archon harness vs Symphony runtime

Archon (Cole Medin, open-source) = harnais déterministe pour orchestrer coding agents. Symphony (A'Space, canonique) = runtime A3 pour orchestrer business agents. Pattern commun : durability Postgres + human-in-loop + per-node routing. Différence : Archon focus code, Symphony focus business. Importation des patterns Archon dans Symphony Phase 3 = quick win.

### Note Note A3-02 : Token economics du loop engineering

1M+ tokens/run = coût réel à tracker. Si Sonnet à $3/M input + $15/M output, 1M tokens run moyen = ~$5. Avec Archon per-node routing, on peut descendre à Haiku pour classify (~$0.25/M) → économie 90% sur 50% du workflow = ~45% économie globale. Sister-skill `/symphony-fabuleux-discipline` peut prototyper.

### Note Note A3-03 : Anti-patterns à éviter dans le loop engineering

(1) Loop sans observability = 'go for a day and come back to crap', (2) loop sans durability DB = perte complète au crash, (3) loop sans human-in-loop = burn de tokens sans validation. Les 3 sont des deal-breakers pour production. Archon les adresse tous les 3.

---

*Fiche de connaissances souveraine d'03_IT générée sous A'Space OS V2 — Standard Antigravity Premium (D6 #48).*
