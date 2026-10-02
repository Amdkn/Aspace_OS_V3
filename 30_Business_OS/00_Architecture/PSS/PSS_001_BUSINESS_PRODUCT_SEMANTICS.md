# [A-SPEC][PSS-001][BUSINESS] Product Semantics, Positioning, Surfaces & Repo Lineage

**Object Type:** A-SPEC PSS (Product Semantics Specification)
**Date:** 2026-10-02
**Status:** ACCEPTED

## 1. Intent
This specification establishes the canonical semantic freeze for the Business OS product family. It explicitly defines products, audiences, surfaces, and the classification of operational repositories to eliminate semantic ambiguity and overlapping identities across the architecture.

## 2. Canonical Glossary

The current product family strictly uses the following vocabulary. Any aliases or superseded names are prohibited.

| Term | Canonical Meaning |
|---|---|
| **The OMK Services** | The organization / operating company. |
| **The OMK Office** | The market-facing client-service product (acquisition, catalog, onboarding, and client access). |
| **OMK Business OS** | The authenticated operations engine / back-office. |
| **Coach OS** | A vertical configuration of OMK Business OS specifically for coaches, consultants, and operators. |
| **OMK Mobile** | The edge/mobile projection of the same Business OS state and capabilities. |
| **Business OS Factory** | The internal configuration/compiler control plane used by A'Space to manage tenant instances. |
| **Tenant Operators (OMK, ABC, Marina)** | Tenant/operator/franchise instances; these are configurations, not separate software architectures. |

### Prohibited Aliases & Superseded Names
- *Prohibited:* "Business-Office-3-OS" (use **OMK Business OS**)
- *Prohibited:* "SaaS Garden", "AI Studio" (these denote upstream/historical lineage, not current canonical products)
- *Prohibited:* "The OMK Back Office" when referring to the public front door (use **The OMK Office** for public, **OMK Business OS** for operations)

## 3. ProductContext Schema

The `ProductContext` is the universal tuple used to route intent across surfaces. Every surface and operation must resolve to exactly one `ProductContext`.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ProductContext",
  "type": "object",
  "properties": {
    "organization": { "type": "string", "enum": ["The OMK Services"] },
    "brand": { "type": "string", "description": "Tenant brand projection (e.g., OMK, Marina, ABC)" },
    "product": { "type": "string", "enum": ["The OMK Office", "OMK Business OS", "Coach OS", "OMK Mobile", "Business OS Factory"] },
    "offer": { "type": "string", "description": "The specific commercial offering (e.g., Solo Consultant, Riverside Clinic)" },
    "audience": { "type": "string", "enum": ["PUBLIC", "CLIENT", "OPERATOR", "FACTORY_ADMIN"] },
    "tenant": { "type": "string", "description": "UUID or slug for the tenant instance" },
    "workspace": { "type": "string", "description": "UUID or slug for the isolated workspace within the tenant" },
    "role": { "type": "string", "description": "User's RBAC/ABAC role within the workspace" },
    "surface": { "type": "string", "enum": ["PUBLIC_WEB", "OPERATIONS_DESKTOP", "EDGE_MOBILE", "FACTORY_CLI", "CROSS_CUTTING_API"] },
    "capabilities": {
      "type": "array",
      "items": { "type": "string" },
      "description": "List of authorized Business OS capabilities bound to this context"
    }
  },
  "required": ["organization", "product", "audience", "surface"]
}
```

## 4. Product & Surface Matrix

Every UI surface resolves exactly one `ProductContext` mapping.

| Product | Surface | Audience | Positioning Promise |
|---|---|---|---|
| **The OMK Office** | PUBLIC_WEB | PUBLIC, CLIENT | "The unified front door for your services, catalogs, and onboarding." (B2C/B2B consumer) |
| **OMK Business OS** | OPERATIONS_DESKTOP | OPERATOR | "The uncompromised operations engine to run your entire firm." (B2B operator) |
| **Coach OS** | OPERATIONS_DESKTOP | OPERATOR | "The specialized operations engine configured for coaching and consulting." (B2B niche) |
| **OMK Mobile** | EDGE_MOBILE | OPERATOR, CLIENT | "Your business capabilities at the edge, fully synced." |
| **Business OS Factory** | FACTORY_CLI / API | FACTORY_ADMIN | "The invisible compiler that generates instances without forking code." |

## 5. Repository Lineage Matrix

Repositories are not products. No repository name should be used as a product identity. Every repository is classified exactly once under the following lifecycle roles:

| Repository / Context | Lifecycle Role | Justification |
|---|---|---|
| **The OMK Office repo** | `UPSTREAM_COMPONENT` | Projects the public front door. |
| **omk-services/OMK-DESKTOP-WEB-OS** | `CANONICAL` | The central operations engine (Business OS). |
| **The-OMK-Mobile-Back-Office** | `UPSTREAM_COMPONENT` | Edge/mobile projection. |
| **Astra 30_Business_OS** | `UPSTREAM_COMPONENT` | Factory control plane. |
| **historical BusinessOS** | `ARCHIVED_LINEAGE` | Lineage after extraction. |
| **historical Business-Office-3-OS** | `ARCHIVED_LINEAGE` | Lineage after extraction. |
| **historical SaaS Garden** | `ARCHIVED_LINEAGE` | Lineage after extraction. |
| **historical AI Studio** | `ARCHIVED_LINEAGE` | Lineage after extraction. |

## 6. Migration Map

Any existing routes, copy, or UI elements using prohibited names must be migrated according to this map:

- `route:/business-office-3` → Migrate context to `OMK Business OS`.
- `copy:"Welcome to SaaS Garden"` → Update to the specific tenant brand or `Coach OS` if applicable.
- `api:/v1/ai-studio/capabilities` → Reroute to `Business OS Factory` endpoints or canonical capability registries.
