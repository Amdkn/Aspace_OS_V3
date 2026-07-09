# AAAS B2/B3 Growth Experiment Protocol

## Growth Packet
Every Growth task or experiment must carry this packet before B3 execution:

`yaml
project: 00 Agency as a Service
codename: SOLARIS
b2_owner: Superman
b3_swarm: Guardians of the Galaxy
audience:
voc_evidence:
icp_filter:
promise:
channel:
experiment:
metric:
budget_or_time_cap:
sales_handoff:
product_boundary:
ops_feasibility:
it_tracking:
finance_boundary:
people_owner:
legal_review:
status:
`

## Assignment Rules
| Rule | Standard |
| --- | --- |
| Evidence first | VOC or signal must exist before claim writing |
| One audience | Each experiment targets one ICP segment |
| One promise | The promise must map to a deliverable and boundary |
| One metric | Every experiment has a success/failure measure |
| One owner | Growth owner and reviewer are named |
| One learning loop | Experiment ends with keep/kill/change decision |

## Refusal Conditions
Growth blocks execution when:
- VOC evidence is absent;
- ICP is too broad;
- promise exceeds Product/Ops capacity;
- tracking source of truth is missing;
- budget or time cap is missing;
- legal/compliance-sensitive claim is unreviewed;
- Sales cannot receive or handle the lead/member/customer signal.

## Output
Growth emits one of three states:
- GROWTH_READY: B3 can run the experiment.
- NEEDS_SIGNAL: return to VOC/ICP extraction.
- BLOCKED_PROMISE: return to Product/Ops/Legal/Finance for boundary repair.