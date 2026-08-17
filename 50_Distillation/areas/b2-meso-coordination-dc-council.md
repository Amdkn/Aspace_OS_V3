---
type: Concept
title: B2 meso coordination — le DC Direction Council
description: Le DC Direction Council (les 8 hero-managers B2) reçoit les mandates B1, résout les tradeoffs meso, et garde B1 hors du churn opérationnel. Trois modes : parallel, handoff, negotiation.
tags: [b2, council, meso, dc, hero-managers, coordination]
generated: { by: minimax-m3, at: 2026-08-17T21:20:00Z }
verified:
  - { by: process:extraction-areas, at: 2026-08-17T21:20:00Z }
sources:
  - id: dc-council
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/B2_DC_DIRECTION_COUNCIL_WORKFLOW.md"
    title: B2 DC Direction Council Workflow
    last_modified: 2026-05-27
  - id: fractal-arch
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md"
    title: L2 Business — The B1 / B2 / B3 Fractal Architecture
    last_modified: 2026-06-02
okf_version: "0.2"
---

# B2 meso coordination — le DC Direction Council

Le **DC Direction Council** est l'instance d'arbitrage meso entre les 8 hero-managers B2. Son rôle est sans appel : recevoir les mandates B1, résoudre les tradeoffs entre domaines, et **garder B1 hors du churn opérationnel**.

## Les 8 membres du Council

Liste canonique depuis `B2_DC_DIRECTION_COUNCIL_WORKFLOW.md` §« Council Members » :

- **Superman** — Growth
- **Martian Manhunter / John Jones** — Sales
- **Flash** — Product
- **Batman** — Ops
- **Cyborg** — IT
- **Wonder Woman** — Finance
- **Green Lantern** — People
- **Aquaman** — Legal

Les 8 noms sont invariants. Renommer un hero = décision B1 documentée. Modifier l'attribution de domaines = décision B1 + ratification A0.

## La routine du Council

`B2_DC_DIRECTION_COUNCIL_WORKFLOW.md` §« Council Routine » pose 8 étapes :

1. Intake B1 mandate ou B2 peer issue.
2. Identifier les domaines impactés.
3. Chaque B2 impacté énonce son DoD, blocker et boundary non-négociable.
4. Council sélectionne un mode parmi trois : **parallel**, **handoff**, ou **negotiation**.
5. B2s créent ou updatent Rocks et DoD packets.
6. B2s dispatchent B3 JTBD packets.
7. Council log la décision meso.
8. Escalade à B1 **seulement** si authority ou North Star changes sont requis.

## Les trois modes de coopération

**Parallel** : les domaines impactés peuvent agir indépendamment, sans dépendance séquentielle. Pas d'arbitrage requis entre eux. Le Council log les DoDs parallèles.

**Handoff** : un domaine doit finir avant qu'un autre commence. Le séquencement est documenté dans la décision meso avec dates explicites.

**Negotiation** : ≥2 DoDs sont en conflit et nécessitent un tradeoff. Le Council arbitre en équilibrant les boundary non-négociables de chaque B2 impacté. Si aucun arbitrage ne préserve la wheel 8-domain, **escalade à B1**.

## Le Meso Decision Packet

Chaque arbitrage produit un packet YAML court (Council Workflow §« Meso Decision Packet ») :

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

## La règle d'escalade

Le Council escalade à B1 **seulement si** il ne peut pas préserver la wheel 8-domain tout en restant dans :

- North Star courant
- cycle priority courante
- authority bounds courantes
- risk appetite courant

Si une de ces quatre contraintes est touchée, l'arbitrage B2 est insuffisant et B1 doit trancher. Dans tous les autres cas, le Council résout.

## Pourquoi un Council et pas un seul B2 owner

Le Council existe parce que les tradeoffs inter-domaines sont la **norme**, pas l'exception. Un Sales qui promet une livraison en 7 jours sans consulter Ops = engagement sans feasibility check. Un Growth qui demande un budget sans Finance = scale sans runway check. Un Product qui ship sans Legal = exposure non couverte. Le Council force la conversation **avant** que les engagements contradictoires ne deviennent des incidents.

## Le lien avec les pair checks

Les pair checks de la matrice d'harmonisation (`business-wheel-harmonization-matrix.md`) sont le **substrat** que le Council arbitre. Un pair check qui échoue = un arbitrage meso à faire. Un red flag = un blocage potentiel qui peut escalader.

## Le risque spécifique

Un Council qui **escalade trop** est un signal : soit les B2 owners n'ont pas l'autorité nécessaire, soit North Star n'est pas clair. Un Council qui **n'escalade jamais** est suspect : soit les décisions sont trop faciles, soit les B2 owners ne signalent pas les vrais conflits. La cadence normale est *« escalader 5-15% des cas »*.