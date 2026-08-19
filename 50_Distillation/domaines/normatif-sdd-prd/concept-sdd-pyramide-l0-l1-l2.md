---
type: Concept
title: SDD Pyramide L0/L1/L2 — la triade Rick/Beth/Jerry
description: La doctrine de la pyramide A'Space OS en trois couches : L0 Bedrock (Rick's Verse, Solarpunk Kernel, 13 Doctors), L1 Conscience (Beth/Morty, 6 Vaisseaux, Life Wheel), L2 Business Pulse (Jerry Prime + 4 Variants, Summer, Justice League DC, Marvel Squads).
tags: [pyramide, l0, l1, l2, bedrock, conscience, business-pulse, rick, beth, jerry, solarpunk-kernel]
generated: { by: minimax-m3, at: 2026-08-19T16:00:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-19T16:00:00Z }
sources:
  - id: sdd-006-pyramide
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-006_business-pulse-l2-pyramide.md (lignes 21-103)"
    title: SDD-006 Partie I §1-§2 — Le Triptyque Souverain + Vue Pyramidale
    last_modified: 2026-08-19
  - id: sdd-005-l1
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-005_life-os-l1-integration.md (lignes 7-103)"
    title: SDD-005 §1-§2 — Paradigme de séparation L0/L1
    last_modified: 2026-04-26
  - id: sdd-001-kernel
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-001_solarpunk-kernel-core.md"
    title: SDD-001 Solarpunk Kernel Core (L0)
    last_modified: 2026-04-27
okf_version: "0.2"
---

# SDD Pyramide L0/L1/L2 — la triade Rick/Beth/Jerry

## Le Triptyque Souverain (verbatim SDD-006 §1)

```
╔═══════════════════════════════════════════════════════════════════╗
║               LE TRIPTYQUE A'SPACE OS                           ║
╠══════════╦════════════════════════════════════════════════════════�
║  COUCHE  ║  SYSTÈME               NATURE         DONNÉES        ║
╠══════════╬════════════════════════════════════════════════════════╣
�          ║                                                       ║
║  L2      ║  Business OS           CORPS          Flow Data      ║
║  Action  ║  Business Pulse        "Le Moteur"    KPIs, Cash,    ║
║          ║  Jerry + Summers       Génère les     Artefacts      ║
║          ║  DC + Marvel           ressources     produits       ║
║          ║                                                       ║
╠══════════╬════════════════════════════════════════════════════════╣
║          ║                                                       ║
║  L1      ║  Life OS               ÂME            Soft Data      ║
║  Conscience  Beth + Morty         "La Conscience" Ikigai,       ║
║          ║  6 Vaisseaux           Donne le sens  Jauges LD,     ║
║          ║  Starfleet Crew        et le veto     GTD, 12WY      ║
║          ║                                                       ║
╠══════════╬════════════════════════════════════════════════════════╣
║          ║                                                       ║
║  L0      ║  Tech OS               OSSATURE       Hard Data      ║
║  Bedrock ║  Rick's Verse          "Le Bedrock"   SQL, Docker,   ║
║          ║  Doctors + Companions  Survie et      SSL, Supabase, �
║          ║  Solarpunk Kernel      mémoire brute  IndexedDB      ║
║          ║                                                       ║
╚══════════╩════════════════════════════════════════════════════════╝
```

## L'Ordre de Priorité Absolu (verbatim)

```
L0 est le sol.              Si L0 tombe → tout s'effondre.
L1 est la conscience.       Si L1 dit HALT → L2 s'arrête.
L2 est le moteur.           Si L2 s'emballe → L1 coupe le circuit.

Ordre d'autorité : L0 ≥ L1 > L2
Ordre de dépendance : L2 dépend de L1 qui dépend de L0.
L2 finance L0 et L1. Jamais l'inverse.
```

## Mapping agents ↔ couches

### L0 — Bedrock (Rick's Verse, Doctors)

| Couche interne | Équipe | Mission |
|---|---|---|
| L0.1 Life Core | Amy · Rory · River | Hôpital (data, persistance SQL, Agent Portal) |
| L0.2 Forge Core | Bill · Clara · Nardol | Forge (skills, CLI, runners) |
| L0.3 Kernel Core | Yaz · Ryan · Graham | Kernel (infra, SSL, Supabase) |

### L1 — Conscience (Beth/Morty, 6 Vaisseaux)

| Vaisseau | Rôle L1 |
|---|---|
| USS Orville | Ikigai (4 piliers) |
| USS Discovery | ZORA + Life Wheel (8 jauges) |
| USS SNW (Enterprise) | Ordinateur SNW (12WY, sprints) |
| USS Enterprise | Picard — Projects |
| USS Cerritos | GTD (Mariner → Boimler → Tendi → Rutherford → Freeman) |
| USS Protostar | Holo-Janeway — DEAL |

### L2 — Business Pulse (Jerry, Summer, DC, Marvel)

- **4 Variants de Jerry** : Prime (LD01+LD02), Bio (LD03+LD04),
  Nexus (LD05+LD06), Solarpunk (LD07+LD08).
- **Summer** (1 par projet B1/B2/B3/C1/J1) — CEO local du Summer's
  Verse.
- **Justice League DC** (A'2, 7 stratèges → 8 avec John Jones /
  Martian Manhunter / Sales post-amendement).
- **Squads Marvel** (A'3, 7 escouades → 8 avec Illuminati).

## Les 3 Lois Fondamentales de L2 (verbatim SDD-006 §2)

1. **Subordination (Veto de Beth)** — Beth a priorité absolue sur L2.
   Si Beth émet HALT 🔴, toute accélération Business est gelée.
2. **Avengers Rule (Loi de l'Artefact)** — Pas d'Action sans
   Artefact. Un ticket n'est « Done » que s'il produit un livrable
   concret, documenté et versionné.
3. **Batman Gating (Ops avant Croissance)** — Si Batman (Ops &
   Stabilité) déclare CRITIQUE 🔴, Flash (Product) et Superman
   (Growth) sont bloqués. La stabilité précède la croissance.

## Verdict

**canon** — la pyramide L0/L1/L2 est l'invariant structurel d'A'Space
OS. Toutes les SDD chain (Legacy V0.x et numérotée 000→010)
s'alignent sur cette triade.

## Source du décompte

`SDD-006 §1-§2` (lu directement) et `SDD-005 §1-§2` (lu directement).

## Concepts liés

- [[concept-sdd-v0-5-sovereign-constitution]] — le pivot « Livre
  des Lois » qui complète la pyramide avec le 8 domaines Ikigai.
- [[concept-amendement-001-8e-domaine]] — l'amendement qui pose le
  8e stratège DC (John Jones / Sales).
