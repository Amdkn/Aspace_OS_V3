---
id: MCP-SUPABASE-ASPACE-SPEC
title: supabase-aspace MCP Server — Read/Write counterpart to supabase-solaris
status: ACCEPTED
date: 2026-06-10
ratified_by: A0 Amadeus (2026-06-10 PM, "GO pour 3. Ratification supabase-aspace MCP (6 next-actions)")
deciders: [A0 Amadeus]
proposed_by: Claude Code (A2) — session "spec + scaffold supabase-aspace"
domain: L0 Tech_OS / Data Plane / Self-Hosted Supabase
related:
  - ADR-SUPABASE-001 (parent: dual MCP doctrine)
  - ADR-ABCOS-001 (first consumer: abc_os schema)
  - 10_Tech_OS/11_Infra_13th_Doctor/06_MCP_Mastery/05_supabase/AGENTS.md (W1-W5 contract)
  - 10_Tech_OS/11_Infra_13th_Doctor/06_MCP_Mastery/06_supabase-aspace/ (target leaf DOX)
tags: [#spec #mcp #supabase #aspace #postgres #schema #migrations #hitl]
---

# supabase-aspace — MCP Server Spec (Read+Write counterpart to supabase-solaris)

> **Ancre canon** : `ADR-SUPABASE-001` (D2, D3, D4, D7).
> **Contrat opérationnel** : `10_Tech_OS/.../05_supabase/AGENTS.md` (W1-W5).
> **Lecteur parent** : `/aspace-supabase-mastery` skill (doctrines gotchas DOCKER-USER + USAGE-vs-DEFAULT-PRIVILEGES).

## 1. Pourquoi ce MCP

`supabase-solaris` (existant) est **read-only** : il pilote `postgres-mcp` (`crystaldba`) via SSH `aspace-vps`, avec le rôle PG `aspace_observer` (SELECT-only). C'est l'outil d'**observation et de diagnostic**.

`supabase-aspace` (à créer) est son **complément read+write** : il pilote directement Postgres (pas PostgREST) avec le rôle `aspace_admin`, et offre les opérations de **schéma, migration et DDL scoped** qu'exige le bootstrap d'un nouveau projet (per `ADR-SUPABASE-001` D3).

**Doctrine "Test Key Pragma"** : deux MCPs distincts = deux tokens rotables indépendamment. Une fuite du token write n'expose pas la surface read, et inversement.

## 2. Position dans l'architecture

| Élément | Valeur | Source |
|---|---|---|
| **Transport** | HTTP (Streamable HTTP, MCP 2025 spec) | spec |
| **Stack** | TypeScript / Node 20+ / `@modelcontextprotocol/sdk@^1.0` | spec |
| **DB driver** | `pg` (node-postgres) | spec |
| **Endpoint DB** | `supabase.kalybana.com:5432` (defaut) via `PG_DSN` | env |
| **Rôle PG** | `aspace_admin` (NoSuperuser, scoped) | ADR-SUPABASE-001 D4 |
| **Mécanisme de lancement (VPS)** | SSH tunnel `aspace-vps` + `socat`/`pgwire-proxy` (HITL) | ADR-SUPABASE-001 D2 |
| **Schemas de référence (cible MVP)** | `abc_os` (P1.1, ADR-ABCOS-001), `life_os` (D6 ADR-SUPABASE-001), extensions futures | registry |

> **Note transport** : le SDK 0.6 (utilisé par `clickup_sovereign`) est stdio-only. Le SDK 1.x (1.29.0+) supporte `StreamableHTTPServerTransport`. Ce MCP exige SDK 1.x — l'upgradepath est isolé dans son propre `package.json`.

## 3. Authentification

### 3.1 Source du token
- **Personal Access Token (PAT)** Supabase, généré sur `supabase.kalybana.com` (dashboard → Account → Access Tokens).
- **PAS** la `service_role` JWT ni l'`anon` JWT (ils ne sont pas acceptés par le endpoint MCP de Supabase Cloud, et le `service_role` doit rester VPS-side per ADR-SUPABASE-001 D4).
- Le PAT n'est utilisé **que** pour ouvrir la connexion DB initiale ; le MCP rebascule immédiatement sur le rôle `aspace_admin` via `SET ROLE aspace_admin` après handshake.

### 3.2 Stockage
- **VPS** : `/srv/aspace/secrets/aspace_admin.pgpass` (chmod 600, owner amadeus).
- **Local Windows** : env var User `ASPACE_SUPABASE_ADMIN_DSN` (jamais en .md/.json/git — doctrine "Test Key Pragma").
- Format DSN : `postgresql://aspace_admin:<pwd>@supabase.kalybana.com:5432/postgres`.
- **Rotation** : trimestrielle ou post-incident. Voir `ROTATION.md` (à produire) quand le MCP passe en ACCEPTED.

### 3.3 PAT vs Anon — doctrine
Le fichier `.mcp.json` actuel contient la `anon` key de Supabase. Le **nouveau** serveur `supabase-aspace` ne réutilise **pas** cette anon key : il demande un PAT distinct. Cela évite le couplage accidentel (rotation anon = casserait aspace).

## 4. Outils exposés

### 4.1 Read-only (parity avec `supabase-solaris`)

| Outil | Description | Paramètres |
|---|---|---|
| `list_schemas` | Liste tous les schémas (sauf core Supabase) | `include_system?: bool` (défaut false) |
| `list_objects` | Liste tables/views/sequences d'un schéma | `schema: string`, `object_type?: 'table'\|'view'\|'sequence'\|'all'` |
| `get_object_details` | Détail d'un objet (colonnes, contraintes, indexes, RLS) | `schema: string`, `name: string` |
| `explain_query` | Plan d'exécution sans exécuter | `query: string`, `analyze?: bool` (défaut false), `hypothetical_indexes?: object[]` |
| `analyze_db_health` | Health checks globaux (vacuum, indexes, replication) | `health_type?: 'all'\|'vacuum'\|'index'\|'replication'\|...` |

### 4.2 Read+Write (scoped, HITL-gated)

| Outil | Description | HITL gate | Logged to audit |
|---|---|---|---|
| `execute_sql` | SQL arbitraire en RW | **Oui** (DROP/DELETE/DDL → confirmation A0) | toujours |
| `apply_migration` | Applique un fichier `.sql` depuis le disque (chemin validé) | **Oui** (toujours, sauf DDL innoffensif) | toujours |
| `create_project_schema` | Bootstrap d'un schéma projet (D3 ADR-SUPABASE-001) | **Oui** (une fois par `<proj>`) | toujours |
| `list_migrations` | Lit `<schema>._aspace_migrations` (état idempotence) | non | non |
| `get_audit_log` | Lit `<schema>._aspace_audit` (qui, quand, hash SQL) | non | non |

### 4.3 Délégués au futur (post-MVP, HITL complet)

- `generate_typescript_types({ schema })` — wrapper `supabase gen types typescript`. Code local, pas VPS.
- `rotate_anon_key` — op manuelle dashboard aujourd'hui.
- `grant_anon_to_schema` — per ADR-SUPABASE-001 D7, HITL au MVP.

## 5. Safety Model — explicite, vérifiable, gatable

### 5.1 DDL allow-list

L'outil `execute_sql` n'autorise **que** les opérations DDL suivantes par défaut. Toute autre DDL doit passer par `apply_migration` (HITL) ou être explicitement approuvée par A0.

| Catégorie | Opérations autorisées par défaut | Statut |
|---|---|---|
| **Schéma (création)** | `CREATE SCHEMA`, `COMMENT ON SCHEMA` | allow |
| **Table (création idempotente)** | `CREATE TABLE IF NOT EXISTS`, `CREATE TABLE` (HITL si existe) | allow + warn |
| **Index** | `CREATE INDEX`, `CREATE UNIQUE INDEX` | allow |
| **Policy RLS** | `CREATE POLICY`, `ALTER TABLE ... ENABLE ROW LEVEL SECURITY` | allow |
| **Default privileges** | `ALTER DEFAULT PRIVILEGES ... GRANT ...` | allow |
| **View (lecture)** | `CREATE OR REPLACE VIEW` (lecture seule) | allow |
| **Function (lecture)** | `CREATE OR REPLACE FUNCTION` (marké `STABLE`/`IMMUTABLE` uniquement) | HITL |
| **DROP/DELETE/TRUNCATE** | **Toujours HITL** | **GATE** |
| `ALTER TABLE ... DROP COLUMN` | **Toujours HITL** | **GATE** |
| `ALTER TABLE ... RENAME` | HITL (log uniquement) | **GATE** |
| Toute DDL sur `auth.*`, `storage.*`, `realtime.*`, `vault.*`, `pgsodium.*`, `extensions.*`, `graphql_public.*` | **BLOQUÉ CÔTÉ CODE** (REVOKE explicite per D4) | **BLOCK** |
| `GRANT ... TO service_role` | BLOQUÉ (per D4 — service_role reste VPS-side) | **BLOCK** |

### 5.2 Pattern de gate HITL (en code)

Le MCP **ne contourne pas** le gate. Il le signale à l'appelant et attend une confirmation explicite :

```typescript
// src/safety/gate.ts (pseudo-code)
type GateDecision = { proceed: false; reason: string; requires: 'A0' }
  | { proceed: true; requiresHITLConfirm: boolean; auditTag: string }

function evaluateGate(sql: string, mode: 'rw' | 'ddl-allow' | 'migration'): GateDecision {
  // 1) Bloqué d'office (system schemas)
  if (hitsSystemSchema(sql)) return { proceed: false, reason: 'system_schema', requires: 'A0' }
  // 2) DROP/DELETE/TRUNCATE -> toujours HITL
  if (/(DROP|DELETE FROM|TRUNCATE)/i.test(sql)) return { proceed: true, requiresHITLConfirm: true, auditTag: 'DESTRUCTIVE' }
  // 3) DDL allow-list
  if (isAllowListedDDL(sql)) return { proceed: true, requiresHITLConfirm: false, auditTag: 'DDL_ALLOW' }
  // 4) Tout le reste : HITL par défaut
  return { proceed: true, requiresHITLConfirm: true, auditTag: 'GENERIC' }
}
```

Le caller (Claude Code A2 ou l'agent A3) doit **re-convoquer** l'outil avec `confirm: true` + le `auditTag` retourné, après l'accord A0. Cette double convocation est volontaire — elle force le HITL dans le transcript de session (traceable).

### 5.3 Audit log

Chaque write tool crée **deux** entrées :

1. **Transcript de session** : log in-process (visible dans la console MCP).
2. **Table Postgres `<schema>._aspace_audit`** : persisté côté serveur.

```sql
CREATE TABLE <schema>._aspace_audit (
  id          bigserial PRIMARY KEY,
  tool        text NOT NULL,
  audit_tag   text NOT NULL,
  sql_hash    text NOT NULL,         -- SHA-256 du SQL, JAMAIS le SQL brut (peut contenir des secrets en DDL grants)
  actor       text NOT NULL,         -- 'aspace_admin' ou nom d'agent A2
  hitl_confirmed_by text,            -- 'A0' si confirmé, NULL sinon
  applied_at  timestamptz NOT NULL DEFAULT now()
);
```

> **Note sécurité audit** : on stocke le **hash** du SQL, pas le SQL brut, pour éviter qu'un DDL contenant accidentellement un mot de passe GRANT ne finisse dans une table audit lisible par `aspace_observer`. Le SQL brut reste dans le transcript de session (A0 peut le lire directement).

### 5.4 Migrations idempotentes

`apply_migration` exige que le fichier contienne un header :

```sql
-- aspace-migration-id: 2026_06_10_001_create_abc_os_patients
-- aspace-migration-checksum: sha256:<hex>
-- aspace-migration-target-schema: abc_os
```

Le MCP :
1. Lit le header, vérifie le checksum.
2. Lookup dans `<schema>._aspace_migrations` par `id`.
3. Si déjà appliqué : skip + log "ALREADY_APPLIED".
4. Sinon : wrap dans `BEGIN ... COMMIT`, applique, INSERT dans `_aspace_migrations`, INSERT dans `_aspace_audit`.

## 6. Configuration

### 6.1 Variables d'environnement (env User Windows)

| Nom | Description | Défaut | Requis |
|---|---|---|---|
| `ASPACE_SUPABASE_ADMIN_DSN` | DSN Postgres du rôle `aspace_admin` | — | **oui** |
| `ASPACE_SUPABASE_PAT` | Personal Access Token Supabase (bootstrap uniquement) | — | non (utilisé au premier set-up) |
| `ASPACE_MCP_PORT` | Port HTTP du MCP | `3100` | non |
| `ASPACE_MCP_HOST` | Bind address | `127.0.0.1` | non |
| `ASPACE_AUDIT_SCHEMA` | Schéma où log l'audit (séparé des projets) | `abc_os` | non |
| `ASPACE_LOG_LEVEL` | debug / info / warn / error | `info` | non |

> **Doctrine "Test Key Pragma"** : aucune de ces valeurs dans `.md`/`.json`/`.ps1` committé. Le scaffold fournit `.env.example` (vide) et lit `process.env.*` au runtime.

### 6.2 Endpoint défaut
- `supabase.kalybana.com:5432` (per `.mcp.json` existant + AGENTS.md du MCP Mastery).
- Fallback `148.230.92.235:5432` (IP VPS directe, utile si le sous-domaine est en panne).

## 7. Structure du serveur

```
C:/Users/amado/.mcp_servers/supabase-aspace/
├── package.json
├── tsconfig.json
├── .env.example
├── .gitignore
├── README.md
└── src/
    ├── index.ts                  # entry: HTTP transport, tool registration
    ├── db/
    │   ├── pool.ts               # node-postgres Pool, lazy connect
    │   ├── role-bootstrap.ts     # SET ROLE aspace_admin + REVOKE system
    │   └── migrations.ts         # read + parse + apply migration file
    ├── safety/
    │   ├── gate.ts               # evaluateGate() — see §5.2
    │   ├── allow-list.ts         # DDL regex allow-list
    │   └── system-schemas.ts     # block-list (auth, storage, ...)
    ├── tools/
    │   ├── read-only/
    │   │   ├── list-schemas.ts
    │   │   ├── list-objects.ts
    │   │   ├── get-object-details.ts
    │   │   ├── explain-query.ts
    │   │   └── analyze-db-health.ts
    │   ├── read-write/
    │   │   ├── execute-sql.ts
    │   │   ├── apply-migration.ts
    │   │   ├── create-project-schema.ts
    │   │   ├── list-migrations.ts
    │   │   └── get-audit-log.ts
    │   └── shared/
    │       ├── audit.ts          # write to _aspace_audit
    │       └── hitl.ts           # HITL double-convocation helper
    ├── server.ts                 # Server factory (StreamableHTTPServerTransport)
    └── logger.ts                 # pino, jamais console.log
```

## 8. Wire-up à Claude Code (HITL — `.mcp.json`)

**Pas fait dans cette spec.** L'ajout dans `.mcp.json` est un changement de config A0. Procédure canonique (à exécuter par A0 après validation) :

```json
{
  "mcpServers": {
    "supabase-aspace": {
      "type": "http",
      "url": "http://127.0.0.1:3100/mcp"
    }
  }
}
```

Pré-requis côté A0 :
1. Définir `ASPACE_SUPABASE_ADMIN_DSN` (PowerShell `[Environment]::SetEnvironmentVariable(...)`).
2. Confirmer que le rôle `aspace_admin` existe côté VPS (`\du aspace_admin` → NoSuperuser, has CREATEROLE or CREATE on DB).
3. Lancer le serveur `npm run start` (en arrière-plan, ou via Task Scheduler per Shadow L0).
4. Tester `mcp__supabase-aspace__list_schemas` → 7+ schémas visibles (`public`, `storage`, `graphql_public`, `solaris_*`, `omk_*`, `abc_os` après bootstrap).

## 9. Validation post-scaffold (livré par cette session)

- [x] Spec rédigée à `_SPECS/MCP/supabase-aspace-spec.md` (ce fichier).
- [x] Scaffold TypeScript créé à `C:/Users/amado/.mcp_servers/supabase-aspace/`.
- [x] `npm install` → 0 vulnérabilités critiques.
- [x] `npx tsc --noEmit` → **0 erreurs** (cible : scaffold compile, même si les impls sont des stubs propres).
- [ ] Connexion DB live → HITL A0 (non couvert par cette session).
- [ ] Bootstrap `abc_os` → HITL A0 (per ADR-ABCOS-001 D8#1).

## 10. Hors-scope (à future ADR)

- Streaming des résultats longs (au-delà de 10k lignes) — `execute_sql` retournera une erreur explicite invitant à `LIMIT` / `COPY TO STDOUT`.
- Row-level security authoring wizard — pattern OMK documenté dans le wiki, pas dans le MCP.
- Gestion des `service_role` keys (volontairement exclue, per D4).
- Auto-bootstrap d'un projet complet (P1.1 `abc_os`) — sub-skill `supabase-schema-onboard` à créer.

## 11. Anti-patterns interdits (rappel doctrine)

| Interdit | Raison | Source |
|---|---|---|
| Hardcoder un DSN / PAT / anon key | doctrine Test Key Pragma | global CLAUDE.md |
| Permettre `DROP` sans HITL | sécurité | ADR-SUPABASE-001 D4 |
| Permettre GRANT sur `auth.*`/`storage.*` | escalade rôle | ADR-SUPABASE-001 D4 |
| Logger le SQL brut dans `_aspace_audit` | fuite secrets GRANT | §5.3 |
| Court-circuiter `SET ROLE aspace_admin` | connexion en `postgres` superuser | ADR-SUPABASE-001 D4 |
| Bypass du gate HITL "double convocation" | pas de trace A0 | §5.2 |
| `console.log` en production | code-style TS common | global CLAUDE.md |
| `any` dans le code TS | code-style TS common | global CLAUDE.md |
| Écrire dans `public` pour ABC OS | viole ADR-SUPABASE-001 D1 | registry |

## 12. Next action for A0

Une fois la spec ratifiée et le scaffold vérifié (D1-D8 anti-paresse) :
1. **A0** : créer le rôle `aspace_admin` côté VPS (Hermes peut le faire, mais la spec dit "L0/Rick task" — décision A0).
2. **A0** : `setx ASPACE_SUPABASE_ADMIN_DSN "postgresql://aspace_admin:..."` (User scope).
3. **A0** : éditer `.mcp.json` pour ajouter le bloc `supabase-aspace` (HITL, trace dans transcript).
4. **A0** : valider via `mcp__supabase-aspace__list_schemas` que la connexion passe.
5. **A3 (futur)** : bootstrapper `abc_os` via `create_project_schema('abc_os')` — P1.1 ADR-ABCOS-001.

<done>
