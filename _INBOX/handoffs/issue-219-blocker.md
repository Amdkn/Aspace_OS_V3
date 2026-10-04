# Issue 219: [DC-SOVEREIGN][RELEASE] v1 Cutover — A'Space DC becomes primary machine gateway

## Blocker Reason
The remaining tasks for issue #219 involve human-only physical/local access and actions that cannot be executed in the autonomous AI environment. Specifically:

- **Host Environment Execution**: Connecting a real client, running the A'Space DC natively on Windows (`Amd-PC`), and verifying behavior under `C:\Users\amado\...`.
- **Irreversible External Action**: Publishing release artifacts and cutting over the primary machine gateway, which involves changing the user's primary operating system environment.

## Required Human Actions
To resolve this issue and perform the cutover, a human operator must:

1. Clean install/start A'Space DC on the local Windows host.
2. Verify normal Chrome and Native Host interactions on the host.
3. Validate one MCP endpoint and restart/replay capabilities.
4. Verify remote second client connectivity.
5. Verify rollback/uninstall.
6. Publish the release artifact/version.
7. Run the golden canary suite and persist receipts/evidence to close out the objective #194 and epic #197.

## Relevant Links
- [Issue #219](https://github.com/Amdkn/Aspace_OS_V3/issues/219)