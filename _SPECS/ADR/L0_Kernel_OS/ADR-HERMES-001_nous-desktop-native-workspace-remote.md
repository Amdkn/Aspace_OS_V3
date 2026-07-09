---
id: ADR-HERMES-001
title: Hermes topology — Nous Research Desktop = Windows-native local · Workspace = remote VPS
status: ACCEPTED
date: 2026-06-03
deciders: [A0 Amadeus]
implemented_by: Codex CLI (13th Doctor / L0 infra)
recorded_by: Claude Code (A2)
domain: L0 Tech_OS / Hermes harness + L1 runtime ; anchors People PE13-PE18 (harness = body)
tags: [#ADR #hermes #nous_research #desktop #workspace #vps #harness #disambiguation #systemd #caddy]
supersedes: prior "Startup = Hermes Workspace Runtime (local)" note in Memory Core (marked superseded 2026-06-03)
---

# ADR-HERMES-001 — Hermes topology & Desktop disambiguation

## Status

**ACCEPTED** — A0 ruling, 2026-06-03. Implemented and validated by Codex CLI; recorded by Claude Code
from the Codex transcript + on-disk verification.

## Context

The Hermes ecosystem is now live across four surfaces: **Hermes Agent CLI**, **Hermes Gateway**,
**Hermes Dashboard**, and **Hermes Workspace** (browser UI, GLM-4.7-Flash via OpenRouter). A swarm
**mission-contract dry-run** (`DRY-RUN-SOLARIS-OPS-001`) passed its Build Gate, proving the CLI +
Workspace + gateway/dashboard chain works end-to-end (artifacts:
`hermes-workspace/docs/swarm/HERMES_MISSION_CONTRACT.md` +
`00_Amadeus/05_OSS_Twin/symphony/L2/WORKFLOW.solaris-clickup-ops.md`).

Two problems forced architectural decisions:

1. **Two different "Hermes Desktop" apps** were on the machine and were being confused:
   - **Nous Research Desktop** — the *official* desktop, part of the `NousResearch/hermes-agent`
     monorepo (`apps/desktop`). It shares the **same** Hermes CLI install: config, sessions, skills,
     gateway.
   - **`fathah/hermes-desktop`** — an *external* Electron companion that merely installs/configures
     Hermes Agent via the official script; a separate app with its own profile.
2. **Desktop Nous and a local Workspace cannot run cleanly at the same time.** Because Nous Desktop
   shares the same Hermes CLI install (same sessions/config/skills), opening it while a *local*
   Workspace runs causes a **surface/session collision** — the visible conversation mixes. (Not a
   backend break; a shared-session collision.)

The install itself crashed initially (see §Install-repair) and had to be repaired.

## Decision

### D1 — Canonical split: Desktop = Windows-native local · Workspace = remote VPS
Since the two surfaces collide on shared CLI sessions, they are **physically separated**:
- **Hermes Desktop (Nous Research) = the Windows-native local surface.** Runs natively on Windows,
  shares the local Hermes CLI install.
- **Hermes Workspace = the remote surface, served from the VPS** (`aspace-vps`), reconfigured cleanly
  with its own runtime. The local Workspace stack is **retired** as a daily surface.

### D2 — Source-of-truth disambiguation (the two Desktops)
**Nous Research Desktop is canonical. `fathah/hermes-desktop` is NOT.** Identity markers to verify
before treating a binary as the Nous Desktop:

| | **Nous Research Desktop (CANONICAL)** | **fathah/hermes-desktop (NON-CANONICAL / legacy companion)** |
|---|---|---|
| Source repo | `https://github.com/NousResearch/hermes-agent.git` (`apps/desktop`) | `https://github.com/fathah/hermes-desktop` |
| Nature | Official desktop, shares CLI config/sessions/skills/gateway | External Electron installer/companion for Hermes Agent |
| App id / product | `com.nousresearch.hermes` / `Hermes`, company **Nous Research** | separate app |
| Binary | `…\AppData\Local\hermes\hermes-agent\apps\desktop\release\win-unpacked\Hermes.exe` | n/a (companion) |
| Electron profile | `C:\Users\amado\AppData\Roaming\Hermes` | `C:\Users\amado\AppData\Roaming\hermes-desktop` |
| Verdict | **use this** | **do not use as the Desktop**; both profiles coexist on disk — keep them distinct |

Documentation-sensitive claims about Hermes are verified via **Context7** (`/websites/hermes-agent_nousresearch`, `/nousresearch/hermes-agent`), not memory.

### D3 — VPS topology (least-exposure)
On `aspace-vps` (Ubuntu 24.04, Node/Pnpm/Caddy present; the pre-existing port-3000 service was
**preserved**, never overwritten), Hermes runs via the **official Nous Linux install** in its own dir,
as three **user systemd** services with `loginctl enable-linger` for persistence:

| Service | Port | Exposure |
|---|---|---|
| `hermes-gateway-vps.service` | 8642 | **loopback only** (127.0.0.1) |
| `hermes-dashboard-vps.service` | 9119 | **loopback only** (admin dashboard kept off the public Internet) |
| `hermes-workspace-vps.service` | 3001 | published via **Caddy HTTPS** at `https://hermes-workspace.148.230.92.235.sslip.io` |

- Only **Workspace** is public (HTTPS via Caddy + sslip.io); gateway + dashboard stay loopback for
  security. Workspace remote requires a **password** (set; never in chat/docs).
- Model law aligned to local canon: **OpenRouter + `z-ai/glm-4.7-flash` + `/api/v1`**. A dedicated
  `API_SERVER_KEY` was generated for the VPS; the OpenRouter key was copied without exposure.
- Validated: gateway `/health` OK, dashboard OK, Workspace OK, and a model call returned `OK_REMOTE`.

### D4 — Startup wiring (single, unambiguous)
- Windows Startup contains **one** entry: `Hermes Desktop Native.lnk` → the official Nous `Hermes.exe`.
- The **local** Workspace stack is **NOT** autostarted (it would collide with Desktop, D1). The
  `Start-HermesFullStack.ps1` / local-stack scripts are **legacy/non-canonical** for daily use.
- Daily canon: **Desktop Nous launches on Windows; Workspace is reached remotely** in the browser at
  the VPS HTTPS URL.

### D5 — Install-repair canon (operational record)
The Nous Desktop install crash was repaired without polluting the source tree:
- `git pull failed` was caused by **local modifications** in `…\AppData\Local\hermes\hermes-agent`.
  Preserved in a git stash (`codex-preserve-local-hermes-overrides-before-nous-desktop-install-2026-06-03`),
  then `git pull --ff-only origin main`.
- A Windows-specific installer bug (`Get-Command npm` returning `npm.ps1` + `npm.cmd`) was patched
  **only in the cached** `…\AppData\Local\hermes\bootstrap-cache\install-main.ps1`.
- The local marker `.hermes-bootstrap-complete` was added to `.git/info/exclude` to avoid false
  "dirty status". Runtime config (OpenRouter + GLM-4.7-Flash) is kept in `.env`, **not** hard-patched
  into source.

## Security constraints (binding)
- **Never** print/commit secret VALUES: `API_SERVER_KEY`, OpenRouter key, or the Workspace remote
  password. The password lives only at
  `C:\Users\amado\hermes-workspace\.runtime\secrets\hermes-vps-workspace-password.txt` — referenced by
  path, never by value.
- Gateway + dashboard remain loopback-only on the VPS; only the password-protected Workspace is public.
- Report only variable names + endpoint status codes (the Codex skill enforces this).

## Consequences
- ✅ One unambiguous Hermes mental model: **Desktop = local Windows brain**, **Workspace = remote VPS
  surface** — no more session-collision.
- ✅ The two-Desktop confusion is closed by D2's identity table; `fathah/hermes-desktop` is explicitly
  non-canonical.
- ✅ This **field-grounds People PE17/PE18** (harness-native swarm + heartbeat) — the doctrine's
  "harden once Hermes is wired" gate is now met; a follow-up People v5 pass can cite this ADR.
- ⚠️ Cleanup follow-up (non-blocking): the legacy local-stack scripts (`Start-HermesFullStack.ps1`,
  `Start-HermesWorkspaceStack.ps1`) and the `fathah/hermes-desktop` profile should be clearly labeled
  legacy to prevent re-wiring the old local Workspace startup.
- ⚠️ Residual: `pywinauto` absent → no deep UIA test of the Desktop UI (OS/process/window/endpoints
  validated instead).

## Related
- `~/.codex/skills/hermes-nous-desktop-finalization/SKILL.md` (Codex repair/validate skill — the
  operational companion to this ADR; Source Boundary + canonical paths + checklist).
- People doctrine `07_People…/03_GREENLANTERN_PEOPLE_PRINCIPLES.md` PE13–PE18 (harness = body).
- `ADR-RICK-001` (OpenHarness incarnation), `ADR-RICK-002` (paperclip-deprecation / Hermes promotion).
- Proof artifacts: `hermes-workspace/docs/swarm/HERMES_MISSION_CONTRACT.md` +
  `00_Amadeus/05_OSS_Twin/symphony/L2/WORKFLOW.solaris-clickup-ops.md` (mission-contract Build-Gate PASS).
- Context7: `/websites/hermes-agent_nousresearch`, `/nousresearch/hermes-agent`.
