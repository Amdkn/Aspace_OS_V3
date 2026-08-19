---
type: Concept
title: Batman — la doctrine remonte-fait, pas décision
description: Batman ne statue pas. Il porte les faits au B1 (Summers) avec leur motif. Deux triplets (56, 57) ancrent cette doctrine : tout fait Ops doit être posé comme un constat vérifiable, et le veto lui-même remonte comme un fait. Conséquence : la séparation Batman/Summers est la même que la séparation observateur/arbitre — Batman est le Captain qui observe, Summers est celui qui tranche.
tags: [doctrine, batman, ops, fait, decision, summers, b1, separation]
generated: { by: minimax-m3, at: 2026-08-19T03:40:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T03:40:00Z }
sources:
  - id: triplet-56
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 56 — Batman remonte à Summers des faits, pas des décisions"
    last_modified: 2026-08-17
  - id: triplet-57
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 57 — Batman veto remonte à Summers comme un fait, avec son motif"
    last_modified: 2026-08-17
  - id: vp-agent-md
    resource: "C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/coach-os/04_Business_Domains/02_Operations_en_Loops_Batman_Fantastic4/VP_AGENT.md"
    title: VP_AGENT Batman — source triplet 56/57
    last_modified: 2026-08-02
  - id: b2-council
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — Batman escalade à B1 dans 3 situations
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Batman — la doctrine remonte-fait, pas décision

## Les deux triplets qui ancrent la doctrine

**Triplet 56** (source `04_Business_Domains/02_Operations_en_Loops_Batman_Fantastic4/VP_AGENT.md`) :
> *« Batman remonte à Summers des faits, pas des décisions — l'arbitrage
> est à Summers. »*

**Triplet 57** (source `04_Business_Domains/02_Operations_en_Loops_Batman_Fantastic4/VP_SOUL.md`) :
> *« Le veto de Batman ne se négocie pas dans le sprint : il remonte
> à Summers comme un fait, avec son motif. »*

Deux phrases, deux conséquences :

- La première borne **ce que Batman produit** — des faits, pas des
  décisions.
- La seconde borne **ce que Batman bloque** — son veto est un fait
  posé à Summers, avec son motif.

## Pourquoi Batman et pas un autre capitaine

Les 8 capitaines B2 n'ont pas tous la même doctrine de remontée. La
différence est dans le **rapport au fait**. Batman est celui pour qui
*« le fait »* est la forme native de la parole — parce que l'Ops est
le domaine où **la boucle doit pouvoir être vérifiée** par quiconque
ouvre le runbook. Superman, à l'inverse, parle en *« promesse »*
(Growth, ce qu'on dira). Flash parle en *« valeur »* (Product, ce que
l'artefact apporte). Wonder Woman parle en *« retour »* (Finance, ce
que la dépense produit).

Batman, lui, parle en *« état »* : *« la procédure tourne »*, *« la
procédure ne tourne pas »*, *« la procédure tourne sans condition
d'arrêt »*. Son unité de parole est le **constat**, pas la
**promesse**, pas la **valeur**, pas le **retour**. C'est ce qui rend
le veto Batman légitime — un veto *catégoriel* (cf.
`b2-eight-domain-vetoes-catalogue.md`) est un fait observé sur une
classe de procédures, pas une opinion sur un cas.

## La séparation Batman/Summers

Batman est **l'observateur**. Summers est **l'arbitre**. La
séparation est la même que dans n'importe quel système à deux
niveaux : l'observateur ramène la mesure, l'arbitre tranche.

Conséquence concrète : Batman ne peut pas écrire une décision
d'arbitrage dans un packet mésoperpétuel. Il écrit le **fait**
(présence ou absence de la condition d'arrêt, état de la boucle,
charge de livraison tenable ou non) ; le packet mésoperpétuel, lui,
est écrit par le B2 Council — pas par Batman seul.

Trois situations où Batman **doit** escalader à Summers, pas
trancher :

1. **Conflit de North Star.** Une procédure Ops qui sert deux rocks
   incompatibles. Le Council ne peut pas choisir entre deux North
   Stars ; Batman remonte le constat et laisse Summers décider.
2. **Violation de cycle.** Une procédure dont la durée dépasse le
   12WY courant. Batman ne peut pas étendre le cycle ; seul Summers
   peut ouvrir un 12WY supplémentaire.
3. **Veto Batman opposé à un mandate B1.** Le triplet 57 le dit :
   Batman oppose son veto (fait) à Summers (B1) — pas à un autre
   capitaine. Summers peut amender le mandate ou réécrire la règle
   catalogue. Batman ne le fait pas lui-même.

## Le contraste avec les autres doctrines

- **Superman (Growth)** parle en promesse publique. Son veto
  s'applique aux promesses que la delivery ne tient pas. Superman
  **peut** bloquer un message sans escalader à Summers, parce que
  c'est un fait *« la delivery ne tient pas la promesse »* et la
  décision de modifier la promesse est ailleurs.
- **Flash (Product)** parle en valeur d'artefact. Son veto
  s'applique aux offres dont la valeur dépend d'une personne nommée.
  Flash peut bloquer une offre sans escalader — c'est un fait
  *« la valeur est nominative »*.
- **Wonder Woman (Finance)** parle en retour chiffré. Son veto
  s'applique aux dépenses récurrentes sans ROI. Wonder Woman peut
  bloquer une dépense sans escalader — c'est un fait *« la dépense
  n'a pas de métrique de retour »*.

Batman, lui, **escalade toujours** quand il oppose un veto (triplet
57). La différence est subtile mais porteuse : Superman, Flash,
Wonder Woman bloquent *« au nom du catalogue »* et la décision
d'arbitrer est dans le Council ; Batman **pose** *« au nom du
catalogue »* mais la décision d'arbitrer est chez Summers. Pourquoi ?

Réponse reconstruite à partir des triplets 56, 57 + fractal
d'escalade : parce que la **condition d'arrêt d'une procédure** est
une décision de cycle, pas une décision opérationnelle. Décider
qu'une procédure tourne ou s'arrête, c'est toucher au cycle — au
12WY, au rock de Summers. Batman n'a pas ce mandat. Il ramène le
fait, Summers tranche.

## Anti-pièges

- **Batman qui écrit *« je décide que… »*** dans un packet. Une
  décision Batman n'a pas de force d'arbitrage — le packet est
  invalide. C'est le B2 Council qui décide, ou Summers en
  escalation.
- **Veto Batman sans motif.** Le triplet 57 exige *« avec son
  motif »*. Un veto non documenté dans le packet mésoperpétuel est
  invalide, et le Council peut passer outre (propriété *vérifiable*
  du catalogue).
- **Batman qui statue sur un autre capitaine.** Si une procédure
  People (Green Lantern) ou Finance (Wonder Woman) n'a pas de
  condition d'arrêt, ce n'est pas un veto Batman — c'est un signal
  Batman à Green Lantern ou Wonder Woman. Le veto People est *«
  recrutement sans critère de sortie »* ; le veto Finance est *«
  dépense récurrente sans ROI »*. Batman ne porte pas les vetos des
  autres.
- **Batman qui se tait.** L'anti-piège symétrique : Batman qui voit
  une procédure sans condition d'arrêt et qui **ne remonte pas**. Le
  triplet 56 dit *« remonte à Summers »*, pas *« remonte parfois »*.
  C'est un devoir, pas une option.

## Liens

- [[domaine-batman-ops-perimetre-frontieres]] — le périmètre où s'applique la doctrine
- [[batman-veto-condition-arret-procedure]] — le veto qui remonte comme un fait
- [[b2-council-arbitrage-rule]] — les 3 escalades canoniques à B1
- [[b2-eight-domain-vetoes-catalogue]] — les 8 vetos et leurs 3 propriétés

## Note de confiance

**Confirmé par machine.** Les triplets 56 et 57 sont cités verbatim.
La séparation observateur/arbitre est **reconstruite** à partir du
fractal d'escalade (B2 Council arbitre l'opérationnel, B1 arbitre le
cycle) et de la doctrine canonique *« on ne saute jamais un échelon,
sauf emergency triggers explicites »*. Le contraste avec les
doctrines Superman/Flash/Wonder Woman est **mon inférence** à partir
des trois autres vetos catalogue. L'explication *« parce que la
condition d'arrêt d'une procédure est une décision de cycle »* est
**mon raisonnement** — pas une citation.