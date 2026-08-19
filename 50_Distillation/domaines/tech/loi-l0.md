---
type: Concept
title: Loi L0 — Souveraineté, anti-fragilité, sobriété, idempotence
description: Les quatre principes fondateurs du Tech OS (couche 0) qui cadrent toute doctrine Rick's Verse.
tags: [tech, governance, rick, constitution, fondation]
generated: { by: minimax-m3, at: 2026-08-19T12:00:00Z }
verified:
  - { by: process:read, at: 2026-08-19T12:00:00Z }
sources:
  - id: loi-l0
    resource: 05_From_V2_Domains/10_Tech_OS/00_Governance_Rick/Loi_L0.md
    title: La Loi du L0 (Layer 0)
    last_modified: 2026-01-01
  - id: sobriete
    resource: 05_From_V2_Domains/10_Tech_OS/00_Governance_Rick/Sobriete.md
    title: Protocole de Sobriété
    last_modified: 2026-01-01
  - id: adr-000
    resource: 05_From_V2_Domains/10_Tech_OS/00_Governance_Rick/Drivers/A1 - Rick Sanchez (Visionnaire & Gatekeeper Absolu).md
    title: ADR-000 Constitution Solarpunk Kernel
    last_modified: 2026-04-26
okf_version: "0.2"
---

> "Je ne suis pas là pour débattre. Je suis là pour que ça marche quand tout le reste s'effondre." — Rick Sanchez, Loi_L0

La Loi L0 acte quatre principes non-négociables du Solarpunk Kernel :

1. **Souveraineté absolue** — pas de location d'existence. Si un outil ferme demain, il doit être remplaçable en 24 h. Données locales d'abord ; le cloud n'est qu'une copie de sauvegarde.
2. **Anti-fragilité** (Chaos Engineering) — ne pas réparer un serveur, le tuer et laisser un script en reconstruire un nouveau. Toute tâche manuelle est une faille de sécurité.
3. **Sobriété radicale** — un script de 10 lignes vaut mieux qu'une application de 100 Mo. CLI for life, pas de GUI serveur.
4. **Idempotence** — l'état désiré est déclaré, le script converge vers lui ; relancer l'installation sur un système déjà en place ne casse rien.

## Conséquences architecturales

- **Stack souveraine close** : React (interface), Supabase (ADN), OpenClaw (système nerveux). Aucune autre solution SaaS d'automatisation n'est admise comme dépendance de production (ADR-000 §1).
- **Pas de bloatware propriétaire** (Sobriete.md) : monitoring open-source uniquement, pas de GUI serveur, `npm prune` régulier.
- **Directives d'Apoptose** (ADR-000 §4) : un agent qui viole la souveraineté, corrompt Supabase ou boucle infiniment est détruit sans préavis.

## Pourquoi ça compte

Ces quatre principes servent d'**Axiome 0** : tout autre choix architectural (framework, dépendance, contrat) se justifie contre eux. Un AD qui consomme trop d'énergie ou crée une usine à gaz déclenche l'Apoptose immédiate — la frugalité n'est pas un nice-to-have, c'est un filtre de sélection.

Voir aussi : [[caste-doctor-who]], [[tardis-inverse]], [[sovereignty-tier-pyramid]].