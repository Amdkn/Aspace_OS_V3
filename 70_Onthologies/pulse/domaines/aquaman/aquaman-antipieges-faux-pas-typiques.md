---
type: Concept
title: Aquaman — anti-pièges et faux pas typiques du domaine Legal
description: Six anti-pièges typiques du domaine Aquaman : confondre dormant et absent, veto sur cas spécifique sous couvert de classe, périmètre implicite non documenté, Aquaman qui opère au lieu de cadrer, DoD invérifiable, et Aquaman qui signe sans matrice de signature People. Chaque anti-piège a un signal et un remède.
tags: [b2, aquaman, anti-pieges, dormant, veto, dod, signature, cadre]
generated: { by: minimax-m3, at: 2026-08-19T03:55:00Z }
verified:
  - { by: process:lecture-canon-aquaman, at: 2026-08-19T03:55:00Z }
sources:
  - id: legal-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/README.md"
    title: 08 Legal - Aquaman / Eternals — Operating Rule
    last_modified: 2026-05-25
  - id: veto-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — anti-pièges
    last_modified: 2026-08-19
  - id: legal-pipeline
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md"
    title: Rock → DoD → JTBD Pipeline — DoD Quality Bar
    last_modified: 2026-05-27
  - id: legal-control-room
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: Legal Control Room — B2 Must Not
    last_modified: 2026-05-27
  - id: harmonization-md
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — pair checks
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Aquaman — anti-pièges et faux pas typiques

## Anti-piège 1 — Confondre dormant et absent

**Le faux pas** : un Aquaman qui ne produit pas de `SPRINTS.md`
Legal est parfois pris pour un Aquaman *inactif*, voire
*inutile*. La tentation est de *« réveiller »* le domaine en lui
donnant un Rock inventé (par exemple *« cartographier les risques
Legal »*).

**Le signal** : un Rock Legal sans Master Agreement à traiter, ou
un Rock dont le livrable ne sera *jamais consommé* par personne.

**Le remède** : rappeler la doctrine des triplets 35 et 36 — le
domaine est dormant, pas absent. Le veto catalogue tient, les
pair-checks sont Consulted, mais le *flow de production* est gelé.
Forcer un Rock inventé, c'est créer un coût pur.

**Source** : triplet 35 *« un domaine dormant qui produit est un
coût sans contrepartie »*.

## Anti-piège 2 — Veto sur cas spécifique sous couvert de classe

**Le faux pas** : Aquaman bloque *ce* client ou *ce* contrat sous
couvert du veto *« engagement-sans-périmètre »*. La formulation est
bonne, l'intention est politique.

**Le signal** : le veto revient systématiquement sur les mêmes
domaines (par exemple *« tous les clients de l'industrie X »*). Un
veto légitime devrait toucher *toute* prestation sans accord écrit,
pas un segment.

**Le remède** : vérifier les trois propriétés canoniques
(catégoriel, vérifiable, non-négociable). Si le veto n'opère que sur
un cas, il est *ad hoc*, pas catalogue. Le B2 Council peut passer
outre.

**Source** : `b2-eight-domain-vetoes-catalogue.md` §Anti-pièges.

## Anti-piège 3 — Périmètre implicite non documenté

**Le faux pas** : un mandat arrive avec un périmètre *« améliorer
le tunnel de conversion »* ou *« auditer la privacy de la feature
Y »*. Aquaman oppose le veto — à raison — mais sans pointer
l'élément manquant dans `B2_DC_DIRECTION_COUNCIL_DECISIONS.md`.

**Le signal** : le veto est émis, mais le porteur ne sait pas *quoi
amender* pour le lever. La conversation dure, le mandat traîne, le
sprint dérape.

**Le remède** : la propriété *vérifiable* du veto exige un motif
écrit. *« Cette prestation n'a pas d'accord écrit sur la propriété
du livrable, cf. ligne 12 du brief commercial »* est vérifiable.
*« Cette prestation n'est pas claire »* ne l'est pas.

**Source** : `b2-eight-domain-vetoes-catalogue.md` §Propriété 2.

## Anti-piège 4 — Aquaman qui opère au lieu de cadrer

**Le faux pas** : Aquaman commence à *produire* — signer des
contrats lui-même, faire les privacy reviews en personne, opérer
les consentements utilisateurs. C'est ce que `00_B2_DOMAIN_CONTROL_ROOM.md`
§B2 Must Not interdit explicitement.

**Le signal** : Aquaman passe plus de 50 % de son temps sur des
tâches B3 (exécution) et moins de 50 % sur des Rocks / DoD / JTBD.
Le squad Eternals n'a plus de travail propre.

**Le remède** : dispatcher le travail opérationnel vers le swarm
Eternals via JTBD packets. Aquaman redevient *cadreur* — il fixe le
cadre, le swarm opère dans le cadre.

**Source** : `00_B2_DOMAIN_CONTROL_ROOM.md` §B2 Must Not
*« Micromanage each B3 action »* et *« Turn B3 into a checklist
executor when a goal contract is enough »*.

## Anti-piège 5 — DoD Legal invérifiable

**Le faux pas** : Aquaman émet un DoD *« le contrat est
juridiquement solide »* ou *« la feature est privacy-safe »*. Aucun
agent tiers ne peut vérifier ces DoD depuis des artefacts.

**Le signal** : le swarm Eternals remonte des outputs marqués
*« done »* par Aquaman, mais personne d'autre ne peut confirmer le
DoD depuis un fichier.

**Le remède** : appliquer la DoD Quality Bar du pipeline
Rock→DoD→JTBD. Réécrire le DoD en termes d'*artefacts observables* :
*« Le template de contrat X est signé par 3 clients pilotes »*, *«
La privacy review de la feature Y couvre RGPD art. 13, 14, 30 »*.

**Source** : `01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md` §DoD Quality Bar.

## Anti-piège 6 — Aquaman signe sans matrice de signature People

**Le faux pas** : Aquaman signe un contrat parce que personne d'autre
n'a la matrice de signature posée. C'est un single point of failure
— Aquaman devient *le* signataire, pas *un* signataire autorisé.

**Le signal** : tous les contrats passent par Aquaman, qui doit
re-signer à chaque nouveau document. La vélocité baisse, le risque
augmente (un Aquaman surchargé fait des erreurs).

**Le remède** : escalader à Green Lantern (People) pour poser la
matrice de signature. Aquaman redevient un signataire parmi
d'autres, avec un seuil de montant ou de risque qui le concerne.

**Source** : triplet 23 — *« Green Lantern bloque tout recrutement
sans mandat écrit »* — la matrice de signature est un sous-produit
de People, pas de Legal.

## Synthèse — la grille de signal

| Anti-piège | Signal d'alerte | Remède |
|---|---|---|
| Dormant ≠ absent | Rock inventé, livrable non consommé | Rappel doctrine triplet 35-36 |
| Veto ad hoc | Veto récurrent sur mêmes segments | Vérifier 3 propriétés canoniques |
| Périmètre implicite | Porteur ne sait pas quoi amender | Motif écrit dans packet mésoperpétuel |
| Aquaman opérateur | Aquaman > 50 % sur tâches B3 | Dispatcher via JTBD vers Eternals |
| DoD invérifiable | Output marqué *« done »* non vérifiable | Réécrire avec artefacts observables |
| Aquaman seul signataire | Tous contrats via Aquaman | Escalader People pour matrice |

## Anti-pièges transverses (rappel)

- **Aquaman qui n'a pas de gate status pour la release active** : le
  projet reste `PRODUCT_ONLY_PROTOTYPE` (README §Operating Rule).
- **Aquaman qui oublie son veto en état dormant** : un pair-check
  Legal réveille le veto, pas le domaine.
- **Aquaman qui émet `LEGAL_READY` sans balayer les 7 surfaces** :
  c'est une fiction.

## Liens

- [[aquaman-domaine-legal-perimetre]] — l'état dormant
- [[aquaman-veto-engagement-sans-perimetre]] — les trois propriétés
  canoniques
- [[aquaman-squad-eternals-et-dormance]] — la discipline DoD du swarm
- [[aquaman-couplages-invisibles]] — les couplages qui forcent
  Aquaman à opérer
- [[aquaman-gates-et-pair-checks]] — les 3 gates et les
  pair-checks
- [[b2-eight-domain-vetoes-catalogue]] — les anti-pièges veto
  globaux

## Note de confiance

**Reconstruit.** Les 6 anti-pièges sont projetés à partir des
doctrines citées (triplet 35-36, veto catalogue anti-pièges, DoD
Quality Bar, B2 Must Not). Les signaux et remèdes sont **projetés** à
partir de la doctrine et n'ont pas été observés en cycle réel — pas
de paquet mésoperpétuel Legal enregistré dans le corpus visible (cf.
rapport). La grille est un *framework de vigilance*, pas une trace
d'incidents.
