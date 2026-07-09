// ============================================================================
// Edge Function: case-confidence-recalc
// Scheduled (daily) — recompute confidence_score per case based on signals
// ============================================================================
import { serve } from "https://deno.land/std@0.208.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.45.0";

interface CaseRow {
  id: string;
  status: string;
  amount: number;
  created_at: string;
}

function computeScore(row: CaseRow, hasSalesItem: boolean, salesStage: string | null): number {
  let score = 0;

  // Amount tier
  if (row.amount >= 50000) score += 2;
  else if (row.amount >= 10000) score += 1;

  // Status progression
  if (["ready", "filed"].includes(row.status)) score += 1;
  if (["hearing", "won"].includes(row.status)) score += 2;

  // Sales pipeline signal
  if (hasSalesItem) {
    if (salesStage === "signed") score += 2;
    else if (salesStage === "opened") score += 1;
  }

  return Math.min(5, score);
}

serve(async (_req) => {
  const supabase = createClient(
    Deno.env.get("SUPABASE_URL")!,
    Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!,
    { auth: { persistSession: false } },
  );

  const { data: cases, error } = await supabase
    .schema("app")
    .from("cases")
    .select("id, status, amount, created_at")
    .is("deleted_at", null);

  if (error) {
    return new Response(JSON.stringify({ ok: false, error: error.message }), {
      status: 500,
    });
  }

  let updated = 0;
  for (const c of cases ?? []) {
    const { data: sales } = await supabase
      .schema("crm")
      .from("sales_pipeline_items")
      .select("stage")
      .eq("case_id", c.id)
      .maybeSingle();

    const newScore = computeScore(
      c as CaseRow,
      !!sales,
      sales?.stage ?? null,
    );

    const { error: upErr } = await supabase
      .schema("app")
      .from("cases")
      .update({ confidence_score: newScore })
      .eq("id", c.id);

    if (!upErr) updated += 1;
  }

  return new Response(
    JSON.stringify({ ok: true, updated_count: updated, total: cases?.length ?? 0 }),
    { status: 200, headers: { "Content-Type": "application/json" } },
  );
});
