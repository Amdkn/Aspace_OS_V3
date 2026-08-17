---
type: Concept
title: Harmonisation de la wheel — pair checks et red flags
description: La matrice d'harmonisation B2 vérifie les appariements de domaines deux à deux (Growth×Sales, Sales×Ops, etc.) et identifie les combinaisons de drapeaux rouges qui doivent bloquer un lancement même si un seul domaine passe au vert.
tags: [harmonization, b2, red-flags, b2-council, gates]
generated: { by: minimax-m3, at: 2026-08-17T21:00:00Z }
verified:
  - { by: process:extraction-areas, at: 2026-08-17T21:00:00Z }
sources:
  - id: harmonization
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md"
    title: B2 Business Wheel Harmonization Matrix
    last_modified: 2026-05-27
  - id: council
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/B2_DC_DIRECTION_COUNCIL_WORKFLOW.md"
    title: B2 DC Direction Council Workflow
    last_modified: 2026-05-27
okf_version: "0.2"
---

# Harmonisation de la wheel — pair checks et red flags

Une wheel Business peut afficher huit domaines au vert tout en étant **inopérante** : il suffit que les transitions entre domaines soient cassées. La matrice d'harmonisation teste ces transitions deux à deux, et **bloque** un lancement quand une combinaison de red flags rend l'ensemble incohérent.

## Les 9 pair checks canoniques

Tirés de `B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md` §« Domain Pair Checks » :

| Paire | Question | Escalade si non résolu |
|---|---|---|
| Growth × Sales | L'attention devient-elle opportunité qualifiée ? | B2 Council |
| Sales × Ops | Les promesses peuvent-elles être tenues répétitivement ? | B2 Council |
| Product × Ops | L'artefact est-il supportable opérationnellement ? | B2 Council |
| Product × IT | Le produit tourne-t-il, déploie, récupère, est-il accessible ? | B2 Council |
| Finance × Growth | La dépense est-elle justifiée par l'apprentissage ou la traction ? | B2 Council |
| Finance × Product | Le coût de build protège-t-il la marge ? | B2 Council |
| Legal × Growth | Les claims sont-ils safe ? | B2 Council |
| Legal × Product | Les frontières IP/privacy/terms sont-elles claires ? | B2 Council |
| People × All | La propriété et la charge sont-elles tenables ? | B2 Council, ou B1 si structurel |

Chaque pair check teste un **transfert** : passer une responsabilité d'un domaine à l'autre. Si le transfert ne marche pas, le B2 Council doit arbitrer — pas B1, pas B3.

## Les 5 red flags

Toujours depuis la même matrice :

1. **Product green, Ops/IT red** : ne pas lancer. Le produit ne peut pas être livré ou maintenu.
2. **Growth green, Sales red** : valider l'offre avant de scaler l'attention.
3. **Sales green, Ops/People red** : risque de charge de livraison (la promesse ne pourra pas être tenue).
4. **Finance red + Growth/Product green** : ralentir ou re-pricer. Le cash ne suit pas.
5. **Legal red + public-facing work** : geler les claims et le launch.

Ces combinaisons sont **des arrêts durs** : la wheel affiche du vert sur un domaine, mais l'ensemble reste non-livrable. C'est précisément le piège que la wheel simple-rate ne détecte pas.

## Le B2 Council comme instance d'arbitrage

`B2_DC_DIRECTION_COUNCIL_WORKFLOW.md` pose le Council comme instance d'arbitrage :

- Membres : les 8 hero-managers B2.
- Routine : intake d'un mandate B1 ou d'un problème B2 pair → identification des domaines impactés → chaque B2 impacted énonce son DoD, blocker et boundary non-négociable → sélection du mode (parallel / handoff / negotiation) → création ou update des Rocks et DoD → dispatch B3 JTBD → log de la décision meso.
- **Escalade à B1 seulement** si le Council ne peut pas préserver la wheel 8-domain tout en restant dans North Star, cycle, autorité et appétit pour le risque courants.

Trois modes de coopération entre B2 :

- **parallel** : les domaines peuvent agir indépendamment.
- **handoff** : un domaine doit finir avant qu'un autre commence.
- **negotiation** : deux DoDs ou plus sont en conflit et nécessitent un tradeoff.

## Le format de décision meso

Chaque arbitrage produit un packet YAML court (`B2_DC_DIRECTION_COUNCIL_WORKFLOW.md` §« Meso Decision Packet ») :

```yaml
meso_decision_id: B2-MESO-DECISION-YYYY-NN
source_mandate: B1-B2-MANDATE-YYYY-NN
mode: parallel | handoff | negotiation
impacted_domains:
  - domain
tradeoff: short statement
decision: accepted | blocked | escalate_to_B1
proof_expected:
  - B2 gate update
  - B3 proof path
next_review: date-or-cycle
```

## Cadence de revue

- **Weekly** pendant les cycles de build actif.
- **Immédiatement avant** un launch ou un commitment public.
- **Après** tout B3 blocker qui touche un autre domaine.

Trois contextes où la matrice doit être ré-évaluée explicitement. Une cadence de revue plus espacée (mensuelle, trimestrielle) rate les dérives naissantes.

## Pourquoi cette matrice existe

Sans la matrice, un domaine fort **peut masquer** une readiness faible ailleurs. Le cas typique : Growth green parce que paid media marche, Ops red parce que le support s'effondre, et le lancement explose en rétention. La matrice force la conversation inter-domaines **avant** que le damage ne soit visible.