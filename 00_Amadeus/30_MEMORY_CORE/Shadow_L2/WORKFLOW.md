---
source: Shadow_L2
date: 2026-05-19
type: workflow
status: DRAFT_ACTIVE
inherits: ../Shadow_L0/WORKFLOW.md
tags: [#Workflow, #ShadowL2, #BusinessPulse, #Symphony]
---

# Shadow_L2 / WORKFLOW.md

> Hérite du Mission Card Format Shadow_L0 §1. Documente les missions L2-spécifiques.

## 1. Mission Types L2

| Type | Description | Autonomy |
|---|---|---|
| `prod-health-probe` | HTTP health check round-robin | auto |
| `incident-triage` | Diagnostiquer cause + draft mission card Squad | signoff (signoff for execute, not draft) |
| `airtable-enrich-trigger` | Suggérer batch enrichissement (jamais lancer auto) | signoff |
| `vercel-build-diagnose` | Lire build logs + suggest fix | auto (read-only) |
| `supabase-advisor-digest` | Capture security/perf advisors | auto |
| `margin-shield-report` | Daily cost burn summary | auto |
| `squad-mission-draft` | Draft mission card pour Squad business | signoff par A0 avant écriture inbox Squad |
| `dns-snapshot-before-change` | Précondition obligatoire toute mutation DNS Hostinger | signoff |

## 2. Squad Routing Map

Quand un incident persistent → quelle Squad reçoit la mission card ?

| Anomaly | Squad cible |
|---|---|
| L2-A01 prod down (solaris) | 02_IT_Cyborg + 04_Product_Flash |
| L2-A02 vercel build fail | 04_Product_Flash |
| L2-A03/A04 VPS pressure | 02_IT_Cyborg |
| L2-A05 raw queue | 05_Growth_Superman |
| L2-A06 clickup overdue | 03_Operations_Batman |
| L2-A07 supabase security | 02_IT_Cyborg + 07_Legal_Aquaman |
| L2-A09 quota MiniMax | 06_Finance_WonderWoman |
| L2-A10 cost burn | 06_Finance_WonderWoman |

## 3. Turn 1 Template

```markdown
# Turn 1 — Mission ${MISSION_ID}

## SOUL
${SOUL_CLAUDE_CODE_L2}

## AGENT
${AGENT_HEARTBEAT_L2}

## MISSION
${MISSION_CARD}

## SURFACE STATE
- Cooldown active: ${COOLDOWN_TABLE}
- Last anomaly: ${LAST_ANOMALY_ID} @ ${LAST_TS}
- MCP status: ${MCP_HEALTH}

## TOOLS
${TOOLS_L2}

## INSTRUCTION
Execute the due check. Emit one terminal marker.
Respect cooldown. Append cooldown.json update on alert.
```

## 4. Continuation Template

```markdown
# Turn ${N} — Mission ${MISSION_ID}

Continue. Last: outbox/turn-$((N-1)).md
State: Context.md
Cooldown: cooldown.json

If criteria met → <DONE>
If incident persistent → <ESCALATE> with Squad mission card draft attached.
```

## 5. Cross-refs

- `../Shadow_L0/WORKFLOW.md`
- `./SPEC.md`
- `./HEARTBEAT_PROTOCOL.md`
