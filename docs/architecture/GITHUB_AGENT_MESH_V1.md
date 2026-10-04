# A'Space GitHub Agent Mesh v1

Status: canonical architecture draft
Steward: Nardole / DISPATCH-INTERCONNECTION
Related: AGENTS.md, #318, #333, #404, #484, #512

## Purpose

Use GitHub as the event/control plane for agent work without making Copilot,
Codex, Claude, Hermes, Antigravity, Jules, or any other harness the institutional
identity of an A'Space holon.

GitHub-native agents are adapters.
External/local harnesses are adapters.
The portable unit is a typed AgentTaskEnvelope plus return evidence.

## Three layers

### 1. Institutional layer

A'Space holons remain provider-neutral:
- Ryan / BUILD
- Yaz / OBSERVE
- Graham / STATE
- Amy / INTERFACE
- Rory / PERSISTENCE/COHERE
- River / FLOW
- Bill / RESEARCH
- Clara / DESIGN/FORGE
- Nardole / DISPATCH/INTERCONNECTION
- Donna / RECOVER

These names are stewardship anchors, not cognitive limits.

The canonical bootstrap remains the repository AGENTS.md hierarchy and capability
contracts. A runtime never owns the holon identity.

### 2. GitHub control plane

GitHub provides:
- Issues for executable cells;
- PRs for mutations and review;
- Actions for deterministic verification;
- Discussions for exploration;
- Projects/Milestones for portfolio/convergence;
- custom agents for GitHub/Copilot-native embodiments;
- partner coding agents where supported;
- webhooks/GitHub App events for external embodiments.

### 3. Harness execution plane

Provider adapters may include:
- github-copilot
- github-codex
- github-claude
- hermes
- codex-local
- claude-code
- antigravity
- jules
- future harnesses

Every adapter consumes the same AgentTaskEnvelope and returns an AgentResultEnvelope.

## Native GitHub agents

Repository custom agents live under `.github/agents/*.agent.md`.

They are thin GitHub-specific projections over A'Space role/capability contracts.
They MUST NOT become a second source of institutional truth.

The profile should:
- name the GitHub-visible specialization;
- point to AGENTS.md and the relevant local canon;
- constrain tools;
- declare only GitHub/Copilot-specific configuration;
- avoid duplicating the full holon constitution.

GitHub also recognizes repository agent instructions such as AGENTS.md, so the
existing A'Space hierarchy remains the portable context substrate.

## Native third-party GitHub agents

Where GitHub supports a partner agent directly, treat it as another adapter.

Current policy:
- GitHub-hosted Codex may be selected directly for an Issue/agent session.
- GitHub-hosted Claude may be selected directly for an Issue/agent session.
- Their provider-specific session IDs are evidence, never institutional identity.

Using a native partner path is an optimization. It must produce the same return
contract as a webhook-routed local harness.

## External agent gateway

Create one GitHub App / Webhook receiver:

`A'Space Agent Gateway`

It receives a minimal event set:
- issues
- issue_comment
- pull_request
- pull_request_review
- workflow_run
- check_run (optional)
- push only when a concrete use requires it

Do not subscribe to every event.

The gateway validates the GitHub webhook signature before parsing or dispatching.

## Dispatch trigger convention

Preferred executable trigger:

- Issue already contains a bounded acceptance contract.
- label `agent:ready`
- one or more capability labels such as `needs:ryan`, `needs:nardole`
- optional command comment:
  `/agent run`
  `/agent reroute provider=auto`
  `/agent retry`

External harnesses are not represented as GitHub assignees unless they genuinely
have a GitHub-native agent identity.

The dispatcher resolves:
`capability need -> eligible holons -> eligible harnesses -> HostPolicy -> lease`.

Provider choice is downstream of capability/authority choice.

## Event normalization

Every accepted GitHub event is normalized to:

`AgentTaskEnvelope.v1`

Required cross-cutting coordinates:
- delivery_id
- repository
- event/action
- issue/pr/ref
- mission_id
- work_id/cell_id when present
- correlation_id
- parent_correlation_id when present
- requested capability
- intended holon/steward if already resolved
- acceptance/evidence refs
- authority scope
- effect class
- base ref / workspace constraints
- allowed or preferred harnesses
- budget/quota hints
- return_to

Raw webhook payloads are evidence inputs, not the internal dispatch schema.

## Provider-neutral routing

Example:

```
GitHub Issue #484 + agent:ready + needs:nardole
        |
        v
A'Space Agent Gateway
        |
        v
normalize AgentTaskEnvelope
        |
        v
Nardole / Reflex / Resource eligibility
        |
        +--> GitHub Codex
        +--> GitHub Claude
        +--> Hermes
        +--> Codex local
        +--> Antigravity
        +--> Jules
        +--> Copilot custom agent
        |
        v
HostPolicy + lease/fencing
        |
        v
HarnessAdapter
```

The issue never says "this work IS Codex".
It says what capability is required and which authority/effect is permitted.

## Return contract

All harnesses return an `AgentResultEnvelope.v1` containing:
- correlation_id
- provider/harness/model
- session/run id
- status: SUCCEEDED | FAILED | BLOCKED | UNKNOWN
- branch/commit/PR refs when created
- stdout/log/artifact/evidence refs
- observed effect
- test/check results
- continuation recommendation
- recovery hint
- exact return_to

Results are projected back into GitHub as:
- PR;
- Issue/PR comment;
- Check Run / status;
- Action artifact;
- evidence reference.

UNKNOWN is preserved and routed to recovery; it is not converted into retry.

## Bidirectional bridge

GitHub -> external harness:
GitHub App webhook -> Agent Gateway -> HarnessAdapter.

External harness -> GitHub:
GitHub App installation token -> comments/branches/PR/checks.

For events that need to re-enter Actions, the gateway may emit a typed
`repository_dispatch` event rather than inventing a provider-specific workflow.

## Security / authority

Mandatory:
- verify `X-Hub-Signature-256`;
- deduplicate GitHub delivery IDs;
- allowlist repository and accepted actor associations;
- do not place raw credentials in prompts/envelopes;
- use GitHub App installation tokens instead of long-lived personal PATs where possible;
- read-only by default;
- require explicit authority/effect scope for writes;
- fence conflicting mutation/effect scope;
- preserve operation/correlation IDs;
- no blind retry on UNKNOWN.

A model confidence score cannot widen GitHub permissions.

## GitHub Actions role

Actions are validators and bridges, not institutional agents.

Good uses:
- validate AgentTaskEnvelope schema;
- validate custom-agent profiles;
- run tests/security checks;
- publish Evidence Receipts;
- trigger or receive repository_dispatch;
- reconcile stale agent sessions;
- gate closure after deterministic conditions.

Do not put the entire agent orchestration ontology inside workflow YAML.

## copilot-setup-steps.yml

This file should only prepare the GitHub Copilot cloud-agent environment:
dependencies, runtimes, caches, deterministic setup.

It must not become the universal A'Space dispatcher.

The same repository task should remain runnable by a local Hermes/Codex/
Antigravity/Jules adapter even if Copilot setup is absent.

## Implementation order

M0:
- schema AgentTaskEnvelope/AgentResultEnvelope;
- one GitHub custom-agent adapter (Nardole);
- one webhook gateway route;
- one external HarnessAdapter canary;
- return comment/check with same correlation_id.

M1:
- Codex/Claude native GitHub adapters;
- Hermes/Antigravity/Jules local adapters;
- Project/Issue/PR lifecycle integration;
- lease/backpressure/recovery.

M2:
- organization-level agent profiles;
- multi-repo routing;
- resource/cost-aware dispatch;
- Agent OS / CubeFarm projection.

## Acceptance canary

1. Create or select one bounded Issue.
2. Add `agent:ready` + `needs:nardole`.
3. GitHub webhook reaches Agent Gateway.
4. Gateway validates signature and normalizes one AgentTaskEnvelope.
5. Nardole chooses an eligible harness without changing institutional identity.
6. Harness returns AgentResultEnvelope.
7. Gateway posts the evidence/result to the same Issue/PR.
8. A second run may use a different harness with the same task contract.
9. Both runs preserve correlation/authority/return_to.
10. UNKNOWN routes to Donna/RecoveryPort instead of blind replay.
