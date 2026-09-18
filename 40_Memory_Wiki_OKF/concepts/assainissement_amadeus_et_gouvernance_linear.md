---
type: Architecture Decision
title: Assainissement Structurel de 00_Amadeus et Alignement du Flux d Execution sur Linear
description: Diagnostic rigoureux de la pollution de 00_Amadeus (depotoir de traces), cadrage de l isolation du build deepseek-harness et de 30_MEMORY_CORE, arret de la dispersion de Jules sur Business OS sans tickets Linear, et activation du pilotage deterministe.
tags: [amadeus-cleanup, deepseek-harness, linear-governance, memory-core, coach-os, business-os, okf]
generated: { by: "gemini-pro", at: "2026-09-11T20:35:00Z" }
verified:
  - { by: "human:amdkn", at: "2026-09-11T20:35:00Z" }
sources:
  - id: amadeus-dox
    resource: "00_Amadeus/AGENTS.md"
    title: "DOX Child 00_Amadeus - Memory lives in Geordi, not here"
    last_modified: 2026-08-16
  - id: linear-autonomy-spec
    resource: "delegation-a-jules/SPEC-003-LINEAR-AUTONOMY-AND-STRUCTURE.md"
    title: "SPEC-003 Structuration Autonome de Linear par Jules"
    last_modified: 2026-09-09
okf_version: "0.2"
---

# Assainissement Structurel de 00_Amadeus & Alignement du Flux d'Execution sur Linear

## 1. Diagnostic Chirurgical de 00_Amadeus (L'Effet Depotoir Elucide)

L'audit physique approfondi de 00_Amadeus revele exactement pourquoi ce dossier a derive en depotoir au detriment des dossiers reels du systeme :

1. **L'Elephant 20_Harness/deepseek-harness (13 662 fichiers, 216 Mo) :**
   - Un depot monolithique entier a ete clone avec son node_modules complet (39 packages de tooling), ses dossiers .agents/ (2 578 fichiers de traces) et ses builds intermediaires dans 00_Amadeus/20_Harness/.
   - Cet intrus representait a lui seul **97% des fichiers de 00_Amadeus**, polluant la cartographie et masquant le reste.
2. **L'Anomalie 30_MEMORY_CORE/ (532 fichiers, 405 .md) :**
   - Regle locale n 1 violee : "Memory lives in Geordi, not here. 30_MEMORY_CORE/ is a transitional artifact."
   - Ce dossier stocke des archives de sessions brutes (sessions_md/, 382 fichiers), des logs intermediaires de conversion (journal_carto*.log) et des scripts obsoletes qui n'ont rien a faire dans l'Identity Core.
3. **Le Trompe-l'oeil des Observers (10_Observers/) :**
   - 10_Observers/ contient 3 Jonctions NTFS (agent-os, pocketbase-vec, super-simple-software-factory) pointant vers des dizaines de milliers de fichiers externes (agent-os a 463 991 fichiers), tandis que les 7 autres observers ne sont que des repertoires coquilles vides (.gitkeep).

---

## 2. Retablissement de la Hierarchie et des Vrais Dossiers

Contrairement a 00_Amadeus qui accumulait des residus passifs :
- **30_Business_OS** detient le vrai socle applicatif : le template complet 10_Projects/coach-os-app (28 apps reelles, stores Zustand, RLS multi-tenants, CRM, CMS, Tasks & DoDs).
- **20_Life_OS** detient les moteurs vivants : 00_Gatekeepers_Beth_Morty, 21_Ikigai_Orville, 23_12WY_SNW, 24_PARA_Enterprise.
- **10_Tech_OS** detient le noyau : uc.db (121 works, 0 pending, DLQ vide), dlq.py, controleur.py.

---

## 3. Recadrage de Jules : Interdiction de Bricoler sans Cadre Linear

L'utilisateur a pose un interdit sans appel : **Arreter d'envoyer Jules bricoler a perte sur Business OS alors que rien n'est structure dans Linear.**

1. **Arret des delegations dispersees :** Les sessions de surface (ex: mini-retouches cosmetiques) sont stoppees.
2. **Linear comme Unique Source de Pilotage :**
   - Jules et l'orchestrateur doivent s'adosser a **Linear** pour tout dispatch de travail.
   - Les 3 equipes canoniques definies dans SPEC-003 sont sanctuarisees :
     - **Kernel Core (KFR)** : 13e Docteur, Ryan, Yaz, Graham.
     - **Life Core (LC)** : 11e Docteur, Amy, Rory, River.
     - **Forge Core (FOR)** : 12e Docteur, Clara, Bill, Nardole.
   - Aucun PRD ne doit etre envoye a Jules sans reference explicite a une issue Linear identifiee et un critere d'acceptation falsifiable mesurable.
