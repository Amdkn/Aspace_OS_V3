---
type: Concept
title: Cyborg ↔ Green Lantern — couplage People × IT sur la charge Kang Dynasty (6 agents × tenure × spécialité)
description: Green Lantern (People) cite un « couplage invisible People×IT » dans son rapport tour 1. Cyborg est C sur le pair-check #9 People→Tous. Concrètement : Kang Dynasty = 6 agents (Kang Prime, Iron Lad, Scarlet Centurion, Immortus, Victor Timely, Rama-Tut) avec chacun une spécialité, un horizon, et une charge. People doit *coordonner* la charge — pas *statuer* sur IT. Trois cas concrets où le couplage se manifeste, trois cas où il serait abusif.
tags: [cyborg, green-lantern, people, kang-dynasty, charge, tenure, couplage-invisible, pair-check-9]
generated: { by: minimax-m3, at: 2026-08-19T04:40:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T04:40:00Z }
sources:
  - id: cyborg-domain
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-domain-it-perimetre-frontieres.md"
    title: Cyborg (IT) — périmètre et trois frontières
    last_modified: 2026-08-19
  - id: cyborg-pair-checks
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-pair-checks-product-it-fantastic-four.md"
    title: Cyborg pair-checks — #4 (A) et chaîne Product→IT→Ops
    last_modified: 2026-08-19
  - id: b2-pair-raci
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang — Cyborg C sur #9 People→Tous
    last_modified: 2026-08-19
  - id: green-lantern-couplages-invisibles
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-couplages-invisibles-people-it.md"
    title: Green Lantern — couplages invisibles People × IT / Legal / Finance / Growth
    last_modified: 2026-08-19
  - id: b3-roster-kang
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B3_Warp_Core_Execution/05_IT_Cyborg_KangDynasty/01_B3_AGENT_ROSTER.md"
    title: B3 Agent Roster IT / Kang Dynasty — 6 charges + escalation rule
    last_modified: 2026-05-27
okf_version: "0.2"
---

# Cyborg ↔ Green Lantern — couplage People × IT

## Le couplage canonique People × IT transverse

`green-lantern-couplages-invisibles-people-it.md` (rapport Green
Lantern tour 1) cite explicitement *« couplages invisibles People
× IT »* parmi les 4 couplages hors matrice canonique (avec Legal,
Finance, Growth). Le RACI par rang place Cyborg **C** sur le
pair-check #9 People → Tous (transverse).

**Concrètement** : Kang Dynasty = 6 agents avec chacun une
spécialité, un horizon, et une charge. Green Lantern doit *coordonner*
la charge — pas *statuer* sur IT. Cyborg doit *consulter* Green
Lantern quand la charge change — pas *demander une autorisation*.

C'est un couplage **invisible** parce que la matrice d'harmonisation
ne le pose pas explicitement. Mais le triplet 21 (Cyborg pairedWith
Kang Dynasty) + le RACI #9 (Cyborg C) + la pratique People =
*coordination de charge* rendent le couplage opérationnel.

## Kang Dynasty — 6 agents, 6 charges, 6 profils

`01_B3_AGENT_ROSTER.md` pose 6 charges canoniques :

| B3 agent | Spécialité | Horizon | Charge type (estimée) |
|---|---|---|---|
| **Kang Prime** (lead) | Architecture, orchestration | H10 | Lead infra, 80% disponibilité |
| **Iron Lad** | Provisioning, scripts bootstrap | H3 | Greenfield, 60% disponibilité |
| **Scarlet Centurion** | Sécurité réseau, firewall, SSL/TLS | H30 | Spike, 40% disponibilité |
| **Immortus** | Long-term planning, capacity | H90 | Legacy, 30% disponibilité |
| **Victor Timely** | Time-boxing, CI/CD | H3 | Frontier feature, 70% disponibilité |
| **Rama-Tut** | Backup, disaster recovery | H90 | Backup/review, 30% disponibilité |

**Note** : charge type et disponibilité sont **projetées** depuis
la doctrine IT dispatch + le rôle canonique — pas mesurées en cycle.
Le Ownerbook T1 DoD-1 attend *« ≥7 agents par squad »* mais Kang
Dynasty roster OMK liste 6 charges, ce qui crée une **asymétrie**
constante (cf. rapport tour 1 *« divergence X-Men 8 (triplet 15) vs
~7 (fifty-three-b3-agent-roster) non arbitree »*).

## Trois cas concrets où le couplage People × IT se manifeste

### Cas 1 — Mission IT longue (migration infra 12 semaines)

Une mission IT qui mobilise Kang Dynasty à plein temps (ex :
migration infra d'On Premise vers Cloud, projet Solaris AaaS).
**Le RACI** :

- Cyborg : **A** (Accountable) sur la décision IT.
- Kang Dynasty : **R** (Responsible) sur l'exécution.
- Green Lantern : **C** (Consulted) sur la charge.
- Summers (B1) : **I** (Informed) sur l'impact org.

Green Lantern consulte Cyborg sur 4 dimensions :

1. **Charge** — combien d'heures-agent sur 12 semaines ? Kang Prime
   80% × 12 = 384 h, Iron Lad 60% × 12 = 288 h, etc.
2. **Tenure** — les 6 agents sont-ils *disponibles* sur 12 semaines ?
   (pas en burnout, pas en mission ailleurs, pas en formation).
3. **Spécialité** — la mission IT exige quelle spécialité ?
   (security, legacy, refactor, etc.)
4. **Séquençage** — la mission peut-elle être séquencée pour
   éviter le burnout ? (ex : 4 sprints × 3 semaines, avec rotation).

**Test concret** : Green Lantern propose un plan de charge
*« Kang Prime 100% × 12 semaines »*. Cyborg accepte ou refuse selon
la capacité réelle — mais **Cyborg ne décide pas seul** du plan de
charge, parce que People coordonne, IT statue sur la faisabilité
technique.

### Cas 2 — Burnout agent Kang Dynasty

Un agent Kang Dynasty (ex : Scarlet Centurion, sécurité réseau) montre
des signes de burnout (charge >80% sur 3 mois, incidents qualité,
absences répétées). **Le RACI** :

- Cyborg : **A** sur l'arbitrage IT (peut-on alléger la charge de
  Scarlet Centurion ?).
- Green Lantern : **R** sur le plan de charge (peut-on réaffecter
  Scarlet Centurion sur autre chose ?).
- Kang Dynasty : **C** sur la faisabilité (peut-on basculer
  Scarlet Centurion vers un autre B3 ?).
- Summers (B1) : **I** sur l'impact People (burnout = risque RH).

**Test concret** : Scarlet Centurion est à 90% sur 3 mois. Cyborg
arbitre *« mission sécurité pause 2 semaines »* ; Green Lantern
arbitre *« Scarlet Centurion en formation pendant la pause »*.
C'est **deux arbitrages couplés**, pas un.

### Cas 3 — Recrutement Kang Dynasty 7e agent

Le Ownerbook T1 attend ≥7 agents par squad. Kang Dynasty a 6.
**Faut-il recruter un 7e agent** ? **Le RACI** :

- Green Lantern : **A** sur le recrutement People (mandat humain,
  grille de mandat, etc. — cf. veto Green Lantern *« recrutement
  sans mandat »*).
- Cyborg : **C** sur la fiche de poste IT (quelle spécialité manque ?
  quel horizon ? quel couplage avec les 6 existants ?).
- Kang Dynasty (Kang Prime) : **R** sur l'intégration (briefing,
  premier JTBD).
- Summers (B1) : **I** sur l'impact org.

**Test concret** : Kang Dynasty manque un agent *« Backup / DR
spécialiste »* (Rama-Tut est à 30% seulement). Green Lantern propose
un recrutement. Cyborg statue *« OK, c'est cohérent avec la charge
et la spécialité »*. Mais c'est Green Lantern qui signe le mandat,
pas Cyborg.

## Trois cas d'abus du couplage People × IT

### Abus 1 — Green Lantern qui statue sur la faisabilité IT

Green Lantern qui impose *« Cyborg doit livrer la migration en 8
semaines, pas 12 »*. C'est People qui *statue* sur IT. Mais le RACI
est clair : Cyborg A sur la décision IT, Green Lantern C sur la
charge. **Green Lantern consulte, Cyborg tranche.**

**Test concret** : la décision technique est-elle People ou IT ?
Si technique → Cyborg tranche. Si People → Green Lantern tranche.

### Abus 2 — Cyborg qui refuse la coordination People

Cyborg qui dit *« Green Lantern n'a pas à connaître ma charge
Kang Dynasty »*. C'est Cyborg qui *ignore* le couplage People. Mais
le RACI #9 est explicite : Cyborg est C, Green Lantern coordonne.
**Cyborg partage sa charge, Green Lantern coordonne.**

**Test concret** : la mission IT impacte-t-elle un autre domaine
que IT ? Oui → Green Lantern doit être consulté. Non → coordination
People peut être minimale.

### Abus 3 — Bypass mutuel sans consultation

Cyborg ET Green Lantern qui prennent une décision *« migration
infra + recrutement Kang 7e agent »* sans se consulter mutuellement.
C'est un **bypass du RACI** — chaque capitaine décide *pour soi*
sans Coordinated ni Consulted.

**Test concret** : la décision impacte-t-elle les deux domaines ?
Oui → les deux doivent être consultés. Non → un seul décide.

## La règle de résolution pratique

Cinq issues possibles, par ordre de fréquence :

1. **Mission séquencée** (Cas 1) — Cyborg accepte la charge avec
   séquençage People. **Résultat** : plan de charge validé
   conjointement, RACI respecté.
2. **Mission allégée** (Cas 2) — Cyborg statue *« pause technique »*,
   Green Lantern statue *« pause People »*. **Résultat** : double
   pause alignée, RACI respecté.
3. **Recrutement lancé** (Cas 3) — Green Lantern signe le mandat,
   Cyborg accepte la fiche de poste. **Résultat** : recrutement
   Kang 7e, RACI respecté.
4. **Conflit escaladé** — Cyborg et Green Lantern ne s'accordent
   pas sur la charge. **Résultat** : B2 Council arbitre, RACI
   respecté.
5. **Mission refusée par Cyborg** — la charge est incompatible
   avec la disponibilité Kang. **Résultat** : B1 Summers tranche
   (priorisation), RACI respecté (Cyborg A sur la décision finale).

## La chaîne canonique People → IT → Ops (Batman)

Le couplage People × IT *ne s'arrête pas* à Green Lantern ↔ Cyborg.
Il *s'étend* à Batman (Ops) via la chaîne Product → IT → Ops
(cf. [[cyborg-pair-checks-product-it-fantastic-four]]).

```
Green Lantern (People, C sur charge)
       │
       └──> Cyborg (IT, A sur faisabilité)
              │
              └──> Batman (Ops, A sur procédure)
                     │
                     └──> Fantastic Four (B3 Ops)
```

**Lecture** : une décision People × IT a des *conséquences Ops*
même si Batman n'est pas dans la décision initiale. La remontée
People → IT → Ops est *transverse*, pas isolée.

**Conséquence opérationnelle** : un arbitrage People × IT qui
ignore Batman est *incomplet*. Si la décision touche la procédure
Ops (runbook, escalation), Batman doit être C — pas I.

## Le cas spécial — 7e agent Kang Dynasty (Ownerbook T1)

Le Ownerbook T1 attend ≥7 agents par squad. Kang Dynasty roster
OMK en a 6. **Trois lectures** :

1. **Kang Dynasty incomplet** — le Ownerbook n'est pas atteint pour
   IT. Recrutement nécessaire.
2. **Roster OMK stale** — le roster OMK date 2026-05-27 et n'a pas
   été révisé. Le compte réel est peut-être 7+ aujourd'hui.
3. **Compte assertif vs calculé** — `fifty-three-b3-agent-roster.md`
   note *« Le nombre 53 est assertif, pas calculé. Ownerbook T1 DoD-1
   attend "≥7 agents par squad" sans donner le total cible »*.

**Recommandation** : ne pas recruter un 7e agent Kang Dynasty sur
la base d'un compte OMK potentiellement stale. **Vérifier d'abord** :
`find .claude/agents -name 'b3-*kang*' -o -name 'b3-*cyborg*' | wc -l`.
Si 6 → Ownerbook T1 manque. Si 7+ → roster OMK stale.

**Statut** : cette vérification est **bloquée en attente**
(commande non exécutée dans le corpus visible).

## Anti-pièges spécifiques People × IT

- **Cyborg qui absorbe le People.** IT ne recrute pas, People
  recrute. Si Cyborg signe un mandat People, c'est un abus.
- **Green Lantern qui absorbe l'IT.** People ne statue pas sur la
  faisabilité technique. Si Green Lantern signe un arbitrage IT,
  c'est un abus.
- **Charge = disponibilité.** La charge d'un agent n'est pas sa
  disponibilité. Un agent à 60% de charge peut être à 100%
  disponible (charge faible mais constante). Inversement.
- **RACI = hiérarchie.** RACI n'est pas hiérarchie. Cyborg A sur
  la décision IT ≠ Cyborg supérieur à Green Lantern. A = décide,
  C = consulte, pas plus.
- **Couplage transverse = escalade B1.** Le couplage People × IT
  *peut* escalader B1 si Summers tranche la priorisation, mais
  ce n'est *pas* l'issue par défaut. Le B2 Council arbitre d'abord.

## Liens

- [[cyborg-domain-it-perimetre-frontieres]] — le périmètre IT
- [[cyborg-pair-checks-product-it-fantastic-four]] — RACI #4 et chaîne Ops
- [[green-lantern-couplages-invisibles-people-it]] — couplages People × IT (Green Lantern)
- [[b2-pair-check-raci-by-rank]] — RACI par rang
- [[b2-council-arbitrage-rule]] — quand le Council arbitre

## Note de confiance

**Confirmé par machine** pour le RACI #9 (Cyborg C sur People→Tous)
et le roster Kang Dynasty 6 agents. Les trois cas concrets sont
**projetés** depuis le triplet 21 + le RACI + la pratique People =
*coordination de charge*. Les trois cas d'abus sont **reconstruits**
depuis la matrice d'harmonisation. La règle de résolution pratique
est **mon raisonnement** par combinaison RACI + doctrine People. La
chaîne People → IT → Ops (Batman) est **reconstruite** depuis la
chaîne Product → IT → Ops (cf. rapport Batman). Le compte Kang
Dynasty 6 vs Ownerbook T1 ≥7 reste **non arbitré**.
