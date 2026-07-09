---
source: youtube-to-guide (transcript fourni par A0 in-chat 2026-07-02)
date: 2026-07-02
type: video-guide
ld: LD07_Creativity_Reno
ld_domain: Creativity / IT
a3_owner: Reno
video_id: UNKNOWN
title: "Matt Pocock's Agentic Engineering Workflow (just copy him)"
channel: "David Ondrej (invité : Matt Pocock)"
watch_url: null
status: GUIDED
tags: [#youtube, #geordi, #ld07, #harness, #queues, #skills, #grilling, #strategic]
---

# Guide — Matt Pocock's Agentic Engineering Workflow

> **Thèse** : le harness > le modèle (50/50, et tu contrôles le harness). L'IA a mangé la programmation tactique ; tes compétences stratégiques sont **le plafond** de ce que l'IA peut faire pour toi. Et : « ce ne sont pas des loops, ce sont des **queues** ».

## 1. Tactique vs Stratégique (Ousterhout, *Philosophy of Software Design*)

- **Tactique** = écrire le code, la syntaxe, les bugs du jour → **mangé par l'IA** (elle le fait moins cher).
- **Stratégique** = gagner la guerre : architecture, interfaces entre modules, scoping des tâches, vélocité → **inchangé par l'IA**. On délègue à l'IA comme on déléguait aux juniors : design des parties dures en amont, tâches bien scopées, juste assez de doc pour pointer l'agent au bon endroit.
- Corollaire mesuré : l'IA rend les seniors ~10× meilleurs, les juniors un peu — **tes skills sont le multiplicateur**.

## 2. Queues, pas loops (le recadrage clé)

- Le développement a TOUJOURS été une queue : backlog → des nœuds (devs/agents) piochent → résolution. Un « loop infini unique » ne matche pas la réalité d'une équipe.
- Setup Pocock : issues GitHub + **labels comme triggers** (`agent-explore`, `agent-implement`) → GitHub Actions lance l'agent AFK en **sandbox** (son outil Sandcastle : Docker/Podman, jamais d'agent hors sandbox — home dir, exfiltration env vars) → PR avec review agent → l'humain clique.
- **HITL checkpoints poussés progressivement vers la droite** : bug report → exploration auto → fix auto → review auto → il ne te reste QUE le bouton merge. Mais : « qui review l'IA qui décide qu'on peut ne pas reviewer ? » → **on ne review pas que le code, on review le SYSTÈME qui produit le code** (échantillonnage des PRs auto-validées).

## 3. Doctrine skills : procédures vs abilities

| Type | Invocation | Exemple | Coût contexte |
|---|---|---|---|
| **Procédure** | par l'HUMAIN | `grill-me`, `2prd`, `teach` | maîtrisé (peut être `disable-model-invocation`) |
| **Ability** | par le MODÈLE | coding standards React | **chaque description fuit dans le contexte** — 100 skills = 100 descriptions leakées |

- Pocock préfère les procédures : « je ne veux pas déléguer ma pensée au modèle ». **Grill-me** (5 phrases !) = interviewer adversarial jusqu'à compréhension partagée — remplace le plan mode. **Teach** = skill STATEFUL (mission.md + learning record local) : cours personnalisé à la volée, quizzes, HTML riche.
- Connaissance / compétence / **sagesse** : les deux premières se bundlent en skills partageables ; la sagesse (quand agir) ne s'obtient qu'en contexte réel.

## 4. Les 2 actions concrètes qu'il prescrit

1. **Reset minimaliste** : supprime TOUS les skills/plugins/MCP/CLAUDE.md → observe l'agent nu → re-superpose UNIQUEMENT ce qui manque, en procédures que TU choisis. (Tout le monde bloat son contexte.)
2. **Passe AFK** : le moment où il a « vraiment » décollé = sortir du human-in-the-loop — se paralléliser (2, 3, 5 versions de toi qui produisent, toi qui review).

## 5. Positions notables

- Optimiser le token spend = **avoir une codebase facile à changer** (un modèle plus bête suffit si l'architecture est bonne). Penser modèle-d'abord = l'erreur ; les fondamentaux 30-40 ans tiennent.
- Sur les nouveaux modèles (Fable inclus) : attendre ~1 mois que ça décante — « you're not losing that much ».
- AX (Agent Experience) = le nouveau DX : le senior qui sait construire une bonne DX construit une bonne AX.

## Mapping A'Space

- **Grill-me = la raison d'être d'A0-L** (le plan Jumeau Challenger référence CE skill de CE repo). Ce guide = la doctrine source.
- **Queues, pas loops** = converge avec Donna DLQ + nos stop-conditions §10.4 — un backlog pioché, jamais une boucle qui tourne pour tourner.
- **Review le système producteur** = notre D5/D1 (pas d'auto-congratulation sans preuve) porté au niveau harness.
- **Reset minimaliste** = candidat audit Rick S1 : notre contexte (145 commandes × 130 skills) est exactement le bloat qu'il décrit — à auditer, pas à subir.
- **Sandbox obligatoire AFK** = aligné P6-E3 (dry-run sandbox gated).
