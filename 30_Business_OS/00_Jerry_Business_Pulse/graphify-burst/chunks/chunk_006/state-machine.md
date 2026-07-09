---
title: Form State Machine
---

## Rule

Client components that submit forms use a 4-state machine and **never
allow double-submit** during in-flight requests.

## State type

```ts
type Status = "idle" | "submitting" | "success" | "error";
```

| State | Meaning | Submit button | UI |
|-------|---------|---------------|----|
| `idle` | Initial | enabled | form |
| `submitting` | Request in flight | disabled (no double-submit) | form, spinner |
| `success` | 2xx response | hidden | thank-you message |
| `error` | non-2xx | re-enabled | form, error banner + `errorFields` |

## Pattern (`src/components/sections/LeadForm.tsx`)

```ts
const [status, setStatus] = useState<Status>("idle");
const [errorFields, setErrorFields] = useState<string[]>([]);

async function onSubmit(e: React.FormEvent<HTMLFormElement>) {
  e.preventDefault();
  if (status === "submitting") return;   // guard
  setStatus("submitting");
  setErrorFields([]);

  try {
    const res = await fetch("/api/leads", { method: "POST", … });
    if (res.ok) {
      setStatus("success");
    } else {
      const data = await res.json().catch(() => ({}));
      if (data?.error === "validation" && Array.isArray(data.fields)) {
        setErrorFields(data.fields);
      }
      setStatus("error");
    }
  } catch {
    setStatus("error");  // network failure
  }
}
```

## Why this shape

- **Single source of truth** — `status` drives the whole UI
- **No double-submit** — the `if (status === "submitting") return` guard
  is the entire protection. No `disabled` prop, no debounce, no lock.
- **Typed error UX** — `errorFields: string[]` lets the form highlight
  specific inputs (not just show a generic banner)
- **Network failure handled** — `catch` lands in `error` (same UI as
  validation), not a thrown promise

## Don't

- ❌ Use a boolean `loading` flag — can't distinguish success from
  error in the UI
- ❌ Reset form state in the submit handler — keep `errorFields` until
  the next submit, so the user sees what to fix
- ❌ Allow submit during `submitting` — even if the button looks enabled
