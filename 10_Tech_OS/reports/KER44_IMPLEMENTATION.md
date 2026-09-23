# KER-44: Companion constitution and Dao/Jing projections

Canonical contract: 10_Tech_OS/kernel/COMPANIONS_CONSTITUTION.json.
The lowercase companion_constitution_v2.json is an identical compatibility snapshot.
Nine S3 identities preserve home stewardship and cross-core reach. The typed handoff
loop is Ryan -> Yaz -> Graham -> Bill -> Clara -> Nardole -> Amy -> Rory -> River
-> WorldState -> Ryan. System-1/2 describe cognition, never organizational authority.

## Commands
python -X utf8 10_Tech_OS/kernel/topology_validator.py
python -X utf8 10_Tech_OS/kernel/dao_jing.py --role Rick --work-id 180
python -X utf8 -m unittest discover -s 10_Tech_OS/kernel -p test_ker44_evidence.py -v

Pass --db for an alternate SQLite snapshot and --as-of for repeatable lease evaluation.
Thirteen roles are supported: Rick, Doctor11/12/13, and the nine companions.
Doctor default views use their home layer. Explicit work-id focus can traverse cores.
All SQL reads occur in a single read-only transaction; no schema changes occur.

## Agent OS
GET /api/tech-os/workgraph/projection?role=Rick&work_id=180
The companion parameter is a compatibility alias for role. Invalid role/work-id
returns 400; write methods return 405. The backend calls dao_jing.py with argv,
without a shell. No domain logic is added to the UI. Kernel failure returns 503.

A projection returns at most eight works and 8192 UTF-8 bytes, with omitted_count.
This is a measured byte ceiling, not an estimated token guarantee.
source_snapshot_sha256 identifies the selected source snapshot before omission.
snapshot_sha256 verifies the delivered compact sorted UTF-8 JSON, excluding its
own hash field, after byte-bound omission. hash_contract makes this explicit.
Expired ownership, missing bindings and unsupported done claims are visible drift.
A claim/binding is never reported as executing without a fresh provider observation;
this read-only projection explicitly says execution_observation=not_observed.

## Preservation and validation
Existing ROLE_CONTRACTS*.json files were preserved untouched and copied byte-for-byte
to kernel/backups/ker44-20260923T214045Z before changes. Their truncated legacy
contents are not silently promoted into the canonical constitution.
Focused tests cover invalid topology/authority and mutation-sensitive projections,
byte/cardinality bounds, read-only access and all thirteen roles.
The Node adapter integration test is desktop/tools/test-workgraph-projection.mjs:
node --experimental-strip-types tools/test-workgraph-projection.mjs <absolute-kernel-dir>

This delivers the KER-44 contracts and projection API, not full autonomous Kernel
operation or acceptance of unrelated historical PRs.
