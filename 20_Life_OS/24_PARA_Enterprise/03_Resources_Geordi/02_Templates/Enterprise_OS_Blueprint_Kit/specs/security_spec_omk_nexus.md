---
type: spec-override
id: SPEC_OMK_SECURITY
title: "SECURITY_SPEC OMK Nexus BOS - DLP-light 7 patterns (Phase 1), 9 patterns (Phase 2)"
status: RATIFIED
date: 2026-07-05T09:45:00-04:00
author: HA
refines: specs/SECURITY_SPEC.md (template canon)
sister: ADR-LD01-011 D2
---

# SECURITY_SPEC - OMK Nexus BOS (override DLP-light subset)

> Override du template canon. Phase 1 = DLP-light 7 patterns minimum (Q1 validee par A0). Phase 2 = DLP complet Blueprint section 6 (9 patterns) des premier client signe.

## Phase 1 - DLP-light (PoC scope)

### 7 patterns a scanner sur **chaque output** des 11 prompts AAARR et du Quiz d'Acquisition

| Pattern | Regex | Action |
|---|---|---|
| AWS access keys | `AKIA[0-9A-Z]{16}` | **BLOCK** + log |
| GitHub PATs | `ghp_[0-9a-zA-Z]{36}` | **BLOCK** + log |
| Slack tokens | `xox[baprs]-[0-9a-zA-Z]+` | **BLOCK** + log |
| PEM private keys | `-----BEGIN .* PRIVATE KEY-----` | **BLOCK** + log |
| Credit cards (Luhn) | `\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}` | **BLOCK** + log |
| US SSNs | `\d{3}-\d{2}-\d{4}` | **BLOCK** + log |
| PII basic (email + phone) | email ET phone | **WARN** + opt-in masking |

### Implementation Phase 1
- Fichier : `dlp_light_filter.py` (middleware Python standalone)
- Input : output de chaque prompt AAARR ou Quiz d'Acquisition (string)
- Output : tuple (cleaned_output, scan_report: dict)
- Action BLOCK : raise `DLPLightViolationError`, write audit, return None
- Action WARN : prepend `PII detected (email/phone masked)`, return masked_output

### Quand le DLP complet arrive (Phase 2)
- Des le premier client signe (Phase 3 per Gemini T2 Sales closing)
- Monte les 9 patterns Blueprint complet (section 6 BLUEPRINT.md) :
  - **Block (7)** : AWS keys, API key headers, private keys, Slack tokens, GitHub PATs, credit cards, US SSNs
  - **Warn (2)** : AWS-secret-key-shaped strings, JWTs
- Conformite EU AI Act : transparence algorithmique, human oversight (A1 Beth), audit trail

## 5 RBAC roles (per Blueprint section 9)
- **viewer** : beta-coachs en early access, read-only sur leur data propre
- **analyst** : beta-coachs avances, peuvent lancer Quiz d'Acquisition pour leurs clients
- **operator** : A0 + Abdaty, operent l'infra, peuvent creer des prospects, generent MANIFEST.md
- **admin** : A0 seul, configure les prompts, monte le DLP complet, kill switches
- **owner** : A0 (single point), veto absolu sur toute action definitive

## Kill switches (Blueprint section 6 = 42 switches ; Phase 1 subset 8)
1. **Kill AAARR scrapers** (if scraping abuse detected)
2. **Kill Quiz d'Acquisition** (if Quiz defect)
3. **Kill Telegram bot** (if bot malfunction)
4. **Kill Bedrock calls** (if cost cap approaching)
5. **Kill DLP-light filter** (= block ALL outputs until restored)
6. **Kill MiniMax plan fallback** (= switch to local-only models)
7. **Kill MANIFEST.md writes** (= freeze projects)
8. **Kill audit log reads** (= privacy lockdown)

## IAM least-privilege (Phase 1 minimal)
- Each agent IAM role scoped to **only** its DynamoDB tables + S3 buckets
- No wildcard policies anywhere
- Secrets in AWS Secrets Manager (rotated 90j)
- Bedrock invoke only, no admin
- DLP-light filter role: Read inputs + Write audit log only

## Audit trail (WORM 7-year hold, per Blueprint section 6)
- Every action dual-written: hot copy in DynamoDB + write-once S3 Object Lock
- Governance mode (not compliance - governance allows privileged bypass, logged)
- Break-glass events (panic, auth failures, role changes) always audited
- Suppression elle-meme laisse une marker ("audit_disabled_marker" row)
