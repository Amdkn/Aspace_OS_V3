# AAAS B2/B3 Systems Access Protocol

## Systems Packet
Every B2/B3 task that touches a tool, record, automation, repository, account, or data path must carry this packet:

`yaml
project: 00 Agency as a Service
b2_domain:
b2_owner:
b3_agent:
system_or_tool:
source_of_truth:
access_owner:
permissions_needed:
data_boundary:
automation_boundary:
support_owner:
rollback_path:
proof_required:
status:
`

## Assignment Rules
| Rule | Standard |
| --- | --- |
| One system owner | Every tool or runtime has one accountable owner |
| One access owner | Permissions are approved and revocable |
| One source of truth | Records do not scatter across hidden locations |
| One support path | Users/agents know where failure goes |
| One rollback path | Changes can be paused, reverted, or quarantined |

## Refusal Conditions
IT blocks execution when:
- tool owner is missing;
- access boundary is unclear;
- client/member/childcare/entity/finance/legal data path is vague;
- automation can act without approval where approval is required;
- there is no support or rollback path;
- a B3 agent needs credentials or permissions without People owner approval.

## Output
IT emits one of three states:
- SYSTEM_READY: B3 can execute within the named boundary.
- NEEDS_SYSTEM_OWNER: return to B2/People for ownership.
- QUARANTINE: route to Donna/DLQ because the system, data, or access path is unsafe.