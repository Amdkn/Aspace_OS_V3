---
type: Concept
title: B3 cross-squad DOFLD — l'annuaire qui rend la sollicitation traçable
description: Le DOFLD (Domain-Owner-Federated Lookup Dispatch) est l'annuaire qui permet à un B3 de trouver le bon pair cross-squad sans connaître tous les squads. Publié par chaque squad lead dans `01_B3_AGENT_ROSTER.md`, lu par les autres squads, format de lookup 4 champs, anti-patterns. Le DOFLD ne sert pas qu'à trouver : il rend la sollicitation visible au squad lead de l'agent ciblé.
tags: [b3, dofld, cross-squad, lookup, dispatch, federation, annuaire, audit]
generated: { by: minimax-m3, at: 2026-08-19T03:20:00Z }
verified:
  - { by: process:lecture-b3-corpus-tour-1, at: 2026-08-19T03:20:00Z }
  - { by: process:synthese-pulse-b3-tour-2, at: 2026-08-19T03:20:00Z }
sources:
  - id: peer-unblock
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-peer-unblock-protocol.md"
    title: B3 peer-unblock — l'escalader entre pairs avant d'escalader à B2
    last_modified: 2026-08-19
  - id: 53-roster
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/fifty-three-b3-agent-roster.md"
    title: 53 B3 Agent Roster
    last_modified: 2026-08-17
  - id: eight-domain
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel
    last_modified: 2026-08-17
  - id: dispatch
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-squad-lead-dispatch-protocol.md"
    title: B3 squad lead dispatch
    last_modified: 2026-08-19
  - id: fracture
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — pair checks et red flags
    last_modified: 2026-08-17
okf_version: "0.2"
---

# B3 cross-squad DOFLD — l'annuaire qui rend la sollicitation traçable

> Le `b3-peer-unblock-protocol.md` mentionne le DOFLD en une ligne
> (*« pool B3 transverse (DOFLD = Domain-Owner-Federated Lookup
> Dispatch) »*). Ce concept **étend** le DOFLD en protocole complet :
> qui publie, qui lit, le format de lookup, les 4 cas d'usage, les
> anti-patterns. Le DOFLD est la **mémoire fédérée** des spécialités
> cross-squad.

## Pourquoi un annuaire, pas un bottin

Sans DOFLD, un B3 qui cherche un pair cross-squad a trois options,
toutes coûteuses :

1. **Demander à son squad lead** — mais le squad lead ne connaît
   pas forcément les spécialités des 7 autres squads (4-7 agents
   × 7 squads = 28-49 agents à tenir en tête).
2. **Contacter directement un agent qu'il « connaît »** — casse la
   trace d'audit (cf. `b3-peer-unblock-protocol.md` §« Anti-patterns
   3 »), et le squad lead de l'agent ciblé ne voit pas la
   sollicitation.
3. **Escalader à B2** — mais le B2 captain n'est pas l'annuaire ;
   c'est l'arbitre. L'escalader pour un lookup, c'est le
   surcharger.

Le DOFLD est la **mémoire partagée** qui tient à jour les
spécialités de chaque agent, versionnée, lisible par tous les
squads, et **tenue** par chaque squad lead pour son propre squad.

## Le format de lookup

Le DOFLD est une fonction de lookup, pas un annuaire statique. La
forme canonique :

```
DOFLD.lookup(<domaine_b2>, <besoin>) → [<b3_handle>, <squad>, <contact>, <hit_strength>]
```

Quatre champs en sortie :

1. `<b3_handle>` — l'identifiant canonique de l'agent (cf.
   `fifty-three-b3-agent-roster.md`).
2. `<squad>` — le squad d'appartenance (X-Men, Avengers, etc.).
3. `<contact>` — le canal de contact (page Notion AGENT.md, channel
   dédié, etc.).
4. `<hit_strength>` — `STRONG` | `MEDIUM` | `WEAK` — à quel point
   l'agent a la spécialité canonique.

**`hit_strength` est crucial.** Un `STRONG` signifie que l'agent
est dans le roster canonique avec la spécialité. Un `MEDIUM` signifie
que l'agent a déjà traité un cas analogue. Un `WEAK` signifie que
l'agent est dans un squad adjacent (ex. Aquaman pour une question
Legal touchant le squad Guardians).

## Qui publie, qui lit

### Publication

Chaque squad lead tient le DOFLD pour **son** squad dans
`01_B3_AGENT_ROSTER.md` (cf. `fifty-three-b3-agent-roster.md`
§« Le pattern de la fiche roster »). La structure d'entrée :

```
AGENT_<b3_handle>
  handle:       <b3-handle>
  squad:        <squad-marvel>
  b2_owner:     <captain>
  specialites:
    - <domaine>: <description en 1 ligne>
    - <domaine>: <description en 1 ligne>
  sister_canon: [<autre-agent>, <autre-agent>]  # pour la triangulation
  hit_strength_par_defaut: STRONG | MEDIUM
  last_updated: <YYYY-MM-DD>
```

### Lecture

Tous les squads lisent le DOFLD des autres squads. La lecture se
fait via un index consolidé, idéalement
`_doctrine/agents/dofld_index.md` qui agrège les 8 Roster files.

**Anti-pattern** : un B3 qui lit le Roster d'un autre squad en
direct sans passer par l'index. Si le Roster change (et il change —
un agent peut changer de spécialité sans changer de handle), le
lecteur en direct voit une version stale.

## Les 4 cas d'usage canoniques

### Cas 1 — Pair cross-squad pour un blocker technique

**Exemple** : un B3 sous Batman (Ops) qui bloque sur une question
cloud (le squad Cyborg IT a la spécialité). Le B3 fait
`DOFLD.lookup("IT", "cloud-migration")`, obtient
`[("Cyborg-7", "Kang Dynasty", "AGENT.md", STRONG)]`, et envoie
le ping pair (cf. `b3-peer-unblock-protocol.md`) à l'agent
**en citant le hit DOFLD** dans le champ `to:`.

### Cas 2 — Pair cross-squad pour une revue sémantique

**Exemple** : un B3 sous Flash (Product) qui livre une offre et
veut une relecture Legal avant envoi. Le B3 fait
`DOFLD.lookup("Legal", "offer-review")`, obtient
`[("Ajak", "Eternals", "AGENT.md", STRONG)]`, et envoie un ping
*« peer-relecteur mandat »* (cf. `agent-relecteur-mandat.md`).

### Cas 3 — Spécialité vacante, escalade B2

**Exemple** : un B3 sous Superman (Growth) qui cherche un pair pour
une question de **fiscalité US** (post-pivot US, cf.
`omk-business-os.md`). Le DOFLD lookup renvoie **vide** — la
spécialité n'est pas dans le roster. Le B3 ne fait **pas** un
mapping par défaut ; il applique
`b3-hole-signaling-doctrine.md` avec `kind: HOLE_OTHER: skill_vacant`
et escalade à B2.

### Cas 4 — Demande de renfort en cours de sprint

**Exemple** : un squad lead sous Aquaman (Legal) a 3 sprints
ouverts en parallèle, et doit **détacher** un de ses agents
(Eternals) sur un sprint sous Superman (Growth) pour une review
express. Le squad lead Aquaman consulte le DOFLD inverse (qui
cherche un Legal dans Growth ?) et découvre que la spécialité est
**vacante cross-squad**. Il remonte à B2 avec un
`HOLE_OTHER: squad_overload`.

## Le format du ping DOFLD

Quand un B3 envoie un ping pair cross-squad, le ping **doit**
citer le DOFLD lookup. Format étendu du pair-unblock :

```
SQUAD_UNBLOCK_REQUEST (cross-squad)
  from:          <b3-handle>  (ex. Rocket, sous Guardians)
  to:            <peer-handle>  (ex. Ajak, sous Eternals)
  dofld_lookup:  # 4 champs — la trace audit
    domaine:     <ex. "Legal">
    besoin:      <ex. "offer-review pré-envoi">
    resultat:    [{"handle": "Ajak", "squad": "Eternals", "hit": "STRONG"}]
  context:       <job_id + état>
  tried:         <ce qui a été tenté>
  blocked:       <pourquoi ça bloque>
  ask:           <ce qui est demandé>
```

**Sans `dofld_lookup` cité**, le ping est en AP9
(`b3-anti-patterns-catalogue.md` §AP9) — cross-squad contact sans
DOFLD.

## Le HIT_UPDATE — quand le résultat est faux

Un lookup peut renvoyer un résultat **incorrect** (l'agent n'a
plus la spécialité, ou est en congé). Le B3 qui s'en aperçoit
émet un `HIT_UPDATE` au squad lead de l'agent, dans un format
verrouillé à 3 champs :

```
HIT_UPDATE
  by:            <b3-handle>
  agent:         <b3-handle cité dans le DOFLD>
  expected:      <ce que le DOFLD promettait>
  observed:      <ce que le B3 a constaté>
  suggested:     <ex. "Mark MEDIUM instead of STRONG" | "Mark vacant">
```

Le squad lead de l'agent met à jour le Roster. Le HIT_UPDATE est
la **boucle de feedback** qui maintient le DOFLD honnête.

## Le DOFLD et la matrice d'harmonisation

`business-wheel-harmonization-matrix.md` pose 9 pair checks
cross-domaines. Quand un B3 émet `BLOCKED` à cause d'un pair
check qui ne passe pas, le DOFLD est l'outil qui **trouve** le
pair à solliciter — pas le B2 Council. L'escalade B2 vient
**après** que le pair a tenté et échoué, pas avant.

```
B3 émet BLOCKED (pair check rouge)
  → B3 consulte DOFLD pour le domaine adjacent
  → B3 envoie un ping pair cross-squad (cité DOFLD)
  → Pair répond (résout ou escalade)
  → Si non résolu : B3 escalade B2 avec le pair check + tentative pair
```

## Anti-patterns

1. **AP9 — Cross-squad contact sans DOFLD** (cf.
   `b3-anti-patterns-catalogue.md` §AP9). Le plus coûteux, parce
   qu'il casse la trace d'audit et le squad lead de l'autre squad
   ne voit pas la sollicitation.
2. **Lookup par défaut** — un B3 qui prend le **premier**
   résultat du DOFLD sans vérifier le `hit_strength`. Un
   `WEAK` doit être traité comme un **hit à confirmer**, pas
   comme une certitude.
3. **DOFLD stale non signalé** — un B3 qui voit un Roster daté
   de plus de 6 mois (cf. `fifty-three-b3-agent-roster.md` §«
   Cycle de mise à jour ») et qui ne fait pas de `HIT_UPDATE`
   quand il constate la staleur.
4. **Escalade B2 sans tentative DOFLD** — un B3 qui remonte à
   B2 *« je n'ai pas trouvé de pair »* sans avoir laissé de
   trace DOFLD. Le B2 ne peut pas distinguer *« pas de pair »*
   de *« pas cherché »*.
5. **DOFLD comme annuaire de personnes, pas de spécialités** —
   un Roster qui liste les agents sans leurs spécialités est
   inutilisable. Le format `specialites:` est obligatoire
   (cf. AGENT_<b3_handle> ci-dessus).

## Lien avec les 5 méthodes

| Méthode | Application au DOFLD |
|---|---|
| Examen préalable | Le squad lead qui met à jour son Roster passe un mini-examen (champs obligatoires, dates récentes). |
| Agent relecteur | L'agent relecteur d'un Roster vérifie que les `specialites:` sont alignées sur le packet JTBD-001 du squad (section `supports`). |
| Bacs à sable | Si deux squad leads éditent leur Roster en parallèle, cloisonnement par brief (chacun son Roster). |
| Goodhart | Le compteur de spécialités publiées n'est pas la métrique. Un Roster avec 5 spécialités STRONG vérifiées vaut mieux qu'un Roster avec 12 spécialités dont 8 sont WEAK non-vérifiées. |
| Tension Q/Q | Un DOFLD tenu à jour en continu (par HIT_UPDATE) est mieux qu'un DOFLD tenu par re-vague annuelle qui stale. |

## Source du concept

- `b3-peer-unblock-protocol.md` §« Le DOFLD — Domain-Owner-Federated
  Lookup Dispatch » — la première mention en 1 ligne.
- `fifty-three-b3-agent-roster.md` §« Le pattern de la fiche roster »
  — la structure `01_B3_AGENT_ROSTER.md` qui porte le DOFLD.
- `business-wheel-harmonization-matrix.md` §« Les 9 pair checks » —
  le contexte cross-squad que le DOFLD sert.

## Liens

- [[b3-peer-unblock-protocol]] — le ping pair qui cite le DOFLD
- [[b3-squad-lead-dispatch-protocol]] — étape 2 du dispatch utilise DOFLD
- [[b3-hole-signaling-doctrine]] — quand le DOFLD est vide (cas 3)
- [[b3-anti-patterns-catalogue]] — AP9 (cross-squad sans DOFLD)
- [[fifty-three-b3-agent-roster]] — la source du DOFLD
- [[eight-domain-avengers-wheel]] — les 8 domaines que DOFLD couvre

## Note de confiance

**Confirmé par machine.** Le DOFLD est nommé dans
`b3-peer-unblock-protocol.md`. La structure `AGENT_<b3_handle>`
est **projetée** à partir du format `01_B3_AGENT_ROSTER.md`
(cf. `fifty-three-b3-agent-roster.md` §« Le pattern de la fiche
roster »). Le format `HIT_UPDATE` est **projeté** à partir de
la pratique de feedback sur les Roster stale (cf.
`fifty-three-b3-agent-roster.md` §« Cycle de mise à jour » —
3 mois sans révision).

**Limite signalée** : aucun exemple réel de HIT_UPDATE n'a été
observé dans le corpus. La structure `_doctrine/agents/dofld_index.md`
(qui agrégerait les 8 Roster files) est **proposée**, pas
**existante**. La convention `hit_strength` à 3 valeurs (STRONG /
MEDIUM / WEAK) est **projetée** à partir de la pratique
d'incertitude dans les pair checks — à calibrer au premier HIT_UPDATE
réel.
