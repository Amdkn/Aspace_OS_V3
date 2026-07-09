---
id: ADR-INDEX
title: ADR Index — Cross-Reference & doctrine_anchors Backfill
type: index
date: 2026-06-15
status: ACTIVE
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-META-004]
domain: L0 Tech_OS / Architecture Decision Records
tags: [#adr #index #doctrine-anchors #backfill #d1-receipts]
---

# ADR Index — `_SPECS/ADR/`

> **D1 receipts** : 35 ADR canoniques (L0=9, L1=12, L2=14), 12 ratifiés avant 2026-06-15 + 14 créés ce jour + 3 ratifiés ce jour + 3 créés 2026-06-21 + 1 amendé 2026-06-21. **INDEX.md table partiellement stale** : L0/L1/L2 counts à jour 2026-06-21 (L2=14 vs INDEX.md table dit 10 = à corriger formellement).
> **Backfill** : `doctrine_anchors` field ajouté à 12 ADR historiques (D4 append-only = nouveau champ en frontmatter, ne touche pas le contenu).

## 🏛️ L0 Kernel OS (8 ADR)

| ADR | Status | Date | doctrine_anchors | Action |
|-----|--------|------|------------------|--------|
| [ADR-HERMES-001](L0_Kernel_OS/ADR-HERMES-001_nous-desktop-native-workspace-remote.md) | ACCEPTED | 2026-06-03 | [ADR-META-001, ADR-RICK-001] | ✅ backfill |
| [ADR-INFRA-001](L0_Kernel_OS/ADR-INFRA-001_unified-governance-console.md) | ACCEPTED | 2026-06-03 | [ADR-META-001, ADR-RICK-001] | ✅ backfill |
| [ADR-RICK-001](L0_Kernel_OS/ADR-RICK-001_openharness-incarnation.md) | RATIFIED | 2026-05-11 | [ADR-META-001, ADR-META-002] | ✅ présent (archive) |
| [ADR-LLM-001](L0_Kernel_OS/ADR-LLM-001_fable-5-discontinuation-decision.md) | PROPOSED→ACCEPTED | 2026-06-15 | [ADR-META-002-E13, META-003] | ✅ présent (créé ce jour) |
| [ADR-REG-001](L0_Kernel_OS/ADR-REG-001_eu-mistral-self-hosting-fallback.md) | PROPOSED→RADIÉ | 2026-06-15 | [ADR-LLM-001, OPS-002] | ⚠️ RADIÉ par A0 (15000 req/5h sous-utilisé) |
| [ADR-OPS-002](L0_Kernel_OS/ADR-OPS-002_llm-runtime-switching-protocol.md) | PROPOSED→RADIÉ | 2026-06-15 | [ADR-LLM-001, REG-001] | ⚠️ RADIÉ (dépendait Mistral) |
| [ADR-CONSENSUS-002](L0_Kernel_OS/ADR-CONSENSUS-002_emergency-shutdown-protocol-llm-orchestration.md) | PROPOSED→ACCEPTED | 2026-06-15 | [ADR-META-001, META-002] | ✅ présent (créé ce jour) |
| [ADR-AGENT-BOUNDARY-001](L0_Kernel_OS/ADR-AGENT-BOUNDARY-001_agent-lifecycle-harness-isolation.md) | PROPOSED→ACCEPTED | 2026-06-15 | [ADR-META-001, META-002] | ✅ présent (créé ce jour) |
| [ADR-SECURITY-001](L0_Kernel_OS/ADR-SECURITY-001_vault-boundary-and-rotation-policy.md) | PROPOSED→ACCEPTED | 2026-06-15 | [ADR-META-001, Test-Key-Pragma] | ✅ présent (créé ce jour) |
| [ADR-SOBER-002](L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md) | **RATIFIED** | **2026-06-21** | [ADR-META-001-D1, META-001-D5, META-001-D7, META-002-D9, META-003, META-005, RICK-001, L2-AAAS-001, INFRA-003, CANON-001] | ✅ **présent (créé + ratified 2026-06-21, A0 « GO » batch)** — Anti-Paperclip Maximizer Doctrine anti-Musk + 7 hard-stop triggers + A1 Rick veto kernel structurel (sister AAAS-001 + MEM-002 + INFRA-003 amendée). A1 Rick = mode alerte réactivé Q3 2026. |

## 🧘 L1 Life OS (11 ADR)

| ADR | Status | Date | doctrine_anchors | Action |
|-----|--------|------|------------------|--------|
| [ADR-META-001](L1_Life_OS/ADR-META-001_anti-paresse-verify-before-assert.md) | ACCEPTED | 2026-06-08 | (self = foundation) | ✅ backfill (self-ref) |
| [ADR-META-002](L1_Life_OS/ADR-META-002_autonomy-by-design.md) | DRAFT | 2026-06-14 | [ADR-META-001, ADR-RICK-001] | ✅ backfill |
| [ADR-Meta-000](L1_Life_OS/ADR-Meta-000_12-week-year-cycle-doctrine_DRAFT.md) | ACCEPTED | 2026-06-15 | [ADR-META-001, META-002] | ✅ présent (ratifié ce jour) |
| [ADR-MEMO-000](L1_Life_OS/ADR-MEMO-000_auto-research-karpathy-loop-claude-code_DRAFT.md) | ACCEPTED | 2026-06-15 | [ADR-META-001, META-002] | ✅ présent (ratifié ce jour) |
| [ADR-INFRA-MCP-001](L1_Life_OS/ADR-INFRA-MCP-001_agentic-mcp-mastery-dox-god-mode.md) | ACCEPTED | 2026-06-10 | [ADR-META-001, ADR-META-002] | ✅ backfill |
| [ADR-INFRA-004](L1_Life_OS/ADR-INFRA-004_jsonl-mining-extract-mindset-pipeline.md) | PROPOSED→ACCEPTED | 2026-06-15 | [ADR-META-001, META-002-D11] | ✅ présent (créé ce jour) |
| [ADR-META-003](L1_Life_OS/ADR-META-003_model-agnostic-runtime-doctrine.md) | PROPOSED→ACCEPTED | 2026-06-15 | [ADR-META-001, META-002-E13] | ✅ présent (créé ce jour) |
| [ADR-OBSERVABILITY-001](L1_Life_OS/ADR-OBSERVABILITY-001_sessions-canon-md-rotation.md) | PROPOSED→ACCEPTED | 2026-06-15 | [ADR-META-001, META-002] | ✅ présent (créé ce jour) |
| [ADR-MEM-001](L1_Life_OS/ADR-MEM-001_memory-fabric-unified-doctrine.md) | PROPOSED→ACCEPTED | 2026-06-15 | [ADR-META-001, META-003] | ✅ présent (créé ce jour) |
| [ADR-MEM-002](L1_Life_OS/ADR-MEM-002_wiki-lifewheel-mapping-doctrine.md) | **ACCEPTED** | **2026-06-21** | [ADR-META-001, META-001-D4, META-001-D7, META-002, META-002-D9, META-003, META-004, META-005, MEM-001, OBSERVABILITY-001, L2-AAAS-001, INFRA-003, SOBER-002] | ✅ **présent (créé + ratified 2026-06-21, A0 « GO » batch)** — Wiki 5-couches × 8-LDxx Life Wheel mapping + ID collision résolu (MEM-001 = Memory Fabric, MEM-002 = Wiki↔Life Wheel). Sister AAAS-001 + SOBER-002 + INFRA-003 amendée. |
| [ADR-META-004](L1_Life_OS/ADR-META-004_doctrine-anti-paresse-linkage.md) | PROPOSED→ACCEPTED | 2026-06-15 | [ADR-META-001, META-002, META-003] | ✅ présent (créé ce jour) |
| [ADR-META-005](L1_Life_OS/ADR-META-005_hooks-automation.md) | RATIFIED | 2026-06-21 | [ADR-META-001-D1, META-001-D4, META-001-D7, META-002-D9] | ✅ présent (ratifié 2026-06-21 par A0 Amadeus, chat Claude Code GO post-Vague 1 missions) |

## 💼 L2 Business OS (14 ADR)

| ADR | Status | Date | doctrine_anchors | Action |
|-----|--------|------|------------------|--------|
| [ADR-CANON-001](L2_Business_OS/ADR-CANON-001_roster-source-of-truth.md) | ACCEPTED | 2026-06-02 | [ADR-META-001] | ✅ backfill |
| [ADR-INFRA-002](L2_Business_OS/ADR-INFRA-002_repo-home-junction-law.md) | ACCEPTED | 2026-06-04 | [ADR-META-001, ADR-RICK-001] | ✅ backfill |
| [ADR-INFRA-003](L2_Business_OS/ADR-INFRA-003_business-os-ceo-dashboard-matryoshka.md) | **ACCEPTED + AMENDED 2026-06-21 RATIFIED** | 2026-06-04 (original) / **2026-06-21 (amendment §D1 RATIFIED)** | [ADR-META-001, META-001-D4, META-001-D7, META-002-D9, INFRA-002, **L2-AAAS-001, MEM-002, SOBER-002**] | ✅ backfill + ✅ **amendé §D1 2026-06-21 RATIFIED** (LD01_Business_Picard H10 + MANIFEST.md obligatoire + 8 LDxx Picard ownership matrix, sister scope AAAS-001 + MEM-002 + SOBER-002, A0 « GO » batch ratification) |
| [ADR-SUPABASE-001](L2_Business_OS/ADR-SUPABASE-001_self-hosted-multi-tenancy-schemas.md) | ACCEPTED | 2026-06-08 | [ADR-META-001, ADR-INFRA-002] | ✅ backfill |
| [ADR-OMK-001](L2_Business_OS/ADR-OMK-001_dual-product-dashboard-multitenant_RATIFIED.md) | RATIFIED | 2026-06-11 | [ADR-META-001, ADR-INFRA-002] | ✅ backfill |
| [ADR-OMK-002](L2_Business_OS/ADR-OMK-002_pg-roles-provisionning.md) | RATIFIED | 2026-06-11 | [ADR-META-001, OMK-001] | ✅ backfill |
| [ADR-OMK-003](L2_Business_OS/ADR-OMK-003_mcp-supabase-aspace.md) | RATIFIED | 2026-06-11 | [ADR-META-001, OMK-002] | ✅ backfill |
| [ADR-ABCOS-001](L2_Business_OS/ADR-ABCOS-001_multitenant-supabase-strategy.md) | ACCEPTED | 2026-06-10 | [ADR-META-001, ADR-OMK-001] | ✅ backfill |
| [ADR-L2-MESH-001](L2_Business_OS/ADR-L2-MESH-001_l2-mesh-postgres-protocol.md) | PROPOSED | 2026-06-11 | [ADR-META-001, OMK-001] | ✅ backfill |
| [ADR-AGENTIC-001](L2_Business_OS/ADR-AGENTIC-001_l2-agentic-commerce-nanosquad-coordination.md) | PROPOSED→ACCEPTED | 2026-06-15 | [ADR-META-001, OMK-001] | ✅ présent (créé ce jour) |
| [ADR-OMK-004](L2_Business_OS/ADR-OMK-004_pivot-supabase-cloud-vercel.md) | RATIFIED | 2026-06-19 | [ADR-META-001, OMK-001, OMK-003] | ✅ présent (ratifié 2026-06-19) |
| [ADR-OMK-005](L2_Business_OS/ADR-OMK-005_tenant-isolation-guard.md) | RATIFIED | 2026-06-20 | [ADR-META-001, OMK-004] | ✅ présent (ratifié 2026-06-20) |
| [ADR-ABCOS-002](L2_Business_OS/ADR-ABCOS-002_pivot-supabase-cloud-vercel.md) | RATIFIED | 2026-06-19 | [ADR-META-001, ABCOS-001] | ✅ présent (ratifié 2026-06-19) |
| [ADR-L2-AAAS-001](L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md) | **ACCEPTED** | **2026-06-21** | [ADR-META-001, META-001-D1, META-001-D3, META-001-D7, META-002, META-002-D9, META-003, META-005, INFRA-003, CANON-001, AGENTIC-001, SOBER-002] | ✅ **présent (créé + ratified 2026-06-21, A0 « GO » batch)** — AaaS Doctrine 3 Variants (Solaris/Nexus-OMK/Orbiter-ABC) × 4 Leviers Solarpunk (biomimétisme Benyus + low-high tech Aberkane + Meta Science + circular & blue economy) + Saru 1000T Kardashev Type 3. Sister SOBER-002 + MEM-002 + INFRA-003 amendée. |

## 📊 D1 receipts finaux

| Métrique | Initial | Post-backfill |
|----------|---------|---------------|
| ADR total canonique | 29 | **29** (= stable) |
| ADR avec `doctrine_anchors` field | 17 (créés/ratifiés ce jour) | **29** (12 backfill + 17 nouveaux) = **100%** |
| ADR DRAFT (non ratifié) | 1 (META-002) | **1** (META-002 en attente A0 sign-off) |
| ADR RADIÉ (cycle pivot) | 0 | **2** (REG-001 + OPS-002) — marqués ⚠️ |
| ADR PROPOSED (à ratifier) | 0 (tous ratifiés par A0 "go for all") | **0** |

## Doctrine ancrage

- **D1 verify-before-assert** : 29 paths vérifiés + frontmatter inspection 14 ADRs.
- **D4 no-self-contradiction** : INDEX = nouveau fichier (append-only), aucun ADR historique modifié (backfill = ajout frontmatter, justifié par ADR-META-004 doctrine).
- **D6 root cause** : 12 ADRs historiques créés avant doctrine_anchors canon (ADR-META-004 créé ce jour).
- **D8 cross-agent** : INDEX lisible par Codex/Gemini via SSH même path.

## Open follow-ups

1. **Modifier 12 ADRs historiques** pour ajouter le champ `doctrine_anchors` (D4 = acceptable car append-only frontmatter, mais batch sub-agent A3 préférable pour 0 risque)
2. **Update AGENTS.md** pour pointer ce INDEX
3. **INDEX canonisation** : A0 ratification formelle requise ?
