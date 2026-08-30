---
type: Concept
title: Wonder Woman présidence tournante Council — quand, comment, limites
description: Le Council B2 a une présidence tournante par impacted captain (b2-council-cadence-and-chair §« La présidence tournante »). Wonder Woman préside dans 3 contextes canoniques : arbitrage où Finance est en aval (ex: red flag #4 Growth→Finance), arbitrage où Finance est impliquée avec un autre capitaine en aval, séance bilan si Wonder Woman a le plus de décisions mésoperpétuelles ouvertes dans le cycle. Doctrine des 3 prérogatives (ordre du jour, minutage 60min, signature packet) + 3 limites strictes (conflit d'intérêt, partialité, escalade B1).
tags: [wonder-woman, finance, council, presidence, tournante, cadence, quorum, conflit-interet]
generated: { by: minimax-m3, at: 2026-08-19T06:35:00Z }
verified:
  - { by: process:lecture-corpus-tour-5, at: 2026-08-19T06:35:00Z }
sources:
  - id: council-cadence
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-cadence-and-chair.md"
    title: B2 Council — cadence, présidence tournante, et mécanique de séance
    last_modified: 2026-08-19
  - id: council-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
  - id: meso-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — format canonique
    last_modified: 2026-08-19
  - id: red-flag-4
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-red-flag-4-trigger.md"
    title: Wonder Woman red flag #4 trigger
    last_modified: 2026-08-19
  - id: veto-cascade
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-veto-cascade-with-batman-ops.md"
    title: Veto cascade Wonder Woman × Batman — matrice 8 cellules
    last_modified: 2026-08-19
  - id: omk-finance-active
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-omk-finance-active-migration-urgency.md"
    title: OMK Finance SHADOW_ACTIVE → ACTIVE migration urgence
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Wonder Woman présidence tournante Council — quand, comment, limites

## Pourquoi ce concept

`b2-council-cadence-and-chair.md` pose la présidence tournante comme règle
canonique : **pas de président permanent**, le captain au centre de
l'arbitrage préside. Le corpus ne dit pas quels contextes concrets font
de Wonder Woman la présidente d'une séance, ni quelles prérogatives/
limites s'appliquent dans son cas spécifique. Ce concept填补 ce trou.

## 3 contextes où Wonder Woman préside

### 1. Arbitrage où Finance est en **aval** de la transition

Le R `b2-council-cadence-and-chair.md` §« La présidence tournante » pose
explicitement : « Pour un arbitrage Growth × Sales, le président est
Sales (en aval). » La règle se généralise : **le captain en aval de
la transition préside**.

Wonder Woman préside donc quand Finance est en aval. Trois pair-checks
canoniques où Finance est en aval :

| Pair-check | Rôle WW | Présidence WW |
|---|---|---|
| **Growth → Finance** (#5 canon) | A (Accountable sur transition) | **Oui — préside** |
| **Sales → Finance** (couplage projeté tour 4) | A sur discount >15% | **Oui — préside** |
| **Product → Finance** (couplage projeté via F22 moat) | A sur marge compression | **Oui — préside** |

**Cas concret typique** : Superman (Growth) demande un budget paid media
sans métrique de retour chiffrée (veto WW §06 — triplet 28). Le Council
convoqué en séance ad hoc, WW préside. WW pose l'ordre du jour, tient
le minutage 60min, signe le packet `decision: blocked` (vet catalogue
actif) avec motif « métrique de retour chiffrée manquante ».

**Présidence ≠ Accountable** : WW préside l'arbitrage ET est Accountable
sur la transition. Les deux rôles ne sont pas en conflit parce que
l'arbitrage est sur la transition, pas sur le contenu Finance. La nuance
est dans `b2-pair-check-raci-by-rank.md` : « A est toujours le B2
captain en aval de la transition (le domaine qui reçoit) ». WW préside
en tant que downstream captain, pas en tant que juge impartial.

### 2. Arbitrage où Finance est impliquée avec un autre capitaine en aval

Cas de la **cascade veto** (concept 15 — tour 3) : Wonder Woman × Batman
opposent leurs vetos simultanément sur une même dépense (WW veto
catalogue §06 + Batman veto procédure §02 sur condition d'arrêt).

Le captain en aval de la transition est Batman (Ops). Batman devrait
présider. **Mais** : WW est partie prenante — sa présidence serait
biaisée. Le corpus cadence ne tranche pas explicitement ce cas.

**Doctrine proposée** (à soumettre Council) :

> Quand un arbitrage implique Wonder Woman comme **partie prenante**
> (détenant un veto catalogue sur le cas), la présidence revient au
> **second captain impacté** ou, à défaut, au captain dont le
> domaine est en aval strict de la transition. Wonder Woman ne
> préside jamais un arbitrage où elle oppose son veto.

**Application concrète** :

- Cascade WW × Batman sur dépense Ops : Batman préside (Ops est aval).
- Cascade WW × Superman sur budget Growth : Superman préside (Growth est aval).
- Cascade WW × Aquaman sur deal contract (Legal aval) : Aquaman préside (Legal aval).
- Cascade WW × Flash sur release payante (Product aval) : Flash préside (Product aval).
- Cascade WW × Cyborg sur infra (IT aval) : Cyborg préside (IT aval).
- Cascade WW × Green Lantern sur recrutement (People transverse) : cas limite — présidée par WW (elle n'est pas opposante au veto People) ou par Green Lantern (People en tant que transversal). **Recommandation** : présidée par Green Lantern.

### 3. Séance bilan fin de 12WY

`b2-council-cadence-and-chair.md` §« Séance bilan » : « le président est
le captain dont le domaine a le plus de décisions mésoperpétuelles
ouvertes dans le cycle ».

Wonder Woman préside le bilan si, en fin de 12WY, le compteur de
décisions mésoperpétuelles Finance ouvertes (decision: accepted sans
next_review atteint) est le plus élevé parmi les 8 capitaines.

**Cinq décisions potentielles WW en cycle 12WY** :

1. **Migration OMK Finance** (concept 17) — packet mésoperpétuel
   `B2-MESO-DECISION-2026-31` proposé, next_review T+90.
2. **F24 co-signature Cyborg** (concept 21) — packet mésoperpétuel
   projeté si cycle.
3. **F23 pricing pouvoir A** (concept 20) — packet décision droits si
   amplification triplet 58 Council-adopted.
4. **Couplage triangulaire discount >15%** (concept 24) — packet
   `B2-MESO-DECISION-2026-NN` saisissable en mode negotiation.
5. **Cadence Paid Release Gate** (concept 16) — packet mésoperpétuel
   avec champ `gate_cadence_trigger`.

Si les 5 sont ouverts en fin de cycle, WW préside le bilan. Sinon, la
présidence revient au captain au compteur le plus élevé.

**Hypothèse implicite** : Wonder Woman préside **au moins une fois par
cycle** si les 5 packets sont émis, soit ~3-4 cycles par an selon
cadence sprint. Cohérent avec cadence hebdo B2.

## 3 prérogatives canoniques (verbatim cadence)

Le `b2-council-cadence-and-chair.md` §« La présidence tournante » pose
trois prérogatives pour tout président de séance — Wonder Woman les
reçoit quand elle préside :

### 1. Poser l'ordre du jour

Chaque capitaine impacté énonce son DoD, son blocker, son veto éventuel.
WW en tant que présidente structure l'ordre :

- Capitaines amont énoncent leur position en premier (F1 runway,
  F3 MRR, F19-F22 allocation si impactés).
- Capitaines aval énoncent en second.
- Capitaines transverses (People, Legal) en dernier.
- WW tranche si DoDs se contredisent dans l'ordre du jour — mais
  l'arbitrage final reste le cercle, pas la présidente seule.

### 2. Tenir le minutage (60 min max)

La séance ne dépasse pas 60 minutes ; un arbitrage non résolu escalade B1.
WW applique cette borne au minuteur près. Si à 50 min l'arbitrage n'est
pas résolu, WW ouvre le vote (mode parallel ou escalate_to_B1 par défaut).

**Pourquoi 60 min** : au-delà, les autres capitaines saturent et les
arbitrages suivants du sprint ne sont pas traités. La cadence sprint
VP (triplet 10) impose 4 sprints/mois ; un arbitrage qui consomme un
sprint entier casse la cadence.

### 3. Signer le packet de sortie

Le packet mésoperpétuel porte la signature WW présidente. La signature
vaut **cosignataire des 8 capitaines** : le Council tranche en cercle,
mais le journal porte une signature (l. WW signe sans隐匿 la décision
du cercle.

**Limite de signature** : WW ne signe pas un packet qui contredit son
propre veto catalogue. Si la séance lève le veto WW pour adopter le
mandat, WW **refuse de signer** — l'arbitrage est documenté mais sans
sa signature, et le packet escalade B1 implicitement (cf. section
suivante).

## 3 limites strictes

### Limite 1 — Conflit d'intérêt (veto opposé)

Si WW oppose son veto catalogue sur le cas en arbitrage, elle ne préside
pas. La présidence revient au captain en aval de la transition
(cf. section 2 ci-dessus). Cette limite est **doctrinale**, pas
« optionnelle — un veto opposant et présidant simultanément est un
conflit d'intérêt non résolu ».

### Limite 2 — Partialité (intérêt financier personnel)

Si WW a un intérêt financier personnel dans le cas (ex : elle est
aussi actionnaire d'un vendor SaaS que la dépense finance), elle ne
préside pas **et** ne vote pas. La séance escalade B1 si le quorum
tombe à 4/8.

**Pourquoi** : la partialité financière d'un capitaine sur un arbitrage
Finance n'est pas un cas théorique — c'est un piège récurrent des
PME early-stage. La doctrine D4 append-only impose la transparence :
WW disclose tout intérêt financier dans le journal Council en début
de séance.

### Limite 3 — Escalade B1 (North Star en jeu)

Si l'arbitrage touche North Star (ex : « pivoter US premium » vs
« consolider EU SMB »), WW **ne préside pas l'arbitrage final**. La
présidence revient à B1 (Summers). C'est la position canonique
`b2-council-arbitrage-rule.md` §« Quand le Council escalade à B1 » —
« Conflit de North Star. Deux mandates B1 simultanés exigent des
wheel-states incompatibles. Le Council n'a pas la légitimité pour
choisir entre deux directions. »

## Distinction présidence vs Accountable

Deux rôles distincts :

| Rôle | Déclencheur | Qui |
|---|---|---|
| **Accountable (A)** sur transition | pair-check déclenché | B2 captain en aval (Wonder Woman si Finance aval) |
| **Présidence de séance** | arbitrage Council convoqué | B2 captain en aval OU en conflit (cf. section 2) |

Ces deux rôles sont **compatibles** quand WW est en aval pur (Finance
reçoit sans veto opposant) : elle préside ET est Accountable. Mais
**incompatibles** quand WW oppose son veto : elle reste Accountable
mais cède la présidence.

**Cas où WW préside SANS être Accountable** :

- Séance bilan (présidence = compteur décisions ouvertes, pas Accountable).
- Arbitrage transversal où WW est upstream mais pas opposante (ex :
  Finance → Growth sur budget paid — Superman aval, mais WW upstream
  ne préside pas — Superman préside).
- Arbitrage où WW est impactée mais sans veto opposé (ex : arbitrage
  sur cadence de revue F1-F25 où WW est elle-même le sujet — Batman
  préside en tant que capitaine du domaine Ops qui héberge la cadence).

## Le cas spécifique de la **migration OMK Finance** (concept 17)

Le packet `B2-MESO-DECISION-2026-31` proposé pour la migration OMK
Finance → ACTIVE est saisi en mode **parallel** (Finance seule impactée
par la migration, les autres domaines ne bougent pas). Wonder Woman
est à la fois Accountable ET seule capitaine impactée — **elle préside
sa propre migration**.

C'est défendable parce que :

- Aucun veto catalogue n'est opposé (la migration n'est pas une
  dépense récurrente — c'est un changement de statut opérationnel).
- Aucun conflit d'intérêt financier (la migration est interne au
  domaine Finance).
- Aucun arbitrage North Star (la migration est dans le mandat B1
  « cycle 12WY courant »).

**Mais** : la doctrine canon exige 5/8 quorum. Une séance où WW est
seule n'atteint pas le quorum. La migration OMK passe donc par **un
packet mésoperpétuel auto-signé** (sans séance Council), ce qui n'est
pas la position canonique. **Recommandation** : la migration est
saisie en séance hebdomadaire ordinaire avec les 5 autres capitaines
présents (Batman, Superman, Flash, Cyborg, JohnJones — quorum atteint),
et WW préside.

## Asymétrie avec Batman présidence

Batman préside plus souvent que WW parce que :

- Batman est **aval** de Sales → Ops (#2) et Product → Ops (#3) — deux
  pair-checks canoniques où Batman est systématiquement aval.
- Batman est aussi aval implicite de Finance → Ops (dépenses Ops) —
  troisième pair-check où Batman aval.

Wonder Woman est **aval** de Growth → Finance (#5) et Sales → Finance
(projeté) et Product → Finance (projeté via F22). **3 cas aussi**, mais
la fréquence d'occurrence est asymétrique : les paires Growth→Finance
et Sales→Finance se déclenchent à chaque cycle de build, tandis que
Sales→Ops se déclenche à chaque closing deal (plus fréquent).

**Hypothèse** : Batman préside ~3x par cycle sprint, WW ~2x par cycle,
Flash ~2x (Product aval de Finance et de Legal), Superman ~1x (Growth
aval de Sales et Finance), autres ~1x chacun. Le compteur bilan
fin de 12WY reflète cette fréquence — Batman préside souvent le bilan.

## Anti-pièges

- **WW préside une séance où elle oppose son veto.** Conflit d'intérêt
  non résolu. Le packet signé est non-vérifiable par les pairs (les
  pairs n'ont pas tranché — la présidente a tranché seule en réalité).
- **WW refuse de signer un packet légitime.** Si le cercle tranche
  mais que le packet contredit le veto catalogue WW, WW ne peut pas
  bloquer en refusant la signature — l'arbitrage doit escalader B1
  pour réécriture du catalogue. La doctrine `b2-council-cadence-and-chair.md`
  §« Quorum » précise que la séance plein quorum peut amender un veto
  (à majorité 5/8 + escalade B1).
- **WW signe un packet en cascade Batman × WW.** Si Batman préside
  (aval) et que WW oppose son veto, WW refuse de co-signer — la
  séance escalade B1 automatiquement (cf. limite 1).
- **Présidence tournante devenue permanente.** Si WW préside 4 séances
  d'affilée (par cumul de décisions bilan ou de cas aval), le Council
  a dérivé. Le `b2-council-cadence-and-chair.md` §« Anti-pièges » pose
  le signal d'alerte.
- **Confondre présidence et Accountable RACI.** Un RACI qui pose « WW
  préside les arbitrages Finance » est mal posé — la présidence est
  par arbitrage, pas par pair-check. WW préside quand Finance est
  impliquée, pas « tous les arbitrages Finance ».

## Liens

- [[b2-council-cadence-and-chair]] — la présidence tournante canonique
- [[b2-council-arbitrage-rule]] — l'instance qui mandate la présidence
- [[b2-meso-decision-packet-spec]] — le format packet signé
- [[wonder-woman-red-flag-4-trigger]] — quand WW préside sur red flag #4
- [[wonder-woman-veto-cascade-with-batman-ops]] — la cascade où WW cède la présidence
- [[wonder-woman-omk-finance-active-migration-urgency]] — la migration auto-présidée
- [[wonder-woman-couplage-sales-discount-signoff]] — couplage Sales×Finance×Legal discount
- [[wonder-woman-f24-sovereign-infra-arbitrage-doctrine]] — co-signature WW × Cyborg

## Note de confiance

**Confirmé par machine, à moitié.** Les 3 contextes où WW préside
(aval transition, conflit d'intérêt cède, séance bilan compteur) sont
**projetés** depuis la règle canonique de présidence tournante par
impacted captain (`b2-council-cadence-and-chair.md` §« La présidence
tournante »). Les 3 prérogatives sont citées verbatim. Les 3 limites
sont **reconstruites** depuis la doctrine conflit d'intérêt (implicite
dans la règle de quorum 5/8) et la doctrine North Star escalade B1.
La doctrine « WW ne préside jamais un arbitrage où elle oppose son
veto » est une **projection** — le corpus ne l'explicite pas, mais
elle est cohérente avec la doctrine d8 vetos catalogue §3 (veto non-
négociable). L'asymétrie Batman vs WW présidence est **projetée** par
comptage des pair-checks aval — pas mesurée en cycle réel.