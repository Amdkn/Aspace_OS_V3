# Frontier Observatory: Research Evidence

## 1. Problem Space & Customer Needs
Customers and engineers struggle to build AI agents capable of reliably operating in "long-horizon" task regimes (12+ hours). Local, single-player agents tend to be purely reactive and lack access to broad organizational context, while small models fail to maintain coherence over long sessions. There is a need for robust, asynchronous, multi-player environments (e.g., org-level harnesses) that provide deep memory and security against prompt injection.

## 2. Frontier Models vs. Smaller Models
- **Capability Gap**: Frontier models (e.g., Mythos class from OpenAI, latest from Anthropic) currently dominate long-horizon tasks, being able to operate in the 12+ hour regime on benchmarks like SWE-bench/meter.
- **Architectural Needs**: It is not just the model's raw intelligence, but the combination of memory improvements, security (prompt injection resistance), and architecture (decoupling the "brain" from the "hand" for safe execution).
- **Memory Management**: The most successful approach is providing models with "general substrates" for memory (like raw file systems or standard databases) rather than pre-defining strict memory schemas. Models are better at reasoning about their own memory structure than humans are at prescribing it.

## 3. Asynchronous Org-Level Harnesses
- **Multi-Player Agents**: Moving away from single-player desktop agents towards org-level harnesses (e.g., Claude Tag accessed via Slack) that any employee can use.
- **Shared Identity**: These harnesses possess organizational identity and credentials, independent of the individual user, enabling collaborative workflows, de-duplication of findings, and immediate onboarding.
- **Proactive Steering**: Asynchronous agents with organizational context can proactively alert users to important events instead of waiting for explicit input.

## 4. Simulation & Benchmarking Environments
- **Environment Parity**: Constructing benchmarks for agents requires building simulated environments that mimic production without needing full production scale (like integration tests).
- **Simulation Patterns**: Use of mock API services, simulated users, and diff environments where changes to the state can be isolated and evaluated.
- **Multi-Step Execution**: Simulating long-horizon tasks requires breaking them down into steps, each with its own prompt and verifier, to catch failures early.
