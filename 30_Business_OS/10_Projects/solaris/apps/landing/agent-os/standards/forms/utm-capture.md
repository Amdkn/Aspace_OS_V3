---
title: UTM Capture
---

## Rule

Every form submission includes the 6 standard UTM params from the page
URL, even if the visitor arrived via a link that didn't have them (just
send the subset that exists).

## Helper (in `LeadForm.tsx`)

```ts
function readUtm(): Record<string, string> {
  if (typeof window === "undefined") return {};
  const p = new URLSearchParams(window.location.search);
  const out: Record<string, string> = {};
  for (const k of [
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_content",
    "utm_term",
    "ref",
  ]) {
    const v = p.get(k);
    if (v) out[k] = v;
  }
  return out;
}
```

- **Read once on submit** (not on mount) — UTM can land via hash change
  or `?ref=` redirect, but for v1 we trust the URL at submit time
- **`ref` is our internal param** (separate from `utm_*` standard) for
  partner referrals
- **Only non-empty values** are sent — server caps to 10 entries

## SSR safety

`typeof window === "undefined"` guard because the helper may be called
during a re-render after a server-injected prop. Returns `{}` on server.

## Server side (api/lead-capture.md)

`parseLead()` accepts `utm: Record<string, string>`, normalizes each
value to a string, slices to ≤ 200 chars, max 10 entries. Anything
malformed is silently dropped.

## Cross-refs

- `forms/state-machine.md` — submission flow
- `api/lead-capture.md` — server-side validation
