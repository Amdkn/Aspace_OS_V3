# aspace-intent-capture

Canonical source for the live Supabase Edge Function `aspace-intent-capture`.

- Supabase project: `biyecksylqonuovqmbtz` (Agent OS Backend)
- Live function status at reconciliation: ACTIVE, version 1
- `verify_jwt=false` is intentional for this version because the function performs its own `x-aspace-capture-token` authentication before privileged projection.
- The stored SHA-256 value is a digest, not the capture token itself. The token remains outside the repository.
- Remote projection calls `public.aspace_capture_ipbd`, which is executable only by `service_role`.
- Local clients must use `scripts/aspace_capture.py`; they never receive the service-role key.

Do not deploy edits blindly. Compare this source against the live function and verify the local-first capture path before promotion.
