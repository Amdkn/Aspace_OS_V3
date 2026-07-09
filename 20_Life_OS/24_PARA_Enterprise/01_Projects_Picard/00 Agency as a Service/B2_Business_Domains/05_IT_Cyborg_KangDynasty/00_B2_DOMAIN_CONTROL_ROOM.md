---
id: B2_DOMAIN_CONTROL_ROOM
layer: B2_DOMAIN_SUPERVISION
project: 00_Agency_aaS
domain: IT
b2_owner: Cyborg
b3_swarm: Kang Dynasty
status: SHADOW_ACTIVE
updated: 2026-05-27
---

# IT Control Room - 00_Agency_aaS

This folder is the B2 supervision room for the IT domain. B2 is the orchestra conductor between B1 strategic vision and B3 autonomous execution.

## Mission

Transform B1 direction into domain Rocks, Definition of Done packets, and JTBD prompts that let the B3 swarm execute without step-by-step babysitting.

## B2 Responsibility

- Receive intent from B1 through B1_Summer_Direction/04_B2_HANDOFF_QUEUE.md.
- Define the domain Rock and the Definition of Done.
- Translate the Rock into bounded JTBD packets for B3.
- Set guardrails, evidence requirements, risks, and escalation thresholds.
- Review B3 outputs against DoD, not against personal taste.
- Report status back to B1 and the B2 gate matrix.

## B2 Must Not

- Micromanage each B3 action.
- Rewrite B1 strategy.
- Hide blockers from B1.
- Promote work to Business Done without evidence.
- Turn B3 into a checklist executor when a goal contract is enough.

## B3 Swarm Scope

B3 swarm (canon Notion — 6 members): Kang Prime (infra VPS/DNS/Dokploy), Iron Lad (provisioning Hostinger API), Scarlet Centurion (sécurité réseau / SSL), Immortus (capacity planning), Victor Timely (CI/CD), Rama-Tut (backup / DR).

> Canon = `B3_Squad_KangDynasty/00_B3_SQUAD_CANON.md` + Notion `AGENT_REGISTRY_DB`.

Core domain surface: runtime, access, deployment, backup, technical boundaries.

B3 agents may choose their execution strategy, tools, order of operations, and exploration path if they stay inside the DoD, JTBD, safety limits, and evidence contract.

## Handoff Rule

B2 gives goals, constraints, and proof requirements. B3 chooses tactics. B2 reviews artifacts and metrics.