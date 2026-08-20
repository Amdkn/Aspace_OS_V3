---
type: Concept
title: Doctrine D7 — mandat B1 sans acceptance check sous 24h est STALE
description: Doctrine verrouillée D7 qui ferme le trou entre `b1-mandate-packet-spec` (émission) et `b1-mandate-acceptance-check` (verrou 24h) : un mandat B1 sans acceptance check B2 sous 24h est marqué STALE, et entre dans le cycle de rollover comme dette reconnue (cf. `b1-cycle-rollover-protocol.md`).
tags: [b1, doctrine, d7, mandate, stale, acceptance, rollover]
generated: { by: minimax-m3, at: 2026-08-19T03:50:00Z }
verified:
  - { by: process:synthese-pulse-b1-tour-3, at: 2026-08-19T03:50:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: b1-mandate-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-mandate-packet-spec.md"
    title: B1→B2 Mandate Packet Spec (concept tour 1)
    last_modified: 2026-08-19
  - id: b1-mandate-acceptance-check
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-mandate-acceptance-check.md"
    title: B1 Mandate Acceptance Check (concept tour 2)
    last_modified: 2026-08-19
  - id: b1-cycle-rollover-protocol
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-cycle-rollover-protocol.md"
    title: B1 Cycle Rollover Protocol (concept tour 2)
    last_modified: 2026-08-19
  - id: b1-success-signal-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-success-signal-spec.md"
    title: B1 Success Signal Spec (concept tour 2)
    last_modified: 2026-08-19
  - id: d4-canon
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/runbooks/runbook-D-repositories.md"
    title: Runbook D — doctrine D4 append-only (référence)
    last_modified: 2026-07-15
okf_version: "0.2"
---

# Doctrine D7 — mandat B1 sans acceptance check sous 24h est STALE

D4 (append-only) et D6 (no-self-contradiction) sont les deux doctrines
verrouillées posées dans le canon OMK (cf. `omk-business-os.md` §Doctrine).
Ce concept pose une **troisième doctrine verrouillée — D7 — qui
ferme un trou** entre deux concepts B1 :

- `b1-mandate-packet-spec.md` (tour 1) — la grammaire d'émission d'un
  mandat B1→B2.
- `b1-mandate-acceptance-check.md` (tour 2) — le verrou d'acceptance
  par les capitaines B2 destinataires en 24h.

Le trou : entre l'émission et l'acceptance, **rien ne force le passage**.
Un mandat B1 peut rester en suspens — émis, pas accepté — sans que
rien ne le signale. C'est un mandat **fantôme** : il existe dans le
handoff queue, il consomme un slot, il n'est pas exécuté.

D7 corrige : un mandat sans acceptance check sous 24h est **STALE**.

## Le besoin — un mandat fantôme est une dette

Trois symptômes d'un mandat fantôme :

1. **Slot consommé.** Le handoff queue B1 (cf.
   `00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` §flux) a un nombre fini de
   slots par cycle. Un mandat fantôme en bloque un, sans qu'aucune
   squad B3 ne travaille dessus.
2. **B2 captain non sollicité.** Le captain destinataire ignore qu'il a
   un mandat en attente. S'il ne lit pas le handoff queue, il passe à
   côté pendant 12 semaines — jusqu'au rollover, où le mandat sera
   marqué `declared not delivered`.
3. **B1 re-émet sans savoir.** Si B1 ne voit pas le mandat fantôme,
   il peut émettre un nouveau mandat sur le même intent, créant un
   doublon. Les deux mandates courent ensuite en parallèle.

D7 rend la staleté **visible** : un mandat sans acceptance check
sous 24h est marqué STALE, et le B1 director (Summer pour J01) en
est notifié.

## La règle D7

> **D7 — Stale Mandate.** Tout mandat B1→B2 émis (`b1-mandate-packet-spec`)
> dont aucun acceptance check (`b1-mandate-acceptance-check`) n'est
> enregistré sous 24h est marqué **STALE**. Le statut STALE est
> terminal pour le cycle en cours ; le mandat entre dans le rollover
> suivant comme **dette reconnue** (cf. `b1-cycle-rollover-protocol.md`).
> Toute exception à D7 est un amendement `B1-D7-WAIVER-YYYY-NN` signé
> B1 direction.

Trois corollaires :

- **24h est une borne dure, pas indicative.** Le captain qui prend 25h
  à attester a un mandat STALE — pas un mandat tardif. La raison :
  le silence 24h est en soi un signal (cf.
  `b1-mandate-acceptance-check.md` §4, issue `silence 24h = STALE`).
- **STALE n'est pas un échec B2.** C'est un signal de friction
  d'interface — le captain n'a pas attesté, mais le motif peut être
  légitime (indisponibilité, désaccord, mandat hors-scope). D7 marque
  la staleté, pas la faute.
- **STALE ne bloque pas l'émission.** B1 peut émettre un nouveau
  mandat sur un intent différent pendant que l'ancien est STALE —
  mais ne peut pas émettre un mandat doublon sur le même intent
  (anti-pattern #3 ci-dessous).

## Le format — `B1_STALE_YYYY-NN.md`

```yaml
stale_mandate_id: B1-STALE-YYYY-NN
issued_at: YYYY-MM-DDTHH:MM:SSZ
source_mandate: B1-B2-MANDATE-YYYY-NN
intended_captain: green-lantern | batman | flash | superman | john-jones | wonder-woman | cyborg | aquaman
acceptance_due_by: issued_at + 24h
acceptance_received_at: null  # ou timestamp si reçu hors-délai
status: STALE
cycle_at_stale: 12WY-YYYY-QN
rollover_target: 12WY-YYYY-QN+1  # où le mandat entre comme dette

# optionnel — motif déclaré par le captain ou B1
motif:
  - silence_24h
  - acceptance_refused
  - mandate_off_scope
  - captain_unavailable

# action obligatoire
next_action: |
  Réémission amendée (nouvel ID) OU abandon (route vers dossier
  parked-mandates/ avec raison explicite).
```

Ce fichier est append-only (D4) — il ne se réécrit pas, il s'ajoute
au dossier `70_Onthologies/pulse/b1/_stale/` (à créer au premier
mandat stale).

## Intégration avec le rollover 12WY

`b1-cycle-rollover-protocol.md` §3 sorties par Rock identifie 3
sorties possibles (Doctrine Area, Project gradué, dette reconnue). D7
ajoute une **4ᵉ catégorie implicite** dans la dette reconnue : les
mandats STALE du cycle qui doivent être **réémis ou abandonnés** au
cycle suivant.

Au rollover, le B1 director :
1. Liste tous les `B1-STALE-*.md` du cycle qui vient de clore.
2. Pour chacun, décide `reissue_amended` ou `abandon`.
3. Les `reissue_amended` reçoivent un nouveau `B1-B2-MANDATE-YYYY-NN+1`
   avec un intent éventuellement révisé à la lumière du silence 24h.
4. Les `abandon` sont routés vers `parked-mandates/` avec une raison
   explicite — jamais supprimés silencieusement (D4).

## Anti-patterns

Quatre pièges :

1. **D7 comme punition.** D7 marque la staleté, pas la faute. Un
   captain B2 qui refuse un mandat pour cause de veto catalogue
   (`b1-mandate-acceptance-check.md` §4 issue `veto_opposed`) émet
   un signal plus utile que STALE — il faut le distinguer dans le
   log.
2. **B1 émet 10 mandates/jour.** Le 24h n'est pas un quota — c'est
   une friction d'interface. Si B1 sature le handoff, B2 ne peut pas
   attester, et la moitié des mandates deviennent STALE par
   sur-charge, pas par désaccord. D7 met en évidence ce risque ; il
   ne le corrige pas.
3. **B1 ré-émet un mandat STALE sans amendement.** Si B1 ré-émet le
   même mandat avec le même intent, B2 atteste en silence (pour éviter
   la staleté), et le cycle continue avec un mandat inadéquat. La
   parade : tout `reissue_amended` doit porter un champ `delta_vs_prior`
   qui documente la différence.
4. **Waiver D7 sans amendement doctrinal.** Si B1 waive la 24h pour
   un mandat spécifique, le waiver doit documenter la raison
   (disponibilité A0, force majeure, etc.). Sans raison, le waiver
   devient un canal de contournement.

## Liens

- [[b1-mandate-packet-spec]] — la grammaire amont
- [[b1-mandate-acceptance-check]] — le verrou 24h (face amont de D7)
- [[b1-cycle-rollover-protocol]] — la mécanique d'intégration au rollover
- [[b1-success-signal-spec]] — la règle de choix du signal
- [[b1-stop-conditions-escalier]] — l'escalier d'escalade, distinct de D7
- [[b1-macro-stewardship-cadence]] — la revue macro annuelle où D7
  apparaît comme axe « évolution doctrinale ».

## Sources

- `b1-mandate-packet-spec.md` — la grammaire d'émission.
- `b1-mandate-acceptance-check.md` §4 — l'issue `silence 24h = STALE`.
- `b1-cycle-rollover-protocol.md` §3 — la 3ᵉ sortie « dette reconnue ».
- `omk-business-os.md` §Doctrine — D4 et D6 comme précédents
  canoniques du verrouillage doctrinal.

## Note de confiance

**Confirmé par machine.** Les précédents D4 et D6 sont verbatim
`omk-business-os.md` §Doctrine. La face amont
(`b1-mandate-packet-spec`) et le verrou 24h
(`b1-mandate-acceptance-check`) sont des concepts B1 existants dans
ce dossier. Le format `B1-STALE-YYYY-NN.md` et la règle des 24h
comme borne dure sont **extrapolés** du verrou 24h. **Extrapole
fort** : la doctrine D7 elle-même. Elle n'existe pas dans le canon
lu. Sa ratification dépend d'un cas réel où un mandat OMK (T1, T2, ou
T3) reste sans acceptance check pendant 24h, et où B1 direction
tranche que STALE est le bon traitement ( vs par exemple une escalade
B2 Council). La doctrine est proposée, pas canonisée.