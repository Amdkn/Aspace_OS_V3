---
title: Honeypot Anti-Spam
---

## Rule

Every public form on this site includes a hidden `company_website` field
that humans can't see but bots fill in automatically.

## Pattern (server side)

```ts
// src/app/api/leads/route.ts
const hp = (body as Record<string, unknown>)?.company_website;
if (typeof hp === "string" && hp.trim() !== "") {
  return NextResponse.json({ ok: true });
}
```

- If the field is **non-empty**, return `200 { ok: true }` **silently**
- Do NOT persist the record
- Do NOT log the bot's payload
- Do NOT reveal that it was caught

## Pattern (client side)

In `LeadForm.tsx`, the form's `FormData` includes the honeypot field
**as a regular input** — but the input is hidden via CSS
(`position: absolute; left: -9999px`) or `tabIndex={-1}` + `aria-hidden`.

```html
<input
  type="text"
  name="company_website"
  tabIndex={-1}
  autoComplete="off"
  aria-hidden="true"
  style={{ position: "absolute", left: "-9999px" }}
/>
```

## Why

- **Silent accept** — bots that probe for honeypot detection will get
  `200 ok` and move on, instead of retrying with new tactics
- **No log noise** — adversarial payloads never hit our logs
- **Cheap** — 4 lines of code, no JS dep, no captcha, no 3rd party

## Don't

- ❌ Return a different status code (e.g. `400`) — reveals the trap
- ❌ Persist the record (even marked as spam) — wastes storage
- ❌ Log the bot's payload — log noise + privacy
- ❌ Use a real-looking field name like `email_confirm` — bots may avoid
  it. Use the oddly-named `company_website` (we already collect `url`)

## Cross-refs

- `api/lead-capture.md` — full lead flow
