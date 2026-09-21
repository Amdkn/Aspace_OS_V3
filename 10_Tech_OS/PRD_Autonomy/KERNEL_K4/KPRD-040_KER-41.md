# KPRD-040: LM Studio Local Serving Lifecycle + TTL Policy

## Overview
Productionize the local serving registry for LM Studio to manage GGUF backends effectively. This involves discovery, estimation, load/unload operations, managing context/TTL/resource policies, and providing health evidence for the backends.

## Goals
1. Implement a registry for discovering local GGUF models via LM Studio.
2. Develop a mechanism to load and unload models gracefully.
3. Establish a TTL (Time To Live) policy for loaded models to optimize resource usage.
4. Implement resource estimation and health checks for backends.
5. Provide evidence logging for model lifecycle events.

## Specifications
- The registry should query the LM Studio API to discover available models.
- Model loading/unloading should use the `/v1/models` and `/v1/unload` (or equivalent) endpoints.
- The TTL policy should automatically unload models that haven't been accessed within a specified timeframe (e.g., 5 minutes).
- Health checks should verify the `/v1/models` endpoint for active models.
- Evidence of load, unload, and TTL events should be logged to a predefined sink (e.g., standard output or a log file).

## Constraints
- Do not expand the scope beyond LM Studio lifecycle management.
- Do not modify unrelated domains or authority contracts.
