---
source: Shadow_L1
date: 2026-05-19
type: workflow
status: DRAFT_ACTIVE
domain: Shadow_L1 / Symphony / Task_Lifecycle
inherits: ../Shadow_L0/WORKFLOW.md
tags: [#Workflow, #ShadowL1, #LifeOS, #Symphony]
---

# Shadow_L1 / WORKFLOW.md

> Hérite intégralement du Mission Card Format Shadow_L0 §1.
> Cette page documente les **types de missions L1-spécifiques**
> et leurs templates Turn 1 / Continuation.

## 1. Mission Types L1-spécifiques

| Type | Description | Autonomy |
|---|---|---|
| `life-os-audit` | Scan Baserow Life OS, anomalies digest | auto |
| `scorecard-prep` | Préparer review hebdo W{n} | auto |
| `rock-proposal` | Suggérer un nouveau Rock (jamais créer) | signoff |
| `tactic-deprioritization` | Proposer top-3 tactiques à fermer (surcharge) | signoff |
| `time-use-synthesis` | Synthèse Time Use Tracker sur N jours | auto |
| `gtd-inbox-triage` | Pré-trier inbox GTD Cerritos | signoff |
| `zora-drift-report` | Rapport domaines ZORA stagnants | auto |

## 2. Turn 1 Template (Workflow.md render)

```markdown
# Turn 1 — Mission ${MISSION_ID}

## SOUL
${SOUL_CLAUDE_CODE_L1}

## AGENT (capsule)
${AGENT_HEARTBEAT_L1}

## MISSION
${MISSION_CARD}

## CURRENT STATE
- Baserow Life OS last seen: ${BASEROW_LAST_TS}
- Plane status: ${PLANE_STATUS}
- LD04 last scorecard entry: ${LD04_LAST_TS}
- Open tactics count: ${TACTICS_OPEN_COUNT}

## TOOLS AVAILABLE
${TOOLS_L1}

## INSTRUCTION
Execute the mission. Emit one terminal marker.
```

## 3. Continuation Template (Turn N+ render)

```markdown
# Turn ${N} — Mission ${MISSION_ID}

Continue mission. Last output: outbox/turn-$((N-1)).md
State: Context.md
Mission: inbox/${MISSION_ID}.md

If acceptance criteria met → <DONE>
If blocked → <ESCALATE> with reason
If partial → <NEEDS_REVIEW>
```

## 4. Output Conventions

- Anomaly digests : table markdown, anomaly_ids référencés
- Scorecard prep : checklist H1/H10/H30
- Tous outputs en outbox/ avec frontmatter YAML minimal (mission_id, turn, ts, executor)

## 5. Cross-refs

- `../Shadow_L0/WORKFLOW.md` (template parent)
- `./SPEC.md`
- `./HEARTBEAT_PROTOCOL.md`
