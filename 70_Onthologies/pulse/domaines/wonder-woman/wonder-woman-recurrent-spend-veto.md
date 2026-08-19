---
type: Concept
title: Veto Finance — la dépense récurrente sans date de revue et sans métrique de retour
description: Le veto catalogue de Wonder Woman bloque toute dépense récurrente qui n'a pas (a) une date de revue explicite et (b) une métrique de retour chiffrée. C'est un veto catégoriel (porte sur une classe de dépenses, pas une dépense), vérifiable (les deux critères sont dans le packet ou le journal Council), non-négociable au niveau mésoperpétuel (Batman, Superman ou JohnJones ne peuvent pas l'écarter sans escalader B1).
tags: [b2, finance, veto, recurrent-spend, revue-metrique, wonder-woman, categoriel, verifiable, non-negociable]
generated: { by: minimax-m3, at: 2026-08-19T03:42:00Z }
verified:
  - { by: process:lecture-domaine-finance-corpus, at: 2026-08-19T03:42:00Z }
sources:
  - id: vetos-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: "Catalogue des 8 vetos B2 — un domaine, un blocage légitime"
    last_modified: 2026-08-19
  - id: finance-principles
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/03_WONDERWOMAN_FINANCE_PRINCIPLES.md"
    title: Wonder Woman Finance Principles (v4) — Jerry Area Perpetual Doctrine
    last_modified: 2026-06-25
  - id: omk-control-room
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: OMK Finance — B2 Domain Control Room
    last_modified: 2026-05-25
  - id: rocket-pipeline
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md"
    title: Rock → DoD → JTBD Pipeline
    last_modified: 2026-05-27
  - id: b2-council-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Veto Finance — la dépense récurrente sans date de revue et sans métrique de retour

## Citation verbatim

Le veto catalogue de Wonder Woman est posé verbatim dans
`b2-eight-domain-vetoes-catalogue.md` §« Les 8 vetos — un par
capitaine » et dans `triplets/v3-business.jsonl` ligne 28 :

> « **Wonder Woman** (Finance, 06) : Bloque toute **dépense
> récurrente** sans **date de revue** et sans **métrique de retour**. »

Le veto tient en **deux conditions cumulatives** :

1. **Date de revue** — une date calendaire ou un cycle (ex. :
   « revue 2026-Q3 », « tous les 90 jours »).
2. **Métrique de retour** — une métrique chiffrée (ex. : « ROI ≥ 1.5x
   à 90 jours », « payback ≤ 6 mois », « réduction de coût ≥ $X/mois »).

L'absence d'**une seule** des deux suffit à déclencher le veto. La
présence formelle des deux ne suffit pas si elles sont vagues — la
métrique doit être **chiffrée** (cf. règles B2 sur les DoD).

## Les trois propriétés du veto légitime

Tout veto catalogue respecte les trois propriétés posées dans
`b2-eight-domain-vetoes-catalogue.md` §« Les trois propriétés » :

### 1. Catégoriel

Le veto porte sur une **classe** de dépenses (récurrentes), pas sur
une dépense individuelle. Conséquence : Wonder Woman ne peut pas
utiliser son veto pour bloquer un SaaS qu'elle n'aime pas — elle
peut seulement invoquer la règle générale « toute dépense
récurrente sans date de revue ni métrique ».

Conséquence opérationnelle : si Superman achète un SaaS X avec
date de revue et métrique chiffrée, **Wonder Woman ne peut pas le
bloquer au catalogue**, même si elle pense que X est mauvais. Elle
peut signaler dans le packet mésoperpétuel que la métrique est
trop optimiste, mais c'est un avis C, pas un veto.

### 2. Vérifiable

Le motif doit être **vérifiable par un tiers** qui n'est pas le
capitaine. Concrètement :

- « Cette dépense n'a pas de date de revue dans le packet B2 » →
  vérifiable : on ouvre le packet, on regarde le champ.
- « Cette dépense n'a pas de métrique chiffrée » → vérifiable :
  on cherche le chiffre, on ne le trouve pas.
- « Cette dépense est inutile » → **PAS** vérifiable → ce n'est
  pas un veto catalogue, c'est un blocage ad hoc.

Conséquence : tout packet mésoperpétuel qui déclenche le veto
Finances contient **un pointeur** vers le champ manquant (la ligne
du packet, le commit, la note de revue).

### 3. Non-négociable au niveau mésoperpétuel

Un capitaine B2 (Batman, Flash, Superman, etc.) ne peut pas
passer outre le veto de Wonder Woman. Les seules issues
(`b2-eight-domain-vetoes-catalogue.md` §« La règle de résolution
quand un veto est opposé ») :

1. **Le mandat est amendé** — le demandeur ajoute date de revue +
   métrique → veto levé.
2. **Le mandat est retiré** — le veto tient, le mandat est mort.
3. **Le veto est escaladé à B1** pour réécriture de la règle
   catalogue (rare).
4. **Le veto est invalide** (manque une des trois propriétés) →
   passe outre.

## Cas concrets où le veto se déclenche

### Cas 1 — Abonnement SaaS sans métrique de ROI

Situation : le B3 produit demande l'achat de Notion AI Pro pour
accélérer la rédaction ($20/utilisateur/mois). Le packet B2 cite
« gain de productivité attendu », pas de chiffre.

- **Veto Wonder Woman ? OUI.** La métrique « gain de
  productivité attendu » n'est pas chiffrée. Le veto tient
  jusqu'à amendement (ex. : « cible : ≥ 3h/semaine gagnées sur 5
  testeurs, revue à 30 jours »).

### Cas 2 — Recurring spend avec date mais sans métrique

Situation : un budget cloud de $500/mois récurrent avec date de
revue trimestrielle, mais sans métrique de retour (le packet ne
dit pas ce que les $500 doivent rapporter).

- **Veto Wonder Woman ? OUI.** Il manque une des deux conditions
  (la métrique). Le veto tient.

### Cas 3 — Recurring spend avec métrique vague

Situation : abonnement Zapier à $50/mois, métrique « devrait
améliorer l'automatisation », pas de payback chiffré.

- **Veto Wonder Woman ? OUI.** « Devrait améliorer » n'est pas
  chiffré. Le veto tient. Amendement possible : « cible : ≥ 10h
  de travail manuel économisées/mois, payback ≤ 1 mois ».

### Cas 4 — Dépense one-shot (pas récurrente)

Situation : un setup fee de $5 000 pour un client, à payer une
seule fois.

- **Veto Wonder Woman ? NON.** Le veto porte explicitement sur
  **récurrent**. Le setup fee a son propre cycle de décision
  (revue pricing, marge brute) qui n'est pas ce veto-là. Le
  discount >15% requiert un sign-off Wonder Woman séparé (cf.
  `03_WONDERWOMAN_FINANCE_PRINCIPLES.md`), mais c'est un veto de
  pricing, pas le veto catalogue récurrent.

### Cas 5 — Engagement annuel prepay (techniquement récurrent mais lissé)

Situation : un contrat annuel Hostinger de $120/an, payé d'avance,
$10/mois amortis.

- **Veto Wonder Woman ? OUI** au sens strict — le contrat est
  récurrent. Mais le packet peut注明 « équivalent $10/mois,
  alignement runway 24 mois ». Le veto tient tant que la
  métrique de retour n'est pas là.

## Cas où le veto serait ABUSIF

Un veto légitime est **catégoriel**. Wonder Woman abuse de son veto
si elle tente de l'utiliser pour :

- **Bloquer une dépense au cas par cas** qu'elle juge mauvaise
  (« je n'aime pas ce SaaS »).
- **Bloquer un investissement productif** sous prétexte qu'il
  consomme du cash (paire-check #5 Growth→Finance : « la
  dépense est-elle justifiée par l'apprentissage ou la traction ? »).
  Si la métrique de retour est chiffrée et la date de revue
  posée, Superman tranche, **pas Wonder Woman**.
- **Bloquer une dépense stratégique (F13-F18)** sous prétexte
  qu'elle ne rentre pas dans le runway. Le veto catalogue porte
  sur la **forme** (date + métrique), pas sur le **fond**
  (stratégie vs opérationnel). Bloquer une dépense stratégique
  qui respecte la forme relèverait d'un blocage ad hoc, pas du
  veto catalogue.
- **Bloquer une dépense de compliance fiscale** (F10, SOP -004).
  Les filings sont obligatoires au-delà de toute métrique de
  retour. Wonder Woman ne peut pas opposer son veto à un
  paiement d'impôt — c'est un blocker externe, pas un arbitrage
  de catalogue.

Si un de ces cas se présente, le packet mésoperpétuel porte la
mention « veto invalide » et le mandate s'exécute. Cf.
`b2-eight-domain-vetoes-catalogue.md` §« Issue 4 — veto invalide ».

## Lien avec le red flag #4 (Finance red + Growth/Product green)

Le veto catalogue **et** le red flag matrice
(`b2-harmonization-matrix-exploitable.md` §« Red flag #4 ») jouent
à des niveaux différents :

- Le veto catalogue bloque **une dépense individuelle récurrente**
  qui n'a pas la forme (date + métrique).
- Le red flag bloque **un lancement** quand Finance est red pendant
  que Growth/Product sont green.

Le veto est un **outil de granularité fine** ; le red flag est un
**arrêt dur transversal**. Voir
[[wonder-woman-red-flag-4-trigger]] pour le détail.

## Lien avec le packet mésoperpétuel

Quand le veto bloque un mandat B2, le packet mésoperpétuel
(`b2-meso-decision-packet-spec.md`) porte :

- `decision: blocked`
- `tradeoff: short statement` mentionnant l'absence de date OU de
  métrique (vérifiable par un tiers)
- `proof_expected` typique : amendment du mandat avec les deux
  champs fournis
- `next_review` : date de la prochaine revue après amendement

## Anti-pièges

- **Veto opposé puis levé sans amendement visible**. Si le veto
  est levé sans que le packet mésoperpétuel montre l'amendement
  (date + métrique ajoutées), c'est un veto qui n'a pas servi. Le
  journal Council perd sa valeur.
- **Veto systématique sur le même domaine**. Si Wonder Woman
  oppose son veto systématiquement aux dépenses Growth ou
  Product, c'est un signal de veto politique (jalousie,
  défense de territoire), pas un veto catalogue. Le Council doit
  le signaler en revue mensuelle.
- **Confondre veto catalogue et blocage ad hoc**. Le veto
  catalogue est un raccourci réservé aux dépenses récurrentes sans
  forme. Les autres blocages Finance (compliance fiscale,
  discount >15%, pricing stratégique) passent par le B2 Council,
  pas par ce veto.

## Liens

- [[wonder-woman-finance-frontiers]] — le périmètre racine
- [[wonder-woman-red-flag-4-trigger]] — le red flag #4 qui complète le veto
- [[wonder-woman-finance-couplings]] — qui dépend du veto
- [[b2-eight-domain-vetoes-catalogue]] — la théorie des 8 vetos
- [[b2-meso-decision-packet-spec]] — le format qui porte le motif du veto

## Note de confiance

**Confirmé par machine.** Le veto catalogue est cité verbatim
(`triplets/v3-business.jsonl` ligne 28 + `b2-eight-domain-vetoes-catalogue.md`).
Les 4 cas de déclenchement et les 4 cas d'abus sont **projetés** à
partir de la définition (« récurrente + sans date + sans métrique »)
et des principes Finance (F19-F22 sur l'allocation, F23-F25 sur
l'arbitrage ROI, F10 sur compliance qui contourne le veto). À
vérifier en cycle réel : la doctrine distinguera-t-elle toujours
« one-shot setup fee » (pas de veto) vs « recurring with annual
prepay » (veto) ?
