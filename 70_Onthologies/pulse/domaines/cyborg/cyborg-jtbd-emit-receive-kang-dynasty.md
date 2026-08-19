---
type: Concept
title: Cyborg — paquets JTBD émis vers Kang Dynasty et reçus des domaines amont
description: Cyborg émet vers la squad Kang Dynasty des JTBD packets bornés par le Rock→DoD→JTBD pipeline (5 étapes, autonomy contract, peer unlock rule). Il reçoit en amont des pair-checks #3 Product→IT (Flash), #5 Finance→Growth (Wonder Woman sur coût d'infra) et indirectement #9 People→Tous (charge). Six formes de paquets canoniques observées, trois failure modes si le paquet est trop vague.
tags: [cyborg, jtbd, kang-dynasty, b3, packet, dofle, proof, escalation]
generated: { by: minimax-m3, at: 2026-08-19T04:10:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T04:10:00Z }
sources:
  - id: b2-rock-pipeline
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/05_IT_Cyborg_KangDynasty/01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md"
    title: Rock → DoD → JTBD Pipeline (5 étapes, anti-bottleneck rule)
    last_modified: 2026-05-27
  - id: b2-swarm-protocol
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/05_IT_Cyborg_KangDynasty/02_B3_SWARM_SUPERVISION_PROTOCOL.md"
    title: B3 Swarm Supervision Protocol (autonomy contract, JTBD packet)
    last_modified: 2026-05-27
  - id: cyborg-dispatch-doctrine
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/06_Claude_Code_Bare/mindsets/B2_Cyborg_IT_Dispatch.md"
    title: B2 Cyborg IT Dispatch Doctrine (heuristic par charge)
    last_modified: 2026-08-02
  - id: b3-roster-kang
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B3_Warp_Core_Execution/05_IT_Cyborg_KangDynasty/01_B3_AGENT_ROSTER.md"
    title: B3 Agent Roster IT / Kang Dynasty — 6 charges + escalation rule
    last_modified: 2026-05-27
  - id: b2-b3-handoff
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — 3 failure modes, double signature
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Cyborg — paquets JTBD émis et reçus

## Le pipeline Rock → DoD → JTBD

`01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md` pose 5 étapes canoniques pour
transformer une direction B1 en travail B3 exécutable :

1. **Lire la handoff queue B1.**
2. **Nommer un Rock du domaine IT.**
3. **Définir le Definition of Done.**
4. **Créer acceptance criteria et evidence requirements.**
5. **Splitter le Rock en B3 Jobs to be Done.**

Le Rock packet canonique (YAML verbatim) inclut :

- `rock_id` (B2-IT-YYYY-NN)
- `rock_statement` (*« As IT, achieve [outcome] so that [business reason] »*)
- `definition_of_done` (mesurable, artifact proof, customer impact)
- `acceptance_criteria`, `lead_indicators`, `lag_indicators`
- `b3_jobs` (liste de `jtbd_id`)

La règle **anti-bottleneck** :

> *« If B2 must answer more than one clarification before B3 can
> start, the JTBD is too vague. Rewrite the job, not the swarm. »*

Conséquence : un JTBD qui exige plus d'une clarification Cyborg est
un JTBD à réécrire — pas un B3 à clarifier.

## Le JTBD packet canonique (B2 → B3)

`02_B3_SWARM_SUPERVISION_PROTOCOL.md` pose le format :

```yaml
jtbd_id: B3-IT-YYYY-NN
source_rock_id: B2-IT-YYYY-NN
assigned_swarm: Kang Dynasty
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

Le contrat bilatéral `b2-b3-jtbd-handoff-contract.md` ajoute trois
champs non explicites ici (cf. infra).

## Autonomy contract — ce que B3 peut et ne peut pas

`02_B3_SWARM_SUPERVISION_PROTOCOL.md` pose un contrat bilatéral :

**B3 est libre de :**
- choisir sa séquence d'exécution
- inspecter les contraintes et proposer des workarounds
- utiliser les outils locaux et surfaces approuvées
- produire mieux que la demande initiale
- **stopper et déclarer un blocker** si le DoD est intenablement
  honnête

**B3 n'est pas libre de :**
- changer le Rock
- changer le DoD
- bypasser les gates Legal, Finance, Ops, IT, People
- committer des clés privées, credentials, valeurs sensibles
- marquer son propre travail comme Business Done sans revue B2

Trois interdits structurels : le Rock, le DoD, et les gates
cross-domaines. Le B3 signale, ne décide pas (triplet 41 :
*« B3 interdit-combler-trou »*).

## Le dispatch — 5 formes canoniques vers Kang Dynasty

`B2_Cyborg_IT_Dispatch.md` pose un mapping heuristique par charge :

| Forme de paquet | B3 cible | Déclenché par |
|---|---|---|
| **Architecture decision** | Kang Prime (LEAD) | décision d'architecture nouvelle |
| **Greenfield / prototype** | Iron Lad | nouveau build, POC |
| **Spike / alt-stack** | Scarlet Centurion | test d'une stack alternative |
| **Legacy / déprécation** | Immortus | code legacy, archivage, déprécation |
| **Frontier feature** | Victor Timely | feature frontière, civic-grade IT |
| **Refactor / review** | Rama-Tut | refactor, code review, chaos engineering |

Six formes, six B3 distincts. Le B3 squad lead (Kang Prime)
**arbitre** si une demande est à cheval sur deux charges — c'est son
mandat de lead.

## Les paquets émis — 6 archétypes observés

Trois archétypes **pérennes** (reviennent chaque cycle) et trois
**épisodiques** (déclenchés par événement).

### Pérennes

1. **Provisioning JTBD** (Iron Lad) — *« Provisionne un VPS Hetzner
   pour le tenant XYZ, DoD = SSH joignable en <5 min, IaC Terraform
   mergé. »*
2. **Monitoring JTBD** (Rama-Tut) — *« Ajoute une alerte Uptime Kuma
   sur le service ABC, DoD = alerte testée + escalade Cyborg en
   <15 min. »*
3. **Backup JTBD** (Rama-Tut / Immortus) — *« Backup quotidien du
   bucket DEF, DoD = restore testé en <30 min, RPO 24h, RTO 1h. »*

### Épisodiques

4. **Migration JTBD** (Immortus) — *« Migre le service legacy GHI
   vers la stack JKL, DoD = service équivalent, IaC complet,
   rollback testé. »*
5. **Chaos engineering JTBD** (Rama-Tut) — *« Joue un game day
   où le DNS tombe, DoD = RTO mesuré, escalade Cyborg documentée. »*
6. **Sovereignty gate JTBD** (Kang Prime) — *« Documente le chemin
   de sortie du vendor MNO, DoD = clause contractuelle + alternative
   testée. »*

## Les paquets reçus — pair-checks amont

Cyborg **reçoit** des paquets en amont de trois pair-checks canoniques
(cf. `b2-pair-check-raci-by-rank`) :

- **#4 Product → IT** (Flash amont, Cyborg A) — feature shippe,
  Cyborg prend la charge de la faire tourner. Le JTBD reçu de Flash
  est *« voici la PR mergée, déploie et monitore »*.
- **#5 Finance → Growth** (Wonder Woman en C sur le coût d'infra) —
  Wonder Woman consulte Cyborg sur le ROI d'une dépense d'infra. Le
  JTBD reçu est *« chiffre la métrique de retour de cette dépense
  récurrente »*.
- **#9 People → Tous** (charge, ownership) — Green Lantern consulte
  Cyborg sur la charge Kang Dynasty (6 agents). Le JTBD reçu est
  *« quel est le load et la tenure des 6 agents ? »*.

Cyborg est aussi **Impliqué indirectement** dans :
- **#3 Product → Ops** (Batman A) — la chaîne Product→IT→Ops signifie
  que Batman dépend de Cyborg pour la sortie de #4 (cf.
  [[batman-couplage-ops-it]]).
- **#7 Legal → Growth** (Superman A) — Aquaman consulte parfois
  Cyborg sur les clauses contractuelles de fournisseurs IT (chemin
  de sortie = clause de réversibilité).

## Les 3 failure modes (cf. b2-b3-jtbd-handoff-contract)

Le contrat B2 → B3 pose trois failure modes canoniques qui
s'appliquent à Cyborg ↔ Kang Dynasty :

### 1. Scope creep

B3 produit plus que demandé (« c'était plus simple »). Cyborg refuse
la livraison excédentaire et consigne dans le journal Council.

### 2. Silent rework

B3 a livré, mais a refait en cours d'exécution sans escalader. Cyborg
ouvre un arbitrage *« rework non-escaladé »* en séance hebdomadaire.

### 3. Escalade tardive

B3 a tenu jusqu'au bout, puis a escaladé un blocker qu'il connaissait
depuis 3 jours. Cyborg exige un *« escalator register »* pour le
sprint suivant.

## L'escalation rule canonique

`01_B3_AGENT_ROSTER.md` pose l'escalade B3 → B2 :

> *« Escalade vers Jerry si uptime mensuel < 99% ou MTTR infra > 1h. »*

Deux seuils chiffrés : **uptime < 99%** et **MTTR > 1h**. Ces deux
seuils sont des **gates B2** : en dessous, Kang Dynasty escalade
automatiquement. Au-dessus, Kang Dynasty est **autonome**.

## La review loop

`02_B3_SWARM_SUPERVISION_PROTOCOL.md` pose 4 étapes :

1. B3 poste l'artifact et la proof.
2. B2 (Cyborg) check la proof contre le DoD.
3. B2 retourne un de : **accepted, revise, blocked, escalate_to_B1**.
4. B2 update la B2 gate matrix et report à B1.

## La Donna Safety Exit

Si la swarm **loops, fabriques proof, ou keeps asking for permission**
au lieu d'exécuter dans le contrat, Cyborg route le cas à **Donna/DLQ**
pour safety review. C'est un anti-pattern de gouvernance : un B3 qui
ne joue pas son mandat d'autonomie.

## Anti-pièges

- **JTBD trop vague.** Anti-bottleneck rule : si Cyborg doit
  répondre >1 clarification avant que B3 démarre, réécrire le JTBD.
- **B3 qui change le DoD.** Interdit structurel. Cyborg consigne
  dans le journal Council.
- **B3 qui bypasse une gate cross-domaine.** Interdit structurel.
  Cyborg remonte à Summers.
- **B3 qui marque son propre travail Business Done.** Interdit
  structurel. La review est à Cyborg.
- **Cyborg qui micro-manage chaque action B3.** Anti-bottleneck
  symétrique : si Cyborg répond à chaque action B3, le contrat est
  cassé. Cyborg revoit les **artifacts**, pas les actions.

## Liens

- [[cyborg-domain-it-perimetre-frontieres]] — le périmètre
- [[cyborg-veto-cloud-only-sortie]] — le veto applicable aux paquets reçus
- [[cyborg-couplages-l0-rick-river-song-pyramide]] — la pyramide L0
- [[cyborg-pair-checks-product-it-fantastic-four]] — pair-check #4 détaillé
- [[b2-b3-jtbd-handoff-contract]] — le contrat bilatéral

## Note de confiance

**Confirmé par machine** pour le pipeline 5 étapes, le format JTBD,
l'autonomy contract et l'escalation rule (4 sources verbatim). Les
six archétypes de paquets émis (3 pérennes + 3 épisodiques) sont
**projetés** à partir du dispatch heuristic et de la doctrine IT
OMK — non observés en cycle réel dans le corpus disponible. Les
trois failure modes sont **applicables** depuis
[[b2-b3-jtbd-handoff-contract]] mais non vérifiés en cycle Cyborg ↔
Kang Dynasty. La Donna Safety Exit est **citée verbatim** mais non
déclenchée en corpus.
