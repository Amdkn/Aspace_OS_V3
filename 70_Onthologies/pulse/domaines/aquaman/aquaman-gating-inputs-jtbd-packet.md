---
type: Concept
title: Aquaman — proposition d'un champ `gating_inputs:` dans le contrat B2→B3, justifiée par les 4 formes reçues
description: Le contrat B2→B3 actuel pose 7 champs (3 côté B2, 4 côté B3) mais aucun ne couvre les inputs amont dont Aquaman a besoin pour produire. Les 4 formes reçues par Aquaman (Flash feature spec, Superman claim draft, JohnJones deal structure, Cyborg privacy spec) sont des gating_inputs explicites. Proposition : ajouter un champ `gating_inputs:` au gabarit, applicable à tous les domaines qui reçoivent des inputs amont, avec 3 cas d'application légitime et 3 cas d'abus. Tour 3 transforme une remontée ouverte depuis tour 2 en proposition de champ générique.
tags: [b2, b3, contract, gating-inputs, jtbd, packet, amendment, aquaman]
generated: { by: minimax-m3, at: 2026-08-19T05:45:00Z }
verified:
  - { by: process:lecture-canon-aquaman-tour-3, at: 2026-08-19T05:45:00Z }
sources:
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — quand une décision mésoperpétuelle devient un JTBD packet
    last_modified: 2026-08-19
  - id: b3-jtbd-reception
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-jtbd-packet-reception-checklist.md"
    title: B3 JTBD packet reception checklist
    last_modified: 2026-08-19
  - id: aquaman-jtbd
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-jtbd-emit-receive.md"
    title: Aquaman catalogue JTBD émis et reçus
    last_modified: 2026-08-19
  - id: aquaman-defensibility
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-defensibility-triple-signature.md"
    title: Aquaman triple signature pour la defensibilité
    last_modified: 2026-08-19
  - id: aquaman-pair-check-10
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-pair-check-10-legal-risk-launch.md"
    title: Aquaman pair-check #10 Legal risk → Launch
    last_modified: 2026-08-19
  - id: b2-veto-amplification
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: Amplification des vetos B2 — le catalogue est vivant, pas figé
    last_modified: 2026-08-19
  - id: triplet-13
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 13 — B3 dependsOn B2-sprint"
    last_modified: 2026-08-17
  - id: triplet-41
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 41 — B3 interdit-combler-trou"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Aquaman — proposition d'un champ `gating_inputs:` dans le contrat B2→B3

## Le trou dans le contrat B2 → B3 actuel

Le contrat B2→B3 (cf. [[b2-b3-jtbd-handoff-contract]] §« Le contrat
bilatéral ») pose **7 champs obligatoires** :

- 3 côté B2 sponsor : `cadre d'exécution`, `bornes DoD explicites`,
  `preuves attendues par forme`.
- 4 côté B3 squad lead : `plan de livraison`, `lead indicators`,
  `lag indicators`, `chemin d'escalade`.

**Aucun de ces 7 champs ne couvre les inputs amont dont le B2 a
besoin pour produire.** Le triplet 13 pose *« B3 dependsOn B2-sprint »*
— la dépendance va de B3 vers B2, pas dans le sens inverse. Mais le
catalogue JTBD Aquaman ([[aquaman-jtbd-emit-receive]]) montre que
**Aquaman lui-même a besoin d'inputs amont** pour produire :

- Forme 1 (privacy review) ← Flash feature spec + data flow.
- Forme 2 (claim safety) ← Superman claim draft + substantiation.
- Forme 3 (contract template) ← JohnJones deal structure +
  reformulation validée.
- Forme 4 (defensibility doc) ← Batman incident ou Cyborg breach
  (avec cas proactif Aquaman).

Sans ces inputs, Aquaman produit *de la fiction* (un privacy review
sans data flow diagram, un claim safety sans claim draft). Le contrat
B2→B3 actuel ne capture pas ces *pré-requis d'input* — il suppose
implicitement que le B2 sponsor a déjà reçu ses inputs amont, ce qui
n'est pas toujours vrai.

## La proposition : un champ `gating_inputs:`

Le champ `gating_inputs:` est ajouté au gabarit YAML du contrat
B2→B3, **côté B2 sponsor** (parce que c'est le B2 qui consomme les
inputs amont). Format proposé :

```yaml
gating_inputs:
  - source: <B2 captain amont>
    input: <type d'artefact attendu>
    required: true | false
    fallback: <gate B2 si input manquant>
  - source: ...
```

Chaque ligne précise :

- **source** : le B2 captain amont (par exemple *flash-product*,
  *superman-growth*, *johnjones-sales*).
- **input** : le type d'artefact attendu (par exemple *feature-spec*,
  *claim-draft*, *deal-structure*).
- **required** : booléen — l'input est-il bloquant ou advisory ?
- **fallback** : le gate B2 émis si l'input amont n'arrive pas
  (par exemple *BLOCKED_RISK*, *NEEDS_REVIEW*).

## Les 4 cas d'application pour Aquaman

### Cas 1 — Forme 1 (privacy review) ← Flash

```yaml
gating_inputs:
  - source: flash-product
    input: feature-spec-with-data-flow
    required: true
    fallback: BLOCKED_RISK
```

Sans la feature spec + data flow diagram de Flash, Aquaman ne peut
pas produire le privacy review. Le fallback est `BLOCKED_RISK` —
Aquaman refuse de démarrer le JTBD émis.

### Cas 2 — Forme 2 (claim safety) ← Superman

```yaml
gating_inputs:
  - source: superman-growth
    input: claim-draft-with-substantiation
    required: true
    fallback: BLOCKED_RISK
```

Sans le draft de claim + l'évidence de substantiation, Aquaman ne
peut pas produire le defensibility memo. Le fallback est
`BLOCKED_RISK`.

### Cas 3 — Forme 3 (contract template) ← JohnJones

```yaml
gating_inputs:
  - source: johnjones-sales
    input: deal-structure-with-reformulation
    required: true
    fallback: veto_engagement-sans-perimetre
```

Sans la structure du deal + la reformulation client validée,
Aquaman ne peut pas produire le contract template. Le fallback est
le **veto catalogue Aquaman lui-même** — c'est le cas où le veto
catégoriel *« sans accord écrit »* se déclenche en amont du
JTBD émis.

### Cas 4 — Forme 4 (defensibility doc) ← Batman / Cyborg / Aquaman

```yaml
gating_inputs:
  - source: batman-ops
    input: incident-report-with-decision-log
    required: false  # peut être proactif
    fallback: NEEDS_REVIEW
  - source: cyborg-it
    input: breach-spec-with-threat-model
    required: false  # peut être proactif
    fallback: NEEDS_REVIEW
```

La Forme 4 est **proactive possible** (cf.
[[aquaman-defensibility-triple-signature]] §Cas 4) — Aquaman peut
initier le binder sans incident. Les inputs sont donc `required:
false` ; le fallback `NEEDS_REVIEW` signale qu'Aquaman peut produire
un binder *draft* en attendant l'incident.

## Le champ `gating_inputs:` est-il Aquaman-spécifique ou générique ?

**Hypothèse générique** : les 7 autres domaines ont des inputs amont
analogues. Par exemple :

- Flash (Product) reçoit une spec UI/UX d'un designer (squad
  Designer) avant de merger une feature.
- Superman (Growth) reçoit un brief ICP d'un PM avant de produire
  une claim.
- Batman (Ops) reçoit un plan de capacity d'un squad Capacity avant
  d'armer une procédure.
- Cyborg (IT) reçoit une spec privacy d'Aquaman avant de merger une
  implémentation IT.

**Hypothèse Aquaman-spécifique** : seul Aquaman a des gating_inputs
aussi formalisés, parce que sa doctrine (engagement-sans-périmètre)
est *catégoriellement* sensible à la présence d'un input amont.

**Manque de données pour trancher** : aucun concept B2 ne pose les
gating_inputs des 7 autres domaines en Vague 2. L'hypothèse générique
est *plausible* mais non vérifiée.

## Proposition d'amendement : `gating_inputs:` comme champ générique

Le champ `gating_inputs:` est proposé comme **champ générique**
applicable à tous les domaines B2 qui ont des inputs amont. La
procédure d'amendement suit la doctrine veto amplification :

1. **Observation documentée** : les 4 formes reçues par Aquaman
   sont documentées en [[aquaman-jtbd-emit-receive]] §Les 4 formes
   reçues par Aquaman depuis les domaines amont (condition 1 de
   [[b2-veto-amplification-cycle]]).
2. **Draft en une phrase** : *« Le contrat B2→B3 inclut un champ
   optionnel `gating_inputs:` listant les inputs amont dont le B2
   sponsor a besoin pour produire, avec un fallback explicite par
   ligne. »*
3. **Décision d'archivage D4** : ligne dans le journal Council avec
   le draft et les cas d'application.

**Vote requis** : majorité simple (5/8), conformément à
[[b2-veto-amplification-cycle]] §« La procédure d'amendement ». Le
champ est *additionnel*, pas restrictif — il n'enlève aucune
possibilité aux domaines qui n'ont pas de gating_inputs.

## Les 3 cas d'application légitime

1. **Domaine qui dépend d'un input amont structuré.** Aquaman est le
   cas typique — son veto catalogue engagement-sans-périmètre bloque
   toute prestation dont le périmètre n'est pas tracé. Le
   `gating_inputs:` rend ce pré-requis explicite.
2. **Domaine qui dépend d'un input amont avec gate.** Batman (Ops)
   peut avoir besoin d'un capacity plan avant d'armer une procédure
   — sans capacity plan, Batman émet `LAUNCH_READY` (rouge). Le
   `gating_inputs:` formalise le gate.
3. **Domaine qui dépend d'un input amont critique pour la defensibilité.**
   Cyborg (IT) merge une implémentation privacy — sans spec privacy
   d'Aquaman, l'implémentation est *non-défendable*. Le
   `gating_inputs:` rend la dépendance visible.

## Les 3 cas d'abus

1. **Gating_inputs sur toute dépendance, même non-bloquante.** Si un
   domaine liste 10 inputs amont avec `required: true`, le contrat
   devient *infra-gérable* — le B2 sponsor passe son temps à
   vérifier que tous les inputs sont présents. La règle : limiter
   les `gating_inputs:` aux 2-3 inputs vraiment bloquants.
2. **Gating_inputs comme outil de pouvoir.** Un B2 sponsor qui liste
   des gating_inputs *impossibles à satisfaire* (par exemple
   *« attendez la confirmation du Council North Star »*) bloque
   l'exécution sans opposer de veto. La règle : chaque
   `gating_input` doit être *falsifiable* — un input *« la
   confirmation North Star »* n'est pas un input, c'est une
   condition politique.
3. **Gating_inputs sans fallback.** Un `gating_input: required: true`
   sans `fallback:` laisse le B2 sponsor sans porte de sortie si
   l'input n'arrive pas. La règle : chaque `gating_input` doit
   déclarer son `fallback` (par exemple *BLOCKED_RISK*,
   *NEEDS_REVIEW*, ou *escalate_to_B1*).

## Anti-pièges

- **Champ `gating_inputs:` confondu avec champ `contract_signed:`.**
  Le `contract_signed:` est la **double signature** B2 sponsor + B3
  lead (cf. [[b2-b3-jtbd-handoff-contract]] §« Le format conjoint »).
  Le `gating_inputs:` est une **liste d'inputs amont** dont le B2
  sponsor a besoin. Les deux champs sont compatibles et
  indépendants.
- **Gating_inputs utilisés pour combler un trou.** Le triplet 41
  interdit à B3 de combler un trou du sprint. Le `gating_inputs:`
  est *l'opposé* — il rend le trou visible. Un B2 sponsor qui
  *omet* un `gating_input` plutôt que de le signaler fait du
  silent rework ([[b2-b3-jtbd-handoff-contract]] §« Les trois
  failure modes »).
- **Gating_inputs non-côté-B2.** Le champ est **côté B2 sponsor** —
  il liste ce dont le B2 a besoin, pas ce dont le B3 a besoin. Un
  B3 qui ajoute ses propres pré-requis dans le `gating_inputs:`
  du contrat brouille la responsabilité.
- **Gating_inputs sur des inputs déjà capturés ailleurs.** Si un
  input amont est déjà documenté dans une pair-check canonique
  (par exemple #7 ou #8 pour Aquaman), il ne doit pas être
  re-listé dans `gating_inputs:`. Le doublon crée une ambiguïté de
  responsabilité.
- **Gating_inputs comme veto déguisé.** Un B2 sponsor qui liste un
  `gating_input` *« attendez que Superman confirme sa claim »* bloque
  l'exécution sans utiliser son veto catalogue. C'est du *veto
  déguisé*. La règle : un `gating_input` doit être un *artefact
  factuel* (spec, draft, brief), pas une *décision d'un autre
  capitaine*.

## Liens

- [[b2-b3-jtbd-handoff-contract]] — le contrat bilatéral que le
  champ `gating_inputs:` étend
- [[b3-jtbd-packet-reception-checklist]] — la vue B3 du même contrat
  (qui doit rester compatible)
- [[aquaman-jtbd-emit-receive]] — les 4 gating_inputs Aquaman qui
  motivent la proposition
- [[aquaman-defensibility-triple-signature]] — la Forme 4 avec
  gating_inputs `required: false`
- [[aquaman-pair-check-10-legal-risk-launch]] — quand le gating
  input est *« la décision du pair-check #10 »*, pas un artefact
- [[b2-veto-amplification-cycle]] — la procédure d'amendement que
  la proposition suit

## Note de confiance

**Confirmé par machine pour le contrat B2→B3 (7 champs) et le
catalogue Aquaman (4 formes reçues). Reconstruit pour la proposition
de champ `gating_inputs:`.** Le contrat B2→B3 est cité verbatim avec
ses 7 champs obligatoires. Les 4 formes reçues par Aquaman sont
posées verbatim en [[aquaman-jtbd-emit-receive]]. Le champ
`gating_inputs:` est une **projection** depuis les 4 gating
conditions implicites d'Aquaman — il n'est posé dans aucun concept
canonique. La procédure d'amendement (majorité 5/8 + D4) est tirée
de [[b2-veto-amplification-cycle]] §La procédure d'amendement. Les
3 cas d'application légitime et 3 cas d'abus sont **projetés** depuis
la pratique observée (gating Aquaman, capacity Batman, privacy
Cyborg). **À vérifier en cycle** : (1) les 7 autres domaines
ont-ils des gating_inputs analogues, ou est-ce une particularité
Aquaman ?, (2) la majorité 5/8 du Council est-elle tenable pour un
champ *additionnel* (pas restrictif), ou faut-il l'unanimité ?, (3)
le `fallback:` par input est-il *toujours* un gate B2 (BLOCKED_RISK,
NEEDS_REVIEW), ou peut-il être un autre type d'action (escalade,
amendement) ?
