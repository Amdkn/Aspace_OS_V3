# Frontier Observatory: Simulation Topology

Based on the research evidence, the following architectural topology is observed for evaluating and executing agents safely in complex, long-horizon tasks.

## 1. Simulation Isolation (The "Integration Test" Pattern)
Agents should not operate directly on production infrastructure during benchmarking or early execution.
- **Diff Environment**: The agent operates within an isolated environment where all state changes are tracked as a diff from the initial state.
- **Side Containers / Sidecars**: Essential services (APIs, databases, MCP tools) are provided as adjacent containers to the main agent runtime.

## 2. Component Mocking
- **Mock API Services**: The agent accesses local, lightweight replicas of external APIs.
- **Simulated Users**: Synthetic user inputs are provided to the environment to test the agent's interaction capabilities without human-in-the-loop dependencies for automated benchmarking.

## 3. Multi-Step Checkpointing
- **Intermediate Verification**: Long-horizon tasks (spanning hours) are divided into distinct steps.
- **Step-wise Context**: Each step possesses a specific prompt and a dedicated verifier.
- **Early Termination**: The simulation framework evaluates the agent at each step, aborting the process early if the agent diverges from the expected path, saving compute and time.

## 4. Evaluation Artifacts
The topology produces three key artifacts for verifiers to evaluate:
- **Final State**: The modified state of the mock database/filesystem.
- **Trace**: The sequence of actions, tool calls, and LLM reasoning steps.
- **Output Artifacts**: The generated code, reports, or data files.
