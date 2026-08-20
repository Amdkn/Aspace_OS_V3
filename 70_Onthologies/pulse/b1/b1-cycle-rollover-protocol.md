---
type: Concept
title: B1 cycle rollover protocol — la mécanique de fin de 12WY
description: Le rollover 12WY est le moment où B1 fait son vrai travail : revue, accept/replace/geler, doctrine ou dette. Cinq étapes (revue, scan wheel, accept/replace/geler, log, communication) + trois sorties possibles (Doctrine, Project gradué, dette reconnue).
tags: [b1, 12wy, rollover, cycle, revue, accept, doctrine, dette]
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
  - id: twelve-weeks-year
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-twelve-weeks-year-cadence.md"
    title: B1 twelve-weeks-year cycle — la cadence qui rend B1 vivant
    last_modified: 2026-08-19
  - id: fractal
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/fractal-b1b2b3-architecture.md"
    title: Le fractal B1/B2/B3 — Areas perpétuelles vs Summer's Verse datées
    last_modified: 2026-08-17
  - id: b2-meso
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — le format canonique d'une décision B2
    last_modified: 2026-08-19
  - id: b1-cockpit
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/b1-direction-cockpit.md"
    title: B1 direction cockpit — North Star, 12WY, decision charter
    last_modified: 2026-08-17
okf_version: "0.2"
---

# B1 cycle rollover protocol — la mécanique de fin de 12WY

`b1-twelve-weeks-year-cadence.md` pose le 12WY comme **fréquence
d'horloge** de l'étage B1. Mais il décrit surtout le *pendant* du
cycle (3 rocks, 1/mois). Il ne dit pas ce qui se passe au **moment**
où le cycle finit. Or c'est précisément à ce moment que B1 fait son
travail le plus structurant : distinguer ce qui devient doctrine de ce
qui devient dette.

Sans protocole de rollover, le 12WY devient un calendrier (cf.
`b1-twelve-weeks-year-cadence.md` § anti-pièges) et la doctrine ne
durcit jamais.

## Les cinq étapes du rollover

Cinq étapes en séquence stricte. Le rollover dure entre 5 et 10 jours
ouvrés (sur un cycle de 12 semaines, c'est < 15% du temps — c'est un
investissement, pas une taxe).

### Étape 1 — Revue des 3 rocks

Pour chaque Rock actif du cycle qui finit :

- **Preuve collectée.** Le proof_expected du meso-decision-packet B2
  (cf. `b2-meso-decision-packet-spec`) est rassemblé en un dossier de
  rollover. B2 captain remet son rapport, B1 agrège.
- **Statut déclaré.** Trois valeurs possibles : `atteint`,
  `partiellement atteint`, `raté`. Pas de quatrième.
- **Motif consigné.** Pour tout statut ≠ `atteint`, le motif est écrit
  en une à trois phrases. Pas un roman, pas un silence.

### Étape 2 — Scan wheel 8-domain (immutable)

Le scan wheel tourne **avant** toute décision de accept/replace/geler,
parce que les Rocks ne sont qu'une lecture de la wheel. Si la wheel est
imbalanced, le statut des Rocks peut être techniquement `atteint` mais
structurellement trompeur (cf. `b1-wheel-imbalance-six-signes.md`).

Le scan produit un verdict :

- `wheel balanced` → continuer à l'étape 3 sans alerte.
- `wheel imbalanced` → alerte explicite, B1 consigne les 6 signes actifs
  (cf. `b1-wheel-imbalance-six-signes.md`).

### Étape 3 — Accept / Replace / Geler

Pour chaque Rock, B1 choisit une des trois issues :

| Issue | Définition | Conséquence cycle suivant |
|---|---|---|
| **Accept** | Le Rock a atteint son signal. La doctrine/le standard qu'il a instancié **reste**. | Le Rock devient Doctrine si Area, ou contributeur au Project gradué si Summer |
| **Replace** | Le Rock est partiellement atteint, ou le signal a glissé. B1 le **reformule** pour le cycle suivant. | Le Rock ancien est archivé dans le journal de rollover, le nouveau Rock prend sa place |
| **Geler** | Le Rock n'a pas sa place dans le cycle suivant — environnement changé, priorisation revue, ou wheel imbalance impose un gel. | Le Rock est archivé sans successeur. La raison du gel est documentée (pas de gel silencieux) |

**Une seule règle** : pas plus de 3 Rocks par cycle, peu importe l'issue.
Si B1 veut pousser un 4e Rock, il doit en geler ou en remplacer un
(extrapolation de `b1-twelve-weeks-year-cadence.md` § Pourquoi 3 rocks).

### Étape 4 — Log append-only

Toutes les décisions de l'étape 3 sont loguées dans un fichier
`B1_ROLLOVER_YYYY-QN.md`, **append-only** (D4) :

```yaml
rollover_id: B1-ROLLOVER-2026-Q4
cycle_in: 12WY-2026-Q3-Q4
cycle_out: 12WY-2026-Q4-Q1
decided_at: 2026-10-15T17:00:00Z
decided_by: <Jerry area | Summer project>

rocks:
  - rock_id: B1-1 (T1 People+Ops+Product)
    status: atteint | partiellement_atteint | raté
    issue: accept | replace | geler
    motif: "<une à trois phrases>"
    successor: B1-1' | null
  - rock_id: B1-2 (T2 Growth+Sales+Finance, pivot US)
    status: ...
    ...
  - rock_id: B1-3 (T3 Legal+R&D)
    status: ...
    ...

wheel_scan:
  verdict: balanced | imbalanced
  signs_active:
    - empty_domain | overloaded_domain | blocked_gate | product_only_drift | cross_domain_conflict | missing_proof

mandates_b1_emitted_next_cycle:
  - b1_b2_mandate_id: B1-B2-MANDATE-YYYY-NN
    ...
```

Le log est **public** (lu par A0 et les gatekeepers) et **immutable**.

### Étape 5 — Communication

Trois communications, dans cet ordre :

1. **Aux 8 capitaines B2.** Liste des mandates à ouvrir au cycle
   suivant, avec lien vers les Rocks retenus.
2. **À A0 Amadeus et aux gatekeepers Rick/Morty.** Résumé exécutif du
   rollover : 3 Rocks statut, wheel verdict, mandates émis, doctrine
   consolidée. Format : 1 page.
3. **Au B2 Council.** Roulement des arbitrages mésoperpétuels
   (`next_review` atteints, red flags actifs, vetos opposés).

## Les trois sorties possibles — Doctrine, Project gradué, dette reconnue

Le rollover produit l'une des trois sorties **par Rock** :

### Doctrine (Area perpetuelle)

Le Rock a atteint son signal, et la doctrine/le standard qu'il a
instancié est **réutilisable**. Conséquence : la doctrine remonte dans
l'Area macro (cf. `fractal-b1b2b3-architecture.md` §« Le fractal
compounds »). La wheel ne perd pas ce que le Rock a appris.

### Project gradué (Summer daté)

Le Rock a atteint son signal **et** le Project qui le portait graduate.
Conséquence : la doctrine produite **remonte à l'Area** (micro →
macro), et le Project bascule en `COMPLETE → ARCHIVED`. C'est le
**fractal compounds** dans sa forme la plus explicite.

### Dette reconnue (Rock raté, doctrine non produite)

Le Rock n'a pas atteint son signal. Trois issues possibles :

- **Rattrapage au cycle suivant** (replace avec motif *« rattrapage »*).
  Le Rock est reformulé, le motif de l'échec est la première
  contrainte du nouveau mandat.
- **Abandon accepté** (geler avec motif *« environnement changé »*).
  La dette est consignée : ce que le Rock visait n'a pas été produit,
  personne ne prétendra le contraire au cycle suivant.
- **Escalade A0** (geler avec motif *« North Star en jeu »*). La
  dette devient A0 ; B1 ne peut pas la gérer seul.

**Pas de quatrième issue.** Pas de *« on verra au prochain cycle »*
sans motif écrit. C'est exactement la dette silencieuse que le rollover
doit tuer.

## Anti-pièges

- **Rollover sans scan wheel.** Si B1 accepte/replace/geler sans scan,
  il risque de garder un Rock dont la wheel est imbalanced — c'est le
  cas du `product_only_drift` qui passe sous le radar.
- **Geler sans motif.** Le gel silencieux est l'anti-pattern majeur. Un
  Rock qui disparaît sans trace pollue le journal de rollover et rend
  impossible la revue de cycle en cycle.
- **Accept sans preuve.** Accepter un Rock dont le proof_expected est
  absent, c'est valider un voeu. La matrice d'harmonisation et le
  relecteur (cf. `agent-relecteur-mandat.md` du corpus autonomie-agents)
  sont là pour empêcher ça.
- **Communication seulement aux capitaines B2.** Oublier A0 et les
  gatekeepers, c'est priver la gouvernance de la trace. Le rollover
  sans lecture A0 est un rollover qui n'a pas de témoin.

## Sources

- `b1-twelve-weeks-year-cadence.md` — la cadence, le 3/12WY, la
  distinction Area perpetuelle vs Project gradué.
- `fractal-b1b2b3-architecture.md` — le fractal compounds, la montée
  Project → Area.
- `b2-meso-decision-packet-spec.md` — le format des proof_expected
  que B1 agrège au rollover.
- `b1-direction-cockpit.md` — l'index cockpit, le North Star 1Y/3Y/10Y.

## Liens

- [[b1-twelve-weeks-year-cadence]] — la cadence qui rend le rollover
  nécessaire
- [[b1-wheel-imbalance-six-signes]] — le scan de l'étape 2
- [[b1-mandate-packet-spec]] — la grammaire des mandates émis à l'étape 5
- [[b1-mandate-acceptance-check]] — le verrou de l'étape 5 côté B2
- [[b1-omk-t2-pivot-us-mandate]] — application au Rock B1-2 OMK T2
- [[b1-stop-conditions-escalier]] — quand un rollover escalade A0
- [[b1-four-jerry-portfolio]] — le rollover vu au niveau macro

## Note de confiance

**Confirmé par machine.** Les cinq étapes sont **extrapolées** à partir
du 12WY cadence + fractal compounds + decision charter — pas un
protocole nommé dans le canon. Les trois sorties (Doctrine, Project
gradué, dette reconnue) sont **reconstruites** à partir de la
distinction Area/Project du fractal. Le format YAML `B1_ROLLOVER_*.md`
est extrapolé du format `B1-B2-MANDATE-YYYY-NN`. Les seuils (5-10 jours
ouvrés, 15% du cycle) sont **motivationnels** — pas mesurés.