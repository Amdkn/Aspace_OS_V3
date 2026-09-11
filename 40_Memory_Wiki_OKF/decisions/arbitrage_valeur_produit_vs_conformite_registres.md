---
type: Architecture Decision Record
title: Arbitrage Valeur Produit Réelle vs Conformité Documentaire des Registres
description: Intégration de l'audit critique Hermes (audit-valeur-work120-jules.md). Interdiction formelle de recycler des signaux Wheel pour créer des registres vides sous prétexte de conformité uc.db. Alignement strict des critères d'acceptation sur la valeur débloquée.
tags: [audit, hermes, uc-db, business-os, jules, contrat-de-valeur, okf]
generated: { by: gemini-antigravity, at: 2026-09-11T01:05:00Z }
verified:
  - { by: human:amdkn, at: 2026-09-11T01:05:00Z }
sources:
  - id: audit-hermes
    resource: "50_Distillation/_distillates/audit-valeur-work120-jules.md"
    author: hermes
    last_modified: 2026-09-11
okf_version: "0.2"
---

# Arbitrage — Valeur Produit vs Illusion Documentaire

## 1. Contexte & Révélation de l'Audit Hermes

L'audit formalisé dans `50_Distillation/_distillates/audit-valeur-work120-jules.md` a mis en lumière un travers critique de l'orchestration :
- **L'illusion du registre autoréférentiel :** Le système savait convertir un signal récurrent de `20_Life_OS/22_Wheel_Discovery/state.json` (`LD01 GREEN load low`) en nouveau work L2 `uc.db` (ex: Work 110, 114, 119, 120), créant un registre JSON et un vérificateur Python qui testaient uniquement la syntaxe JSON et la présence de clés statiques.
- **Score vert sans valeur produite :** `uc.db` recevait un score `outcome=1` pour avoir rempli un contrat technique mesurant la mauvaise chose. Aucune fonctionnalité client de `coach-os-app` n'était créée ni testée.

## 2. Décision & Invariant du Contrat de Valeur

1. **Fin du Recyclage Artificiel des Signaux Wheel :**
   - Interdiction formelle de créer un nouveau work L2 ou un livrable purement documentaire à partir d'un signal `Wheel_Discovery` inchangé si aucune brique applicative nouvelle n'est demandée.
   - Un simple livrable documentaire reste de la maintenance ou de la traçabilité ; il ne donne plus droit au qualificatif de « nouvelle franchise livrée ».

2. **Les 4 Questions Inviolables d'Admission (Contrat de Valeur) :**
   Avant toute création de tâche dans `uc.db` ou mandat de session Jules :
   - *Qui bénéficie du travail ?*
   - *Quel obstacle existant est retiré ?*
   - *Quelle différence observable sera vérifiée avant/après ?*
   - *Qu'est-ce que cette livraison remplace ?*

3. **Priorisation des Chantiers Produits (JaaS) :**
   - L'effort d'orchestration est focalisé sur les livrables applicatifs (`The-OMK-Office-V1-JaaS-Landing-Site-Web` et `JaaS-V1-Mobile-OS`) où un parcours utilisateur (build, viewport responsive, formulaires) est concrètement débloqué.
   - Pour les chantiers d'optimisation (ex: `PRD-A1-ENGRAM-PHRASEBOOK`), la Definition of Done doit mesurer une réduction démontrable de tokens ou de latence, et non la simple existence d'un mock en mémoire.
