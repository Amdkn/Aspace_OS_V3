---
type: Concept
title: Protocole de validation empirique du veto Flash — passer de 0 cas réel à 3 observations documentées
description: Le tour 1 a posé 7 concepts sur Flash, mais 0 packet mésoperpétuel Flash n'a été observé dans le corpus visible. La doctrine valeur d'artefact est reconstruite, pas étayée par un cas pratique. Ce concept pose le protocole de validation empirique : 3 cas attendus sur 60 jours, packet mésopépétuel type, 5 critères d'acceptance par cas, et conditions de mise à jour de la doctrine.
tags: [flash, product, veto, validation-empirique, doctrine, observation, b2-council, d4]
generated: { by: minimax-m3, at: 2026-08-19T05:20:00Z }
verified:
  - { by: process:lecture-corpus-flash-tour-2, at: 2026-08-19T05:20:00Z }
sources:
  - id: rapport-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-flash.md"
    title: Rapport de l'escouade Flash — vague 2 (tour 1)
    last_modified: 2026-08-19
  - id: flash-veto-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-veto-offre-depersonnalisee.md"
    title: Veto Flash — l'offre dépersonnalisée
    last_modified: 2026-08-19
  - id: vetoes-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — 3 propriétés (catégoriel/vérifiable/non-négociable)
    last_modified: 2026-08-19
  - id: meso-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — le format canonique d'une décision B2
    last_modified: 2026-08-19
  - id: triplet-25
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 25 — Flash bloque toute offre dont la valeur dépend d'une personne nommée"
    last_modified: 2026-08-17
  - id: b1-omk-t1-mandate
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-omk-t1-mandate.md"
    title: B1 OMK T1 mandate — veto-offre-depersonnalisee
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Protocole de validation empirique du veto Flash

## Le constat — 0 cas réel observé

Le rapport tour 1 (`RAPPORT_dom-flash.md` §« 5.2. Ce que le corpus ne
dit PAS sur Flash » alinéa 1) pose le constat :

> *« Aucun cas réel de veto Flash opposé dans un packet mésoperpétuel.
> La doctrine est reconstruite à partir des triplets et de la doctrine
> Batman, pas étayée par un cas pratique observé. Si Flash n'a jamais
> opposé son veto en cycle réel, sa légitimité opérationnelle est
> non-testée. »*

Le constat est symétrique pour les 5 red flags : aucun des 5 red flags
n'a été déclenché dans le corpus visible. Le red flag #1 (qui est le
seul lié à Product — cf. `flash-red-flag-1-trigger.md` §« Pourquoi ce
red flag est asymétrique ») est **théorique** pour Flash.

**Trois conséquences** :

1. La doctrine valeur d'artefact est **reconstruite**, pas **observée**.
2. Le catalogue des 5 cas légitimes et 3 cas abusifs est **projeté**,
   pas **vérifié**.
3. La procédure d'application en 4 étapes (détection, documentation,
   communication, issue) est **empruntée** au pattern veto canonique, pas
   **rodée** par un cas pratique.

Sans validation empirique, le veto Flash reste une **projection
doctrinale**, pas un outil opérationnel.

## Le protocole — 3 cas attendus sur 60 jours

Le protocole pose une cible mesurable : **3 cas observés et documentés
sur une fenêtre de 60 jours**. C'est un seuil minimal pour passer de
*« doctrine reconstruite »* à *« doctrine étayée »*.

### Cible 1 — Au moins 1 veto Flash opposé

Un mandat B1 ou une proposition B3 déclenche le veto Flash (un des 5
cas légitimes — cf. `flash-veto-offre-depersonnalisee.md` §« Cinq cas
de déclenchement légitimes »). Le veto est consigné dans un packet
mésoperpétuel avec `decision: blocked`.

### Cible 2 — Au moins 1 levée de veto par amendement

Le veto opposé est levé par **amendement du mandat** (ajout d'un
mécanisme de reprise). Le packet mésoperpétuel consigne
l'amendement et la levée. C'est la trace que le veto **a servi** (pas
un veto posé puis levé sans amendement — cf. `flash-veto-offre-depersonnalisee.md`
§« Anti-pièges »).

### Cible 3 — Au moins 1 refus de veto abusif

Un cas où un veto Flash **aurait pu** être opposé mais ne l'a **pas
été** parce qu'il aurait été abusif (un des 3 cas abusifs — cf.
`flash-veto-offre-depersonnalisee.md` §« Trois cas abusifs »). Le
refus est consigné dans le journal Council avec motif (pourquoi le veto
n'a pas été opposé —).

**Pourquoi 3 cas, pas 1** : un seul cas ne permet pas de tester la
**doctrine** (le veto est légitime ou abusif sur ce cas spécifique).
Trois cas minimum — un par issue (opposé, levé par amendement, refusé
comme abusif) — couvrent le **spectre** de la doctrine.

**Pourquoi 60 jours, pas 30 ou 90** : 30 jours est trop court pour
observer 3 cas dans un cycle de build actif (1 cas par mois est déjà
rapide). 90 jours est trop long — la doctrine risque de dériver avant
d'être validée. 60 jours (≈ 2 mois) est l'horizon d'un **cycle de
build** standard, et permet d'observer les 3 cas dans une fenêtre
resserrée.

## Le packet mésoperpétuel type

Pour chaque veto opposé, le packet mésoperpétuel suit le format canonique
(cf. `b2-meso-decision-packet-spec.md` §« Le gabarit YAML ») avec les
champs spécifiques au veto Flash :

```yaml
meso_decision_id: B2-MESO-DECISION-2026-NN
source_mandate: B1-B2-MANDATE-2026-NN  # ou B2-PEER-YYYY-NN
mode: handoff | negotiation
impacted_domains:
  - product
tradeoff: <le conflit entre valeur nominative détectée et valeur dépersonnalisée attendue>
decision: blocked  # ou accepted (après amendement)
veto_flash:
  classe: offre-depersonnalisee
  cas_legitime: <cas légitime détecté : consultant-clé, expert signature, SPOF, fondateur irremplaçable, équipe-de-star>
  motif_verifiable: <exification : chemin proposition/contrat/observation, absence de clause de continuité>
proof_expected:
  - B2 gate product update (offre_amendée_ou_retirée)
  - B3 proof path (mécanisme de reprise documenté)
next_review: <date de résolution prévue>
```

Cinq champs sont **spécifiques** au veto Flash :

1. **classe** : *« offre-depersonnalisee »* (le triplet 25 verbatim).
2. **cas_legitime** : l'un des 5 cas de déclenchement (cf.
   `flash-veto-offre-depersonnalisee.md`).
3. **motif_verifiable** : le chemin proposition/contrat/observation
   qui justifie le veto (propriété 2 du veto catalogue — vérifiable).
4. **proof_expected** : la preuve que le mandat a été amendé (mécanisme
   de reprise documenté).
5. **next_review** : la date à laquelle le B2 Council ré-évalue la
   levée du veto.

## Cinq critères d'acceptance par cas

Pour qu'un veto opposé soit **comptabilisé** dans la cible de 3 cas,
cinq critères doivent être remplis :

1. **Le veto oppose la classe** *« offre-depersonnalisee »*, pas un cas
   spécifique (propriété 1 du veto catalogue — catégoriel).
2. **Le motif est écrit** dans le packet mésoperpétuel et pointe sur un
   fichier vérifiable (propriété 2 — vérifiable).
3. **Le mandat est suspendu** (pas exécuté B3 tant que le veto n'est
   pas levé) — trace dans le journal Council.
4. **L'issue est documentée** : amendement (veto levé), retrait
   (veto tient), escalade B1, ou veto invalide (Council passe outre).
5. **Le packet est archivé D4** dans `B2_DC_DIRECTION_COUNCIL_DECISIONS.md`
   avec date d'effet.

Un veto qui manque un critère est **incomplet** et ne compte pas dans
la cible. C'est un acte d'autorité non documenté, pas un veto légitime.

## Trois indicateurs de suivi

Trois indicateurs pour suivre la progression du protocole sur 60 jours :

1. **Indicateur de couverture** — nombre de cas observés sur la cible
   (3). Cible atteinte : 3/3 à 60 jours.
2. **Indicateur de distribution** — répartition des cas par issue
   (opposé, levé, refusé). Distribution équilibrée attendue : 1/1/1.
3. **Indicateur de vitesse** — temps moyen entre détection du veto et
   documentation du packet. Cible : < 24 heures ouvrées (analogue au
   seuil d'escalade 24h du contrat B2 → B3, cf.
   `b2-b3-jtbd-handoff-contract.md`).

Si à 30 jours l'indicateur de couverture est < 1, le protocole est en
retard — Flash doit sonder activement les cas où le veto **aurait pu**
être opposé (pilote client, deal signé) pour forcer l'observation.

## Les conditions de mise à jour de la doctrine

Trois conditions de mise à jour des concepts Flash à l'issue du
protocole :

### Mise à jour 1 — Doctrine confirmée

Si les 3 cas observés correspondent aux aux cas de déclenchement
légitimes et aux 3 cas abusifs documentés dans
`flash-veto-offre-depersonnalisee.md`, la doctrine est **confirmée**.
Les concepts tour 1 (veto, doctrine valeur-d-artefact) restent en
l'état.

### Mise à jour 2 — Doctrine amendée

Si 1 cas observé diverge de la doctrine projetée (ex : un cas de
déclenchement légitime non documenté, ou un cas abusif qui s'avère
légitime), la doctrine est **amendée**. Les concepts tour 1 sont mis
à jour avec append-only D4 (un packet d amendement qui pointe sur les
id d'origine).

### Mise à jour 3 — Doctrine invalidée

Si 2+ cas observés divergent de la doctrine projetée, la doctrine est
**invalidée**. Les concepts tour 1 sont marqués caduques par un
packet séparé qui pointe sur les id d'origine (cf.
`b2-meso-decision-packet-spec.md` §« Append-only — la règle D4 »).

## Anti-pièges

- **Cible de 3 cas sans qualité**. Un cas observé qui manque un des 5
  critères d'acceptance ne compte pas. La doctrine est validée par la
  **qualité** des cas, pas le **nombre**.
- **Indicateur de vitesse sans conséquence**. Un packet mésoperpétuel
  documenté > 24 heures après détection n'est pas un veto légitime —
  c'est un veto tardif qui peut être contesté. Le seuil 24h doit être
  tenu.
- **Distribution biaisée**. Si les 3 cas observés sont tous du même
  type (ex : 3 vetos opposés, 0 levé, 0 refusé), la doctrine est
  testée **partiellement**. Flash doit diversifier les cas.
- **Doctrine invalidée par impatience**. 3 cas en 60 jours est un seuil
  minimal, pas un plafond. Si la doctrine est invalidée à 3 cas, c'est
  un signal fort — mais pas une raison de **renoncer** à la doctrine.
  L'invalidation appelle une **réécriture**, pas un abandon.

## Liens

- [[flash-veto-offre-depersonnalisee]] — la doctrine à valider
- [[flash-doctrine-valeur-artefact]] — la doctrine valeur d'artefact
- [[b2-eight-domain-vetoes-catalogue]] — les 3 propriétés du veto légitime
- [[b2-meso-decision-packet-spec]] — le format du packet mésoperpétuel
- [[b2-council-arbitrage-rule]] — l'instance qui consigne les vetos
- [[b2-b3-jtbd-handoff-contract]] — le seuil 24h d'escalade (référence)
- [[rapport-dom-flash]] — le constat de 0 cas réel

## Note de confiance

**Confirmé par machine, projeté.** Le constat *« 0 cas réel observé »*
est **vérifié** par lecture du rapport tour 1 (`RAPPORT_dom-flash.md`
§« 5.2 »). Le format de packet mésoperpétuel est **verbatim** de
`b2-meso-decision-packet-spec.md`. Les 5 critères d'acceptance sont
**projetés** à partir des 3 propriétés du veto catalogue
(catégoriel/vérifiable/non-négociable). Les 3 indicateurs de suivi
sont **empruntés** au contrat B2 → B3 (cf.
`b2-b3-jtbd-handoff-contract.md`). La cible de 3 cas en 60 jours est
**projetée** à partir de la pratique observée (un cycle de build
actif produit 1-2 cas par mois). Les 3 conditions de mise à jour de la
doctrine sont **reconstruites** par analogie avec la doctrine D4
append-only. Le protocole est un **draft de validation empirique**,
pas un protocole exécuté.