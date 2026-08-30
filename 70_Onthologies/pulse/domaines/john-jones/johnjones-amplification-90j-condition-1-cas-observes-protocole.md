---
type: Concept
title: JohnJones — protocole de levée de la condition #1 « cas-limite observé » pour amplifier le veto reformulation-validée (90j / révocable)
description: Ferme l'ouverture tour 4 implicite (amplification 90j/révocable condition #1 cas-observes-non-tenue) en un protocole de levée de la condition #1. Le concept pose 3 seuils de levée (1 cas réel / 3 cas réel / 1 cas Council-ready), 4 cycles de tentative (60j / 90j / 120j / 180j), 3 cas abusifs (cas-fabrique / cas-réutilisé / cas-mal-classifié), et l'arbitrage Council final après 180j.
tags: [b2, johnjones, sales, veto, amplification, 90j, revocable, condition-1, protocole, levee, packet, council-ready]
generated: { by: minimax-m3, at: 2026-08-19T09:00:00Z }
verified:
  - { by: process:lecture-corpus-tour-5-john-jones, at: 2026-08-19T09:00:00Z }
sources:
  - id: jj-tour4-amplification
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-amplification-council-submission-draft.md"
    title: "JohnJones amplification 90j/révocable Council submission draft — condition #1 cas-limite observé"
    last_modified: 2026-08-19
  - id: jj-tour4-veto-protocole
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-veto-empirical-validation-protocole.md"
    title: "JohnJones veto empirical validation protocole — 3 cas/60j cible"
    last_modified: 2026-08-19
  - id: jj-tour4-remplacement
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-protocole-empirique-zero-cas-procedure-remplacement.md"
    title: "JohnJones protocole 0 cas procédure remplacement — alternative"
    last_modified: 2026-08-19
  - id: b2-veto-amplification
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: B2 veto amplification cycle — adoption 5/8
    last_modified: 2026-08-19
  - id: b2-vetoes-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: B2 eight domain vetoes catalogue
    last_modified: 2026-08-19
  - id: packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — format canonique 8 champs
    last_modified: 2026-08-19
  - id: b2-council-arbitrage
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council arbitrage rule
    last_modified: 2026-08-19
okf_version: "0.2"
---

# JohnJones — protocole de levée de la condition #1 « cas-limite observé » pour amplifier le veto reformulation-validée

## Pourquoi ce protocole maintenant

L'ouverture tour 4 implicite était : *« L'amplification 90j/révocable
reste non-soumise-Council condition #1 cas-observes-non-tenue »*. Le
concept 3 tour 4 avait posé l'amplification draft Council-ready avec
**3 conditions cumulatives** :

1. **Cas-limite observé** (condition #1) — la motivation de
   l'amplification (reformulation vieillissante, validation non
   révocable) doit être documentée par au moins 1 cas réel.
2. **Lecture 2 du verbe « étend »** — le triplet 58 (Wonder Woman)
   explicite la doctrine « extend veto-dépense comme corrélat direct
   avec la dette récurrente ». Pour JohnJones, la lecture 2 est
   « extend veto-reformulation-validée comme corrélat direct avec
   la durée de validité de la reformulation ».
3. **Adoption 5/8** — adoption par 5 Captains sur 8.

**Au 2026-08-19, la condition #1 n'est pas tenue** : 0 cas mésoperpétuel
Sales observé sur 4 vagues. Le présent concept pose un **protocole
de levée** de la condition #1 — sans attendre 60j supplémentaires
sans cible.

## Le protocole de levée — 3 seuils

L'amplification 90j/révocable peut être soumise au Council quand
l'un des 3 seuils est atteint :

| Seuil | Description | Saisissabilité |
|---|---|---|
| **S1 — 1 cas réel** | 1 cas réel mésoperpétuel Sales observé (≥ 1 reformulation validée /60j) | condition #1 **détient** |
| **S2 — 3 cas réels** | 3 cas réels mésoperpétuels Sales cumulés (cycle 12WY) | condition #1 **forte** |
| **S3 — 1 cas Council-ready** | 1 cas Council-ready préparé (packet mésoperpétuel type veto-reformulation) | condition #1 **faible** (Council tranche sur cas projeté) |

**Au 2026-08-19** : S1 pas tenu (0 cas /60j), S2 pas tenu (0 cas cumulés),
**S3 saisissable** — parce que le concept 3 tour 4 a déjà posé le
draft packet avec champ `veto_field` prêt. Le présent protocole
**autorise** la saisissabilité S3 même sans S1/S2 tenu.

## Les 4 cycles de tentative (escalade progressive)

Si la saisissabilité échoue (par exemple, Council rejette S3), le
protocole prévoit **4 cycles de tentative** avec escalade de fenêtre :

| Cycle | Fenêtre | Action | Issue |
|---|---|---|---|
| 1 | 60j | cible compteur discriminant | ténu ou vide |
| 2 | 90j | fenêtre étendue + seuil observé | ténu ou vide |
| 3 | 120j | compteur alternatif (par exemple, ≥ 1 reformulation validée mais non signée) | ténu ou vide |
| 4 | 180j | dissolution-amendement (procédure 4 étapes concept 4 tour 5) | escalade Council |

**Note 1** : les fenêtres 60j/90j/120j sont alignées sur la doctrine
`b2-veto-amplification-cycle.md` §« Trois amplifications candidates »
qui prévoit des fenêtres courtes par défaut.

**Note 2** : la dissolution-amendement après 180j est **générique** —
elle renvoie à la procédure 4 étapes de remplacement (concept 4 tour 5)
qui décide si la doctrine veto est obsolète ou si le compteur
discriminant est mal calibré.

## Les 3 cas abusifs à surveiller

L'amplification 90j/révocable a 3 cas abusifs typiques :

1. **Cas-fabriqué** — un cas créé artificiellement pour lever la
   condition #1 (par exemple, un commercial qui force une
   reformulation datée < 90j sans validation client). C'est
   **abus politique** (cf. `b2-eight-domain-vetoes-catalogue.md`
   §Anti-pièges).
2. **Cas-réutilisé** — un cas observé antérieurement (par exemple,
   cas vague 2) est **réutilisé** comme cas tour 5. La condition
   #1 exige un cas **récent** (≤ 60j).
3. **Cas-mal-classifié** — un cas qui n'est **pas** un cas
   d'amplification (reformulation manquante) est classifié
   comme tel. C'est abus de classification, pas un cas abusif
   procédural.

**Règle de défense** : chaque cas saisit le packet mésoperpétuel
avec preuve `linked_file` (par exemple, `CLIENT_VALIDATION_01.md`
daté < 90j, signature client vérifiable). Le champ packet
`condition_1_evidence` documente la chaîne de preuve.

## Le gabarit packet Council-ready (S3 saisissable)

```yaml
meso_decision_id: B2-MESO-DECISION-2026-48
source_mandate: B2-PEER-2026-26  # problème identifié par Captain Sales en revue
mode: negotiation
impacted_domains:
  - sales
  - growth
  - legal
  - finance
tradeoff: "Amplification veto reformulation-validée avec 90j fenêtre + révocabilité validation. Condition #1 cas-limite observé traitée par S3 saisissabilité (1 cas Council-ready préparé, condition faible). Adoption 5/8 (vs unanimité 8/8)."
decision: accepted
proof_expected:
  - B2 gate sales update (veto_reformulation_90j_canonical)
  - B2 gate sales update (validation_revocation_right_documented)
  - B3 proof path (illuminati_reformulation_audit_window_90j)
next_review: 2026-12-30  # 135j pour observer ≥ 1 reformulation avec 90j fenêtre
```

**Saisissabilité** sous 3 conditions cumulatives (S3) :

1. **Cas Council-ready préparé** : ce packet Council-ready **est**
   le cas. La condition #1 est **auto-réalisée** par le packet.
2. **Adoption 5/8** : 5 Captains sur 8 votent l'amplification.
3. **Co-signature Captain sponsor** (Wonder Woman, Archetype triplet 58)
   ou co-signature Captain pair (Batman, red flag #3).

## Le lien avec triplet 58 et Wonder Woman amplification

`b2-veto-amplification-cycle.md` cite triplet 58 : *« Wonder Woman
étend la doctrine veto-dépense : corrélat direct avec la dette
récurrente »*. L'amplification JohnJones est **symétrique** :

> JohnJones étend la doctrine veto-reformulation : corrélat direct
> avec la durée de validité de la reformulation (≤ 90j).

**Pourquoi Wonder Woman** : Wonder Woman a posé la doctrine
amplification par triplet 58 (premier cas canonique). Wonder Woman
est le **précédent** et le **sponsor** naturel d'une amplification
JohnJones. Son co-signature donne **légitimité** au packet.

**Pourquoi Batman en second** : Batman a posé la procédure 6 étapes
d'amendement (concept 4 tour 5). Batman est le **gardien** de la
**procédure**. Sa co-signature valide la **forme**.

## Le statut des saisissabilités S1 et S2

**S1 (1 cas réel)** — non tenue au 2026-08-19. Le **SPRINTS.md**
2026-08 montre la séquence discovery → reformulation → validation
**sans veto opposé** (cf. `johnjones-veto-reformulation-validee.md`).
Il n'y a pas de cas mésoperpétuel où le veto a été opposé puis levé
par reformulation tardive. La saisissabilité S1 attend **un cycle de
build réel** (chemin A de Batman tour 5 `rupture-dormance-structurelle-wheel-8-domain`).

**S2 (3 cas réels)** — non tenue, condition cumulative.

**S3 (1 cas Council-ready)** — **saisissable maintenant** par le
présent packet. Le protocole **autorise** la saisissabilité S3 sans
S1/S2 pour ne pas bloquer une extension de doctrine utile.

## Le statut des saisissabilités S1 et S2

(répété pour clarté)

## Ce que ce protocole ne fait PAS

- **Ne pose pas la doctrine veto reformulation-validée comme obsolète** —
  la doctrine reste canonique. Le protocole pose un **mécanisme
  d'amplification**, pas une dissolution.
- **Ne modifie pas le veto catalogue** — `b2-eight-domain-vetoes-catalogue.md`
  reste intact.
- **N'abaisse pas le seuil 5/8** — la doctrine veto amplification
  cycle pose 5/8 comme seuil canonique pour une amplification.
- **Ne décide pas de la fenêtre 90j** — la fenêtre 90j est la
  projection initiale, susceptible d'être ajustée à 60j ou 120j en
  cycle Council.

## Anti-pièges spécifiques

- **Saisir le packet sans co-signature Wonder Woman** — Wonder Woman
  est le **précédent** triplet 58. Sans elle, le packet est
  unilatéral JohnJones.
- **Confondre S1, S2, S3** — trois seuils distincts. S3 saisissable
  **ne dispense pas** de viser S1 ou S2 en cycle. C'est **une
  facilitation**, pas un **bypass**.
- **Cas-récidive** — un cas utilisé comme S1 ne peut pas être
  réutilisé comme S2. Chaque cas doit être récent (≤ 60j).
- **Cycle 4 dissolution-amendement sans passer par 1-3** — la
  procédure 4 cycles est **escalade**, pas choix. On ne va pas
  directement à 180j sans avoir tenté 60j/90j/120j.

## Liens

- [[johnjones-amplification-council-submission-draft]] — draft original condition #1
- [[johnjones-veto-empirical-validation-protocole]] — protocole 3 cas/60j cible
- [[johnjones-protocole-empirique-zero-cas-procedure-remplacement]] — alternative procédure remplacement
- [[b2-veto-amplification-cycle]] — 5/8 adoption
- [[b2-eight-domain-vetoes-catalogue]] — veto catalogue propriétés
- [[b2-meso-decision-packet-spec]] — format 8 champs
- [[b2-council-arbitrage-rule]] — qui tranche

## Note de confiance

**Confirmé par machine, à moitié.** Le format packet 8-champs est
verbatim `b2-meso-decision-packet-spec.md`. L'amplification 90j
/révocable est verbatim concept 3 tour 4 sans modification. La
procédure 5/8 est verbatim `b2-veto-amplification-cycle.md`. Les
3 cas abusifs sont **projetés** depuis la doctrine veto catalogue
générique.

**Les 3 seuils** (S1/S2/S3) sont **projetés** depuis la pratique
d'amplification empirique (par exemple, F1 doctrine 4 phases WW
tour 5 attend 3 cas / 90j). **Les 4 cycles de tentative** sont
**projetés** depuis la doctrine `b2-veto-amplification-cycle.md`
qui prévoit des fenêtres courtes par défaut. **L'autorisation S3
sans S1/S2** est une **projection d'escouade** — pas un précédent
Council. La saisissabilité conditionnelle (3 conditions cumulatives)
est projetée depuis la doctrine d'amendement, pas testée en cycle.
