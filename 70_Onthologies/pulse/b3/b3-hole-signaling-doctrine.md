---
type: Concept
title: B3 hole-signaling — un B3 qui trouve un trou ne le comble pas, il le signale
description: Étend au B3 l'invariant Coach OS « interdire de combler un trou du sprint ». Un trou de paquet (champ manquant, dépendance non résolue, hypothèse non vérifiable) n'est jamais comblé en silence par le B3 : il est signalé en format canonique 4 champs (location, kind, impact, suggested_fix). Le trou devient un objet de signalement, pas une décision invisible.
tags: [b3, hole, signaling, interdits, anti-pattern, dependance, silence-bug]
generated: { by: minimax-m3, at: 2026-08-19T02:45:00Z }
verified:
  - { by: process:lecture-triplets-v3, at: 2026-08-19T02:45:00Z }
  - { by: process:synthese-pulse-b3-tour-1, at: 2026-08-19T02:45:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: triplet-interdit
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: v3-business triplets (ligne 41 — interdit-combler-trou)
    last_modified: 2026-08-17
  - id: jtbd-grammar
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/b3-jtbd-packet-grammar.md"
    title: JTBD-001 packet grammar — la grammaire B3 canonique
    last_modified: 2026-08-17
  - id: agent-relecteur
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/autonomie-agents/agent-relecteur-mandat.md"
    title: Agent relecteur — mandat unique, contexte vierge
    last_modified: 2026-08-17
  - id: b3-reception
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-jtbd-packet-reception-checklist.md"
    title: JTBD packet — checklist de réception côté B3
    last_modified: 2026-08-19
okf_version: "0.2"
---

# B3 hole-signaling — un B3 qui trouve un trou ne le comble pas, il le signale

> Étend au B3 un invariant Coach OS déjà posé pour les techniciens :
> *« Tout B3 a l'interdit de combler lui-même un trou du sprint — il le
> signale à son VP au lieu de laisser le défaut invisible. »* (triplet
> v3 ligne 41). Ce concept pose le **format canonique** du signalement
> de trou et la liste des trous que le B3 doit savoir reconnaître.

## Pourquoi « ne pas combler en silence »

Trois raisons tirées du canon et de la doctrine :

1. **Le trou est un fait, pas une décision.** Combler un trou de paquet
   sans le signaler, c'est prendre une décision à la place de B2 (qui
   aurait pu combler autrement, ou refuser de combler). L'autorité
   d'arbitrage reste à B2.
2. **Le trou invisible devient un bug.** Un B3 qui patche un ICP filter
   manquant pour avancer **engage** le squad sur une ICP qu'il a
   lui-même définie. Quand le squad lead ou le B2 s'en aperçoit (plus
   tard), la dette est plus grande que si le trou avait été signalé
   d'emblée.
3. **Le trou signalé est un asset.** Un trou bien décrit (location,
   kind, impact) permet à B2 de :
   - corriger le paquet à la source ;
   - re-prioriser les jobs ;
   - documenter un pattern récurrent qui deviendra un nouveau champ
     canonique du packet JTBD-001.

## Les 7 catégories de trous qu'un B3 doit savoir reconnaître

Le B3 ne signale pas « quelque chose manque » — il catégorise. 7
catégories, dérivées de la checklist de réception
(`b3-jtbd-packet-reception-checklist.md`) :

| Catégorie | Description | Origine probable |
|---|---|---|
| **HOLE_FIELD** | Un champ obligatoire du frontmatter est absent ou vide. | Packet mal rédigé par B2. |
| **HOLE_VOC** | La VOC (5 pains) est absente ou trop générique pour le mode. | B2 n'a pas interviewé / n'a pas calibré. |
| **HOLE_ICP** | L'ICP filter n'a pas de critère de rejet, ou le scoring est manquant. | B2 a sauté l'étape. |
| **HOLE_HYP** | Une painkiller hypothesis n'a pas de variant ou n'a pas de kill-gate. | B2 a omis la rigueur canonique. |
| **HOLE_LEAD_LAG** | Pas de lead indicator, ou lag indicator non-mesurable. | B2 n'a pas défini la mesure. |
| **HOLE_GATE** | Un build gate est manquant ou sans condition d'arrêt. | B2 a omis la clause d'arrêt (Batman veto). |
| **HOLE_ACCEPT** | `Acceptance <Hero>` est déjà cochée à la réception (faux canon). | Packet recyclé sans reset de l'acceptance. |

Cette catégorisation **n'épuise pas** les trous. Si le B3 voit un trou
qui ne rentre pas dans ces 7 cases, il le signale avec `kind: HOLE_OTHER`
et une description en une phrase. La règle : ne pas inventer une
catégorie pour faire sérieux.

## Le format canonique du signalement

Chaque trou signalé est un objet distinct, dans `SCRUMS.md` (le journal
B3 quotidien) **et** dans le ping au squad lead ou B2. Le format est
verrouillé à 4 champs, dans cet ordre :

```
HOLE_SIGNAL
  location: <packet_id>:<section>:<champ>
  kind:     HOLE_FIELD | HOLE_VOC | HOLE_ICP | HOLE_HYP |
            HOLE_LEAD_LAG | HOLE_GATE | HOLE_ACCEPT | HOLE_OTHER
  impact:   <1 phrase — qu'est-ce que ça empêche>
  suggested_fix: <1 phrase — comment B2 pourrait combler, OU
                  pourquoi il ne faut pas le combler>
```

### Critère de complétude

Si le B3 ne peut pas填写 l'`impact`, il n'a pas compris le trou —
creuse d'abord. Si le B3 ne peut pas proposer un `suggested_fix`,
c'est OK : il écrit `suggested_fix: <à arbitrer par B2>` et laisse
B2 trancher.

## Le ping associé

Le signalement de trou **n'est pas un ping pair-unblock**. C'est un
ping **hiérarchique** — vers B2 owner, parfois via le squad lead.
Trois reasons :

- Le pair ne peut pas combler un trou de paquet — seul B2 (qui a écrit
  le paquet) peut le corriger.
- Le pair risque de **re-normaliser** le trou (proposer un patch par
  défaut), ce qui est l'anti-pattern inverse du signalement.
- Le trou peut signaler un défaut de **pair check** (cf.
  `business-wheel-harmonization-matrix.md`) que seul le B2 Council peut
  arbitrer.

Le format du ping suit celui de `b3-peer-unblock-protocol.md` avec un
champ supplémentaire `hole_id` qui lie le trou à son entrée dans
`SCRUMS.md`.

## Le cycle de vie du trou

Un trou signalé traverse 4 états :

1. **OPEN** — le B3 l'a consigné et pingé B2.
2. **ACKNOWLEDGED** — B2 a lu et confirme qu'il arbitre.
3. **RESOLVED** — B2 a comblé (mise à jour du packet) ou a décidé de
   ne pas combler (et le job B3 est annulé ou re-scopé).
4. **WONT_FIX** — B2 a explicitement choisi de laisser le trou (avec
   justification). Le B3 **documente** l'acceptation dans son SCRUM et
   poursuit.

L'état `WONT_FIX` est important : un B3 ne peut pas le deviner, c'est
B2 qui l'autorise. Sans cette autorisation, le B3 ne comble pas — il
ré-émet le signal.

## Anti-patterns

1. **B3 qui invente le champ manquant** (HOLE_FIELD) avec une valeur
   plausible. C'est le **premier** anti-pattern de la discipline B3.
2. **B3 qui choisit une VOC par défaut** parce que la VOC manque. Le
   B3 n'a pas la légitimité pour définir à qui parle le job.
3. **B3 qui skip le signal pour « ne pas déranger B2 ».** Le B3 n'est
   pas là pour protéger B2 de ses oublis — il est là pour exécuter un
   job bien formé. Un B2 dérangé par un signal de trou est un B2 qui
   peut corriger ; un B2 **pas** dérangé par un trou comblé est un B2
   qui arbitre à l'aveugle.

## Lien avec la preuve et l'examen

`b3-proof-path-4-formes.md` pose que la preuve est due à `DONE`. Un
job B3 qui se termine avec un trou non-résolu (état `OPEN`) **n'est
pas** `DONE` — c'est `BLOCKED` (cf.
`b3-veto-and-signal-vocabulary.md`). Le B3 ne peut pas émettre
`DONE` sur un job qui contient des trous `OPEN`.

`examen-prealable.md` ajoute : l'examen porte sur le code rendu, pas
sur le paquet. Mais un paquet incomplet **rend** un code rendu sur des
hypothèses implicites — l'examen ne détecte pas cette dette. Seul le
signalement de trou le fait.

## Source du concept

- `triplet v3 ligne 41` — *« Tout B3 a l'interdit de combler
  lui-même un trou du sprint — il le signale à son VP au lieu de
  laisser le défaut invisible. »*
- `agent-relecteur-mandat.md` §« Pourquoi ne pas automatiser » — la
  séparation entre défauts mécaniques (automatisés) et défauts
  sémantiques (humain / agent relecteur). Le trou de paquet est un
  défaut **sémantique** — il faut un pair pour le voir.
- `b3-jtbd-packet-reception-checklist.md` §1 — la liste des champs
  obligatoires du frontmatter, dérivée des 7 catégories de trous.

## Liens

- [[b3-jtbd-packet-reception-checklist]] — les champs que le B3 vérifie
  à la réception, dont l'absence est un HOLE_FIELD
- [[b3-peer-unblock-protocol]] — quand le trou n'est pas un trou de
  paquet mais un blocker technique, c'est un peer-unblock
- [[b3-veto-and-signal-vocabulary]] — le trou escalade en `BLOCKED`,
  et le format du ping B2
- [[b3-cycle-scrums-five-per-week]] — où les HOLE_SIGNAL sont consignés
- [[b3-proof-path-4-formes]] — un job avec HOLE_OPEN n'est pas `DONE`

## Note de confiance

**Confirmé par machine.** L'invariant « interdire de combler un trou »
est verbatim du triplet v3 ligne 41. Le format 4 champs (location,
kind, impact, suggested_fix) est dérivé du format pair-unblock
(`b3-peer-unblock-protocol.md` §« Le format canonique »). Les 7
catégories sont dérivées de la checklist de réception.

**Limite signalée** : le cycle de vie à 4 états (OPEN / ACKNOWLEDGED /
RESOLVED / WONT_FIX) est une **structuration** de la pratique B3
attendue, pas un format canonique publié. Le triplet source pose
l'invariant, pas le cycle de vie.