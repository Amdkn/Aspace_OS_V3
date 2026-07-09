---
title: Lead Capture (D09)
---

> Resolves audit debt D09. The landing CTAs ("submit your url") POST to
> `/api/leads` and persist a lead.

## Two pure functions

All lead logic lives in `src/lib/leads.ts`. No Next imports, no
fetch, no fs — fully unit-testable.

### `parseLead(body: unknown)`

Validates and coerces the raw body into a `LeadInput`.

- **URL** — accepts `"acme.com"`, normalizes to `"https://acme.com"`.
  Rejects if no dot in hostname.
- **Email** — trimmed + lowercased. Regex
  `/^[^\s@]+@[^\s@]+\.[^\s@]+$/`.
- **Archetype** — optional, sliced to 40 chars.
- **Note** — optional, sliced to 1000 chars.
- **UTM** — optional, max 10 entries, key ≤ 40 chars, value ≤ 200 chars.
  All values coerced to string.

Returns `{ ok: true, lead }` or `{ ok: false, fields: string[] }`.

### `captureLead(body, meta)`

Orchestrates: `parseLead` → add `capturedAt` (ISO) + `meta.referrer` +
`meta.ua` + `source: "landing"` → try persist (Supabase → file) → return
`CaptureResult`.

`meta` is the request context: `referrer` and `ua` from headers.

## Endpoint

`src/app/api/leads/route.ts` (POST only):

1. Parse JSON body — `400 invalid_json` on failure
2. **Honeypot check** — if `company_website` is a non-empty string,
   return `{ ok: true }` silently (don't store, don't reveal)
3. Call `captureLead(body, { referrer, ua })` from headers
4. Map result to HTTP response (see [api/result-types.md](./result-types.md))

## Form

`src/components/sections/LeadForm.tsx` (rendered in `FinalCTA`,
id `#vault-form`; Hero + Topbar CTAs anchor to it). Client component
with state machine — see [forms/state-machine.md](../forms/state-machine.md).

## Cross-refs

- `api/result-types.md` — response shape
- `api/storage-fallback.md` — persistence chain
- `api/honeypot.md` — anti-spam
- `forms/utm-capture.md` — UTM hydration before submit
- `security/rgpd-consent.md` — email+URL = consent required
