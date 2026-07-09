// D09 — Lead capture core (AaaS Solaris).
// Persists a captured lead to Supabase (REST, no client dep) when configured,
// else to a local JSONL file in dev. Never logs secret values.

export const SOLARIS_ARCHETYPE_IDS = ["revops", "forges", "aaa", "boutiques"] as const;
export type ArchetypeId = (typeof SOLARIS_ARCHETYPE_IDS)[number];

export interface LeadInput {
  url: string;
  email: string;
  archetype?: ArchetypeId | string;
  note?: string;
  utm?: Record<string, string>;
}

export interface LeadRecord extends LeadInput {
  capturedAt: string; // ISO
  referrer?: string;
  ua?: string;
  source: "landing";
}

export interface CaptureMeta {
  referrer?: string;
  ua?: string;
}

export type CaptureResult =
  | { ok: true; stored: "supabase" | "file" }
  | { ok: false; error: "validation"; fields: string[] }
  | { ok: false; error: "storage" };

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

/** Normalize a user-typed URL ("acme.com" -> "https://acme.com"). Returns null if unusable. */
function normalizeUrl(raw: unknown): string | null {
  if (typeof raw !== "string") return null;
  const t = raw.trim();
  if (!t) return null;
  const withProto = /^https?:\/\//i.test(t) ? t : `https://${t}`;
  try {
    const u = new URL(withProto);
    if (!u.hostname.includes(".")) return null;
    return u.toString();
  } catch {
    return null;
  }
}

/** Validate + coerce raw body into a LeadInput. */
export function parseLead(body: unknown): { ok: true; lead: LeadInput } | { ok: false; fields: string[] } {
  const b = (body ?? {}) as Record<string, unknown>;
  const fields: string[] = [];

  const url = normalizeUrl(b.url);
  if (!url) fields.push("url");

  const email = typeof b.email === "string" ? b.email.trim().toLowerCase() : "";
  if (!EMAIL_RE.test(email)) fields.push("email");

  if (fields.length) return { ok: false, fields };

  const archetype =
    typeof b.archetype === "string" && b.archetype.trim() ? b.archetype.trim().slice(0, 40) : undefined;
  const note = typeof b.note === "string" ? b.note.trim().slice(0, 1000) : undefined;
  const utm =
    b.utm && typeof b.utm === "object"
      ? Object.fromEntries(
          Object.entries(b.utm as Record<string, unknown>)
            .filter(([, v]) => typeof v === "string")
            .slice(0, 10)
            .map(([k, v]) => [k.slice(0, 40), String(v).slice(0, 200)]),
        )
      : undefined;

  return { ok: true, lead: { url: url!, email, archetype, note, utm } };
}

async function persistToSupabase(record: LeadRecord): Promise<boolean> {
  const base = process.env.SUPABASE_URL;
  const key = process.env.SUPABASE_SERVICE_ROLE_KEY ?? process.env.SUPABASE_ANON_KEY;
  if (!base || !key) return false;
  try {
    const res = await fetch(`${base.replace(/\/$/, "")}/rest/v1/leads`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        apikey: key,
        Authorization: `Bearer ${key}`,
        Prefer: "return=minimal",
      },
      body: JSON.stringify({
        url: record.url,
        email: record.email,
        archetype: record.archetype ?? null,
        note: record.note ?? null,
        utm: record.utm ?? null,
        referrer: record.referrer ?? null,
        ua: record.ua ?? null,
        source: record.source,
        captured_at: record.capturedAt,
      }),
    });
    return res.ok;
  } catch {
    return false; // never leak the error / secret
  }
}

async function persistToFile(record: LeadRecord): Promise<boolean> {
  // Dev fallback only — Vercel/serverless fs is ephemeral. Canonical store = Supabase.
  if (process.env.NODE_ENV === "production") return false;
  try {
    const { mkdir, appendFile } = await import("node:fs/promises");
    const path = await import("node:path");
    const dir = path.join(process.cwd(), ".data");
    await mkdir(dir, { recursive: true });
    await appendFile(path.join(dir, "leads.jsonl"), JSON.stringify(record) + "\n", "utf8");
    return true;
  } catch {
    return false;
  }
}

export async function captureLead(body: unknown, meta: CaptureMeta = {}): Promise<CaptureResult> {
  const parsed = parseLead(body);
  if (!parsed.ok) return { ok: false, error: "validation", fields: parsed.fields };

  const record: LeadRecord = {
    ...parsed.lead,
    capturedAt: new Date().toISOString(),
    referrer: meta.referrer,
    ua: meta.ua,
    source: "landing",
  };

  if (await persistToSupabase(record)) return { ok: true, stored: "supabase" };
  if (await persistToFile(record)) return { ok: true, stored: "file" };
  return { ok: false, error: "storage" };
}
