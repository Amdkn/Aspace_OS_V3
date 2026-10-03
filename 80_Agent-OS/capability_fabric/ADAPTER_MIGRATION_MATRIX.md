# Adapter Migration Matrix - Business OS to Agent OS Capability Fabric

This matrix captures the inventory, classification, and target state for transferring AI-native adapters and tooling abstractions from Business OS / Coach OS into the shared Agent OS Capability Fabric, adhering to the migration laws of Issue #411.

## Migration Law
```text
Business OS innovation
      │ classify
KEEP DOMAIN-SPECIFIC ────────────────► Business OS remains owner
GENERALIZE PLATFORM ─────────────────► Agent OS Capability Fabric
RUNTIME/MACHINE PRIMITIVE ───────────► Tech OS
UI/PROJECTION ───────────────────────► Agent OS projection layer
EXPERIMENTAL/UNCERTIFIED ────────────► Quarantine / research
```

---

## Detailed Adapter Inventory & Migration Matrix

### Batch M0: Canonical Capability Core

| ID | Current Path | Semantic Owner | Transport / Protocol | Generic vs Business Logic | Dependencies | Auth / Secrets Model | Schema (In / Out) | Authority / Effect Semantics | Evidence / Provenance Behavior | Target Layer | Target Module / Package | Migration Status | Compatibility Test | Deprecation / Removal Plan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M0-01 | `coach-os-app/src/lib/tooling/defineTool.ts` | Agent OS | Declarative JS/TS & Python DSL | Generic tool declaration contract | None | Inherited from execution context | JSON Schema (typed args & result) | Declarative | Correlation ID + EffectReceipt | Agent OS | `80_Agent-OS/capability_fabric/capability.py` | COMPLETED | `test_define_tool_contract` | Deprecated in Business local platform code; thin wrapper re-exports shared core |
| M0-02 | `coach-os-app/src/lib/tooling/registry.ts` | Agent OS | In-Memory Registry | Generic capability registration & lookup | Python stdlib | Context-scoped | Contract objects | Registry lookup only (no effect) | Registry snapshot | Agent OS | `80_Agent-OS/capability_fabric/registry.py` | COMPLETED | `test_registry_registration` | Replaced by shared `CapabilityRegistry` |
| M0-03 | `coach-os-app/src/lib/tooling/types.ts` | Agent OS | Type Contracts | Generic ToolContext, ToolResult, EffectReceipt | dataclasses / typing | Bearer / Tenant context | Dict / JSON | Standardized status codes & error reporting | Provenance string + evidence refs | Agent OS | `80_Agent-OS/capability_fabric/capability.py` | COMPLETED | `test_capability_contract_types` | Types imported from `capability_fabric` |
| M0-04 | `coach-os-app/src/lib/tooling/hooks.ts` | Agent OS / Tech OS | Hook Execution | Authority verification, effect receipt creation, audit logging | WorkGraph / Evidence | Tenant / Actor token | Invocation payload / EffectReceipt | COMMAND / QUERY gating | EffectReceipt + evidence_refs | Agent OS | `80_Agent-OS/capability_fabric/capability.py` | COMPLETED | `test_effect_receipt_generation` | Domain hooks wrap shared EffectReceipt |
| M0-05 | `coach-os-app/src/lib/tooling/discovery.ts` | Agent OS | Search / Discovery API | Capability discovery across surfaces & tags | Registry | Read-only surface permissions | Query filter / Capability list | QUERY | Surface health matrix snapshot | Agent OS | `80_Agent-OS/capability_fabric/registry.py` | COMPLETED | `test_capability_discovery` | Business OS calls `registry.list_capabilities()` |

---

### Batch M1: Core Transport Adapters

| ID | Current Path | Semantic Owner | Transport / Protocol | Generic vs Business Logic | Dependencies | Auth / Secrets Model | Schema (In / Out) | Authority / Effect Semantics | Evidence / Provenance Behavior | Target Layer | Target Module / Package | Migration Status | Compatibility Test | Deprecation / Removal Plan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M1-01 | `coach-os-app/src/lib/tooling/mcpAdapter.ts` | Agent OS | Model Context Protocol (MCP) | Generic JSON-RPC MCP tool wrapper | MCP SDK | API Key / Bearer | MCP tool schema / MCP result | Standardized invocation | Invocation provenance trace | Agent OS | `80_Agent-OS/capability_fabric/adapters.py` (`MCPAdapter`) | COMPLETED | `test_mcp_adapter_invocation` | Local MCP adapter delegates to `MCPAdapter` |
| M1-02 | `coach-os-app/src/lib/tooling/apiAdapter.ts` | Agent OS | REST / HTTP API | Generic HTTP request endpoint wrapper | requests / urllib | OAuth2 / Bearer / Headers | JSON Body / Response | Endpoint execution | HTTP trace + EffectReceipt | Agent OS | `80_Agent-OS/capability_fabric/adapters.py` (`APIAdapter`) | COMPLETED | `test_api_adapter_invocation` | REST routes wrap shared `APIAdapter` |
| M1-03 | `coach-os-app/src/lib/tooling/cliAdapter.ts` | Agent OS | CLI / Subprocess | Generic stdout/stderr CLI execution | subprocess / sys | Environment variables | Args list / Stdout JSON | CLI command execution | Stdout capture + status code | Agent OS | `80_Agent-OS/capability_fabric/adapters.py` (`CLIAdapter`) | COMPLETED | `test_cli_adapter_invocation` | CLI entrypoints delegate to `CLIAdapter` |
| M1-04 | `coach-os-app/src/lib/tooling/skillAdapter.ts` | Agent OS | Agent Skill Protocol | Generic agent skill execution & validation | Python stdlib | Skill context token | Skill input / output payload | Executable skill step | Skill run log | Agent OS | `80_Agent-OS/capability_fabric/adapters.py` (`SkillAdapter`) | COMPLETED | `test_skill_adapter_invocation` | Business skills wrap `SkillAdapter` |
| M1-05 | `coach-os-app/src/lib/tooling/inAppAdapter.ts` | Agent OS | In-App / IPC Projection | Generic UI/App command bridge | Window / IPC | App session token | In-App event / Component state | UI action trigger | In-App event receipt | Agent OS | `80_Agent-OS/capability_fabric/adapters.py` (`InAppAdapter`) | COMPLETED | `test_in_app_adapter_invocation` | UI components consume `InAppAdapter` |

---

### Batch M2: Harness Adapters

| ID | Current Path | Semantic Owner | Transport / Protocol | Generic vs Business Logic | Dependencies | Auth / Secrets Model | Schema (In / Out) | Authority / Effect Semantics | Evidence / Provenance Behavior | Target Layer | Target Module / Package | Migration Status | Compatibility Test | Deprecation / Removal Plan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M2-00 | `10_Tech_OS/kernel/harness.py` | Agent OS / Tech OS | Generic Harness Contract | Universal harness invocation interface | Python stdlib | Harness API token | Harness input / execution output | Capability execution across ADEs | Provenance + runtime binding trace | Agent OS | `80_Agent-OS/capability_fabric/harness_adapters.py` (`GenericHarnessAdapter`) | COMPLETED | `test_generic_harness_adapter` | Harness base class shared across all ADEs |
| M2-01 | `10_Tech_OS/machine_fabric/harness_runtime/` | Agent OS | Claude Code ADE | Claude CLI tool projection | Claude CLI | `ANTHROPIC_API_KEY` | Claude tool format | ADE command execution | Claude tool receipt | Agent OS | `80_Agent-OS/capability_fabric/harness_adapters.py` (`ClaudeCodeHarnessAdapter`) | COMPLETED | `test_claude_code_harness_adapter` | Private harness wrappers removed |
| M2-02 | `10_Tech_OS/machine_fabric/harness_runtime/` | Agent OS | OpenAI Codex / GPT ADE | Codex tool call adapter | OpenAI API | `OPENAI_API_KEY` | Function call schema | ADE code execution | Codex execution receipt | Agent OS | `80_Agent-OS/capability_fabric/harness_adapters.py` (`CodexHarnessAdapter`) | COMPLETED | `test_codex_harness_adapter` | Private harness wrappers removed |
| M2-03 | `10_Tech_OS/machine_fabric/harness_runtime/` | Agent OS | Hermes ADE | Hermes cron/agent protocol | Hermes daemon | Hermes token | Hermes task contract | Autonomous agent step | Hermes run log | Agent OS | `80_Agent-OS/capability_fabric/harness_adapters.py` (`HermesHarnessAdapter`) | COMPLETED | `test_hermes_harness_adapter` | Private harness wrappers removed |
| M2-04 | `10_Tech_OS/machine_fabric/harness_runtime/` | Agent OS | Antigravity ADE | Multimodal/TTS execution harness | Antigravity daemon | System service token | Audio/Visual/Tool payload | Multimodal execution | Antigravity receipt | Agent OS | `80_Agent-OS/capability_fabric/harness_adapters.py` (`AntigravityHarnessAdapter`) | COMPLETED | `test_antigravity_harness_adapter` | Private harness wrappers removed |
| M2-05 | `10_Tech_OS/machine_fabric/harness_runtime/` | Agent OS | Jules ADE | Sandbox execution harness | Jules proxy | Jules session key | Code/Bash task contract | Sandbox execution | Jules execution receipt | Agent OS | `80_Agent-OS/capability_fabric/harness_adapters.py` (`JulesHarnessAdapter`) | COMPLETED | `test_jules_harness_adapter` | Private harness wrappers removed |
| M2-06 | `10_Tech_OS/machine_fabric/harness_runtime/` | Agent OS | Qwen / Qwen Coder ADE | Local/SLM execution harness | Qwen SLM | Local endpoint | Ollama / SLM schema | Local code inference | Qwen execution receipt | Agent OS | `80_Agent-OS/capability_fabric/harness_adapters.py` (`QwenHarnessAdapter`) | COMPLETED | `test_qwen_harness_adapter` | Private harness wrappers removed |

---

### Batch M3: Agent & Protocol Adapters

| ID | Current Path | Semantic Owner | Transport / Protocol | Generic vs Business Logic | Dependencies | Auth / Secrets Model | Schema (In / Out) | Authority / Effect Semantics | Evidence / Provenance Behavior | Target Layer | Target Module / Package | Migration Status | Compatibility Test | Deprecation / Removal Plan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M3-01 | `coach-os-app/src/lib/tooling/agentOsProjection.ts` | Agent OS | Agent OS Native Projection | OS Desktop / Surface state projection | Agent OS Desktop | Local session token | Surface state payload | QUERY / PROJECTION | Desktop surface receipt | Agent OS | `80_Agent-OS/capability_fabric/adapters.py` (`AgentOSProjectionAdapter`) | COMPLETED | `test_agent_os_projection_adapter` | Consumes shared `AgentOSProjectionAdapter` |
| M3-02 | `coach-os-app/src/lib/tooling/a2aAdapter.ts` | Agent OS | Agent-to-Agent (A2A) Protocol | Inter-agent message & task delegation | A2A Protocol SDK | Agent pair token | A2A Message contract | Inter-agent command | Delegation receipt | Agent OS | `80_Agent-OS/capability_fabric/adapters.py` (`A2AAdapter`) | COMPLETED | `test_a2a_adapter_invocation` | Consumes shared `A2AAdapter` |
| M3-03 | `coach-os-app/src/lib/tooling/a2uiAdapter.ts` | Agent OS | Agent-to-UI (A2UI) Protocol | Agent-driven UI component rendering | UI Bridge | Web session token | Component UI payload | UI rendering event | Component render receipt | Agent OS | `80_Agent-OS/capability_fabric/adapters.py` (`A2UIAdapter`) | COMPLETED | `test_a2ui_adapter_invocation` | Consumes shared `A2UIAdapter` |
| M3-04 | `coach-os-app/src/lib/tooling/acpAdapter.ts` | Agent OS | Agent Communication Protocol (ACP) | IBM/Zed ACP message transport | ACP SDK | ACP channel token | ACP frame payload | Async protocol message | Protocol frame receipt | Agent OS | `80_Agent-OS/capability_fabric/adapters.py` (`ACPAdapter`) | COMPLETED | `test_acp_adapter_invocation` | Consumes shared `ACPAdapter` |
| M3-05 | `coach-os-app/src/lib/tooling/aguiAdapter.ts` | Agent OS | Agent-User Interaction (AG-UI) | Interactive human-in-the-loop dialog | Bill AG-UI daemon | User approval token | Question / Answer payload | Approval gate | Human decision receipt | Agent OS | `80_Agent-OS/capability_fabric/adapters.py` (`AGUIAdapter`) | COMPLETED | `test_agui_adapter_invocation` | Consumes shared `AGUIAdapter` |
| M3-06 | `coach-os-app/src/lib/tooling/webmcpAdapter.ts` | Agent OS | WebMCP Browser Protocol | Browser-hosted MCP capability | Browser Extension | WebMCP origin token | Web Tool schema / result | Web DOM / API action | Browser action receipt | Agent OS | `80_Agent-OS/capability_fabric/adapters.py` (`WebMCPAdapter`) | COMPLETED | `test_webmcp_adapter_invocation` | Consumes shared `WebMCPAdapter` |
| M3-07 | `coach-os-app/src/lib/tooling/experimental/` | Quarantine | FCP, OAP, TAP, TDF, UCP, RDF-agent | Uncertified experimental protocols | None / External | None | Unspecified | Experimental / Uncertified | None | Quarantine | `80_Agent-OS/capability_fabric/quarantine.py` (`QuarantineRegistry`) | QUARANTINED | `test_quarantined_adapter_isolation` | Strictly isolated in QuarantineRegistry; barred from auto-promotion |

---

### Batch M4: Business OS Capability Consumption

| ID | Current Path | Semantic Owner | Transport / Protocol | Generic vs Business Logic | Dependencies | Auth / Secrets Model | Schema (In / Out) | Authority / Effect Semantics | Evidence / Provenance Behavior | Target Layer | Target Module / Package | Migration Status | Compatibility Test | Deprecation / Removal Plan |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M4-01 | `30_Business_OS/capabilities/research_corpus.py` | Business OS | Capability Fabric (Shared) | Business research & discovery domain logic | Shared Capability Fabric | Business domain token | Corpus query / Research summary | Business QUERY | Business research receipt | Business OS | `30_Business_OS/capabilities/research_corpus.py` | COMPLETED | `test_business_research_corpus_capability` | Consumes `CapabilityRegistry` and `define_tool` from shared fabric while remaining Business-owned |
| M4-02 | `30_Business_OS/10_Projects/coach-os-app/src/lib/tooling/` | Business OS / Agent OS | Legacy Tooling Infrastructure | Business-local platform fork | None | Legacy session | Legacy tool format | Legacy execution | Legacy logs | Business OS / Agent OS | Legacy code deprecated | DEPRECATED | `test_capability_fabric_parity` | Removed platform infrastructure; thin wrappers redirect to `80_Agent-OS/capability_fabric/` |
