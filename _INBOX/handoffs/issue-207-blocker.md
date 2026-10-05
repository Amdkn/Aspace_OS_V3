# [BLOCKER] Issue #207 - Discover AI Corpus 01 GWS Replay

I am attempting to execute GitHub issue #207 (`[BILL-RD][CORPUS-01][BUILD] Discovery AI — papers + transcripts + captures + GWS Sheets`).

The issue states:
> M8 — local authenticated GWS full-corpus replay + counts/dedup/provenance proof

## Blocker Reason
Executing the full corpus harvest and writing the payloads to the operational Google Spreadsheet (`1lqI1uJhqK9K45kibmZzpKTrnI5VHiAxSLu20RU3zTA0`) requires the authenticated `gws` CLI. This requires human-only authorization and involves irreversible external actions (mutating the Google Spreadsheet). As an agent, I cannot authenticate or safely execute this operational projection in a sandbox.

## Required Resolution
A human operator must run the pipeline locally with their authenticated GWS CLI to execute M8, prove the postconditions, and complete the full-corpus replay.
