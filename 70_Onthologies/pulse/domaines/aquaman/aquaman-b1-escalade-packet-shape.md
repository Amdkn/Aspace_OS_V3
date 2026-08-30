---
type: Concept
title: Aquaman — forme packet quand Aquaman escalade B1
description: Quand Aquaman oppose son veto à un mandate B1 lui-même (cas 3 de [[b2-council-arbitrage-rule]] §Quand le Council escalade à B1), il ne peut pas amender le mandate — il doit l'escalader. Le packet Aquaman→B1 a une forme distincte du packet mésoperpétuel B2→B3. Trois cas déclencheurs, six champs obligatoires, procédure de cosignature Aquaman + Council, conservation dans le journal Council en append-only D4. Le concept donne le gabarit YAML et les 5 erreurs typiques.
tags: [b2, aquaman, b1, escalade, packet, veto, mandate, north-star, d4]
generated: { by: minimax-m3, at: 2026-08-19T06:05:00Z }
verified:
  - { by: process:lecture-canon-aquaman-tour-4, at: 2026-08-19T06:05:00Z }
sources:
  - id: b2-council-arbitrage
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: "B2 Council arbitrage rule §Quand le Council escalade à B1 — 3 situations concrètes"
    last_modified: 2026-08-19
  - id: b2-meso-packet
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — le format canonique d'une décision B2
    last_modified: 2026-08-19
  - id: aquaman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-veto-engagement-sans-perimetre.md"
    title: Aquaman veto canonique — engagement-sans-périmètre
    last_modified: 2026-08-19
  - id: aquaman-pair-check-10
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-pair-check-10-legal-risk-launch.md"
    title: Aquaman pair-check #10 — quand le risque Legal est l'enjeu principal
    last_modified: 2026-08-19
  - id: b1-stop-conditions
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-stop-conditions-escalier.md"
    title: B1 stop conditions — escalier canonique 5 échelons
    last_modified: 2026-08-19
  - id: b2-council-cadence
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-cadence-and-chair.md"
    title: "B2 Council cadence and chair §Le journal Council — append-only D4"
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Aquaman — forme packet quand Aquaman escalade B1

## Pourquoi un packet spécifique Aquaman→B1

Le [[b2-council-arbitrage-rule]] §« Quand le Council escalade à B1 »
distingue **trois situations** où le B2 Council ne peut pas trancher et
**doit** escalader B1 :

1. **Conflit de North Star** — deux mandates B1 simultanés exigent des
   wheel-states incompatibles.
2. **Violation de cycle** — un arbitrage exige de dépasser le 12WY
   courant.
3. **Boundary non-négociable tierce** — un veto catalogue s'oppose à un
   mandate B1 lui-même.

Aquaman est **le seul des 8 capitaines dont le veto catalogue peut
déclencher le cas 3** dans sa forme canonique — *« prestation démarrée
sans accord écrit sur le périmètre et la propriété du livrable »*
(cf. [[aquaman-veto]]). Le veto oppose un **manque** (pas de périmètre)
à une **décision** (manifester le livrable). Le cas 3 escalade B1 quand
le demandeur du mandate **est B1 lui-même** (par exemple un Summers
qui mandate une livraison sans passer par Aquaman).

Le packet mésoperpétuel standard ([[b2-meso-packet]]) ne suffit pas : il
documente une décision B2 interne ; ici, Aquaman **remonte** à B1. Il faut
une **forme distincte** qui signale explicitement *« ce packet est un
escalade B1, pas une décision B2 »*.

## Les 3 cas où Aquaman escalade B1

### Cas E1 — Veto opposé à un mandate B1 directement

Le cas canonique. B1 mandate une prestation (par exemple *« lance le
produit sur le marché EU sans relecture Aquaman »*). Aquaman émet son
veto (périmètre écrit exigé). B1 mandate **n'a pas** de périmètre écrit
parce que la doctrine Aquaman est contournée. Aquaman ne peut pas amender
le mandate B1 — il escalate.

**Source** : [[b2-council-arbitrage]] §3 (verbatim).

### Cas E2 — Cycle 12WY ne permet pas la validation Aquaman

B1 mandate un launch à T-30j ; Aquaman évalue que le délai de validation
Légal est incompatible (par exemple regulator inquiry en cours bloque
un go-to-market propre). Cas 2 du Council — *« violation de cycle »*.

**Source** : [[b2-council-arbitrage]] §2 (verbatim).

### Cas E3 — Conflit de North Star Legal

Cas 1 du Council — deux mandates B1 simultanés incompatibles sur le
Legal (par exemple *« pivoter US premium »* ET *« ne pas signer de clause
de limitation US »*). Aquaman ne tranche pas le pivot commercial, mais
le **risque Legal** est l'enjeu identifié. Cas 1 escalade B1.

**Source** : [[b2-council-arbitrage]] §1 (verbatim).

**Note** : le cas 3 (conflit North Star) est **rare** pour Aquaman. Plus
souvent, le conflit est porté par Sales (JohnJones) ou Growth (Superman).
Mais Aquaman peut l'identifier quand le risque Legal est *l'*enjeu
principal, par exemple via le pair-check #10 (cf.
[[aquaman-pair-check-10]]).

## Le gabarit YAML Aquaman→B1

```yaml
escalation_id: B2-B1-ESCALATION-YYYY-NN
source_mandate: B1-B2-MANDATE-YYYY-NN  # ou B1 direct
escalating_captain: aquaman (Legal)
escalation_class: E1 | E2 | E3
veto_class: legal-engagement-sans-perimetre | legal-amplification-1 | legal-amplification-2
tradeoff: short statement (1-3 phrases)
downstream_impact:
  - impacted_domain
  - impacted_domain
amendement_proposed:
  short_text: <nouvelle clause ou pivot>
  rationale: <pourquoi ça résout>
cosignature_required:
  - aquaman (Legal, captain escalateur)
  - 5 autres capitaines B2 (quorum Council standard — cf. [[b2-council-cadence]])
packet_d4_archived: line in B2_DC_DIRECTION_COUNCIL_DECISIONS.md
```

### Les 6 champs obligatoires

Chaque champ est obligatoire. Un packet Aquaman→B1 sans champ obligatoire
est invalide (par symétrie avec le packet mésoperpétuel standard — cf.
[[b2-meso-packet]] §Chaque champ est obligatoire).

1. **`escalation_id`** — `B2-B1-ESCALATION-YYYY-NN`. Compteur annuel,
   reset par 12WY, jamais réutilisé. Permet de citer l'escalade dans
   d'autres packets.
2. **`source_mandate`** — le mandate B1 qui est escaladé. Si la source
   n'est pas un mandate B1 (par exemple Aquaman initie l'escalade sur
   un veto auto-déclenché), la valeur est `B2-PEER-YYYY-NN` par
   symétrie avec [[b2-meso-packet]].
3. **`escalation_class`** — l'un des 3 cas E1, E2, E3. Une 4ᵉ valeur
   (`E4-other`) est invalide.
4. **`veto_class`** — référence explicite à la classe de veto invoquée
   (catalogue) ou au mécanisme d'amplification ([[b2-veto-amplification-cycle]]).
   Sans classe citée, l'escalade est non-vérifiable.
5. **`amendement_proposed`** — la contre-proposition Aquaman. Une
   escalade sans amendement est une escalade **non-opérationnelle** —
   B1 ne peut pas trancher sans savoir quoi faire à la place.
6. **`cosignature_required`** — Aquaman + quorum Council. Sans
   cosignature Council, l'escalade n'a pas de **légitimité collective**
   — c'est Aquaman seul qui escalade, ce qui est overreach.

## La procédure de cosignature

L'escalade Aquaman→B1 **n'est pas un acte unilatéral Aquaman**. Elle passe
par le B2 Council en séance hebdomadaire (cf. [[b2-council-cadence]] §1.
Séance hebdomadaire) ou en séance ad hoc (cf. §2. Séance ad hoc). La
procédure :

1. **Aquaman initie** le packet (5 des 6 champs remplis).
2. **Séance B2 Council** — Aquaman présente le packet, motive l'escalade,
   propose l'amendement.
3. **Vote Council** — quorum 5/8. Adoption = cosignatureCollective.
   Refus = Aquaman ne peut pas escalader seul (sauf veto catalogue
   auto-déclenché, cf. Anti-pièges §Sauter le Council).
4. **Archivage D4** — ligne dans `B2_DC_DIRECTION_COUNCIL_DECISIONS.md`
   (append-only, cf. [[b2-council-cadence]] §Le journal Council).
5. **Transmission B1** — packet Aquaman + cosignature Council transmis
   à B1 par le canal Council → B1 (cf. [[b1-stop-conditions]] §L'escalier
   canonique 5 échelons).
6. **Décision B1** — B1 statue : accept amendement / refuse / heal
   (réécriture North Star).

## Les 5 erreurs typiques

### Erreur 1 — Escalade sans amendement proposé

Aquaman refuse le mandate B1 mais ne propose pas de **solution de
rechange**. B1 ne peut pas trancher — résultat : B1 mandate reste
bloqué, le travail stagne.

**Mitigation** : le champ `amendement_proposed` est obligatoire. Un
packet sans amendement est invalide.

### Erreur 2 — Cosignature Council rampante

Aquaman demande à un seul autre capitaine de cosigner (par exemple
Wonder Woman pour des raisons de coût) avant la séance. Le packet
arrive en Council avec une cosignature **politique** qui biaise le
vote.

**Mitigation** : cosignature uniquement **après** la séance Council,
par adoption formelle du quorum.

### Erreur 3 — Sauter le Council

Aquaman escalate directement B1 sans passer par le Council. Le
packet est unilatéral — il a la légitimité du veto catalogue mais
pas la légitimité **collective** d'une escalade de routine.

**Mitigation** : un veto catalogue auto-déclenché peut escalader
sans Council *si* la violation est **flagrante** (par exemple B1
ordonne *« livre les données clients sans DPA »*). Mais un cas
**litigieux** (par exemple une clause discutable) doit passer par
le Council.

### Erreur 4 — Archiver la mauvaise classe

Un packet dont `escalation_class` est `E1` mais dont le contenu
relève de `E2` (cycle). L'archivage D4 crée une trace
**incorrecte** que le journal Council ne peut pas corriger.

**Mitigation** : `escalation_class` revu par le president de séance
Council (cf. [[b2-council-cadence]] §La présidence tournante) avant
archivage D4.

### Erreur 5 — Escalader sans vérifier Aquaman ACTIVE

Un Aquaman SHADOW_ACTIVE (cf. [[aquaman-dormant-activation]]) qui
escalade B1 engage sa responsabilité sur la doctrine Legal. Un
escalade B1 depuis un état non-ACTIVE est *inadmissible* côté
Aquaman.

**Mitigation** : la passe d'escalade commence par la vérification
de l'état Aquaman. Si Aquaman n'est pas ACTIVE, l'escalade est
**différée** jusqu'à activation (sauf cas E3 conflit North Star,
où l'escalade prime sur l'activation).

## Anti-pièges

- **Confondre packet mésoperpétuel et packet Aquaman→B1.** Les deux ont
  des champs différents. Le mésoperpétuel a `decision: accepted | blocked
  | escalate_to_B1` (cf. [[b2-meso-packet]] §`decision`). L'escalade B1
  **est** la valeur `escalate_to_B1` du mésoperpétuel — mais le packet
  *Aquaman→B1* est ce qui voyage vers B1 après la décision mésoperpétuel
  `escalate_to_B1`. Ce sont deux objets distincts.
- **Aquaman qui devient bloquant de routine.** Si Aquaman escalade B1
  tous les 12WY, c'est un signal de **dérive** (cf. doctrine veto
  politique — [[b2-eight-domain-vetoes-catalogue]] §Anti-pièges). Le
  compteur annuel `B2-B1-ESCALATION-YYYY-NN` permet de suivre la
  cadence.
- **B1 qui accepte tout amendement Aquaman.** B1 peut **refuser**
  l'amendement proposé, ou **réécrire** le North Star. Aquaman n'a pas
  le dernier mot — le dernier mot est B1 (cf. [[b1-stop-conditions]]
  §L'escalier canonique).
- **Cycle 12WY comme excuse.** Un Cas E2 (cycle 12WY) ne doit pas
  devenir une excuse pour rejeter un launch rapide. Le cas E2
  exige une **preuve** que le cycle ne peut pas être tenu — pas un
  argument générique.
- **Escalade B1 qui réécrit le veto catalogue.** Une escalade E1 peut
  conduire B1 à réécrire le veto catalogue Aquaman. C'est légitime
  — mais c'est une **réécriture**, pas une amplification. La
  réécriture exige unanimité 8/8 + B1 (cf. [[b2-veto-amplification-cycle]]
  §L'amplification n'est pas la réécriture).

## Liens

- [[b2-council-arbitrage-rule]] §Quand le Council escalade à B1 — les 3
  situations canoniques
- [[b2-meso-decision-packet-spec]] — le packet mésoperpétuel qui contient
  la valeur `escalate_to_B1` menant au présent packet
- [[b2-veto-amplification-cycle]] — la distinction amplification vs
  réécriture qui borne le E1
- [[aquaman-veto-engagement-sans-perimetre]] — le veto canonique
  Aquaman qui déclenche E1
- [[aquaman-pair-check-10-legal-risk-launch]] — le #10 qui peut déclencher
  E3 (conflit North Star Legal)
- [[aquaman-dormant-activation]] — la condition ACTIVE pour E1
- [[b1-stop-conditions-escalier]] §L'escalier canonique — la position B1
  comme arbitre final
- [[b2-council-cadence-and-chair]] §Le journal Council — l'archivage D4
  du packet escaladé
- [[b2-eight-domain-vetoes-catalogue]] §Anti-pièges veto politique — la
  surveillance de la cadence d'escalade Aquaman

## Note de confiance

**Reconstruit, projeté depuis 3 sources canoniques.** Les 3 cas
déclencheurs (E1, E2, E3) sont **tirés verbatim** de [[b2-council-arbitrage]]
§3 situations concrètes. Le gabarit YAML est **projeté** par généralisation
du packet mésoperpétuel ([[b2-meso-packet]]) vers le cas d'escalade B1 —
c'est une **projection** depuis un format posé, pas une doctrine citée.
Les 6 champs obligatoires sont **empirés** du packet mésoperpétuel +
des champs spécifiques à l'escalade (veto_class, amendement_proposed).
La procédure de cosignature en 6 étapes est **reconstruite** par
application de [[b2-council-cadence]] §Séance hebdomadaire. Les 5
erreurs typiques sont **extrapolées** depuis les anti-pièges veto
politique ([[b2-eight-domain-vetoes-catalogue]]) et la doctrine
D4 append-only. **À vérifier en cycle** : (1) le champ
`amendement_proposed` est-il exigé par B1, ou B1 peut-il statuer
sur la base du tradeoff seul ?, (2) la cosignature Council
interfère-t-elle avec la présidence tournante (un capitaine qui
préside cosigne-t-il son propre packet ?), (3) B1 peut-il
réécrire le veto catalogue Aquaman via une escalade — c'est une
réécriture, mais est-elle unilatérale B1 ou exige-t-elle le
passage par Council ?
