---
type: Concept
title: Cyborg — extension optionnelle du packet mésoperpétuel avec mediation_actor + l0_dependency_ref (River Song, Sobriété Rick, A0 HITL)
description: Le triplet 38 (Cyborg dependsOn River Song, SDD-004 §7.2) et la Sobriété Rick (A1) sont des dépendances structurelles qui peuvent bloquer une décision IT. Le format packet mésoperpétuel canonique (b2-meso-decision-packet-spec.md) a 7 champs obligatoires, dont aucun ne porte la cette dépendance. Ce concept propose 2 champs optionnels — mediation_actor + l0_dependency_ref — applicables transversalement (pas seulement IT) sans casser la compatibilité D4.
tags: [cyborg, mediation, river-song, rick, a0-hitl, packet-mesoperpetuel, mediation_actor, l0_dependency_ref, extension-format]
generated: { by: minimax-m3, at: 2026-08-19T05:40:00Z }
verified:
  - { by: process:lecture-bcorpus-cyborg-tour-3, at: 2026-08-19T05:40:00Z }
sources:
  - id: b2-meso-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — format canonique 7 champs obligatoires
    last_modified: 2026-08-19
  - id: cyborg-couplages-l0
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-couplages-l0-rick-river-song-pyramide.md"
    title: Cyborg — couplages invisibles avec L0 Rick, River Song et la pyramide L0≥L1>L2 (triplets 38 + 39)
    last_modified: 2026-08-19
  - id: agents-md-canon
    resource: "C:/Users/amado/ASpace_OS_V3/30_Business_OS/AGENTS.md"
    title: AGENTS.md canonique — protocole Forge/Inject, triplets 37/38 sources verbatim
    last_modified: 2026-08-19
  - id: cyborg-doctrine-5-principes
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-doctrine-5-principles-dispatch.md"
    title: Cyborg — Sobriété Rick + A0 HITL (médiations transverses)
    last_modified: 2026-08-19
  - id: aquaman-couplages-invisibles
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-couplages-invisibles-legal-it.md"
    title: Aquaman — couplages Legal × IT (triplet canonique réversibilité)
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Cyborg — extension optionnelle du packet mésoperpétuel

## Le trou canon observé au tour 2

Le rapport Cyborg tour 2 §« Règles B2 qui me paraissent mal
ajustées » (règle 3) a noté :

> *« Le format packet mésoperpétuel standard a 7 champs [...] Aucun
> champ ne mentionne la médiation L0 (River Song, Sobriété Rick,
> A0 HITL). Or le triplet 38 (Cyborg → River Song) est une
> dépendance structurelle qui peut bloquer une décision IT. Cyborg
> qui signale un blocker L0 persistant devrait pouvoir documenter
> la cause dans un champ optionnel `mediation_actor`. »*

Ce concept acte la proposition en champs explicites, **optionnels
et transversaux** (pas seulement Cyborg — tout domaine B2 peut
utiliser les champs si une médiation structurelle s'applique).

## Le format packet mésoperpétuel canonique (avant extension)

`b2-meso-decision-packet-spec.md` pose 7 champs obligatoires :

```yaml
meso_decision_id: B2-MESO-DECISION-YYYY-NN
source_mandate: B1-B2-MANDATE-YYYY-NN | B2-PEER-YYYY-NN
mode: parallel | handoff | negotiation
impacted_domains:
  - domain
tradeoff: short statement
decision: accepted | blocked | escalate_to_B1
proof_expected:
  - B2 gate update
  - B3 proof path
next_review: date-or-cycle
```

Le rapport `b2-meso-decision-packet-spec.md` §Anti-pièges pose
5 anti-pièges dont :

- **Packet incomplet.** Un champ manquant est un signal de scan
  non terminé.
- **Packet sans next_review.** Indique une décision qui ne sera
  jamais ré-évaluée.

**Lecture clé** : les 7 champs sont **obligatoires**. L'extension
proposée est **optionnelle** — un packet sans `mediation_actor`
reste valide. L'extension **ajoute**, ne **substitue** pas.

## La proposition — 2 champs optionnels

### Champ 1 — `mediation_actor`

**Définition** : instance L0 / A0 / A1 / B1 qui **médiatise** la
décision B2, soit en amont (le packet ne peut pas être exécuté
sans son aval), soit en aval (la décision impacte la médiation
mais ne la bloque pas).

**Valeurs canoniques** (par lecture du corpus) :

| Valeur | Domaine B2 usager | Rôle |
|---|---|---|
| `river_song` | Cyborg (IT) | L0 mediation (triplet 38, AGENTS.md ligne 16) |
| `bill_forge` | Green Lantern (People) | L0.2 Forge mediation (triplet 37, AGENTS.md ligne 18) |
| `rick_sobriety` | Cyborg (IT) | A1 Sobriété kernel/infra (Dispatch Doctrine P11+P13) |
| `a0_hitl` | Cyborg (IT) | A0 HITL gate cron/kernel (B1_Manifesto §Sobriety) |
| `beth_veto` | transversale | L1 veto Beth (pyramide SDD-006 §1.1:59) |
| `<agent-name>` | autre | extension libre |

**Format YAML** :

```yaml
mediation_actor:
  - actor: <name>
    role: <L0|L0.2|A1|A0|L1>
    ref: <triplet-id|AGENTS.md-line|ADR-id>
    status: blocker | informed | n/a
```

**Statut** :

- `blocker` : la médiation est un prérequis — la décision ne peut
  pas être exécutée sans son aval.
- `informed` : la médiation est notifiée mais ne bloque pas.
- `n/a` : la médiation est dans le voisinage mais non pertinente.

### Champ 2 — `l0_dependency_ref`

**Définition** : référence canonique (SDD, ADR, triplet, AGENTS.md
line) qui pose la médiation structurelle. **Sans cette référence**,
le champ `mediation_actor` n'est pas vérifiable.

**Format YAML** :

```yaml
l0_dependency_ref:
  - type: s | | triplet | agents-md | adr | doctrine
    id: <stable-id>
    location: <path-or-line>
```

**Valeurs canoniques** :

| Type | ID exemple | Location |
|---|---|---|
| `triplet` | `triplet-38` | `triplets/v3-business.jsonl` ligne N |
| `agents-md` | `30_Business_OS/AGENTS.md` | ligne N |
| `sdd` | `SDD-004 §7.2` | chemin SDD |
| `adr` | `ADR-OMK-004` | chemin ADR |
| `doctrine` | `B2_Cyborg_IT_Dispatch` | chemin dispatch doctrine |

## L'extension packet — exemple IT

Packet mésoperpétuel Cyborg avec extension (exemple) :

```yaml
meso_decision_id: B2-MESO-DECISION-2026-XX
source_mandate: B1-B2-MANDATE-2026-XX
mode: negotiation
impacted_domains:
  - it
tradeoff: "Décision d'architecture touchant L0 Identity core.
  Médiation River Song requise."
decision: accepted
proof_expected:
  - B2 gate catalog update
  - B3 proof path
next_review: 12WY-2026-Q4
mediation_actor:
  - actor: river_song
    role: L0
    ref: triplet-38
    status: blocker
  - actor: rick_sobriety
    role: A1
    ref: B2_Cyborg_IT_Dispatch
    status: informed
l0_dependency_ref:
  - type: triplet
    id: triplet-38
    location: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
  - type: agents-md
    id: AGENTS.md-canon
    location: "C:/Users/amado/ASpace_OS_V3/30_Business_OS/AGENTS.md ligne 16"
```

C'est un packet **vérifiable** : chaque mediation_actor a une
ref, chaque ref a une location. La décision B2 documente la
médiation sans l'occulter.

## L'extension packet — exemple non-IT

Un packet mésoperpétuel **Aquaman** (Legal) qui touche une clause
contractuelle de réversibilité cloud (cf.
[[aquaman-couplages-invisibles-legal-it]]) :

```yaml
meso_decision_id: B2-MESO-DECISION-2026-YY
source_mandate: B2-PEER-2026-YY
mode: parallel
impacted_domains:
  - legal
  - it
tradeoff: "Clause de réversibilité contractuelle — vendor SaaS."
decision: accepted
proof_expected:
  - B2 gate catalog update (clause type A)
next_review: 12WY-2026-Q4
mediation_actor:
  - actor: cyborg
    role: B2-IT
    ref: triplet-29
    status: informed
l0_dependency_ref:
  - type: triplet
    id: triplet-29
    location: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
```

L'extension est **transversale** — Aquaman peut signaler que
Cyborg est informé (ou blocker) sans modifier son propre packet.
La traçabilité cross-domaine est **renforcée** sans complexifier
le format.

## Pourquoi 2 champs séparés, pas 1

La séparation `mediation_actor` (qui) / `l0_dependency_ref` (où
c'est posé) suit le **principe de moindre couplage** :

- `mediation_actor` : nom canonique + rôle + statut — *exécution*.
- `l0_dependency_ref` : référence canonique — *vérification*.

Un packet qui n'a que `mediation_actor` sans `l0_dependency_ref`
est **non-vérifiable** (la médiation peut être inventée). Un
packet qui n'a que `l0_dependency_ref` sans `mediation_actor`
est **incomplet** (la référence existe mais l'agent n'est pas
nommé). Les deux sont **cumulatifs**.

C'est symétrique au triplet canonique Aquaman × Cyborg
(contrat + IaC + failover) : trois éléments indissociables, mais
chacun avec un rôle différent.

## Compatibilité D4 append-only

`b2-meso-decision-packet-spec.md` §« Append-only — la règle D4 »
pose que le fichier `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` est
append-only. L'extension proposée est **compatible D4** :

- Un packet **sans** les champs optionnels reste valide (7 champs
  obligatoires suffisent).
- Un packet **avec** les champs optionnels est valide (les
  champs sont ajoutés, pas substitués).
- Le journal Council **accepte** les deux formes — D4 ne
  requiert pas l'uniformité des champs optionnels.

C'est une **extension backward-compatible**, pas une refonte du
format.

## La procédure d'adoption — submission B2 Council

L'extension est proposée comme **amendement au format packet
mésoperpétuel canonique**. Procédure recommandée :

1. **Soumission au B2 Council** par packet mésoperpétuel type
   avec `mode: parallel`, `impacted_domains: [it, legal,
   people, ops, sales, growth, product, finance]`, `tradeoff:
   "Extension optionnelle du format packet avec mediation_actor +
   l0_dependency_ref, applicable transversalement."`
2. **Vote** : 5/8 minimum (cf. quorum canonique
   `b2-council-cadence-and-chair.md`).
3. **Archivage D4** dans le journal Council + amendement de
   `b2-meso-decision-packet-spec.md` §« Le gabarit YAML » pour
   inclure les 2 champs optionnels.
4. **Effet** : tout packet mésoperpétuel ultérieur peut utiliser
   les champs optionnels sans casser la compatibilité D4.

## Anti-pièges spécifiques

- **mediation_actor inventé.** Un packet qui nomme un
  mediation_actor sans l0_dependency_ref est **non-vérifiable**.
  L'extension exige la cumulativité des champs.
- **l0_dependency_ref cassé.** Si la référence canonique pointe
  vers un fichier inexistant (cf. SDD-004 §7.2 introuvable, cf.
  rapport Cyborg tour 2 §« Ce que le corpus ne dit pas » §1),
  le packet est non-vérifiable. La cumulativité protège.
- **mediation_actor comme escalade de fait.** L'extension est
  informationnelle, pas hiérarchique. Un mediation_actor en
  statut `blocker` ne donne pas de droit d'arbitrage sur la
  décision B2 — c'est un prérequis d'exécution, pas une
  contestation.
- **Confondre optionnel et obligatoire.** Les 7 champs
  obligatoires restent obligatoires. L'extension est **ajout**,
  pas **substitution**.
- **Adoption sans amendement canonique.** Si le Council adopte
  l'extension oralement sans amender
  `b2-meso-decision-packet-spec.md`, l'extension n'a pas de
  force canonique — les packets restent au format 7 champs.
  L'archivage D4 + amendement canonique sont **tous deux
  requis**.

## Liens

- [[b2-meso-decision-packet-spec]] — format packet canonique 7 champs
- [[cyborg-couplages-l0-rick-river-song-pyramide]] — triplets 37/38
- [[cyborg-doctrine-5-principes-dispatch]] — Sobriété Rick + A0 HITL
- [[aquaman-couplages-invisibles-legal-it]] — triplet canonique réversibilité
- [[rapport-dom-cyborg]] §5.2 règle 3 — proposition source du concept

## Note de confiance

**Reconstruit, prêt à soumettre.** Les 2 champs optionnels sont
**ma proposition** (cf. rapport Cyborg tour 2 §5.2 règle 3). Le
principe de cumulativité `mediation_actor` + `l0_dependency_ref`
est **projeté** par symétrie avec le triplet canonique Aquaman ×
Cyborg (contrat + IaC + failover). La compatibilité D4 est
**vérifiée** par lecture de `b2-meso-decision-packet-spec.md`
§« Append-only — la règle D4 ». Les exemples IT (Cyborg) et
non-IT (Aquaman) sont **illustratifs**, pas observés en cycle. La
liste canonique des mediation_actor (`river_song`, `bill_forge`,
`rick_sobriety`, `a0_hitl`, `beth_veto`) est **construite** par
lecture des triplets 37, 38, 39 + AGENTS.md canon + Dispatch
Doctrine.

**Statut** : extension packet proposée, en attente de soumission
B2 Council. Compatible D4 append-only. Quorum 5/8 non testé en
cycle (cf. dormance structurelle wheel 8-domain).