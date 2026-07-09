# JTBD-005 RILCOT Transverse Growth Signal Gate

## Job
When 03 RILCOT Members Space OS prepares any Growth campaign, channel test, offer message, acquisition push, member/client activation, or public positioning action, Growth must verify signal quality and cross-domain readiness before execution.

## Trigger
Use this gate before:
- publishing a claim, campaign, landing page, post, ad, or outreach sequence;
- handing leads or member/customer signals to Sales;
- launching an experiment that needs IT tracking or Finance budget;
- scaling a promise that Product/Ops must deliver;
- communicating anything Legal-sensitive.

## Output
A dated Growth readiness decision:
- GROWTH_READY
- NEEDS_SIGNAL
- BLOCKED_PROMISE

## Readiness Checks
| Check | Question |
| --- | --- |
| VOC | What evidence says the audience cares? |
| ICP | Who exactly is this for? |
| Promise | What value is promised and what is excluded? |
| Sales handoff | Can Sales receive and act on this signal? |
| Product boundary | Can Product support the promise? |
| Ops feasibility | Can Ops deliver repeatedly? |
| IT tracking | Where is attribution and source of truth? |
| Finance | What is the spend, CAC, or margin boundary? |
| People | Who owns, creates, reviews, and learns? |
| Legal | Are claims, privacy, and compliance safe? |

## Guardrail
No member-facing growth motion may launch without member VOC, activation path, retention loop, and community owner.

## Proof
Attach the Growth packet, VOC evidence, ICP filter, experiment plan, metric, cross-domain approvals, and final Growth decision.