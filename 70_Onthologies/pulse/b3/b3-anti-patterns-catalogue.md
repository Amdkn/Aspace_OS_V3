---
type: Concept
title: B3 anti-patterns catalogue — 9 façons de trahir la doctrine sans le vouloir
description: Catalogue consolidé des 9 anti-patterns B3 les plus coûteux, dispersés dans les concepts antérieurs (réception, peer-unblock, hole-signaling, cycle-scrums, veto-signal, proof, dispatch, sprint-close, proof-return). Pour chaque : symptôme, détection, remède, source. Lit en 5 minutes, à consulter en ouverture de sprint.
tags: [b3, anti-patterns, catalogue, doctrine, discipline, escroquerie-silencieuse]
generated: { by: minimax-m3, at: 2026-08-19T03:15:00Z }
verified:
  - { by: process:lecture-b3-corpus-tour-1, at: 2026-08-19T03:15:00Z }
  - { by: process:synthese-pulse-b3-tour-2, at: 2026-08-19T03:15:00Z }
sources:
  - id: reception
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-jtbd-packet-reception-checklist.md"
    title: JTBD packet — checklist de réception côté B3
    last_modified: 2026-08-19
  - id: peer-unblock
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-peer-unblock-protocol.md"
    title: B3 peer-unblock
    last_modified: 2026-08-19
  - id: hole-signaling
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-hole-signaling-doctrine.md"
    title: B3 hole-signaling
    last_modified: 2026-08-19
  - id: cycle-scrums
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-cycle-scrums-five-per-week.md"
    title: B3 cycle — 5 scrums par semaine
    last_modified: 2026-08-19
  - id: veto-signal
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-veto-and-signal-vocabulary.md"
    title: B3 veto and signal vocabulary
    last_modified: 2026-08-19
  - id: proof
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-proof-path-4-formes.md"
    title: B3 proof path
    last_modified: 2026-08-19
  - id: dispatch
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-squad-lead-dispatch-protocol.md"
    title: B3 squad lead dispatch
    last_modified: 2026-08-19
  - id: sprint-close
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-sprint-close-mechanics.md"
    title: B3 sprint close
    last_modified: 2026-08-19
  - id: return-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-proof-return-contract.md"
    title: B3 proof return contract
    last_modified: 2026-08-19
okf_version: "0.2"
---

# B3 anti-patterns catalogue — 9 façons de trahir la doctrine sans le vouloir

> La doctrine B3 a 9 concepts publiés (cf. `b3-` au 2026-08-19). Chacun
> liste ses propres anti-patterns. Ce concept **consolide** les 9
> anti-patterns les plus coûteux, regroupés par symptôme. Lit en 5
> minutes ; à consulter en ouverture de sprint.

## Pourquoi un catalogue consolidé

Les 9 concepts B3 ont été produits en 2 tours. Chacun porte sa
propre liste d'anti-patterns, mais un B3 qui ouvre un sprint
n'a pas le temps de lire 9 fichiers. Le catalogue est un
**résumé exécutif** : un B3 qui voit un de ces 9 symptômes sait
quel concept ouvrir pour le remède.

Les 9 anti-patterns sont triés par **coût** (du plus coûteux au
moins coûteux), pas par ordre de concept source.

## AP1 — Combler un trou de paquet en silence

**Sources** : `b3-jtbd-packet-reception-checklist.md` §« Ce que le
B3 refuse d'inventer », `b3-hole-signaling-doctrine.md` §«
Anti-patterns 1 ».

**Symptôme** : le B3 reçoit un packet avec un champ manquant (ICP,
VOC, painkiller, lead/lag, gate) et **invente** une valeur plausible
pour ne pas déranger B2.

**Détection** : la valeur manquante a été **ajoutée** dans
`SCRUMS.md` ou dans le code livré, sans `HOLE_SIGNAL` correspondant.

**Coût** : le squad lead ou le B2 s'en aperçoit (plus tard), la
dette est plus grande que si le trou avait été signalé d'emblée,
et l'autorité d'arbitrage de B2 a été contournée.

**Remède** : `b3-hole-signaling-doctrine.md` — 4 champs
(`location`, `kind`, `impact`, `suggested_fix`), 4 états du cycle
de vie (OPEN / ACKNOWLEDGED / RESOLVED / WONT_FIX).

## AP2 — Émettre `DONE` sans bloc `delivery:` rempli

**Sources** : `b3-proof-path-4-formes.md` §« L'arbre de décision »,
`b3-proof-return-contract.md` §« Anti-patterns 1 ».

**Symptôme** : le B3 émet le signal `DONE` au B2 sponsor sans
joindre la preuve dans l'une des 4 formes canoniques.

**Détection** : le B2 sponsor voit passer un `DONE` sans
`delivery:` dans le format conjoint.

**Coût** : la livraison est **invisible** au B2. Le `READY` de la
gate suivante est bloqué, et le sprint suivant ne s'ouvre pas.

**Remède** : `b3-proof-return-contract.md` §« Le bloc delivery: » —
6 champs obligatoires, dont `proof_forms` (1-4 formes avec
`chemin` et `consommateur`).

## AP3 — Escalader à B2 sans tentative de pair-unblock

**Sources** : `b3-peer-unblock-protocol.md` §« Anti-patterns 1 ».

**Symptôme** : le B3 remonte *« bloqué sur X »* à B2 sans avoir
listé `tried` dans son ping pair.

**Détection** : le ping B2 ne porte pas de référence à un ping
pair préalable, ou le `tried` est vide.

**Coût** : le B2 peut refuser d'arbitrer et renvoyer au pair. Le
sprint perd une itération, et le signal de dépendance mal placé
dévalue le B3 aux yeux du B2.

**Remède** : `b3-peer-unblock-protocol.md` §« Le format canonique »
— 5 champs (`from`, `to`, `context`, `tried`, `blocked`, `ask`),
4 niveaux (pair / squad lead / DOFLD / B2 owner).

## AP4 — Inventer son propre vocabulaire de signal

**Sources** : `b3-veto-and-signal-vocabulary.md` §« Anti-patterns
1 ».

**Symptôme** : le B3 émet *« le job est en pause »* ou *« ça
avance à moitié »* en prose libre, au lieu de
`AT_RISK` / `BLOCKED` / `ON_TRACK` / `DONE`.

**Détection** : le `SCRUMS.md` contient des verbes d'état qui ne
sont pas dans le vocabulaire fermé.

**Coût** : le squad lead et le B2 owner ne peuvent pas tenir la
wheel sans ces 4 états (cf. veto-signal §« Le signal n'est pas
optionnel »). La wheel devient illisible.

**Remède** : `b3-veto-and-signal-vocabulary.md` §« Couche 3 » — 4
états, libellés en MAJUSCULES_SNAKE_CASE.

## AP5 — Batcher les scrums en fin de semaine

**Sources** : `b3-cycle-scrums-five-per-week.md` §« Anti-patterns
1 ».

**Symptôme** : *« J'ai fait 5 choses cette semaine »* écrites en
bloc le vendredi, au lieu de 5 scrums étalés sur 5 jours.

**Détection** : 5 entrées de `SCRUMS.md` à la même date, ou des
dates qui ne couvrent pas les 5 jours ouvrés.

**Coût** : la cadence est **structurelle**, pas **productiviste**
(cf. cycle-scrums §« Anti-patterns »). Un batch signale un drift
silencieux — le B3 n'a peut-être pas travaillé sur le sprint
pendant 4 jours, et le vendredi il reconstruit une histoire.

**Remède** : `b3-cycle-scrums-five-per-week.md` §« Le format
canonique d'un scrum » — un scrum par jour ouvré, format 6
champs.

## AP6 — DRAGGED classé CLEAN pour éviter le HOLD

**Sources** : `b3-sprint-close-mechanics.md` §« Issue 2 — DRAGGED »
et §« Anti-patterns 2 ».

**Symptôme** : le squad lead termine le sprint avec un scope
incomplet, mais classe `outcome: CLEAN` pour éviter un `HOLD` qui
ressemble à un échec.

**Détection** : `sprints_done: <N>` < `scrums_total: <N>` dans
`SPRINT_SUMMARY.md`, mais `outcome: CLEAN` sans `notes`
explicatif.

**Coût** : la dette s'accumule. Le squad lead finit par ne plus
signaler les dérives, et le B2 sponsor arbitre à l'aveugle.

**Remède** : `b3-sprint-close-mechanics.md` §« Anti-patterns 2 » —
le DRAGGED n'est pas un échec, c'est un **fait** à signaler. Le
B2 sponsor arbitre la suite.

## AP7 — Rendre `DONE` avec un `HOLE_OPEN` non résolu

**Sources** : `b3-hole-signaling-doctrine.md` §« Lien avec la
preuve et l'examen », `b3-proof-return-contract.md` §« Failure
mode 3 ».

**Symptôme** : le B3 émet `DONE` alors qu'un `HOLE_OPEN` est
encore dans `holes_open`. Le `DONE` est invalide.

**Détection** : `holes_open` est non vide dans le bloc `delivery:`.
Le bloc est rejeté par le B2 sponsor.

**Coût** : la livraison est rejetée, le sprint est re-classé
DRAGGED, et le B2 sponsor doit ré-arbitrer. L'agent relecteur
voit un faux `DONE` et signale.

**Remède** : `b3-hole-signaling-doctrine.md` §« Le cycle de vie
du trou » — un HOLE_OPEN est un `BLOCKED`, pas un `DONE`. Le B3
classe DRAGGED et laisse B2 arbitrer.

## AP8 — Fermer un sprint en silence (pas de SPRINT_SUMMARY)

**Sources** : `b3-sprint-close-mechanics.md` §« Anti-patterns 1 ».

**Symptôme** : le squad lead clôt mentalement le vendredi et passe
au sprint suivant, sans écrire `SPRINT_SUMMARY.md`, sans notifier
le B2 sponsor, sans archiver les preuves.

**Détection** : le `SPRINT_SUMMARY_<YYYY-Wnn>.md` n'existe pas
pour la semaine en cours, et le sprint suivant a déjà un
`DISPATCH.md`.

**Coût** : le sprint **n'a pas existé** aux yeux du système. La
trace disparaît, et la mémoire du squad ne capitalise pas.

**Remède** : `b3-sprint-close-mechanics.md` §« Le calendrier de la
close » — 6 étapes de 9h à 17h, 3 artefacts dus, signal
`SPRINT_CLOSED_<issue>` au B2 sponsor.

## AP9 — Cross-squad contact sans DOFLD

**Sources** : `b3-peer-unblock-protocol.md` §« Anti-patterns 3 ».

**Symptôme** : un B3 contacte directement un agent d'un autre
squad sans passer par le DOFLD, parce qu'il « connaît » l'agent.

**Détection** : le ping pair n'a pas de `DOFLD.lookup()` cité en
référence, et le squad lead de l'autre squad n'a pas vu la
sollicitation.

**Coût** : la trace d'audit est cassée, le squad lead de l'autre
squad ne voit pas la sollicitation, et le DOFLD n'est pas mis à
jour avec le retour d'expérience.

**Remède** : `b3-cross-squad-dofld-protocol.md` (concept en
projet) — le DOFLD est l'annuaire qui rend la sollicitation
traçable.

## Synthèse — la matrice anti-pattern / concept source

| AP | Concept source principal | Coût relatif |
|---|---|---|
| AP1 | hole-signaling-doctrine | Critique (autorité d'arbitrage contournée) |
| AP2 | proof-return-contract | Critique (livery invisible) |
| AP3 | peer-unblock-protocol | Élevé (perte d'itération) |
| AP4 | veto-and-signal-vocabulary | Élevé (wheel illisible) |
| AP5 | cycle-scrums-five-per-week | Moyen (drift silencieux) |
| AP6 | sprint-close-mechanics | Élevé (dette accumulée) |
| AP7 | hole-signaling + return-contract | Critique (faux DONE) |
| AP8 | sprint-close-mechanics | Élevé (mémoire perdue) |
| AP9 | cross-squad-dofld-protocol | Moyen (audit cassé) |

## Comment lire ce catalogue

**À l'ouverture d'un sprint** : lire les 9 symptômes en 5
minutes. Si l'un d'eux te tente, ouvrir le concept source pour le
remède.

**À la close d'un sprint** : vérifier que **son propre squad** n'a
pas produit un de ces 9 patterns. L'auto-revue prend 10 minutes
et évite une escalade B2.

**Au relecteur** : ce catalogue est l'inventaire à vérifier
systématiquement, en plus du mandat unique de
`agent-relecteur-mandat.md`.

## Anti-pièges du catalogue lui-même

- **Catalogue comme checklist de complaisance** — un squad qui
  coche *« j'ai évité les 9 AP »* sans les avoir vraiment
  cherchés est en AP6 (DRAGGED classé CLEAN). Le catalogue
  signale, il ne prouve pas.
- **Catalogue comme excuse à la paralysie** — un B3 qui passe
  plus de temps à chercher les 9 AP qu'à exécuter est en AP5
  (batcher en fin de semaine par prudence). Le catalogue sert
  l'exécution, pas l'inverse.

## Source du concept

- 9 concepts B3 publiés (`b3-` directory, 2026-08-19).
- `agent-relecteur-mandat.md` §« Liste, pas prose » — la
  discipline de format qui inspire ce catalogue.
- `b3-proof-return-contract.md` §« Failure mode 1-3 » — les
  failure modes B3 qui s'ajoutent aux anti-patterns分散.

## Liens

- [[b3-jtbd-packet-reception-checklist]] — AP1
- [[b3-proof-path-4-formes]] — AP2, AP7
- [[b3-peer-unblock-protocol]] — AP3, AP9
- [[b3-veto-and-signal-vocabulary]] — AP4
- [[b3-cycle-scrums-five-per-week]] — AP5
- [[b3-sprint-close-mechanics]] — AP6, AP8
- [[b3-hole-signaling-doctrine]] — AP1, AP7
- [[b3-proof-return-contract]] — AP2, AP7
- [[b3-squad-lead-dispatch-protocol]] — AP6, AP8 (côté squad lead)
- [[b3-cross-squad-dofld-protocol]] — AP9

## Note de confiance

**Confirmé par machine.** Les 9 anti-patterns sont **tous** cités
dans les 9 concepts B3 publiés. La consolidation est **mécanique**
— pas d'invention, juste un regroupement par symptôme.

**Limite signalée** : le coût relatif est **estimé**, pas mesuré.
Un cycle B3 réel documenté permettrait de recalibrer (par exemple,
AP5 (batcher) est peut-être moins coûteux en pratique qu'AP9
(DOFLD cassé) — la matrice sera affinée au premier sprint
documenté).
