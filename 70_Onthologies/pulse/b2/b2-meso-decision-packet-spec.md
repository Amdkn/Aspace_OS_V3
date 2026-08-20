---
type: Concept
title: Meso Decision Packet — le format canonique d'une décision B2
description: Chaque arbitrage B2 Council produit un packet YAML court, append-only dans `B2_DC_DIRECTION_COUNCIL_DECISIONS.md`. Champs obligatoires : id, source mandate, mode, impacted domains, tradeoff, decision, proof expected, next review. Format doctoriné par D4 append-only.
tags: [b2, meso, decision, packet, yaml, format, d4]
generated: { by: minimax-m3, at: 2026-08-19T02:00:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T02:00:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: dc-workflow
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/B2_DC_DIRECTION_COUNCIL_WORKFLOW.md"
    title: B2 DC Direction Council Workflow
    last_modified: 2026-05-27
  - id: omk-project
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/omk-business-os.md"
    title: OMK Business OS — Triptyque V4 status ACTIVE 2026-07-15
    last_modified: 2026-08-17
  - id: b1-mandate
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-mandate-packet-spec.md"
    title: B1 mandate packet spec
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Meso Decision Packet — le format canonique d'une décision B2

## Pourquoi un format strict

Le B2 Council prend plusieurs arbitrages par cycle 12WY. Sans
format, le journal devient un fourre-tout de styles et la traçabilité
du *qui a tranché quoi* devient impossible. La doctrine D4 (append-only)
exige aussi que toute décision ait un identifiant stable — sinon
l'historique ne peut pas être reconstitué.

## Le gabarit YAML

Tiré verbatim de `B2_DC_DIRECTION_COUNCIL_WORKFLOW.md` §« Meso Decision
Packet » :

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

Chaque champ est obligatoire. Le packet est invalide s'il manque un
champ — et un packet invalide n'a pas de force d'arbitrage.

## Les champs — un par un

### `meso_decision_id`

Format : `B2-MESO-DECISION-YYYY-NN` (année sur 4 chiffres,序号
sur 2 chiffres). Compteur annuel, reset à chaque 12WY cycle. **Jamais
réutilisé** — un id mort reste dans le journal à titre d'archive.

### `source_mandate`

Le mandate B1 qui a déclenché l'arbitrage. Si l'arbitrage provient
d'un problème B2 pair (pas d'un mandate), le champ prend la valeur
`B2-PEER-YYYY-NN` (problème identifié par un capitaine B2 en revue).

### `mode`

L'un des trois modes (cf. `b2-three-cooperation-modes.md`). Le champ
est figé à la décision initiale. Un changement de mode en cours
d'exécution **est un nouveau packet**, pas une édition du premier.

### `impacted_domains`

Liste des 8 domaines B2 (growth, sales, product, ops, it, finance,
people, legal) qui sont touchés par l'arbitrage. Une liste vide est
invalide — soit l'arbitrage ne touche aucun domaine (donc il n'est
pas un arbitrage B2), soit le scan n'a pas été fait.

### `tradeoff`

Une à trois phrases. Décrit ce qui est sacrifié et ce qui est gagné.
**Pas** la justification morale (ça, c'est le journal Council). **Pas**
le détail opérationnel (ça, c'est le packet B3).

### `decision`

Trois valeurs possibles :

- `accepted` — l'arbitrage est tronqué, mode choisi, packet dispatché.
- `blocked` — un red flag matrice d'harmonisation bloque l'arbitrage;
  le packet est conservé comme historique de blocage, mais aucun B3
  dispatch n'est produit.
- `escalate_to_B1` — l'arbitrage remonte à B1 ; le packet est conservé
  comme motif d'escalade.

### `proof_expected`

Liste de 2 à 4 éléments. Chacun est soit une B2 gate update (un état
de gate qui doit changer), soit un B3 proof path (un chemin de preuve
à inspecter). Sans proof_expected, le packet est un voeu pieux, pas
une décision.

### `next_review`

Date (`YYYY-MM-DD`) ou cycle (`12WY-2026-Q3`). Indique quand le
Council **doit** ré-évaluer cette décision pour confirmer qu'elle a
produit l'effet attendu. Trois contextes obligent à raccourcir le
next_review : (1) un red flag matrice, (2) un veto catalogue, (3)
un risque identifié dans le tradeoff.

## Append-only — la règle D4

Le fichier `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` est append-only.
Aucune ligne existante n'est éditée. Une décision qui change de mode
produit un nouveau packet. Une décision qui devient caduque (mission
annulée, pivot de cycle) est marquée caduque par un packet séparé
qui pointe sur l'id d'origine.

C'est la même doctrine D4 que OMK Business OS (mentionnée dans
`omk-business-os.md` §« Doctrine — D4, D6, Spec-Loop »). Le packet
mésoperpétuel hérite de la doctrine mésoperpétuelle.

## Exemple — pivot US 2026-07-15

Imaginons un arbitrage B2 sur le pivot marché US décidé par B1 le
2026-07-15 (cf. `omk-business-os.md`). Le packet pourrait être :

```yaml
meso_decision_id: B2-MESO-DECISION-2026-15
source_mandate: B1-B2-MANDATE-2026-21
mode: negotiation
impacted_domains:
  - growth
  - sales
  - finance
tradeoff: "Pivot US premium B2B $7.5-25K ACV — abandonnement des références EUR
  historiques non nettoyées. Wonder Woman étend la doctrine veto-dépense avec
  ROI à 30 jours."
decision: accepted
proof_expected:
  - B2 gate finance update (depense_recurrente_now_chiffree)
  - B2 gate sales update (offre_US_premium_lancee)
  - B3 proof path (Sales_Illuminati_ABM_Linkedin_qualified_30d)
next_review: 2026-09-15
```

Le packet est **vérifiable** sans faire confiance à l'auteur — trois
proof_expected, trois chemins distincts, un cycle de revue aligné sur
le pivot (60 jours).

## Anti-pièges

- **Packet en prose.** Un packet sans YAML est un packet sans
  identifiant, sans mode, sans impacted_domains. Il n'a pas de force
  d'arbitrage.
- **Packet incomplet.** Un champ manquant est un signal de scan non
  terminé. Le Council doit refuser le packet ou le compléter
  explicitement.
- **Packet sans next_review.** Indique une décision qui ne sera
  jamais ré-évaluée. C'est un voeu, pas une décision.
- **Packet avec un id réutilisé.** Casse la traçabilité. D4 l'interdit
  explicitement.
- **Confidentialité du tradeoff.** Si le tradeoff est trop sensible
  pour être écrit, c'est un escalate_to_B1, pas un packet mésoperpétuel.

## Liens

- [[b2-council-arbitrage-rule]] — qui tient le Council
- [[b2-three-cooperation-modes]] — la signification de `mode`
- [[b2-harmonization-matrix-exploitable]] — les red flags qui peuplent `decision: blocked`
- [[b1-mandate-packet-spec]] — l'amont B1/B2

## Note de confiance

**Confirmé par machine.** Le gabarit YAML est tiré verbatim de
`B2_DC_DIRECTION_COUNCIL_WORKFLOW.md`. Les 7 champs et leurs
significations sont reformulés à partir du contexte du fichier. La
règle D4 append-only et l'exemple de pivot US sont **extrapolés** à
partir de la doctrine OMK (T1/T2/T3) et du statut ACTIVE 2026-07-15.
