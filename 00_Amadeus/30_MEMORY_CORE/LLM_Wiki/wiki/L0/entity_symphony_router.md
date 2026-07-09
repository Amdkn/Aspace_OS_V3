---
source: LLM_Wiki_A0
date: 2026-05-10
type: entity
domain: Tech_OS / Solarpunk_Kernel / Agent_Runtime
tags: [#entity #Symphony_Router #Symphony #Payload_JSON #Zod_Contracts #L2_Technical #Agent_Orchestration]
---

# Entity: Symphony Router

> Canonical: `A'Space_OS_V2/30_Business_OS/07_Legal_Aquaman/02_Symphony_Body/`

Symphony Router est l'**orchestrateur de payloads inter-agents** pour A'Space OS V2. Il reçoit des payloads JSON, les valide avec [[entity_zod]], et les route vers le bon agent/domaine.

---

## Architecture

```
Amadeus Intent
    ↓
Symphony Router (payload orchestrator)
    ├── Validate (Zod schema)
    ├── Route (par domaine SOA01-08)
    └── Dispatch (→ A2/A3 agents)
```

**Position dans le stack :**
- A0 Amadeus → Intent
- Symphony Router → Orchestration layer
- Zod → Type validation (runtime safety)
- A2/A3 agents → Execution

---

## Payload JSON Schema

Chaque payload Symphony contient :

```typescript
{
  intent: string,           // "complete_task" | "query_knowledge" | etc.
  source: string,           // A0 | A1 | A2 | A3
  target_domain: string,    // SOA01-08
  payload: object,          // Data (Zod-validated)
  metadata: {
    timestamp: string,
    adr_ref?: string,       // Which ADR governs this intent
    priority: "low" | "medium" | "high" | "critical"
  }
}
```

---

## Zod Integration

Symphony n'accepte que des payloads validés par Zod. Pas de raw JSON.

```typescript
import { z } from 'zod'

const PayloadSchema = z.object({
  intent: z.enum(['complete_task', 'query_knowledge', 'delegate', 'report']),
  source: z.enum(['A0', 'A1', 'A2', 'A3']),
  target_domain: z.string().regex(/^SOA\d{2}$/),
  payload: z.record(z.unknown()),
  metadata: z.object({
    timestamp: z.string(),
    adr_ref: z.string().optional(),
    priority: z.enum(['low', 'medium', 'high', 'critical'])
  })
})
```

---

## Role dans les 8 Domaines

Symphony Router est le **cross-domain orchestrator** — il permet aux agents SOA01-08 de communiquer sans couplage direct. Chaque domaine est un microservice qui ne connaît que Symphony.

| Domaine | Communication via Symphony |
|---------|--------------------------|
| SOA01 People (X-Men) | Échange de tasks org design |
| SOA02 IT (Kang Dynasty) | Infrastructure requests |
| SOA03 Ops (Fantastic Four) | Execution coordination |
| SOA04 Product (Avengers) | Sprint payloads |
| SOA05 Growth (Guardians) | Acquisition pipeline |
| SOA06 Finance (Thunderbolts) | Cashflow reports |
| SOA07 Legal (Eternals) | Compliance payloads |
| SOA08 Sales (Illuminati) | Revenue/ROI data |

---

## Stats

- **Mentions dans 2026-05**: 826 (2e entité la plus fréquente)
- **Canonical source**: [[sources/source_gemini-takeout-2026-05]]
- **Related**: [[entity_zod]] (validation layer), [[entity_rick]] (governance), [[entity_adr_symph_003]] (Agent OS = standards injection + observability layer consumed at every tick)

---



---

## Inbounds

- [[entity_symphony_router]]
*Last updated: 2026-05-10*
*Source: [[sources/source_gemini-takeout-2026-05]]*