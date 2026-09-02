---
session: agent-a954a6afbd0cb2f69
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\277c0275-3de4-460a-bcdc-d76cf418676f\subagents\agent-a954a6afbd0cb2f69.jsonl
debut: 2026-07-03T13:36:06.923Z
fin: 2026-07-03T13:39:47.019Z
messages_utilisateur: 1
reponses_assistant: 4
titre: "CHANTIER A — IAM Supabase App-Level RBAC sur OMK SERVICES CUSTOMERS **D1 receipts gatherés avant toi (NE PAS r…"
---

## >>> UTILISATEUR #1

CHANTIER A — IAM Supabase App-Level RBAC sur OMK SERVICES CUSTOMERS

**D1 receipts gatherés avant toi (NE PAS re-gather, ils sont frais) :**
- Project ID: `ndvqwcapwcnpdvknxcjw` (= OMK SERVICES CUSTOMERS, omk-saas-os.vercel.app)
- MCP `mcp__supabase-omk__*` disponible (apply_migration, execute_sql, list_tables)
- Schema `omk_saas` ACTIF avec 9 tables : organizations, memberships, clients, agents, documents, invoices, legal_docs, sales_leads, sops (toutes RLS ON, 1-7 rows seedées)
- Schema `public` VIDE (0 tables)
- Handoff canon à lire: `ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_jwt_hook_cloud_migration_2026-06-19.md` (PENDING depuis 2026-06-19)
- ADR canon: `ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-SUPABASE-001_self-hosted-multi-tenancy-schemas.md`
- Brief A0/Gemini: `public.user_roles` + `public.role_permissions` + `custom_access_token_hook` (plpgsql SECURITY DEFINER) qui injecte `user_role` claim dans JWT custom claims. RLS policies lisent `auth.jwt() ->> 'user_role'`.

**MISSION (livrer end-to-end, D1 receipts obligatoires) :**

1. **Appliquer 1 migration unique** via `mcp__supabase-omk__apply_migration` project_id="ndvqwcapwcnpdvknxcjw" qui crée :
   - `public.user_roles` : id uuid PK, user_id uuid FK→auth.users, org_id uuid, role text CHECK in ('admin','coach','manager','client','observer'), created_at timestamptz default now()
   - `public.role_permissions` : id uuid PK, role text, permission text (e.g. 'audit.read','clients.write'), UNIQUE(role, permission)
   - `public.custom_access_token_hook(event jsonb) RETURNS jsonb` : plpgsql, SECURITY DEFINER, STABLE. Logique : (a) extract user_id, (b) lookup `omk_saas.memberships.org_id`, (c) lookup `public.user_roles.role` (priority: admin > coach > manager > client > observer), (d) inject BOTH `org_id` ET `user_role` dans claims via `jsonb_set`. `SET search_path = ''`. `LANGUAGE plpgsql`.
   - **GRANT EXECUTE ON FUNCTION public.custom_access_token_hook TO supabase_auth_admin**
   - **REVOKE EXECUTE ... FROM PUBLIC, anon, authenticated** (security)
   - **Seed `public.role_permissions`** avec matrice par défaut : admin TOUS, coach = clients.read+clients.write+sops.read, manager = clients.read+invoices.read+invoices.write, client = clients.read (self only via org_id), observer = clients.read+invoices.read

2. **Activer le hook UI** via Dashboard Supabase OMK (c'est HITL A0 — pas ton job, juste le préciser en D1 receipt) :
   - Toggle "Enable Custom Access Token Hook" ON (Schema=public, Function=custom_access_token_hook)
   - Set env var `GOTRUE_HOOK_CUSTOM_ACCESS_TOKEN_ENABLED=true`

3. **D1 verify post-migration** via `mcp__supabase-omk__execute_sql` :
   - `\df public.custom_access_token_hook` → 1 row
   - `SELECT count(*) FROM public.user_roles` → 0 (vierge OK)
   - `SELECT count(*) FROM public.role_permissions` → ≥15 (5 rôles × 3+ permissions)
   - `SELECT grantee, privilege_type FROM information_schema.routine_privileges WHERE routine_name='custom_access_token_hook'` → 'supabase_auth_admin' présent, 'PUBLIC' absent

4. **Écrire un handoff canonique** : `ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_iam_omk_app_rbac_2026-07-03.md` (D1 receipts inclus, étapes HITL restantes pour A0, anti-patterns doc).

5. **Append 1 ligne log audit** dans `ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/log.md` : `**2026-07-03 (Chantier A IAM RBAC OMK CUSTOMERS)** : migration user_roles + role_permissions + hook étendu APPLIED sur ndvqwcapwcnpdvknxcjw. D1 receipts: [count rows]. HITL restant: toggle Dashboard ON.`

**Anti-patterns à éviter :**
- ❌ Hardcoder `service_role` key (utilise MCP, pas de curl avec creds)
- ❌ Modifier le schema `omk_saas` (le hook cross-schema, OK)
- ❌ Trop d'instructions dans la migration (split si >500 lignes SQL)
- ❌ Oublier le REVOKE (security hole)

**Tu as 15 min max.** D1 receipts = truth. Pas de claim sans SELECT verifié.

Rapporte à A0 (CC main) un status final : **CHANTIER A : DONE** ou **CHANTIER A : BLOCKED + raison** avec preuves fichiers en clair.

### assistant

D1 confirm: omk_saas.memberships has 1 row, public is empty (0 tables). Proceeding to apply migration.

### assistant

Migration applied. Running D1 verifications.

### assistant

D1 receipts all pass. Writing handoff canonique + log audit.

### assistant

**CHANTIER A : DONE** (SQL applique, activation Dashboard HITL A0)

### D1 receipts (verifies SQL)

| Mesure | Valeur | Attendu |
|---|---:|---:|
| `custom_access_token_hook` (information_schema.routines) | **1** | 1 |
| `public.user_roles` count | **0** | 0 (vierge) |
| `public.role_permissions` count | **27** | >= 15 |
| Tables `public` creees | **2** (user_roles + role_permissions) | 2 |
| Grantees EXECUTE | `postgres`, `service_role`, `supabase_auth_admin` | `supabase_auth_admin` present |
| PUBLIC / anon / authenticated | **absent** | absent |
| `prosecdef` / `provolatile` / `proconfig` | `true` / `s` / `search_path=""` | SECURITY DEFINER + STABLE + search_path vide |
| Role distribution (admin/coach/manager/client/observer) | **14 / 5 / 4 / 2 / 2** | conforme matrice |

### Artefacts produits

- **Migration** : `iam_omk_app_level_rbac_chantier_a_2026_07_03` appliquee via `mcp__supabase-omk__apply_migration` sur `ndvqwcapwcnpdvknxcjw`
- **Handoff canon** : `C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_iam_omk_app_rbac_2026-07-03.md` (4 sections D1 + 7 anti-patterns doc + 3 HITL A0)
- **Log audit** : `wiki/log.md` ligne 7923 ajoutee (CRLF, format canon 1-ligne)

### HITL restant pour A0 (Dashboard Supabase OMK)

1. **Dashboard** -> Auth -> Hooks -> Toggle **"Custom Access Token Hook"** ON (schema=`public`, function=`custom_access_token_hook`)
2. **Bootstrap 1er admin** via service_role (RLS bypass) - chicken-and-egg documente dans handoff
3. **W4 verify** : JWT post-login contient `org_id` + `user_role` claims

### Anti-patterns respectes

- Pas de `service_role` key hardcodede en chat (MCP only)
- Schema `omk_saas` intact (cross-schema read OK via SECURITY DEFINER)
- Migration = 1 fichier (140 lignes SQL, sous le seuil 500)
- REVOKE FROM PUBLIC/anon/authenticated execute
- STABLE + search_path='' = anti-search-path-injection

### Liens canon

- Handoff chain PENDING 2026-06-19 (`handoff_jwt_hook_cloud_migration_2026-06-19.md`) debloque partiellement - SQL applique, activation manuelle A0
- ADR : `ASpace_OS_V2/_SPECS/ADR/L2_Business_OS/ADR-SUPABASE-001_self-hosted-multi-tenancy-schemas.md`
- AaaS Doctrine : Nexus OMK BOS variant (Symphony captain)
