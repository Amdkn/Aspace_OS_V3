---
type: Bundle index
title: 40_Memory_Wiki_OKF — mémoire canonique du poste
description: Point d'entrée de la mémoire durable, au format OpenWiki, avec des concepts en OKF v0.2. C'est ici qu'on cherche avant d'agir et qu'on écrit après avoir fini.
tags: [memoire, okf, openwiki, aspace-os-v3]
generated: { by: claude-opus-5, at: 2026-08-17T15:10:00Z }
verified:
  - { by: human:amdkn, at: 2026-08-17T15:05:00Z }
sources:
  - id: decision-emplacement
    resource: "arbitrage utilisateur — « déplacer les concepts hors d'openwiki/ dans un nouveau dossier 40_Memory_Wiki_OKF »"
    author: human:amdkn
    last_modified: 2026-08-17
okf_version: "0.2"
---

# À quoi sert ce bundle

C'est la **mémoire du poste**. Pas les notes d'une session, pas un dossier de
travail : l'endroit où une connaissance durable est écrite une fois et
retrouvée ensuite.

Deux obligations, à chaque session :

1. **Chercher ici avant de chercher ailleurs.** Toute question sur une
   intégration, une décision passée, un piège déjà payé, une configuration se
   lit d'abord dans ce bundle. Redécouvrir à l'aveugle ce qui est déjà écrit
   coûte du quota et rend une réponse moins sûre que le document.
2. **Écrire ici à la fin de chaque tâche.** Une tâche qui a produit une
   connaissance durable — une intégration câblée, une cause racine trouvée,
   une décision d'architecture — se consigne avant de clore.

Le format des pages est décrit dans [OKF v0.2](OKF.md). Comment s'en servir au
quotidien : [Démarrage rapide](quickstart.md).

# Pourquoi ce dossier existe

La mémoire vivait auparavant dans `openwiki/openwiki/`, qui est un **clone du
dépôt amont `langchain-ai/openwiki`** — le dépôt d'un tiers, avec son propre
`.git`, invisible depuis le dépôt parent et impossible à pousser.

Écrite là, la mémoire ne survivait pas à une perte de disque. Ici, elle est
suivie par `Amdkn/ASpace_OS_V3` et part avec chaque push.

Le clone `openwiki/` reste en place : c'est l'outil qui **génère** des wikis,
pas l'endroit où l'on **range** les siens.

# Files

- [Démarrage rapide](quickstart.md) - Comment chercher dans ce bundle, et comment y écrire un concept sans casser l'index.
- [OKF v0.2](OKF.md) - Le format : frontmatter minimal, provenance, et les trois niveaux de confiance qui se déduisent de `verified`.
- [Instructions du bundle](INSTRUCTIONS.md) - Ce qui a sa place ici et ce qui n'en a pas.

# Directories

- [architecture](architecture/) - Décisions de structure et leurs raisons (inclut [Architecture Agent OS V3 Template Reproductible](architecture/agent_os_v3_reproducible_desktop.md), [Architecture CMS Hiérarchique Agent OS V2](architecture/agent_os_v2_cms_hierarchique.md), [Neutralisation de 9Router et OmniRoute](architecture/9router_omniroute_neutralisation.md), [Semantica AGI & Context Graphs](architecture/semantica_graph_native_ai.md), [Matrice 3D-7D des Trois Docteurs & Cores](architecture/matrice_3d_7d_docteurs_cores.md), [Matrice 3D-7D des Domaines Business BD01-BD08](architecture/matrice_3d_7d_business_domaines.md), [Matrice 3D-7D Life Wheel & Frameworks A2](architecture/matrice_3d_7d_life_wheel.md), [Moteur Temporel de Compression Fractale 12WY](architecture/moteur_temporel_compression_12wy.md), [Roster des 14 Subagents Antigravity](architecture/roster_subagents_tech_os.md), [Co-Évolution Modèle-Harnais HoH](architecture/harness_of_harness_coevolution.md), [Dynamic Ontology & Graph Engineering](architecture/dynamic_ontology_and_graph_engineering.md), [Orchestration des 13 Scheduled Tasks](architecture/scheduled_tasks_orchestration_tech_os.md), [Méta-Tâche T-00 A0 Amadeus](architecture/meta_a0_scheduled_tasks_adaptation.md)).

- [concepts](concepts/) - Concepts atomiques durables (inclut [Intégration Ryan Software Factory & Antigravity SSSF](concepts/ryan_software_factory_antigravity.md), [Pyramide Déterministe à 7 Niveaux, Hooks, Webhooks et Meta-Routeur DOX](concepts/pyramide_7_niveaux_hooks_webhooks_dox.md), [Architecture Vocale 2-en-1 & Résilience d'Élocution Antigravity](concepts/architecture_vocale_2_en_1_antigravity.md), [Architecture Trimodale & Runtime Business Office 3 OS](concepts/business_office_3_os_trimodal_runtime.md), [Mode Full Économie — Orchestration Jules & Stitch](concepts/mode_full_economie_orchestration_jules_stitch.md), [Engram Hook IA O(1), Jules Bedrock Linear/Stitch & Morty Local CPU](concepts/engram_hook_ia_jules_linear_morty_local.md), [Cartographie & Stratégie de Migration Picard/Spock V2-V3](concepts/cartographie_et_strategie_migration_picard_spock_v2_v3.md), [Holding de Prototypes de Franchise — Matrice V2/V3](concepts/holding_prototypes_franchise_business_os_v3.md), [Posture Visionnaire E-Myth & Swarm Sémantique Hermes dans Life OS](concepts/posture_visionnaire_emyth_hermes_swarm_life_os.md)).
- [decisions](decisions/) - ADRs et arbitrages d'orchestration (inclut [Délégation Jules — Refonte Multi-Tenant & Back-Office The OMK Office](decisions/delegation_jules_refonte_the_omk_office_jaas.md), [Délégation Jules — Moteur Local SLM Morty & Ingestion Marin CPU](decisions/delegation_jules_moteur_local_morty_slm.md), [ADR — Heartbeat Daemon 15 Min, Plancher Jules >= 3 & Préservation Quotas Antigravity](decisions/heartbeat_15min_plancher_jules_preservation_quotas.md), [Arbitrage Valeur Produit Réelle vs Conformité Registres](decisions/arbitrage_valeur_produit_vs_conformite_registres.md)).
- [canon](canon/) - Sauvegarde des deux `CLAUDE.md` qui pilotent l'agent et vivent hors de tout dépôt.
- [integrations](integrations/) - Ce qui est branché à quoi, et ce que ça a coûté d'y arriver.
- [operations](operations/) - Playbooks, runbooks, gestes de remise en route (inclut [Ingestion Takeout Gemini](operations/takeout_gemini_geordi_ingestion.md), [Distillat Conversations Gemini](C:/Users/amado/ASpace_OS_V3/50_Distillation/ressources/distillat_gemini_conversations_2026_09.md), [Distillat Sessions ChatGPT](C:/Users/amado/ASpace_OS_V3/50_Distillation/ressources/distillat_chatgpt_shares_2026_09.md), [Distillat Vague 2 Innovations](C:/Users/amado/ASpace_OS_V3/50_Distillation/ressources/distillat_wave2_harness_coevolution_2026_09.md)).
- [learning](learning/) - Les echecs mesures, pour ne pas les rejouer (inclut [Skill Misevolution & Rempart Immunitaire](learning/skill_misevolution_and_immune_defense.md)).
- [security](security/) - Modèles de sécurité, vulnérabilités, cloisonnements.
