---
title: RGPD Consent (L6)
---

## Context

The lead form collects **email + URL** — both are personal data under
RGPD (L6). The form currently has **no consent checkbox**, which blocks
scaling diffusion to EU traffic.

## Required before scaling to EU

1. **Consent checkbox** in `LeadForm.tsx` — unchecked by default,
   required to enable submit
2. **Privacy notice link** — anchor to a `/privacy` page (TBD) below
   the submit button
3. **Retention policy** — defined in the privacy page (e.g. 24 months
   for `leads` table, then auto-delete via Supabase scheduled function)
4. **Data export on request** — a route or admin tool that returns a
   lead's full record by email (right of access, L6 art. 15)
5. **Right to erasure** — DELETE endpoint by email + token (L6 art. 17)
6. **DPO contact** — listed in the privacy page

## Why this is a standard, not a ticket

The form's `parseLead()` is shape-locked to `{ url, email, archetype?,
note?, utm? }`. Adding consent means:

- Schema addition: `consent: boolean` to `LeadInput` (required)
- UI addition: checkbox with `required` attribute
- Storage addition: column on `public.leads` table
- Validation: 422 if `consent !== true`

Get the consent state in the same `FormData` payload as the rest of
the form. Don't split the submission into two steps.

## Cross-domain (per L0/A2/12th)

- **Legal** (L2/07) — owns the privacy page + retention policy
- **IT** (L2/02) — provisions the consent column + RLS policy
- **Growth** (L2/05) — owns the diffusion channels; can't scale to EU
  until this standard is implemented

## Status

- [ ] Consent checkbox in `LeadForm.tsx`
- [ ] Privacy page written
- [ ] Retention + export + delete implemented
- [ ] EU traffic enabled

**Do not enable EU ad traffic until all 4 are checked.**
