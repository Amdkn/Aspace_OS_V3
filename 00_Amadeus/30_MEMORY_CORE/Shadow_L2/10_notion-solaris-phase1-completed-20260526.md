# Shadow L2 — Notion Solaris Phase 1 COMPLETED + ID Reference

**Date :** 2026-05-26 (session de fin)
**Niveau :** L2 Business OS
**Sources doctrinales :** ADR-NOTION-001 + Shadow_L2/09 (bootstrap plan)
**Status Phase 1 :** ✅ COMPLETED — workspace Notion vivant, MASTER_SOP_DB dense

---

## Bilan exécution Phase 1

| Étape ADR-NOTION-001 plan | Status | Volumétrie |
|---------------------------|--------|------------|
| 1. Top-level `Solaris HQ` | ✅ | 1 page (icon ☀️ + 5 sections + 8 portails listés) |
| 2. `MASTER_SOP_DB` (14 props) | ✅ | 1 DB, 38 rows (Draft × 37 + Active × 0) |
| 3. 8 portails domaines | ✅ | 8 sub-pages enrichies (mission, SOPs, KPIs, anti-patterns) |
| 4. `AGENT_REGISTRY_DB` (8 props) | ✅ | 1 DB, 8 rows enrichies (lore, members, stack, SOPs) |
| 5. 3 SOPs P0 test | ✅ | 3 initiales + 35 ajoutées = 38 total |

**Total** : 1 top page + 8 portail pages + 2 databases + 8 squads + 38 SOPs = **57 entries Notion** dans `Business Pulse ∞ AMADEUS`.

## ID Reference (canonique pour Phase 2)

### Workspace & Top
- **Workspace** : `Business Pulse ∞ AMADEUS`
- **Solaris HQ** (top page) : `36c7e9e2-658c-8185-bd87-e76c9f5360b6` — https://www.notion.so/36c7e9e2658c8185bd87e76c9f5360b6

### Databases
- **MASTER_SOP_DB** : `6b07315e-06ca-4652-9049-d72a1e79e906`
  - data_source_id : `4327f922-cc79-4f9f-ae29-9157057d34d5`
- **AGENT_REGISTRY_DB** : `d46826d5-ce3c-4c92-96b9-f50e4cc38795`
  - data_source_id : `e9f082b5-1099-4cf6-943c-0fa7fdb0fc68`

### 8 Portails domaines (sub-pages Solaris HQ)
| Domaine | Page ID |
|---------|---------|
| 01 Growth · Superman · Guardians | `36c7e9e2-658c-81ec-b10a-e987543524a3` |
| 02 Sales · John Jones · Illuminati | `36c7e9e2-658c-8155-beb1-c6d25015c03c` |
| 03 Product · Flash · Avengers | `36c7e9e2-658c-817b-ae64-f7d2a68600b7` |
| 04 Ops · Batman · Fantastic4 | `36c7e9e2-658c-818b-87f5-f60e53047660` |
| 05 IT · Cyborg · KangDynasty | `36c7e9e2-658c-8160-a139-e2c9eeb037dd` |
| 06 Finance · Wonder Woman · Thunderbolts | `36c7e9e2-658c-812a-ac29-c4952530d433` |
| 07 People · Green Lantern · XMen | `36c7e9e2-658c-8114-9c90-fb2ff1751716` |
| 08 Legal · Aquaman · Eternals | `36c7e9e2-658c-8186-8712-efa09e024150` |

### 8 Squads (AGENT_REGISTRY_DB rows)
| Squad | Row ID |
|-------|--------|
| Guardians | `36c7e9e2-658c-81dc-b958-f473bb806c4d` |
| Illuminati | `36c7e9e2-658c-814f-a15b-fce26e0de283` |
| Avengers | `36c7e9e2-658c-81ba-b05e-fcfa153cf957` |
| Fantastic4 | `36c7e9e2-658c-81f4-980f-eedb977edbb5` |
| KangDynasty | `36c7e9e2-658c-81aa-91b5-e9be3cedcb52` |
| Thunderbolts | `36c7e9e2-658c-81f7-a3e9-c2d65a13626f` |
| XMen | `36c7e9e2-658c-810e-905a-c108e9839bb2` |
| Eternals | `36c7e9e2-658c-81ce-ac4b-f5337b9affb3` |

### 38 SOPs MASTER_SOP_DB (par domaine)

**Growth (5)** — Numbers 1-5, Owner Superman, Executor Guardians
1. `36c7e9e2-658c-81b6-8540-c45e4a56a97f` (Provision VPS Nexus — *attente: en réalité c'est IT-001, voir IT*)
2. Publish LinkedIn Personal Brand Post · `36c7e9e2-658c-8172-b6e0-d043980480c3`
3. Apollo Outbound Sequence Launch · `36c7e9e2-658c-81a8-9d62-d8b3231d6bf1`
4. Landing Page A/B Test · `36c7e9e2-658c-816d-bcfc-f2397fc84db0`
5. Weekly CPQL Calculation · `36c7e9e2-658c-8131-945a-e2a818f8cd4d`
6. Publish SEO Blog Article · `36c7e9e2-658c-8119-ba09-f1a73bec46c6`

**Sales (5)** — Owner JohnJones, Executor Illuminati
- SALES-001 Qualify Inbound Lead · `36c7e9e2-658c-8125-98b9-d542466b2894` (créée Phase 1 initial)
- SALES-002 Conduct Solaris Nexus Demo · `36c7e9e2-658c-8131-80f4-c634aa8e77a5`
- SALES-003 Generate Proposal PandaDoc · `36c7e9e2-658c-8199-beee-e916da61ac46`
- SALES-004 Negotiate & Close Deal · `36c7e9e2-658c-8138-bf5c-e01a857798b0`
- SALES-005 Postmortem Deal Lost · `36c7e9e2-658c-815f-a863-feb48291f9a7`

**Product (5)** — Owner Flash, Executor Avengers
- PRODUCT-001 Write New Feature PRD · `36c7e9e2-658c-81c4-8d4e-c6213a2fa546`
- PRODUCT-002 Solaris Bi-Weekly Release Notes · `36c7e9e2-658c-81a1-819f-cbfcde29aff4`
- PRODUCT-003 Bug Triage P0 P1 P2 P3 · `36c7e9e2-658c-815e-8511-daeab4d00414`
- PRODUCT-004 User Research Interview · `36c7e9e2-658c-8163-abfd-e904bacb27b6`
- PRODUCT-005 Feature A B Test · `36c7e9e2-658c-818d-9b29-fbe870c4d3ed`

**Ops (4)** — Owner Batman, Executor Fantastic4
- OPS-001 Onboard New Nexus Client · `36c7e9e2-658c-816c-a0e3-d6a871c3150a`
- OPS-002 Weekly System Health Check · `36c7e9e2-658c-818a-b019-ccb6c21b64c5`
- OPS-003 Incident Postmortem · `36c7e9e2-658c-81d0-a2d3-fe01cf929904`
- OPS-004 Quarterly SOP Audit · `36c7e9e2-658c-812d-9d4e-d0d72e4dafec`

**IT (5)** — Owner Cyborg, Executor KangDynasty
- IT-001 Provision VPS Nexus · `36c7e9e2-658c-81b6-8540-c45e4a56a97f` (créée Phase 1 initial)
- IT-002 Deploy Solaris Instance via Dokploy · `36c7e9e2-658c-8186-b01d-e414fd86ed81`
- IT-003 Rotate Hostinger API Keys · `36c7e9e2-658c-81f2-ba42-eafc6dc260b8`
- IT-004 VPS Backup Snapshot · `36c7e9e2-658c-8105-afab-cbd24a377e3e`
- IT-005 Disaster Recovery Restore · `36c7e9e2-658c-812e-9a00-c2461dbb1d8b`

**Finance (5)** — Owner WonderWoman, Executor Thunderbolts
- FINANCE-001 Send Invoice Stripe · `36c7e9e2-658c-8123-bbbb-d07fe7084d57` (créée Phase 1 initial)
- FINANCE-002 Monthly MRR Reconciliation · `36c7e9e2-658c-813b-a806-fc04605a0ac5`
- FINANCE-003 Quarterly Margin Analysis · `36c7e9e2-658c-819a-b13f-e1f86d062551`
- FINANCE-004 Annual Tax Filing Checklist · `36c7e9e2-658c-8159-b5a1-e4392c4018ca`
- FINANCE-005 Overdue Invoice Escalation · `36c7e9e2-658c-81a6-a2a3-d299278c0bff`

**People (5)** — Owner GreenLantern, Executor XMen
- PEOPLE-001 Onboard New Agent Capsule · `36c7e9e2-658c-81e7-b06f-c9ba927a5081`
- PEOPLE-002 Weekly Agent Performance Review · `36c7e9e2-658c-81b3-a8e9-d1a401dd3b00`
- PEOPLE-003 Quarterly Ethics Audit · `36c7e9e2-658c-8165-b598-d2ca8a11adad`
- PEOPLE-004 Decommission Deprecated Agent · `36c7e9e2-658c-8128-b1e6-e5d72d98bdd3`
- PEOPLE-005 Skill Registry Update · `36c7e9e2-658c-8108-b29f-ff670c4e84c4`

**Legal (4)** — Owner Aquaman, Executor Eternals
- LEGAL-001 New Client Contract Signing · `36c7e9e2-658c-81ff-adb5-f730ba099506`
- LEGAL-002 Quarterly RGPD Compliance Audit · `36c7e9e2-658c-8199-af23-e082365d8be2`
- LEGAL-003 IP Filing and Renewal Trademarks · `36c7e9e2-658c-813e-8e10-c217dba125e0`
- LEGAL-004 DPA Breach Notification · `36c7e9e2-658c-814e-9349-c5d332969b3e`

## Reste manuel UI (avant Phase 2)

1. **Linked DB Views filtrées** — `/linked` dans chaque portail → MASTER_SOP_DB → filtrer Domain (8 × 30s)
2. **SOP_ID formula** — Add property Formula sur MASTER_SOP_DB : `"SOP-L2-" + prop("Domain") + "-" + format(prop("Number"))`
3. **Embed DBs dans Solaris HQ** — `/linked` sous "📚 Bibliothèque SOPs TVR" et "🧬 Hall des Agents"
4. **Vues** : Par Domaine (Kanban groupBy Domain) · Active uniquement (filter Status=Active) · À auditer (filter Last_Audited<30j OR null)

Estimation : **15-20 min de finition UI**.

## Promotion Draft → Active : critère

Avant qu'une SOP passe `Draft → Active`, **Build_Gate doit avoir été testée au moins 1 fois**. C'est la doctrine ADR-NOTION-001 §D4 ("Batman refuse les SOPs floues"). Tant que pas testée, statut Draft.

Suggestion : 1 SOP par domaine à activer cette semaine, choisie selon priorité business (ex: SALES-001 Qualify Lead + FINANCE-001 Send Invoice + IT-001 Provision VPS).

## Phase 2 (à venir, bloquée sur ADR-SYMPH cluster impl)

Sync Notion → Supabase :
- Listener sur MASTER_SOP_DB changes (Notion webhook → PM2 worker)
- Push SOPs `Active` vers Supabase table `sops`
- Skill : `Shadow_L0/agents/Claude_Code_CLI/skills/sync-notion-to-supabase.ps1` (Phase 1 cluster A2 = AntiPanicGuards.psm1 doit être codée d'abord)

## Références

- ADR-NOTION-001 (canon)
- Shadow_L2/09 (bootstrap plan)
- Handoff `handoff_20260526_notion-solaris-bootstrap.md`
- ADR-SYMPH-001 + HEART-002 (cluster bloquant Phase 2)
- ADR-INFRA-001 (PM2 VPS pour Phase 2 prod sync)
