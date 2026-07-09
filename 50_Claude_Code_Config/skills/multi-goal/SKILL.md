---
name: multi-goal
description: Multi-agent goal-driven loop — orchestrates A1 → A2 → A3 → B1/B2/B3 with completion criteria. Routes via Beth (Ikigai lock) for alignment or Morty (12WY cadence) for execution. Spawns 8 sub-agents in parallel per iteration.
---

# /multi-goal — A0 Multi-Agent Goal Loop

> **Skill Symphony Multi-Workflow** — invocable par A0 Amadeus via `/multi-goal <outcome> [<cadence>]`.
>
> **Complément de** : `/goal` natif CC (CHANGELOG 2.1.139, single-agent loop). `/multi-goal` étend à multi-agent multi-workflow via Symphony twin runtime.

## Différence vs /goal natif CC

| Aspect | `/goal` natif | `/multi-goal` |
|---|---|---|
| Agents | 1 (Main Agent loop) | 8+ (Main Agent + 8 sub-agents //) |
| Routage | Linear single-agent | A1 → A2 → A3 → B1/B2/B3 (matrice canon) |
| State | Implicit | `state.json` (state-bus.v1, lock atomique) |
| TTS | None | Stop hook SAPI Hortense (D3 nuancé : claude-voice MCP = poison, SAPI = canon) |
| D7 ROI | N turns = N coût | 1 A0 turn = N sub-agents // = D7 ROI ×N |

## Workflow canonique (5 steps)

### Turn 1 — Air Lock Clarification
`/multi-goal` demande à A0 :
1. **Outcome mesurable** : quel livrable concret ou signal observable définit "GO" ?
2. **A1 Gatekeeper** : Beth (sens/alignement) ou Morty (exécution/cadence) ?
3. **Cadence** : one-shot / daily / weekly / until-done
4. **Critères de succès** : 3-5 critères vérifiables (D1 receipt obligatoire)

### Turn 2 — Route A1 → A2

**Si A1 Beth (Ikigai Lock)** :
- A2 Orville Meaning Engine → A3 Ed (Profession) + Kelly (Mission) + Gordon (Passion) + Claire (Vocation)
- A2 Discovery Zora Balance → A3 Book (LD01 Business) + Saru (LD02 Finance)
- A2 Protostar Holo Janeway Liberation → A3 Dal (Define) + Rok-Tahk (Eliminate) + Zero (Automate) + Gwyn (Liberate)

**Si A1 Morty (12WY Cadence)** :
- A2 SNW Curie Execution → A3 Pike (Vision) + Una (Planning) + Chapel (Measure) + M'Benga (Focus) + Ortegas (Execution)
- A2 Enterprise Computer Structure → A3 Picard (Projects) + Spock (Areas) + Geordi (Resources) + Data (Archives)
- A2 Cerritos Holodeck Chaos → A3 Mariner (Capture) + Boimler (Clarify) + Rutherford (Organize) + Tendi (Review) + Freeman (Engage)

### Turn 3 — Spawn N sub-agents A3 en parallèle (D8)

Chaque sub-agent `general-purpose` reçoit :
- 1 intention canon (handoff / ADR / spec / transcript YouTube)
- 1 livrable attendu (output json structuré)
- 1 deadline (timeout_seconds)

**Pattern Phase 2** (depuis `symphony-phase2-batch` canon) : 8 sub-agents // = 1 tour A0 = D7 ROI ×8.

### Turn 4 — Symphony orchestration

Chaque sub-agent écrit dans `state.json` (state-bus.v1) :
```json
{
  "cycle": "Q3-2026",
  "week": "W2",
  "stage": "executed",
  "agent_path": "A1:Beth > A2:Orville > A3:Kelly",
  "para_bucket": "01_Projects/life-os-2026",
  "12wy_discipline": "Planning",
  "next_step": "A3:Ed",
  "tokens_used": 12450,
  "drift_flag": false,
  "updated_at": "2026-06-21T..."
}
```

Lock atomique via `.state.lock` + retry 3× (backoff 100/300/900ms).

### Turn 5 — GO detection + TTS

Si tous les critères du Turn 1 sont OK dans `state.json` :
- Beth (veto) ou Morty (routeur) lit le state.json final
- Retourne `<DONE>` au Main Agent
- Stop hook SAPI Hortense joue "Objectif atteint. Voir terminal."

Sinon : flag `next_step` pointe vers nouvelle itération, Main Agent relance le cycle.

## Doctrine ancrage

- **D1 verify-before-assert** : state.json lu + critères vérifiés avant `<DONE>`
- **D2 research-first** : lire canon (handoff/AGENTS.md/ADR) avant spawn sub-agents
- **D3 nuance** : Ikigai = A2 Orville ≠ A1 Beth (canon AGENTS.md)
- **D7 cost-of-escalation** : 8 sub-agents // = 1 A0 turn vs 35 escalades
- **D8 cross-agent** : Claude + Codex + Gemini respectent matrice A1→A2→A3

## Fichiers canon liés

- `C:\Users\amado\.claude\commands\routine.md` — orchestrateur 3-tiers utilisé par /multi-goal
- `C:\Users\amado\.claude\skills\swarm-orchestrator\SKILL.md` — spawn sub-agents
- `C:\Users\amado\.claude\skills\symphony-fabuleux-discipline\SKILL.md` — doctrine
- `C:\Users\amado\.claude\skills\symphony-phase2-batch\SKILL.md` — Phase 2 = 8 sub-agents // precedent
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\01_Identity_Core\AGENTS.md` — 3-Turn BMad Air Lock
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\handoff_a0_divinity_arsenal_2026-06-20.md` — A0 doctrine + arsenal CC

## Usage

```
/multi-goal <outcome> [<cadence>]
```

Exemples :
- `/multi-goal "ship Life-OS-2026 BETA V2.0 by 09/07/26" weekly`
- `/multi-goal "verify Ikigai lock for 1000T Saru vision" until-done`
- `/multi-goal "complete Q3 W2 items 3-4" one-shot`