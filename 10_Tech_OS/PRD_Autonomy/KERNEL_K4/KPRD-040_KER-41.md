# KPRD-040: LM Studio local serving lifecycle + TTL policy
## Scope
Productionize local serving registry: discovery, estimate, load/unload, context/TTL/resource policy and health evidence for GGUF backends.

## Owner
Kernel Core

## Dependencies
None

## Acceptance
- `LMStudioRegistry` handles discovery via `/v1/models`
- Models can be logically loaded and unloaded.
- A TTL policy is enforced.
- Health checks return True if available.

## Evidence
- `10_Tech_OS/kernel/slm/test_lm_studio_registry.py` verifies all functionality.

## Exclusive Files
- `10_Tech_OS/kernel/slm/lm_studio_registry.py`
- `10_Tech_OS/kernel/slm/test_lm_studio_registry.py`
