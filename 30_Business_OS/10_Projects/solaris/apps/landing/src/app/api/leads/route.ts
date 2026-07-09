import { NextRequest, NextResponse } from "next/server";
import { captureLead } from "@/lib/leads";

// D09 — lead capture endpoint. Node runtime (Supabase REST fetch + dev fs fallback).
export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function POST(req: NextRequest) {
  let body: unknown;
  try {
    body = await req.json();
  } catch {
    return NextResponse.json({ ok: false, error: "invalid_json" }, { status: 400 });
  }

  // Honeypot: a hidden field bots fill in. If present, accept silently (don't store, don't reveal).
  const hp = (body as Record<string, unknown>)?.company_website;
  if (typeof hp === "string" && hp.trim() !== "") {
    return NextResponse.json({ ok: true });
  }

  const result = await captureLead(body, {
    referrer: req.headers.get("referer") ?? undefined,
    ua: req.headers.get("user-agent") ?? undefined,
  });

  if (result.ok) return NextResponse.json({ ok: true });

  if (result.error === "validation") {
    return NextResponse.json({ ok: false, error: "validation", fields: result.fields }, { status: 422 });
  }
  // storage unavailable (e.g. Supabase env not set in prod)
  return NextResponse.json({ ok: false, error: "storage_unavailable" }, { status: 503 });
}
