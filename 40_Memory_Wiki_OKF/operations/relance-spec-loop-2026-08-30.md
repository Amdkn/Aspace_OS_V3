---
type: Operations runbook
title: "Relance spec-loop — diagnostic et remise en route du 2026-08-30"
description: Pourquoi la cadence 1 m (Beth/Morty, spec-loop) ne tournait plus — cinq causes imbriquées de l'API au dépôt cible — et les correctifs appliqués pour la relancer sur le canal claude-glm avec A0 en superviseur.
tags: [aspace-v3, spec-loop, ordonnanceur, a0, cadences, relance, minimax, claude-glm]
generated: { by: verdent-gpt-5.6-sol, at: 2026-08-30T13:55:00-04:00 }
verified:
  - { by: human:amdkn, at: 2026-08-31T21:30:59Z }
  - { by: verdent-gpt-5.6-sol, at: 2026-08-30T13:55:00-04:00 }
sources:
  - id: ordonnanceur
    resource: "C:/Users/amado/.claude/skills/ordonnanceur/"
    title: "A0.sh, ordonnanceur.sh, CADENCES.md, programmes/cadence_1m.md"
    last_modified: 2026-08-30
  - id: canal-glm
    resource: "C:/Users/amado/.claude/custom-models/claude-glm.cmd"
    title: "Canal de délégation GLM 5.3 Flash via routeur local 8792"
    last_modified: 2026-08-30
  - id: memoire-minimax
    resource: "C:/Users/amado/.claude/projects/C--Users-amado/memory/minimax-deux-bourses-cle-incompatible.md"
    title: "Abonnement MiniMax expiré le 2026-08-15, mort silencieuse sans alerte"
    last_modified: 2026-08-20
okf_version: "0.2"
---

# État vérifié

Relance réussie à 13:43:09 le 2026-08-30. `A0.sh 4` tourne (fin prévue 17:43),
l'ordonnanceur porte la cadence 1, et le premier tour de Beth est terminé :

```
[13:43:28] A0 · glm repond PONG
[13:43:28] A0 · ordonnanceur lance (pid 2371) — cadence 1 (spec-loop)
[13:45:08] cadence 1m terminee (exit 0)
```

`etat_1m.md` contient une spec réelle et la métrique `agents_en_derive = 0`.
Le tour chevauchant suivant a été sauté proprement (« TOUR SAUTE »).

# Pourquoi spec-loop ne tournait plus — cinq causes imbriquées

La chaîne complète est : skill `spec-loop` → programme `cadence_1m.md` →
`ordonnanceur.sh` → `A0.sh`. Elle était morte à chaque étage.

## C1 — Moteur API mort (cause racine économique)

MiniMax a deux bourses séparées. La clé `sk-cp-…` de `settings.json` puise dans
le **Token Plan** (abonnement), expiré le 2026-08-15 (dernier paiement
2026-07-15, mensuel). La vague d'agents s'est arrêtée sur un 429 sans préavis
(Balance alert et Auto-recharge désactivés). Aucun script ne pouvait détecter
une abonnement expiré.

## C2 — Clé déplacée, scripts non suivis

La clé MiniMax a quitté `~/.claude/settings.json` pour
`~/.claude/_secrets_local/settings.json`. `A0.sh` et `ordonnanceur.sh` lisaient
l'ancien chemin : `python -c ... KeyError` silencieux → clé vide.

## C3 — Le CLI `claude` refuse désormais les modèles personnalisés

Claude Code 2.1.250 rejette en client-side tout identifiant non Anthropic
(`[claude-code:unrecognized_model]` sur `MiniMax-M3[1m]` comme sur
`z-ai/glm-5.2:free`), même via `ANTHROPIC_DEFAULT_*_MODEL`. Le canal historique
`claude -p` + MiniMax est donc **doublement** mort. Le canal valide est
`claude-glm.cmd` (GLM 5.3 Flash via routeur local 8792) avec les deux drapeaux
MCP obligatoires.

## C4 — Dépôt cible éventré

`coach-os` (cible de Beth) ne contient plus que `.git` — arbre de travail vide
depuis le 2026-08-23. Même motorisée, la cadence tournait à vide.

## C5 — Aucun superviseur de superviseur

A0 est borné par conception (4-12 h) puis sort. Aucune tâche planifiée ne le
relance : `WSL-Kernel-WakeUp` cible la distribution `Ubuntu` inexistante
(la réelle est `Ubuntu-24.04`) et prétend une cascade systemd qui n'existe pas.
Le répertoire d'état `Temp/ordonnanceur` avait de surcroît été nettoyé.

# Correctifs appliqués

1. **Skill réinstallée** : `npx --yes skills add dpolivaev/spec-loop -y -g` —
   10 skills `spec-loop-*` restaurées dans `~/.claude/skills` et
   `~/.agents/skills`. L'installation interactive s'était figée sur le TUI des
   77 agents ; `-y -g` la bypassse.
2. **`ordonnanceur.sh`** : canal `claude-glm.cmd` + `--dangerously-skip-permissions
   --strict-mcp-config --mcp-config '{"mcpServers":{}}' -p` ; exports MiniMax
   supprimés (ils contaminaient les sous-processus).
3. **`A0.sh`** : même canal pour le test PONG et le rêve ; rotation
   minimax/openrouter neutralisée (glm est l'unique moteur, la « bascule »
   l'annonce au lieu de mentir) ; lancement restreint à `ordonnanceur.sh 1`
   (les six autres programmes visent des cibles à requalifier).
4. **`cadence_1m.md`** : dépôt repointé vers `C:/Users/amado/ASpace_OS_V3`,
   specs lues dans `00_Amadeus/60_Tape_Specs/`, Morty branché sur la file
   `10_Tech_OS/kernel/uc.db`. Sauvegarde de l'original :
   `cadence_1m.coach-os-2026-08-30.bak`.

# Ce qui reste ouvert

- **Aucun redémarrage automatique** : A0 s'arrêtera à 17:43 et rien ne le
  relancera. Le correctif structurel est une tâche planifiée qui relance A0 au
  boot et à intervalle, avec test de fumée intégré (PONG) pour ne pas empiler
  des morts.
- Les six autres cadences (5 m à 30 m) pointent vers des cibles V2 à
  requalifier une par une avant réactivation.
- `babysitter` v6.0.0 installé à 15:00 (`npm i -g @a5c-ai/babysitter`, test :
  `babysitter --version`). Morty tourne toujours en discipline inline ; le
  brancher sur `run:create` / `session:*` est le chemin ouvert suivant.
- Surveiller le plancher de tokens du routeur 8792 et le plafond
  `MAX_NODE=45`.
