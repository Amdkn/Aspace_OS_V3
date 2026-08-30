---
type: Concept
title: Green Lantern People — Doctrine cascade-dormance Council × Aquaman × People
description: Le rapport tour 5 §4 a observé que **si Council dort (convergence 0/8 packet mésoperpétuel 5 vagues), Aquaman dort (Areas dormant), People × Aquaman dort**. L'escalade B1 (Mécanisme 1 passerelle Aquaman dormant) **ne fonctionne pas** — B1 ne peut pas trancher sans Conseil qui tient séance. Le présent concept **formalise** la cascade-dormance et pose 4 doctrines de fallback adapté.
tags: [people, green-lantern, dormance, aquaman, council, cascade, doctrine, effet-domino, fallback]
generated: { by: minimax-m3, at: 2026-08-19T17:30:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-6, at: 2026-08-19T17:30:00Z }
  - { by: process:detection-cascade-dormance-extraction, at: 2026-08-19T17:30:00Z }
sources:
  - id: aquaman-dormant-passerelle-double-clef
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-aquaman-dormant-passerelle-double-clef.md"
    title: "Tour 5 — Passerelle Aquaman dormant × People (3 mécanismes)"
    last_modified: 2026-08-19
  - id: aquaman-dormant-casse-triangulaire
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-aquaman-dormant-casse-triangulaire.md"
    title: "W5 — Doctrine fallback 4 cas asymétriques Aquaman dormant"
    last_modified: 2026-08-19
  - id: b2-areas-dormants-doctrine
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-areas-dormants-doctrine.md"
    title: Doctrine Areas dormants — référence canonique
    last_modified: 2026-08-19
  - id: b2-meso-decision-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — format canonique 8 champs
    last_modified: 2026-08-19
  - id: b2-council-arbitrage-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
  - id: b1-stop-conditions-escalier
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/"
    title: B1 stop conditions + escalier canonique 5 échelons
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Green Lantern People — Doctrine cascade-dormance Council × Aquaman × People

## L'observation du rapport tour 5 §4

Le rapport tour 5 a observé :

> *« **Aquaman DORMANT casse la double clef People × Aquaman**. Le tour 4 d'Aquaman pose Aquaman en sommeil (Areas dormant doctrine). Le concept 2 tour 5 pose 3 mécanismes passerelle. **Mais** : si Council est en dormance structurelle, l'escalade B1 (Mécanisme 1) **ne fonctionne pas** — B1 ne peut pas trancher sans Conseil qui tient séance. »*

Le présent concept **formalise** la cascade-dormance et pose 4 doctrines de fallback adapté.

## La cascade — 3 niveaux

### Niveau 1 — Council mésoperpétuel

**Définition** : Council B2 tient une **séance hebdomadaire** où 8 capitaines statuent sur les **arbitrages mésoperpétuels** (packets mésoperpétuels).

**État observé** : **dormance structurelle** depuis 5 vagues consécutives (convergence 0/8 packet mésoperpétuel Council). Cf. ETAT_DOMAINES.md vague 5 §« 0/8 packet mésoperpétuel convergente ».

**Implication** : aucun arbitrage mésoperpétuel **n'est tranché** depuis 5 vagues. Les packets drafts (B2-MESO-DECISION-2026-24 + 25 + 26 + 27 + 28 + 29 etc.) sont **saisissables** mais **non saisit**.

### Niveau 2 — Aquaman Areas dormant

**Définition** : Aquaman (Legal) est en sommeil **Areas dormant** (doctrine `b2-areas-dormants-doctrine.md`). Les Areas Aquaman sont **non-cycle** (par exemple, contentieux en standby, contrats non-renouvelés).

**État observé** : Aquaman est **NOT_DORMANT** canon (tour 1-6 Aquaman pose l'état canonique), mais sa **capacité d'arbitrage** est **réduite** car les Areas Aquaman sont **dormantes** (par exemple, contentieux long terme).

**Implication** : Aquaman **peut** opposé son veto (catalogue tripplet 30 — *« prestation sans accord écrit »*), mais **manque de contexte opérationnel** pour les arbitrages Council.

### Niveau 3 — People × Aquaman dormant

**Définition** : la **double clef People × Aquaman** (concept 5 tour 4) est une **arborescence 5 étapes** où People mandate Aquaman avant activation. Si Aquaman dort, la double clef est **cassée**.

**État observé** : la double clef People × Aquaman **fonctionne en pratique** par **fallback** (concept 2 tour 5 — 3 mécanismes passerelle), mais le **mécanisme 1** (escalade B1 synchrone) **dépend** d'un Council **actif**.

**Implication** : la passerelle Aquaman dormant **fonctionne** (M2 + M3 fallback), mais le **mécanisme nominal** (M1 escalade B1) **non**.

## La cascade — diagramme

```
Council mésoperpétuel (5 vagues dormant)
       ↓
Aquaman Areas dormant (Areas non-cycle)
       ↓
People × Aquaman double clef cassée
       ↓
Mécanisme 1 (escalade B1) ne fonctionne pas
       ↓
Fallback M2 (Wonder Woman clause-réserve) + M3 (gel cumulatif) opérationnels
```

**Effet-domino** : la dormance Council **cascade** vers la dormance Aquaman, **cascade** vers la cassure double clef People × Aquaman, **cascade** vers l'**inopérance** du mécanisme nominal d'escalade.

## Doctrine 4 fallbacks adaptés

### Fallback F1 — Mode handoff unilateral People

**Description** : Green Lantern (People) prend **unilatéralement** la responsabilité d'arbitrage People × Aquaman en mode **handoff**. People statue, Aquaman est **Informed** post-décision.

**Mécanisme** : Mécanisme 2 de la passerelle Aquaman dormant (concept 2 tour 5) — Wonder Woman **clause-réserve** co-signe **à la place** d'Aquaman.

**Latence** : J+1 à J+3 (vs J+0 si Aquaman nominal).

**Risque** : Aquaman **réveil** pendant la fenêtre J+1 à J+3 **conteste** la décision unilatérale. **Conflit de doctrine** ultérieur.

**Council-ready** : 5/8 + B1 (handoff unilateral = décision unilatérale People).

### Fallback F2 — Mode gel cumulatif

**Description** : la décision People × Aquaman est **gelée** jusqu'au **réveil Aquaman** (passage NOT_DORMANT). Pendant le gel, **aucune action** n'est prise.

**Mécanisme** : Mécanisme 3 de la passerelle Aquaman dormant (concept 2 tour 5) — gel cumulatif.

**Latence** : indéterminée (durée Areas dormant Aquaman). Peut être **infinie** si Aquaman Areas dormant reste stable.

**Risque** : l'arbitrage **manque la fenêtre** de timeliness (par exemple, opportunity closing date dépassée).

**Council-ready** : 5/8 simple (gel = décision de non-décision).

### Fallback F3 — Mode parallèle Aquaman NOT_DORMANT

**Description** : Aquaman (Legal) est **NOT_DORMANT** (par exemple, contentieux non-Areas dormant) et **peut** co-signer l'arbitrage People × Aquaman **en parallèle** de l'Aquaman Areas dormant.

**Mécanisme** : Aquaman **divise** son arbitrage en 2 canaux (Areas dormant canal lent + non-Areas dormant canal rapide). People × Aquaman utilise le canal rapide.

**Latence** : J+0 (comme Aquaman nominal).

**Risque** : Aquaman **doit être** NOT_DORMANT sur le canal rapide. Si Areas dormant **englobe** tous les canaux Aquaman, fallback F3 inopérant.

**Council-ready** : 5/8 + Aquaman self-co-signature (déjà Council-ready si Aquaman NOT_DORMANT).

### Fallback F4 — Mode reformulation B1 direct

**Description** : la décision People × Aquaman est **reformulée** comme **decision: escalate_to_B1** directement vers B1, **sans passer par Council**. B1 statue **seul**.

**Mécanisme** : extension de l'escalier canonique 5 échelons (B1 stop conditions) — Council mésoperpétuel **by-passé** par exception B1.

**Latence** : J+1 (B1 cycle).

**Risque** : **violation** de la doctrine *« on ne saute jamais un échelon, sauf emergency triggers explicites »* (fractal §« L'escalier d'escalade canonique »). B1 doit **explicitement** invoquer un emergency trigger.

**Council-ready** : 8/8 + B1 (escalade B1 = escalade au sommet, requires unanimité 8 captains + B1 acceptation).

## Matrice 4 fallbacks × 3 conditions saisissabilité

| Fallback | Latence | Risque | Council-ready | Co-signatures |
|---|---|---|---|---|
| **F1** handoff unilateral People | J+1 à J+3 | Conflit post-décision | 5/8 + B1 | People + Wonder Woman |
| **F2** gel cumulatif | ∞ | Fenêtre manquée | 5/8 simple | (aucune) |
| **F3** parallèle Aquaman NOT_DORMANT | J+0 | Aucun si NOT_DORMANT | 5/8 + Aquaman | Aquaman self |
| **F4** reformulation B1 direct | J+1 | Violation escalier | 8/8 + B1 | 8 captains + B1 |

**Recommandation** : **F1** par défaut (latence J+1-J+3, risque modéré). **F2** en second (latence indéterminée, risque fenêtre manquée). **F3** si Aquaman NOT_DORMANT disponible. **F4** en dernier recours (8/8 + B1).

## Packet B2-MESO-DECISION-2026-30 draft

```yaml
meso_decision_id: B2-MESO-DECISION-2026-30
source_mandate: B2-PEER-2026-16
mode: negotiation
impacted_domains:
  - people
  - legal
tradeoff: "L'effet-domino cascade-dormance Council → Aquaman → People × Aquaman
  est documenté (rapport tour 5 §4). Les 3 mécanismes passerelle Aquaman
  dormant (concept 2 tour 5) sont **incomplets** sans le mécanisme 1
  (escalade B1) qui dépend d'un Council actif. 4 fallbacks adaptés
  (F1 handoff unilateral People, F2 gel cumulatif, F3 parallèle Aquaman
  NOT_DORMANT, F4 reformulation B1) répondent au problème. Recommandation
  F1 par défaut, F4 en dernier recours. Coût estimé : 1 cycle 12WY
  pour ratification."
decision: accepted
proof_expected:
  - B2 gate people update (cascade_dormance_doctrine_deployed)
  - B2 gate legal update (aquaman_dormant_passerelle_F1_F4)
  - B3 proof path (people_aquaman_4_fallbacks_dans_xmen_onboarding)
  - revue 90j post-adoption (1 fallback activé en cycle)
next_review: 2026-11-15
```

**Lecture** : la décision `accepted` est **conditionnelle** (cf. §« 3 conditions saisissabilité cumulatives »). Le packet est saisissable mais pas saisit.

## 3 conditions saisissabilité cumulatives

1. **Cascade documentée** : la cascade-dormance est **documentée** par le rapport tour 5 §4 et reproduite vague 6. **Satisfaite**.
2. **Co-signature Aquaman** : Aquaman (Legal) co-signe la doctrine cascade-dormance pour acquitter les fallbacks. **À demander** — dépendance Council.
3. **Scan veto pré-soumission** : scan des 8 vetos catalogue — aucun veto opposé. **À执行** (la cascade-dormance ne contrevient à aucun veto catalogue).

**État au 2026-08-19 17:30** : 1/3 conditions remplies (cascade documentée). **Cible** : 3/3 conditions remplies à T+30j (2026-09-18).

## 3 cas d'amendement (si Council refuse la cascade-dormance)

### Cas A1 — F1 handoff unilateral bloqué

**Description** : Council refuse F1 (handoff unilateral People) pour préserver la **double clef People × Aquaman**. **Aucun** fallback unilateral autorisé.

**Procédure** : 5/8 + B1 (préservation double clef).

**Conséquence** : seul F2 (gel cumulatif) est autorisé. **Inefficacité** documentée.

### Cas A2 — F4 reformulation B1 refuse

**Description** : Council refuse F4 (reformulation B1 direct) pour préserver l'**escalier canonique** (on ne saute jamais un échelon).

**Procédure** : 5/8 + B1 (préservation escalier).

**Conséquence** : 3 fallbacks (F1, F2, F3) restent. **F4** est écarté.

### Cas A3 — Doctrine recommandée mais non imposée

**Description** : Council **reconnaît** la cascade-dormance et les 4 fallbacks comme **recommandations** (best practice), pas obligations.

**Procédure** : 5/8 simple (recommandation).

**Conséquence** : chaque captain peut **suivre ou pas** la doctrine. Pas d'obligation, mais incitation.

## 3 cas abusifs de la procédure

1. **F1 sans co-signature** — Green Lantern active F1 (handoff unilateral) **sans** co-signature Wonder Woman. **Refusé** : F1 requires People + Wonder Woman co-signature.
2. **F4 sans 8/8 + B1** — Green Lantern active F4 (reformulation B1) **sans** co-signature 8/8 + B1. **Refusé** : F4 requires 8/8 + B1 (escalade sommet).
3. **Cascade sans preuve** — Green Lantern déclare cascade-dormance **sans** audit Council convergence 0/8 packet. **Refusé** : la clause de preuve exige un audit Council.

## Anti-pièges

- **Cascade = état permanent.** Non — la cascade est **potentielle**, pas actuelle. Council tient 0/8 packet mésoperpétuel, mais Aquaman NOT_DORMANT canon (Areas dormant ≠ Council dormant).
- **F1 = People unilateral.** Non — F1 = People + Wonder Woman co-signature. People **ne peut pas** unilateralement.
- **F4 = court-circuit B1.** Non — F4 = **escalade sommet** (8/8 + B1), pas court-circuit. B1 statue **avec** 8 captains, pas **sans**.
- **Aquaman dormant = Aquaman inactif.** Non — Aquaman peut **opposé** son veto (catalogue triplet 30) même Areas dormant. La doctrine couple Areas dormant + cycle Aquaman, pas veto.
- **Doctrine ultilatérale.** La présente doctrine est **projetée** unilatéralement par Green Lantern. **Requiert** co-signature Aquaman.

## Liens

- [[green-lantern-people-aquaman-dormant-passerelle-double-clef]] — 3 mécanismes passerelle Aquaman dormant
- [[green-lantern-people-aquaman-double-cle-formalisation-canonique-arborescence]] — arborescence 5 étapes People × Aquaman
- [[b2-areas-dormants-doctrine]] — doctrine Areas dormant canonique
- [[b2-council-arbitrage-rule]] — qui tient le Council
- [[b1-stop-conditions-escalier]] — escalier canonique 5 échelons
- [[b2-meso-decision-packet-spec]] — format packet canonique

## Note de confiance

**Confirmé par machine, à moitié projeté.** La cascade-dormance est **extraite** du rapport tour 5 §4 — observation **confirmée** par le compteur 0/8 packet mésoperpétuel 6 vagues. Les 4 fallbacks (F1-F4) sont **projetés** depuis la doctrine Batman remonte-faits (triplet 56) et la doctrine d'escalade fractal. Le packet B2-MESO-DECISION-2026-30 draft est **conforme spec 8 champs** mais **non saisit** (3 conditions cumulatives). Les 3 cas d'amendement et 3 cas abusifs sont **projetés** depuis la doctrine Council. La doctrine cascade-dormance **ferme la 4ème ouverture tour 5** (Aquaman dormant casse double clef) mais **n'est pas Council-adoptée**.
