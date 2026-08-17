---
type: Concept
title: Spock = A3 Areas officer
description: Le gardien de la classification PARA Areas ; il protège la distinction entre responsabilité durable et livrable à échéance, et route le reste vers Geordi (ressources) ou Picard (projet).
tags: [spock, areas, para, classification, a3, life-os, business-os]
generated: { by: minimax-m3, at: 2026-08-17T20:30:00Z }
verified:
  - { by: process:extraction-areas, at: 2026-08-17T20:30:00Z }
sources:
  - id: spock-spec
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/A3_Spock_Areas_Spec.md"
    title: A3 Spock Spec - Areas (parent A2 Computer Enterprise PARA)
    last_modified: 2026-06-21
  - id: areas-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/README.md"
    title: 02_Areas_Spock root README
    last_modified: 2026-05-21
  - id: references-index
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/Business_Pulse/L2_Business_Pulse_References_Index.md"
    title: L2 Business Pulse References Index
    last_modified: 2026-05-21
okf_version: "0.2"
---

# Spock — Areas officer (A3)

Spock est l'officier **A3 Areas** du PARA Enterprise. Sa mission unique tient en une question :

> *Est-ce une responsabilité ou un standard qui doit être maintenu dans le temps ?*

Si oui, c'est une **Area** et il l'incube. Si non, il route ailleurs. Sa doctrine est minimaliste et non-négociable : il ne transforme pas toute responsabilité en Project, et il ne mute ni Obsidian ni les plugins.

## La question centrale et ses outputs

L'output de Spock est un verdict de classification, pas un plan d'exécution. Le format canonique est posé dans `A3_Spock_Areas_Spec.md` :

```yaml
a3: Spock
classification: Areas
finding: area|not_area|needs_standard|project_leak|archive_candidate|hypothesis
area_name: ""
standard: ""
evidence:
  - path: ""
    note: ""
next_owner: Computer|Picard|Geordi|Data
```

Le verdict n'est jamais « je garde » — il est soit **area** (Spock incube), soit **route vers un autre officier** (Computer, Picard, Geordi, Data). Spock ne garde que ce qui est sa juridiction ; le reste est rejeté explicitement.

## Frontières d'autorité (mesurées)

Spock **maintient** des standards ; il **n'exécute pas** les tâches d'un Project. Si l'item a une échéance et un livrable, il route vers **Picard**. Si l'item est purement référentiel, il route vers **Geordi**. Si l'item est clos mais conservé, il route vers **Data**. C'est la frontière qui empêche le seau Areas de devenir un dépotoir de « ce qui n'a pas de place ailleurs » — un piège déjà documenté ailleurs dans le canon.

L'alignement patché du 2026-06-21 (`A3_Spock_Areas_Spec.md`, section « Alignement Plan fancy-hugging-bengio.md ») confirme :

- Parent **A2** : Computer (USS Enterprise)
- Owner **A1** : Morty (Focus Gatekeeper)
- Horizon : **H30** (Areas = revue continue sur 30 jours, doctrine tenue à jour)
- Jerry variants : J01_Prime / J02_Bio / J03_Nexus / J04_Solarpunk = les **4 quartiers** canoniques de l'Areas

Spock n'est donc pas le gardien d'un cas : il est l'officier **catégoriel** qui décide **qu'est-ce qui devient une Area** et **qui en est responsable**.

## Le piège à éviter

L'alignement patché corrige une erreur fréquente : « Spock = Life Wheel drift ». C'est faux. Le Life Wheel drift (Tilly + Spock combiné) appartient au niveau A1/A2, pas à l'officier Areas. Confondre les deux fait dériver Spock hors de sa juridiction et Areas devient un fourre-tout Life OS. Le patch D3 nuance est explicite là-dessus.

## Anchor canonique

- **Parent** : `A2_COMPUTER_ENTERPRISE_PARA` (Computer orchestre la structure)
- **Classification** : Areas (PARA permanent, sans deadline)
- **Statut courant** : `SHADOW_ACTIVE` (les Areas sont incubées mais pas encore toutes actives)
- **Mission textuelle** : « Areas are not 'to-do' projects ; they are maintained systems. »