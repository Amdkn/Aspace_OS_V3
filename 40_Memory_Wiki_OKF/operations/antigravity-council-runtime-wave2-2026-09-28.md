---
type: Operations memory
title: Antigravity Council runtime — recursive execution proven
date: 2026-09-28
tags: [antigravity, council, rick, doctors, companions, subagents, pdr, jules, recovery]
okf_version: "0.2"
confidence: machine-verified
---

# Antigravity Council runtime — recursive execution proven

A'Space no longer needs nine parallel ChatGPT windows as its normal execution model.

Runtime target proven:
`Rick → 3 Doctors → 9 Companions`

ChatGPT remains an A0/supervision/exception surface, not the daily Kernel message bus.

Proof:
- Rick: `07581fce-8c7e-43d0-bcb5-bf0a365378b5` → `RICK_READY`
- Doctor13: `2675a0d1-43e7-4a28-8efe-be09fbdb0847`
- Doctor11: `ab712460-5ad3-4809-a73b-1e3839b2e6e2`
- Doctor12 recovery: `c400ef8e-905e-4451-9551-210a126f071f`
- Doctor13 recursive parent: `6626ee1e-0b05-456f-a28f-3f125082930b`
- Ryan/Yaz/Graham all returned READY from isolated worktrees.
## Durable lessons

- Recover only the missing child after server/parent failure; never rerun the whole Council blindly.
- Never poll `manage_subagents` in a loop. Child `send_message` notifications are delivered automatically.
- 17 legacy scheduled sidecars were disabled and backed up; post-restart scheduled process count = 0.
- Compact `GEMINI.md` replaced the oversized/truncated runtime prompt.
- Jules must be an execution-edge worker, not a prerequisite for Rick/Doctors bootstrap.
- PDR is the bounded delegation primitive; avoid mandatory document cascades.
- Projection completion does not resolve parent IPBD.

Current gate:
**one real Foundation PDR via Jules → Ryan integration → Yaz verification → Graham evidence → Doctor13 reconciliation.**

Only after that should PR #187 leave Draft.

Canon:
- `10_Tech_OS/council/evidence/council_runtime_canary_20260928.json`
- `10_Tech_OS/council/legacy_sidecars_disabled_20260928.json`
- `_INBOX/handoffs/HANDOVER-2026-09-28-ANTIGRAVITY-COUNCIL-WAVE2.md`
