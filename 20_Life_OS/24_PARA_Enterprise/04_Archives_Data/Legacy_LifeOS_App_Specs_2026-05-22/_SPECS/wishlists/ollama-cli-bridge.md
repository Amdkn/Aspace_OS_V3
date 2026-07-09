# Wishlist: Ollama Sovereign Bridge (ALA) [GOD MODE]

## Strategic Intent
Transform **Ollama** from a standalone local tool into a **Universal Sovereign Model Proxy**. The goal is to leverage high-performance Cloud models while maintaining local-first control and Anthropic API compatibility for pro-agent tools like Claude Code.

## 🎯 High-Level Requirements

### 1. Hybrid Backend Selection (Cloud-First)
- **Primary**: Connect to Ollama Cloud/Pro for heavy reasoning tasks (H3).
- **Secondary**: Fallback to local Ollama (Gemma 3, Qwen) for embeddings and lightweight ops.
- **Switching**: Seamless backend switching via ALA Skills.

### 2. Anthropic SDK "Hijack"
- **API Simulation**: The ALA must expose an endpoint compatible with the Anthropic Messages API.
- **Provider Injection**: Agents should be able to set `base_url` to the local ALA instead of `api.anthropic.com`.
- **Secret Management**: Pass-through of local keys while masking them from the agent reasoning loop.

### 3. Sovereign Environment Hardening
- **Purge**: Completely audit and clean existing "broken" Ollama configs.
- **Optimization**: Standardize environment variables (`OLLAMA_HOST`, `OLLAMA_MODELS`) in the Bedrock.
- **CLI Mastery**: Full coverage of Ollama CLI commands (pull, run, ps, list, show).

## 🧪 TVR Assessment
- **Teachable**: ✅ (T) The ingestion will produce its own Meta-Skill for other agents to "learn" Ollama.
- **Valuable**: ✅ (V) Zero-cost (local) or low-cost (Ollama Cloud) access to SOTA models without proprietary lock-in.
- **Repeatable**: ✅ (R) Standardized ingestion workflow ensures idempotent setup on any A'Space install.

## 🚀 Research Sprint (A1 Priorities)
- **Ollama Pro Capabilities**: Investigation of Cloud API limits and model access.
- **Claude Code Open Source**: Analysis of how it handles providers to identify the best injection point.
- **Anthropic SDK Compatibility**: Deep dive into `base_url` overrides and header requirements.

---
**Status**: Wishlist Approved by A0. Transitioning to A1 Research Phase. 🧿🚀
