---
type: Concept
title: Veto Superman — cinq cas concrets où il bloque légitimement, trois où il serait abusif
description: Le veto Superman (Growth/01) bloque "toute prise de parole publique qui promet un résultat que la delivery ne tient pas". Le veto est catégoriel, vérifiable, non-négociable au niveau mésoperpétuel. Cinq cas concrets de déclenchement légitime (claim sans date, démo sans DoD, case-study sans contrat, intégration annoncée sans build, métrique de traction sans source). Trois cas où il serait abusif (proof path négatif, claim vérifié a posteriori, refactor de formulation).
tags: [superman, growth, veto, catalogue, b2, promesse, delivery, abus]
generated: { by: minimax-m3, at: 2026-08-19T04:01:00Z }
verified:
  - { by: process:lecture-corpus-superman, at: 2026-08-19T04:01:00Z }
sources:
  - id: vetoes-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — Superman (Growth) ligne 27
    last_modified: 2026-08-19
  - id: triplet-v3-line-27
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet v3 ligne 27 — Superman hasVetoOver promesse-non-tenue"
    last_modified: 2026-08-17
  - id: org-json
    resource: "C:/Users/amado/ASpace_OS_V3/../ASpace_OS_V2/30_Business_OS/10_Projects/coach-os/ORG.json"
    title: Coach OS ORG.json — vetos catalogue
    last_modified: 2026-08-02
  - id: veto-amplification
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: Amplification des vetos B2 — cycle vivant, 3 conditions
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Veto Superman — cinq cas concrets où il bloque légitimement, trois où il serait abusif

## Le veto canonique

Triplet v3 ligne 27, cité verbatim depuis `coach-os/ORG.json` :

> *« Superman bloque toute prise de parole publique qui promet un
> résultat que la delivery ne tient pas. »*

`b2-eight-domain-vetoes-catalogue.md` pose ce veto comme **classe
#5** du catalogue 8 vetos (catégoriel, vérifiable, non-négociable
au niveau mésoperpétuel). Le triplet 58 (Wonder Woman étend) montre
qu'un veto peut être amplifié — voir
`veto-amplification-candidate.md` pour l'amplification candidate de
Superman.

## Cinq cas où le veto se déclenche légitimement

### 1. Claim sans date (« ROI en 30 jours » sans DoD daté)

Un mandat B2 Growth demande à Groot (B3 Content) de produire un
blog post qui annonce *« ROI en 30 jours »* pour un segment précis.
Le DoD du squad est de tenir la promesse sur 30 jours mesurés.

**Pourquoi le veto tient** : la promesse est publique, chiffrée,
mais le DoD de delivery (Sales × Ops × Finance × People) n'a pas
été validé. Le ROI peut être < promesse ; le client peut le mesurer
différemment ; la promesse n'est pas tenable répétitivement.

**Forme de l'opposition** : Superman consigne `veto: promesse-non-tenue,
classe: claim-sans-date, source: Groot-blogpost-2026-Q3,
next_review: <date-fin-30j>` dans le packet mésoperpétuel.
L'amplification candidate (date ou horizon mesurable) rend le veto
plus strict.

### 2. Démo produit sans DoD supportable

Un mandat B2 Growth organise un webinar avec démo live. La démo
utilise un endpoint staging qui n'est pas représentatif du prod. Ops
(Batman) n'a pas validé que la démo peut rejouer en démo live
répétée sans incident.

**Pourquoi le veto tient** : la prise de parole publique (webinar)
promet une expérience (le produit marche) que la delivery (Ops)
n'a pas garantie. Si la démo crashe, le claim « le produit marche »
est rompu publiquement.

**Forme de l'opposition** : `veto: promesse-non-tenue, classe:
demo-sans-dod, source: webinar-2026-Q3-staging-vs-prod`.

### 3. Case-study publié sans contrat signé

Un mandat B2 Growth demande à Mantis (B3 VoC) de publier un
case-study « Client X a obtenu Y résultat ». Le client n'a pas
signé d'autorisation de publication, et Legal (Aquaman) n'a pas
validé le périmètre.

**Pourquoi le veto tient** : la promesse publique est conditionnée
à un accord client — qui n'existe pas. C'est un claim conditionnel
traité comme absolu. Aquaman peut aussi veto (classe Legal :
prestation sans accord écrit), mais Superman tient un veto
indépendant sur la parole publique.

**Forme de l'opposition** : `veto: promesse-non-tenue, classe:
case-study-sans-contrat, source: Mantis-casestudy-client-X,
cross-veto: Aquaman-aquaman-contrat-non-signe`.

### 4. Intégration annoncée avant build

Un mandat B2 Growth annonce une intégration avec un partenaire Z
sur le site public et dans les emails sortants, avant que le PR
Product × IT (matrice d'harmonisation critère #4) ne soit mergé.

**Pourquoi le veto tient** : la parole publique promet une
capacité technique qui n'existe pas encore en prod. Si l'intégration
est repoussée ou annulée, le claim devient une promesse non tenue.

**Forme de l'opposition** : `veto: promesse-non-tenue, classe:
integration-annoncee-avant-build, source: Groot-emails-partenaire-Z,
proof-expected: PR-marchera-prod-date-X`.

### 5. Métrique de traction sans source

Un mandat B2 Growth publie *« 10,000 utilisateurs actifs »* ou
*« 100% NPS »* sans citer la fenêtre temporelle, la cohorte, ou la
méthode de mesure. La métrique est invérifiable par un lecteur
tiers.

**Pourquoi le veto tient** : la promesse publique (chiffre) est
in vérifiable. C'est une **classe distincte du claim sans date** :
la promesse est chiffrée mais pas auditée. Le veto tient sans
amplification, parce que le canon « traçabilité » est posé par D4
append-only.

**Forme de l'opposition** : `veto: promesse-non-tenue, classe:
metrique-sans-source, source: Groot-press-release-NPS-100`.

## Trois cas où le veto serait **abusif**

Un veto abusif est un veto **catégoriellement valide mais
contextuellement faux** — il bloque un cas qui ne tombe pas dans la
classe. Trois pièges concrets :

### Abusif 1 — Proof path négatif utilisé comme veto

Un B3 signale un proof path qui montre que **la promesse est déjà
non tenue**. Superman peut citer le veto pour geler la parole
publique. Mais le veto porte sur la **promesse à venir**, pas sur
la **promesse passée**. Le proof path négatif est un *fait* à
remonter au captain sponsor (Batman pour Ops × Sales, ou Flash pour
Product) — pas un veto Growth.

**Distinction** : *« la promesse n'a pas été tenue hier »* ≠ *« la
promesse ne sera pas tenue demain »*. Le veto porte sur la seconde.

### Abusif 2 — Claim vérifié a posteriori

Un claim est publié, puis vérifié a posteriori par un B3 ou un
tiers (PostHog, mixpanel, audit client). Si le claim est confirmé,
Superman ne peut pas maintenir un veto rétroactivement sur un
**claim tenu**. Le veto catalogue bloque les claims *non-tenables
répétitivement*, pas les claims passés qui ont été vérifiés.

**Distinction** : *« je veto un claim futur qui n'est pas tenable »*
vs *« je veto un claim passé qui a été tenu »*. Le second est
abusif.

### Abusif 3 — Refactor de formulation

Un claim est reformulé (changement de wording, ajustement de
promesse) pour lever un veto précédent. Superman refuse le refactor
en disant *« le veto tient, je ne lève pas »*. C'est abusif si la
nouvelle formulation a un DoD tenable et un proof path valide. Le
veto porte sur la **classe** (promesse non tenue), pas sur le
**mot** utilisé.

**Distinction** : *« la formulation est inchangée, donc le veto
tient »* vs *« la nouvelle formulation a un DoD tenable, le veto
est levé »*. Le second est la procédure canonique.

## Pourquoi le veto Superman est **le plus difficile à opérationnaliser**

Comparé aux 7 autres vetos catalogue :

| Capitaine | Veto | Critère de vérification |
|---|---|---|
| Green Lantern | recrutement sans mandat | mandat écrit (vérifiable) |
| Batman | procédure sans condition d'arrêt | condition d'arrêt écrite |
| Flash | valeur dépend d'une personne | DoD non-personne-dépendant |
| JohnJones | proposition sans problème reformulé | problème client validé |
| **Superman** | **promesse que la delivery ne tient pas** | **tenabilité de la delivery (pas un document, une pratique)** |
| Wonder Woman | dépense sans revue | date et métrique écrites |
| Cyborg | fournisseur cloud-only sans sortie | chemin de sortie documenté |
| Aquaman | prestation sans accord écrit | accord écrit |

Sept vetos portent sur des **artefacts documentaires vérifiables**.
Le veto Superman porte sur une **pratique de delivery** — quelque
chose qui n'est pas un document mais une trajectoire. Conséquence :
le motif du veto doit citer **les critères de la matrice
d'harmonisation qui ne sont pas validés** (ex : Finance × Growth —
la dépense paid media n'a pas de métrique de retour), pas
simplement *« la promesse n'est pas tenable »*.

## La règle de résolution

`b2-eight-domain-vetoes-catalogue.md` pose 4 issues :

1. **Mandat amendé** : le mandat B2 ajoute un DoD daté et un proof
   path → arbitrage accepté, veto levé.
2. **Mandat retiré** : B1 retire le mandat → `decision: blocked`,
   motif = veto.
3. **Veto escaladé B1** : Superman maintient le veto face à un
   mandat B1 → `decision: escalate_to_B1`, motif = veto + demande
   de réécriture de la classe.
4. **Veto invalide** : le veto manque une des 3 propriétés
   (catégoriel/vérifiable/non-négociable) → Council passe outre.

Pour Superman, la **vérifiabilité** (propriété #2) est le point
d'achoppement. Un veto qui ne cite pas la pair-check matrice
manquante est invalide.

## Anti-pièges

- **Veto sur parole interne.** Le veto porte sur la parole **publique**
  (cf. triplet 27 verbatim). Une parole interne (Slack, email
  interne, draft non publié) n'est pas une prise de parole publique.
  Superman n'a pas de veto sur la parole interne.
- **Veto rétroactif.** Un veto qui bloque un claim passé qui a été
  tenu est invalide (cf. Abusif 2).
- **Veto par défaut.** Sans pair-check matrice manquante citée, le
  veto n'est pas vérifiable. Le captain sponsor doit refuser le veto
  « flou ».
- **Veto comme outil de gel.** Un veto qui dure > 1 cycle 12WY sans
  amendement de mandat doit escalader B1 pour réécriture. Le veto
  n'est pas un état permanent — c'est un blocage avec date de revue.

## Liens

- [[b2-eight-domain-vetoes-catalogue]] — le catalogue 8 vetos
- [[b2-veto-amplification-cycle]] — comment amplifier (3 conditions)
- [[veto-amplification-candidate]] — l'amplification candidate pour
  Superman
- [[domain-perimeter]] — les frontières où le veto s'applique
- [[pair-checks-dependencies]] — les pair-checks que le veto cite
- [[jtbd-emit-receive]] — les paquets B3 où le veto peut être
  consigné

## Note de confiance

**Confirmé par machine, reconstruit pour les cas.** Le veto canonique
est cité verbatim du triplet ligne 27 et de `b2-eight-domain-vetoes-catalogue.md`.
Les 5 cas concrets de déclenchement légitime sont **projetés** à
partir de la pratique documentée (matrice d'harmonisation + RACI par
rang + triplet 58 Wonder Woman extension) — ce ne sont pas des cas
historiques du corpus, mais des **cas-limites plausibles** que le
veto est censé couvrir. Les 3 cas abusifs sont **reconstruits** par
lecture critique du triplet 27 et de la propriété « vérifiable » du
catalogue. La difficulté d'opérationnalisation (table comparatif 8
vetos) est **projetée** à partir des triplets ligne 24-31 et de la
doctrine D4 append-only.
