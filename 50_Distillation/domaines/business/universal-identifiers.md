---
type: Concept
title: Identifiants universels — SOP_ID, CLIENT_ID, BRIEF_ID et autres
description: Les conventions ADR-ID-001 pour qu'un identifiant survive aux migrations, refactorings, changements de plateforme. Préfixes sémantiques, slugs courts, immutabilité à vie.
tags: [identifiants, sop-id, client-id, brief-id, adr-id-001, conventions]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: ADR-ID-001
    resource: "30_Business_OS/09_Blueprints/02-ADR/ADR-ID-001_identifiants-universels.md"
    title: ADR-ID-001 — Conventions Identifiants Universels Tri-Plateforme
    last_modified: "2026-05-27"
  - id: client-onboarding-kit
    resource: "30_Business_OS/09_Blueprints/03-ONBOARDING/client-onboarding-kit-v1.md"
    title: Client Onboarding Kit v1 — Solaris Nexus Agency
    last_modified: "2026-05-27"
okf_version: "0.2"
---

# Identifiants universels — SOP_ID, CLIENT_ID, BRIEF_ID et autres

> **Une seule chose à retenir.** Tout identifiant qui traverse au moins 2 plateformes (Notion, ClickUp, Airtable) suit un préfixe sémantique canonique (`SOP_ID`, `CLIENT_ID`, `BRIEF_ID`, etc.), un slug court, et l'**immutabilité à vie**.

## Énoncé canonique (ADR-ID-001 §D1)

| ID          | Pattern                                       | Source de vérité          | Exemple                              |
|-------------|-----------------------------------------------|---------------------------|--------------------------------------|
| `SOP_ID`    | `SOP-L2-{DOMAIN}-{NN}`                        | Notion `MASTER_SOP_DB`    | `SOP-L2-SALES-001`                   |
| `SQUAD_ID`  | `SQUAD-{NAME}`                                | Notion `AGENT_REGISTRY_DB`| `SQUAD-Illuminati`                   |
| `CLIENT_ID` | `CL-{slug-agence}`                            | Airtable 🌞 Clients       | `CL-acme-corp`                       |
| `BRIEF_ID`  | `BR-{CLIENT_ID}-{YYYYMMDD}-{NN}`              | Airtable 🦇 Briefs        | `BR-CL-acme-corp-20260527-01`        |
| `ASSET_ID`  | `AS-{BRIEF_ID}-{NN}`                          | Airtable ⚡ Assets        | `AS-BR-CL-acme-corp-20260527-01-03`  |
| `LEAD_ID`   | `LD-{slug-agence}-{YYYYMM}`                   | Airtable 🦸 Leads         | `LD-acme-corp-202605`                |
| `DEAL_ID`   | `DL-{CLIENT_ID}-{NN}`                         | Airtable 💸 Sales Pipeline| `DL-CL-acme-corp-01`                 |
| `INVOICE_ID`| `INV-{CLIENT_ID}-{YYYYMM}`                    | Airtable 🛡️ Finance       | `INV-CL-acme-corp-202605`            |
| `KB_ID`     | `KB-{CLIENT_ID}-{NN}`                         | Airtable 🏮 Knowledge     | `KB-CL-acme-corp-01`                 |
| `INFRA_ID`  | `IN-{CLIENT_ID}-{TYPE}`                       | Airtable 🤖 Infra         | `IN-CL-acme-corp-s3bucket`           |
| `LEGAL_ID`  | `LG-{CLIENT_ID}-{TYPE}-{NN}`                  | Airtable 🔱 Compliance    | `LG-CL-acme-corp-DPA-01`             |
| `TASK_ID`   | natif ClickUp `9014...`                       | ClickUp tasks (URL)       | `9014167...` (non-doctrinal)         |

## Règles de slug

- ASCII uniquement, lowercase.
- Mots séparés par tirets (`-`), pas d'underscores.
- Max 24 caractères (économise l'écran ClickUp).
- Pas de chiffres en début.
- Unicité vérifiée à la création (Airtable formule + alerte).

## Domaines canoniques (D3)

| Code court | Squad              |
|------------|--------------------|
| `GROWTH`   | Guardians          |
| `SALES`    | Illuminati         |
| `PRODUCT`  | Avengers           |
| `OPS`      | Fantastic4         |
| `IT`       | KangDynasty        |
| `FINANCE`  | Thunderbolts       |
| `PEOPLE`   | XMen               |
| `LEGAL`    | Eternals           |

Pas de domaine custom sans création préalable d'un `ADR-NOTION-00X`.

## Numération NN

- Toujours sur 2 chiffres minimum (`01`, `02`, … `99`).
- Si dépassement > 99 dans un sous-ensemble, refactor du namespace — signal de stress doctrinal.
- Pas de réutilisation après archivage (un ID archivé garde son numéro à vie).

## Le titre ClickUp canonique

```
[SOP-L2-{DOMAIN}-{NN}] {CLIENT_ID} — {action courte impérative}
```

Exemples réels lus dans `client-onboarding-kit-v1.md` :
- `[SOP-L2-SALES-001] CL-acme-corp — Qualifier lead inbound`
- `[SOP-L2-FINANCE-001] CL-acme-corp — Émettre invoice Stripe février`
- `[SOP-L2-IT-002] CL-acme-corp — Déployer instance Solaris via Dokploy`

## Immutabilité (D7)

> Une fois assigné, un ID **ne change jamais**. Renommer un client → garder l'ancien `CLIENT_ID`, ajouter un champ `Display_Name`. (`ADR-ID-001` §D7)

## Anti-patterns

- ❌ Slugs avec espaces, majuscules, ou caractères spéciaux.
- ❌ Réutilisation d'un numéro archivé.
- ❌ IDs basés sur des hash (illisibles, impossibles à débugger).
- ❌ Préfixes redondants (`CL-CL-...`).
- ❌ Mix de langues dans les codes (toujours anglais : `LEGAL` pas `JURIDIQUE`).

## Conséquence opérationnelle

Un `CLIENT_ID` qui change casse toutes les références croisées — la perte est en O(N) sur l'ensemble du mesh. La règle D7 (immutabilité) est la protection. Le jour où un client change de nom commercial, on **ajoute** un champ `Display_Name`, on ne touche pas l'ID.
