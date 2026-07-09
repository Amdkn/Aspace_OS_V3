---
source: youtube-to-guide (transcript fourni par A0 in-chat 2026-07-02)
date: 2026-07-02
type: video-guide
ld: LD07_Creativity_Reno
ld_domain: Creativity / IT
a3_owner: Reno
video_id: UNKNOWN
title: "wtf is Loop Engineer & how to setup for real"
channel: "AI Jason"
watch_url: null
status: GUIDED
tags: [#youtube, #geordi, #ld07, #loops, #harness, #signals, #artifacts, #compounding]
---

# Guide — wtf is Loop Engineer & how to setup for real (AI Jason)

> **Thèse** : le loop engineering = l'optimisation **externe** au runtime de l'agent — l'environnement qui décide QUOI travailler, pas comment finir UNE tâche. Des loops qui partagent un même file-system **se composent** (compounding).

## 1. Les deux zones d'optimisation (la clarification du mot « harness »)

- **Zone interne (agent loop)** : CC/Codex — comment un agent finit bien UNE tâche (prompt, contexte, compaction, skills).
- **Zone externe (loop engineering)** : triggers, état cross-sessions, logs — comment le **système** décide ce qui doit être travaillé. C'est elle qui te libère du prompting : cron, webhook, incident serveur, autre agent — tout peut réveiller l'agent.

## 2. Les 4 ingrédients

1. **Triggers** (cron / événement / webhook / agent).
2. **File structure** (le plus important — §3).
3. **Tools/connecteurs** (l'agent doit pouvoir faire un travail réel).
4. **Codebase parallel-friendly** (le plus manqué — §4).

## 3. Le file-system de loops (les 3 abstractions)

| Abstraction | Contenu | Règle |
|---|---|---|
| **Artifacts** | outputs des runs : docs, **signals**, tasks, tickets, campaigns | 1 dossier/type + README (schéma : quoi entre, quoi n'entre pas, process d'ajout) ; chaque item = frontmatter + corps + timeline |
| **Contracts** (1/loop) | README par loop : **goal + workflow + backlog + timeline** | chaque réveil : lire le contrat → comprendre le but + l'historique → agir |
| **Logs** | work-log global | écrire après chaque bloc ; **lire les 5-10 dernières entrées avant de travailler** |

**Le mécanisme de composition** : chaque loop **lit ET écrit** les dossiers partagés. Le support loop écrit un signal « export file demandé 3× » → le growth loop le lit et priorise → le ads loop trouve un keyword à fort CTR → signal → le SEO loop produit l'organique. **Même cerveau, cadences différentes = compounding.**

## 4. Codebase harness : legible · executable · verifiable

- **Legible** : AGENTS.md racine ~100 lignes pointant vers la doc (progressive discovery) + **règles injectées en lint programmatique** (l'erreur surface automatiquement au lieu d'espérer que l'agent trouve la règle).
- **Executable** : dev server en 1 script, **worktree-friendly** (5 agents parallèles sans conflit), scripts pour sauter à un état de test précis.
- **Verifiable** : Playwright CLI (vidéo attachée au PR), e2e sur les flux critiques, PR-queue (checklist avant submit). **Règle d'or : l'agent ne s'auto-vérifie JAMAIS — spawn un verifier read-only séparé.**

## 5. Setup type (support loop)

Skills d'accès (tickets/paiements/logs) + skill de triage (workflow métier) + CLAUDE.md contexte business → **test run manuel** → calibrage → « crée le contrat README » → **alors seulement** poser le cron horaire. Le loop log les frictions en signals ; version 2 : il spawn directement l'agent de fix et prévient le client.

## Mapping A'Space

- **Signals** ≈ notre `wiki/log.md` (curé) + `turn-journal.md` (brut) — le delta : nous n'avons pas encore de dossier signals **typé lisible par tous les loops** → candidat artifact OKF (`type: Signal`).
- **Contracts** ≈ nos loop-plans (`loop-plan-2026-06-15.md`, §10 Méta-Mémoire) — le delta : goal+workflow+backlog+timeline dans UN fichier par loop.
- **Verifier read-only** = renforce le §10.2 (les batchs passent par sub-agents ; ajouter : la vérif par un agent DIFFÉRENT du maker).
- **Legible codebase** = exactement l'arbre **DOX P4** ; « lint programmatique » = nos hooks PostToolUse log-only.
