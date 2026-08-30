---
type: Concept
title: Profil gardien vs producteur — Wonder Woman et Aquaman gardiens, les 6 autres producteurs
description: La matrice RACI par rang révèle une asymétrie structurelle : Wonder Woman (Finance) et Aquaman (Legal) n'ont aucun A sur les 9 pair-checks canoniques — ils sont C uniquement. Les 6 autres capitaines ont au moins un A. La doctrine sous-jacente est « gardien vs producteur » : les gardiens arbitrent la cohérence (vérité et conformité), les producteurs tranchent les transitions cross-domaines. Le profil de gardien se reconnaît à trois traits : veto catalogue, droit de blocage hard, escalade B1 directe.
tags: [b2, profil, gardien, producteur, wonder-woman, aquaman, raci, veto, blocking-authority, escalade-b1]
generated: { by: minimax-m3, at: 2026-08-19T04:35:00Z }
verified:
  - { by: process:lecture-domaine-finance-corpus, at: 2026-08-19T04:35:00Z }
sources:
  - id: raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks
    last_modified: 2026-08-19
  - id: vetos-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2
    last_modified: 2026-08-19
  - id: omk-control-room
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: OMK Finance — B2 Domain Control Room
    last_modified: 2026-05-25
  - id: aquaman-control-room
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: OMK Legal — B2 Domain Control Room
    last_modified: 2026-05-27
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel
    last_modified: 2026-08-17
  - id: areas-dormants-doctrine
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-areas-dormants-doctrine.md"
    title: B2 Areas-dormants — la doctrine Aquaman
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Profil gardien vs producteur — Wonder Woman et Aquaman gardiens, les 6 autres producteurs

## L'asymétrie révélée par le RACI par rang

Le tableau du RACI par rang
(`b2-pair-check-raci-by-rank.md` §) « « Le tableau par rang ») pose :

| Capitaine | Pair-checks où A | Pair-checks où C | Profil déduit |
|---|---|---|---|
| Superman (Growth) | 1, 5, 7 | — | Producteur |
| JohnJones (Sales) | 1 | — | Producteur |
| Flash (Product) | 3, 4, 6, 8 | — | Producteur |
| Batman (Ops) | 2, 3 | — | Producteur |
| Cyborg (IT) | 4 | — | Producteur |
| Green Lantern (People) | — (transverse) | 9 | Producteur transverse |
| **Wonder Woman (Finance)** | — | **5, 6** | **Gardien** |
| **Aquaman (Legal)** | — | **7, 8** | **Gardien** |

**Wonder Woman et Aquaman sont les deux capitaines sans aucun A
sur les 9 pair-checks canoniques**. Tous les autres ont au moins
un A — la plupart en ont plusieurs.

Le rapport tour 1
(`wonder-woman-pair-check-consulted-role.md` § « L'asymétrie cachée »)
avait noté cette singularité. Elle prend ici un statut doctrinal :
**Wonder Woman et Aquaman sont des gardiens, pas des producteurs**.

## Les trois traits du gardien

Un capitaine B2 est **gardien** ssi les trois propriétés suivantes
sont remplies. Wonder Woman et Aquaman sont les deux à les remplir.

### 1. Pas de A sur les 9 pair-checks canoniques

La règle canonique du RACI par rang est `A = B2 en aval de la
transition` (`b2-pair-check-raci-by-rank.md` § « Pourquoi A = B2
en aval, pas B1 »). Un gardien **n'est jamais en aval** — il est
toujours en amont (lecture) ou en parallèle (veto transversal).
Wonder Woman est en amont sur #5 (Finance→Growth) et #6
(Finance→Product) ; Aquaman est en amont sur #7 (Legal→Growth) et
#8 (Legal→Product).

**Conséquence opérationnelle** : un gardien n'a pas le dernier
mot sur une transition. Il a le premier mot sur la forme.

### 2. Veto catalogue propre

Chaque gardien tient son veto catalogue :

- **Wonder Woman** : « Bloque toute dépense récurrente sans date
  de revue et sans métrique de retour » (`triplets/v3-business.jsonl`
  ligne 28, `b2-eight-domain-vetoes-catalogue.md` § « Les 8
  vetos »).
- **Aquaman** : « Bloque toute prestation démarrée sans accord
  écrit sur le périmètre et la propriété du livrable »
  (`triplets/v3-business.jsonl` ligne 30, `b2-eight-domain-vetoes-catalogue.md`).

Le veto catalogue est **unaire** : il ne nécessite pas de Council,
le capitaine bloque seul. C'est l'inverse d'un arbitrage — un
gardien peut arrêter un flux sans réunir le Council.

### 3. Droit de blocage hard ou veto de porte

Wonder Woman a le **blocking authority** sur la marge négative
(`00_B2_DOMAIN_CONTROL_ROOM.md` § « Blocking Authority » : « Blocks
Product when it creates hidden recurring cost, unclear pricing,
or margin-negative delivery »). Aquaman a un droit analogue sur la
conformité : un deal signé sans CGV ne peut pas être facturé.

Le gardien peut **bloquer la sortie d'un produit** (Wonder Woman)
ou **bloquer l'entrée d'une prestation** (Aquaman) indépendamment
du RACI pair-check.

## Les trois traits du producteur

Les 6 autres capitaines (Superman, Flash, Batman, JohnJones, Cyborg,
Green Lantern) sont des producteurs. Le producteur a les trois
traits inverses du gardien.

### 1. Au moins un A sur les pair-checks canoniques

Producteurs ont A sur la transition où leur aval est le récepteur
final. Superman A sur Growth × Sales (pair-check #1), Flash A sur
Product × Ops (#3), Batman A sur Sales × Ops (#2) et Product × Ops
(#3), Cyborg A sur Product × IT (#4), JohnJones A sur Growth × Sales
(#1), Green Lantern transversal C sur #9.

### 2. Pas de veto catalogue propre (sauf Batman — nuance)

Le catalogue des 8 vetos attribue **un veto par capitaine**. Mais
Batman a un veto qui ressemble plus à un gardien
(« procédure-sans-condition-arret », triplet 25). La nuance :
Batman est un **producteur avec un veto de garde-fou**. Le veto
de Batman teste la **forme** (la procédure a-t-elle une condition
d'arrêt ?), pas le **fond** (la procédure est-elle correcte ?).
Wonder Woman et Aquaman testent aussi la forme (date + métrique ;
accord écrit). **La différence** : Batman tranche l'**arrêt** des
procédures, pas leur **validité financière ou légale**.

Green Lantern (People) a un veto sur le recrutement — c'est
encore différent : c'est un veto sur l'**entrée** d'un nouvel
agent/humain, pas sur la sortie d'un produit. Green Lantern
est un **producteur transverse** avec un veto d'**admission**,
pas de blocage.

### 3. Droit de trancher l'opérationnel, pas la cohérence

Le producteur tranche les pair-checks, mais ne tient pas la
**vérité comptable** ou la **conformité légale**. Superman tranche
la **continuation paid media** (pair-check #5) sur la base du CAC
payback livré par Wonder Woman — mais Superman ne tient pas le
chiffre lui-même. C'est Wonder Woman qui arbitre la cohérence du
chiffre (réconciliation, marge réelle, runway réel).

## Pourquoi le profil gardien n'est pas un défaut de RACI

Le RACI pourrait être lu comme « Wonder Woman est faible, Aquaman
est faible ». C'est **faux** pour trois raisons structurelles :

### a. Le gardien a plus de pouvoir en régime de stress

Le RACI pair-check teste le **régime normal** — quand Growth
scale et Product ship, Superman et Flash tranchent les transitions.
Mais en **régime de stress** (runway <6 mois, marge négative,
contrat sans CGV), c'est le gardien qui décide. Wonder Woman
peut bloquer un produit sans escalader le Council
(`00_B2_DOMAIN_CONTROL_ROOM.md` § « Blocking Authority »).
Aquaman peut bloquer une prestation sans signer de Council.

Le gardien est **faible en régime normal, fort en régime de
stress**. C'est le profil d'un filet de sécurité.

### b. Le gardien tient la cohérence, pas la croissance

Wonder Woman arbitre la **vérité comptable** (F7 « Transparent
reporting »). Superman arbitre la **croissance** (F3 « MRR growth
discipline »). Aquaman arbitre la **conformité** (veto §08).
Batman arbitre la **maintenabilité** (veto §04).

Les gardiens **gardent** ce que les producteurs **produisent**.
Sans gardien, le producteur peut produire n'importe quoi sans
que la cohérence des chiffres ou des clauses ne s'oppose.

### c. Le gardien a un canal d'escalade distinct

Wonder Woman peut escalader B1 directement sans passer par le
B2 Council quand le runway <6 mois (KR-5g). Aquaman peut
escalader B1 quand un contrat manque de périmètre écrit
(veto §08).

Les deux gardiens ont un **canal d'escalade court** — un échelon
entre eux et B1, pas les 2-3 échelons des producteurs (qui
passent par le B2 Council d'abord).

## L'asymétrie cachée — les gardiens sont aussi en dormance possible

`b2-areas-dormants-doctrine.md` pose Aquaman comme exemple canonique
de dormance (« ne produit rien tant que le premier contrat n'est
pas signé »). Wonder Woman n'est **pas** dormant — son cycle F1-F25
a des outils actifs en continu. **Mais les deux gardiens
peuvent être en dormance** quand :

- Aucune ressource externe ne requiert leur doctrine (Aquaman
  sans contrat, Wonder Woman sans dépense récurrente détectée).
- Leur DoD est vide pour le cycle courant.
- Le captain a consigné l'état dans le journal Council.

Les **producteurs** ne sont casi jamais en dormance — Superman
tient toujours l'attention, Flash tient toujours l'artefact,
Batman tient toujours la maintenabilité. Les gardiens peuvent
se taire légitimement quand leur filet n'a rien à attraper.

## L'asymétrie des domaines dormants

| Capitaine | Profil | Dormance possible ? |
|---|---|---|
| Aquaman | Gardien | Oui — exemple canonique |
| Wonder Woman | Gardien | Oui — peu probable (F1 runway toujours actif) |
| Superman | Producteur | Non (sauf attente B1 = absence, pas dormance) |
| Flash | Producteur | Non |
| Batman | Producteur | Non |
| JohnJones | Producteur | Non |
| Cyborg | Producteur | Non |
| Green Lantern | Producteur transverse | Non (sauf attente B1) |

**Conclusion asymétrique** : les gardiens **peuvent** se taire,
les producteurs **doivent** produire. C'est la conséquence directe
de la doctrine : un gardien qui parle trop casse son rôle (veto
politique, défense de territoire) ; un producteur qui se tait
casse sa mission.

## Anti-pièges du profil gardien

- **Lire « pas de A » comme « pas d'autorité ».** Wonder Woman
  peut bloquer un produit sans escalation. Aquaman peut bloquer
  un deal sans escalation. Le A du RACI est l'autorité **de
  trancher les transitions** ; les gardiens ont d'autres formes
  d'autorité (veto, blocking, escalade directe).
- **Confondre gardien et consultant.** Un consultant observe et
  recommande. Un gardien **bloque**. Wonder Woman qui se contente
  de signaler une marge négative sans bloquer le produit **n'est
  pas un gardien** — elle est un consultant qui trahit son rôle.
- **Élargir le profil gardien aux transversaux.** Green Lantern
  est transverse C sur #9 (People → Tous), mais il n'a pas le
  profil gardien — il n'a pas de veto de porte, pas de droit de
  blocage hard. C'est un **producteur transverse** avec un veto
  d'admission (recrutement). La distinction est subtile mais
  compte.
- **Croire que tous les domaines à C sont des gardiens.** Aucun
  autre capitaine n'a la combinaison (C sur tous les pair-checks
  le concernant + veto catalogue + droit de blocage hard + canal
  d'escalade directe). Wonder Woman et Aquaman sont **les deux
  seuls**.

## Liens

- [[wonder-woman-finance-frontiers]] — le périmètre Finance
- [[wonder-woman-pair-check-consulted-role]] — le statut C approfondi
- [[wonder-woman-recurrent-spend-veto]] — le veto catalogue Finance
- [[b2-pair-check-raci-by-rank]] — la matrice RACI source
- [[b2-eight-domain-vetoes-catalogue]] — la théorie des 8 vetos
- [[b2-areas-dormants-doctrine]] — la doctrine de dormance Aquaman

## Note de confiance

**Confirmé par machine** sur l'asymétrie RACI (Wonder Woman = 0 A,
Aquaman = 0 A, Superman = 3 A, Flash = 4 A — cités verbatim).
**Reconstruit** sur le profil gardien vs producteur : la
distinction n'est **pas posée comme telle** dans le corpus. La
projection « gardien » est une inférence depuis la combinaison
(C sur tous + veto catalogue + blocking authority + escalade B1
directe). **Inféré** également : Batman est un producteur avec
un veto de garde-fou (pas un gardien) parce que son veto teste
la forme procédurale, pas la cohérence substantielle. Green
Lantern est producteur transverse avec veto d'admission, pas
gardien.