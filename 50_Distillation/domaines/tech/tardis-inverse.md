---
type: Concept
title: TARDIS Inversé — ordre d'invocation Kernel d'abord
description: L'ordre canonique d'invocation de l'infrastructure L0 : L0.3 Kernel Core (13ème Doctor) avant L0.2 Forge (12ème) avant L0.1 Life Core (11ème).
tags: [tech, architecture, ordre, kernel, ford]
generated: { by: minimax-m3, at: 2026-08-19T12:00:00Z }
verified:
  - { by: process:read, at: 2026-08-19T12:00:00Z }
sources:
  - id: sdd-001
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-001_solarpunk-kernel-core.md
    title: SDD-001 Solarpunk Kernel Core L0.3
    last_modified: 2026-04-27
  - id: sdd-003
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-003_tardis-protocol-orchestration.md
    title: SDD-003 TARDIS Protocol Orchestration
    last_modified: 2026-04-25
okf_version: "0.2"
---

Le SDD-001 corrige SDD-003 : l'ordre d'invocation de l'infrastructure suit le **TARDIS Inversé** :

```
ÉTAPE 1 ── L0.3 KERNEL CORE (13ème Doctor)         ← premier
           Yaz structure le VPS via Hostinger MCP
           Ryan conçoit les déploiements via Dokploy MCP
           Graham prépare la mémoire RAG via Supabase MCP
           → Sans Kernel stable : rien ne peut être forgé.

ÉTAPE 2 ── L0.2 FORGE CORE (12ème Doctor)         ← deuxième
           Bill blueprinte sur le sol Yaz
           Clara forge les CLIs dans le sandbox Ryan
           Nardol valide avec les hooks ECC

ÉTAPE 3 ── L0.1 LIFE CORE (11ème Doctor)         ← troisième
           Amy construit l'interface sur la Forge
           Rory persiste sur la DB que Graham surveille
           River orchestre les workflows que Ryan déploie
```

**Séquence de redémarrage total (panne complète)** : Graham → Yaz → Ryan → Kernel stable → Bill → Clara → Nardol → Skills prêts → Amy → Rory → River → Life Web OS restauré.

## Fractale interne au 13ème Doctor

La loi se réplique à l'échelle du Kernel Core :
- Graham (état) → Yaz (périmètre) → Ryan (action). Sans Graham d'abord, Yaz ne peut pas cadrer, Ryan ne peut pas déployer.

## Pourquoi Kernel d'abord

C'est l'inverse du réflexe « produit d'abord » : sans machine stable, pas d'outils fiables ; sans outils, pas de produit durable. L'Amiral (A0) qui touche au Kernel viole la règle 50/30/20 et s'enlise dans le technique — le piège fondateur que SDD-001 a documenté.

Voir aussi : [[caste-doctor-who]], [[axiomes-antifragilite-k1-k4]], [[paniques-k1-k4-kernel]].