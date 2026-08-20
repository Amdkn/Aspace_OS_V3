---
type: Concept
title: B3 sprint close — la mécanique du vendredi, et ses trois issues
description: Le sprint B2 dure 5 jours ouvrés. Le vendredi (ou dernier jour ouvré) tient la close : 3 artefacts dus (SPRINT_SUMMARY, proof attachments, next-sprint trigger), 3 issues possibles (clean, dragged, cancelled), un signal `DONE` ou `AT_RISK` qui remonte au B2 sponsor. Anti-patterns typiques : sprint clos en silence, next-sprint non-triggeré, archive manquante.
tags: [b3, sprint, close, friday, summary, archive, done, cancel, drag]
generated: { by: minimax-m3, at: 2026-08-19T03:05:00Z }
verified:
  - { by: process:lecture-b3-corpus-tour-1, at: 2026-08-19T03:05:00Z }
  - { by: process:synthese-pulse-b3-tour-2, at: 2026-08-19T03:05:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: cycle-scrums
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-cycle-scrums-five-per-week.md"
    title: B3 cycle — 5 scrums par semaine
    last_modified: 2026-08-19
  - id: proof-path
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-proof-path-4-formes.md"
    title: B3 proof path — la preuve inspectable
    last_modified: 2026-08-19
  - id: veto-signal
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-veto-and-signal-vocabulary.md"
    title: B3 veto and signal vocabulary
    last_modified: 2026-08-19
  - id: handoff
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — quand une décision mésoperpétuelle devient un JTBD packet
    last_modified: 2026-08-19
  - id: triplet-b2-sprint
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: v3-business triplets (ligne 10 — VP cycle-hebdomadaire, lundi ouvre / vendredi clôt)
    last_modified: 2026-08-17
okf_version: "0.2"
---

# B3 sprint close — la mécanique du vendredi, et ses trois issues

> La doctrine B3 cycle pose *« 5 scrums/semaine, un par jour ouvré »*
> (cf. `b3-cycle-scrums-five-per-week.md`). Mais la **close** du
> sprint — ce qui se passe au-delà du 5ᵉ scrum — n'est pas documentée.
> Ce concept pose la mécanique du dernier jour ouvré et ses trois
> issues canoniques, parce qu'un sprint qui se termine sans close est
> un sprint dont personne ne sait s'il a été tenu.

## Pourquoi une close explicite

Le triplet v3 ligne 10 dit : *« le lundi ouvre le sprint, le vendredi
le clôt (tenu ou non, avec motif) »*. La close n'est pas un détail
administratif — c'est l'instant où :

- le **squad lead** consigne ce qui a été livré, et ce qui ne l'a pas
  été ;
- le **B2 sponsor** reçoit le statut final et arbitre la suite
  (next-sprint trigger ou rollback) ;
- la **mémoire du squad** archive le sprint pour les cycles à venir
  (recherche, post-mortem, calibration).

Un sprint qui se termine sans close est un sprint dont la trace
disparaît. Le `DONE` final ne suffit pas — il dit « ce scrum est
terminé », pas « ce sprint est terminé ».

## Les 3 artefacts dus à la close

### Artefact 1 — `SPRINT_SUMMARY.md`

Un fichier au même niveau que `SCRUMS.md`, nommé
`SPRINT_SUMMARY_<YYYY-Wnn>.md`, avec 7 champs :

```
SPRINT_SUMMARY_<YYYY-Wnn>
  sprint_id:    <B2-SPRINT-YYYY-NN>
  packet_id:    <J01-B3-<DOMAIN>-YYYY-NNN>
  squad:        <squad-marvel>
  cycle:        <YYYY-Wnn, ISO week>
  scrums_total:  <N>                # 5 par agent × N agents
  scrums_done:  <N_done>
  scrums_at_risk: <N_at_risk>
  scrums_blocked: <N_blocked>
  outcome:      CLEAN | DRAGGED | CANCELLED
  proof_paths:  [<path>, ...]       # chemins vers les 4 formes
  holes_open:   [<hole_id>, ...]    # HOLE non résolus à la close
  next_sprint:  TRIGGER | HOLD | ROLLBACK
  notes:        <1 paragraphe — ce qui a été appris>
```

### Artefact 2 — Preuves attachées

Les 4 formes canoniques de preuve (`b3-proof-path-4-formes.md`)
produites pendant le sprint sont **regroupées** dans un dossier
`proof/<YYYY-Wnn>/`, indexé par agent et par date. Le B2 sponsor
lit l'index, pas chaque fichier.

### Artefact 3 — Next-sprint trigger

Le sprint qui se termine **doit** déclencher le suivant, ou
explicitement demander un **HOLD** ou un **ROLLBACK**. Le squad lead
n'a pas le droit de terminer la close sans décision sur la suite.

## Les 3 issues canoniques

### Issue 1 — CLEAN

**Définition** : tous les scrums du sprint sont `DONE`, ou ont été
escaladés en HOLE résolu (`RESOLVED` ou `WONT_FIX`), et le `Acceptance
<Hero>` du packet est signé.

**Action** : `next_sprint: TRIGGER`. Le squad lead émet le signal
`SPRINT_CLOSED_CLEAN` au B2 sponsor, qui ouvre le sprint suivant dans
la journée.

### Issue 2 — DRAGGED

**Définition** : au moins un scrum est `AT_RISK` ou `BLOCKED` à la
close, sans escalade B2 formelle. Le sprint a produit, mais pas tout
ce qui était dans le scope.

**Action** : `next_sprint: HOLD`. Le B2 sponsor arbitre : soit
prolonger le scope incomplet dans le sprint suivant, soit re-scopé
pour accommoder la dette, soit escalader au B2 Council si la dérive
touche un pair check (cf. `business-wheel-harmonization-matrix.md`).

**Anti-pattern** : un sprint DRAGGED classé CLEAN par le squad lead
« pour ne pas déranger ». C'est l'anti-pattern du B3 qui comble un
trou en silence, transposé à l'échelle du sprint.

### Issue 3 — CANCELLED

**Définition** : un veto B2 a été posé pendant le sprint (cf.
`b3-veto-and-signal-vocabulary.md` §« Couche 1 »), ou un emergency
trigger B1 a stoppé net. Le sprint n'est pas mené à terme.

**Action** : `next_sprint: ROLLBACK`. Le B2 sponsor consigne le motif
du cancel, archive les artefacts produits jusqu'à l'arrêt, et
ré-arbitre le scope avant le prochain sprint.

## Le calendrier de la close

| Heure (jour 5) | Action | Owner |
|---|---|---|
| 09:00 | Le squad lead ouvre la close, vérifie que tous les scrums du jour 4 ont un signal. | squad lead |
| 10:00 | Chaque agent clôture son 5ᵉ scrum avec signal + preuve si `DONE`. | chaque agent |
| 11:00 | Le squad lead agrège dans `SPRINT_SUMMARY.md`. | squad lead |
| 14:00 | Le squad lead notifie le B2 sponsor avec `SPRINT_CLOSED_<issue>`. | squad lead |
| 15:00 | Le B2 sponsor arbitre `next_sprint`. | B2 sponsor |
| 16:00 | Si `TRIGGER`, le squad lead prépare le DISPATCH.md du sprint suivant. | squad lead |
| 17:00 | Archive `proof/<YYYY-Wnn>/` vers `archive/<YYYY>/<YYYY-Wnn>/`. | squad lead |

Cette cadence est **indicative** — l'important est que la close soit
**un événement** (pas une chute de sprint), avec un temps dédié et
des artefacts produits.

## Le `SPRINT_CLOSED_<issue>` — le signal formel de close

Le signal est émis par le squad lead au B2 sponsor, dans un format
fermé à 3 valeurs (cf. `b3-veto-and-signal-vocabulary.md` §« Couche 3 »
pour le format B3 → B2) :

```
SPRINT_CLOSED_<issue>
  by:          <squad-lead>
  sprint_id:   <B2-SPRINT-YYYY-NN>
  cycle:       <YYYY-Wnn>
  outcome:     CLEAN | DRAGGED | CANCELLED
  next_sprint: TRIGGER | HOLD | ROLLBACK
  proof_index: <path vers proof/<YYYY-Wnn>/index.md>
  holes_open:  [<hole_id>, ...]
```

Le B2 sponsor accuse réception dans la journée. Sans accusé, le
sprint n'est pas clos — il est **en attente de close**, statut que
le squad lead consigne dans `SPRINT_SUMMARY.md`.

## Anti-patterns

1. **Close en silence** — le squad lead clôt mentalement et passe au
   sprint suivant. Le `SPRINT_SUMMARY.md` n'est pas écrit, le B2
   sponsor n'est pas notifié, l'archive n'est pas faite. Le sprint
   **n'a pas existé** aux yeux du système.
2. **DRAGGED classé CLEAN** — pour éviter un HOLD qui ressemble à un
   échec. Conséquence : la dette s'accumule, et le squad lead finit
   par ne plus signaler les dérives.
3. **Next-sprint TRIGGER sans DISPATCH.md** — le sprint suivant
   s'ouvre, mais sans décomposition préalable. Les agents ouvrent
   des scrums « au feeling », et le squad lead ne peut pas tenir
   le suivi de cohérence de scope.
4. **Archive manquante** — `proof/<YYYY-Wnn>/` n'est pas déplacé
   vers `archive/`. Les preuvres s'accumulent, le squad lead
   ne peut plus retrouver un sprint passé, et l'agent relecteur
   n'a plus de matériau pour les revues rétrospectives.
5. **`SPRINT_CLOSED_CLEAN` avec un `HOLE_OPEN`** — un HOLE non
   résolu à la close invalide le `CLEAN`. Le squad lead doit
   classer DRAGGED et arbitrer avec B2.

## Lien avec l'agent relecteur

L'agent relecteur (`agent-relecteur-mandat.md`) lit
`SPRINT_SUMMARY.md` et l'index `proof/<YYYY-Wnn>/`. Son mandat
s'étend à la **close** : il signale les DRAGGED classés CLEAN, les
CLEAN avec HOLE_OPEN, les CANCELLED sans motif, et les archives
manquantes.

## Lien avec les 5 méthodes

| Méthode | Application à la close |
|---|---|
| Examen préalable | Avant d'émettre `SPRINT_CLOSED_<issue>`, le squad lead lance un mini-examen sur le SPRINT_SUMMARY (champs obligatoires, cohérence outcome/next_sprint). |
| Agent relecteur | Revue du SPRINT_SUMMARY.md et de l'index proof/ après chaque close. |
| Bacs à sable | Si deux squads clôturent en parallèle, cloisonnement par brief suffit (chacun son SPRINT_SUMMARY). |
| Goodhart | Le compteur de `SPRINT_CLOSED_CLEAN` n'est pas la métrique. Un sprint DRAGGED avec un HOLE signalé est **mieux** qu'un sprint CLEAN de complaisance. |
| Tension Q/Q | Une close minutée (1 h) avec 3 artefacts est mieux qu'une close improvisée qui rate l'archive. |

## Source du concept

- `b3-cycle-scrums-five-per-week.md` §« Pourquoi 5, pas 7 » — la
  semaine 5 jours ouvrés, vendredi close.
- `triplet v3 ligne 10` — *« le lundi ouvre le sprint, le vendredi
  le clôt (tenu ou non, avec motif). »*
- `b3-proof-path-4-formes.md` §« L'arbre de décision » — les 4
  formes à archiver.
- `b2-b3-jtbd-handoff-contract.md` §« Rôle du capitaine B2 sponsor »
  — le destinataire du SPRINT_CLOSED.

## Liens

- [[b3-cycle-scrums-five-per-week]] — les 5 scrums qui précèdent la close
- [[b3-proof-path-4-formes]] — les preuves à archiver
- [[b3-veto-and-signal-vocabulary]] — SPRINT_CLOSED, signal B3 → B2
- [[b3-squad-lead-dispatch-protocol]] — le DISPATCH.md du sprint suivant
- [[b3-hole-signaling-doctrine]] — les HOLE_OPEN qui invalident un CLEAN
- [[b2-b3-jtbd-handoff-contract]] — ce que le B2 sponsor fait du signal

## Note de confiance

**Confirmé par machine.** Le triplet v3 ligne 10 pose la close
hebdomadaire. La structure `SPRINT_SUMMARY.md` à 7 champs est
**projetée** à partir de la pratique scrum et du format
`SCRUM_YYYY-MM-DD` (6 champs) — c'est une structuration de la
pratique attendue, pas un canon publié ailleurs.

**Limite signalée** : aucun exemple réel de `SPRINT_SUMMARY.md` n'a
été lu dans le corpus. La cadence horaire de la close (9h-17h) est
**proposée** pour un cycle ouvré standard, et doit être calibrée au
premier sprint réel documenté.
