---
type: Concept
title: B1 OMK T3 Legal+R&D — mandat calibré sur domaine dormant + découverte externe
description: Mandat B1 calibré sur le Rock B1-3 OMK Business OS (T3 Legal+R&D — Aquaman Eternals + Cyborg Kang Dynasty) avec intent « conformité activée par premier contrat signé + R&D External Discovery » et success_signal conditionnel (le signal Legal n'est mesurable qu'au premier contrat ; le signal R&D est mesurable en pistes externes).
tags: [b1, b2, mandate, omk, t3, legal, r-and-d, domaine-dormant, external-discovery]
generated: { by: minimax-m3, at: 2026-08-19T03:40:00Z }
verified:
  - { by: process:synthese-pulse-b1-tour-3, at: 2026-08-19T03:40:00Z }
sources:
  - id: omk-project
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/omk-business-os.md"
    title: OMK Business OS — Triptyque V4 status ACTIVE 2026-07-15
    last_modified: 2026-08-17
  - id: omk-t3-ownerbook
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/ownerbooks/ownerbook_T3_legal_rd.md"
    title: Ownerbook T3 Legal/R&D (Rock B1-3, 2026-07-15)
    last_modified: 2026-07-15
  - id: triplets-v3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: v3-business triplets — Aquaman dormant + Cyborg external discovery
    last_modified: 2026-08-17
okf_version: "0.2"
---

# B1 OMK T3 Legal+R&D — mandat calibré sur domaine dormant + découverte externe

T3 est le Rock B1-3 d'OMK Business OS. C'est le Rock le plus
**asymétrique** du Triptyque V4 : un de ses deux capitaines (Aquaman
Legal) est en **état dormant** par défaut (triplet v3 ligne 35), l'autre
(Cyborg R&D) est en posture **external discovery** (triplet v3 ligne 22
+ omk-business-os.md). Le mandat B1 doit calibrer cette asymétrie sans
forcer Legal à produire ni R&D à s'enfermer.

## L'asymétrie T3 — deux captains, deux régimes

```yaml
captain_legal:
    name: Aquaman
    squad: Eternals
    status: dormant (triplet v3 L35-L36)
    activation_condition: |
      Premier fichier déposé dans 00_Summers_CEO/03_Master_Agreements/
      = premier contrat de coaching signé (triplet v3 L36).
    veto: engagement-sans-perimetre (triplet v3 L30)
    doctrine: |
      « Un domaine dormant qui produit est un coût sans contrepartie. »
      Aquaman steward Legal & Compliance en état dormant — il ne
      produit rien tant que le canon Master Agreements reste vide.

captain_rd:
    name: Cyborg
    squad: Kang Dynasty
    status: external_discovery (omk-business-os.md T3)
    veto: cloud-only-sans-sortie (triplet v3 L29)
    doctrine: |
      Cyborg absorbe l'IT infra à L0 Rick (W40 §M1+M2 patches) ; le
      périmètre Kang Dynasty devient R&D External Discovery plutôt
      qu'infrastructure interne.
```

Un mandat B1 qui ne respecte pas cette asymétrie produit l'un des deux
échecs symétriques :
1. **Forcer Legal à produire** sans contrat signé → Aquaman consomme
   du quota sans livrable, viole sa propre doctrine de dormant.
2. **Forcer R&D à s'enfermer** dans l'interne → Cyborg perd sa raison
   d'être (external discovery), contredit le pivot.

Le mandat T3 doit calibrer **deux signaux distincts**, pas un.

## Le mandat Rock B1-3 — T3 Legal+R&D

```yaml
b1_b2_mandate_id: B1-B2-MANDATE-2026-23
issued_at: 2026-08-19T10:00:00Z
issued_by: summer-coach-os
cycle: 12WY-2026-Q3-Q4
source_rock: B1-3 (T3 Legal+R&D, Ownerbook T3)

intent: |
  T3 opère sur deux fronts indépendants : (1) tenir Legal & Compliance
  prêt à s'activer au premier contrat signé, sans production avant ;
  (2) faire tourner la R&D External Discovery de Cyborg, qui n'a pas
  besoin d'un contrat pour produire. Sans cette asymétrie respectée,
  T3 consomme du quota sans livrer — Legal parce qu'il est dormant,
  R&D parce qu'on l'a enfermé.

contraintes:
  - Aucune production Aquaman tant que le canon Master Agreements est
    vide (doctrine domaine dormant — triplet v3 L35-L36).
  - Tout engagement client (contrat, NDA, accord-cadre) doit porter
    un périmètre écrit et une propriété du livrable identifiée (veto
    Aquaman — triplet v3 L30, doctrine veto-engagement-sans-perimetre).
  - Aucun fournisseur cloud-only sans chemin de sortie documenté (veto
    Cyborg — triplet v3 L29, doctrine veto-cloud-only-sans-sortie).
  - La R&D Cyborg reste en posture external discovery — pas de
    ré-absorption de l'infrastructure interne L0 Rick, qui est le
    périmètre L0.2 Forge (Bill) et L0.1 (cf. AGENTS.md Coach OS).

success_signal: |
  Signal composite, deux compteurs indépendants :

  Compteur A — Legal dormant actif (mesurable conditionnellement) :
  Activé au premier fichier dans 00_Summers_CEO/03_Master_Agreements/.
  Cible : 1 accord-cadre US pivot signé sous 60 jours (cf. couplage
  avec T2 — b1-omk-t2-pivot-us-mandate). Si A = 0 à fin de cycle, le
  compteur A est `non_measured` et ne compte pas dans le verdict.

  Compteur B — R&D External Discovery (mesurable inconditionnel) :
  Au moins 3 pistes R&D externes documentées (cible : 1 vendor LLM
  alternative, 1 canal de distribution US, 1 partenaire compliance)
  avec note de due-diligence (3 critères : reversibility, lock-in,
  cost-path) par piste, sous 60 jours.

  Verdict final : B atteint 70%+ de sa cible (3/3 pistes) =
  Rock tenu ; A non_measured n'invalide pas le Rock.

  Cycle de mesure : 12WY-2026-Q3-Q4 (fin 2026-10-15).
```

## Pourquoi ce mandat respecte la grammaire — et la complique

| Champ | Critère `b1-success-signal-spec.md` | Conformité |
|---|---|---|
| `intent` | Pourquoi ce mandat maintenant, dans le North Star | OK — réfère l'asymétrie Legal dormant + R&D external |
| `contraintes` | Limites non-négociables | OK — 4 contraintes, toutes sourcées (3 vetoes + 1 doctrine domaine dormant) |
| `success_signal` | Mesurable ou observable, mesurable privilégié | **Adapté** — compteur A conditionnel (non_measured est une réponse valide) + compteur B inconditionnel. La règle « mesurable > observable » est respectée, mais la doctrine « un signal = un compteur » est amendée pour T3. |

**Type de signal : mesurable composite.** C'est une **extension** de
la règle `b1-success-signal-spec.md` : un signal peut être composite
lorsque le Rock couvre deux captains aux régimes asymétriques. Le
compteur A est conditionnel à un trigger externe (premier contrat) ;
le compteur B est inconditionnel et porte seul le verdict.

Cette extension n'est pas dans le canon — c'est une **proposition**
de ce concept. Si la doctrine canon l'interdit (un signal = un
compteur), alors T3 doit être **éclaté en deux Rocks** (B1-3a Legal
+ B1-3b R&D) avec mandates séparés. C'est une décision B1 à prendre.

## Acceptance check — deux capitaines, deux régimes

| Captain | Domaine | Ce qu'il atteste |
|---|---|---|
| **Aquaman** | Legal (08) | Reformulation intent → Legal dormant prêt à s'activer ; contrainte engagement-sans-perimetre tenue ; DoD-Una : 3 critères (template accord-cadre US pivot, périmètre écrit, propriété livrable) — applicables dès le premier contrat |
| **Cyborg** | IT/R&D (05) | Reformulation intent → R&D External Discovery tenue ; contrainte cloud-only-sans-sortie tenue ; DoD-Una : 3 critères (piste documentée, due-diligence 3 axes, réversibilité) par piste |

**Note sur la cadence d'attestation.** L'attestation Aquaman est
**anticipée** : il atteste sa doctrine de dormant, pas une production
courante. Si le contrat n'est pas signé pendant le cycle, Aquaman est
en `maintain dormant` — pas un échec. C'est conforme à
`b1-mandate-acceptance-check.md` §4 (issue `accepted_with_substitut`
quand le signal est non_measured).

## Ce que ce mandat n'est PAS

- **Pas un signal de production Legal forcée.** Le mandat ne demande
  pas à Aquaman de produire un livrable Legal. Il demande à Aquaman
  d'**être prêt** à produire.
- **Pas une absorption de L0 par Cyborg.** La R&D reste external —
  l'infrastructure interne reste Forge L0.2 / Bill. La contrainte 4
  verrouille cette frontière.
- **Pas un arbitrage Nord Star.** Le T3 est déjà acquis dans le
  Triptyque V4 (Ownerbook T3). Le mandat opère, ne re-décide pas.

## Le couplage avec T1 et T2

T3 est le **client aval** de T1 (cf. `b1-omk-t1-mandate.md`) :
- Aquaman a besoin des SOP canon (Flash Product) pour rédiger des
  accord-cadre reproductibles.
- Cyborg a besoin du ProcessDesign MrFantastic (Batman Ops) pour
  documenter ses pistes R&D en format compatible.

T3 alimente T2 indirectement : sans accord-cadre Legal signé, T2 ne
peut pas closer de contrat US. Le compteur A du mandat T3 est donc
un **input critique** pour le mandat T2 — sa non-mesure ne casse pas
T3, mais elle casse la chaîne de valeur.

## Sources

- `omk-business-os.md` — Triptyque V4, status ACTIVE 2026-07-15.
- `ownerbook_T3_legal_rd.md` — Rock B1-3 et ses DoD-1 (référencée,
  non lue intégralement dans cette passe).
- `v3-business.jsonl` lignes 29-30 — les 2 vetoes (Cyborg +
  Aquaman).
- `v3-business.jsonl` lignes 35-36 — la doctrine Aquaman domaine
  dormant et sa condition d'activation (verbatim).
- `omk-business-os.md` §« trois questions — ce qu'il visait » —
  périmètre R&D External Discovery de Cyborg (verbatim).

## Liens

- [[b1-omk-t1-mandate]] — le fournisseur interne de T3
- [[b1-omk-t2-pivot-us-mandate]] — le client aval de T3
- [[b1-mandate-packet-spec]] — la grammaire du paquet
- [[b1-success-signal-spec]] — la règle de choix du signal (étendue ici)
- [[b1-mandate-acceptance-check]] — le verrou d'acceptance
- [[b1-cycle-rollover-protocol]] — la mécanique de mesure
- [[b1-doctrine-d7-stale-mandate]] — la doctrine de mandat stale

## Note de confiance

**Confirmé par machine.** L'asymétrie Legal dormant / R&D external
est verbatim des triplets v3 lignes 29-30 et 35-36 + omk-business-os.md
T3. Les deux vetoes (Aquaman engagement-sans-perimetre, Cyborg
cloud-only-sans-sortie) sont verbatim triplet v3. **Extrapole** : le
signal composite (compteur A conditionnel + compteur B inconditionnel)
est une proposition de ce concept, pas dans le canon. Le Ownerbook T3
n'a pas été lu intégralement (chemin ASpace_OS_V2, hors-périmètre
d'écriture) ; les cibles chiffrées (1 accord-cadre, 3 pistes R&D) sont
des **estimations raisonnables** extrapolées de la doctrine. La
proposition « éclater T3 en B1-3a + B1-3b si le canon refuse le signal
composite » est ouverte — décision à prendre au cycle réel.