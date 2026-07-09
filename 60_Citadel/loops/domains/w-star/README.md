---
type: loop-contract
loop: w-star (template — 1 instance par client)
flag: enable_ship_internal.flag (interne) · enable_ship_outboard.flag (gagné : 3 cycles verts)
trigger: onboarding client signé (WF2) → instancier `w-star/<tenant-id>/README.md` depuis CE template
rails: wargames 05 (DLP) · 06 (AARRR) · 07 (Quiz)
---
# Contrat W* — Workflow client L2 (template)

**Goal** : livrer le forfait 1000$/mo d'UN client (ADR-NEXUS-NICHE-001) : capture matière noire → skills `.md` exécutables → livrables WK.
**Workflow** : tick WK : lire le MANIFEST client (`10_Projects/<client>/`) → exécuter les tasks du client (queue taggée `<tenant-id>`) → TOUT passage réseau = proxy DLP d'abord (mission 05) → livrable → verse Summers → rapport MiroFish Picard.
**Boundaries** : cloisonnement strict par tenant (RLS + dossiers) · PII jamais en clair dans loops/ · ship interne libre (flag interne) ; ship outboard (prod client, envois) SEULEMENT si `enable_ship_outboard.flag` présent — gagné par 3 cycles verts, retiré au 1er rollback/fuite (airlock B3) · les clients ne voient ni L1 ni le canon.
**Timeline** : - [2026-07-06] template posé (0 client instancié — l'amorçage est le job des missions 06/07).
