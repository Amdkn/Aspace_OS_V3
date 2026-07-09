---
id: MCP-SUPABASE-ASPACE-OMK-V0.1-SPEC
title: mcp-supabase-aspace-v0.1 — Implementation Spec (OMK-scoped, sibling of A'Space-OS-wide)
status: SPEC (awaiting code post-ADR-OMK-003 ratification)
date: 2026-06-11
deciders: [A0 Amadeus]
proposed_by: Claude Code (A2)
domain: L2 Business OS / OMK Services / Data Plane / Self-Hosted Supabase
related:
  - ADR-OMK-003 (parent: tool surface, scope, rate limit, audit, wire-up)
  - _SPECS/MCP/supabase-aspace-spec.md (sibling: A'Space-OS-wide, role aspace_admin)
  - _SPECS/ADR/ADR-SUPABASE-001 (parent: dual-MCP doctrine)
  - _SPECS/ADR/ADR-INFRA-MCP-001 (dox + vault + rotation pattern)
tags: [#spec #mcp #supabase #aspace #omk #postgres #rls #pat #readwrite]
---

# mcp-supabase-aspace-v0.1 — Implementation Spec (OMK-scoped)

> **Parent ADR** : `_SPECS/ADR/ADR-OMK-003_mcp-supabase-aspace.md` (RATIFIED 2026-06-11).
> **Sibling spec** : `_SPECS/MCP/supabase-aspace-spec.md` (A'Space-OS-wide, ACCEPTED 2026-06-10).
> **Lecteur** : A3 sub-agent (future session de dev) qui implémentera le code TypeScript.

## 1. Pourquoi ce MCP (rappel)

L'OMK Dashboard est bloqué en Phase B par le manque d'un canal Postgres direct, agent-agnostique (Claude Code + Codex + Gemini), qui expose 5 outils standard : `exec_sql`, `list_objects`, `get_object_details`, `generate_types`, `apply_migration`. Ce MCP est la réponse.

**Différenciation vs `_SPECS/MCP/supabase-aspace-spec.md`** :

| Aspect | A'Space-OS-wide (sibling) | **OMK v0.1 (ce MCP)** |
|---|---|---|
| Rôle PG | `aspace_admin` (A'Space scope) | user A0 + PAT (OMK scope via whitelist applicative) |
| Whitelist schemas | aucune applicative (admin) | `omk_internal` + `omk_saas` + `public` (limité) |
| Block-list | `auth.*`, `storage.*`, `realtime.*`, `vault.*`, `pgsodium.*`, `extensions.*`, `graphql_public.*` | Idem + `supabase_functions.*` |
| Port | 3100 | 8080 |
| Tools | 10+ | 5 (1:1 API officielle Supabase) |
| Audit | `<schema>._aspace_audit` (DB, hash SQL) | `pulse.log` (fichier, pas de query body) |
| Rate limit | non spécifié | 60 req/min/token |
| Scope env var | non | `MCP_SCOPE=read` (défaut) ou `readwrite` |

## 2. Arborescence cible du repo (à créer post-ratification)

```
C:/Users/amado/.mcp_servers/supabase-aspace-v0.1/
├── package.json            (deps ci-dessous §3)
├── tsconfig.json           (strict, target ES2022, module NodeNext)
├── .env.example            (VIDE — env vars User scope only, Test Key Pragma)
├── .gitignore              (node_modules, dist, pulse.log, .env)
├── pulse.log               (généré au runtime, gitignored, append-only)
├── README.md               (quick start pour A0)
└── src/
    ├── index.ts                  # entry: HTTP transport init, tool registration, graceful shutdown
    ├── server.ts                 # Server factory (StreamableHTTPServerTransport, bind 127.0.0.1:8080)
    ├── config/
    │   └── env.ts                # parse + validate env vars (zod), fail-fast si manquant
    ├── auth/
    │   └── pat-validator.ts      # GET api.supabase.com/v1/profile avec Bearer, fail-fast si 401
    ├── scope/
    │   ├── whitelist.ts          # { omk_internal, omk_saas, public-utilities }
    │   ├── blocklist.ts          # { auth, storage, vault, supabase_functions, pgsodium, extensions, graphql_public, realtime }
    │   └── gate.ts               # parse SQL, extract schemaname.tablename refs, ALLOW | DENY
    ├── safety/
    │   ├── rate-limit.ts         # token bucket sliding window 60s, par token PAT
    │   └── origin-check.ts       # validate Origin header (MCP 2025-11-25 MUST per spec)
    ├── audit/
    │   └── logger.ts             # pino, write JSONL to pulse.log, jamais query body
    ├── tools/
    │   ├── exec-sql.ts           # exec_sql: query → pg.Pool.query, retourne {rows, rowCount, durationMs, auditTag}
    │   ├── list-objects.ts       # list_objects: query information_schema.tables/views/sequences/extensions
    │   ├── get-object-details.ts # get_object_details: query columns + indexes + pg_policies + pg_class.relrowsecurity
    │   ├── generate-types.ts     # generate_types: wrapper `supabase gen types typescript` via child_process
    │   └── apply-migration.ts    # apply_migration: read file, parse aspace-migration-id header, exec in tx, INSERT _aspace_migrations
    └── shared/
        ├── pg-pool.ts            # node-postgres Pool, lazy connect
        ├── zod-schemas.ts        # input/output JSON Schemas (Zod) pour les 5 tools
        └── errors.ts             # McpError factory: BLOCKED_SYSTEM_SCHEMA, BLOCKED_NON_WHITELIST_SCHEMA, READ_ONLY_MODE, RATE_LIMITED, INVALID_HEADER, PATH_OUTSIDE_ROOT
```

## 3. Dépendances npm

```json
{
  "name": "supabase-aspace-v0.1",
  "version": "0.1.0",
  "type": "module",
  "engines": { "node": ">=20.0.0" },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.29.0",
    "@supabase/supabase-js": "^2.107.0",
    "pg": "^8.13.0",
    "zod": "^3.23.0",
    "pino": "^9.5.0",
    "pino-pretty": "^11.3.0"
  },
  "devDependencies": {
    "@types/node": "^22.10.0",
    "@types/pg": "^8.11.10",
    "typescript": "^5.8.0",
    "tsx": "^4.19.0"
  },
  "scripts": {
    "start": "node --import tsx/esm src/index.ts",
    "dev": "node --import tsx/esm --watch src/index.ts",
    "typecheck": "tsc --noEmit",
    "lint": "echo 'TODO: add eslint'"
  }
}
```

> **Pourquoi `@supabase/supabase-js` 2.107** : c'est la version pinned dans `omk/apps/dashboard/package.json` (cf. `omk/apps/dashboard/CLAUDE.md:24`). On garde la cohérence.
> **Pourquoi `pg` 8.13** : DSN direct, pas via PostgREST (qui est RLS-scoped). Le MCP parle à Postgres en raw, comme `supabase-solaris` (sibling).
> **Pourquoi pas `@supabase/mcp-server-postgres` officiel** : il est conçu pour **Supabase Cloud** (URL `https://mcp.supabase.com/mcp`), pas pour self-hosted avec whitelist OMK. On ré-implémente la même surface tool (5 outils 1:1) pour avoir le scope gate.

## 4. Contrat doctrinal (les 5 outils + scope + rate limit + audit)

Voir ADR-OMK-003 §Tool Schemas pour les JSON Schemas complets. Résumé opérationnel :

| Outil | Direction | HITL côté caller | Rate-limited | Audité |
|---|---|---|---|---|
| `exec_sql` | RW | OUI (toujours) | oui | `audit_tag=RW` |
| `list_objects` | R | non | oui | `audit_tag=R` |
| `get_object_details` | R | non | oui | `audit_tag=R` |
| `generate_types` | R | non | oui | `audit_tag=R` |
| `apply_migration` | RW | OUI (toujours) | oui | `audit_tag=RW` ou `ALREADY_APPLIED` |

**Whitelist gate** (chaque appel `exec_sql` / `apply_migration`) :
1. Parse SQL, extrait les schemaname.tablename via regex `/\b(omk_internal|omk_saas|public|auth|storage|...)\.\w+/g`.
2. Pour chaque ref : si dans block-list → `McpError(403, 'BLOCKED_SYSTEM_SCHEMA', audit_tag='BLOCKED_SYSTEM_SCHEMA')`.
3. Si dans whitelist → laisser passer.
4. Sinon (schéma inconnu) → `McpError(403, 'BLOCKED_NON_WHITELIST_SCHEMA', audit_tag='BLOCKED_NON_WHITELIST_SCHEMA')`.
5. Toute la transaction est dans une `BEGIN ... COMMIT` (apply_migration wrappe tout, exec_sql fait un seul statement).

**Rate limit** (token bucket sliding window 60s) :
- Bucket key = hash(SUPABASE_ACCESS_TOKEN) (per-token, pas global).
- Capacity 60, refill 1 token/sec.
- Au-delà : `McpError(429, 'RATE_LIMITED', audit_tag='RATE_LIMITED')`.

**Audit log** (`pulse.log`, JSONL append-only) :
```json
{"ts":"2026-06-11T14:32:01.123Z","tool":"exec_sql","schema":"omk_saas","row_count":3,"duration_ms":42,"actor_hash":"a1b2c3d4...","audit_tag":"RW"}
```
- `actor_hash` = SHA-256 du PAT (jamais le PAT lui-même, jamais le user email).
- `query` JAMAIS loggé.
- Rotation : Shadow L0 `heartbeat-tick` (déjà câblé sur `.mcp_servers/*`).

## 5. Env vars (Windows User scope, jamais en .md/.json/.git)

| Nom | Description | Défaut | Requis |
|---|---|---|---|
| `SUPABASE_ACCESS_TOKEN` | PAT généré dans Dashboard self-hosted | — | **oui** |
| `MCP_SCOPE` | `read` (refuse exec_sql + apply_migration) ou `readwrite` | `read` | non |
| `MCP_RATE_LIMIT_PER_MIN` | Capacity du token bucket | `60` | non |
| `SUPABASE_DB_URL` | DSN Postgres direct (utilisé par `pg.Pool`) | `postgresql://postgres:<pwd>@148.230.92.235:5432/postgres` | non (défaut OK) |
| `MCP_PORT` | Bind port | `8080` | non |
| `MCP_HOST` | Bind address | `127.0.0.1` | non |
| `PULSE_LOG_PATH` | Chemin du fichier de log | `C:\Users\amado\.mcp_servers\supabase-aspace-v0.1\pulse.log` | non |
| `LOG_LEVEL` | pino level | `info` | non |

> **Doctrine "Test Key Pragma"** : aucune de ces valeurs dans `.md`/`.json`/`.ps1` committé. Le `.env.example` est VIDE.

## 6. Wire-up `.mcp.json` (snippet pour A0, manuel post-ratification)

```json
{
  "mcpServers": {
    "supabase-aspace-omk": {
      "type": "http",
      "url": "http://127.0.0.1:8080/mcp",
      "headers": {
        "Authorization": "Bearer ${SUPABASE_ACCESS_TOKEN}"
      }
    }
  }
}
```

> Le nom du serveur MCP est `supabase-aspace-omk` (pas `supabase-aspace` qui est l'A'Space-OS-wide) pour éviter la collision.

## 7. Plan d'implémentation (future session de dev A3)

### Phase 1 — Scaffold (1h)
- [ ] `mkdir C:/Users/amado/.mcp_servers/supabase-aspace-v0.1/`
- [ ] `npm init -y`
- [ ] Install deps §3
- [ ] `tsconfig.json` strict mode
- [ ] `.env.example` VIDE + `.gitignore` (pulse.log, node_modules, dist, .env)
- [ ] `src/index.ts` boilerplate (HTTP server, port 8080, bind 127.0.0.1)
- [ ] `npm run typecheck` → 0 erreurs

### Phase 2 — Auth + Scope gate (1h)
- [ ] `src/config/env.ts` — zod parse env vars, fail-fast si manquant
- [ ] `src/auth/pat-validator.ts` — `GET api.supabase.com/v1/profile` au boot, refuse si 401
- [ ] `src/scope/whitelist.ts` + `blocklist.ts` + `gate.ts` — parse SQL, ALLOW/DENY
- [ ] Test : `exec_sql({query: "SELECT * FROM auth.users"})` → 403 BLOCKED_SYSTEM_SCHEMA

### Phase 3 — Tools (2h)
- [ ] `src/tools/list-objects.ts` — `information_schema.tables` filter par schema + type
- [ ] `src/tools/get-object-details.ts` — `information_schema.columns` + `pg_indexes` + `pg_policies` + `pg_class.relrowsecurity`
- [ ] `src/tools/exec-sql.ts` — `pg.Pool.query(query)`, retourne `{rows, rowCount, durationMs, auditTag}`
- [ ] `src/tools/generate-types.ts` — `child_process.execFile('npx', ['supabase', 'gen', 'types', 'typescript', '--linked', '--schema', schema])` puis lire stdout
- [ ] `src/tools/apply-migration.ts` — `fs.readFileSync(path)` → parse `aspace-migration-id` header → check `_aspace_migrations` table → exec in tx → INSERT
- [ ] Test : 5 calls manuels sur Supabase OMK self-hosted (3 read + 2 RW si MCP_SCOPE=readwrite)

### Phase 4 — Rate limit + Audit + Origin check (1h)
- [ ] `src/safety/rate-limit.ts` — token bucket sliding window 60s, par hash(PAT)
- [ ] `src/audit/logger.ts` — pino, JSONL append à `PULSE_LOG_PATH`
- [ ] `src/safety/origin-check.ts` — middleware Express-like, refuse si Origin != localhost:*
- [ ] Test : 61 calls en 1 min → 61e retourne 429 RATE_LIMITED ; `tail -f pulse.log` montre les 60 premières + 1 RATE_LIMITED

### Phase 5 — Validation end-to-end (1h)
- [ ] Lancer le MCP (`npm run start` en background)
- [ ] Wire-up `.mcp.json` (HITL A0)
- [ ] 5 smoke tests parallèles : `list_objects`, `get_object_details`, `generate_types`, `exec_sql(SELECT now)`, `apply_migration(une migration idempotente)`
- [ ] Vérifier `pulse.log` à chaque appel
- [ ] Vérifier qu'aucun `query` n'est loggé (juste `schema` + `row_count` + `duration_ms`)
- [ ] Vérifier qu'aucun `auth.*`/`storage.*` n'est accessible

### Total estimé : ~6h de dev A3 (1 journée 12WY)

## 8. Hors-scope (à future ADR ou amendement)

- Streaming des résultats longs (au-delà de 10k rows) — `exec_sql` retournera une erreur explicite invitant à `LIMIT` / `COPY TO STDOUT`.
- RLS authoring wizard — pattern OMK documenté dans le wiki, pas dans le MCP.
- `service_role` key management — volontairement exclue (per ADR-SUPABASE-001 D4).
- Auto-bootstrap d'un projet complet — sub-skill `supabase-schema-onboard` à créer.
- OAuth 2.1 à la place de PAT — v1.0 (per ADR-OMK-003 follow-ups).
- Multi-project support — v1.0 (per ADR-OMK-003 follow-ups).

## 9. Anti-patterns interdits (rappel doctrine)

Voir ADR-OMK-003 §"Anti-patterns interdits" pour la liste complète. Résumé :
- Pas de secret en clair dans le code, le `.env.example`, le `package.json`, ou les logs.
- Pas de `console.log` (utiliser `pino`).
- Pas de `any` dans le code TS.
- Pas de bind sur `0.0.0.0` (toujours `127.0.0.1`).
- Pas de bypass du scope gate (même en debug).
- Pas de logging du query body (PII + log bloat).

## 10. Next action for A0 (post-ratification ADR-OMK-003)

1. **A0** : ratifier ADR-OMK-003 (si pas déjà fait).
2. **A0** : créer le PAT dans Dashboard self-hosted (`Step 1` ADR-OMK-003).
3. **A0** : set env vars User scope (`Step 2`).
4. **A3 (future session)** : implémenter le code MCP selon §7 ci-dessus (~6h).
5. **A0** : smoke test 5 calls (`Step 5` ADR-OMK-003).
6. **A0** : wire-up `.mcp.json` (`Step 4`).
7. **A3** : démarrer Phase B du dashboard OMK (DDL + RLS + types) en utilisant ce MCP.
