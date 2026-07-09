---
name: multi-routines-12wy
description: Multi-routine 12 Week Year cycle scheduler — transforms 12 verbatim items into scheduled routines with W1/W2/W3/W4 milestones. Routes via Morty → SNW 5 disciplines (Pike/Vision, Una/Planning, Chapel/Measure, M'Benga/Focus, Ortegas/Execution). Uses /routine (3-tiers) for scheduling.
---

# /multi-routines-12wy — A0 12 Week Year Routine Scheduler

> **Skill Symphony Multi-Workflow** — invocable par A0 Amadeus via `/multi-routines-12wy [<cycle-id>]`.
>
> **Spécialisé pour cycle 12WY** : transforme 12 items verbatim en routines schedulées avec milestones hebdo.
>
> **Utilise `/routine`** (commande custom 2026-06-21) pour 3-tiers routing.

## Cycle Q3 2026 (06/15 → 09/07/26) — 12 items canoniques

| # | Item | Horizon | A1 → A2 → A3 | Swarm |
|---|------|---------|-------------|-------|
| 1 | SOB à Abdaty (OMK + ABC) | H10 | A1 Beth → A2 Discovery → A3 Burnham | B1 + B2-01 |
| 2 | 09/14 = W13 + 09/21 = W0 C4 | H10 | A1 Morty → A2 Curie SNW → A3 Una | B1 (12WY) |
| 3 | IA Autonomie Auto Research | H1 | A1 Morty → A2 Discovery → A3 Stamets | B1 + B3-IT |
| 4 | Frugalité TOKEN MiniMax + Ollama | H1 | A1 Morty → A2 Enterprise → A3 Data | B1 + B2-06 |
| 5 | YouTube → PARA Resources | H10 | A1 Morty → A2 Enterprise → A3 Spock | B2-03 + B2-07 |
| 6 | Hermes Agent orchestration | H1 | A1 Morty → A2 Cerritos → A3 Mariner | B2-05 + B3-IT |
| 7 | Agent OS = Spec/Workflow Symphony | H10 | A1 Morty → A2 Enterprise → A3 Geordi | B2-03 + B3-IT |
| 8 | Business OS par Life OS Agents | H10 | A1 Morty → A2 Enterprise → A3 Picard + Spock | B1 + B2/B3 |
| 9 | Structuration 36 A3 Life OS | H30 | A1 Beth + A1 Morty → A2 Orville + A2 Enterprise | B1 (governance) |
| 10 | Solaris + OMK + ABC // | H10 | A1 Morty → A2 Enterprise → A3 Picard | B1/B2/B3 |
| 11 | VPS Memory core → DEAL Muse | H30 | A1 Beth → A2 Protostar → A3 Rok-Tahk + Zero | B1 + B2-04 |
| 12 | Planification auto-amélioration C+1 | H30 | A1 Beth → A2 Discovery → A3 Tilly | B1 (FRACTAL) |

## Workflow canonique (5 steps)

### Turn 1 — Air Lock Clarification

`/multi-routines-12wy` demande à A0 :
1. **Cycle ID** : "Q3-2026" par défaut. Custom autorisé (Q4-2026, Q1-2027, etc.)
2. **Items override** : utiliser les 12 items canoniques du cycle, ou custom ?
3. **Milestones override** : W1/W2/W3/W4 par défaut (semaines 1-4)
4. **Validation cadence** : A0 valide milestones à W1/W2/W3/W4 (4 fois max) ou weekly (12 fois) ?

### Turn 2 — Route A1 Morty → A2 SNW 5 disciplines

**Cadence 12WY = 5 disciplines SNW orchestrées** :

| Discipline SNW | A3 twin | Routine scope |
|---|---|---|
| Vision | A3 Pike (H10) | North star Q3 + W1 north star (item 1) |
| Planning | A3 Una (H10) | W1/W2/W3/W4 planning (items 2, 12) |
| Measure | A3 Chapel (H10) | Weekly scorecard (items 4, 6 — frugalité TOKEN) |
| Focus | A3 M'Benga (H1) | Deep work blocks (items 3, 7 — IA Autonomie) |
| Execution | A3 Ortegas (H1) | Daily standup + real-test-after-edit (items 5, 8, 10) |

### Turn 3 — Schedule routine par item (via `/routine`)

Pour chaque item, créer routine schedulée :
- **Cadence par défaut** : weekly check-in (chaque lundi 8h)
- **Duration par défaut** : 84 jours (cycle 12WY Q3)
- **Routing 3-tiers** : `/routine` choisit loop/desktop/cloud selon besoin :
  - One-shot + machine allumée → loop
  - Récurrent > 7 jours + machine allumée → Desktop scheduled task
  - Récurrent + laptop fermé → Cloud Routine

### Turn 4 — Dispatch swarms (B1/B2/B3)

Chaque item → dispatch vers son swarm canon :
- B1 (Summers/Jerry direction) — items 1, 2, 9
- B2 (8 Domaines DC) — items 3, 4, 5, 7, 8
- B3 (Squad Marvel) — items 3, 6, 7, 11

Sub-agents `general-purpose` spawn en parallèle (D8) :
- 1 sub-agent par item × 12 items = 12 sub-agents //
- D7 ROI ×12

### Turn 5 — Validation milestone A0 (4× max)

A0 board observer (passif H30/H90) valide :
- **W1 fin 07/05** : items 1-2 livrés
- **W2 fin 07/26** : items 3-4 livrés
- **W3 fin 08/16** : items 5-6 livrés
- **W4 fin 09/07** : items 7-12 livrés

Validation = `/goal` détecte l'état via `state.json` + retourne `<DONE>` au Main Agent.

## Doctrine ancrage

- **D1 verify-before-assert** : state.json milestone tracking vérifié avant `<DONE>`
- **D3 nuance** : Pike/Vision = A3 SNW ≠ A2 SNW (canon AGENTS.md)
- **D6 root-cause** : drift steerable via checkpoint A0 manuel si symptôme persistant
- **D7 cost-of-escalation** : A0 passif board observer 4× max (H30 cadence)
- **D8 cross-agent** : Claude + Codex + Gemini respectent matrice routage

## Fichiers canon liés

- `C:\Users\amado\.claude\commands\routine.md` — orchestrateur 3-tiers (utilisé par /multi-routines-12wy)
- `C:\Users\amado\.claude\skills\multi-goal\SKILL.md` — sœur (alignment goals)
- `C:\Users\amado\.claude\skills\multi-loop-karpathy\SKILL.md` — sœur (recherche iter)
- `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L1_Life_OS\ADR-Meta-000_12-week-year-cycle-doctrine_DRAFT.md` — 12WY doctrine
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\handoff_a0_divinity_arsenal_2026-06-20.md` §15 — A0 dette Q3

## Usage

```
/multi-routines-12wy [<cycle-id>]
```

Exemples :
- `/multi-routines-12wy` (default = Q3-2026 avec 12 items canoniques)
- `/multi-routines-12wy Q3-2026-custom` (override items custom)
- `/multi-routines-12wy Q4-2026` (prochain cycle)