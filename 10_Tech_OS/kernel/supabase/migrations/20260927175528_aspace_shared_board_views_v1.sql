-- Synced from Supabase project Agent OS Backend (20260927175528)
-- Migration: aspace_shared_board_views_v1
-- This file records the already-applied live migration; do not reapply blindly.

create or replace view aspace.v_work_board as
select
  w.id as cloud_work_id,
  w.core,
  w.layer,
  w.title,
  w.status as work_status,
  w.priority,
  w.external_refs->>'linear_issue' as linear_issue,
  nullif(w.external_refs->>'pr_number','')::integer as declared_pr_number,
  sb.role_name,
  sb.manager_role,
  sb.provider,
  sb.session_id,
  sb.status as session_status,
  sb.pr_number as session_pr_number,
  sb.branch,
  e.uri as latest_evidence_uri,
  e.payload->>'policy' as evidence_policy,
  w.updated_at
from aspace.work w
left join lateral (
  select s.*
  from aspace.session_binding s
  where s.work_id=w.id
  order by s.updated_at desc
  limit 1
) sb on true
left join lateral (
  select ev.*
  from aspace.evidence ev
  where ev.work_id=w.id
  order by ev.created_at desc, ev.id desc
  limit 1
) e on true;

create or replace view aspace.v_session_mesh as
select
  sb.provider,
  sb.session_id,
  sb.role_name,
  sb.manager_role,
  coalesce(w.core, sb.metadata->>'core') as core,
  w.external_refs->>'linear_issue' as linear_issue,
  sb.status as session_status,
  sb.repo,
  sb.branch,
  sb.pr_number,
  sb.metadata,
  sb.started_at,
  sb.updated_at,
  sb.ended_at
from aspace.session_binding sb
left join aspace.work w on w.id=sb.work_id;

grant select on aspace.v_work_board to service_role;
grant select on aspace.v_session_mesh to service_role;
