---
type: Concept
title: JohnJones veto — reformulation-validée, déclenchement et abus
description: Le veto catalogue de JohnJones bloque toute proposition envoyée avant qu'un problème client ait été reformulé et validé par le client. Le motif est double (reformulation écrite en mots client + validation explicite). Les trois propriétés canoniques s'appliquent (catégoriel, vérifiable, non-négociable au niveau mésoperpétuel). Les abus typiques : bloquer une proposition qui a une reformulation mais pas de validation formelle, ou lever le veto sous pression commerciale.
tags: [b2, johnjones, sales, veto, reformulation, validation, client, proposition, catalogue]
generated: { by: minimax-m3, at: 2026-08-19T04:05:00Z }
verified:
  - { by: process:lecture-corpus-sales, at: 2026-08-19T04:05:00Z }
sources:
  - id: triplet-26
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 26 — Martian Manhunter hasVetoOver proposition-sans-reformulation"
    last_modified: 2026-08-17
  - id: org-json-veto
    resource: "C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os/ORG.json"
    title: Coach OS ORG.json — Martian Manhunter veto
    last_modified: 2026-08-02
  - id: veto-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — un domaine, un blocage légitime
    last_modified: 2026-08-19
  - id: sprints-sales
    resource: "C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os/04_Business_Domains/04_Sales_et_Cognition_MartianManhunter_Illuminati/SPRINTS.md"
    title: SPRINTS — Martian Manhunter · Sprint 1 critères reformulation valide + validation client
    last_modified: 2026-08-02
okf_version: "0.2"
---

# JohnJones veto — reformulation-validée

## Le motif canonique

Triplet 26 (verbe `hasVetoOver`) : *« Martian Manhunter bloque toute
proposition envoyée avant qu'un problème client ait été reformulé et
validé par le client. »*

`SPRINTS.md` mois 2026-08 §« Mois 2026-08 — rock hérité » précise
le motif sous une forme **opérante** :

> *« Au moins un problème client a été reformulé et validé par le
> client, puis relié explicitement à la promesse de l'offre. »*

Le motif est **double** (reformulation + validation) et il est
**doublement lié** (à l'offre). Les deux sont cumulatifs :

- **Reformulation** — le problème est-il écrit dans les mots du
  client (pas ceux du vendeur) ? Une reformulation qui paraphrase
  l'offre Coach OS au lieu de citer le client n'est pas une
  reformulation, c'est un pitch.
- **Validation explicite** — le client a-t-il confirmé cette
  reformulation par signature, mail daté, ou tout écrit vérifiable ?
  Sans cette trace, la reformulation est unilatérale.
- **Lien explicite à l'offre** — le problème reformulé pointe-t-il
  sur une promesse précise de l'offre ? C'est ce qui empêche une
  reformulation générique suivie d'une vente opportuniste.

`SPRINTS.md` Sprint 1 pose trois critères minimaux pour la
reformulation valide et trois critères minimaux pour la validation
client — six critères cumulatifs.

## Quand le veto se déclenche (cas concrets)

Cinq cas où le veto s'oppose de manière légitime, observés dans le
corpus B2 et la doctrine OMK :

1. **Proposition orale sans trace.** Un commercial qui sort un *« on
   vous envoie une propale »* sans discovery préalable — JohnJones
   oppose le veto avant l'envoi.
2. **Propale basée sur un brief de demande non reformulé.** Le client
   a demandé *« on a un problème de rétention »* mais aucune
   reformulation écrite en ses mots n'a été signée — veto.
3. **Reformulation paraphrasant l'offre au lieu de citer le client.**
   *« Vous avez besoin d'un coaching structuré »* — c'est la reformulation
   du vendeur, pas du client. Veto.
4. **Validation par oral uniquement.** Le client a dit *« OK ça me
   parle »* au téléphone, mais aucun écrit daté — veto. La
   validation doit être vérifiable par un tiers qui n'était pas
   dans la conversation.
5. **Lien reformulation-offre manquant.** Le problème reformulé ne
   pointe sur aucune promesse précise de l'offre — veto, parce que
   la proposition qui suivrait n'aurait pas de cohérence vérifiable.

`SPRINTS.md` §« Ce que ce mois ne fait pas » liste explicitement
*« Pas de proposition écrite envoyée à un prospect. Le veto de
domaine l'interdit avant l'étape 3. »*

## Quand le veto serait abusif

Cinq cas où invoquer le veto serait un détournement de la classe
catalogue (cf. `b2-eight-domain-vetoes-catalogue.md` §Anti-pièges) :

1. **Bloquer un cas spécifique sous couvert de la classe.** *« Ce
   client, je bloque parce qu'il n'a pas validé »* n'est pas un veto
   catalogue — c'est un blocage ad hoc. Le veto porte sur **toute
   proposition sans reformulation validée**, pas sur un client nommé.
2. **Veto sur reformulation valide mais cross-cycle.** Une
   reformulation validée il y a 6 mois pour un produit A ne
   s'applique pas à un produit B. Si JohnJones oppose le veto
   cross-cycle sans le dire, c'est abusif.
3. **Veto levé sous pression commerciale.** *« Le commercial a
   promis au client, on valide quand même »* — c'est un veto levé
   sans amendement visible du mandat. Le packet mésoperpétuel doit
   documenter l'amendement, sinon la trace est faible.
4. **Veto sur du non-Sales.** Un autre capitaine oppose un veto qui
   n'est pas le sien. JohnJones qui bloque une dépense cloud
   récurrente (c'est le veto de WonderWoman) est overreach.
5. **Veto rétroactif.** JohnJones découvre a posteriori qu'une de
   ses propositions aurait dû être bloquée — il escalade pour
   relecture, pas un veto rétroactif.

## Les trois propriétés canoniques (cf. veto catalogue)

Le veto JohnJones est légitime ssi les trois propriétés suivantes
sont remplies (cf. `b2-eight-domain-vetoes-catalogue.md`) :

### 1. Catégoriel

Le veto porte sur une **classe** (toute proposition sans
reformulation-validée-liée), pas sur un cas. JohnJones ne peut pas
bloquer *ce* client sous couvert de la classe — il peut bloquer
*toute* proposition sans reformulation validée.

Conséquence : un JohnJones qui refuse de réviser la classe catalogue
quand un cas-limite émerge (par exemple, une proposition dont la
reformulation est implicite mais évidente) est en dérive. Le
catalogue reste à 8 classes, mais une **amplification** peut être
soumise au Council (cf. `b2-veto-amplification-cycle.md`).

### 2. Vérifiable

Le motif doit être **écrit** dans le packet mésoperpétuel ou dans
le journal Council. *« Je bloque cette propale »* n'est pas
vérifiable. *« Cette propale n'a pas de reformulation en mots
client (cf. transcript manquant), ni de validation explicite (cf.
mail absent), ni de lien reformulation-offre »* est vérifiable.

`SPRINTS.md` Sprint 1 rend le motif **vérifiable par construction** :
le fichier `INTERVIEW_CANVAS.md` contient les 3 critères reformulation
valide et les 3 critères validation client, le `INTERVIEW_01_RAW.md`
contient la trace verbatim, et le `CLIENT_VALIDATION_01.md` contient
la preuve de validation. Sans ces trois fichiers, le motif est
invérifiable.

### 3. Non-négociable *au niveau mésoperpétuel*

Un capitaine B2 ne peut pas passer outre le veto d'un autre
capitaine B2. Superman (Growth) ne peut pas dire *« OK on lance la
campagne même sans reformulation validée, c'est une exception »*.
La seule option est d'escalader B1 pour amender la règle catalogue.

## La règle de résolution

Quatre issues possibles, par ordre de fréquence
(cf. `b2-eight-domain-vetoes-catalogue.md` §Règle de résolution) :

1. **Le mandat est amendé** avant le dispatch B3. Le commercial
   complète la séquence discovery → reformulation → validation →
   liaison. **Résultat : arbitrage accepté, mode inchangé.**
2. **Le mandat est retiré** par B1 ou par le commercial qui le
   portait. Le veto tient, le mandat est mort. **Résultat : packet
   mésoperpétuel avec `decision: blocked`, motif = veto
   reformulation-non-validée.\*\***
3. **Le veto est escaladé à B1** pour réécriture de la règle
   catalogue. **Résultat : `decision: escalate_to_B1`.** Très
   rare — B1 ne réécrit pas les vetos à la légère.
4. **Le veto est invalide** (manque une des trois propriétés). Le
   Council passe outre. **Résultat : packet mésoperpétuel avec note
   d'invalidation.**

## Amplification candidate — projetée

`b2-veto-amplification-cycle.md` §« Trois amplifications candidates »
ne mentionne pas JohnJones. Mais une amplification candidate est
projetable :

> **Veto canonique** : bloque toute proposition sans reformulation
> validée. **Amplification candidate** : la reformulation doit
> dater de moins de 90 jours, et la validation doit être révocable
> (le client peut la retirer).

**Why projetée** : une reformulation vieille de 6 mois peut ne plus
refléter le problème actuel du client (le client a changé, le
marché a changé). Une validation non révocable lie le client à une
lecture qu'il ne peut plus corriger. Les deux cas-limites sont
observés dans la pratique documentée mais pas dans le triplet v3.

Cette amplification n'est **pas soumise** au Council — elle est
notée ici comme candidate, à discuter en cycle réel.

## Anti-pièges spécifiques JohnJones

- **Veto sur pitch déguisé en discovery.** Une conversation où le
  commercial passe 80% du temps à pitcher et 20% à écouter n'est
  pas une discovery. Le veto s'oppose, mais le motif est *« discovery
  absente »*, pas *« reformulation absente »*. Le packet doit
  documenter la distinction.
- **Confondre reformulation et résumé de brief.** *« Le client veut
  résoudre X, Y, Z »* est un résumé de brief, pas une reformulation.
  Une reformulation cite les mots du client (verbatim ou
  quasi-verbatim).
- **Validation par le décideur, pas par le contact.** Si le contact
  qui valide n'est pas le décideur qui signera, la validation est
  faible. Le packet doit documenter le rôle du validateur.
- **Veto oublié sur le repeat business.** Un client existant qui
  achète une nouvelle offre n'a pas besoin d'une nouvelle discovery
  pour le **même** problème. Mais il en a besoin pour un
  **problème nouveau**. Le veto porte sur la proposition, pas sur le
  client.

## Liens

- [[b2-eight-domain-vetoes-catalogue]] — la doctrine veto applicable
- [[johnjones-domaine-sales-perimetre]] — le périmètre du domaine qui
  légitime le veto
- [[johnjones-gates-et-pair-checks]] — gates SALES_READY /
  NEEDS_QUALIFICATION / BLOCKED_COMMITMENT
- [[b2-pair-check-raci-by-rank]] — pair-checks #1 (C) et #2 (A)
- [[b2-meso-decision-packet-spec]] — format packet où le motif est écrit
- [[b2-veto-amplification-cycle]] — procédure pour étendre le veto

## Note de confiance

**Confirmé par machine.** Motif verbatim triplet 26 et `ORG.json`.
Trois propriétés canoniques tirées verbatim de
`b2-eight-domain-vetoes-catalogue.md`. Les 5 cas de déclenchement
incluent 4 projetés (1 cité verbatim de `SPRINTS.md`). Les 5 cas
d'abus sont **projetés** depuis la doctrine veto + matrice
d'harmonisation. L'amplification candidate est **explicitement
projetée**, pas étayée par un triplet canonique.