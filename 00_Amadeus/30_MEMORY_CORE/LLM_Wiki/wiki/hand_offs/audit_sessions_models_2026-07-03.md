---
title: Audit sessions Claude Code × modèles #1 — méthode tilly-fable-rhythm
date: 2026-07-03
layer: L0
tags: [tilly-fable-rhythm, LD04_Cognition_Tilly, jsonl-mining, behavioral-delta, MiniMax-M3, claude-fable-5, claude-opus-4-8, mindsets, D1-receipts]
author: A3 auditeur cognition (Claude Fable 5)
method: Fable Mindset kit (DATASET.md + PROMPTS.md) + skill tilly-fable-rhythm
corpus: C:/Users/amado/.claude/projects/C--Users-amado/*.jsonl
source: CC-M3 (tilly-fable-rhythm skill)
type: audit
domain: cross_layer
---

# 🎼 Audit sessions × modèles #1 (tilly-fable-rhythm) — 2026-07-03

> **Mission** : premier audit des sessions Claude Code locales + delta comportemental
> MiniMax-M3 vs Claude Fable 5 vs Opus 4.8/4.7, confronté à la baseline mesurée 2026-06-25
> (M3 reason 53% / re-evaluate 50% / real-test 33% ; Opus 74% / 67% ; Fable 88% / 63%).
> Rythme audité : `GROUND → REASON → ACT → OBSERVE → RE-EVALUATE → VERIFY → NARRATE`.

## 1. Inventaire corpus (D1)

- **29 fichiers `.jsonl`**, **591,0 MB** au total (plus gros : `b3bb406c` 90,6 MB ; `9627821e` 81,4 MB).
- Période couverte : **2026-06-06 → 2026-07-03** (28 jours).
- Mining : streaming ligne-à-ligne (jamais de `cat`), turns regroupés par `message.id`, **dédupliqués par `message.id` global** (les forks/resume dupliquent les turns : `3ba354b0` = `d31ec261` ⊂ `9b0dfb5a`, même chaîne Opus 4.8 du 06-25→06-29).

| Modèle (`message.model`) | Sessions (fichiers) | Sessions distinctes | Turns dédupliqués | Tool calls dédup. | Période |
|---|---|---|---|---|---|
| **MiniMax-M3** | 27 | 27 | 9 049 | 11 336 | 06-06 → 07-03 |
| **claude-opus-4-8** | 4 | **2** (chaîne fork ×3 + 1) | 438 | 414 | 06-08 → 06-29 |
| **claude-fable-5** | 1 | 1 (= la session d'audit courante, self-measurement) | 63 | 71 | 07-02 → 07-03 |
| **claude-opus-4-7** | 1 | 1 | 42 | 39 | 06-08 |
| `<synthetic>` | 21 | — (messages harness, 0 tool call) | 180 | 0 | exclu de l'analyse |

**Disponibilité échantillon** : l'objectif "≥5 sessions par modèle" n'est atteignable que pour M3 (27). Opus 4.8 = 2 sessions distinctes, Fable 5 = 1, Opus 4.7 = 1 — dit honnêtement, les deltas Fable/Opus4.7 sont indicatifs, pas statistiques.

## 2. Asymétrie de mesure découverte (D6 root cause — À NE PAS RE-DÉCOUVRIR)

1. **M3 persiste ses thinking blocks dans le JSONL local (58 % des turns) ; les backends Anthropic (Fable 5, Opus 4.8/4.7) en stockent 0.** Toute comparaison "reason-before-act" doit donc être publiée en **double règle** : A = thinking OU texte avant tool call ; B = **narration texte uniquement** (même règle pour tous → comparable à la baseline).
2. **Dédupe obligatoire par `message.id`** : sans dédupe, la chaîne fork Opus 4.8 compte 3× (920 turns bruts vs 438 réels).
3. Le runtime écrit **1 ligne JSONL par content block** (même `message.id`) : compter les "messages" sans regrouper par id donne 0 % de reason-first partout (artefact vérifié en v1 de ce mining).

## 3. Tableau behavioral delta (rythme Fable, dédupliqué)

Règle B = narration texte avant action (comparable baseline). Règle A entre parenthèses quand différente.

| Métrique | MiniMax-M3 (n=27) | Opus 4.8 (n=2) | Fable 5 local (n=1) | Opus 4.7 (n=1) | Baseline 2026-06-25 |
|---|---|---|---|---|---|
| **Reason-before-act** | **47 %** (A: 77 %) | **74 %** | 25 %* | 18 % | M3 53 / Opus 74 / Fable 88 (cot HF) |
| **Re-evaluate after result** | **49 %** (A: 77 %) | **75 %** | 26 %* | 21 % | M3 50 / Opus 67 |
| **Reads-before-edits** (fichier lu avant Edit) | **98 %** (2 092/2 136) | **98 %** (223/227) | **96 %** (23/24) | n/a (0 edit) | non baselinée |
| **Real-test-after-edit** (session avec vrai check après dernier edit) | **30 %** (7/23) | **25 %** (1/4 fichiers) | **0 %** (0/1) | 0/1 | M3 33 / Fable 63 (HF) |
| **Plan-gate** (TodoWrite/Plan si ≥15 tool calls) | **75 %** (15/20) | **75 %** (3/4) | 0 % (0/1) | 0/1 | non baselinée |
| Thinking persisté | 58 % des turns | 0 % | 0 % | 0 % | — |

*\* Fable 5 local : le thinking interleaved n'est PAS persisté dans le JSONL → 25 % mesure la **narration visible**, pas la cognition (le dataset HF avec cot donne 92 % reason-first). Échantillon n=1 = la session d'audit elle-même.*

**Convergence D1** : la règle B reproduit la baseline indépendante du 2026-06-25 à ±6 pts (M3 47≈53, re-eval 49≈50, real-test 30≈33 ; Opus 74=74). Deux instruments, même verdict → la mesure est robuste.

**Test lift Mindsets (déployés 2026-06-25)** : split M3 avant/après le 06-25 → reason-first **77 % / 77 %** (règle A), re-eval **77 % / 77 %**. **Aucun lift mesurable** sur ces 2 métriques (647 turns post-06-25 seulement — le hook `posttooluse-test-after-edit.ps1` agit sur real-test, pas sur la narration).

## 4. Top 3 anti-patterns par modèle (exemples concrets)

### MiniMax-M3
1. **Retry aveugle (viole D6 diagnose-then-fix)** — **21 incidents** de la même commande Bash relancée ≥3× à l'identique. Ex : session `291e25f2`, `curl -X POST https://transcriptapi.com/mcp` relancé 3× identique (avec Bearer token en dur dans la commande — redacté ici, violation Test Key Pragma "jamais en clair" en prime). Aussi `176c663e` : même heredoc Python relancé 3×.
2. **Pas de vrai test après edit (le gap #1)** — 16/23 sessions avec edits se terminent sans check réel après le dernier edit. Ex : `9627821e` (la plus grosse session M3 : 2 657 turns, 3 162 tool calls, edits présents) → 0 test-after-last-edit.
3. **Chaînes silencieuses / narration absente** — 47 % de narration seulement ; M3 "pense" en thinking blocks mais ne narre pas les transitions (NARRATE du loop). Ex : `77ff60f7`, 9 tool-turns consécutifs (Edit×4, TodoWrite×2, Read, Bash) sans un mot ; session outlier `09d6c0e1` : 16 % de reason-first sur 699 turns.

### Claude Opus 4.8
1. **Real-test-after-edit faible (25 %)** — ex : chaîne `9b0dfb5a` (346 turns, 87 edits) terminée sans vrai check après le dernier edit. Opus écrit le rapport plutôt que de lancer la preuve.
2. **Volume élevé de Write de nouveaux fichiers non re-vérifiés** — 158 new-file writes vs 227 edits (41 % de la production = fichiers neufs, handoffs/docs) rarement suivis d'une lecture/validation.
3. **Artefact fork/resume** — la même chaîne comptée 3× (`3ba354b0`=`d31ec261`⊂`9b0dfb5a`) : tout audit sans dédupe surestime Opus ×2-3. (Harness, pas cognition — mais piège d'audit réel.)

### Claude Fable 5 (local, n=1 — indicatif)
1. **0/1 real-test-after-edit** — le weak spot connu de Fable (65 % sur le dataset HF, déjà flaggé dans le SKILL.md) se reproduit localement : 24 edits + 14 writes dans la session d'audit, dernier edit non suivi d'un check réel au moment de la mesure.
2. **Narration visible faible (25 %)** — Fable batch ses tool calls en silence (raisonnement dans le thinking non persisté). Cognition probable, **observabilité A0 nulle** → anti-pattern opérationnel A'Space (D9.3 NARRATE).
3. **Pas de plan-gate** — 0 TodoWrite sur une session à 93 tool calls (>seuil 15).

### Claude Opus 4.7 (bonus, n=1)
- Chaîne silencieuse record : 15 tool-turns Bash consécutifs sans narration (`b4d15a9d`) — session sonde/status.

## 5. Recommandations playbook (Mindsets)

**À RENFORCER pour M3** (ordre de priorité par taille du gap) :
1. **VERIFY mécanique** : le real-test-after-edit (30 %) est le gap #1. Garder le hook `posttooluse-test-after-edit.ps1` (log-only) ET ajouter dans `Morty_Mindset.md` une règle explicite : *"après le dernier edit d'une unité de travail, lance la commande réelle (test/build/curl), pas un proxy narratif (ls/echo)"*.
2. **Anti-retry-aveugle (D6)** : ajouter aux Mindsets : *"ne JAMAIS relancer une commande identique qui vient d'échouer ; lis l'erreur, change une variable, ou diagnostique"* — 21 incidents mesurés, 0 chez Opus/Fable.
3. **NARRATE ≠ think** : M3 raisonne (77 % règle A) mais ne narre que 47 %. Exiger 1 ligne de narration par batch de tool calls (D9.3, max 5 items) — c'est la seule trace lisible par A0.

**À RETIRER des prompts Fable** (natif, instruction morte) :
1. **"Read before edit"** : 96-98 % natif chez TOUS les modèles mesurés — instruction inutile, la retirer des playbooks pour économiser du budget prompt.
2. **"Don't retry blindly"** : 0 incident Fable/Opus — natif chez les backends Anthropic, à garder uniquement côté M3.

**À GARDER/AJOUTER pour Fable** :
1. **Real-test-after-edit** : weak spot propre à Fable (65 % HF, 0/1 local) — le playbook doit le renforcer, pas copier Fable aveuglément (déjà acté dans le SKILL.md, confirmé par cette mesure).
2. **NARRATE obligatoire** : le thinking Fable étant invisible dans les logs locaux, exiger la narration texte des décisions/transitions pour l'observabilité A0.

**Doctrine d'audit (D6 lessons, pour le prochain run)** :
- Toujours dédupliquer par `message.id` (forks) ; toujours regrouper les lignes par `message.id` (1 ligne = 1 block) ; toujours publier en double règle A/B (asymétrie de persistance du thinking M3 vs Anthropic).

## 6. Receipts (commandes + sorties chiffrées)

```
# Corpus
ls ~/.claude/projects/C--Users-amado/*.jsonl → 29 fichiers, 591 028 062 bytes (591,0 MB)

# Miner v2 (turns groupés par message.id, non dédupliqué) — mine_sessions2.py
model            sess  turns  tcalls reason1st%  reeval% readb4edit% test-after% plangate%
MiniMax-M3         27  15457   18490        69%      69%         98%         30%       75%
claude-opus-4-8     4    920     939        65%      66%         98%         25%       75%
claude-fable-5      1     84      93        18%      19%         96%          0%        0%
claude-opus-4-7     1     42      39        18%      21%         n/a          0%        0%

# Miner v3 (dédupliqué par message.id, double règle) 
model                   turns     tc  think%  rfA%  rfB% reevalA% reevalB%
MiniMax-M3               9049  11336     58%   77%   47%      77%      49%
claude-opus-4-8           438    414      0%   74%   74%      75%      75%
claude-fable-5             63     71      0%   25%   25%      26%      26%
claude-opus-4-7            42     39      0%   18%   18%      21%      21%

# Split M3 avant/après déploiement Mindsets (2026-06-25)
pre-0625  turns 8402 toolcalls 10619 reason1st 77% reeval 77%   (règle A)
post-0625 turns  647 toolcalls   717 reason1st 77% reeval 77%

# Anti-patterns
Blind retries (même Bash 3× consécutifs) : MiniMax-M3 = 21 incidents ; Opus 4.8 = 0 ; Fable 5 = 0
Silent chains (≥8 tool-turns sans narration) : M3 = 3 (max 9, `77ff60f7`) ; Opus 4.7 = 1 (max 15, `b4d15a9d`)

# Compteurs bruts par modèle (metrics2.json, non dédup.)
M3    : edits 2136, edits_with_prior_read 2092 (98%), new_file_writes 1103,
        sessions_with_edit 23, sessions_test_after_edit 7 (30%), big_sessions_plan 15/20 (75%)
Opus48: edits 227, prior_read 223 (98%), new_file_writes 158, test_after 1/4, plan 3/4
Fable5: edits 24, prior_read 23 (96%), new_file_writes 14, test_after 0/1, plan 0/1

Scripts : C:/Users/amado/AppData/Local/Temp/audit_fable_rhythm/{mine_sessions.py, mine_sessions2.py, mine_v3.py, metrics.json, metrics2.json}
```

## 7. Verdict (1 ligne)

**Le gap M3 est confirmé et localisé : narration 47 % vs Opus 74 % + real-test 30 % + 21 retries aveugles — mais M3 raisonne en interne (77 % avec thinking) : le fix Mindsets prioritaire est VERIFY mécanique + anti-retry D6 + NARRATE, pas "penser plus" ; côté Fable, retirer read-before-edit (natif 96-98 % partout) et renforcer real-test (0/1 local, weak spot HF confirmé).**

---
*Audit #1 — prochain run recommandé après 5+ sessions Fable 5 réelles (n=1 aujourd'hui, self-measurement) et avec le hook test-after-edit actif pour mesurer son lift sur M3.*
