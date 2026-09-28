-- A'Space Supabase hardening + FK coverage
-- Live database was corrected first via execute_sql and verified with Supabase advisors.
-- This migration records the canonical change for future environments/replays.

alter function aspace.touch_updated_at() set search_path = aspace, pg_catalog;
alter function aspace.enforce_work_transition() set search_path = aspace, pg_catalog;
alter function aspace.log_intent_transition() set search_path = aspace, pg_catalog;
alter function aspace.forbid_intent_delete() set search_path = aspace, pg_catalog;
alter function aspace.touch_intent_updated_at() set search_path = aspace, pg_catalog;
alter function public.audit_memberships_changes() set search_path = public, auth, pg_catalog;

alter table aspace.capture_event force row level security;
alter table aspace.intent force row level security;
alter table aspace.intent_source force row level security;
alter table aspace.intent_link force row level security;
alter table aspace.intent_transition force row level security;
alter table aspace.capture_cursor force row level security;

create index if not exists dlq_last_evidence_idx on aspace.dlq(last_evidence_id);
create index if not exists dlq_session_binding_idx on aspace.dlq(session_binding_id);
create index if not exists dlq_work_idx on aspace.dlq(work_id);
create index if not exists event_session_binding_idx on aspace.event(session_binding_id);
create index if not exists evidence_session_binding_idx on aspace.evidence(session_binding_id);
create index if not exists intent_canonical_capture_idx on aspace.intent(canonical_capture_id);
create index if not exists intent_parent_idx on aspace.intent(parent_intent_id);
create index if not exists intent_source_capture_idx on aspace.intent_source(capture_event_id);
create index if not exists sync_run_world_idx on aspace.sync_run(world_id);
create index if not exists work_parent_idx on aspace.work(parent_id);
create index if not exists work_tape_idx on aspace.work(tape_id);
create index if not exists work_dependency_depends_idx on aspace.work_dependency(depends_on_id);
create index if not exists world_asset_sync_run_idx on aspace.world_asset(sync_run_id);
create index if not exists world_entity_source_asset_idx on aspace.world_entity(source_asset_id);
create index if not exists world_entity_sync_run_idx on aspace.world_entity(sync_run_id);
