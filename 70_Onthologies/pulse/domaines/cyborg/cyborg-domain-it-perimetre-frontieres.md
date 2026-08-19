---
type: Concept
title: Cyborg (IT) — périmètre et trois frontières qui demandent arbitrage
description: Cyborg tient l'architecture IT et l'infra souveraine : runtime, accès, déploiement, backup, technical boundaries. Sa mission B2 est de transformer un rock B1 en JTBD packets bornés pour la squad B3 Kang Dynasty (6 agents). Trois frontières sont poreuses avec Batman (Ops), Flash (Product) et Wonder Woman (Finance), et chacune appelle un arbitrage Council plutôt qu'une décision Cyborg seul.
tags: [cyborg, it, perimetre, souverain, kang-dynasty, frontieres, ops, product, finance]
generated: { by: minimax-m3, at: 2026-08-19T04:00:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T04:00:00Z }
sources:
  - id: triplet-cyborg
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 21 — Cyborg pairedWith Kang Dynasty (R&D & IT)"
    last_modified: 2026-08-17
  - id: triplet-cyborg-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 29 — Cyborg hasVetoOver cloud-only-sans-sortie"
    last_modified: 2026-08-17
  - id: b2-domain-control-room
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/05_IT_Cyborg_KangDynasty/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: B2 Cyborg IT — Domain Control Room (mission, surface, handoff)
    last_modified: 2026-05-27
  - id: b2-cyborg-it-agent
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/06_Claude_Code_Bare/agents/b2-06-cyborg-it.md"
    title: b2-06-cyborg-it — Manager E-Myth IT (mission + squad roster)
    last_modified: 2026-08-02
  - id: cyborg-dispatch-doctrine
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/06_Claude_Code_Bare/mindsets/B2_Cyborg_IT_Dispatch.md"
    title: B2 Cyborg IT Dispatch Doctrine — heuristic + 5 IT principles
    last_modified: 2026-08-02
  - id: b3-roster-kang
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B3_Warp_Core_Execution/05_IT_Cyborg_KangDynasty/01_B3_AGENT_ROSTER.md"
    title: B3 Agent Roster IT / Kang Dynasty (6 agents canoniques)
    last_modified: 2026-05-27
okf_version: "0.2"
---

# Cyborg (IT) — périmètre et trois frontières

## Ce que Cyborg tient

Le domaine **IT** sous Cyborg porte une surface canonique définie par
`B2_DOMAIN_CONTROL_ROOM.md` :

> **Core domain surface :** runtime, access, deployment, backup,
> technical boundaries.

Cinq dimensions, toutes dans le **système** (vs Batman Ops qui tient la
**procédure** — la frontière Ops/IT est reconstruite par Batman's
couplage, cf. [[batman-couplage-ops-it]]). Cyborg produit des
artefacts IT : pipelines CI/CD, dashboards de monitoring, alertes,
playbooks de recovery, et — depuis l'amendement 001 de SDD-006 (2026-08-19)
— la **pyramide L0/L1/L2** qui surplombe l'ensemble (cf.
`concept-sdd-006-collision.md`).

La mission B2 Cyborg (`b2-06-cyborg-it.md`) :

> Manager IT architecture + infra souveraine. Pilot B3 Kang Dynasty
> (Kang Prime lead, 6 members). Horizon H10 IT architecture review.

Trois mots-clés : **architecture**, **infra souveraine**, **horizon
H10**. Cyborg n'est pas un opérateur quotidien — il arbitre les
**décisions d'architecture** sur un horizon trimestriel, et laisse
l'exécution à la squad Kang Dynasty.

## La squad Kang Dynasty — 6 agents, 6 charges

`01_B3_AGENT_ROSTER.md` liste les 6 charges canoniques :

| B3 agent | Charge canonique | Dispatch déclenché par |
|---|---|---|
| **Kang Prime** (lead) | Lead infra, architecture VPS + DNS + Dokploy | décision d'architecture |
| **Iron Lad** | Provisioning rapide, scripts bootstrap Hostinger API | greenfield, prototype |
| **Scarlet Centurion** | Sécurité réseau, firewall, SSL/TLS | spike, alt-stack |
| **Immortus** | Long-term planning, capacity planning, scaling | legacy, déprécation |
| **Victor Timely** | Time-boxing déploiements, CI/CD discipline | feature frontière |
| **Rama-Tut** | Backup and disaster recovery | refactor, review |

Le triplet 21 confirme le **mapping 6 agents / 6 charges** côté
Coach OS : `KangPrime, IronLad, ScarletCenturion, Immortus, VictorTimely, RamaTut`.
Le `B2_Cyborg_IT_Dispatch.md` ajoute un mapping sémantique légèrement
différent (legacy code / archival pour Immortus, time-series infra ;
refactor / review pour Rama-Tut) — **les deux mappings se recouvrent
sans contradiction** : la version OMK est **infra**, la version Coach
OS est **code/architecture**. Les deux lectures sont vraies
simultanément, et la distinction est un arbitrage que Cyborg tranche
en sprint hebdo.

## Frontière 1 — Cyborg ↔ Batman (Ops) : la chaîne Product→IT→Ops

Frontière **nette mais poreuse**, reconstruite par
[[batman-couplage-ops-it]] :

| Dimension | Cyborg (IT) | Batman (Ops) |
|---|---|---|
| Tient | le système (déploiement, monitoring, infra) | la procédure (runbook, escalation, condition d'arrêt) |
| Question de garde | *« le système tient quand X arrive ? »* | *« on sait répondre quand X arrive ? »* |
| Veto | cloud-only sans chemin de sortie | procédure sans condition d'arrêt |

**Cas concret de porosité :** un runbook Ops exige un monitoring IT.
Batman dépend de Cyborg pour que le dashboard existe ; Cyborg dépend
de Batman pour que le runbook soit suivi. Sans les deux, le red flag
#1 (*Product green, Ops/IT red — ne pas lancer*) se déclenche.

**Arbitrage :** le RACI par rang place Cyborg **A** sur le pair-check
#4 (Product → IT) et Batman **A** sur le pair-check #3 (Product → Ops)
— Batman est dépendant de la sortie Cyborg, pas l'inverse. Si Cyborg
oppose son veto (cloud-only sans chemin de sortie), Batman remonte le
fait à Summers (B1). Cf. [[b2-pair-check-raci-by-rank]].

## Frontière 2 — Cyborg ↔ Flash (Product) : le code shippe, IT déploie

Frontière **nette** : Flash shippe la feature dans le produit (PR
mercée, version taguée), Cyborg prend la charge de la faire **tourner**
sur le système (déploiement, monitoring, recovery). Le pair-check #4
(Product → IT) teste ce transfert.

**Cas concret de porosité :** une feature qui dépend d'un service
cloud (SaaS) que Cyborg n'a pas homologué. Flash shippe la feature ;
Cyborg refuse le déploiement car le chemin de sortie n'est pas
documenté. Le veto Cyborg bloque le déploiement, pas le code.

**Arbitrage :** si Flash argue que la dépendance est *transitoire*
(moins de 30 jours), Cyborg accepte une dérogation avec date de revue
— c'est le cas typique d'un **Wonder Woman amplification** (cf.
triplet 58 cité par Wonder Woman) : la dépense récurrente sans date
de revue est bloquée par Wonder Woman, mais Cyborg transpose
l'amplification sur **dépendance cloud sans chemin de sortie**.

## Frontière 3 — Cyborg ↔ Wonder Woman (Finance) : coût de l'infra

Frontière **nette** : Wonder Woman tient le retour chiffré de chaque
dépense récurrente ; Cyborg tient le coût d'infra (VPS, DNS,
monitoring, CI/CD). Les deux sont **complémentaires**, pas
concurrents — Cyborg consomme, Wonder Woman mesure.

**Cas concret de porosité :** un déploiement qui multiplie par 4 le
coût VPS mensuel. Wonder Woman oppose son veto *« dépense récurrente
sans métrique de retour »* si Cyborg n'a pas chiffré le ROI
(latence réduite, downtime évité, throughput gagné). Cyborg, lui,
oppose son veto *« cloud-only sans chemin de sortie »* sur le même
sujet — **deux vetos cumulables**, pas redondants.

**Arbitrage :** le pair-check #5 (Finance → Growth) ne touche pas
directement IT, mais le couple (Cyborg ↔ Wonder Woman) est cité
dans `b2-06-cyborg-it.md` *« Sister B2 : WonderWoman_Finance (cost of
infra) »*. Le Council arbitre les deux vetos cumulés en mode
**negotiation**.

## La divergence de numérotation Coach OS vs canonique 08

`b2-06-cyborg-it.md` et le triplet 21 numérotent Cyborg **domaine 7**
(R&D & IT). L'Avengers Wheel canonique (`eight-domain-avengers-wheel.md`)
le numérote **domaine 5** (IT). Batman's rapport ([[batman-numerotation-coach-os-vs-canon-08]])
documente la même divergence pour Ops. La **numérotation canonique
devrait être déclarée source de vérité** dans les packets
mésoperpétuels — sinon les citations croisées sont ambiguës.

Cette divergence est **résidue de la transition OMK → Coach OS**, pas
une vraie contradiction de fond. Le périmètre IT est le même des
deux côtés ; seul l'ordre change.

## Anti-pièges

- **Cyborg qui statue sur la procédure.** Un runbook est Batman, pas
  Cyborg. Cyborg peut documenter le monitoring, mais la procédure
  d'escalade qui suit l'alerte est Batman. Cf. anti-pièges
  [[batman-couplage-ops-it]].
- **Cyborg qui touche L0 directement.** Triplet 38 : *« Cyborg ne
  touche pas L0 directement — il passe par River Song (SDD-004 §7.2),
  médiation agentique imposée. »* Cf.
  [[cyborg-couplages-l0-rick-river-song-pyramide]].
- **Cyborg qui absorbe R&D.** Le triplet 21 cite *« R&D & IT »* mais
  l'extension R&D n'est pas définie canoniquement. Si Cyborg absorbe
  la R&D externe (W40 patches), il faut une **décision Summers**
  explicite, pas une glissement de périmètre. Cf. rapport.
- **Cyborg qui décide seul un arbitrage cross-domaine.** Toute
  décision qui touche Flash, Batman ou Wonder Woman passe par le
  B2 Council, pas par Cyborg seul. La double signature
  B2 sponsor + B3 lead n'est pas une délégation Cyborg.

## Liens

- [[batman-couplage-ops-it]] — la chaîne Product→IT→Ops
- [[cyborg-veto-cloud-only-sortie]] — le veto catalogue
- [[cyborg-jtbd-emit-receive-kang-dynasty]] — les paquets JTBD
- [[cyborg-couplages-l0-rick-river-song-pyramide]] — les contraintes L0/L1/L2
- [[cyborg-pair-checks-product-it-fantastic-four]] — pair-check #4 détaillé
- [[b2-pair-check-raci-by-rank]] — Cyborg A sur #4

## Note de confiance

**Confirmé par machine** pour la surface canonique et la squad
Kang Dynasty (4 sources verbatim). **Reconstruit** pour les trois
frontières — la matrice canonique pose Ops×IT, Product×IT et
Finance×Product, mais pas les frontières sémantiques décrites
ici. La divergence de numérotation 7 (Coach OS) vs 5 (canonique 08)
est **documentée** par [[batman-numerotation-coach-os-vs-canon-08]]
— pas tranchée ici. La **lecture « R&D absorbé à L0 Rick »** du
W40 patch est **présumée** (cf. triplet 21 cite *« R&D & IT »* mais
ne définit pas R&D) — **remontée vers B1**.
