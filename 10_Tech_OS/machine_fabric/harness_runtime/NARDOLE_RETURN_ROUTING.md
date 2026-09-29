# Nardole Dispatch + Return Contract — Harness Runtime

Nardole is the durable router around River/FLOW.

## Dispatch

A dispatch is valid only when:
- canonical work_id exists;
- dependency gates permit execution;
- required capability release exists;
- no conflicting live owner exists;
- lease/fencing token is issued;
- return_route is complete.

Nardole routes by capability/version/availability, not by remembered chat context.
## Return map

Rory verdict -> Nardole route:

ACCEPT_CONTINUE -> NEXT_FLOW or declared next capability
COMPLETE -> DONE / terminal_consumer
RETRY_SAFE -> RETRY under same correlation_id
RECOVER_UNKNOWN -> DONNA
REOPEN_BUILD -> RYAN
REOPEN_DESIGN -> CLARA
HOLD -> WAIT

Nardole creates the next lease only after the previous owner releases or expires.

No verdict can be converted into In Progress without valid claim + lease/binding + fresh worker evidence.
## Retry / backpressure

Retry preserves:
- work_id;
- correlation_id;
- original request/evidence refs;
- prior receipt chain.

Retry gets a new execution/operation identity only when the replay contract requires it.

Backpressure may delay dispatch by not_before/quota/health.
Delay is not failure.

Unresolved dispatch attempts must be reconciled before new dispatch, matching the existing fleet ownership invariant.
## Machine return vs handover

ContinuationEnvelope is the machine return channel.

Markdown handovers and ChatGPT group chats may explain context to humans, but Nardole must never parse them to decide:
- target capability;
- retry;
- terminal completion;
- recovery route;
- reopened cell.

Those decisions come from typed ReconcileDecision + ReturnRoute + current WorkGraph state.
