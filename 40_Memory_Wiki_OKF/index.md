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

- [architecture](architecture/) - Décisions de structure et leurs raisons.
- [integrations](integrations/) - Ce qui est branché à quoi, et ce que ça a coûté d'y arriver.
- [operations](operations/) - Playbooks, runbooks, gestes de remise en route.
- [security](security/) - Modèles de sécurité, vulnérabilités, cloisonnements.
