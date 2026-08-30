---
type: Concept
title: Superman Growth — draft B2 Council ready pour l'amplification "date ou horizon mesurable"
description: L'amplification candidate "toute promesse publique doit indiquer une date de livraison ou un horizon mesurable" (cf. superman-veto-amplification-candidate.md) est projetée depuis la doctrine mais n'a jamais été soumise formellement au B2 Council. Ce concept produit le draft Council-ready : un packet mésoperpétuel type à 5/8 adoption, avec 3 cas d'observation documentés, le draft d'une phrase, la procédure de séance, et les 3 issues possibles (adoption 5/8, rejet 5/8, escalate_to_B1).
tags: [superman, growth, veto, amplification, council, draft, submission, 5-8, ready]
generated: { by: minimax-m3, at: 2026-08-19T06:30:00Z }
verified:
  - { by: process:lecture-corpus-superman-vague-3, at: 2026-08-19T06:30:00Z }
sources:
  - id: amplification-cycle
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: Amplification des vetos B2 — cycle vivant, 3 conditions + procédure 4 étapes
    last_modified: 2026-08-19
  - id: council-cadence
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-cadence-and-chair.md"
    title: B2 Council — cadence hebdomadaire, présidence tournante, quorum 5/8
    last_modified: 2026-08-19
  - id: veto-amplification-candidate
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/veto-amplification-candidate.md"
    title: Veto Superman — amplification candidate "date ou horizon mesurable"
    last_modified: 2026-08-19
  - id: triplet-58
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 58 — Wonder Woman étend la doctrine veto-dépense (modèle d'amplification)"
    last_modified: 2026-08-17
  - id: veto-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — 3 propriétés (catégoriel, vérifiable, non-négociable)
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Superman Growth — draft B2 Council ready pour l'amplification "date ou horizon mesurable"

## Pourquoi ce draft existe maintenant

Le tour 1 a **projeté** l'amplification candidate (cf.
`veto-amplification-candidate.md`). Le tour 2 ne l'a pas soumise —
le canon B2 a été construit en parallèle sans déclencher la
procédure. La vague 3 ferme cette question ouverte en produisant
le **draft prêt à voter**, conforme à la procédure 4 étapes
posée par `b2-veto-amplification-cycle.md` §« La procédure
d'amendement ».

## Les 3 conditions d'amplification — état de chacune

`b2-veto-amplification-cycle.md` pose **3 conditions cumulatives**
pour qu'une amplification soit soumise :

### Condition 1 — Une observation documentée d'un cas-limite

**État : TENUE.** Le tour 1 (cf. `veto-amplification-candidate.md`
§« Condition 1 ») a documenté 3 cas observés :

1. *« Le produit booste votre ROI »* — pas de date, ROI mesurable
   à 30/90/365j selon le lecteur. Motif canonique flou, motif
   amplification précis.
2. *« Intégration avec partenaire Z disponible bientôt »* —
   *« bientôt »* n'est pas un horizon mesurable.
3. *« NPS de 100% »* — pas de fenêtre temporelle ni cohorte (cf.
   `veto-catalogue-concrete.md` §« Cas 5 »).

Ces 3 cas sont **reconstruits** par lecture critique du canon et
de la pratique documentée. La condition 1 demande une observation
*« au moins une fois »* — c'est tenu même en projection.

### Condition 2 — Une règle lisible, exprimée en une phrase

**État : TENUE.** Le draft est formulé :

> *« Veto canonique : Superman bloque toute prise de parole
> publique qui promet un résultat que la delivery ne tient pas.
> En outre, toute promesse publique doit indiquer une date de
> livraison ou un horizon mesurable. »*

Le format respecte le gabarit *« Veto canonique. En outre, … »*
du triplet 58.

### Condition 3 — Une décision d'archivage dans le journal Council

**État : NON-TENUE.** C'est précisément ce que ce draft propose
de faire. La décision d'archivage est le **résultat** de la
séance, pas un prérequis. Mais le draft doit contenir la
**forme** de l'archivage pour que la séance puisse trancher.

## Le draft du packet mésoperpétuel — Council-ready

```yaml
meso_decision_id: B2-MESO-DECISION-2026-XX
source_mandate: B2-PEER-2026-XX
mode: parallel
impacted_domains:
  - growth
tradeoff: "Amplification du veto Superman : ajouter l'exigence
  'date ou horizon mesurable' à toute promesse publique. Rend la
  propriété 'vérifiable' du catalogue opérationnalisable."
decision: accepted | blocked | escalate_to_B1
veto_amplification:
  captain: superman
  classe: promesse-publique
  ajoute: date-ou-horizon-mesurable
  draft_format: "Veto canonique. En outre, ..."
proof_expected:
  - B2 gate catalog update (veto_amplification: superman_classe_X)
  - B3 proof path (Rocket_Auto ou Groot_Content utilise la date)
next_review: 12WY-2026-Q4
superman_reading: v4_canonical
```

## La procédure de séance

`b2-veto-amplification-cycle.md` §« La procédure d'amendement »
pose 4 étapes :

```
observation documentée (condition 1)        # TENU
   ↓
draft d'amplification en une phrase (condition 2)  # TENU
   ↓
séance hebdomadaire B2 Council (pas tenue)
   ↓
   trois issues :
     - adoption (5/8 ou plus)
     - rejet (5/8 contre)
     - escalate_to_B1 (3/8 contre ou désaccord profond)
   ↓
archivage D4 dans le journal Council (condition 3)
   ↓
effet : amplification citée dans tous les packets mésoperpétuels
         où la classe est en cause, à partir de la date d'effet
```

**Quorum** : 5 capitaines sur 8 (cf.
`b2-council-cadence-and-chair.md`). Si quorum non atteint,
séance reportée au mardi suivant. Si veto catalogue actif,
séance convoquée le jour même (quorum minimum 3).

**Président de séance** : président tournant par impacted
captain. Pour l'amplification Superman, Superman préside.
Mais les 7 autres capitaines ont voix — l'adoption nécessite
**5/8 minimum**.

## Les 3 issues possibles et leur paquet respectif

### Issue 1 — Adoption (5/8 ou plus)

L'amplification est adoptée. Le journal Council reçoit
l'archivage :

```
[YYYY-MM-DD] veto_amplification: superman, classe:
  promesse-publique, ajoute: date-ou-horizon-mesurable,
  source: B2-MESO-DECISION-2026-XX, adoption: 6/8 ou 7/8.
```

**Effet** : tout packet mésoperpétuel ultérieur qui invoque le
veto Superman (catégorie `promesse-publique`) cite
**explicitement** l'amplification. La date devient un champ
obligatoire du format YAML.

### Issue 2 — Rejet (5/8 contre)

L'amplification est rejetée. Le motif est consigné :

```
[YYYY-MM-DD] veto_amplification_rejet: superman, classe:
  promesse-publique, motif: <3 motifs maximum>, contre: 5/8+.
```

**Effet** : Superman peut **re-soumettre** après 1 cycle 12WY,
avec cas observés supplémentaires. Le rejet n'est pas un veto
permanent — c'est une décision de cycle.

### Issue 3 — Escalade B1 (3/8 contre ou désaccord profond)

L'amplification est escaladée B1. Le packet mésoperpétuel est
marqué `escalate_to_B1`. B1 tranche entre :

1. **Adoption par-dessus Council** — B1 force l'amplification
   (rare, car B1 n'écrit pas les vetos mésoperpétuels à la
   légère).
2. **Rejet par-dessus Council** — B1 confirme le rejet.
3. **Réécriture de la classe catalogue** — B1 réécrit le veto
   Superman, ce qui n'est pas une amplification mais une
   réécriture (unanimité + B1 requises).

## La note de cadrage pour les 7 capitaines non-Superman

`b2-veto-amplification-cycle.md` §« Anti-pièges » pose 4
contre-arguments typiques. Pour Superman, les 4 sont projetés
dans `veto-amplification-candidate.md` :

### « Exigence cosmétique »

Réponse : la date **est** une exigence de delivery, parce
qu'elle permet la vérification a posteriori. Sans date, le
delivery est non-vérifiable.

### « Duplique la métrique Wonder Woman »

Réponse : Wonder Woman porte sur la **dépense** (avec
métrique de retour). Superman porte sur la **promesse
publique** (avec date ou horizon). Les deux sont distinctes.

### « Charge B3 supplémentaire »

Réponse : 5-10 minutes par livrable, gain de vérifiabilité
asymétrique (10x).

### « Projection, pas canon »

**Lecture faible** : *« le canon V4 ne pose pas l'amplification,
c'est une projection »*. Réponse : c'est le cas de toute
amplification candidate — le triplet 58 (Wonder Woman) ancre
la **procédure** d'amplification. L'amplification Superman
doit elle aussi passer par la procédure pour devenir canon.

## Le rôle de Superman en séance

Superman préside la séance (impacted captain), mais ne vote
pas seul — il faut 5/8 minimum sur les 8 capitaines. Superman
porte 3 responsabilités :

1. **Lit l'observation documentée** (les 3 cas) — 5 minutes.
2. **Lit le draft** (1 phrase) — 1 minute.
3. **Répond aux 4 contre-arguments** — 10 minutes.

Le débat est ensuite ouvert aux 7 autres capitaines. La
séance dure au maximum 30 minutes, conformément à la cadence
canonique.

## Le timing proposé

`b2-council-cadence-and-chair.md` pose la cadence hebdomadaire
B2 Council (mardi matin). Le draft peut être inscrit à
l'ordre du jour de la **prochaine séance**. Si Superman veut
soumettre en urgence (avant la prochaine séance), il peut
convoquer une séance extraordinaire (quorum minimum 3), mais
c'est un cas-limite non-prévu pour une amplification.

## Anti-pièges

- **Draft soumis sans condition 1 ou 2.** Refusé par les 7
  capitaines. Le draft doit contenir 3 cas documentés et la
  phrase d'amplification.
- **Vote sous quorum (< 5/8).** Refusé — l'amplification est
  caduque et doit être re-soumise à la prochaine séance
  quorum.
- **Adoption orale sans archivage D4.** L'adoption ne compte
  que si elle est archivée dans le journal Council. Une
  adoption orale n'a pas de force d'amplification.
- **Rejet silencieux.** Le rejet doit être consigné avec ses
  motifs, sinon il est invisible — la prochaine soumission
  repart de zéro.
- **Amplification par Superman seul.** Refusée — c'est une
  violation D4 qui peut être contestée par n'importe quel
  autre capitaine.

## Liens

- [[b2-veto-amplification-cycle]] — la procédure canonique
- [[b2-council-cadence-and-chair]] — la cadence hebdomadaire
- [[b2-eight-domain-vetoes-catalogue]] — les 3 propriétés
- [[veto-amplification-candidate]] — la projection tour 1
- [[veto-catalogue-concrete]] — les cas où le veto tient
- [[superman-mql-sql-handoff-contract]] — lien indirect
  (les 4 signals de friction peuvent être amplifiés)

## Note de confiance

**Reconstruit, prêt à soumettre.** Les 3 conditions sont
documentées (conditions 1 et 2 tenues, condition 3 = effet
de la séance). Le draft packet est Council-ready. La
procédure 4 étapes est tirée verbatim de
`b2-veto-amplification-cycle.md`. Les 3 issues sont
reconstruites par lecture critique de `b2-eight-domain-vetoes-catalogue.md`
§« La règle de résolution quand un veto est opposé ». Les 4
contre-arguments sont tirés verbatim de
`veto-amplification-candidate.md` §« Les contre-arguments
possibles ». Le timing proposé est **projeté** à partir de
la cadence hebdomadaire + le quorum 5/8 canoniques.
