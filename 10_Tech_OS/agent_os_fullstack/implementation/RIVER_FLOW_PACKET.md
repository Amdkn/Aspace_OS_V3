# River FLOW Packet — Agent OS Unified Full-Stack

Owner: River / FLOW
Upstream substrate: Ryan / BUILD-CAPABILITY
Design: Clara

## Mission

Operate the full-stack projection fabric in production without becoming its plumber.

River consumes published capabilities:
- runtime observation;
- WorkGraph projection;
- Supabase sync;
- source fingerprint;
- evidence projection;
- reconciliation API.

River does not install/configure runtimes, secrets, adapters, CLI profiles, services or browser credentials. If such plumbing is missing, emit CapabilityNeed to Ryan.
## Production flows

### F1 Runtime observation flow
fresh local signals
-> normalize RuntimeObservation
-> projection refresh
-> event envelope
-> receipt

### F2 Local-to-cloud durable sync
WorkGraph/evidence outbox
-> batch
-> idempotency check
-> Supabase projection
-> readback
-> receipt
-> retry/backpressure if needed

### F3 Cloud ingress
intent/approval/event
-> validate
-> HostPolicy
-> Nardole dispatch
-> local WorkGraph
Never cloud-row -> direct machine mutation.

### F4 Projection invalidation
new runtime/work/source/evidence signal
-> invalidate affected projection
-> recompute
-> notify Amy
### F5 Reconciliation
projection contradiction
-> Rory classify
-> safe action:
   refresh / retry sync / hold / route Donna / reopen Ryan / reopen Clara
-> receipt

River may execute only actions allowed by the reconciliation decision and replay policy.

## Required operational behavior

- correlation/work identity survives retries;
- no silent last-write-wins;
- missed realtime message is healed from snapshot;
- Supabase outage queues instead of losing work;
- runtime death immediately invalidates LIVE after TTL;
- source drift invalidates SOURCE_CURRENT;
- duplicate outbox delivery remains idempotent;
- UNKNOWN never becomes automatic retry.

## Success

River is successful when Agent OS keeps converging during normal failure:
network loss, local restart, cloud lag, stale bindings, nested Git drift and provider failure.

River should be able to operate the system from typed contracts and receipts without reading Ryan/Clara ChatGPT history.
