---
type: Concept
title: B1 mandate acceptance check — la face miroir, le verrou de gouvernance
description: Six critères qu'un B2 captain doit valider dans les 24h après réception d'un mandat B1. Si un seul échoue, le mandat est gelé et B1 reformule. Sans ce verrou, la handoff queue accumule des mandats morts-nés qui polluent la matrice d'harmonisation en aval.
tags: [b1, mandate, acceptance, gouvernance, verrou, handoff]
generated: { by: minimax-m3, at: 2026-08-19T02:15:00Z }
verified:
  - { by: process:synthese-pulse-b1-tour-2, at: 2026-08-19T02:15:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: b1-mandate-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-mandate-packet-spec.md"
    title: B1 mandate packet — la grammaire du paquet B1 vers B2
    last_modified: 2026-08-19
  - id: b1-stop-conditions
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-stop-conditions-escalier.md"
    title: B1 stop conditions et escalier d'escalade
    last_modified: 2026-08-19
  - id: council
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
okf_version: "0.2"
---

# B1 mandate acceptance check — la face miroir, le verrou de gouvernance

`b1-mandate-packet-spec.md` pose la grammaire du paquet B1 → B2. Mais la
grammaire est unilatérale : elle dit ce que B1 émet. Elle ne dit pas ce
que B2 doit attester pour que le mandat *prenne*. Sans acceptance check,
un mandat est un coup d'envoi unilatéral — et la discipline de la handoff
queue s'effrite dès qu'un mandat part sans destinataire confirmé.

## Pourquoi un verrou côté B2

Trois défaillances observées quand l'acceptance manque :

1. **Le mandat part sans owner.** B1 l'émet, B2 ne le lit pas, B3 ne
   reçoit jamais de DoD/JTBD. La handoff queue accumule des mandats
   fantômes. Le scan wheel imbalance ne les voit pas, parce qu'ils ne
   sont ni actifs ni clos.
2. **Le mandat est mal routé.** B1 mandate un B2 dont le domaine ne
   matche pas. Sans acceptation, le mandat reste en queue ; le bon B2
   ne le voit pas ; le mauvais B2 l'ignore. La roue tourne à vide.
3. **Le mandat est impossible.** B1 fixe un signal ou une contrainte que
   le B2 ne peut pas tenir (cf. `b1-success-signal-spec.md` § mécanisme
   de substitution). Sans acceptation, B2 ne remonte pas la friction —
   il ignore le mandat et attends le prochain rollover pour s'en plaindre.

Dans les trois cas, **le coût est porté par B1** : il pense avoir
mandaté, il découvre au rollover que rien n'a bougé.

## Les six critères d'acceptance (24h)

Un mandat B1 est **accepté** ssi les six critères suivants sont validés
par le B2 captain destinataire dans les **24 heures** suivant la
réception. Passé ce délai sans réponse, le mandat est en `STALE` et B1
doit relancer.

### 1. Owner identifié

Le mandat est routé à **un captain B2 unique** (un seul des 8 domaines).
Si le mandat touche plusieurs domaines, il est multi-destinataires et
doit passer par le B2 Council (cf. `b2-council-arbitrage-rule.md`) — pas
un acceptance check direct.

### 2. Intent compris en une phrase

Le B2 captain reformule l'intent en une phrase, dans ses propres mots.
Si sa reformulation diverge de l'intent B1, l'acceptance échoue —
l'intent doit être ré-écrit ou clarifié.

### 3. Contraintes tenables

Pour chaque contrainte listée par B1, le B2 captain atteste qu'il peut
la tenir **sans** amender la doctrine du domaine. Si une contrainte
exige un amendement doctrinal (ex. : changer la doctrine veto-dépense),
le mandat remonte à B1 avec un veto catalogue anticipé (cf.
`b2-eight-domain-vetoes-catalogue`).

### 4. Signal tenable ou substitut proposé

Le signal B1 est soit accepté tel quel, soit remplacé par un substitut
de la même famille (cf. `b1-success-signal-spec.md` § mécanisme de
substitution). Pas de substitut = acceptance échouée.

### 5. DoD-Una anticipé

Le B2 captain énonce un **DoD-Una** préliminaire — les 3 critères
minimum qui définiront le DoD final (cf. `b2-harmonization-matrix-exploitable`
§« B2 mandate → Rock → DoD »). Sans DoD-Una, le mandat n'a pas de
forme de sortie ; il est un voeu.

### 6. Veto catalogue vérifié

Le B2 captain vérifie que le mandat ne contrevient à aucun des 8 vetos
catalogue (cf. `b2-eight-domain-vetoes-catalogue`). Si un veto
s'applique, l'issue n'est pas l'acceptance — c'est un veto opposé (le
mandat amendé, retiré, ou escaladé B1).

## Le format de l'attestation

L'attestation est courte, en YAML, append-only dans la handoff queue B1 :

```yaml
mandate_id: B1-B2-MANDATE-YYYY-NN
accepted_by: <captain B2>
accepted_at: <ISO 8601>
reformulated_intent: "<une phrase, dans les mots du B2 captain>"
constraints_acknowledged:
  - "<contrainte 1 du mandat B1>"
  - "<contrainte 2 du mandat B1>"
signal_status: accepted | substituted
signal_substitute: |
  <substitut si proposé, dans la même famille>
dod_una_draft:
  - "<critère 1>"
  - "<critère 2>"
  - "<critère 3>"
veto_check: passed | veto_opposed | escalated_to_b1
```

Si un seul champ manque ou est invalide, l'attestation est rejetée. B2
recommence, B1 attend.

## L'échec d'acceptance — la chaîne d'escalade

Quatre issues possibles, par ordre de fréquence attendue :

1. **Acceptation complète.** Le mandat entre en file B2 active. Le B2
   captain ouvre un Rock et dispatche en B3 dans les 48h.
2. **Acceptation avec signal substitué.** Le mandat entre en file, mais
   avec un signal différent. B1 doit contre-signer le substitut dans
   les 72h (cf. `b1-success-signal-spec.md` § mécanisme).
3. **Veto opposé.** Le mandat est gelé. Le B2 captain documente le veto
   catalogue. Le mandat passe en `BLOCKED` dans la handoff queue. B1
   peut amender le mandat, retirer, ou escalader A0 (cf.
   `b1-stop-conditions-escalier` § escalier canonique).
4. **Acceptation échouée — silence 24h.** Le mandat passe en `STALE`.
   B1 relance. Si le B2 captain reste silencieux 48h, le mandat est
   escaladé au B2 Council pour redistribution.

## Anti-pièges

- **Acceptation par défaut.** Un B2 captain qui accepte sans reformuler
  l'intent (critère 2) crée un mandat dont l'exécution diverge de
  l'intent B1. La reformulation en une phrase est non-négociable.
- **Acceptation sans DoD-Una.** Un mandat accepté sans DoD-Una est un
  mandat dont la sortie est inconnue — c'est exactement le cas que la
  matrice d'harmonisation ne peut pas tester (cf.
  `b2-harmonization-matrix-exploitable`).
- **Acceptation partielle.** Un mandat qui coche 4 critères sur 6 n'est
  pas accepté. Il est `BLOCKED` et B1 reformule. La règle est binaire :
  tout ou rien.
- **Acceptation multiple.** Un mandat routé à deux captains sans passer
  par le Council n'est pas accepté — c'est une confusion d'autorité.
  Le Council tranche d'abord, l'acceptance suit.

## Sources

- `b1-mandate-packet-spec.md` — le gabarit amont.
- `b1-stop-conditions-escalier.md` — l'escalier qui absorbe les échecs
  d'acceptance.
- `b2-council-arbitrage-rule.md` — quand plusieurs capitaines sont visés.

## Liens

- [[b1-mandate-packet-spec]] — la grammaire amont
- [[b1-success-signal-spec]] — le format du champ `success_signal`
- [[b1-stop-conditions-escalier]] — l'aval en cas d'échec
- [[b2-council-arbitrage-rule]] — quand le mandat est multi-domaine
- [[b2-eight-domain-vetoes-catalogue]] — les 8 vetos qui bloquent l'acceptance
- [[b1-omk-t2-pivot-us-mandate]] — application au pivot US OMK T2

## Note de confiance

**Confirmé par machine.** Le besoin d'un verrou côté B2 est **reconstruit**
à partir du constat que le mandat-packet-spec ne pose que la grammaire
B1→B2 sans face B2→B1. Les six critères sont **extrapolés** depuis la
doctrine matrice (DoD-Una), veto catalogue, et Council. Le format YAML
d'attestation suit le gabarit des meso-decision-packets de B2 (cf.
`b2-meso-decision-packet-spec`). Le délai 24h/72h est motivé par la
cadence B2 (hebdomadaire), pas une section explicite du canon.