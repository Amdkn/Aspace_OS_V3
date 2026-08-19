---
type: Concept
title: JohnJones — squad Illuminati, effectif 6 (Coach OS) ou 7 (canonique 53-roster), divergence non arbitrée
description: La squad Illuminati compte 6 techniciens dans Coach OS (BlackBolt, IronMan, MrFantastic, Namor, ProfessorX, DoctorStrange), contre 7 attendus dans le canonique 53-roster. La divergence n'est pas tranchée par un packet mésoperpétuel visible. Trois triplets OMK (18, 19, 20) citent 6 techniciens, le triplet 21 mentionne 7 attendues par Ownerbook T1 DoD-1. Le 7ᵉ agent n'est pas nommé.
tags: [b2, johnjones, sales, illuminati, effectif, 6-ou-7, divergence, squad]
generated: { by: minimax-m3, at: 2026-08-19T04:25:00Z }
verified:
  - { by: process:lecture-corpus-sales, at: 2026-08-19T04:25:00Z }
sources:
  - id: vp-agent-sales
    resource: "C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os/04_Business_Domains/04_Sales_et_Cognition_MartianManhunter_Illuminati/VP_AGENT.md"
    title: VP_AGENT — squad Illuminati 6 techniciens
    last_modified: 2026-08-02
  - id: triplet-18-martian
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 18 — Martian Manhunter pairedWith Illuminati"
    last_modified: 2026-08-17
  - id: triplet-19-superman
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 19 — Superman pairedWith Guardians (6 agents)"
    last_modified: 2026-08-17
  - id: triplet-21-canard-count
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/fifty-three-b3-agent-roster.md"
    title: "Triplet canonique 53-roster — Ownerbook T1 DoD-1 attend ≥ 7 agents par squad"
    last_modified: 2026-08-17
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — Mapping Sales = 02 = JohnJones/Illuminati
    last_modified: 2026-08-17
okf_version: "0.2"
---

# JohnJones — squad Illuminati, effectif 6 ou 7

## Les 6 techniciens de Coach OS

`VP_AGENT.md` §« Mon squad — Illuminati » liste verbatim 6
techniciens avec leurs périmètres respectifs :

| # | Technicien | Charge | Ce qu'il décide |
|---|---|---|---|
| 1 | **BlackBolt** | Closer | Parle peu, conclut. Décide du moment de la demande. |
| 2 | **IronMan** | Demo | La démonstration. Décide de ce qu'on montre et de ce qu'on tait. |
| 3 | **MrFantastic** | Discovery | L'entretien de découverte. Décide des questions posées. |
| 4 | **Namor** | Negotiation | La négociation. Décide du plancher et de ce qui s'échange contre quoi. |
| 5 | **ProfessorX** | BuyerRead | La lecture de l'acheteur. Décide du modèle mental en face. |
| 6 | **DoctorStrange** | Forecasting | Le prévisionnel de pipeline. Décide de ce qui est probable. |

## L'attendu canonique 7 — Ownerbook T1 DoD-1

`fifty-three-b3-agent-roster.md` §« Répartition par squad » pose la
table canonique :

> | Squad | B2 captain | Agent count (estimé) |
> | Illuminati | JohnJones (Sales) | ~7 |

Le verbatim est *« ~7 »* — pas 7 strict. Ownerbook T1 DoD-1 attend
*« ≥ 7 agents par squad »* (cf. `fifty-three-b3-agent-roster.md`
§« Le 53 — pourquoi ce nombre »).

C'est l'invariant canonique : **chaque squad B3 doit avoir au moins
7 agents**. Coach OS V3 livre 6 pour Illuminati, contre 6 pour
plusieurs autres squads (Guardians, Thunderbolts, Kang Dynasty —
cf. triplets 19, 20, 21).

## La divergence — trois triplets OMK disent 6

Les triplets OMK pour les squads citent toutes **6 noms** :
triplet 18 (Martian Manhunter/Illuminati), triplet 19
(Superman/Guardians), triplet 20 (WonderWoman/Thunderbolts), triplet
21 (Cyborg/KangDynasty). Seul triplet 22 (Aquaman/Eternals) cite 10
noms — Aquaman est sur-doté, les autres squads sont sous-dotées.

**Le 7ᵉ agent Illuminati n'est pas nommé** dans le corpus visible.
Trois hypothèses explicites :

1. **Un agent dormant**, jamais activé parce que Coach OS V3 n'a pas
   encore de matière suffisante sur Sales.
2. **Un agent prévu mais non créé**, dont le profil `_doctrine/agents/`
   n'a pas été écrit.
3. **Une erreur de comptage Ownerbook** : le DoD-1 attend ≥ 7 sans
   garantir qu'il y en a 7.

`fifty-three-b3-agent-roster.md` §« Le 53 — pourquoi ce nombre »
est explicite : *« Le nombre 53 est assertif, pas calculé. »* Le
« ≥ 7 » est un invariant formulé avant d'être compté. Si le
comptage exhaustif révèle 6 réels, c'est l'invariant qui doit
s'ajuster, pas le comptage.

## Quelle squad 7ᵉ agent pour Illuminati ?

Si un 7ᵉ agent était ajouté, la charge manquante la plus probable
(lecture du périmètre Coach OS V3 et de la pratique documentée) :

- **CycleOps / PipelineHygiene** — un agent qui tient la qualité du
  pipeline (cleanup, déduplication, refresh des données CRM).
  C'est une charge que MrFantastic (Discovery) et DoctorStrange
  (Forecasting) ne portent pas explicitement.
- **SalesEnablement / Coaching** — un agent qui forme les
  commerciaux sur la doctrine Sales (reformulation-validée,
  scope, etc.). C'est une charge People (Green Lantern) en
  transverse, mais Sales pourrait avoir son propre coach interne.

Le Ownerbook T1 ne tranche pas. C'est un **trou canonique** à
signaler à B1+ (Persones) ou à Summers.

## Le rôle canonique vs le rôle observé

`b2-b3-jtbd-handoff-contract.md` §« Le rôle du B3 squad lead » pose
le squad lead comme tenant du `scrums.md` du sprint. Pour
Illuminati, le squad lead n'est **pas explicite** dans Coach OS V3.

Trois candidats au squad lead Illuminati :

1. **MrFantastic** (Discovery) — le seul technicien qui apparaît
   dans 3 des 4 sprints (S1, S2, S3). Cohérent avec un lead qui
   pilote la séquence discovery → reformulation → validation.
2. **ProfessorX** (BuyerRead) — le seul à apparaître en S1 et S3
   (en support). Plus transverse, plus consultant.
3. **DoctorStrange** (Forecasting) — apparaît en S4. Trop tardif
   pour un lead.

L'absence de squad lead explicite est un **trou** à signaler. Si
MrFantastic est lead, sa charge de discovery se cumule avec la
tenue du `scrums.md` — un conflit d'horizon possible.

## Comparaison effectif B3 — Coach OS V3 vs canonique

| Squad | Coach OS V3 | Canonique | Écart |
|---|---|---|---|
| Illuminati (Sales) | 6 | ~7 | **-1** |
| Guardians (Growth) | 6 | ~7 | -1 |
| Thunderbolts (Finance) | 6 | ~7 | -1 |
| Kang Dynasty (IT) | 6 | ~7 | -1 |
| Fantastic Four (Ops) | 4 | ~4 | 0 |
| Avengers (Product) | 7 | ~7 | 0 |
| X-Men (People) | 8 | ~7 | +1 |
| Eternals (Legal) | 10 | ~7 | +3 |

Pattern : les 4 squads sous-dotées (Illuminati, Guardians,
Thunderbolts, Kang Dynasty) sont **les 4 qui sont en cours
d'activation** dans Coach OS V3. Les squads à effectif conforme ou
sur-doté sont celles dont la doctrine est plus mature (Avengers,
X-Men) ou dont le périmètre est plus petit (Fantastic Four) ou
spécifique (Eternals).

Conséquence : **Illuminati est sous-doté par rapport au canonique,
mais cohérent avec le pattern « squads en activation »**. La
divergence n'est pas un défaut Coach OS, c'est une **non-maturité**
du domaine Sales.

## Anti-pièges

- **Compter 7 sans nommer le 7ᵉ.** Le canonique *« ≥ 7 »* est un
  invariant, pas un comptage. Si le 7ᵉ n'est pas nommé, il n'est
  pas compté.
- **Prendre BlackBolt ou Namor pour le 7ᵉ.** Les 6 listés par
  Coach OS sont déjà BlackBolt, IronMan, MrFantastic, Namor,
  ProfessorX, DoctorStrange. Le 7ᵉ est **différent**.
- **Changer l'effectif sans packet mésoperpétuel.** L'effectif B3
  est documenté par Ownerbook T1. Le modifier sans Council ni
  amendement Ownerbook casse la traçabilité.
- **Croire que l'écart est un défaut Coach OS.** L'écart est
  cohérent avec le pattern squads en activation. La divergence
  est une **non-maturité**, pas une faute.

## Liens

- [[fifty-three-b3-agent-roster]] — le canonique 53-roster
- [[eight-domain-avengers-wheel]] — le mapping B2 → B3
- [[b2-b3-jtbd-handoff-contract]] — le contrat qui exige un squad
  lead nommé
- [[johnjones-domaine-sales-perimetre]] — le périmètre qui sous-tend
  les 6 charges
- [[johnjones-jtbd-emit-receive]] — la répartition des 6 charges sur
  les 4 sprints

## Note de confiance

**Confirmé par machine, à moitié.** Les 6 techniciens Coach OS sont
tirés verbatim de `VP_AGENT.md`. Le canonique ~7 est tiré verbatim
de `fifty-three-b3-agent-roster.md`. Les triplets OMK (18-22) sont
cités verbatim. La divergence 6 vs ~7 est **documentée et non
arbitrée**. L'identification du 7ᵉ agent candidat
(CycleOps/PipelineHygiene ou SalesEnablement/Coaching) est
**projetée** depuis la pratique documentée — non étayée par un
triplet canonique. La comparaison effectif Coach OS V3 vs
canonique est **recalculée** depuis Coach OS (OMK et triplets) —
pas citée comme un tableau dans le corpus.