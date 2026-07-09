# 13_Data_12th_Doctor (The Factory)

**The Backend, Data, and Protocol Layer.**
Managed by the **12th Doctor** (Data Doctor).
The Mission: **Robustness, Pipes, and Truth.**

---

## 🎸 The Magician: 12th Doctor [A2]
*   **Role**: **Chief Data Officer & Backend Architect**.
*   **Archetype**: The Punk Rock Professor.
*   **Mission**: "Shut up and process the data."

## 🎓 The Team TARDIS (Data Squad)

### 1. [Clara Oswald](01_Clara_MCP/) (Context)
*   **Role**: MCP Master.
*   **Function**: Connects LLMs to Files, DBs, and APIs.
*   **The Glue**: She makes the AI "Smart" about *your* data.

### 2. [Nardole](02_Nardole_A2A/) (Protocol)
*   **Role**: A2A Orchestrator.
*   **Function**: Managing the Swarm. Who talks to whom.
*   **The Guard**: Rate limits and permissions.

### 3. [Missy](03_Missy_Chaos/) (Security)
*   **Role**: Red Team / Chaos.
*   **Function**: Trying to break the system.
*   **The Vault**: Sandboxed testing environment.

### 4. [Bill Potts](04_Bill_AG-UI/) (AG-UI)
*   **Role**: Agent-Generated UI Designer.
*   **Function**: Hosting the React Templates for GenUI.
*   **Note**: She is deployed here (Code) but renders there (Interface).

---

## 💽 The Stack
*   **DB**: Supabase (Postgres).
*   **Vector**: PgVector (Embedding Knowledge).
*   **Protocol**: MCP (Model Context Protocol).
*   **Bus**: Redis Pub/Sub.

*"Be kind."*
