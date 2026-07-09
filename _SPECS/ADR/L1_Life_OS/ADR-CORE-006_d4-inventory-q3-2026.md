---
id: ADR-CORE-006
title: D4 Inventory Q3 2026 — fermeture des 13 violations/gaps du §15 plan Mère
date: 2026-07-03
author: A0 Jumeau Numérique (CC Fable 5) sur impératif A+ "Corrigeons les Gaps et Contradictions"
status: RATIFIED
ratified: 2026-07-03T14:38 ET (A0 Amadeus GO 3/4 ratify post-audit Fable 13:55)
ratified_by: A0 Amadeus (Mavis/MC exécute l'édit sur instruction A+)
layer: L1 — Life OS / Canon hygiene
preserves:
  - ADR-META-001 D4 (append-only : le §15 de la Mère reste intact, cet ADR FERME sans réécrire)
  - Règle d'Or #3 (le Canon est immuable — fermetures par ADR nouveau, pas réécriture)
sister:
  - plan-L1-life-os.md §15 (l'inventaire source, inchangé)
  - plan-minimax-l1-book-lune/_ROSTER.md (mécanisation ROSTER-SOURCE, corrigée ce jour)
  - wiki/hand_offs/audit_minimax_executions_plans_2026-07-03.md (les récidives roster qui ont motivé la mécanisation)
tags: [#ADR #d4-inventory #canon-hygiene #cerritos #q3-2026]
---

# ADR-CORE-006 — D4 Inventory Q3 2026

## Décision

Les 13 violations/gaps documentés au §15 du plan Mère (audit 26 Explore sub-agents, 2026-06-21) reçoivent chacun un **statut de fermeture** ci-dessous. Le §15 reste intact (D4 append-only) — cet ADR est l'acte de fermeture. Résolution suprême : **le verbatim A+ prime sur toute source dérivée** (twins symphony, registre agents, cartography).

## La fermeture majeure — #1 Cerritos (TRANCHÉE A+ 2026-07-03)

**La "correction proposée" du 2026-06-21 était INVERSÉE.** Elle proposait d'ajouter Tendi au workflow GTD (sur la foi des fichiers `symphony/cerritos/`). A+ a re-ratifié verbatim le canon du plan Mère §3.2 :

| Stage | A3 | Mission (verbatim A+ 2026-07-03) |
|---|---|---|
| **Capture** | Mariner | inbox permanent |
| **Clarify** | Boimler | clarification de handoff en next action + relation avec Plan et Sister ADR |
| **Organize** | Rutherford | **router interne des frameworks Morty entre 12WY, PARA, GTD et DEAL** |
| **Review** | Tilly | review des **vetos Beth + sobriété Rick** — bypass UNIQUEMENT par les compressions temporelles de A0 ou A+ |
| **Engage** | Freeman | **transition L1↔L2** : Structuration Life OS ↔ Conception Business OS |

**Conséquences** : (a) Tendi = twin runtime existant du ship Cerritos, HORS workflow 5 stages, réassignation gated A0 ; (b) Tilly (Discovery LD04 Cognition) est prêtée au workflow GTD pour Review — cohérent avec la violation #4 (drift = Tilly+Spock) ; (c) le crew DEAL (Dal/Rok-Tahk/Zero/Gwyn sous Data) est confirmé complet dans la Mère — aucun débat n'était nécessaire.

**Artefacts corrigés ce jour (D5 receipts)** : plan-minimax-l1-book-lune.md ×2 (l.82, l.103) · `plan-minimax-l1-book-lune/_ROSTER.md` (table Cerritos + note Tendi) · `05_OSS_Twin/symphony/L2/symphony-supabase.spec.md` l.8 (le drift que Fable lui-même avait propagé le 2026-07-03 matin — D4 auto-correction nommée).

## Table de fermeture des 13

| # | Violation/Gap (§15) | Statut | Résolution |
|---|---|---|---|
| 1 | Tendi "manquant" Cerritos | **CLOSED-INVERSÉ** | Verbatim A+ 2026-07-03 (ci-dessus) — la correction du 06-21 est rejetée |
| 2 | Noms AaaS Solaris/Nexus/Orbiter | **CLOSED** | 3 ADR-ICP-*-001 RATIFIED 2026-06-24 ont fixé les noms canon |
| 3 | "Saru 1000T" = invention | **CLOSED-DOC** | 1000T = intention A0 (pas canon Saru) — dorénavant cité comme tel |
| 4 | Life Wheel drift Saru+Stamets | **CLOSED** | Drift = Tilly+Spock — cohérent avec Tilly/Review du canon #1 |
| 5 | "Beth supervise Ikigai" imprécis | **CLOSED-DOC** | Beth supervise A2 Orville qui porte Ikigai (D3 nuance actée partout depuis) |
| 6 | Life-OS-2026 "ALPHA V1.0" faux (réel : V0.9 Nexus Convergence) | **OPEN → W4** | Amendement ⚡ daté en fin de plan Mère (pattern §36), jamais de réécriture §5 |
| 7 | Clone hors `10_Projects/` (ADR-INFRA-002 violé) | **OPEN → W4** | Move ou junction gated A0 (Deep Checkpoint Law : inventaire avant move) |
| 8 | `.env.example` = local default | **CLOSED-DOC** | Dualité local/cloud documentée |
| 9 | "88 ressources" → 114 réelles | **CLOSED** | Chiffre canon = 114 (et recompte à chaque citation, jamais de mémoire) |
| 10 | 5 ADRs frameworks manquants | **PARTIAL → W4-W5** | DEAL (§25), GTD (§27), PARA (§29) existent en spec dans la Mère → extraction en fichiers `_SPECS/ADR/` + créer LIFE-WHEEL-001 + SYMPHONY-001 (convergent avec reco Hermes #10) |
| 11 | 2 vidéos non ingérées (CMA CGM + Biomimétisme) | **OPEN → Item 5 cycle** | Route `youtube-takeout-to-lifeos` |
| 12 | Dokploy killed non documenté au plan | **CLOSED** | Documenté (MEMORY.md, handoffs, plans L2) |
| 13 | symphony-supabase twin live non reflété | **CLOSED+** | Dépassé : U1 SHIPPED 2026-07-03 (table `symphony_state` vivante) + specs canon R2 écrites (`symphony-supabase.spec.md` + `supabase-specifics.md`) |

**Bilan : 8 CLOSED · 1 PARTIAL · 3 OPEN routées (W4/W4-W5/Item 5) · 1 INVERSÉE.**

## Leçon structurelle (la 4e récidive roster)

Quatre incidents roster en 24h : Kirk/Spock/McCoy (M3 scorecard) → Pia (wager) → Rita Boimler (chaîne E-Myth) → **Tendi-Organize/Rutherford-Reflect (propagé par Fable ET la cartography elle-même)**. Le 4e est le plus instructif : même l'auditeur a propagé le drift, parce que **la source dérivée (registre agents/cartography) divergeait du canon Mère sans que personne ne l'ait confrontée au verbatim A+**. Fix mécanisé : `_ROSTER.md` (fait) + règle : *tout conflit entre sources nominatives remonte au plan Mère puis à A+ — jamais tranché par une source dérivée.*

## Hors périmètre

Le registre runtime `.claude/agents/a3-cerritos-*` (descriptions Tendi=Organize, Rutherford=Reflect) reste en drift vs le canon — sa correction touche l'Identity/runtime et le tool registry statique (D6 #4 : effet au restart CC). **Gated A0**, routé W4.

## Sacred exclusions

§15 Mère intact · aucun ADR RATIFIED touché · pas de hard-delete · ADR en PROPOSED (pas de self-ratify), la résolution #1 étant néanmoins déjà exécutoire (verbatim A+ = ratification orale).
