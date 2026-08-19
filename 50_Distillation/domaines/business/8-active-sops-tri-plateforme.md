---
type: Concept
title: 8 Active SOPs tri-plateforme — le vrai Build Gate
description: Les 8 SOPs (une par SOB) qui sont activées par le Client Onboarding Kit v1. Le vrai Build Gate doctrinal n'est pas unitaire : c'est l'exercice des 8 SOPs en réel sur un onboarding client.
tags: [sop, build-gate, onboarding, 8-sops, tri-plateforme]
generated: { by: minimax-m3, at: 2026-08-19 }
verified:
  - { by: process:lecture-directe, at: 2026-08-19 }
sources:
  - id: client-onboarding-kit
    resource: "30_Business_OS/09_Blueprints/03-ONBOARDING/client-onboarding-kit-v1.md"
    title: Client Onboarding Kit v1 — Solaris Nexus Agency
    last_modified: "2026-05-27"
  - id: ADR-NOTION-001
    resource: "30_Business_OS/09_Blueprints/02-ADR/ADR-NOTION-001_back-office-solaris-template.md"
    title: ADR-NOTION-001 — Notion Back Office Solaris Prototype
    last_modified: "2026-05-26"
okf_version: "0.2"
---

# 8 Active SOPs tri-plateforme — le vrai Build Gate

> **Une seule chose à retenir.** Le vrai **Build Gate** doctrinal n'est pas la rédaction d'une SOP en isolation. C'est l'exercice des **8 SOPs en réel** sur un onboarding client. Une SOP qui n'a pas été exercée n'est pas `Active` ; elle reste `Draft`.

## Énoncé canonique (ADR-NOTION-001 §D4 + Client Onboarding Kit § "Sortie attendue")

> Règle d'or : une SOP qui ne peut pas être exécutée par un agent B3 sans clarification humaine est `Draft`, jamais `Active`. Batman refuse les SOPs floues. (`ADR-NOTION-001` §D4)
>
> À la fin de cet onboarding, **les 8 SOPs Active** ont été exercées au moins 1 fois en réel. C'est le **vrai Build_Gate** doctrinal. Mettre à jour Notion `Build_Gate` field avec : "Tested via onboarding {CLIENT_ID} on {date} — see Airtable CL-{slug}". (`client-onboarding-kit-v1.md` § "Sortie attendue end-to-end")

## Les 8 SOPs exercées dans l'ordre d'onboarding

| Étape | Squad déclenchant    | SOP_ID canonique       | Action                                                    |
|-------|---------------------|------------------------|-----------------------------------------------------------|
| 1     | Fantastic4 (Ops)    | (OPS-001 implicite)    | Créer record Airtable 🌞 Clients & Workspaces            |
| 2     | KangDynasty (IT)    | `[SOP-L2-IT-001]`      | Provision VPS Nexus instance (S3 bucket, Dokploy, Supabase, domaine) |
| 3     | XMen (People)       | `[SOP-L2-PEOPLE-001]`  | Vectoriser Brand Book + créer Context Pack                |
| 4     | Illuminati (Sales)  | `[SOP-L2-SALES-001]`   | Qualifier lead inbound + audit margin bleed              |
| 5     | Eternals (Legal)    | `[SOP-L2-LEGAL-001]`   | Préparer contrat client + DPA                              |
| 6     | Thunderbolts (Finance)| `[SOP-L2-FINANCE-001]`| Émettre invoice Stripe setup fee + M1                      |
| 7     | Guardians (Growth)  | `[SOP-L2-GROWTH-001]`  | Publier post personnal branding fondateur agence        |
| 8     | Avengers (Product)  | (cascade S2-4 → S3-5 / S3-6) | Premier brief Build-Gate validé, premier livrable Factory produit |

> L'étape 9 ajoute Bug Triage (SOP-L2-PRODUCT-003) si un bug est rapporté pendant l'onboarding, task ClickUp avec sévérité P0/P1/P2/P3.

## Le pipeline canonique déclenché

```
1. OPS-001    → Airtable 🌞 Clients & Workspaces (record + CLIENT_ID)
2. IT-001     → ClickUp S3-8 + Airtable 🤖 Infra & Media Logs (S3 bucket, Dokploy, Supabase, domaine)
3. PEOPLE-001 → Airtable 🏮 Knowledge & Brand Books (vectorisation + Context Pack)
4. SALES-001  → Airtable 🦸 Leads & Audits → 💸 Sales Pipeline (DL-{slug}-01)
5. LEGAL-001  → Airtable 🔱 Compliance & Contrats (LG-CL-{slug}-MSA-01 + DPA-01)
6. FINANCE-001→ Airtable 🛡️ Finance & Compute (INV-CL-{slug}-{YYYYMM})
7. GROWTH-001 → ClickUp S2-1 Publish LinkedIn Personal Brand Post
8. PRODUCT-003 (si bug) → ClickUp dédié sévérité
```

## Le statut 100% onboarding (checklist)

- [ ] Record 🌞 Clients & Workspaces créé, CLIENT_ID assigné
- [ ] Infra provisionnée (S3 + Solaris instance + Supabase schema + domaine)
- [ ] Brand Book vectorisé + Context Pack créé
- [ ] Contrats MSA + DPA signés
- [ ] Première facture émise + paiement reçu
- [ ] Premier brief Build-Gate validé
- [ ] Premier livrable Factory produit
- [ ] Portail Space Agent accessible au client
- [ ] `Taux de Complétion Onboarding` = 100%
- [ ] `Statut du Compte` passé de "Onboarding" à "Active"

## Le vrai Build Gate n'est pas unitaire

> C'est l'exercice des 8 SOPs en réel sur un onboarding client. Mettre à jour Notion `Build_Gate` field avec : "Tested via onboarding {CLIENT_ID} on {date} — see Airtable CL-{slug}". (`client-onboarding-kit-v1.md` § "Sortie attendue")

Une SOP isolée, même validée par un Loom 5 min, **n'est pas Active** au sens canon. Active = exercée en production sur un tenant.

## Ce que ce n'est pas

- Pas un test unitaire. Une SOP qui passe un Loom + un Loom_URL reste `Draft` si elle n'a pas été exercée.
- Pas un livrable marketing. Le `Build_Gate` field n'est pas un badge ; c'est un pointeur vers Airtable.
- Pas une checklist interne. La checklist 100% est l'aval ; le Build Gate est l'amont.

## Conséquence opérationnelle

Une SOP qui n'a pas été exercée sur au moins un onboarding **doit être marquée `Under_Audit`** dans Notion `MASTER_SOP_DB` (champ `Status`). Batman (B2 Ops) refuse les statuts `Active` non justifiés.
