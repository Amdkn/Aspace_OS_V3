---
type: Concept
title: Enterprise OS Blueprint Kit — single-chokepoint, 42 kill switches, write-once audit S3 Object Lock
description: Kit AWS-spécifique de 53 fichiers (BluePrint + 11 prompts + 8 spec templates + 4 exemples par tier) qui impose l'architecture single-chokepoint runAgentTurn — daté sur AWS pricing 2026, canon sur les patterns abstraits.
tags: [templates, enterprise-os, aws, bedrock, cdk, kill-switches, write-once-audit, single-chokepoint, datation]
generated: { by: minimax-m3, at: 2026-08-19T19:45:00Z }
verified:
  - { by: process:lecture_kit_enterprise_integral, at: 2026-08-19T19:45:00Z }
sources:
  - id: enterprise-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Enterprise_OS_Blueprint_Kit/README.md"
    title: "Enterprise OS Blueprint Kit — README"
    last_modified: 2026-05
  - id: enterprise-blueprint
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Enterprise_OS_Blueprint_Kit/BLUEPRINT.md"
    title: "Enterprise OS — Blueprint (16 sections)"
    last_modified: 2026-05
  - id: enterprise-quickstart
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Enterprise_OS_Blueprint_Kit/QUICKSTART.md"
    title: "Enterprise OS — Quickstart"
    last_modified: 2026-05
  - id: enterprise-checklist
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Enterprise_OS_Blueprint_Kit/CHECKLIST.md"
    title: "Enterprise OS — Build Checklist"
    last_modified: 2026-05
  - id: enterprise-troubleshooting
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Enterprise_OS_Blueprint_Kit/TROUBLESHOOTING.md"
    title: "Enterprise OS — Troubleshooting (10 pièges)"
    last_modified: 2026-05
  - id: enterprise-faq
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Enterprise_OS_Blueprint_Kit/FAQ.md"
    title: "Enterprise OS — FAQ (10 questions)"
    last_modified: 2026-05
  - id: enterprise-specs-listing
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Enterprise_OS_Blueprint_Kit/specs"
    title: "Dossier specs (8 templates : SETUP, SYSTEM, ARCHITECTURE, SECURITY, COST, READINESS, AGENT, BUILD_PLAN)"
    last_modified: 2026-05
  - id: enterprise-examples-listing
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Enterprise_OS_Blueprint_Kit/examples"
    title: "Dossier examples (3 profils : solo-consultant T0, northgate-law T1, riverside-clinic T2)"
    last_modified: 2026-05
okf_version: "0.2"
---

# Enterprise OS Blueprint Kit — single-chokepoint + write-once audit

## Périmètre

53 fichiers : 9 manifestes racine + 11 prompts (`.txt`) en 3 parties + 8 spec templates (8 vides + 8 remplis pour omk-nexus-coaching-agency) + 4 exemples par tier + 3 PDFs.

| Sous-dossier | Fichiers | Rôle |
|---|---|---|
| racine (8 MD) | README, BLUEPRINT, QUICKSTART, CHECKLIST, FAQ, TROUBLESHOOTING, GLOSSARY, COMMANDS, FIRST_SESSION | navigation + théorie |
| `prompts/` | 11 `.txt` (Part A 1-3 setup, Part B 4-7 plan, Part C 8-11 draft & deploy) + `aaarr_growth_signal_pack.md` | prompts copy-paste |
| `specs/` | 8 templates vides + 8 remplis (omk-nexus-coaching-agency) | handoff Claude Code → humain |
| `examples/` | 3 profils (solo-consultant, northgate-law, riverside-clinic) + 1 omk-nexus-coaching-agency | exemples filled-in |

## Verdict

**`synthese-datee`** — daté sur les références AWS mai 2026, canon sur les patterns d'architecture.

**Daté sur :**
- Le pricing AWS 2026 (T0 $65-$95/mois, T1 $130-$180, etc.) — déjà en partie obsolète en août 2026 (Bedrock pricing a évolué).
- Les références à `Amazon Nova Sonic` pour la voix (modèle jeune, peut être discontinué) et `Stability` en us-west-2 only (typage régional AWS).
- Le coût VPC interface endpoints « ~$175/mois » — chiffre rond mai 2026.

**Canon sur :**
- **Single chokepoint** : toute action passe par `runAgentTurn` dans cet ordre strict —
  `rate limit → load agent → Bedrock kill switch → cost cap (fail-closed) → tool switch → guardrail → converse loop → tool dispatch → DLP scan → audit`.
- **Cost cap fails closed** : si le coût du jour ne peut être calculé, on s'arrête plutôt que de laisser les dépenses filer.
- **42 kill switches** : un booléen par comportement dangereux, chacun flipable en `<2s`.
- **Write-once audit trail** : double écriture — copie chaude en DynamoDB + copie en S3 Object Lock (governance mode, 7-year hold). Note explicite : « governance mode is not literally un-deletable; a privileged bypass is possible and is itself logged. »
- **DLP 9 patterns** : 7 à bloquer (AWS keys, API headers, PEM, Slack, GitHub PAT, credit cards, SSNs) + 2 à avertir (AWS-secret-shaped strings, JWTs).
- **IAM least-privilege** : aucune wildcard, pas de master keys.
- **3 customer-managed KMS keys** — retirer une clé rend les données illisibles, même pour AWS.
- **4 rollback classes** : image / infrastructure / config / data.
- **TTL tripwire** : auto-détruit un demi-déploiement abandonné pour ne pas payer.
- **4 tiers (T0 Hobby / T1 Standard / T2 Pro / T3 Enterprise)** qui scalment le task count, log retention, WAF, X-Ray, CloudFront, WORM audit bucket, GuardDuty/Config, daily cap.

## Trace dans V3

**Aucune.** Pas d'artefact A'Space V3 ne porte la marque de ce kit : pas de `cdk.out`, pas de fichier `*-cdk.ts`, pas de tag AWS sur les dépôts. A'Space V3 utilise SQLite local et un orchestrateur Python, pas Bedrock / Fargate / DynamoDB.

C'est un **moule non-deployé** dans V3 — un excellent **référentiel de design** pour qui voudrait héberger un agent OS dans son propre cloud AWS, mais qui n'a pas été le patron retenu.

## Comparaison avec ClaudeClaw Mission Control Kit

Les deux kits partagent les **mêmes patterns abstraits** (kill switches, audit log, three-layer memory, exfiltration guard) mais diffèrent sur le **patron d'isolation** :

| Dimension | ClaudeClaw (local) | Enterprise (AWS) |
|---|---|---|
| Runtime | subprocess Node.js sur la machine locale | Fargate dans VPC privé |
| Données | SQLite sur disque | DynamoDB + S3 + KMS |
| Modèle | Claude Code CLI direct | Amazon Bedrock in-account |
| Audit | SQLite `audit_log` table | DynamoDB chaud + S3 Object Lock froid |
| Coût | abonnement Claude Code | $65-$800/mois infrastructure + $10-$40/mois inference |
| Kill switches | 6 env vars hot-reload | 42 switches + Bedrock kill |
| Bridge | Telegram bot polling | ALB + WAF gated |

Lequel est meilleur ? Aucun — ils répondent à des contextes différents. **Le ClaudeClaw est un kit solo, l'Enterprise est un kit pour firme manipulant des données tier-2 (PHI, légal).**

## Concepts liés

- [[concept-claudeclaw-mission-control-kit]] — le jumeau local
- [[concept-five-cross-cutting-patterns]] — patterns partagés
- [[concept-kits-utilisation-trace]] — trace nulle dans V3
