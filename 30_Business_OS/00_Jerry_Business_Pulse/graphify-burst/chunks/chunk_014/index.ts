// ============================================================================
// Edge Function: docusign-webhook
// Receives DocuSign Connect callbacks and updates sales_pipeline_items.stage
// ============================================================================
import { serve } from "https://deno.land/std@0.208.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.45.0";

type DocuSignEvent =
  | "envelope-sent"
  | "envelope-delivered"
  | "envelope-opened"
  | "envelope-completed"
  | "envelope-declined"
  | "envelope-voided"
  | "recipient-completed";

interface DocuSignPayload {
  event: DocuSignEvent;
  data: {
    envelopeId: string;
    envelopeSummary?: { status: string };
    accountId?: string;
  };
}

const STAGE_MAP: Record<DocuSignEvent, string | null> = {
  "envelope-sent": "sent",
  "envelope-delivered": "sent",
  "envelope-opened": "opened",
  "envelope-completed": "signed",
  "recipient-completed": "signed",
  "envelope-declined": "lost",
  "envelope-voided": "lost",
};

async function verifyHmac(req: Request, rawBody: string): Promise<boolean> {
  const secret = Deno.env.get("DOCUSIGN_WEBHOOK_SECRET");
  if (!secret) return true; // soft mode if not configured (dev)

  const sigHeader = req.headers.get("x-docusign-signature-1");
  if (!sigHeader) return false;

  const enc = new TextEncoder();
  const key = await crypto.subtle.importKey(
    "raw",
    enc.encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"],
  );
  const sigBuf = await crypto.subtle.sign("HMAC", key, enc.encode(rawBody));
  const sigHex = Array.from(new Uint8Array(sigBuf))
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");

  return sigHeader.toLowerCase() === sigHex.toLowerCase();
}

serve(async (req) => {
  if (req.method !== "POST") {
    return new Response("Method not allowed", { status: 405 });
  }

  const rawBody = await req.text();

  const ok = await verifyHmac(req, rawBody);
  if (!ok) {
    return new Response("Invalid signature", { status: 401 });
  }

  let payload: DocuSignPayload;
  try {
    payload = JSON.parse(rawBody);
  } catch {
    return new Response("Bad JSON", { status: 400 });
  }

  const supabase = createClient(
    Deno.env.get("SUPABASE_URL")!,
    Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!,
    { auth: { persistSession: false } },
  );

  const newStage = STAGE_MAP[payload.event];
  if (!newStage) {
    // Log unknown event but don't fail
    await supabase
      .schema("ops")
      .from("agent_events")
      .insert({
        agent_id: null,
        severity: "info",
        event_type: `docusign.${payload.event}`,
        message: "Unhandled DocuSign event",
        payload,
      });
    return new Response("OK (unhandled)", { status: 200 });
  }

  const { data: item, error: findErr } = await supabase
    .schema("crm")
    .from("sales_pipeline_items")
    .update({
      stage: newStage,
      views_count: payload.event === "envelope-opened" ? undefined : undefined,
      last_event_at: new Date().toISOString(),
    })
    .eq("envelope_id", payload.data.envelopeId)
    .select("id, case_id")
    .maybeSingle();

  if (findErr) {
    console.error("[docusign-webhook] update error", findErr);
    return new Response("DB error", { status: 500 });
  }

  // Increment views_count on opened (separate query for atomic increment)
  if (payload.event === "envelope-opened" && item) {
    await supabase.rpc("increment_envelope_views", {
      p_case_id: item.case_id,
    }).then(() => {}, () => {});
  }

  // Audit + agent_events
  const { data: agent } = await supabase
    .schema("ops")
    .from("agents")
    .select("id")
    .eq("slug", "docusign-bot")
    .maybeSingle();

  await supabase.schema("ops").from("agent_events").insert({
    agent_id: agent?.id ?? null,
    case_id: item?.case_id ?? null,
    severity: payload.event === "envelope-declined" ? "warning" : "info",
    event_type: `docusign.${payload.event}`,
    message: `Envelope ${payload.data.envelopeId} -> stage=${newStage}`,
    payload,
  });

  return new Response(
    JSON.stringify({ ok: true, envelope: payload.data.envelopeId, new_stage: newStage }),
    { status: 200, headers: { "Content-Type": "application/json" } },
  );
});
