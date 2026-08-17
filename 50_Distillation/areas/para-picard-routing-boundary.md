---
type: Concept
title: Para-Picard routing boundary — Jerry → Cerritos → Picard Summer's Verse
description: Le pipeline canonique Jerry (proposition de standard/score) → Cerritos/GTD (filtre, qualification, routage 48h) → Picard (instancie un Summer's Verse Project). Le boundary tient en trois gates : Cerritos inbox zero, routage <48h, Picard action <72h.
tags: [para, picard, cerritos, gtd, routing, pipeline, summer-verse]
generated: { by: minimax-m3, at: 2026-08-17T22:05:00Z }
verified:
  - { by: process:extraction-areas, at: 2026-08-17T22:05:00Z }
sources:
  - id: area-standard
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/AREA_STANDARD.md"
    title: Jerry Prime — LD01 Business Area Standard
    last_modified: 2026-05-21
  - id: jerry-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/Jerry_Areas_README.md"
    title: Jerry Areas - Spock Incube Operating Layer
    last_modified: 2026-05-22
  - id: a1-spec
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/A1_Jerry_Areas_Spec.md"
    title: A1 Jerry Areas Spec
    last_modified: 2026-05-21
okf_version: "0.2"
---

# Para-Picard routing boundary — Jerry → Cerritos → Picard Summer's Verse

Le pipeline canonique qui transforme une **idée** de Jerry en **Projet** daté est posé par `Jerry_Areas_README.md` §Doctrine et `AREA_STANDARD.md` §« Cerritos Handoff Protocol ». Trois agents, trois rôles, trois SLA.

## Le pipeline en 3 gates

```
Jerry (propose)
    ↓ standard / score / portfolio decision
Cerritos (filtre, qualifie, route)
    ↓ routage <48h vers Picard
Picard (instancie Summer's Verse)
    ↓ Project daté avec gates Graduation
Summer's Verse (exécute)
```

Trois gates avec SLA :

1. **Jerry → Cerritos** : chaque idée, opportunité, input stratégique est routé à Cerritos **first**. P7 AREA_STANDARD : « Cerritos First, Jerry Second ».
2. **Cerritos → Picard** : chaque idée routée à Picard **dans les 48h**. Cerritos log, triage, route.
3. **Picard → Summer's Verse** : Picard instancie le Project (Summer's Verse). Si Picard n'agit pas dans les 72h, **Jerry escalade à B1**.

## P7 — la règle « Cerritos First, Jerry Second »

`AREA_STANDARD.md` §« Operating Principles » P7 :

> *Ideas do not live in Jerry's head. They live in Cerritos until Picard moves them to Summer's Verse.*
> *Every idea, opportunity, or strategic input routes through Cerritos first.*
> *Jerry's filter : Jerry's role is to set criteria, not to receive directly.*
> *No Jerry-first execution : If Jerry is the first to act on an opportunity, the routing has failed.*

Trois conséquences opérationnelles :

- Jerry ne **reçoit pas** directement une idée — il **pose les critères** que Cerritos applique.
- Si Jerry commence à agir **avant** Cerritos, c'est un signal que le routage a cassé.
- Cerritos est l'inbox zéro du système — toute idée y passe avant d'aller ailleurs.

## Le routage Cerritos (decision tree)

`AREA_STANDARD.md` §« Cerritos Handoff Protocol » pose le decision tree :

```
INPUT RECEIVED
     │
     ▼
Is this a new IDEA or an EXISTING OPERATIONS issue?
     │
   IDEA ────────────────────────────────────────────────────► ROUTE TO CERRITOS
     │                                                   (Cerritos logs, triages,
     │                                                    routes to Picard within 48h)
     │
  EXISTING OPS
     │
     ▼
Does this require Jerry's strategic judgment? ──No──► ROUTE TO B2 MANAGER
     │                                                 (Jerry notified of resolution)
     │
   Yes
     │
     ▼
Is this > 30 min of Jerry's time? ──No──► Jerry handles, logs to Cerritos
     │                                   (Pattern detection : 3+ recurrences →
     │                                    WHO delegation, not HOW)
     │
   Yes
     │
     ▼
Is this blocking a Rock? ──Yes──► EMERGENCY ──► Jerry + B1 immediate
     │
   No
     │
     ▼
Is this > 4 hours? ──Yes──► Jerry + B1 strategy session
     │
   No
     │
     ▼
Jerry handles, logs to Cerritos
```

Le decision tree force **toute** entrée à passer par un filtre unique. Pas de court-circuit.

## Les Cerritos Minimum Standards

`AREA_STANDARD.md` §« Cerritos Minimum Standards » pose trois SLA non-négociables :

- **Inbox zero** : All inputs acknowledged within 4 hours during business days.
- **Routing SLA** : Every idea routed to Picard within 48 hours.
- **Escalation** : If Picard has not actioned within 72 hours → Jerry escalates to B1.
- **Weekly review** : Jerry + Cerritos operator weekly sync to review routing accuracy.

Trois choses à noter :

1. Cerritos a un SLA d'**acknowledgement** (4h) séparé du SLA de routage (48h). L'un ne remplace pas l'autre.
2. Le 72h Picard est l'**escalade automatique** — Jerry n'a pas à la demander.
3. Le weekly review est la rétro-alimentation qui maintient la précision du routage.

## Le Picard Summer's Verse handoff

Quand Cerritos route vers Picard, le packet doit contenir (`AREA_STANDARD.md` §« Picard Summer's Verse Handoff ») :

| Élément | Requirement |
|---|---|
| **Context** | Full background on why this idea matters |
| **Desired outcome** | What success looks like |
| **Constraints** | What's fixed vs flexible |
| **Deadline** | When decision or action is needed |
| **Authority** | What Picard can decide independently |
| **Escalation path** | When to push back vs when to act |

Sans ces six éléments, le packet est incomplet et Picard ne peut pas instancier un Summer's Verse correctement.

## Le rôle de Beth dans le pipeline

Beth est l'**HALT veto authority**. Elle n'est pas dans le pipeline de routage normal, mais elle peut **interrompre** n'importe quelle étape si Life OS charge trop, ou si LD03/LD04 passent en RED. Voir concept `jerry-bio-hard-safety-doctrine.md` §Beth HALT veto.

## Le boundary Spock / Picard / Cerritos

Trois officiers avec trois rôles distincts :

- **Spock** : classifie l'item comme Area / Project / Resource / Archive (voir `area-vs-project-classification.md`). Si l'item a une deadline et un livrable, il route vers Picard.
- **Cerritos (GTD)** : opère le filtre, le triage, et le routage des idées. C'est l'opérateur du pipeline.
- **Picard** : instancie le Summer's Verse. C'est le **createur** de Projects.

Jerry est entre Spock et Cerritos : il **incube** l'Area, **propose** des standards/scores, mais ne crée pas le Project.

## Le risque spécifique

Jerry qui ouvre directement un Project sans passer par Cerritos = **routing failure**. Symptômes : décisions Jerry qui ne sont pas loggées dans Cerritos, scorecards sans provenance, Summer's Verse qui n'ont pas de contexte. Parade : P7 (« Cerritos First, Jerry Second ») appliquée strictement.

Cerritos qui ne route pas dans les 48h = **bottleneck systemique**. Symptôme : ideas s'accumulent, Jerry escalations augmentent. Parade : weekly review Cerritos + Jerry pour identifier les bottlenecks.

Picard qui n'agit pas dans les 72h = **Jerry escalates à B1**. Pas d'exception.