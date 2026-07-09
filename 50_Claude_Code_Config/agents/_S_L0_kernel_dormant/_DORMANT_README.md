# 🌙 _S_L0_kernel_dormant — Solarpunk Kernel (L0) en DORMANCE

> **Zone dormante** créée 2026-06-27 (plan L0 `plans/bedrock-humming-tardis.md`, P3 amorce).
> **But** : donner à Hermes un **SSOT cohérent** des agents L0 Kernel **sans les activer** — A0 craint (à raison) qu'une activation prématurée les fasse échouer à orchestrer L1/L2.

## Pourquoi c'est RÉELLEMENT dormant (mécanisme, D1)
- Capsules au **format identité canon** (`# [S1] Rick` + Identity/Law/…), **ZÉRO frontmatter Claude Code** (`name/description/tools`) → Claude Code **ne les enregistre PAS** comme agents invocables.
- Sous-dossier **préfixé `_`** = hors convention de scan d'agents actifs.
- **Aucun câblage** : zéro cron, zéro workflow, zéro hook les invoque (Posture C).
- → Présents pour la **lecture SSOT** (Hermes), **inertes** pour l'orchestration.

## Rename A→S (évite la collision de namespace)
| Tier | Préfixe | Niveau | Pourquoi |
|---|---|---|---|
| Life OS | **A** (A1/A2/A3) | L1 | Beth/Morty + 6 ships + 35 twins (live) |
| Business OS | **B** (B1/B2/B3) | L2 | Jerry/Summers + 8 B2 + 53 B3 (live) |
| **Kernel OS** | **S** (S1/S2/S3) | **L0** | **Sobriété/Solarpunk** — Rick S1 déjà canon (giggly §4.5) |

## Roster dormant (14 capsules, source `00_Amadeus/01_Identity_Core/agents/L0_*`)
| S-capsule | ← Canon | Rôle |
|---|---|---|
| `S1_Rick` | L0_A1_Rick | Gatekeeper souveraineté + veto anti-fragilité |
| `S2_Doctor_11` | L0_A2_Doctor_11 | Manager Interface (Calm Tech) |
| `S2_Doctor_12` | L0_A2_Doctor_12 | Manager Factory (Robust Pipelines) |
| `S2_Doctor_13` | L0_A2_Doctor_13 | Manager TARDIS/Core (Sovereign) |
| `S3_Amy` | L0_A3_Amy | Interface & esthétique |
| `S3_Rory` | L0_A3_Rory | Sécurité & backup |
| `S3_River` | L0_A3_River | Chronologie & sync |
| `S3_Clara` | L0_A3_Clara | ETL & data cleaning |
| `S3_Nardole` | L0_A3_Nardole | Ops & ticketing |
| `S3_Bill` | L0_A3_Bill | Research & market intel |
| `S3_Yaz` | L0_A3_Yaz | Monitoring infra |
| `S3_Ryan` | L0_A3_Ryan | Connecteur & key master |
| `S3_Graham` | L0_A3_Graham | Router & message bus |
| `Donna_DLQ` | L0_Donna_DLQ | Dead Letter Queue (filet de sécurité) |

> A0 (L0_A0_Amadeus) **non renommé** : A0 = source/jumeau, pas un agent Kernel.

## Protocole d'activation (Q4 2026 / Q1 2027 — gated)
1. **Gate Rick S1** : check anti-fragilité (cette complexité kernel se justifie-t-elle ?).
2. **Gate plan L1** : L1 Life OS stable + cycle 12WY le requiert (items 6/11).
3. **Gate Hermes** : Hermes méta-orchestrateur opérationnel (ADR-L0-META-ORCH-001 RATIFIED + P1-P4 verts).
4. **Activation** = convertir ces capsules en agents CC live (ajout frontmatter `name/description/tools`) OU les câbler dans Hermes — décision A0 explicite, jamais automatique.

**Tant que les 4 gates ne sont pas verts : ces capsules RESTENT inertes.**
