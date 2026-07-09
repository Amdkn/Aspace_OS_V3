---
title: "You Can Make Claude + Codex Plan Together — /Claudex loop"
date: 2026-06-21
source: /youtube-to-guide (sub-agent #2 — sprint cycle 12WY Q3 item 5)
video_id: RChO5deJ_fE
channel: Mark Kashef
author_url: https://www.youtube.com/channel/UCHkzp52CldSPZqU5T49mOnA
url: https://youtu.be/RChO5deJ_fE
duration: ~512s
ld: LD04_Cognition_Tilly
ld_owner: Tilly
a3_twin_owner: A3 Tilly (H30) — Ship's scientist aboard USS Discovery (A2 Zora)
status: DISTILLED_L1
cross_ref_skill: /multi-backend (A0 cross-backend delegation, créé 2026-06-21)
related: 2026-06-19_loop-engineering-10x-hermes-agents__AQRDjI5owZI.md
---

# /Claudex — Faire planifier Claude Code + Codex en boucle (Mark Kashef)

> **Intention** : adopter le pattern **/Claudex** comme **4ème backend loop** de `/multi-backend` — boucle audit-itératif Claude ↔ Codex via Stop Hook + YAML state file. Vidéo CAPITALE car valide la doctrine cross-backend déjà créée le 2026-06-21.

## 🎯 8 points clés (FR)

1. **Pattern core** : `/Claudex plan -3 "build X"` = boucle **N-rounds** où Claude Code draft un plan, Codex CLI l'audit, Claude intègre, Codex ré-audit, jusqu'à convergence ou N atteint.
2. **Stop Hook = bouncer** : Claude Code's **Stop Hook** vérifie un state YAML file avant de quitter — si rounds < N, il invoque Codex CLI puis reprend. Pattern identique à SubagentStop mais cross-process (Claude ↔ Codex, deux runtimes distincts).
3. **YAML state file = source of vérité** : sticky-note qui track `rounds_done`, `main_prompt`, `end_state`. Bash script init au démarrage. Default N=3, sweet spot 2-3 rounds pour 80/20 des bugs planning.
4. **Slash commands disponibles** :
   - `/Claudex plan` — boucle N-rounds complète (le default)
   - `/Claudex review` — audit Codex sans auto-edit (commentary only)
   - `/Claudex cancel` — emergency break (graceful stop)
   - `/Claudex rollback` — nuclear cleanup (wipe YAML + state)
5. **Ask-User-Question injection** : `/Claudex` injecte `AskUserQuestion` (multi-choice MCP) AVANT la boucle si prompt vague → clarifie inputs avant de gaspiller tokens. Pattern canon = "don't burn tokens on a vague plan".
6. **Real-world demo : Pulse Page** (track sessions, no 3rd-party SaaS) — 15-20 min de back-and-forth, 3 rounds = 10 findings Codex intégrés. Claude-only = 5 phases plus "frail". Visible diff = rouges (deletes) + vertes (additions) par tour Codex.
7. **Coût/bénéfice** : "less time you spend going back and forth with Claude Code" — pré-plan N-rounds réduit le coût total vs `Ultra plan` ou itérations manuelles post-build.
8. **Use cases extensibles** : pas que code — fonctionne pour "PowerPoints, Excel files, docx, whatever you want" = n'importe quel livrable où 2 perspectives > 1.

## 📐 Architecture /Claudex (4 composants)

```
[1] Slash command entry (/Claudex plan -3 "...")
        ↓
[2] Bash script init — écrit YAML state (rounds, prompt, end_state)
        ↓
[3] Loop itératif (Claude Code ↔ Codex CLI) :
        ├─ Claude draft plan.md
        ├─ Stop Hook intercepte → lit YAML → si rounds<N : invoke Codex
        ├─ Codex audit plan.md → findings.md
        ├─ Claude lit findings → patch plan.md (rouge=delete, vert=add)
        └─ repeat
        ↓
[4] Stop Hook final — "hard stop reached, all findings integrated" → exit
```

## 🧬 Cross-référence `/multi-backend` skill (D8 prioritaire)

| Composant `/Claudex` | = Équivalent canon Aspace | Source |
|---|---|---|
| Stop Hook bouncer | **SubagentStop** + **TeammateIdle** hooks | CC Agent SDK |
| YAML state file | **`state.json` versionné** (D4 append-only) | multi-backend SKILL.md |
| Bash script init | **Step 1 Air Lock** (clarifier intention) | multi-backend §"Workflow canonique" |
| Loop N-rounds | **Cadence `cycle`** + **max 2 itérations avant escalate** | multi-backend D7 |
| Codex CLI invocation | **`backend-hint="codex"`** → JSON-RPC App Server | multi-backend §"Backend detection" |
| Ask-User-Question | **Step 1 Air Lock** clarifie critères succès D1 | multi-backend canon |
| `/Claudex review` (audit-only) | **Step 3 spawn sub-agents MCP stdio** isolé | multi-backend canon |
| `/Claudex rollback` | **D4 no-hard-delete** → `_TRASH_<date>/` | multi-backend doctrine |

**Conclusion D8** : `/Claudex` est une **implémentation concrète** d'un cas `/multi-backend` avec `cadence="cycle"` + `backend-hint="codex"` + boucle N-rounds. Valide la doctrine sans contredire.

## 🔬 Citations verbatim (référence canon)

- **Bouncer pattern** : *"You can think of this as a bouncer that tells claude code either okay you can leave or wait we have to do something else."* (Mark Kashef, ~3:30)
- **Sweet spot rounds** : *"On average from testing it so far, it seems that two to three rounds is sufficient to get the 80/20 of the planning bugs."* (~2:10)
- **Visible diff colors** : *"Every time you see a red, that is a deletion from the plan. Every time you see a green, that is an addition from the plan."* (~6:30)
- **Hard stop signal** : *"Round three, hard stop reached. All 10 findings by codeex have been actually integrated into the plan."* (~7:00)
- **Vague prompt guard** : *"If you put a very vague plan, it will ask you for more feedback before it even goes into this loop."* (~5:00)
- **Use cases** : *"You could even use this for creating things like assets like PowerPoints, Excel files, docx, whatever you want."* (~7:40)

## 📊 D11 Fable Metrics

| Métrique | Valeur |
|---|---|
| Backends intégrés | 2 (Claude Code + Codex CLI) |
| Hook types utilisés | 1 (Stop Hook as bouncer) |
| State file format | YAML (rounds, prompt, end_state) |
| Default rounds | 3 (sweet spot 2-3) |
| Slash commands | 4 (plan/review/cancel/rollback) |
| Cross-ref Geordi | LD04 Cognition + multi-backend skill |
| Actionnables A0 | 1 (ratifier ADR-LD04-008 `/Claudex` ↔ `/multi-backend` mapping) |
| D11 Fable score | TBD (run manuel 2026-06-21+) |

## 🛠️ Patterns cross-agent extractibles pour Aspace

1. **Stop Hook = bouncer cross-process** : équivalent CC SubagentStop mais vers un **backend différent** (Codex, Hermes). Pattern canon à intégrer dans `/multi-backend` Step 3.
2. **YAML state file comme source de vérité loop** : alternative au JSON state canon — choix YAML = lisibilité humaine pour debug. Mais A0 Aspace = D4 append-only → adopter JSON canon + `.gitignore` YAML.
3. **Hard stop signal** : `Round N, hard stop reached` = pattern propre pour arrêter une boucle sans escalade. Réutilisable dans `/multi-loop-karpathy` pour limiter drift.
4. **Slash command atomic** : `/Claudex` = **4 sub-commands** atomiques (plan/review/cancel/rollback). Pattern à dupliquer : `/multi-backend` pourrait avoir `codex/review/cancel/rollback` en parallèle.
5. **Vague prompt guard** : injecter AskUserQuestion AVANT boucle = D7 cost-of-escalation directe. Aspace pourrait adopter dans Step 1 Air Lock.

## 🔗 Références externes

- **Mark Kashef** : chaîne YouTube "Mark Kashef AI" (D1 verify via metadata)
- **`/Claudex` GitHub** : "link to the GitHub along with a guide on how to use it in the second link in the description below" (D1 verify pending — A0 download to verify)
- **OpenAI Codex CLI MCP server** : https://developers.openai.com/codex (D1 verify)
- **Anthropic Agent SDK Stop Hook** : https://code.claude.com/docs/en/hooks (D1 verify)

## 🎯 Actionnable A0 unique

**Ratifier ADR-LD04-008** : `/Claudex` ↔ `/multi-backend` mapping. Cross-documente que `/Claudex` est un cas d'usage canon de `/multi-backend` avec `cadence="cycle"` + `backend-hint="codex"` + max_rounds paramétrable. ~30 min rédaction ADR.