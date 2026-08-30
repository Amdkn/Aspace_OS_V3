---
type: Concept
title: Cyborg dans AaaS — Solaris (lead IT), Nexus (sub-lead), Orbiter (lead IT partagé)
description: ADR-L2-AAAS-001 ACCEPTED 2026-06-21 pose 3 variants AaaS (Solaris / Nexus OMK / Orbiter ABC) × 4 leviers Solarpunk. Cyborg apparaît dans les 3 variants avec un rôle différent : Solaris = lead IT (Cyborg LD03), Nexus OMK = sub-lead IT (WonderWoman finance lead), Orbiter ABC = lead IT partagé (avec WonderWoman finance). Conséquences sur les paquets JTBD émis vers Kang Dynasty, et sur le couplage IT � Finance (WonderWoman) qui se renforce dans AaaS.
tags: [cyborg, aaas, solarpunk, solaris, nexus-omk, orbiter-abc, sister-adr, ld03-cognition, kardashev]
generated: { by: minimax-m3, at: 2026-08-19T04:35:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T04:35:00Z }
sources:
  - id: adr-l2-aaas-001
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md"
    title: ADR-L2-AAAS-001 — AaaS Doctrine 3 Variants × 4 Leviers Solarpunk (ACCEPTED 2026-06-21)
    last_modified: 2026-06-21
  - id: triplet-cyborg-kang
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 21 — Cyborg pairedWith Kang Dynasty (R&D & IT)"
    last_modified: 2026-08-17
  - id: cyborg-domain
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-domain-it-perimetre-frontieres.md"
    title: Cyborg (IT) — périmètre et trois frontières
    last_modified: 2026-08-19
  - id: b2-cyborg-it-agent
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/06_Claude_Code_Bare/agents/b2-06-cyborg-it.md"
    title: b2-06-cyborg-it — sister ADR-OMK-004 + ADR-L2-AAAS-001
    last_modified: 2026-08-02
  - id: business-wheel-eight-domains
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-eight-domains.md"
    title: Business Wheel 8 Domaines × LD01 (matrice d'ancrage canonique)
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Cyborg dans AaaS — 3 variants, 3 rôles

## Le placement canonique Cyborg × AaaS

`ADR-L2-AAAS-001` (ACCEPTED 2026-06-21) pose 3 variants AaaS
canoniques. Cyborg (IT) est listé dans les 3, avec un rôle
**différent** à chaque fois (Annexe D2 du même ADR) :

| Variant AaaS | Rôle Cyborg | Statut Q3 2026 | 8 Domaines B2 primaires |
|---|---|---|---|
| **Solaris AaaS** (Life-OS-2026) | **Lead IT** (LD03 Cognition) | 🟢 ACTIF | Superman Growth + Flash Product + WonderWoman Finance + **Cyborg IT** |
| **Nexus OMK AaaS** (omk-services) | **Sub-lead IT** (WonderWoman finance lead) | 🟢 ACTIF | WonderWoman Finance + JohnJones Sales + Flash Product + Batman Ops + **Cyborg IT (sub)** |
| **Orbiter ABC AaaS** (abc-community-os) | **Lead IT partagé** (avec WonderWoman finance) | 🟢 ACTIF (récent) | GreenLantern People + Aquaman Legal + WonderWoman Finance (advisory) + **Cyborg IT (partagé)** |

Le 4e variant Family/Home est **dormant** (Q3 2026), réveil Q4
2026 / Q1 2027 par décision canonique.

## Lecture 1 — Solaris AaaS : Cyborg lead IT

Solaris AaaS = Life-OS-2026 Initiative ALPHA. Cyborg est **lead IT**
parce que LD03 (Cognition) est l'ancre canonique du variant
(ADR-L2-AAAS-001 §D2 — mapping Solaris = LD01 Business + LD02
Finance + LD04 Cognition + LD07 Creativity). L'infrastructure IT
est **structurante** : sans Cyborg lead, pas de socle pour Book
(LD01 hebdo), Saru (LD02 quarterly), ou Flash (LD04 Product).

**Conséquence opérationnelle** : la squad Kang Dynasty est *entière*
au service de Solaris. Les 6 charges (Kang Prime lead, Iron Lad,
Scarlet Centurion, Immortus, Victor Timely, Rama-Tut) tournent sur
le Life-OS-2026 stack (Supabase Cloud Life OS org + Vercel
`life-os-2026-liart.vercel.app`).

**Production deploy SHA vérifié** : `b933e4e41849a323c63504e2ecea36b71c8759e5`
(ADR-L2-AAAS-001 Annexe A ligne 219). C'est un *fait*, pas une
projection.

## Lecture 2 — Nexus OMK AaaS : Cyborg sub-lead IT

Nexus OMK AaaS = omk-services, Sprint Zéro Bug `dcc1235` ✅
livré 2026-06-20. Cyborg est **sub-lead IT** parce que le variant
est ancré sur **WonderWoman Finance (LD02)** et que IT est *au
service* du pivot financier Saru 1000T (production de valeur réelle
Kardashev Type 3).

**Conséquence opérationnelle** : la squad Kang Dynasty partage ses
charges entre Solaris (priorité) et Nexus (sub). Le pivot Cloud
ADR-OMK-004 a été *conduit pour Nexus* : 4 Vercel projects OMK +
3 Supabase Cloud orgs + 2 PATs. Cyborg a opéré le pivot pour Nexus,
pas pour Solaris.

**Production deploy SHA vérifié** : `8ad94d1` (post-merge sprint
`dcc1235`, ADR-L2-AAAS-001 Annexe A ligne 220). 9 tables
`omk_saas.*` + JWT hook `e47f4aa1`.

## Lecture 3 — Orbiter ABC AaaS : Cyborg lead IT partagé

Orbiter ABC AaaS = abc-community-os, schema `abc_os` migré
2026-06-17. Cyborg est **lead IT partagé** avec WonderWoman
finance advisory, parce que l'orbite Burnham (LD06 Family) ancre
le variant, et IT est *co-lead* avec Finance (pas sub-lead comme
Nexus).

**Conséquence opérationnelle** : la squad Kang Dynasty *partage*
ses charges entre les 3 AaaS variants. Le ratio typique (projeté
depuis la doctrine, non observé en cycle) :

- Solaris : ~50% (lead, ancre canonique)
- Nexus OMK : ~30% (sub-lead, pivot Cloud)
- Orbiter ABC : ~20% (lead partagé, récent)

**Statut 2026-06-19** : `PGRST_DB_SCHEMAS` env var = P0 blocker en
cours résolution (ADR-L2-AAAS-001 Annexe A ligne 221). Cyborg
doit arbitrER ce blocker (sans bloquer le pivot ABC).

## L'effet sur les paquets JTBD émis vers Kang Dynasty

`cyborg-jtbd-emit-receive-kang-dynasty.md` (tour 1) pose 6 formes
de paquets (Architecture, Greenfield, Spike, Legacy, Frontier,
Refactor) vers Kang Dynasty. **Avec AaaS, chaque forme de paquet
est *pondérée* par le variant dominant** :

| Forme de paquet | Pondération Solaris | Pondération Nexus OMK | Pondération Orbiter ABC |
|---|---|---|---|
| **Architecture decision** (Kang Prime) | 60% | 30% | 10% |
| **Greenfield / prototype** (Iron Lad) | 50% | 40% | 10% |
| **Spike / alt-stack** (Scarlet Centurion) | 30% | 50% | 20% |
| **Legacy / déprécation** (Immortus) | 20% | 30% | 50% (ABC legacy code) |
| **Frontier feature** (Victor Timely) | 70% (civic-grade IT) | 20% | 10% |
| **Refactor / review** (Rama-Tut) | 40% | 40% | 20% |

**Lecture** : Legacy / déprécation est *plus dominant* sur Orbiter
ABC parce que le variant family offices hérite souvent de code
legacy. Frontier feature est *plus dominant* sur Solaris parce que
le variant Life-OS-2026 vise Kardashev Type 3 (high-tech de pointe).

**Statut** : ces pondérations sont **projetées** depuis l'ADR et
la doctrine, pas observées en cycle. Mais elles sont utiles comme
outil de planification — quel agent Kang Dynasty est *plus
sollicité* par quel variant.

## L'effet sur le couplage IT ↔ Finance (WonderWoman)

ADR-L2-AAAS-001 §D2 place WonderWoman (Finance) en **co-lead avec
Cyborg** dans Solaris AaaS et Orbiter ABC AaaS, et **lead** dans
Nexus OMK AaaS. Conséquence : le **couplage IT × Finance se
renforce** dans le contexte AaaS.

Trois manifestations concrètes :

### 1. Le coût d'infra est mesuré comme production de valeur réelle

Avant AaaS : coût VPS = coût récurrent (WonderWoman veto sur
*« dépense récurrente sans métrique »*). Après AaaS : coût VPS =
*production de valeur réelle Kardashev Type 3* (Saru 1000T). La
même dépense est *justifiée différemment* — par impact social
monétisé (SROI), pas par ROI court terme.

### 2. Le pivot Cloud est un investissement Solarpunk, pas un cost-cut

ADR-OMK-004 acte le pivot Cloud (Supabase self-host → Cloud). En
lecture AaaS, ce n'est pas un *coût récurrent* (Supabase Cloud
= $25-50/mois par team, ADR-OMK-004 §Consequences ligne 207) —
c'est un *investissement Solarpunk* (Levier 4 = Circular & Blue
Economy, Memory Core = circular info canonique append-only).

### 3. Le triplet 58 (amplification date+ROI) est validé implicitement

Le triplet 58 (Wonder Woman amplification *« avec ROI à 30 jours »*)
est cité par Wonder Woman rapport tour 1 et tour 2. Cyborg a posé
au tour 1 une amplification symétrique *« date de revue + métrique
de réversibilité »* (cf. [[cyborg-veto-cloud-only-sortie]] §Le cas
Spécial). **En contexte AaaS**, cette amplification est *validée
implicitement* par les 4 leviers Solarpunk — chaque livrable AaaS
doit boucler ≥1 cycle (matière / énergie / information), ce qui
*est* une date de revue + métrique de réversibilité.

## La dépendance Cyborg ↔ Life Wheel LD03 Cognition

`ADR-L2-AAAS-001` ligne 78 cite Cyborg LD03 dans Solaris AaaS.
LD03 = Cognition (Life Wheel). **Le périmètre Cyborg est *étendu*
par AaaS** : il ne tient plus seulement IT (runtime, accès,
déploiement, backup), mais aussi LD03 Cognition — c'est-à-dire
*l'infrastructure de la cognition* (Memoria Core wiki canonique,
LLM_Wiki, Memory Core local-first avant sync VPS).

C'est **précisément** ce que le triplet 21 cite comme *« R&D & IT »*
(et que le rapport tour 1 a noté comme « extension R&D non définie
canoniquement »). **AaaS le définit** : R&D = LD03 Cognition =
infrastructure de la cognition (wiki canonique + Memory Core).

**Conséquence** : le périmètre Cyborg canon = **IT + LD03 Cognition**.
Le triplet 21 est confirmé par ADR-L2-AAAS-001 — la présomption
tour 1 est levée.

## L'absorption W40 §M1+M2 vs AaaS — relecture

Le rapport tour 1 a noté comme **présumée** l'absorption W40 §M1+M2
(IT infra absorbé à L0 Rick, Cyborg devient R&D External
Discovery). En relecture AaaS :

- **ADR-L2-AAAS-001 ne tranche pas** l'absorption. Il place Cyborg
  dans 3 variants comme IT canonique, pas comme *R&D External
  Discovery*.
- **L'absorption reste présumée**, non vérifiée par la lecture AaaS.
- Mais **si l'absorption était confirmée**, Cyborg deviendrait
  *uniquement* R&D External Discovery (LD03 Cognition), perdant
  IT infra (qui migrerait à L0 Rick). Les 3 AaaS variants
  devraient alors re-attribuer IT à un autre capitaine B2 — pas
  trivial.

**Statut** : la mutation W40 reste une **remontée B1**. AaaS ne
la tranche pas ; AaaS rend la mutation plus *risquée* (perte de
lead IT partagé dans 3 variants simultanés).

## Anti-pièges

- **Cyborg = uniquement IT.** Faux. AaaS étend Cyborg à LD03
  Cognition (R&D / infrastructure de la cognition).
- **Solaris AaaS = Life-OS-2026 uniquement.** Faux. Solaris
  est *l'ancre canonique* du triplet Book + Saru + Burnham, pas
  un projet isolé.
- **Cyborg absorbé à L0 Rick par W40.** Présumé, pas tranché.
  AaaS rend cette absorption plus compliquée, pas plus simple.
- **Pondérations 60/30/10 par variant comme règle.** Ce sont des
  *projections*, pas des observations. À vérifier en cycle.
- **Triplet 58 amplification déjà adoptée.** Pas tranchée. AaaS
  la *valide implicitement* par les 4 leviers Solarpunk, mais le
  Council n'a pas formellement adopté l'amplification.

## Liens

- [[cyborg-domain-it-perimetre-frontieres]] — le périmètre IT canonique
- [[cyborg-veto-cloud-only-sortie]] — le veto (motif triple)
- [[cyborg-jtbd-emit-receive-kang-dynasty]] — les 6 formes de paquets
- [[cyborg-souverainete-apres-adr-omk-004]] — sister doctrine Cloud pivot
- [[b2-cyborg-it-agent]] — sister ADR-OMK-004 + ADR-L2-AAAS-001
- [[ADR-L2-AAAS-001]] — la doctrine AaaS canonique (ACCEPTED 2026-06-21)
- [[ADR-OMK-004]] — le pivot Cloud (RATIFIED 2026-06-19)

## Note de confiance

**Confirmé par machine** pour le placement Cyborg dans les 3
variants AaaS (ADR-L2-AAAS-001 §D2 lu verbatim). Les pondérations
60/30/10 par forme de paquet sont **projetées** depuis la doctrine
IT et le triplet 21 — non observées en cycle. L'extension du
périmètre Cyborg à LD03 Cognition (R&D) est **confirmée** par la
lecture AaaS — la présomption tour 1 est levée. L'absorption W40
reste **présumée**. Le couplage renforcé IT × Finance est
*validé implicitement* par les 4 leviers Solarpunk — pas formellement
adopté par le Council.
