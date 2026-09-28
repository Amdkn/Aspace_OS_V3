# Supabase security posture — A'Space private schema

The `aspace` schema is intentionally private. Tables have RLS enabled and client roles `anon` / `authenticated` have no table privileges. No permissive client policies are created merely to silence the `rls_enabled_no_policy` informational advisor.

Security rules:
- service-role / trusted backend paths perform machine-state writes;
- public capture is mediated by the authenticated/custom-token Edge Function and the restricted RPC;
- FORCE RLS is enabled on all `aspace` tables for defense in depth;
- function `search_path` is pinned;
- advisor INFO about “RLS enabled no policy” is therefore expected, not a request to expose rows.

Performance rules:
- foreign keys have covering indexes;
- “unused index” immediately after creation is not grounds for deletion; usage must be observed over a meaningful workload window.
