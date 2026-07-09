<!-- BEGIN:nextjs-agent-rules -->
# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` before writing any code. Heed deprecation notices.
<!-- END:nextjs-agent-rules -->

# ABC Child Care Portal — App Agent Guide

Sovereignty-grade childcare cooperative dashboard (parallel fork to `abc-os-community`). Same 4-hub spine: **Community** · **Learn** · **Build** · **Brand**. Same `next-intl` FR/EN i18n pattern.

## Hosting (post-ADR-ABCOS-002 RATIFIED 2026-06-19)

- **Supabase Cloud** : `abc_child_care` schema désormais sur ABC-OS-COMMUNITY Org (si provisionné, à vérifier A0). Self-host VPS `148.230.92.235` archivé.
- **Vercel** : project `prj_AN7joKC8eSwEc7adzmjzAXQdyt8C` (team `team_d3JjRK4fJUE9ACohbdlhv9Gc`) **ACTIVE**. `.vercel/project.json` confirme canonical (ne PAS cleanup).
- **⚠️ Condition F P0 PENDING** : si schema sur Cloud, ajouter `abc_child_care` à "Exposed schemas" Dashboard UI.
- **Vercel Authentication default ON** : à OFF manuellement via Project Settings → Security (per ADR-ABCOS-002 Condition D).

## Work Guidance

- **Mature fork pattern** : référence pour i18n (`messages/{fr,en}.json`), `/build-hub` rename (Vercel réserve `/build`), `ThemeProvider` SSR-safe via `cookies()`.
- **Commands** (from `apps/abc-childcare-portal/`) : `npm install` (Node 20+), `npm run dev`, `npm run build`, `npm run lint`. Verify with `npx tsc --noEmit` then `npm run build`.
- **Cross-refs** : voir `ADR-ABCOS-002` (hosting pivot), `ADR-ABCOS-001` (multi-tenant model), `abc/CLAUDE.md` (root).
