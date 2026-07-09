// ============================================================================
// Edge Function: audit-rotate
// Weekly archive of audit.log entries > 90 days to Storage, then delete chaud
// ============================================================================
import { serve } from "https://deno.land/std@0.208.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.45.0";

serve(async (_req) => {
  const supabase = createClient(
    Deno.env.get("SUPABASE_URL")!,
    Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!,
    { auth: { persistSession: false } },
  );

  const cutoff = new Date();
  cutoff.setDate(cutoff.getDate() - 90);
  const cutoffIso = cutoff.toISOString();

  const { data: rows, error } = await supabase
    .schema("audit")
    .from("log")
    .select("*")
    .lt("occurred_at", cutoffIso)
    .limit(50_000);

  if (error) {
    return new Response(JSON.stringify({ ok: false, error: error.message }), { status: 500 });
  }

  if (!rows || rows.length === 0) {
    return new Response(JSON.stringify({ ok: true, archived: 0 }), { status: 200 });
  }

  const monthKey = cutoffIso.slice(0, 7); // YYYY-MM
  const filename = `audit-archive/${monthKey}.jsonl`;
  const body = rows.map((r) => JSON.stringify(r)).join("\n");

  const { error: upErr } = await supabase.storage
    .from("marketing-public") // reuse public bucket OR create dedicated 'audit-archive'
    .upload(filename, new Blob([body], { type: "application/x-ndjson" }), {
      upsert: true,
    });

  if (upErr) {
    return new Response(JSON.stringify({ ok: false, error: upErr.message }), { status: 500 });
  }

  // Delete archived rows
  const idsToDelete = rows.map((r) => r.id);
  const { error: delErr } = await supabase
    .schema("audit")
    .from("log")
    .delete()
    .in("id", idsToDelete);

  if (delErr) {
    return new Response(JSON.stringify({ ok: false, error: delErr.message }), { status: 500 });
  }

  return new Response(
    JSON.stringify({ ok: true, archived: rows.length, archive_file: filename }),
    { status: 200, headers: { "Content-Type": "application/json" } },
  );
});
