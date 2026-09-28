-- RECORD OF LIVE DEPLOYMENT: already applied; do not reapply blindly.
-- Public RPC wrapper for the private A'Space intent capture function.
-- Only service_role may execute it; anon/authenticated are explicitly denied.

create or replace function public.aspace_capture_ipbd(
  p_kind text,
  p_verbatim text,
  p_source_type text,
  p_dedupe_key text,
  p_source_ref text default null,
  p_source_event_id text default null,
  p_actor text default null,
  p_raw_payload jsonb default '{}'::jsonb,
  p_core text default null,
  p_owner_role text default null,
  p_framework_map jsonb default '{}'::jsonb,
  p_metadata jsonb default '{}'::jsonb
)
returns uuid
language sql
security invoker
set search_path = public, aspace
as $$
  select aspace.capture_ipbd(
    p_kind, p_verbatim, p_source_type, p_dedupe_key,
    p_source_ref, p_source_event_id, p_actor, p_raw_payload,
    p_core, p_owner_role, p_framework_map, p_metadata
  );
$$;

revoke all on function public.aspace_capture_ipbd(
  text,text,text,text,text,text,text,jsonb,text,text,jsonb,jsonb
) from public, anon, authenticated;

grant execute on function public.aspace_capture_ipbd(
  text,text,text,text,text,text,text,jsonb,text,text,jsonb,jsonb
) to service_role;
