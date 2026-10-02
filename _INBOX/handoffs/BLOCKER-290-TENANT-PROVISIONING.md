# Blocker for Issue 290: Launch Cohort tenant provisioning + isolation canary

**Issue**: #290 [BUSINESS-OS][OPERATIONS][P1] Launch Cohort tenant provisioning + isolation canary
**Status**: BLOCKED_BY_PERMISSION

## Context
The issue #290 requests the implementation of tenant provisioning and isolation canary for the Launch Cohort. The issue states that the target implementation repository is `omk-services/OMK-DESKTOP-WEB-OS`. The instructions specify: "If blocked by human-only auth/permission or an irreversible external action, return a typed blocker instead of faking success."

## Blocker Details
1. **Missing Write Access**: The AI agent executing this task only has `pull: true, push: false` (read-only) permissions for the required repository `omk-services/OMK-DESKTOP-WEB-OS`.
2. **Architecture Contract Constraints**: The issue mentions "Product mutations still belong in the canonical repo." We cannot create issues or commit code there.
3. **Previous Handoff Records**: Session records (e.g. `10_Tech_OS/00_Governance_Rick/SESSION_2026-08-13_condense.md`) explicitly document that "Ton compte GitHub n'a qu'un accès **lecture** sur `omk-services/OMK-DESKTOP-WEB-OS`."

## Required Human Action
A human operator (Amdkn) must grant write access to `omk-services/OMK-DESKTOP-WEB-OS` to the agent/account performing this task, or perform the mutation directly in the target repository. Once the permissions are resolved, this task can be unblocked and the implementation can proceed.

## Return Payload
We are returning this typed blocker to satisfy the issue constraint: "If blocked by human-only auth/permission or an irreversible external action, return a typed blocker instead of faking success."
