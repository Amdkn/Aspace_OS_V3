// ============================================================================
// Edge Function: intake-handler
// Receives Bana landing IntakeForm submissions, validates, inserts, forwards
// ============================================================================
import { serve } from "https://deno.land/std@0.208.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.45.0";

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers":
    "authorization, x-client-info, apikey, content-type",
};

interface IntakePayload {
  full_name?: string;
  email?: string;
  phone?: string;
  case_number?: string;
  estimated_amount?: number;
  notes?: string;
  source?: string;
  [key: string]: unknown;
}

function validate(p: IntakePayload): string | null {
  if (!p.email && !p.phone) return "email or phone required";
  if (p.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(p.email)) {
    return "invalid email";
  }
  return null;
}

serve(async (req) => {
  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: corsHeaders });
  }
  if (req.method !== "POST") {
    return new Response("Method not allowed", {
      status: 405,
      headers: corsHeaders,
    });
  }

  let payload: IntakePayload;
  try {
    payload = await req.json();
  } catch {
    return new Response(
      JSON.stringify({ ok: false, error: "invalid JSON" }),
      { status: 400, headers: { ...corsHeaders, "Content-Type": "application/json" } },
    );
  }

  const validationErr = validate(payload);
  if (validationErr) {
    return new Response(
      JSON.stringify({ ok: false, error: validationErr }),
      { status: 422, headers: { ...corsHeaders, "Content-Type": "application/json" } },
    );
  }

  const supabase = createClient(
    Deno.env.get("SUPABASE_URL")!,
    Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!,
    { auth: { persistSession: false } },
  );

  const { data, error } = await supabase
    .schema("app")
    .from("intake_submissions")
    .insert({
      source: payload.source ?? "bana_intake",
      payload,
      defender_email: payload.email ?? null,
      defender_phone: payload.phone ?? null,
    })
    .select("id")
    .single();

  if (error) {
    console.error("[intake-handler] insert error", error);
    return new Response(
      JSON.stringify({ ok: false, error: "DB error" }),
      { status: 500, headers: { ...corsHeaders, "Content-Type": "application/json" } },
    );
  }

  // Optional outbound webhook to n8n
  const n8n = Deno.env.get("N8N_WEBHOOK_URL");
  if (n8n) {
    fetch(n8n, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        source: "BANA_INTAKE_EDGE_FN",
        submission_id: data.id,
        timestamp: new Date().toISOString(),
        payload,
      }),
    }).catch((e) => console.error("n8n forward failed", e));
  }

  // Wind direction alert (info severity)
  await supabase.schema("ops").from("wind_direction_alerts").insert({
    severity: "info",
    title: "Nouvelle demande d'audit Bana",
    description: payload.full_name
      ? `Reçue de ${payload.full_name}`
      : "Voir intake submission",
  });

  return new Response(
    JSON.stringify({
      ok: true,
      submission_id: data.id,
      message: "Audit Request Secured",
    }),
    { status: 200, headers: { ...corsHeaders, "Content-Type": "application/json" } },
  );
});
