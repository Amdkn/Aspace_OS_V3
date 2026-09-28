import "jsr:@supabase/functions-js/edge-runtime.d.ts";

const EXPECTED_TOKEN_SHA256 = "99fc7b85cdbe3d60db6763822fd1e356b5b4b7fa9605f9044527fad433d7f2ff";

function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "content-type": "application/json; charset=utf-8" },
  });
}

async function sha256Hex(value: string): Promise<string> {
  const bytes = new TextEncoder().encode(value);
  const digest = await crypto.subtle.digest("SHA-256", bytes);
  return Array.from(new Uint8Array(digest))
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
}

Deno.serve(async (req: Request) => {
  if (req.method !== "POST") return json({ error: "method_not_allowed" }, 405);

  const token = req.headers.get("x-aspace-capture-token") ?? "";
  if (!token || (await sha256Hex(token)) !== EXPECTED_TOKEN_SHA256) {
    return json({ error: "unauthorized" }, 401);
  }

  let body: Record<string, unknown>;
  try {
    body = await req.json();
  } catch {
    return json({ error: "invalid_json" }, 400);
  }

  const required = ["kind", "verbatim", "source_type", "dedupe_key"];
  for (const key of required) {
    if (typeof body[key] !== "string" || !(body[key] as string).trim()) {
      return json({ error: "missing_required_field", field: key }, 400);
    }
  }

  const supabaseUrl = Deno.env.get("SUPABASE_URL");
  const serviceRoleKey = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY");
  if (!supabaseUrl || !serviceRoleKey) {
    return json({ error: "server_configuration_missing" }, 500);
  }

  const payload = {
    p_kind: body.kind,
    p_verbatim: body.verbatim,
    p_source_type: body.source_type,
    p_dedupe_key: body.dedupe_key,
    p_source_ref: body.source_ref ?? null,
    p_source_event_id: body.source_event_id ?? null,
    p_actor: body.actor ?? null,
    p_raw_payload: body.raw_payload ?? {},
    p_core: body.core ?? null,
    p_owner_role: body.owner_role ?? null,
    p_framework_map: body.framework_map ?? {},
    p_metadata: body.metadata ?? {},
  };

  const rpc = await fetch(supabaseUrl + "/rest/v1/rpc/aspace_capture_ipbd", {
    method: "POST",
    headers: {
      apikey: serviceRoleKey,
      authorization: "Bearer " + serviceRoleKey,
      "content-type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  const responseText = await rpc.text();
  if (!rpc.ok) {
    return json({ error: "capture_rpc_failed", status: rpc.status, detail: responseText }, 502);
  }

  let intentId: unknown = responseText;
  try { intentId = JSON.parse(responseText); } catch { }

  return json({ ok: true, intent_id: intentId }, 201);
});
