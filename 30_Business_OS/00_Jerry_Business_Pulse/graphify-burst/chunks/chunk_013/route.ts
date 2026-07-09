// ============================================================================
// /api/intake — public POST endpoint for Bana landing form
// Proxies to Supabase Edge Function intake-handler, falls back to direct insert
// ============================================================================
import { NextResponse } from 'next/server';
import { createSupabaseAdminClient } from '@/lib/supabase/admin';

export async function POST(req: Request) {
  let payload: Record<string, unknown>;
  try {
    payload = await req.json();
  } catch {
    return NextResponse.json(
      { ok: false, error: 'invalid JSON' },
      { status: 400 }
    );
  }

  const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
  const anon = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;

  // Prefer Edge Function path (handles validation + outbound webhooks)
  if (url && anon) {
    try {
      const res = await fetch(`${url}/functions/v1/intake-handler`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          apikey: anon,
        },
        body: JSON.stringify(payload),
      });
      const body = await res.json();
      return NextResponse.json(body, { status: res.status });
    } catch {
      // fall through to direct insert
    }
  }

  // Direct insert fallback (requires service role)
  if (process.env.SUPABASE_SERVICE_ROLE_KEY) {
    try {
      const supabase = createSupabaseAdminClient();
      const { data, error } = await supabase
        .schema('app')
        .from('intake_submissions')
        .insert({
          source: 'bana_intake_api_fallback',
          payload,
          defender_email: (payload as { email?: string }).email ?? null,
          defender_phone: (payload as { phone?: string }).phone ?? null,
        })
        .select('id')
        .single();

      if (error) throw error;
      return NextResponse.json({
        ok: true,
        submission_id: data.id,
        source: 'fallback-direct',
      });
    } catch (err: unknown) {
      const message = err instanceof Error ? err.message : 'unknown';
      return NextResponse.json(
        { ok: false, error: message },
        { status: 500 }
      );
    }
  }

  return NextResponse.json(
    { ok: false, error: 'Supabase not configured' },
    { status: 503 }
  );
}
