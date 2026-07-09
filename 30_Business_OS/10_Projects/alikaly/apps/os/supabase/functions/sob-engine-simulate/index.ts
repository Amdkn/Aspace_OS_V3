// ============================================================================
// Edge Function: sob-engine-simulate
// Replaces /api/engine/status mock — aggregates live exposure + metrics
// ============================================================================
import { serve } from "https://deno.land/std@0.208.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.45.0";

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers":
    "authorization, x-client-info, apikey, content-type",
};

serve(async (req) => {
  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: corsHeaders });
  }

  const supabase = createClient(
    Deno.env.get("SUPABASE_URL")!,
    Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!,
    { auth: { persistSession: false } },
  );

  try {
    const { data: activeCases, error: casesErr } = await supabase
      .schema("app")
      .from("cases")
      .select("amount")
      .in("status", ["ready", "filed", "hearing"])
      .is("deleted_at", null);

    if (casesErr) throw casesErr;

    const exposure = (activeCases ?? []).reduce(
      (sum, c) => sum + Number(c.amount ?? 0),
      0,
    );

    const { data: yieldMetric } = await supabase
      .schema("ops")
      .from("system_metrics")
      .select("numeric_value")
      .eq("metric_key", "sob.ytd_yield")
      .order("recorded_at", { ascending: false })
      .limit(1)
      .maybeSingle();

    const body = {
      status: "ONLINE",
      latency: "24ms",
      node: "LX-990",
      engine_version: "V4.82",
      last_scan: new Date().toISOString(),
      global_exposure: exposure,
      ytd_yield: yieldMetric?.numeric_value
        ? `+${yieldMetric.numeric_value}%`
        : null,
      active_cases_count: activeCases?.length ?? 0,
    };

    return new Response(JSON.stringify(body), {
      status: 200,
      headers: { ...corsHeaders, "Content-Type": "application/json" },
    });
  } catch (err) {
    console.error("[sob-engine-simulate]", err);
    return new Response(
      JSON.stringify({ status: "ERROR", message: (err as Error).message }),
      {
        status: 500,
        headers: { ...corsHeaders, "Content-Type": "application/json" },
      },
    );
  }
});
