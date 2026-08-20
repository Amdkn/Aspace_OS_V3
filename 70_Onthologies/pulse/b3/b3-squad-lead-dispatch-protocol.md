---
type: Concept
title: B3 squad lead dispatch — du packet JTBD aux scrums quotidiens
description: Le squad lead est le pont entre le packet JTBD-001 (Area-level, 9 sections en prose) et les 5 scrums/semaine par agent B3 (5 champs chacun). Décomposition explicite à 4 étapes, ledger de dispatch, anti-patterns. Le squad lead est nommé `guardian_lead` dans le frontmatter du packet.
tags: [b3, squad-lead, dispatch, decomposition, jtbd, scrums, guardian-lead, dofld]
generated: { by: minimax-m3, at: 2026-08-19T03:00:00Z }
verified:
  - { by: process:lecture-b3-corpus-tour-1, at: 2026-08-19T03:00:00Z }
  - { by: process:synthese-pulse-b3-tour-2, at: 2026-08-19T03:00:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: jtbd-grammar
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/b3-jtbd-packet-grammar.md"
    title: JTBD-001 packet grammar — la grammaire B3 canonique
    last_modified: 2026-08-17
  - id: jtbd-reception
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-jtbd-packet-reception-checklist.md"
    title: JTBD packet — checklist de réception côté B3
    last_modified: 2026-08-19
  - id: cycle-scrums
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-cycle-scrums-five-per-week.md"
    title: B3 cycle — 5 scrums par semaine
    last_modified: 2026-08-19
  - id: peer-unblock
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-peer-unblock-protocol.md"
    title: B3 peer-unblock — l'escalader entre pairs avant d'escalader à B2
    last_modified: 2026-08-19
  - id: 53-roster
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/fifty-three-b3-agent-roster.md"
    title: 53 B3 Agent Roster
    last_modified: 2026-08-17
  - id: triplet-rhythm
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: v3-business triplets (lignes 7-13 — cascade B2 sprint -> B3 scrum)
    last_modified: 2026-08-17
okf_version: "0.2"
---

# B3 squad lead dispatch — du packet JTBD aux scrums quotidiens

> Le packet JTBD-001 est une **mission** ; le scrum est une **action
> exécutable**. Entre les deux, il y a un pont : le **squad lead**
> (`guardian_lead` dans le frontmatter du packet). Ce concept pose la
> mécanique explicite de la décomposition, parce que le corpus dit
> *qui* (le squad lead) mais pas *comment*.

## Le rôle du squad lead

Le squad lead est nommé dans le frontmatter du packet (`guardian_lead`
+ `supports`, §« Le Squad Roster prime sur les tags inline »). Son rôle
n'est **pas** d'exécuter le job — c'est de le **décomposer** pour que
les 4-7 agents du squad (cf. `fifty-three-b3-agent-roster.md`) puissent
chacun tenir leur cadence de 5 scrums/semaine sans se marcher dessus.

Trois propriétés qu'un squad lead doit tenir :

1. **Cohérence du périmètre** — la somme des scrums couvre le scope du
   packet, sans trou, sans doublon.
2. **Équilibre de charge** — pas un agent à 5 scrums/jour pendant que
   les autres sont à 0.
3. **Visibilité du blocker** — un blocker qui surgit sur un scrum
   remonte au squad lead, qui arbitre localement avant d'escalader à
   B2 (cf. `b3-peer-unblock-protocol.md`).

## Le dispatch en 4 étapes

### Étape 1 — Recevoir et valider le packet

Le squad lead applique la **même checklist** que la réception B3
(`b3-jtbd-packet-reception-checklist.md` §1-8), avec un regard
supplémentaire sur la **faisabilité** :

- Le job statement est-il reformulable en 1 phrase ? (champ 2)
- Le squad roster est-il aligné sur le roster canonique ? (champ 3)
- Les 3 sections ICP/VOC/painkiller sont-elles **suffisantes** pour
  amorcer la décomposition ? (champs 5-7)
- L'experiment RICE est-il chiffré ? (champ 6)
- L'`Acceptance <Hero>` est-elle encore non-cochée ? (champ 8)

Si une réponse est non, le squad lead **ne décompose pas** — il
applique `b3-hole-signaling-doctrine.md` et remonte à B2.

### Étape 2 — Mapper packet → agents par spécialité

Pour chaque bloc de travail identifié dans le packet, le squad lead
consulte le **DOFLD** (Domain-Owner-Federated Lookup Dispatch, cf.
`b3-cross-squad-dofld-protocol.md` en projet). Le lookup renvoie
l'agent du squad dont la spécialité matche le mieux.

Trois cas :

- **Spécialité intra-squad** : un B3 du squad a la charge canonique
  (ex. MrFantastic pour ProcessDesign sous Batman). Priorité haute.
- **Spécialité cross-squad** : la charge traverse un autre squad (ex.
  Legal review sous Aquaman). Lookup DOFLD cross-squad, demande
  d'appoint au squad lead Aquaman.
- **Spécialité vacante** : aucun agent n'a la spécialité. Le squad
  lead **ne fait pas** le mapping — il escalade à B2 avec un
  `HOLE_OTHER: skill_vacant`.

### Étape 3 — Décomposer en 5 scrums par agent, sur 1 sprint

Le sprint B2 dure 5 jours ouvrés (cf. `b3-cycle-scrums-five-per-week.md`
§« La cadence en pratique »). Pour chaque agent, le squad lead écrit
5 entrées de scrum — **une par jour**, dans l'ordre chronologique du
sprint. Chaque entrée pré-remplit 4 champs sur 6 :

| Champ | Pré-rempli par le squad lead ? | Source |
|---|---|---|
| `by` | oui | mapping étape 2 |
| `for` | oui | `source_rock` du packet |
| `action` | oui (verbe d'exécution) | décomposition scope packet |
| `signal` | non | l'agent le pose chaque jour |
| `proof` | non | l'agent le joint si `DONE` |
| `notes` | non | l'agent l'écrit si signal ≠ ON_TRACK |

Le squad lead **ne pré-remplit pas** le signal — c'est l'agent qui
constate l'état réel au soir de la journée.

### Étape 4 — Ouvrir le premier scrum, escalader le HOLE

L'ouverture du sprint est le premier scrum de chaque agent. Trois
issues possibles après l'étape 3 :

1. **Décomposition OK, scope couvert** — le squad lead notifie le B2
   sponsor que le dispatch est prêt, et l'agent ouvre son premier
   scrum avec `signal: ON_TRACK`.
2. **Décomposition partielle** — un bloc de scope ne trouve pas
   d'agent. Le squad lead applique `b3-hole-signaling-doctrine.md` :
   `HOLE_OTHER: skill_vacant` ou `HOLE_OTHER: scope_overflow`.
3. **Décomposition impossible** — le scope est trop flou pour être
   décomposé. Le squad lead **n'ouvre pas** le sprint, applique
   `HOLE_HYP` (painkiller hypotheses floues) ou `HOLE_GATE` (build
   gate manquant), et escalade à B2.

## Le ledger de dispatch

Chaque squad lead tient un fichier `DISPATCH.md` (au même niveau que
`SCRUMS.md` du squad) avec 5 champs par sprint ouvert :

```
DISPATCH_<sprint_id>_<YYYY-Wnn>
  packet_id:    <J01-B3-GROWTH-2026-001>
  squad:        <e.g. Guardians of the Galaxy>
  cycle:        <YYYY-Wnn, ISO week>
  mapping:
    - agent:   <b3-handle>
      by:      <spécialité canonique>
      scrums:
        - day:  1
          action: <verbe d'exécution + objet>
        - day:  2
          action: ...
        ...
        - day:  5
          action: ...
  status:       OPEN | DRAGGED | CLOSED
  blockers:     [<hole_id>, ...]  # si applicable
  close_at:     <YYYY-MM-DD>
```

Le ledger est lu par :

- le **B2 sponsor** (suivi temps réel des lead indicators, cf.
  `b2-b3-jtbd-handoff-contract.md` §« Rôle du capitaine B2 sponsor »)
- l'**agent relecteur** (vérification de la décomposition, cf.
  `agent-relecteur-mandat.md`)
- le **futur squad lead** (handoff de sprint en sprint)

## Le squad lead n'est pas un B2-bis

Trois choses que le squad lead **ne fait pas** :

1. **Ne ré-écrit pas le packet** — un scope qu'il juge mal foutu est
   un `HOLE_SIGNAL`, pas un patch silencieux.
2. **Ne déplace pas un B3 sur un autre squad** — c'est le B2
   sponsor + le B2 captain de l'autre squad qui arbitrent, pas le
   squad lead.
3. **Ne prolonge pas un sprint** — la durée du sprint est fixée par
   B2 (cf. `b2-b3-jtbd-handoff-contract.md` §« Cadre d'exécution »).
   Un sprint qui dérive est un `AT_RISK` escaladé, pas un sprint
   étendu.

## Anti-patterns

1. **Squad lead qui pré-remplit le `signal`** — le squad lead ne
   constate pas l'état, c'est l'agent. Un signal pré-rempli est une
   falsification.
2. **Mapping 1-pour-1 entre blocs de scope et agents** — un scope de
   3 blocs ne donne pas 3 agents ; il donne 5-7 scrums répartis sur
   les agents du squad selon leur spécialité.
3. **DISPATCH.md non écrit** — sans ledger, le B2 sponsor ne peut
   pas voir les lead indicators en temps réel. La décomposition est
   alors opaque, et le contrat B2→B3 n'est pas respecté.
4. **Premier scrum ouvert sans notify B2** — le B2 sponsor doit
   savoir que le dispatch est prêt avant que les agents ne
   commencent. Sinon le B2 ne voit que les `DONE` finaux, et le
   lead indicator n'est pas tenu.

## Lien avec les 5 méthodes autonomie-agents

| Méthode | Application au dispatch |
|---|---|
| Examen préalable | Avant d'envoyer le DISPATCH.md au B2, le squad lead lance un mini-examen (lecture du packet, vérif de cohérence). Pas de `tsc` ici — c'est un examen sémantique, pas mécanique. |
| Agent relecteur | Le DISPATCH.md est revu par un pair squad lead d'un autre squad (cross-check), ou par le B2 sponsor en mode relecteur. |
| Bacs à sable | Si deux squad leads dispatchent en parallèle sur un scope qui se chevauche, worktree partagé. À l'étape 1, cloisonnement par brief suffit. |
| Goodhart | Le compteur de scrums dispatchés n'est pas la métrique. Un dispatch qui couvre 100 % du scope avec 35 scrums est mieux qu'un dispatch qui couvre 80 % avec 50 scrums. |
| Tension Q/Q | Un dispatch minuté (1 h) avec 5 champs obligatoires est mieux qu'un dispatch improvisé qui rate la cohérence de scope. |

## Source du concept

- `b3-jtbd-packet-grammar.md` §« Le packet canon — section par section »
  — les 9 sections que le squad lead décompose.
- `b3-jtbd-packet-reception-checklist.md` §1-8 — la checklist
  ré-appliquée par le squad lead avec un regard faisabilité.
- `b3-cycle-scrums-five-per-week.md` §« Le format canonique d'un scrum »
  — les 6 champs dont 4 sont pré-remplis.
- `fifty-three-b3-agent-roster.md` §« Répartition par squad » — 4-7
  agents par squad, ce qui borne la taille du DISPATCH.md.
- `b2-b3-jtbd-handoff-contract.md` §« Rôle du capitaine B2 sponsor » —
  le B2 sponsor lit le DISPATCH.md, pas seulement le `DONE` final.

## Liens

- [[b3-jtbd-packet-reception-checklist]] — étape 1 du dispatch
- [[b3-cycle-scrums-five-per-week]] — étape 3 (5 scrums par agent)
- [[b3-peer-unblock-protocol]] — quand un agent remonte au squad lead
- [[b3-hole-signaling-doctrine]] — étape 4 quand un HOLE bloque l'ouverture
- [[b3-cross-squad-dofld-protocol]] — étape 2 quand le mapping est cross-squad
- [[b3-proof-return-contract]] — ce que le squad lead doit voir pour fermer le sprint
- [[b2-b3-jtbd-handoff-contract]] — le contrat B2 sponsor qui consomme le DISPATCH.md
- [[fifty-three-b3-agent-roster]] — la taille des squads (4-7 agents)

## Note de confiance

**Confirmé par machine.** Le rôle du squad lead est nommé dans le
fractal B1/B2/B3 (`fractal-b1b2b3-architecture.md` §« Le flux de
commandement »), et le champ `guardian_lead` est dans le frontmatter
canonique du packet. La décomposition en 4 étapes est **projetée** à
partir de la cascade E-Myth et du format 6-champ du scrum — c'est une
structuration de la pratique attendue, pas un canon publié ailleurs.

**Limite signalée** : aucun exemple réel de DISPATCH.md n'a été lu
dans le corpus. La structure 5-champs est **proposée**, pas
**validée** par un cycle B3 réel. Le critère de complétude sera
affiné au premier sprint documenté.
