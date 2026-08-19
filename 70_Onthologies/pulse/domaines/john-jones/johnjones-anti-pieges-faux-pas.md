---
type: Concept
title: JohnJones — anti-pièges spécifiques, faux pas typiques et abus de position B2
description: Six anti-pièges spécifiques au domaine Sales : (1) vendre avant la reformulation, (2) confondre Closer et Discovery, (3) faire la lecture cognitive au niveau captain, (4) numéroter Sales = 04 dans les concepts canoniques, (5) escalader un veto reformulation sans packet vérifiable, (6) confondre pair-check #1 A et pair-check #2 A. Le SPRINT 2026-08 active 4 charges sur 6 et désactive Closer/Negotiation — un précédent à documenter.
tags: [b2, johnjones, sales, anti-pieges, abus, doctrine, vente, reformulation, raci]
generated: { by: minimax-m3, at: 2026-08-19T04:30:00Z }
verified:
  - { by: process:lecture-corpus-sales, at: 2026-08-19T04:30:00Z }
sources:
  - id: vp-soul-sales
    resource: "C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os/04_Business_Domains/04_Sales_et_Cognition_MartianManhunter_Illuminati/VP_SOUL.md"
    title: VP_SOUL — Martian Manhunter — cognition précède la vente
    last_modified: 2026-08-02
  - id: sprints-sales
    resource: "C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os/04_Business_Domains/04_Sales_et_Cognition_MartianManhunter_Illuminati/SPRINTS.md"
    title: SPRINTS — Pourquoi BlackBolt/Namor pas dans le tableau, Why DoctorStrange en S4
    last_modified: 2026-08-02
  - id: veto-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — anti-pièges génériques
    last_modified: 2026-08-19
  - id: raci-par-rang
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks
    last_modified: 2026-08-19
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — Sales = 02 canonique
    last_modified: 2026-08-17
okf_version: "0.2"
---

# JohnJones — anti-pièges spécifiques

## Anti-pièce #1 — Vendre avant la reformulation validée

**Symptôme** : un commercial (BlackBolt Closer, Namor Negotiation,
ou un capitaine qui prend le rôle de closer) pousse une propale
avant que MrFantastic (Discovery) ait mené l'entretien et que
ProfessorX (BuyerRead) ait posé la reformulation.

**Source verbatim** (`VP_SOUL.md`) :

> *« Vendre le coaching en lisant le modèle mental de l'acheteur,
> pas en récitant l'offre. La cognition précède la vente : qui n'a
> pas nommé le problème du client ne peut pas lui vendre la
> solution. »*

**Détection** : un `LINK_TO_OFFER.md` qui n'a pas de `CLIENT_VALIDATION_*.md`
en amont. Le pipeline commercial s'allonge sans reformulation
validée.

**Remède** : veto reformulation-non-validée opposée. Le packet
mésoperpétuel documente le motif *« pas de reformulation validée »*
et le mandat est amendé (reprendre discovery → reformulation →
validation) ou retiré.

**Citation opérante** (`SPRINTS.md` §« Ce que ce mois ne fait pas ») :

> *« Pas de proposition écrite envoyée à un prospect. Le veto de
> domaine l'interdit avant l'étape 3. »*

## Anti-pièce #2 — Confondre Closer et Discovery

**Symptôme** : BlackBolt (Closer) mène un entretien de discovery,
ou MrFantastic (Discovery) pousse une conclusion. Le Closer doit
clore, le Discovery doit découvrir — deux actes différents sur
deux horizons différents (Closer = H1 closing, Discovery = H10
discovery).

**Détection** : un `INTERVIEW_01_RAW.md` qui contient une demande
de signature, ou un `SALES_COMMITMENT.md` qui ne contient pas
de verbatim discovery.

**Remède** : ré-allocation de charge. Si Closer et Discovery sont
confondus, c'est que le captain n'a pas tranché la séquence. Le
sprint doit explicitement marquer qui fait quoi.

**Citation opérante** (`SPRINTS.md` §« Pourquoi BlackBolt et Namor
ne sont pas dans le tableau ») :

> *« Closer et négociation n'ont rien à conclure ni à négocier ce
> mois-ci. »*

## Anti-pièce #3 — Faire la lecture cognitive au niveau captain

**Symptôme** : JohnJones (capitaine B2) prétend porter la lecture
du modèle mental de l'acheteur. C'est une charge ProfessorX (B3
squad Illuminati), pas une charge captain.

**Source verbatim** (`VP_AGENT.md` §« Mon squad — Illuminati ») :

> *« ProfessorX — BuyerRead : la lecture de l'acheteur. Décide du
> modèle mental en face. »*

**Détection** : un arbitrage Council qui attribue la lecture
cognitive au captain, ou un `SPRINTS.md` où ProfessorX n'apparaît
pas mais le captain dit *« j'ai lu le client »*.

**Remède** : allouer ProfessorX explicitement dans le sprint.
Sprint 2026-08 §« Les quatre sprints » fait cela — ProfessorX est
présent en S1 et S3.

**Citation opérante** (doctrine E-Myth Manager E-Myth, Ownerbook T1) :

> *« Le Manager ne fait pas le geste du technicien. »*

## Anti-pièce #4 — Numéroter Sales = 04 dans les concepts canoniques

**Symptôme** : un concept OKF ou un packet mésoperpétuel qui
numérote Sales en 04 (la position Coach OS V3), au lieu de 02 (la
position canonique 8-domain wheel). C'est une erreur de
numérotation qui propage dans tous les référentiels.

**Source verbatim** (`eight-domain-avengers-wheel.md` tableau
mapping ligne 41) :

> *« 02 Sales — Martian Manhunter (legacy) / JohnJones (W40 V4)
> — Illuminati »*

**Détection** : un arbitrage Council ou un RACI qui dit *« Sales =
04 »* et qui croise avec un autre document qui dit *« Sales = 02 »*.
La cross-propagation ne marche pas.

**Remède** : adopter la numérotation **canonique 02** dans tous
les concepts OKF et packets mésoperpétuels. Le code 04 de Coach OS
est noté mais pas adopté (cf.
[[johnjones-domaine-sales-perimetre]] §« La position canonique :
Sales = 02, Coach OS = 04 »).

## Anti-pièce #5 — Escalader un veto reformulation sans packet vérifiable

**Symptôme** : JohnJones oppose son veto reformulation-non-validée
mais le packet mésoperpétuel ne contient pas le motif précis —
*« pas de reformulation »* sans pointer le fichier manquant.

**Source verbatim** (`b2-eight-domain-vetoes-catalogue.md`
§« Les trois propriétés d'un veto légitime » propriété 2) :

> *« Le motif doit être vérifiable par un tiers qui n'est pas le
> capitaine. *« Je bloque cette dépense »* n'est pas vérifiable.
> *« Cette dépense n'a pas de date de revue dans le packet, cf.
> ligne 23 »* est vérifiable. »*

**Détection** : un veto qui revient systématiquement sans packet
vérifiable, ou un Council qui passe outre un veto faute de preuve.

**Remède** : poser le motif en triple référence
(`CLIENT_VALIDATION_*.md` absent, `INTERVIEW_01_RAW.md` absent,
`LINK_TO_OFFER.md` absent), avec les chemins de fichiers. Le veto
est légitime par construction.

## Anti-pièce #6 — Confondre pair-check #1 A et pair-check #2 A

**Symptôme** : un arbitrage Council qui dit *« JohnJones est A sur
Sales → Ops »* (pair-check #2), alors que le RACI par rang donne A
à B2 Ops sur #2 et A à B2 Sales sur #1 (Growth → Sales).

**Source verbatim** (`b2-pair-check-raci-by-rank.md` §« Pourquoi
A = B2 en aval, pas B1 ») :

> *« A est toujours le B2 captain en aval de la transition (le
> domaine qui reçoit). »*

**Détection** : un packet mésoperpétuel qui prend JohnJones comme A
sur #2 (Sales → Ops). C'est une erreur de RACI.

**Remède** : ré-écrire le packet avec A = B2 Ops sur #2, C = B2
Sales. JohnJones reste A sur #1 (Growth → Sales).

## Anti-pièce #7 — Activer DoctorStrange avant la reformulation validée

**Symptôme** : un sprint où DoctorStrange (Forecasting) pose un
chiffre de pipeline avant que MrFantastic (Discovery) et
ProfessorX (BuyerRead) aient livré la reformulation validée et le
lien à l'offre.

**Source verbatim** (`SPRINTS.md` §« Pourquoi DoctorStrange
n'apparaît qu'en S4 ») :

> *« Le forecasting ne sert qu'une fois qu'on a un problème
> reformulé et validé. Lui demander un chiffre avant, c'est faire
> semblant. »*

**Détection** : un `FORECAST_*.md` qui n'a pas de
`CLIENT_VALIDATION_*.md` en amont.

**Remède** : ré-ordonner le sprint. DoctorStrange en S4 minimum.

## Le précédent du SPRINT 2026-08

Le SPRINT 2026-08 documente **un cas où 4 charges sur 6 sont
désactivées explicitement** :

- BlackBolt (Closer) — désactivé ce mois-ci.
- Namor (Negotiation) — désactivé ce mois-ci.
- ProfessorX (BuyerRead) — actif S1 + S3.
- MrFantastic (Discovery) — actif S1 + S2 + S3.
- IronMan (Demo) — actif S4.
- DoctorStrange (Forecasting) — actif S4.

C'est **un précédent utile** : un domain captain qui désactive
explicitement des charges B3, avec un motif documenté, plutôt que
de les laisser inactives silencieusement. La doctrine canonique
E-Myth Manager suppose que le VP sait ce qu'il active.

Conséquence : un domain captain qui n'arrive pas à motiver
explicitement ses désactivations **manque la discipline SPRINT**. Le
SPRINTS.md 2026-08 est un modèle — pas parce qu'il est parfait,
mais parce qu'il documente ses choix.

## Les trois abus de position (analogues aux abus Aquaman)

`b2-eight-domain-vetoes-catalogue.md` §« Anti-pièges » liste 4 abus
génériques (cas spécifique sous couvert de classe, périmètre
implicite mais vérifiable, veto levé sans amendement, veto absent
alors qu'il devrait être opposé). Pour Sales, trois abus
spécifiques :

1. **Bloquer une propale reformulée-validée parce qu'on n'aime pas
   le client.** Le veto porte sur la classe (proposition sans
   reformulation), pas sur le client. Bloquer un client nommé est
   un abus.
2. **Lever le veto sous pression commerciale** (*« le commercial a
   promis, on valide quand même »*). Le veto levé sans amendement
   visible du mandat est un abus.
3. **Veto sur du non-Sales** (par exemple, JohnJones qui bloque une
   dépense récurrente cloud — c'est le veto Wonder Woman Finance
   ou Cyborg IT). Un JohnJones qui bloque au-delà de son périmètre
   est overreach.

## Anti-pièges

- **Vendre avant discovery** (anti-pièce #1).
- **Closer qui discovery** (anti-pièce #2).
- **Captain qui BuyerRead** (anti-pièce #3).
- **Numéroter Sales = 04** (anti-pièce #4).
- **Veto sans packet vérifiable** (anti-pièce #5).
- **A = Sales sur pair-check #2** (anti-pièce #6).
- **Forecast avant reformulation validée** (anti-pièce #7).

## Liens

- [[b2-eight-domain-vetoes-catalogue]] — abus génériques de veto
- [[b2-pair-check-raci-by-rank]] — A vs C sur les pair-checks
- [[eight-domain-avengers-wheel]] — numérotation canonique 02
- [[johnjones-domaine-sales-perimetre]] — le périmètre qui sous-tend les anti-pièces
- [[johnjones-veto-reformulation-validee]] — veto et abus
- [[johnjones-jtbd-emit-receive]] — charges activées ce mois-ci
- [[johnjones-gates-et-pair-checks]] — gates mésoperpétuels émis

## Note de confiance

**Confirmé par machine, à moitié.** Les 7 anti-pièces sont **projetés**
depuis la doctrine canonique (veto catalogue, RACI par rang, E-Myth
Manager) et la pratique documentée dans `SPRINTS.md`. Les citations
opérantes sont verbatim pour 5 anti-pièces (#1, #2, #3, #4, #6, #7).
Les 3 abus de position sont projetés depuis les abus génériques
`b2-eight-domain-vetoes-catalogue.md`. Le précédent SPRINT 2026-08
est cité verbatim — c'est un **cas observable**, pas une
généralisation.