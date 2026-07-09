// ============================================================================
// Domain types — manually defined; supabase gen types may overwrite later.
// Mirror of the SQL schemas (app, crm, identity, ops).
// ============================================================================

export type CasePriority = 'genealogie' | 'b2b' | 'expulsion' | 'other';
export type CaseStatus = 'new' | 'tracking' | 'ready' | 'filed' | 'hearing' | 'won' | 'lost' | 'archived';
export type TxType = 'inflow' | 'outflow';
export type TxStatus = 'pending' | 'completed' | 'failed' | 'reversed';
export type ClientModule = 'cession' | 'buyout' | 'audit_only';
export type SalesStage = 'audit' | 'sent' | 'opened' | 'signed' | 'lost';
export type CourtStage = 'ready' | 'filed' | 'hearing' | 'signed' | 'closed';
export type UserRole = 'admin' | 'operator' | 'agent' | 'viewer' | 'client';
export type ClearanceLevel =
  | 'level_0_public'
  | 'level_1_internal'
  | 'level_3_restricted'
  | 'level_5_sovereign';
export type AgentKind = 'synthetic' | 'human' | 'webhook' | 'cron';
export type EventSeverity = 'debug' | 'info' | 'warning' | 'critical';

export interface Profile {
  user_id: string;
  org_id: string;
  display_name: string;
  email: string;
  role: UserRole;
  clearance: ClearanceLevel;
  avatar_url: string | null;
  preferences: Record<string, unknown>;
  last_seen_at: string | null;
  created_at: string;
  updated_at: string;
}

export interface Case {
  id: string;
  org_id: string;
  case_number: string;
  defendant: string;
  client_id: string | null;
  amount: number;
  priority: CasePriority;
  status: CaseStatus;
  confidence_score: number;
  court_jurisdiction: string | null;
  sourced_from: string | null;
  assigned_to: string | null;
  clearance_required: ClearanceLevel;
  metadata: Record<string, unknown>;
  version: number;
  created_at: string;
  updated_at: string;
  deleted_at: string | null;
}

export interface Client {
  id: string;
  org_id: string;
  name: string;
  module: ClientModule;
  contact_email: string | null;
  contact_phone: string | null;
  notes: string | null;
  status: string | null;
  clearance_required: ClearanceLevel;
  metadata: Record<string, unknown>;
  created_at: string;
  updated_at: string;
  deleted_at: string | null;
}

export interface Transaction {
  id: string;
  org_id: string;
  case_id: string;
  tx_type: TxType;
  amount: number;
  tx_date: string;
  status: TxStatus;
  description: string | null;
  external_ref: string | null;
  created_by: string | null;
  created_at: string;
  updated_at: string;
  deleted_at: string | null;
}

export interface LedgerViewRow {
  id: string;
  date: string;
  case_id_label: string;
  case_id: string;
  type: TxType;
  amount: number;
  status: TxStatus;
  desc: string | null;
  org_id: string;
  created_at: string;
}

export interface SalesPipelineItem {
  id: string;
  org_id: string;
  case_id: string;
  stage: SalesStage;
  envelope_id: string | null;
  views_count: number;
  last_event_at: string | null;
  metadata: Record<string, unknown>;
  created_at: string;
  updated_at: string;
}

export interface SalesKanbanRow extends SalesPipelineItem {
  cases: string;
  name: string;
}

export interface CourtFiling {
  id: string;
  org_id: string;
  case_id: string;
  stage: CourtStage;
  filed_at: string | null;
  hearing_at: string | null;
  filed_amount: number | null;
  delay_days: number | null;
  metadata: Record<string, unknown>;
  created_at: string;
  updated_at: string;
}

export interface CourtKanbanRow extends CourtFiling {
  cases: string;
  name: string;
  amount: number | null;
}

export interface KnowledgeDoc {
  id: string;
  org_id: string;
  category: string;
  title: string;
  body_md: string;
  tags: string[];
  clearance_required: ClearanceLevel;
  author_id: string | null;
  version: number;
  created_at: string;
  updated_at: string;
  deleted_at: string | null;
}

export interface IntakeSubmission {
  id: string;
  org_id: string;
  source: string;
  payload: Record<string, unknown>;
  defender_email: string | null;
  defender_phone: string | null;
  routed_case_id: string | null;
  status: string;
  processed_by: string | null;
  created_at: string;
  processed_at: string | null;
}

export interface WindDirectionAlert {
  id: string;
  org_id: string;
  severity: EventSeverity;
  title: string;
  description: string | null;
  case_id: string | null;
  action_url: string | null;
  acknowledged_at: string | null;
  acknowledged_by: string | null;
  created_at: string;
}

export interface AgentRow {
  id: string;
  org_id: string;
  slug: string;
  display_name: string;
  kind: AgentKind;
  description: string | null;
  endpoint: string | null;
  is_active: boolean;
  metadata: Record<string, unknown>;
  created_at: string;
  updated_at: string;
}

export interface DashboardKpis {
  treasury_mtd: number;
  pipeline_value: number;
  conversion_rate: number;
  avg_delay_weeks: number;
}

export interface PipelineWeeklyPoint {
  week_label: string;
  value: number;
}
