---
type: Concept
title: Aquaman ↔ squad Eternals — composition, dépendance au premier contrat, et DoD vérifiable
description: La squad B3 Eternals sert Aquaman. Le triplet 22 cite 10 agents (Ikaris, Sersi, Ajak, Kingo, Phastos, Sprite, Druig, Thena, Gilgamesh, Makkari) ; le dossier OMK en charge 4 (Ikaris force, Ajak compliance, Phastos IP, Thena defense) ; le roster 53 en attend ~7. La tension n'est pas arbitrée. Le DoD Legal doit être vérifiable par un agent tiers ; l'anti-bottleneck rule du pipeline Rock→DoD→JTBD interdit plus d'une clarification avant démarrage B3.
tags: [b2, b3, aquaman, eternals, swarm, dormant, dod, jtbd, 53-roster]
generated: { by: minimax-m3, at: 2026-08-19T03:45:00Z }
verified:
  - { by: process:lecture-canon-aquaman, at: 2026-08-19T03:45:00Z }
sources:
  - id: triplet-22
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 22 — Aquaman pairedWith Eternals (10 techniciens)"
    last_modified: 2026-08-17
  - id: legal-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/README.md"
    title: 08 Legal - Aquaman / Eternals — B3 swarm scope
    last_modified: 2026-05-25
  - id: legal-pipeline
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md"
    title: Rock → DoD → JTBD Pipeline Legal
    last_modified: 2026-05-27
  - id: legal-swarm-supervision
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/02_B3_SWARM_SUPERVISION_PROTOCOL.md"
    title: B3 Swarm Supervision Protocol — Legal
    last_modified: 2026-05-27
  - id: fifty-three-roster
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/fifty-three-b3-agent-roster.md"
    title: 53 B3 Agent Roster
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Aquaman � squad Eternals

## Composition — tension non arbitrée

Trois sources citent des effectifs différents pour la squad Eternals.
**Aucune ne s'aligne.** La tension est documentée ici, pas tranchée.

| Source | Effectif cité | Agents nommés | Date |
|---|---|---|---|
| Triplet 22 (`coach-os/.../Aquaman_Eternals/VP_AGENT.md`) | **10 techniciens** | Ikaris, Sersi, Ajak, Kingo, Phastos, Sprite, Druig, Thena, Gilgamesh, Makkari | 2026-08-17 |
| Dossier OMK `00_B2_DOMAIN_CONTROL_ROOM.md` | 4 charges | Ikaris (force), Ajak (compliance), Phastos (IP), Thena (defense) | 2026-05-27 |
| Dossier OMK `01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md` | non chiffré | aucun nommé | 2026-05-27 |
| `fifty-three-b3-agent-roster.md` | ~7 par squad attendu | non énuméré pour Eternals | 2026-08-17 |

Lecture : **le triplet 22 est la source la plus précise** (10 noms),
le dossier OMK est **plus ancien** (daté 2026-05-27) et **réduit** à
4 charges *de travail*, pas à 4 *agents*. Le roster 53 attend
*« ≥7 agents par squad »* (cf. Ownerbook T1 DoD-1) sans donner le
total cible.

Conséquence opérationnelle : un audit qui voudrait recompter devrait
faire `find .claude/agents -name 'b3-eternals-*' | wc -l` — commande
citée dans le concept 53-roster, pas exécutée dans le corpus visible.

## Mapping charge ↔ surface Legal

`00_B2_DOMAIN_CONTROL_ROOM.md` pose le scope du swarm :

> *« B3 swarm: Ikaris force, Ajak compliance, Phastos IP, Thena
> defense. Core domain surface: claims, privacy, IP, terms, compliance
> boundaries. »*

Mapping pressenti entre les 4 charges et les 7 surfaces du périmètre
Legal :

| Charge | Surface pressentie | Périmètre Legal |
|---|---|---|
| **Ikaris (force)** | Exécution — contrats, claims, terms | Contract risk, claims, terms |
| **Ajak (compliance)** | Régulation — RGPD, sector rules | Compliance |
| **Phastos (IP)** | Propriété intellectuelle — licences, contrefaçon | IP |
| **Thena (defense)** | Defensibilité — contentieux, audit, incident | Permissions, defensibility |

Trois surfaces (privacy, et deux autres non mappées explicitement)
restent à attribuer. Si la squad passe à 10 (triplet 22), 6 surfaces
supplémentaires peuvent être distribuées — mais aucune source ne le
fait.

## Le pipeline Rock → DoD → JTBD

`01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md` pose un pipeline en 8 étapes :

1. Read B1 handoff queue.
2. Name one domain Rock.
3. Define the Definition of Done.
4. Create acceptance criteria and evidence requirements.
5. Split the Rock into B3 Jobs to be Done.
6. Let the B3 swarm execute autonomously.
7. Review artifacts against the DoD.
8. Update the B2 gate matrix and report to B1.

Pour Legal, ce pipeline **ne s'active pas avant le seuil d'activation**
(cf. [[aquaman-domaine-legal-perimetre]] §Activation). Tant que
`00_Summers_CEO/03_Master_Agreements/` est vide, les étapes 1-8 ne
produisent rien.

## Le DoD Legal — vérifiable par un tiers

`01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md` §DoD Quality Bar pose la barre :

> *« A DoD is valid only when a different agent can verify it from
> artifacts, metrics, logs, links, screenshots, commits, or structured
> notes. »*

Pour Legal, cette barre est particulièrement exigeante. Trois
exemples de DoD vérifiable vs invérifiable :

- ✅ *« Le template de contrat X est signé par 3 clients pilotes »*
  — vérifiable par le fichier dans `03_Master_Agreements/` et le
  journal de signature.
- ❌ *« Le contrat est juridiquement solide »* — non vérifiable sans
  un avocat tiers ; un Aquaman qui émet cette DoD ouvre la porte au
  scope creep.
- ✅ *« Le privacy review de la feature Y couvre RGPD art. 13, 14,
  30 »* — vérifiable par la checklist signée et le lien vers le code.
- ❌ *« La feature Y est privacy-safe »* — trop vague pour servir de
  DoD.

## Le JTBD packet — gabarit

`02_B3_SWARM_SUPERVISION_PROTOCOL.md` §JTBD Packet pose le gabarit
(déjà YAML dans le fichier source, repris ici en syntaxe correcte) :

```yaml
jtbd_id: B3-LEGAL-YYYY-NN
source_rock_id: B2-LEGAL-YYYY-NN
assigned_swarm: Eternals
job_statement: "When [situation], produce [artifact/outcome], so that [DoD progress]."
freedom_of_execution:
  allowed: "B3 chooses tactics, tools, and sequence."
  forbidden: "B3 cannot redefine Rock, DoD, or cross-domain gates."
input_artifacts:
  - path-or-link
expected_output_artifacts:
  - path-or-link
proof_required:
  - command/log/screenshot/report/link
lead_indicator: measurable action
lag_indicator: measurable outcome
blocker_protocol: "Return BLOCKED with missing input, failed assumption, and next B2 decision needed."
```

Le `blocker_protocol` est crucial pour Aquaman : un B3 Eternals qui
ne peut pas remplir le DoD (par exemple parce qu'un privacy review
manque) retourne `BLOCKED` *sans tenter de combler* (cf. triplet 41).

## L'anti-bottleneck rule

`01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md` §Anti-Bottleneck Rule :

> *« If B2 must answer more than one clarification before B3 can
> start, the JTBD is too vague. Rewrite the job, not the swarm. »*

Pour Legal, l'application est nette : un JTBD qui demande *« vérifie
la conformité de ce livrable »* sans préciser *« RGPD art. 13 sur les
données collectées, output = checklist signée »* oblige Aquaman à
répondre à plusieurs clarifications. Le JTBD est vague ; Aquaman doit
le réécrire, pas répondre trois fois.

## Autonomie contractuelle du swarm

`02_B3_SWARM_SUPERVISION_PROTOCOL.md` §Autonomy Contract pose les
frontées explicites :

**B3 peut librement** : choisir la séquence d'exécution, inspecter les
contraintes et proposer des workarounds, utiliser les outils locaux et
les surfaces approuvées, produire de meilleurs artefacts que la
demande initiale, **s'arrêter et déclarer un blocker quand le DoD ne
peut pas être satisfait honnêtement**.

**B3 ne peut PAS librement** : changer le Rock, changer le DoD,
contourner les gates Legal/Finance/Ops/IT/People, commiter des clés
privées ou credentials, marquer son propre travail comme Business Done
sans revue B2.

Pour Aquaman, cela donne un swarm **discipliné mais non domestique** :
Eternals ne sont pas des exécutants dociles, ils sont des agents qui
peuvent refuser un DoD impossible.

## Donna Safety Exit

`02_B3_SWARM_SUPERVISION_PROTOCOL.md` §Donna Safety Exit pose la
sortie de secours :

> *« If the swarm loops, fabricates proof, or keeps asking for
> permission instead of executing inside the contract, route the case
> to Donna/DLQ for safety review. »*

Pour Aquaman, cela signifie qu'un Eternals qui boucle sur une privacy
review (par exemple) est routé vers DLQ plutôt que vers le B2 captain
— Aquaman n'est pas dans la boucle de la safety review, ce qui est
cohérent avec sa position Consulted.

## Anti-pièges

- **Compter les Eternals sans préciser la source.** 4, 7, ou 10 sont
  trois nombres différents selon la source. Citer le nombre sans
  citer la source, c'est ouvrir la porte à l'arbitraire.
- **Activer le swarm avant le seuil.** Un Aquaman qui dispatch un
  JTBD Legal avant le premier Master Agreement est un coût pur (cf.
  [[aquaman-domaine-legal-perimetre]] §L'état dormant).
- **DoD non vérifiable.** Un DoD Legal que seul Aquaman peut
  reconnaître comme rempli n'est pas un DoD — c'est une opinion.
- **Confondre charges et agents.** Le dossier OMK cite 4 *charges*
  (force, compliance, IP, defense). Le triplet cite 10 *agents*. Les
  deux ne sont pas en contradiction directe — une charge peut être
  portée par plusieurs agents — mais la confusion est facile.

## Liens

- [[aquaman-domaine-legal-perimetre]] — le seuil d'activation
- [[aquaman-veto-engagement-sans-perimetre]] — le veto qui bloque
  un JTBD sans périmètre écrit
- [[aquaman-gates-et-pair-checks]] — les gates que le swarm doit
  faire bouger
- [[aquaman-couplages-invisibles]] — avec qui le swarm coordonne
- [[fifty-three-b3-agent-roster]] — la tension sur l'effectif

## Note de confiance

**Confirmé par machine pour le pipeline et la supervision ; tension
documentée pour l'effectif.** Pipeline 8 étapes, DoD Quality Bar,
anti-bottleneck, gabarit JTBD, Autonomy Contract et Donna Safety
Exit sont cités verbatim des fichiers OMK. La tension sur l'effectif
Eternals (10 vs 4 vs ~7) est **documentée et non arbitrée** — voir
rapport. Le mapping charge ↔ surface est **projeté** à partir des
noms et du scope B3 swarm du `00_B2_DOMAIN_CONTROL_ROOM.md`.
