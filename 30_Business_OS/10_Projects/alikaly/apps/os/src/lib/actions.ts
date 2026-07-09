// ============================================================================
// Server Actions — Supabase-backed (replaces mock store)
// ============================================================================
'use server';

import { createSupabaseServerClient } from './supabase/server';
import type {
  Case,
  Client,
  LedgerViewRow,
  SalesKanbanRow,
  CourtKanbanRow,
  KnowledgeDoc,
  AgentRow,
  WindDirectionAlert,
  DashboardKpis,
  PipelineWeeklyPoint,
  SalesStage,
  CourtStage,
} from './supabase/types';

// ---------- DASHBOARD ----------

export async function getDashboardKpis(): Promise<DashboardKpis | null> {
  const supabase = await createSupabaseServerClient();
  const { data, error } = await supabase.schema('app').rpc('dashboard_kpis');
  if (error) {
    console.error('[getDashboardKpis]', error);
    return null;
  }
  return (data as DashboardKpis[])?.[0] ?? null;
}

export async function getPipelineWeekly(): Promise<PipelineWeeklyPoint[]> {
  const supabase = await createSupabaseServerClient();
  const { data, error } = await supabase
    .schema('app')
    .rpc('dashboard_pipeline_weekly');
  if (error) {
    console.error('[getPipelineWeekly]', error);
    return [];
  }
  return (data as PipelineWeeklyPoint[]) ?? [];
}

export async function getWindDirectionAlerts(
  limit = 5
): Promise<WindDirectionAlert[]> {
  const supabase = await createSupabaseServerClient();
  const { data, error } = await supabase
    .schema('ops')
    .from('wind_direction_alerts')
    .select('*')
    .is('acknowledged_at', null)
    .order('created_at', { ascending: false })
    .limit(limit);
  if (error) {
    console.error('[getWindDirectionAlerts]', error);
    return [];
  }
  return data as WindDirectionAlert[];
}

// ---------- DOCKET (cases) ----------

export async function getActiveCases(): Promise<Case[]> {
  const supabase = await createSupabaseServerClient();
  const { data, error } = await supabase
    .schema('app')
    .from('cases')
    .select('*')
    .is('deleted_at', null)
    .order('amount', { ascending: false })
    .limit(100);
  if (error) {
    console.error('[getActiveCases]', error);
    return [];
  }
  return data as Case[];
}

// ---------- CLIENTS ----------

export async function getClients(): Promise<Client[]> {
  const supabase = await createSupabaseServerClient();
  const { data, error } = await supabase
    .schema('app')
    .from('clients')
    .select('*')
    .is('deleted_at', null)
    .order('updated_at', { ascending: false });
  if (error) {
    console.error('[getClients]', error);
    return [];
  }
  return data as Client[];
}

// ---------- FINANCE (ledger) ----------

export async function getLedgerEntries(limit = 50): Promise<LedgerViewRow[]> {
  const supabase = await createSupabaseServerClient();
  const { data, error } = await supabase
    .schema('app')
    .from('ledger_view')
    .select('*')
    .order('date', { ascending: false })
    .limit(limit);
  if (error) {
    console.error('[getLedgerEntries]', error);
    return [];
  }
  return data as LedgerViewRow[];
}

// ---------- SALES SANCTUM kanban ----------

export async function getSalesKanban(): Promise<
  Record<SalesStage, SalesKanbanRow[]>
> {
  const supabase = await createSupabaseServerClient();
  const { data, error } = await supabase
    .schema('crm')
    .from('sales_kanban')
    .select('*');
  if (error) {
    console.error('[getSalesKanban]', error);
    return {
      audit: [],
      sent: [],
      opened: [],
      signed: [],
      lost: [],
    };
  }
  const rows = (data ?? []) as SalesKanbanRow[];
  return {
    audit: rows.filter((r) => r.stage === 'audit'),
    sent: rows.filter((r) => r.stage === 'sent'),
    opened: rows.filter((r) => r.stage === 'opened'),
    signed: rows.filter((r) => r.stage === 'signed'),
    lost: rows.filter((r) => r.stage === 'lost'),
  };
}

// ---------- LEGAL kanban ----------

export async function getCourtKanban(): Promise<
  Record<CourtStage, CourtKanbanRow[]>
> {
  const supabase = await createSupabaseServerClient();
  const { data, error } = await supabase
    .schema('crm')
    .from('court_kanban')
    .select('*');
  if (error) {
    console.error('[getCourtKanban]', error);
    return {
      ready: [],
      filed: [],
      hearing: [],
      signed: [],
      closed: [],
    };
  }
  const rows = (data ?? []) as CourtKanbanRow[];
  return {
    ready: rows.filter((r) => r.stage === 'ready'),
    filed: rows.filter((r) => r.stage === 'filed'),
    hearing: rows.filter((r) => r.stage === 'hearing'),
    signed: rows.filter((r) => r.stage === 'signed'),
    closed: rows.filter((r) => r.stage === 'closed'),
  };
}

// ---------- KNOWLEDGE ----------

export async function getKnowledgeDocs(category?: string): Promise<KnowledgeDoc[]> {
  const supabase = await createSupabaseServerClient();
  let q = supabase
    .schema('app')
    .from('knowledge_docs')
    .select('*')
    .is('deleted_at', null)
    .order('updated_at', { ascending: false });
  if (category) q = q.eq('category', category);
  const { data, error } = await q;
  if (error) {
    console.error('[getKnowledgeDocs]', error);
    return [];
  }
  return data as KnowledgeDoc[];
}

// ---------- PEOPLE (agents) ----------

export async function getAgentRoster(): Promise<AgentRow[]> {
  const supabase = await createSupabaseServerClient();
  const { data, error } = await supabase
    .schema('ops')
    .from('agents')
    .select('*')
    .eq('is_active', true)
    .order('display_name');
  if (error) {
    console.error('[getAgentRoster]', error);
    return [];
  }
  return data as AgentRow[];
}

// ---------- BANA INTAKE (anon-friendly) ----------

export async function submitIntake(formData: FormData): Promise<{
  success: boolean;
  message: string;
  id?: string;
}> {
  const supabase = await createSupabaseServerClient();
  const data = Object.fromEntries(formData.entries());

  const { data: inserted, error } = await supabase
    .schema('app')
    .from('intake_submissions')
    .insert({
      source: 'bana_intake',
      payload: data,
      defender_email: (data.email as string) || null,
      defender_phone: (data.phone as string) || null,
    })
    .select('id')
    .single();

  if (error) {
    console.error('[submitIntake]', error);
    return { success: false, message: error.message };
  }

  // Optional outbound webhook (kept from original behavior)
  const webhookUrl = process.env.N8N_WEBHOOK_URL;
  if (webhookUrl) {
    try {
      await fetch(webhookUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          source: 'BANA_INTAKE_ACTION',
          submission_id: inserted?.id,
          timestamp: new Date().toISOString(),
          payload: data,
        }),
      });
    } catch (e) {
      console.error('[submitIntake] webhook failed', e);
    }
  }

  return {
    success: true,
    message: 'Audit Request Secured',
    id: inserted?.id,
  };
}

// ---------- AUTH HELPERS ----------

export async function getCurrentProfile() {
  const supabase = await createSupabaseServerClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return null;
  const { data, error } = await supabase
    .schema('identity')
    .from('profiles')
    .select('*')
    .eq('user_id', user.id)
    .maybeSingle();
  if (error) {
    console.error('[getCurrentProfile]', error);
    return null;
  }
  return data;
}
