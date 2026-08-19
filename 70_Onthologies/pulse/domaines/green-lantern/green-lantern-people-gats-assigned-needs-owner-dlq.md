---
type: Concept
title: People — trois gates émis, ASSIGNED / NEEDS_OWNER / DLQ
description: People émet trois états B2 vers les autres domaines : ASSIGNED (owner valide, charge tenable, mandat vérifiable), NEEDS_OWNER (mandat posé mais owner vacant ou charge saturée), DLQ (pas d'owner possible, escalade B1 ou abandon du mandat). Chaque état a un déclencheur vérifiable et un couplage avec le veto People. Le mapping avec les 8 gates des autres domaines révèle un sous-ensemble commun mais une asymétrie : People est le seul à pouvoir émettre DLQ sans veto externe.
tags: [people, green-lantern, gates, assigned, needs-owner, dlq, b2, etat]
generated: { by: minimax-m3, at: 2026-08-19T04:10:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T04:10:00Z }
sources:
  - id: avengers-wheel-canon
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: "Eight Domain Avengers Wheel — gates B2 émis par domaine"
    last_modified: 2026-08-17
  - id: harmonization-pair-check-9
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: "Harmonisation — pair-check #9 People → Tous"
    last_modified: 2026-08-17
  - id: veto-triplet-23
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 23 — veto People sur recrutement sans mandat"
    last_modified: 2026-08-17
  - id: raci-pair-check
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: "RACI par rang — People C transverse, jamais A"
    last_modified: 2026-08-19
okf_version: "0.2"
---

# People — trois gates émis, ASSIGNED / NEEDS_OWNER / DLQ

## Énoncé canon

> *« People B2 émet `ASSIGNED` / `NEEDS_OWNER` / `DLQ`. »*
> — `eight-domain-avengers-wheel.md` ligne « B2 emet », domaine 07

Les trois états sont les **outputs officiels** de People vers les autres
domaines B2 et vers le B2 Council. Ils répondent au pair-check #9 *People
→ Tous* : *« la propriété et la charge sont-elles tenables ? »*

## Gate 1 : `ASSIGNED`

**Définition.** Un poste ou un mandat a un **owner valide** (humain ou
agent), une **charge tenable** (≤ 1.0 sur la carte de charge), et un
**mandat vérifiable** (rôle + horizon + critère de sortie).

**Déclencheurs vérifiables** :

- Le poste est occupé par un humain ou un agent nommé dans
  `b3-squad-roster.md` du domaine d'accueil.
- La charge de l'owner est documentée et ≤ 1.0 (cf. charge-capacité
  canonique, à vérifier — non posé explicitement dans V4).
- Le mandat de l'owner contient les trois champs obligatoires (rôle,
  horizon, critère de sortie).

**Effet.** Le pair-check #9 passe. Le domaine d'accueil peut émettre son
gate propre (ex : `PRODUCT_READY`, `SALES_READY`). People **ne bloque
pas** la chaîne.

**Couplage avec le veto.** Aucun veto People ne s'oppose. `ASSIGNED` est
l'état **par défaut** quand le mandat est complet.

## Gate 2 : `NEEDS_OWNER`

**Définition.** Un poste ou un mandat **est posé** (le rôle existe, le
besoin est reconnu) mais **manque d'owner** — soit le poste est vacant,
soit l'owner est en surcharge, soit le mandat est incomplet.

**Déclencheurs vérifiables** :

- **Vacance** — un owner a quitté (fin de mandat, démission, rotation)
  et aucun successeur n'est mandaté.
- **Surcharge** — l'owner actuel a une charge > 1.0, vérifiable par
  cumul des mandats actifs (méthode de calcul à fixer).
- **Mandat incomplet** — le rôle est posé mais le mandat ne contient
  pas les trois champs obligatoires. **Note** : ce cas confine au veto
  People ; voir §« Frontière avec le veto » ci-dessous.

**Effet.** Le pair-check #9 ne passe pas. Le domaine d'accueil reçoit un
**avertissement** mais peut continuer (mode `negotiation` au sens matrice
d'harmonisation). People ouvre un arbitrage B2 — soit la charge est
redistribuée, soit un recrutement est lancé.

**Couplage avec le veto.** Si `NEEDS_OWNER` est causé par un mandat
incomplet, le veto People peut s'opposer — voir `green-lantern-people-veto-recrutement-sans-mandat`.

## Gate 3 : `DLQ`

**Définition.** *Dead-Letter Queue* — un poste ou un mandat **ne peut
pas être assigné** dans le cycle courant. People a essayé, et a échoué :
aucun owner possible (pool trop étroit, charge globale saturée, scope
abandonné).

**Déclencheurs vérifiables** :

- **Pool insuffisant** — aucun humain ou agent dans le squad B3 cible
  n'a la compétence requise, et aucun recrutement n'est possible dans
  le cycle.
- **Charge globale saturée** — tous les owners potentiels du domaine
  sont à charge > 1.0, et aucun arbitrage de redistribution n'aboutit.
- **Scope abandonné** — le besoin lui-même est caduque (projet annulé,
  pivot North Star).

**Effet.** Le pair-check #9 échoue. Le domaine d'accueil **gèle** son
gate propre (ex : `PRODUCT_READY` ne peut pas être émis si People émet
`DLQ`). C'est un **arrêt dur** sur la transition.

**Couplage avec le veto.** `DLQ` peut être causé par un veto People
opposé à un recrutement qui aurait pu résoudre le cas. Le Council doit
distinguer les deux : `DLQ` *par absence de candidat* vs `DLQ` *par
veto non levé*. Le second est un **conflit de périmètre** qui escalade
B1.

## Frontière avec le veto

Les trois gates ne sont **pas** le veto. Le veto est une **opposition**
— *« je bloque ce recrutement »*. Les gates sont des **constats** —
*« dans l'état actuel, l'owner est / n'est pas disponible »*.

Confusion typique : un domaine d'accueil voit `NEEDS_OWNER` et croit que
People a opposé un veto. C'est faux. `NEEDS_OWNER` est un signal de
vacance ou de surcharge, pas une opposition. Le veto vient **après**,
quand le recrutement proposé n'a pas de mandat complet.

## Asymétrie avec les autres gates

Comparaison rapide avec les gates des autres domaines (cf.
`eight-domain-avengers-wheel.md`) :

| Domaine | Gates émis | DLQ ? |
|---|---|---|
| Growth | `GROWTH_READY` / `NEEDS_SIGNAL` / `BLOCKED_PROMISE` | Non (3ᵉ état = `BLOCKED_*`) |
| Sales | `SALES_READY` / `NEEDS_QUALIFICATION` / `BLOCKED_COMMITMENT` | Non |
| Product | `PRODUCT_READY` / `NEEDS_SCOPE` / `BLOCKED_DELIVERY` | Non |
| Ops | `LAUNCH_READY` (gate transverse) | Non |
| IT | `SYSTEM_READY` / `NEEDS_SYSTEM_OWNER` / `QUARANTINE` | Non (3ᵉ état = `QUARANTINE`) |
| Finance | `FINANCE_READY` / `NEEDS_MODEL` / `BLOCKED_LEAKAGE` | Non |
| **People** | **`ASSIGNED` / `NEEDS_OWNER` / `DLQ`** | **Oui** |
| Legal | `LEGAL_READY` / `NEEDS_REVIEW` / `BLOCKED_RISK` | Non |

People est **le seul domaine à émettre un 3ᵉ état qui n'est pas un
`BLOCKED_*` ou un `QUARANTINE`**. Cette asymétrie reflète la nature du
domaine : People **ne bloque pas**, People **constate l'absence**. Le
mandat qui ne peut pas être assigné va en DLQ, pas en blocage.

Conséquence opérationnelle : un `BLOCKED_*` des autres domaines est une
**opposition** (le domaine refuse de continuer). Un `DLQ` People est un
**constat** (People ne peut pas continuer). Les deux bloquent la chaîne,
mais par des mécanismes différents — et le Council doit traiter le
constat comme une **remontée d'information**, pas comme une opposition à
arbitrer.

## Anti-pièges

- **`NEEDS_OWNER` traité comme un blocage** — c'est un signal, pas un
  refus. Le domaine d'accueil peut continuer en mode `negotiation`.
- **`DLQ` traité comme une opposition People** — c'est un constat
  d'absence d'owner possible. Le Council ne peut pas *« passer outre »*
  un DLQ ; il peut seulement **escalader** ou **réallouer**.
- **Gates émis sans mandat vérifiable** — si People émet `ASSIGNED`
  sans que le mandat ait les trois champs, c'est un **veto auto-bloqué**
  par People sur lui-même. Le Council doit invalider le gate.
- **`NEEDS_OWNER` permanent** — un mandat qui reste `NEEDS_OWNER` sur
  plus d'un cycle 12WY est un signal que le scope n'est pas viable. À
  escalader B1 pour arbitrage North Star.

## Liens

- [[green-lantern-people-perimetre-frontieres]] — ce que les gates
  protègent
- [[green-lantern-people-veto-recrutement-sans-mandat]] — la différence
  entre gate et veto
- [[green-lantern-people-raci-transverse-jamais-A]] — comment People
  émet ces gates sans devenir Accountable
- [[b2-harmonization-matrix-exploitable]] — la matrice qui consomme les
  gates

## Note de confiance

**Confirmé par machine, à moitié reconstruit.** Les trois gates sont
cités verbatim dans `eight-domain-avengers-wheel.md`. Les déclencheurs
vérifiables sont **reconstruits** à partir de la notion de mandat
complet (veto People) et de la notion de charge tenable (pair-check #9).
La méthode de calcul de charge (≤ 1.0) est **projetée** depuis le
framework capacité classique — le canon V4 ne pose pas de formule.
L'asymétrie `DLQ` vs `BLOCKED_*` est une **observation** directement
vérifiable sur le tableau 8-domaines, pas une projection.