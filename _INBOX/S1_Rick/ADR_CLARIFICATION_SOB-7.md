# ADR CLARIFICATION: SOB-7 / FPRD-020

## Issue
The mandate requests execution of FPRD-020 for SOB-7, which requires reading the PRD brief at `10_Tech_OS/PRD_Autonomy/FORGE_F2/FPRD-020_SOB-7.md`.

## Problem
- The directory `10_Tech_OS/PRD_Autonomy/` and the file `FPRD-020_SOB-7.md` do not exist in the codebase.
- The `prd_compiler.py` script mentioned in memory for generating PRDs is also missing from `10_Tech_OS/kernel/`.

## Resolution
The requirements are materially ambiguous and blocked by missing files. As per rules: "If requirements are materially ambiguous or need human interaction, STOP implementation and propose an ADR clarification for the Doctor/Rick review path."

Implementation STOPPED. Review required.
