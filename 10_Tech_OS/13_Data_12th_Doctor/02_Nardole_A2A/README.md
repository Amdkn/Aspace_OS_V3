# 02_Nardole_A2A (The Protocol)

**The Agent-to-Agent (A2A) Handshake System.**
Nardole manages the permissions, rate limits, and secure communication between agents.
He is the invisible Cyborg maintaining the flow.

---

## ⚙️ Agent: Nardole [A3]
*   **Role**: **A2A Protocol Orchestrator & Rate Limiter**.
*   **Archetype**: The Cyborg Assistant.
*   **Mission**: "I'm the only one allowed to kick your ass." (Enforce Rules).

## 🚦 The Rules (Swarm Logic)
1.  **Handshake**: Agents must exchange Cryptographic Tokens (`Rick_Auth_V1`) to talk.
2.  **Rate Limiting**: Prevents infinite loops (A thanks B thanks A...).
3.  **Scope**: Creates "lanes". The **Finance Agent** cannot talk to the **Tinder Agent**.

## 📨 The Bus (OpenClaw Gateway)
Nardole routes messages via:
*   **Redis Pub/Sub**: Hot messages (Real-time).
*   **Postgres Queue**: Cold messages (Async tasks).
