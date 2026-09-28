---
name: council-of-doctors
description: Run Rick -> 3 Doctors -> 9 Companions as an evidence-driven management cycle.
---
# Council of Doctors
1. Read campaign + durable evidence.
2. Rick invokes Doctor13/11/12 concurrently using isolated branch workspaces.
3. Doctor13 owns Foundation critical path; Doctor11/12 run consumer validation in parallel.
4. Doctors invoke their three Companions concurrently when PDRs are independent.
5. Each Doctor returns only closed PDRs, evidence refs, real blockers, next wave.
6. Use send_message / Discussion #185 before escalating cross-Core needs to Rick.
7. Rick selects the next wave from acceptance gaps, not ticket count.
8. Repeat until detachment acceptance is proven.

After invoke_subagent, never poll manage_subagents in a loop. The runtime automatically delivers child send_message notifications; continue independent work or wait for messages.
