---
type: Concept
title: Aquaman veto — engagement-sans-périmètre, déclenchement et abus
description: Le veto catalogue d'Aquaman bloque toute prestation démarrée sans accord écrit sur le périmètre et la propriété du livrable. Le motif est double (périmètre + propriété), les trois propriétés canoniques s'appliquent (catégoriel, vérifiable, non-négociable au niveau mésoperpétuel). Les abus typiques : bloquer un cas spécifique sous couvert de la classe, ou lever le veto sans amendement visible du mandat.
tags: [b2, aquaman, veto, perimetre, propriete, livrable, catalogue]
generated: { by: minimax-m3, at: 2026-08-19T03:35:00Z }
verified:
  - { by: process:lecture-canon-aquaman, at: 2026-08-19T03:35:00Z }
sources:
  - id: triplet-30
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 30 — Aquaman hasVetoOver engagement-sans-perimetre"
    last_modified: 2026-08-17
  - id: orgex-json
    resource: "C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/coach-os/ORG.json"
    title: Coach OS ORG.json — veto catalogue
    last_modified: 2026-08-02
  - id: veto-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — un domaine, un blocage légitime
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Aquaman veto — engagement-sans-périmètre

## Le motif canonique

Triplet 30 (verbe `hasVetoOver`) : *« Aquaman bloque toute prestation
démarrée sans accord écrit sur le périmètre et la propriété du
livrable. »*

Le motif est **double** :

- **Périmètre** — le scope d'exécution est-il écrit ? Sans accord sur
  ce qui est *inclus* et ce qui est *exclu*, une prestation peut
  dériver sans qu'aucun signal ne le détecte.
- **Propriété du livrable** — à qui appartient la sortie ? Sans accord
  sur la titularité (client, fournisseur, co-création, licence), un
  litige en cours de route peut bloquer la livraison elle-même.

Les deux sont **cumulatifs** : un périmètre écrit sans accord de
propriété ne lève pas le veto, et inversement.

## Quand le veto se déclenche (cas concrets)

Quatre cas où le veto s'oppose de manière légitime, observés dans le
corpus B2 et la doctrine OMK :

1. **Contrat commercial non signé.** Une proposition orale ou un accord
   verbal de scope avec un client — Aquaman oppose le veto avant que
   Ops ne commence la livraison.
2. **Sprint B3 sans JTBD Rock-source.** Le `02_B3_SWARM_SUPERVISION_PROTOCOL.md`
   pose le DoD comme obligatoire dans le packet. Sans DoD écrit, le
   périmètre d'exécution est flou — Aquaman oppose le veto au démarrage.
3. **Claim publique avant terms.** Toute prise de parole publique qui
   engage l'organisation avant qu'un terms-of-use ne couvre le scope —
   Aquaman oppose le veto, en pair-check #7 avec Superman (Growth).
4. **Feature produit sans privacy review.** Code mergée qui touche de
   la donnée personnelle sans review privacy — Aquaman oppose le veto,
   en pair-check #8 avec Flash (Product).

## Quand le veto serait abusif

Cinq cas où invoquer le veto serait un détournement de la classe
catalogue (cf. [[b2-eight-domain-vetoes-catalogue]] §Anti-pièges) :

1. **Cas spécifique sous couvert de classe.** Bloquer *ce* recrutement
   sous couvert du veto recrutement, bloquer *ce* client sous couvert du
   veto engagement — c'est un blocage ad hoc, pas un veto catalogue.
2. **Périmètre implicite mais vérifiable.** Un périmètre *« améliorer
   le tunnel de conversion »* peut être implicite sans être flou : un
   Aquaman qui oppose le veto sans pointer l'élément manquant dans
   `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` casse la propriété
   *vérifiable*.
3. **Veto levé sans amendement.** Un veto qui ne sert à rien s'il est
   levé sans que le mandat soit amendé. Le packet mésoperpétuel doit
   documenter l'amendement.
4. **Veto opposé sur du non-Legal.** Cyborg (IT) demande une revue de
   chemin de sortie cloud — c'est son veto, pas celui d'Aquaman. Un
   Aquaman qui bloque au-delà de son périmètre est overreach.
5. **Veto rétroactif.** Un Aquaman qui découvre a posteriori qu'un de
   ses vetos aurait dû bloquer un mandat déjà exécuté escalade pour
   relecture — pas un veto rétroactif.

## Les trois propriétés canoniques (cf. veto catalogue)

Le veto Aquaman est légitime ssi les trois propriétés suivantes sont
remplies :

### 1. Catégoriel

Le veto porte sur une **classe** (les prestations sans accord écrit
périmètre + propriété), pas sur un cas. Aquaman ne peut pas bloquer
*ce* client sous couvert de la classe — il peut bloquer *toute*
prestation sans accord écrit.

### 2. Vérifiable

Le motif doit être **écrit** dans le packet mésoperpétuel ou dans le
journal Council. *« Je bloque cette prestation »* n'est pas vérifiable.
*« Cette prestation n'a pas d'accord écrit sur la propriété du
livrable, cf. ligne 12 du brief commercial »* est vérifiable.

### 3. Non-négociable *au niveau mésoperpétuel*

Un capitaine B2 ne peut pas passer outre le veto d'un autre capitaine
B2. Superman (Growth) ne peut pas dire *« OK on lance quand même,
c'est une exception »*. La seule option est d'escalader B1 pour
amender la règle catalogue — et B1 ne réécrit pas les vetos à la
légère.

## La règle de résolution

Quatre issues possibles, par ordre de fréquence
(cf. `b2-eight-domain-vetoes-catalogue.md` §Règle de résolution) :

1. **Le mandat est amendé** avant le dispatch B3. Le porteur écrit
   l'accord périmètre + propriété. **Résultat : arbitrage accepté,
   mode inchangé.**
2. **Le mandat est retiré** par B1 ou par le porteur. Le veto tient,
   le mandat est mort. **Résultat : packet mésoperpétuel avec
   `decision: blocked`, motif = veto engagement-sans-périmètre.**
3. **Le veto est escaladé à B1** pour réécriture de la règle
   catalogue. **Résultat : `decision: escalate_to_B1`.** Très rare.
4. **Le veto est invalide** (manque une des trois propriétés). Le
   Council passe outre. **Résultat : packet mésoperpétuel avec note
   d'invalidation.**

## Anti-pièges spécifiques Aquaman

- **Veto sur périmètre partiel.** Un périmètre *« 80 % écrit, 20 %
  implicite »* oppose le veto, mais le porteur amendera les 20 %. Le
  veto est légitime, pas abusif — la différence tient à la
  vérifiabilité du motif dans le packet.
- **Confondre périmètre et scope.** Le scope est *technique* (ce que
  la prestation va toucher). Le périmètre est *contractuel* (ce qui
  est promis). Le veto porte sur le périmètre, pas sur le scope — mais
  les deux se recouvrent largement dans la pratique.
- **Veto dormant oublié.** Un Aquaman en état dormant (cf.
  [[aquaman-domaine-legal-perimetre]]) n'oublie pas son veto pour
  autant. Le veto catalogue reste valide ; seul le *flow de
  production* est gelé. Un pair-check qui touche Legal réveille le
  veto, pas le domaine.

## Liens

- [[b2-eight-domain-vetoes-catalogue]] — la doctrine veto applicable
- [[aquaman-domaine-legal-perimetre]] — le périmètre du domaine qui
  légitime le veto
- [[aquaman-gates-et-pair-checks]] — les gates émis par Aquaman
- [[b2-pair-check-raci-by-rank]] — les pair-checks où Aquaman oppose
  le veto en position Consulted
- [[b2-meso-decision-packet-spec]] — le format packet où le motif est écrit

## Note de confiance

**Confirmé par machine.** Motif verbatim triplet 30 et `ORG.json`.
Trois propriétés canoniques tirées verbatim de
`b2-eight-domain-vetoes-catalogue.md`. Les 4 cas de déclenchement et
les 5 cas d'abus sont **projetés** depuis la matrice d'harmonisation
et le triplet v3 — non observés en cycle réel dans le corpus
disponible (cf. rapport — pas de paquet mésoperpétuel Legal
enregistré).
