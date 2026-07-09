---
source: LLM_Wiki_A0
date: 2026-05-10
type: entity
domain: Tech_OS / L2_Technical / Type_Validation
tags: [#entity #Zod #Zod_Contracts #Type_Safety #Runtime_Validation #TypeScript]
---

# Entity: Zod (Contracts & Type Validation)

> NPM: `zod` | TypeScript-first schema validation

Zod est la **couche de validation** pour tous les payloads Symphony Router dans A'Space OS. Pas de raw JSON qui entre dans le système — tout doit être Zod-validé.

---

## Usage dans A'Space OS

### Payload Validation

```typescript
import { z } from 'zod'

// Every payload must pass through these schemas
const IntentSchema = z.enum(['complete_task', 'query_knowledge', 'delegate', 'report'])
const DomainSchema = z.string().regex(/^SOA\d{2}$/)

const SymphonyPayloadSchema = z.object({
  intent: IntentSchema,
  source: z.enum(['A0', 'A1', 'A2', 'A3']),
  target_domain: DomainSchema,
  payload: z.record(z.unknown()),
  metadata: z.object({
    timestamp: z.string().datetime(),
    adr_ref: z.string().optional(),
    priority: z.enum(['low', 'medium', 'high', 'critical'])
  })
})
```

### Domain Contracts

Chaque domaine SOA01–SOA08 a son propre Zod contract :

```typescript
// SOA01 People — X-Men Contract
const PeopleContract = z.object({
  agent_id: z.string(),
  action: z.enum(['hire', 'onboard', 'evaluate', 'release']),
  data: z.object({
    name: z.string(),
    role: z.string(),
    squad: z.enum(['X-Men', 'Kang Dynasty', 'Avengers', 'Guardians', 'Thunderbolts', 'Eternals', 'Illuminati']),
    framework: z.enum(['E-Myth', '12WY', 'PARA', 'GTD', 'DEAL'])
  })
})
```

---

## Pourquoi Zod (vs.其他 solutions)

| Criteria | Zod | Joi | Yup | TypeBox |
|---------|-----|-----|-----|---------|
| TypeScript-first | ✅ | ❌ | ⚠️ | ✅ |
| Tree-shakeable | ✅ | ❌ | ❌ | ✅ |
| No runtime overhead | ✅ | ❌ | ❌ | ⚠️ |
| A'Space usage | ✅ | ❌ | ❌ | ❌ |

---

## Inbounds

- **[[entity_symphony_router]]**: dépend de Zod pour valider les payloads
- **[[entity_solaris_os]]**: Solaris génère les Zod contracts pour les 8 domaines
- **[[entity_rick]]**: Rick enforces Zod comme standard dans le Tech OS

---

## Stats

- **Mentions dans 2026-05**: 78
- **Domain**: L2 Technical / Type Validation
- **Source**: [[sources/source_gemini-takeout-2026-05]]

---

*Last updated: 2026-05-10*
*Source: [[sources/source_gemini-takeout-2026-05]]*