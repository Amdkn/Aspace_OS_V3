// ============================================================================
// /api/engine/status — proxies to Supabase Edge Function sob-engine-simulate.
// Falls back to a static payload if Supabase env is not configured.
// ============================================================================
import { NextResponse } from 'next/server';

const FALLBACK = {
  status: 'ONLINE',
  latency: '24ms',
  node: 'LX-990',
  engine_version: 'V4.82',
  last_scan: null as string | null,
  global_exposure: 248192004.0,
  ytd_yield: '+14.2%',
  active_cases_count: 0,
};

export async function GET() {
  const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
  const anon = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;

  if (!url || !anon) {
    return NextResponse.json({
      ...FALLBACK,
      last_scan: new Date().toISOString(),
      source: 'fallback-static',
    });
  }

  try {
    const res = await fetch(`${url}/functions/v1/sob-engine-simulate`, {
      method: 'GET',
      headers: {
        apikey: anon,
        Authorization: `Bearer ${anon}`,
      },
      cache: 'no-store',
    });
    if (!res.ok) throw new Error(`edge fn ${res.status}`);
    const data = await res.json();
    return NextResponse.json({ ...data, source: 'edge-fn' });
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : 'unknown';
    return NextResponse.json({
      ...FALLBACK,
      last_scan: new Date().toISOString(),
      source: `fallback-after-error: ${message}`,
    });
  }
}
