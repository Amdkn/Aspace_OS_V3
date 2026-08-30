---
type: Concept
title: JohnJones — généralisation 8-domain de la procédure de remplacement 0 cas/60j (Council-ready canonical)
description: Ferme l'ouverture tour 4 R4 (procédure de remplacement 0 cas/60j doit être généralisable aux 8 domaines) en un packet mésoperpétuel Council-ready. Batman tour 5 procédure 6 étapes fournit le cadre d'amendement RACI unanime 8/8 + B1. Le concept pose les 4 étapes canonicalisées (recaractérisation, revue, arbitrage, dissolution/amendement), les 3 compteurs discriminants par veto (reformulation-validée Sales, périmètre-propriétaire Aquaman, …), et la procédure d'agrégation Council 8-domain.
tags: [b2, johnjones, sales, 8-domain, procedure-remplacement, 0-cas, 60j, generalisation, canonical, packet, council-ready]
generated: { by: minimax-m3, at: 2026-08-19T08:30:00Z }
verified:
  - { by: process:lecture-corpus-tour-5-john-jones, at: 2026-08-19T08:30:00Z }
sources:
  - id: jj-tour4-procedure
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-protocole-empirique-zero-cas-procedure-remplacement.md"
    title: "JohnJones protocole empirique 0 cas — procédure remplacement 4 étapes"
    last_modified: 2026-08-19
  - id: batman-tour5-procedure
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-procedure-amendement-raci-unanime-8-8-b1-format-complet.md"
    title: "Batman procédure amendement RACI 6 étapes — unanime 8/8 + B1"
    last_modified: 2026-08-19
  - id: aquaman-tour5-dormance
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-dormance-doctrine-canonique-alignement.md"
    title: "Aquaman dormance doctrine canonique alignement — 3 états DORMANT/SHADOW_ACTIVE/ACTIF"
    last_modified: 2026-08-19
  - id: packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — format canonique 8 champs
    last_modified: 2026-08-19
  - id: b2-vetoes-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: B2 eight domain vetoes catalogue — 8 vetos un par capitaine
    last_modified: 2026-08-19
  - id: areas-dormants-doctrine
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-areas-dormants-doctrine.md"
    title: B2 Areas dormants doctrine — 3 états
    last_modified: 2026-08-19
  - id: b2-council-arbitrage
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council arbitrage rule
    last_modified: 2026-08-19
okf_version: "0.2"
---

# JohnJones — généralisation 8-domain de la procédure de remplacement 0 cas/60j

## Pourquoi ce packet maintenant

L'ouverture tour 4 R4 était : *« La procédure de remplacement 0
cas/60j doit être généralisable aux 8 domaines »*. JohnJones tour 4
(concept 1) avait posé une procédure 4 étapes (recaractérisation /
revue / arbitrage / dissolution-amendement) pour son propre compteur
discriminant (≥ 1 reformulation validée /60j). Mais la procédure
n'était **pas canonique** — les 7 autres Captains qui rencontrent
0 cas/60j sur leur veto ne pouvaient pas s'en saisir comme précédent.

Batman tour 5 (concept 4 `batman-procedure-amendement-raci-unanime-8-8-b1-format-complet.md`)
pose la procédure d'amendement RACI en 6 étapes avec délais
1+1+2-4+1+1+0.2 sem. Le présent packet utilise ce cadre pour
proposer la **généralisation 8-domain** comme packet mésoperpétuel
Council-ready, saisissable sous 3 conditions cumulatives.

## Le gabarit packet Council-ready

```yaml
meso_decision_id: B2-MESO-DECISION-2026-47
source_mandate: B2-PEER-2026-25  # problème identifié par Captains Sales + Ops + 6 autres en revue
mode: negotiation
impacted_domains:
  - sales
  - ops
  - growth
  - product
  - it
  - finance
  - people
  - legal
tradeoff: "Procédure 0 cas/60j généralisée 8-domain. Chaque Captain propose son compteur discriminant (1 par veto). Council agrège ou statue. Procédure 4 étapes canonicalisées (recaractérisation → revue → arbitrage → dissolution/amendement). Procédure d'amendement RACI 6 étapes (Batman tour 5) avec unanime 8/8 + B1."
decision: accepted
proof_expected:
  - B2 gate sales update (compteur_reformulation_validee_60j_defini)
  - B2 gate ops update (compteur_procedure_sans_condition_60j_defini)
  - B2 gate legal update (compteur_perimetre_proprietaire_60j_defini)
  - B2 gate growth update (compteur_promesse_publique_60j_defini)
  - B3 proof path (council_arbitrage_0_cas_60j_recorded)
next_review: 2026-12-30  # 135j pour observer ≥ 1 procédure complète 4 étapes
```

**Saisissabilité** sous 3 conditions cumulatives :

1. **Co-signature Batman** (auteur de la procédure 6 étapes).
2. **Adoption unanime 8/8 + B1** — la procédure touche les 8
   domaines, le seuil unanime est requis.
3. **Co-signature des 8 Captains** sur leur compteur discriminant
   spécifique (1 par veto).

## Les 4 étapes canonicalisées (héritage concept 1 tour 4)

| Étape | Owner | Durée cible | Livrable |
|---|---|---|---|
| 1. Recaractérisation compteur | Captain sponsor | 1 sprint | doc compteur discriminant proposé |
| 2. Revue doctrine | Captain sponsor + 2 pairs | 1 sprint | avis doctrinal |
| 3. Arbitrage Council | Council chair | 1 sprint | décision Council |
| 4. Dissolution ou amendement | Captain sponsor | 1 sprint | packet mésoperpétuel final |

**Total** : 4 sprints, soit ~8-12 semaines (cycle 12WY français).
**Asymétrie avec Batman tour 5 procédure 6 étapes** : la procédure
6 étapes est l'**amendement RACI** (modification de la matrice 9
pair-checks), la procédure 4 étapes est l'**observation compteur**
(dissolution ou amendement d'un veto). Elles sont **complémentaires**,
pas redondantes.

## Les 3 compteurs candidats par veto (héritage concept 1 tour 4)

`b2-eight-domain-vetoes-catalogue.md` liste 8 vetos un par Captain.
Chaque veto mérite un **compteur discriminant** spécifique :

| Captain | Veto catalogue | Compteur discriminant candidat |
|---|---|---|
| Superman (Growth) | Promesse publique tenue | ≥ 1 prise de parole /60j avec claim vérifié |
| **JohnJones (Sales)** | Reformulation validée | **≥ 1 reformulation validée /60j** |
| Flash (Product) | Offre dépersonnalisée | ≥ 1 offre reproductible /60j avec revue squad |
| Batman (Ops) | Procédure sans condition d'arrêt | ≥ 1 procédure documentée condition /60j |
| Cyborg (IT) | Cloud-only sortie | ≥ 1 chemin sortie documenté /60j |
| Wonder Woman (Finance) | Dépense récurrente sans date | ≥ 1 revue F19-F22 /60j |
| Green Lantern (People) | Recrutement sans mandat | ≥ 1 mandat signé /60j |
| Aquaman (Legal) | Engagement sans périmètre | ≥ 1 périmètre-propriétaire signé /60j |

**Note 1** : les 8 compteurs sont **candidats**. Chaque Captain peut
proposer un compteur plus adapté (par exemple Batman peut préférer
*« ≥ 1 condition-arrêt-mesure-pair-check /60j »*).

**Note 2** : la généralisation 8-domain **ne fige pas** les
compteurs. La procédure 4 étapes prévoit la **recaractérisation**
(étape 1) : un Captain peut proposer un compteur différent, le
Council agrège ou statue.

## Les 4 issues par ordre de fréquence (héritage concept 1 tour 4)

| Issue | Fréquence attendue | Description |
|---|---|---|
| Compteur-tenu | 60% | compteur discriminant observé, doctrine valide |
| Fenêtre-étendue | 25% | compteur non tenu sur 60j, fenêtre étendue 90j/120j |
| Obsolescence-Council | 10% | compteur non-pertinent, dissolution par Council |
| Dissolution-structurelle | 5% | doctrine veto dissoute, amendement majeure |

**Asymétrie Batman / Aquaman** : Aquaman a un **état dormant**
canonique (triplet 35). Pour Aquaman, la procédure 0 cas/60j est
**différente** — la non-observation d'un compteur Engagement-sans-
périmètre est **canonique** (Aquaman dort par doctrine), pas un
signal d'obsolescence. **La procédure 4 étapes doit être adaptée**
au cas Aquaman : étape 1 « recaractérisation » revient à vérifier
si Aquaman est DORMANT ou ACTIVE, pas à dissoudre le veto.

## Les 3 cas d'adaptation Aquaman (extension asymétrique)

Le paquet Council-ready adresse le cas symétrique (8 Captains avec
même procédure) **et** le cas asymétrique Aquaman :

1. **Aquaman DORMANT** (cas 0) — la procédure 0 cas/60j est **non
   applicable**. Aquaman steward la dormance, pas le décompte. Le
   compteur Aquaman est remplacé par un compteur de **réveil**
   (par exemple, ≥ 1 wake-up /an).
2. **Aquaman SHADOW_ACTIVE** (cas 1) — la procédure 0 cas/60j
   s'applique avec compteur **adapté** (par exemple, ≥ 1 périmètre-
   propriétaire signé /90j, fenêtre étendue).
3. **Aquaman ACTIVE** (cas 2) — la procédure 0 cas/60j s'applique
   normalement.

**Règle générale** : pour les Captains dont l'état Canonique est
**dormant par doctrine** (Aquaman, et **uniquement** Aquaman), la
procédure 0 cas/60j est **conditionnelle** à l'état. Aquaman a déjà
posé cette asymétrie (cf. `aquaman-dormance-doctrine-canonique-alignement.md`
tour 5).

## Ce que ce packet ne fait PAS

- **Ne pose pas la liste fermée des 8 compteurs** — chaque Captain
  propose son compteur, le Council agrège.
- **Ne modifie pas les 8 vetos catalogue** — la procédure 0 cas/60j
  est une **méta-procédure** d'observation des vetos, pas un
  amendement des vetos.
- **Ne décide pas de la fenêtre 60j** — la fenêtre 60j est une
  projection, peut être ajustée à 90j ou 120j en cycle.
- **Ne touche pas à la procédure 6 étapes Batman** — la procédure
  6 étapes est l'**amendement RACI**, la procédure 4 étapes est
  l'**observation compteur**. Elles sont complémentaires.

## Anti-pièges spécifiques

- **Vouloir fixer les 8 compteurs de manière symétrique** — chaque
  Captain peut proposer un compteur plus adapté. La symétrie
  procédurale (4 étapes) n'est pas symétrie de contenu.
- **Saisir le packet sans co-signature Aquaman** — la procédure
  4 étapes a un cas d'adaptation Aquaman (DORMANT). Sans
  co-signature Aquaman, l'adaptation est unilatérale.
- **Confondre dissolution-amendement du compteur et dissolution-
  amendement du veto** — la procédure 4 étapes dissout le compteur,
  pas le veto. Le veto reste canonique jusqu'à amendement
  séparé.
- **Procédure d'amendement trop lourde** — Batman tour 5 §« Réfutation 4 »
  note qu'une procédure 3 étapes sacrifierait la ratification B1.
  La procédure 6 étapes est dogme, mais elle est **l'amendement
  RACI**, pas l'observation compteur. Les 4 étapes peuvent être
  saisissables plus rapidement.

## Liens

- [[johnjones-protocole-empirique-zero-cas-procedure-remplacement]] — procédure 4 étapes héritage
- [[batman-procedure-amendement-raci-unanime-8-8-b1-format-complet]] — procédure 6 étapes amendement RACI
- [[aquaman-dormance-doctrine-canonique-alignement]] — Aquaman DORMANT/SHADOW_ACTIVE/ACTIF
- [[b2-eight-domain-vetoes-catalogue]] — 8 vetos catalogue
- [[b2-areas-dormants-doctrine]] — 3 états
- [[b2-meso-decision-packet-spec]] — format 8 champs
- [[b2-council-arbitrage-rule]] — qui tranche quand deux Captains négocient

## Note de confiance

**Confirmé par machine, à moitié.** Le format packet 8-champs est
verbatim `b2-meso-decision-packet-spec.md`. La procédure 6 étapes
est verbatim `batman-procedure-amendement-raci-unanime-8-8-b1-format-complet.md`.
La procédure 4 étapes est héritée concept 1 tour 4 sans modification.
La liste 8 compteurs candidats est projetée depuis
`b2-eight-domain-vetoes-catalogue.md` (8 vetos un par Captain).

**L'adaptation Aquaman** (3 cas DORMANT/SHADOW_ACTIVE/ACTIVE) est
**projetée** depuis la doctrine Aquaman tour 5 + B2 Areas dormants
doctrine. **L'asymétrie symétrie procédure 4 étapes vs procédure 6
étapes** est projetée depuis la lecture croisée Batman + JohnJones,
pas citée canoniquement. **La saisissabilité conditionnelle** (3
conditions cumulatives) est projetée depuis la doctrine d'amendement
unanimité 8/8 + B1, pas testée en cycle.
