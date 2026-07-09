---
id: ADR-OMK-003
title: MCP `supabase-aspace` v0.1 — 5 tools scoped to OMK schemas (omk_internal, omk_saas, public-utilities)
status: RATIFIED
date: 2026-06-11
deciders: [A0 Amadeus]
proposed_by: Claude Code (A2)
domain: L2 Business OS / OMK Services / Data Plane / Self-Hosted Supabase
tags: [#ADR #omk #mcp #supabase #aspace #postgres #rls #pat #rate-limit #audit #blocker-3]
related:
  - ADR-OMK-001 (parent: dual-product + multi-tenant doctrine)
  - ADR-SUPABASE-001 (parent: dual-MCP doctrine, `aspace_admin` role, scope discipline)
  - ADR-INFRA-MCP-001 (dox + vault + rotation pattern)
  - ADR-META-001 (D1-D8 — every claim in this ADR is verified this turn)
  - _SPECS/MCP/supabase-aspace-spec.md (sibling: A'Space-OS-wide `supabase-aspace` spec, ACCEPTED 2026-06-10)
  - omk/apps/dashboard/AGENTS.md §1 (4 ADR Blockers, #3 = this ADR)
  - omk/apps/dashboard/CLAUDE.md §"Self-hosted Supabase" + gotcha #3, #5, #12
  - omk/apps/dashboard/REBUILD_WORKFLOW.md Phase B
provenance: Née 2026-06-11 d'une session où l'OMK Dashboard est bloqué en Phase B par le manque d'un MCP permettant l'exécution SQL programmatique via Claude Code / Codex / Gemini. Décisions doctrinales validées par A0 Turn 1.
---

# ADR-OMK-003 — MCP `supabase-aspace` v0.1 (OMK-scoped)

## Status

**RATIFIED** — Go A0 Turn 1 (2026-06-11). Phases B/C/D/G du dashboard OMK restent bloquées tant que ce MCP n'est pas wire-up. Décisions figées par 10 points (§Decision), schéma doctrinal des 5 outils (§Tool Schemas), et validation post-ratification (§Validation Plan).

> **Note d'isolation** : ce MCP est une **surface OMK-dédiée** (whitelist `omk_internal` + `omk_saas` + `public` utilitaires). Il coexiste avec `_SPECS/MCP/supabase-aspace-spec.md` (A'Space-OS-wide, ACCEPTED 2026-06-10, rôle `aspace_admin`, scope A'Space complet) — qui n'est PAS ce MCP. Les deux sont compatibles : la spec A'Space-OS-wide agit comme le backend Postgres brut, et la présente instance agit comme un **proxy scopé** consommé uniquement par le dashboard OMK (ou tout autre client qui s'authentifie avec le PAT OMK). Voir §Relationship to `_SPECS/MCP/supabase-aspace-spec.md` pour la nuance.

## Context

L'OMK Dashboard (Vite 6.2 + React 19 + TS 5.8, repo `Amdkn/01-OMK-Business-OS`, Dokploy 2 services × 2 schémas) est **bloqué en Phase B** par 4 ADR blockers, dont **Blocker #3** : *MCP `supabase-aspace` v0.1* (cf. `apps/dashboard/AGENTS.md:14`).

Le dashboard doit pouvoir : (1) créer/migrer les schémas `omk_internal` et `omk_saas` (DDL + RLS), (2) inspecter leur état (tables, vues, indexes, policies), (3) générer `database.types.ts` (gotcha #12 `omk/apps/dashboard/CLAUDE.md:187`), (4) appliquer des migrations idempotentes, (5) exécuter du SQL arbitraire en HITL.

Aucun de ces workflows n'est automatisable via le `@supabase/supabase-js` client (PostgREST, surface RLS-scoped, pas de DDL). Il faut un canal **Postgres direct** avec un rôle admin scopé, exposé via **MCP** — le seul protocole agent-agnostique (Claude Code CLI + Codex + Gemini).

## Relationship to `_SPECS/MCP/supabase-aspace-spec.md` (A'Space-OS-wide spec)

D1 — vérifié par `Read` à `C:\Users\amado\ASpace_OS_V2\_SPECS\MCP\supabase-aspace-spec.md` (289 lignes, ACCEPTED 2026-06-10).

| Aspect | A'Space-OS-wide spec | **OMK-003 (ce ADR)** |
|---|---|---|
| **Rôle PG** | `aspace_admin` (full A'Space scope) | `omk_admin` (NEW role, OMK-scoped) |
| **Whitelist schemas** | aucune applicative | `omk_internal` + `omk_saas` + `public` (utilitaires) |
| **Block-list** | `auth.*`, `storage.*`, `realtime.*`, `vault.*`, `pgsodium.*`, `extensions.*`, `graphql_public.*` | Idem + `supabase_functions.*` |
| **Tools** | 10+ | **5** (1:1 API officielle) |
| **Port** | 3100 | 8080 |
| **Auth** | DSN Postgres + PAT bootstrap | **PAT-only** (`Authorization: Bearer <pat>` per MCP 2025-11-25 spec) |
| **Rate limit** | non | **60 req/min/token** |
| **Audit** | `<schema>._aspace_audit` (DB) | `pulse.log` (fichier, no query body) |
| **Use case** | bootstrap A'Space-OS, mesh, Life-OS | OMK Dashboard Phase B |

**Rationale d'un MCP séparé** (per ADR-INFRA-MCP-001 D2 + ADR-SUPABASE-001 D2 + Test Key Pragma) : (1) PAT rotatable indépendamment, (2) whitelist explicite = défense en profondeur (un bug OMK ne peut pas écrire dans `abc_os`/`life_os`), (3) audit log OMK-spécifique, (4) `MCP_SCOPE=read` vs `readwrite`.

## Decision

### D1 — Les 5 outils exposés (1:1 avec l'API officielle `@supabase/mcp-server-postgres`)

D2 — vérifié par `mcp__context7__query-docs` sur `/supabase-community/supabase-mcp` qui liste *"Database Tools (5 tools): `list_tables`, `list_extensions`, `list_migrations`, `execute_sql`, `apply_migration`"* et *"Development Tools (3 tools): `get_project_url`, `get_publishable_keys`, `generate_typescript_types`"*. La surface "Postgres-direct" canonique est : `execute_sql`, `apply_migration`, `list_*`, `get_object_details`, `generate_types`.

Outils OMK (signatures figées, JSON Schemas en §Tool Schemas) :

| # | Outil | Direction | HITL | Description |
|---|---|---|---|---|
| 1 | `exec_sql` | RW | OUI (toujours) | Exécute SQL arbitraire (param: `query: string`, returns `rows: array`) |
| 2 | `list_objects` | R | non | Liste tables/views/sequences d'un schema (params: `schema: string`, `object_type?: 'table' \| 'view' \| 'sequence' \| 'extension'`) |
| 3 | `get_object_details` | R | non | Détails d'une table (DDL, columns, indexes, policies) (params: `schema: string`, `name: string`) |
| 4 | `generate_types` | R | non | Génère `database.types.ts` (params: `schemas: string[]`, returns `typescript: string`) |
| 5 | `apply_migration` | RW | OUI (toujours) | Applique un fichier de migration (params: `path: string`, returns `version: string`) |

> **Différenciation `exec_sql` (ce MCP) vs `execute_sql` (spec A'Space-OS-wide)** : ce MCP utilise le nom canonique de l'API officielle Supabase (`exec_sql`) pour rester 1:1 compatible avec les clients MCP qui auto-invoquent l'API Supabase Cloud. La spec A'Space-OS-wide utilise `execute_sql` (nom interne). Pas de collision fonctionnelle (les deux MCPs sont distincts).

### D2 — Transport : HTTP (Streamable HTTP, MCP 2025-11-25 spec)

D2 — vérifié par `mcp__context7__query-docs` sur `/modelcontextprotocol/modelcontextprotocol` (docs/specification/2025-11-25/basic/transports.mdx) :

> *"Streamable HTTP transport ... uses HTTP POST and GET requests ... A single HTTP endpoint path (the MCP endpoint) must support both POST and GET methods."*

- **Bind** : `127.0.0.1:8080` (localhost-only, per spec : *"Servers SHOULD bind only to localhost (127.0.0.1) when running locally"*).
- **Endpoint unique** : `http://127.0.0.1:8080/mcp` (POST + GET).
- **Pourquoi pas stdio** : stdio bloque l'usage depuis Claude Code CLI distant (sur VPS), Codex (qui spawn ses propres processus) et Gemini (qui ne sait pas pipe un stdio MCP). HTTP = surface agnostique, un seul process daemon sert N clients.

### D3 — Auth : Supabase PAT (Personal Access Token), Bearer dans `Authorization` header

D2 — vérifié par `mcp__context7__query-docs` sur `/supabase/supabase` (apps/docs/content/guides/ai-tools/mcp.mdx) — config officielle montre `headers: { "Authorization": "Bearer ${SUPABASE_ACCESS_TOKEN}" }`. Et `/modelcontextprotocol/modelcontextprotocol` (authorization.mdx) : *"HTTP GET Request with Authorization ... GET /mcp HTTP/1.1 ... Authorization: Bearer eyJ..."* (RFC 6750, OAuth 2.1).

- **Header** : `Authorization: Bearer ${SUPABASE_ACCESS_TOKEN}`.
- **Source** : Supabase Dashboard → Account → Access Tokens. PAT = *"long-lived tokens ... carry the same privileges as your user account"* (per `supabase/docs/ref/api/introduction.mdx`).
- **Scope env var** : `MCP_SCOPE=read` (défaut v0.1, refuse RW) ou `readwrite` (autorise `exec_sql` + `apply_migration`).
- **Validation boot** : `GET https://api.supabase.com/v1/profile`, fail-fast si 401.
- **Pas de service_role** : JWT service_role non accepté par le endpoint MCP (et ne doit pas l'être — garderait la surface admin côté client).
- **Stockage** : env var Windows User scope `SUPABASE_ACCESS_TOKEN` (Test Key Pragma).
- **Rotation** : rotatable via Dashboard A0 ; webhook notif A2 (v0.2).

### D4 — Scope DB strict : whitelist explicite, block-list explicite

D1 — vérifié par `omk/apps/dashboard/CLAUDE.md:45-50` (mode `internal` → `omk_internal`, mode `saas` → `omk_saas`, RLS via `org_id` JWT claim).

**Whitelist** (le MCP **peut** lire/écrire) : `omk_internal`, `omk_saas`, `public` (limité aux fonctions utilitaires type `custom_access_token_hook`, cf. ADR-OMK-001 D3).

**Block-list** (le MCP **ne peut PAS** toucher, REVOKE explicite au boot, audited) : `auth.*` (users, sessions, identities, refresh_tokens), `storage.*` (objects, buckets), `vault.*` (secrets), `supabase_functions.*` (renforcé vs spec A'Space-OS-wide), `pgsodium.*`, `extensions.*`, `graphql_public.*`, `realtime.*`.

**Mécanisme d'enforcement** (côté MCP) : (1) parse SQL, extrait `schemaname.tablename` référencés via regex · (2) si dans block-list → erreur 403 `BLOCKED_SYSTEM_SCHEMA` · (3) si dans whitelist → laisse passer · (4) sinon → erreur 403 `BLOCKED_NON_WHITELIST_SCHEMA`.

### D5 — Rate limit : 60 req/min par token

Token bucket en mémoire, sliding window 60s, par hash(PAT). Au-delà : erreur 429 + audit `RATE_LIMITED`. **Defensive DoS mitigation** (un agent qui boucle ou un prompt injecté ne sature pas PostgREST/Postgres). Pas de rate limit inter-tools (60 global). Bump future v0.2 via `MCP_RATE_LIMIT_PER_MIN`.

### D6 — Audit log : `pulse.log` côté serveur MCP (fichier, pas DB)

**Chemin** : `C:\Users\amado\.mcp_servers\supabase-aspace-v0.1\pulse.log` (append-only JSONL). Format : `{"ts":"...","tool":"exec_sql","schema":"omk_saas","row_count":3,"duration_ms":42,"actor_hash":"a1b2...","audit_tag":"RW"}`.

**Loggé** : `ts` (ISO 8601 UTC), `tool`, `schema` (touché), `row_count` (0 pour DDL), `duration_ms`, `actor_hash` (SHA-256 du PAT, jamais le PAT ni l'email), `audit_tag` (`R`/`RW`/`BLOCKED_*`/`RATE_LIMITED`).

**NON loggé** : `query` (SQL brut), `params`, `rows` data. **Privacy + log bloat** (un `SELECT * FROM clients` retourne des PII).

**Rotation** : Shadow L0 `heartbeat-tick` quotidien (déjà câblé sur `.mcp_servers/*`). **Pas de table DB** (vs spec A'Space-OS-wide qui log dans `<schema>._aspace_audit`) — choix fichier parce que (a) on ne veut pas créer de table dans `omk_*` à ce stade, (b) shell-standard lisible, (c) Shadow L0 peut rotate.

### D7 — `MCP_SCOPE=read` par défaut, `=readwrite` HITL

- **`read` (défaut v0.1)** : `exec_sql` et `apply_migration` retournent 403 `READ_ONLY_MODE` ; `list_objects`, `get_object_details`, `generate_types` OK.
- **`readwrite`** : tous tools actifs, mais RW tools marquent chaque appel `audit_tag=RW` + loguent `duration_ms` (forensic).
- **HITL côté caller** : ce MCP ne **force** pas la confirmation A0 (le caller le fait). Pattern "double convocation" de `supabase-aspace-spec.md:111-132` documenté mais pas implémenté v0.1 (YAGNI — A0 lit le `pulse.log` de toute façon).

### D8 — Self-hosted URL : `https://supabase.148.230.92.235.sslip.io`

D1 — vérifié par `omk/apps/dashboard/AGENTS.md:45` (*"Self-hosted at `https://supabase.148.230.92.235.sslip.io` (VPS `aspace-vps`)"*) et `omk/apps/dashboard/CLAUDE.md:165` (env Dokploy).

- **Endpoint DB** : `https://supabase.148.230.92.235.sslip.io` (PostgREST + Studio + Auth).
- **Endpoint Postgres direct** : `148.230.92.235:5432` (port standard, ouvert en interne sur le VPS).
- **Pourquoi pas l'URL Cloud Supabase** : on est en self-hosted, le PAT généré sur le Dashboard self-hosted a scope sur **ce projet-là** uniquement.

### D9 — Repo MCP : nouvelle arbo pour la spec d'implémentation (PAS de code MCP dans cette session)

- **Spec d'implémentation** (post-ratification, future session) : `C:\Users\amado\ASpace_OS_V2\_SPECS\MCP\mcp-supabase-aspace-v0.1\README.md` (sibling de `supabase-aspace-spec.md` qui couvre A'Space-OS-wide).
- **Code MCP** : future session, après ratification. Arborescence cible (à figer dans le spec) :
  ```
  C:/Users/amado/.mcp_servers/supabase-aspace-v0.1/
  ├── package.json            (deps: @modelcontextprotocol/sdk@^1.29, @supabase/supabase-js@^2.107, zod, pg, pino)
  ├── tsconfig.json
  ├── .env.example            (vide — env vars User scope only)
  ├── .gitignore
  ├── pulse.log               (généré au runtime, gitignored)
  ├── README.md
  └── src/
      ├── index.ts            (entry: HTTP transport, tool registration, rate limit, scope gate, audit)
      ├── auth/pat-validator.ts
      ├── scope/whitelist.ts
      ├── safety/rate-limit.ts
      ├── audit/logger.ts
      ├── tools/
      │   ├── exec-sql.ts
      │   ├── list-objects.ts
      │   ├── get-object-details.ts
      │   ├── generate-types.ts
      │   └── apply-migration.ts
      └── server.ts           (StreamableHTTPServerTransport, 127.0.0.1:8080)
  ```
- **Cette session ne crée PAS le code MCP** — uniquement le README de spec. Voir §Deliverable 2.

### D10 — Wire-up `.mcp.json` : A0 applique manuellement le snippet après ratification

- Le sub-agent (cette session) **ne modifie PAS** `C:\Users\amado\.mcp.json`. A0 l'ajoutera manuellement après le Go de ratification, pour que la trace HITL soit dans son transcript A0.
- Le snippet **est fourni dans cet ADR** (§Rollout), pour que A0 fasse un copy-paste informé.

## Tool Schemas

D2 — toutes les structures ci-dessous sont des **JSON Schema valides** (parseable par `JSON.parse` + `ajv`). Le format suit la spec MCP 2025-11-25 (cf. `mcp__context7__query-docs` sur `/modelcontextprotocol/modelcontextprotocol`, docs/specification/2025-11-25/schema.mdx) : `inputSchema` et `outputSchema` ont **toujours** `type: "object"` et peuvent inclure `$schema`, `properties`, `required`.

### 1. `exec_sql`

**Description** : Exécute une requête SQL arbitraire sur le Supabase OMK. Refuse si SQL touche un schéma hors whitelist (§D4). Refuse si `MCP_SCOPE=read`. Log audit `audit_tag=RW`.

```json
{
  "name": "exec_sql",
  "title": "Execute SQL (RW, HITL)",
  "description": "Execute an arbitrary SQL query against the OMK Supabase schemas (omk_internal, omk_saas, public utilities). DDL, DML, and SELECT are all accepted. The MCP validates the SQL touches only whitelisted schemas (otherwise 403 BLOCKED_NON_WHITELIST_SCHEMA). Requires MCP_SCOPE=readwrite. Every call is audited (audit_tag=RW) in pulse.log without logging the query body.",
  "inputSchema": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "The SQL query to execute. May be a SELECT, INSERT, UPDATE, DELETE, or DDL statement. Multiple statements separated by ';' are executed in a single implicit transaction."
      }
    },
    "required": ["query"],
    "additionalProperties": false
  },
  "outputSchema": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "rows": {
        "type": "array",
        "description": "Result rows for SELECT queries. For DDL/DML, this is an empty array.",
        "items": { "type": "object", "additionalProperties": true }
      },
      "rowCount": {
        "type": "integer",
        "description": "Number of rows returned (SELECT) or affected (DML)."
      },
      "durationMs": {
        "type": "integer",
        "description": "Server-side execution time in milliseconds."
      },
      "auditTag": {
        "type": "string",
        "enum": ["RW", "BLOCKED_SYSTEM_SCHEMA", "BLOCKED_NON_WHITELIST_SCHEMA", "READ_ONLY_MODE", "RATE_LIMITED"],
        "description": "Audit classification of the call."
      }
    },
    "required": ["rows", "rowCount", "durationMs", "auditTag"],
    "additionalProperties": false
  }
}
```

**Exemple (réduit)** : `exec_sql({query: "SELECT count(*) FROM omk_saas.memberships WHERE org_id = '00000000-0000-0000-0000-000000000001'::uuid"})` → `{rows: [{n: 3}], rowCount: 1, durationMs: 12, auditTag: "RW"}`.

### 2. `list_objects`

**Description** : Liste les tables / vues / sequences / extensions d'un schéma OMK. Pas de HITL. Read-only.

```json
{
  "name": "list_objects",
  "title": "List Objects in Schema",
  "description": "List tables, views, sequences, or extensions in a whitelisted OMK schema. Returns the object name, type, and (for tables) row estimate. Read-only, no HITL.",
  "inputSchema": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "schema": {
        "type": "string",
        "enum": ["omk_internal", "omk_saas", "public"],
        "description": "The schema to list objects from. Must be in the OMK whitelist."
      },
      "objectType": {
        "type": "string",
        "enum": ["table", "view", "sequence", "extension"],
        "description": "Filter by object type. Omit to list all."
      }
    },
    "required": ["schema"],
    "additionalProperties": false
  },
  "outputSchema": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "objects": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": { "type": "string" },
            "type": { "type": "string", "enum": ["table", "view", "sequence", "extension"] },
            "rowEstimate": { "type": ["integer", "null"] }
          },
          "required": ["name", "type"],
          "additionalProperties": false
        }
      },
      "durationMs": { "type": "integer" },
      "auditTag": { "type": "string", "enum": ["R", "BLOCKED_NON_WHITELIST_SCHEMA", "RATE_LIMITED"] }
    },
    "required": ["objects", "durationMs", "auditTag"],
    "additionalProperties": false
  }
}
```

**Exemple (réduit)** : `list_objects({schema: "omk_saas", objectType: "table"})` → `{objects: [{name: "organizations", type: "table", rowEstimate: 12}, {name: "memberships", type: "table", rowEstimate: 47}], durationMs: 8, auditTag: "R"}`.

### 3. `get_object_details`

**Description** : Détails d'une table (DDL, columns, indexes, RLS policies, RLS status). Read-only.

```json
{
  "name": "get_object_details",
  "title": "Get Object Details",
  "description": "Get detailed information about a specific table or view in an OMK schema: columns (name, type, nullable, default), indexes, RLS policies, and whether RLS is enabled. Read-only, no HITL.",
  "inputSchema": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "schema": {
        "type": "string",
        "enum": ["omk_internal", "omk_saas", "public"],
        "description": "The schema containing the object."
      },
      "name": {
        "type": "string",
        "description": "The table or view name."
      }
    },
    "required": ["schema", "name"],
    "additionalProperties": false
  },
  "outputSchema": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "name": { "type": "string" },
      "type": { "type": "string", "enum": ["table", "view"] },
      "columns": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": { "type": "string" },
            "dataType": { "type": "string" },
            "isNullable": { "type": "boolean" },
            "defaultValue": { "type": ["string", "null"] }
          },
          "required": ["name", "dataType", "isNullable"],
          "additionalProperties": false
        }
      },
      "indexes": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": { "type": "string" },
            "definition": { "type": "string" }
          },
          "required": ["name", "definition"],
          "additionalProperties": false
        }
      },
      "rlsEnabled": { "type": "boolean" },
      "policies": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": { "type": "string" },
            "command": { "type": "string", "enum": ["SELECT", "INSERT", "UPDATE", "DELETE", "ALL"] },
            "using": { "type": ["string", "null"] }
          },
          "required": ["name", "command"],
          "additionalProperties": false
        }
      },
      "durationMs": { "type": "integer" },
      "auditTag": { "type": "string", "enum": ["R", "BLOCKED_NON_WHITELIST_SCHEMA", "RATE_LIMITED"] }
    },
    "required": ["name", "type", "columns", "rlsEnabled", "durationMs", "auditTag"],
    "additionalProperties": false
  }
}
```

**Exemple (réduit)** : `get_object_details({schema: "omk_saas", name: "memberships"})` → `{name: "memberships", type: "table", columns: [...3 cols...], indexes: [...], rlsEnabled: true, policies: [...], durationMs: 23, auditTag: "R"}`.

### 4. `generate_types`

**Description** : Génère `database.types.ts` (type-safe Supabase client) pour le(s) schéma(s) OMK. Wrapper autour de `supabase gen types typescript --linked` ou introspection SQL directe. Read-only.

```json
{
  "name": "generate_types",
  "title": "Generate TypeScript Types",
  "description": "Generate TypeScript type definitions (database.types.ts) for the whitelisted OMK schemas. Wraps `supabase gen types typescript` and returns the .ts content as a string. Read-only, no HITL.",
  "inputSchema": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "schemas": {
        "type": "array",
        "items": {
          "type": "string",
          "enum": ["omk_internal", "omk_saas", "public"]
        },
        "minItems": 1,
        "description": "List of schemas to include in the generated types. Must be a subset of the OMK whitelist."
      }
    },
    "required": ["schemas"],
    "additionalProperties": false
  },
  "outputSchema": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "typescript": {
        "type": "string",
        "description": "The generated TypeScript source code. Intended to be written to omk/apps/dashboard/src/lib/database.types.ts."
      },
      "schemasIncluded": {
        "type": "array",
        "items": { "type": "string" }
      },
      "durationMs": { "type": "integer" },
      "auditTag": { "type": "string", "enum": ["R", "RATE_LIMITED"] }
    },
    "required": ["typescript", "schemasIncluded", "durationMs", "auditTag"],
    "additionalProperties": false
  }
}
```

**Exemple (réduit)** : `generate_types({schemas: ["omk_saas"]})` → `{typescript: "export type Json = ...\nexport interface Database { ... }", schemasIncluded: ["omk_saas"], durationMs: 142, auditTag: "R"}`.

### 5. `apply_migration`

**Description** : Applique un fichier de migration SQL depuis le disque (chemin validé). Requiert un header `aspace-migration-id` pour idempotence. Refuse si `MCP_SCOPE=read`. Log audit `audit_tag=RW`.

```json
{
  "name": "apply_migration",
  "title": "Apply Migration (RW, HITL)",
  "description": "Apply a SQL migration file from disk to the OMK Supabase. The file must contain an `aspace-migration-id` header for idempotency. The MCP reads the file, parses the header, and applies the SQL in a transaction. If the migration ID is already recorded in the schema's _aspace_migrations table, the call returns audit_tag=ALREADY_APPLIED without re-running. Requires MCP_SCOPE=readwrite. Audited (audit_tag=RW or ALREADY_APPLIED) in pulse.log.",
  "inputSchema": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "path": {
        "type": "string",
        "description": "Absolute Windows path to the .sql migration file. Must reside under C:\\Users\\amado\\ASpace_OS_V2\\30_Business_OS\\10_Projects\\omk\\apps\\dashboard\\sql\\ (path validation: file paths outside this root are rejected for safety)."
      }
    },
    "required": ["path"],
    "additionalProperties": false
  },
  "outputSchema": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "version": {
        "type": "string",
        "description": "The aspace-migration-id extracted from the file header. Format: YYYY_MM_DD_NNN_shortname."
      },
      "appliedAt": {
        "type": "string",
        "format": "date-time",
        "description": "ISO 8601 UTC timestamp of application."
      },
      "durationMs": { "type": "integer" },
      "auditTag": {
        "type": "string",
        "enum": ["RW", "ALREADY_APPLIED", "INVALID_HEADER", "PATH_OUTSIDE_ROOT", "READ_ONLY_MODE", "RATE_LIMITED", "BLOCKED_SYSTEM_SCHEMA", "BLOCKED_NON_WHITELIST_SCHEMA"]
      }
    },
    "required": ["version", "appliedAt", "durationMs", "auditTag"],
    "additionalProperties": false
  }
}
```

**Format du header de migration (obligatoire)** :
```sql
-- aspace-migration-id: 2026_06_11_001_create_omk_saas_organizations
-- aspace-migration-checksum: sha256:<hex>
-- aspace-migration-target-schema: omk_saas
-- (le reste du SQL suit)
```

**Exemple (réduit)** : `apply_migration({path: "C:\\Users\\amado\\ASpace_OS_V2\\30_Business_OS\\10_Projects\\omk\\apps\\dashboard\\sql\\omk_saas\\2026_06_11_001_create_organizations.sql"})` → `{version: "2026_06_11_001_create_omk_saas_organizations", appliedAt: "2026-06-11T14:32:01.123Z", durationMs: 87, auditTag: "RW"}`.

## Consequences

**Positive** : Phase B unblocked (Blocker #3 résolu) · tool surface 1:1 API officielle Supabase · souveraineté (bind 127.0.0.1, VPS Supabase seule surface réseau) · audit complet sans PII leak (`pulse.log` no query body) · whitelist defense-in-depth (un bug MCP ne peut pas écrire dans `auth`/`storage`/`vault`/`supabase_functions`).

**Cost / risk** : rate limit 60 req/min tapeur sur loops (mitigation : batching, future bump env var) · PAT a tous les privilèges A0 (mitigation : Test Key Pragma, rotation trimestrielle, scope `read` défaut) · double-MCP coexiste avec A'Space-OS-wide (mitigation : noms distincts `supabase-aspace` vs `supabase-aspace-omk`) · `PGRST_DB_SCHEMAS` reload reste HITL VPS-side (per `omk/apps/dashboard/CLAUDE.md:180` gotcha #5, ADR-SUPABASE-001 D7).

## Rollout

**Step 1 — A0 crée le PAT** (Dashboard self-hosted `https://supabase.148.230.92.235.sslip.io` → Account → Access Tokens → Generate New Token, name=`mcp-supabase-aspace-omk-v0.1`, scopes="All" par défaut v0.1 ; user dédié `mcp-omk` recommandé v0.2). Token copié 1× (jamais re-affiché, jamais en chat — Test Key Pragma).

**Step 2 — A0 set env vars User scope** :
```powershell
[Environment]::SetEnvironmentVariable('SUPABASE_ACCESS_TOKEN', '<le-token>', 'User')
[Environment]::SetEnvironmentVariable('MCP_SCOPE', 'read', 'User')   # ou 'readwrite' pour autoriser exec_sql + apply_migration
[Environment]::SetEnvironmentVariable('MCP_RATE_LIMIT_PER_MIN', '60', 'User')   # optionnel, défaut 60
```

**Step 3 — A0 lance le MCP en background** (post-impl, future session A3) :
```powershell
cd C:\Users\amado\.mcp_servers\supabase-aspace-v0.1\
npm install
npm run start   # bind 127.0.0.1:8080, log dans pulse.log
```

**Step 4 — A0 wire-up `.mcp.json` manuellement** (HITL, le sub-agent ne touche PAS ce fichier) :
```json
{
  "mcpServers": {
    "supabase-aspace-omk": {
      "type": "http",
      "url": "http://127.0.0.1:8080/mcp",
      "headers": { "Authorization": "Bearer ${SUPABASE_ACCESS_TOKEN}" }
    }
  }
}
```
Nom = `supabase-aspace-omk` (pas `supabase-aspace` qui est l'A'Space-OS-wide) pour éviter la collision.

**Step 5 — A0 smoke test (5 calls parallèles, per `/mcp-mastery` skill)** :
```bash
mcp call supabase-aspace-omk list_objects          '{"schema":"omk_saas"}'
mcp call supabase-aspace-omk get_object_details    '{"schema":"omk_saas","name":"organizations"}'
mcp call supabase-aspace-omk generate_types        '{"schemas":["omk_saas","omk_internal"]}'
mcp call supabase-aspace-omk exec_sql              '{"query":"SELECT now() AS server_time"}'
mcp call supabase-aspace-omk apply_migration       '{"path":"<...>"}'   # skipped si MCP_SCOPE=read
```

**Step 6 — Phase B OMK** : (1) `exec_sql`/`apply_migration` crée `omk_internal`+`omk_saas` (DDL dans `apps/dashboard/sql/99_README.md`) · (2) `exec_sql` GRANT USAGE/SELECT à anon/authenticated, GRANT ALL à service_role (per ADR-SUPABASE-001 D3) · (3) RLS policies (`org_id = (auth.jwt() ->> 'org_id')::uuid`, ADR-OMK-001 D2) · (4) `generate_types` produit `apps/dashboard/src/lib/database.types.ts` (résout gotcha #12) · (5) HITL VPS-side reload `PGRST_DB_SCHEMAS` (NOT automatisable depuis MCP, A0 notifie Codex/Hermes, ADR-SUPABASE-001 D7).

## References

**Sources lues (D1 — path:ligne)** :
- `omk/apps/dashboard/AGENTS.md:14` — *"MCP `supabase-aspace` v0.1 | ⏳ à implémenter"* (Blocker #3)
- `omk/apps/dashboard/AGENTS.md:45` — *"Self-hosted at `https://supabase.148.230.92.235.sslip.io`"*
- `omk/apps/dashboard/CLAUDE.md:50,165,180,187` — blockers list + self-hosted URL + gotcha #5 PGRST_DB_SCHEMAS + gotcha #12 database.types.ts
- `_SPECS/ADR/ADR-OMK-001_dual-product-dashboard-multitenant.md` — D2 multi-tenancy, D3 JWT custom hook, D5 dépendance ADR-SUPABASE-001
- `_SPECS/ADR/ADR-SUPABASE-001_self-hosted-multi-tenancy-schemas.md:53,79` — D2 dual-MCP doctrine + D4 `aspace_admin` role (pas SUPERUSER, REVOKE explicite)
- `_SPECS/ADR/ADR-INFRA-MCP-001_agentic-mcp-mastery-dox-god-mode.md` — vault centralisé, rotation, HITL
- `_SPECS/ADR/ADR-META-001_anti-paresse-verify-before-assert.md` — D1-D8 doctrine
- `_SPECS/MCP/supabase-aspace-spec.md` — sibling spec A'Space-OS-wide (289 lignes, ACCEPTED 2026-06-10)

**Sources context7 (D2 — libraryId / query / finding)** :
- `/supabase-community/supabase-mcp` / tools list query / Finding : *"Database Tools (5 tools): `list_tables`, `list_extensions`, `list_migrations`, `execute_sql`, `apply_migration`. Development Tools (3 tools): `get_project_url`, `get_publishable_keys`, `generate_typescript_types`."* → surface Postgres-direct canonique = `execute_sql` + `apply_migration` + `list_*` + `get_object_details` + `generate_typescript_types` (= notre `generate_types`).
- `/alexander-zuev/supabase-mcp-server` / tools structure query / Finding : `Tool = {name, description, inputSchema: {type:"object", properties, required}}` (cf. `tools/list` + `tools/call`).
- `/modelcontextprotocol/modelcontextprotocol` / spec 2025-11-25 query / Findings : (1) `inputSchema`/`outputSchema` JSON Schema `type:"object"` + `$schema` (schema.mdx) · (2) Streamable HTTP = POST + GET sur même endpoint (basic/transports.mdx) · (3) Auth = `Authorization: Bearer <access-token>` RFC 6750 OAuth 2.1 (basic/authorization.mdx) · (4) Servers MUST validate `Origin` + SHOULD bind localhost.
- `/supabase/supabase` / PAT query / Findings : (1) Format officiel `Authorization: Bearer YOUR_PERSONAL_ACCESS_TOKEN` · (2) `.mcp.json` officielle `headers: { Authorization: Bearer ${SUPABASE_ACCESS_TOKEN} }` (apps/docs/content/guides/ai-tools/mcp.mdx) · (3) Env var canonique `SUPABASE_ACCESS_TOKEN` · (4) PAT = *"long-lived tokens ... carry the same privileges as your user account"* (supabase/docs/ref/api/introduction.mdx).

## Validation Plan

- [ ] A0 ratifie (`"Go pour ADR-OMK-003"`) · crée PAT (Step 1) · set env vars User (Step 2) · implémente code MCP (post-ratification, per spec `_SPECS/MCP/mcp-supabase-aspace-v0.1/`) · lance background (Step 3) + vérifie `pulse.log` · wire-up `.mcp.json` (Step 4) · smoke test 5 calls (Step 5) · Phase B step 1-4 via MCP (Step 6) · Phase B step 5 (HITL VPS-side reload `PGRST_DB_SCHEMAS`) · `apps/dashboard/src/lib/database.types.ts` committé (gotcha #12 résolu) · `apps/dashboard/AGENTS.md` §1 mis à jour (Blocker #3 = ✅ DONE) · `apps/dashboard/REBUILD_WORKFLOW.md` §0 mis à jour · `_SPECS/REGISTRY/supabase_schemas.md` mis à jour.

## Anti-patterns interdits (rappel doctrine)

| Interdit | Raison |
|---|---|
| Hardcoder le PAT dans `.md`/`.json`/`.ps1`/git | Test Key Pragma |
| Logger le query body dans `pulse.log` | PII leak + log bloat |
| `DROP`/`DELETE FROM`/`TRUNCATE` sans HITL côté caller | défense en profondeur |
| GRANT sur `auth.*`/`storage.*`/`vault.*`/`supabase_functions.*` | escalade rôle |
| Bind le MCP sur `0.0.0.0` | exposition réseau |
| Court-circuiter le scope gate | contournement whitelist |
| Wire-up `.mcp.json` par sub-agent sans HITL A0 | trace transcript A0 |
| `console.log` / `any` (futur code MCP) | code-style TS common |
| Oublier de recharger `PGRST_DB_SCHEMAS` | schémas invisibles côté PostgREST |

## Open follow-ups (post-MVP)

- **v0.2** : rôle PG `omk_admin` dédié, env var `MCP_RATE_LIMIT_PER_MIN` configurable, webhook notif rotation PAT, dry-run mode pour `apply_migration`, export `pulse.log` vers dashboard.
- **v1.0** : multi-project support, OAuth 2.1 (per MCP 2025-11-25 spec, rotation automatique).

## Acceptance criteria for ratification

A0 to confirm (10 points) : (1) Tool surface D1 (5 outils) · (2) Transport HTTP D2 (Streamable, 127.0.0.1:8080) · (3) Auth PAT D3 (Supabase PAT, Bearer, scope env var) · (4) Whitelist/block-list D4 (`omk_internal`+`omk_saas`+`public` utilitaires ; `auth.*`/`storage.*`/`vault.*`/`supabase_functions.*` interdits) · (5) Rate limit 60 req/min D5 · (6) Audit log `pulse.log` D6 (no query body) · (7) `MCP_SCOPE=read` défaut D7 · (8) Self-hosted URL D8 · (9) Repo spec-only D9 (cette session livre ADR + spec README, pas le code MCP) · (10) `.mcp.json` wire-up manuel A0 D10.
