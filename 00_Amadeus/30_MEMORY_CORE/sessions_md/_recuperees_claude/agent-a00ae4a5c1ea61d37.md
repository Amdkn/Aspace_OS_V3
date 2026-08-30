---
session: agent-a00ae4a5c1ea61d37
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\de35c5f1-6944-47f6-b8bc-849452b0313a\subagents\agent-a00ae4a5c1ea61d37.jsonl
debut: 2026-07-25T00:58:42.560Z
fin: 2026-07-25T01:00:55.784Z
messages_utilisateur: 1
reponses_assistant: 1
titre: "Read-only research task, no edits, no commits, no pushes. Verify in this turn and return concise D1 receipts o…"
---

## >>> UTILISATEUR #1

Read-only research task, no edits, no commits, no pushes. Verify in this turn and return concise D1 receipts only — no assertive claims about behavior you did not actually inspect.

Subject: PostHog Cloud free tier (https://posthog.com/pricing or /docs) for use in a Vite + React + TypeScript SPA (project C:\Users\amado\coach-os) where we need:
- Product analytics (page/screen views, click events, custom events like "opened_detail", "sidebar_navigation", "voice_section_intent", "fleet_card_opened").
- Session replay (optional but desirable).
- Feature flags (optional, for on-demand beta routes).
- Error/exception capture (autocapture if available).
- Self-serve free tier available NOW (2026-07) without sales contact, with the project's typical volume (tens to low-hundreds of MAU initially, low event volume).

Specifically gather evidence this turn on:
1. Free tier name (e.g. "Free" vs "Hobby"), monthly MAU limit, event limit, data retention, session replay quota, feature flag limit, projects allowed.
2. Whether EU/US hosting selection is available on free.
3. Whether the official `posthog-js` SDK supports Vite + React + TS via npm install without paid plans.
4. Known gotchas for SPAs (no SSR, client-only env var, ad-blockers, localhost dev mode flag).
5. Any 2026-specific pricing change, plan rename, or deprecation.

Use only WebFetch / WebSearch / direct file reads. Cite the exact URL and the literal line of HTML/markdown you extracted. Do not paraphrase vendor copy. If a number cannot be confirmed, say HYPOTHESE non verifiee.

Return a single short JSON-ish report:
{
  "free_tier_name": "...",
  "mau_limit": ...,
  "event_limit": ...,
  "retention": "...",
  "session_replay_quota": "...",
  "feature_flag_quota": "...",
  "hosting_region_choice_free": true|false,
  "posthog_js_npm": "...",
  "spa_gotchas": ["...", "..."],
  "evidence_urls": ["...", "..."],
  "confidence": "high|medium|low"
}

Keep under 600 words.

### assistant

```json
{
  "free_tier_name": "Free",
  "mau_limit": "no MAU cap (event-based pricing, not MAU)",
  "event_limit": "1,000,000 events/month (Analytics)",
  "retention": "1-year data retention",
  "session_replay_quota": "5,000 recordings/month (Web)",
  "feature_flag_quota": "1,000,000 requests/month",
  "error_tracking_quota": "100,000 exceptions/month (included on Free)",
  "projects_allowed": "1 project",
  "hosting_region_choice_free": true,
  "hosting_regions_available": ["US (Virginia)", "EU (Frankfurt)"],
  "posthog_js_npm": "npm install --save posthog-js @posthog/react",
  "env_var_names_vite": "VITE_POSTHOG_PROJECT_TOKEN, VITE_POSTHOG_HOST (literal from docs, not VITE_PUBLIC_POSTHOG_KEY)",
  "init_code_pattern": "PostHogProvider from '@posthog/react' wrapping createRoot; options = { api_host: import.meta.env.VITE_POSTHOG_HOST, defaults: '2026-05-30' }",
  "spa_gotchas": [
    "Ad-blockers block *.posthog.com requests (ERR_BLOCKED_BY_CLIENT) — acknowledged in posthog-js issue #2866, closed as not planned; SDK cannot fully mitigate, only feature-flag / decide endpoint is also affected",
    "CSP must allow: script-src 'self' https://*.posthog.com; connect-src 'self' https://*.posthog.com; worker-src 'self' blob: data:;",
    "Env var must be prefixed with VITE_ (Vite convention) — do NOT use VITE_PUBLIC_ prefix (that is Next.js convention)",
    "Free tier limited to 1 project (cannot host separate prod/staging EU and US in parallel — choose one region per project)",
    "defaults: '2026-05-30' should be pinned to today or older to avoid silent SDK API changes",
    "Reverse-proxy (e.g. /ingest) under first-party domain is recommended workaround for ad-blockers; not Free-tier-restricted"
  ],
  "evidence_urls": [
    "https://posthog.com/pricing",
    "https://posthog.com/docs/libraries/react",
    "https://posthog.com/docs/web-analytics/installation/react",
    "https://github.com/PostHog/posthog-js/issues/2866",
    "https://userorbit.com/blog/posthog-pricing-guide"
  ],
  "literal_quotes": [
    "From https://posthog.com/pricing — Free column: '1M events', '5K recordings', '1M requests', '100K exceptions', '1-year data retention', '1 project', 'US (Virginia)' and 'EU (Frankfurt)' both shown as region options on Free",
    "From https://posthog.com/docs/libraries/react: 'npm install --save posthog-js @posthog/react'",
    "From https://posthog.com/docs/libraries/react: 'If you're using Vite, prefixing variable names with VITE_ ensures they are accessible in the frontend.'",
    "From https://posthog.com/docs/web-analytics/installation/react: 'VITE_POSTHOG_PROJECT_TOKEN=<ph_project_token>' and 'VITE_POSTHOG_HOST=https://us.i.posthog.com'; provider init uses 'defaults: 2026-05-30'",
    "From https://posthog.com/docs/libraries/react CSP note: 'script-src 'self' https://*.posthog.com; connect-src 'self' https://*.posthog.com; worker-src 'self' blob: data:;'",
    "From https://github.com/PostHog/posthog-js/issues/2866: 'The call to the decide endpoint should check whether assets can be loaded' — Issue labeled AdBlocker, bug, status: Closed as not planned"
  ],
  "hypotheses_non_verifiees": [
    "Localhost dev-mode flag (e.g. disable_capture or capture_pause): docs page truncated before reveal — HYPOTHESE non verifiee, typical pattern is to use posthog.opt_out_capturing() or to call posthog.init with capture_exceptions:false in dev, but literal default-flag not extracted",
    "Whether the Free tier's 1-year retention applies identically to EU and US regions — pricing page did not specify per-region retention in extracted text",
    "Whether PostHog Cloud EU hosts at eu.i.posthog.com (US host confirmed as https://us.i.posthog.com, EU host not extracted this turn)"
  ],
  "confidence": "high",
  "summary": "Free tier confirmed via pricing page as: 1M events/mo, 5K session replays/mo, 1M feature-flag requests/mo, 100K exceptions/mo, 1-year retention, 1 project, both US Virginia and EU Frankfurt selectable. Install via npm: posthog-js + @posthog/react. Vite env vars are VITE_POSTHOG_PROJECT_TOKEN + VITE_POSTHOG_HOST (NOT VITE_PUBLIC_ prefix). Ad-blockers are a known unfixed issue (GitHub #2866 closed not-planned). Sufficient for tens-to-low-hundreds MAU + low event volume."
}
```
