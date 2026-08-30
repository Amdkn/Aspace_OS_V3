---
type: Playbook
title: Le prototype de franchise reproductible — ownerbooks et runbooks
description: Comment `01-omk-business-os` sert de gabarit aux quatre autres projets Picard, quelle est la seule variable qui les distingue reellement, et pourquoi les recus D1 du prototype ne se recopient pas.
tags: [franchise, ownerbook, runbook, picard, jerry, triptyque, para, b2, b3]
generated: { by: claude-opus-5, at: 2026-08-30T00:40:00Z }
verified:
  - { by: claude-opus-5, at: 2026-08-30T00:40:00Z }
sources:
  - id: prototype
    resource: "ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os"
    title: Le prototype — 3 ownerbooks, 2 runbooks, 24 chartes cycle 2
    last_modified: 2026-08-30
  - id: north-stars
    resource: "01_Projects_Picard/*/B1_Summer_Direction/01_NORTH_STAR_1Y_3Y_10Y.md"
    title: Les North Star des 4 projets cibles — source du mode de franchise
    last_modified: 2026-05-26
  - id: generateur
    resource: "ASpace_OS_V3/scripts/franchise_ownerbooks.py"
    title: Le generateur, execute le 2026-08-30 — 30 documents
    last_modified: 2026-08-30
okf_version: "0.2"
---

# Ce que le prototype fixe

`01-omk-business-os` porte **3 ownerbooks** (T1/T2/T3) et **2 runbooks**. Ensemble
ils forment un gabarit reproductible dont la structure est l'invariant :

| | Ownerbook | Runbook |
|---|---|---|
| Repond a | le QUOI | le COMMENT |
| Structure | 10 sections, de « Scope (1 phrase) » a « specifique a l'instance » | portes de pre-verification, puis M1-Mn, chacun avec sa preuve |
| Frontmatter | `triptyque`, `rock_id`, `b2_owner`, `b3_squad`, `icp`, `12wy_window`, `doctrine_lock`, `mission` | `chart_source`, `rock_id`, `domain`, `doctrine_lock` |

Les trois triptyques recouvrent exactement les huit domaines B2, et la
correspondance a ete verifiee contre les dossiers de chaque projet :

| | Domaines | Escouades B3 |
|---|---|---|
| **T1** | People · Ops · Product | X-Men + Fantastic Four + Avengers |
| **T2** | Growth · Sales · Finance | Guardians + Illuminati + Thunderbolts |
| **T3** | Legal · IT-R&D | Eternals + Kang Dynasty |

# La seule variable de franchise reellement sourcee

Les North Star des quatre projets cibles contiennent des **litteraux PowerShell
non interpoles** — `$(@{Kind=SummerProject; ...; Mode=...; Parent=...}.Name)`.
Le generateur d'origine a echoue a les remplacer, mais les metadonnees sont
dedans, et elles sont vraies :

| Projet | Mode |
|---|---|
| 02_ABC_OS | Orbiter + Compliance |
| 03_RILCOT | Nexus + Community Ops |
| 04_Alikaly | Nexus + Finance/Legal |
| 05_Marina | Orbiter primary, Nexus secondary |

C'est **le** differenciateur. Tout le reste — triptyques, paires
domaine/escouade, cadence, DoD de forme — est invariant par conception. S'il ne
l'etait pas, il n'y aurait pas une franchise mais cinq systemes.

# Pourquoi les recus D1 ne se recopient pas

Le gabarit OMK cite cinq recus reels : `ADR-AAAS-PRICING-001` (paliers USD),
`ADR-NEXUS-NICHE-001` (Coach premium), W40 §2, `phase_c_saas_auth`,
`B2_DEFINITION_OF_DONE_SPEC`. **Aucun n'est valide pour ABC, RILCOT, Alikaly ou
Marina.**

Les instances generees sortent donc leur §3 en `A SOURCER`, avec les quatre
chemins ou chercher. Un ICP « Coach premium US, $7,5-25K ACV » applique a une
societe de nettoyage ne reste pas une erreur de document : il se propage
jusqu'au pricing.

C'est l'application directe de la regle de confiance OKF — une affirmation
mesuree et une affirmation supposee ne doivent jamais se ressembler.

# La repartition Area / Projet

C'est la correction du 2026-08-29, appliquee :

- **Area** `J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/franchise/`
  → le **canon**, `12wy_window: n/a`. Une Area maintient un standard de
  reproduction perpetuel ; lui donner une echeance est la faute.
- **Projets** `01_Projects_Picard/*/ownerbooks|runbooks/`
  → les **instances**, avec fenetre 12WY et `rock_id`. Un projet a une fin.

Les six dossiers de l'axe B sous `03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/`
(`Ownerbooks_Picard`, `Runbooks_Summers`, `Playbooks_Jerry`, `SOPs_B2`,
`Skills_B3`, `Cookbooks_Coaching`) ne contenaient que `.gitkeep`. Ils recoivent
un **pointeur**, pas une copie : ils vivent sous Geordi, donc dans un miroir,
donc une Ressource. Deux exemplaires d'un standard divergent en silence.

# John Jones, encore

Les dossiers portent toujours `02_Sales_MartianManhunter_Illuminati`. La forme
canonique est **John Jones** (arbitrage du proprietaire, regle de date : la
version tardive gagne). Le neuf ecrit `JohnJones` dans `b2_owner` ;
`MartianManhunter` n'y subsiste que comme **chemin disque cite** et comme note
de red-team explicite. Citer un chemin reel n'est pas recopier l'erreur. Le
renommage des dossiers reste a faire.

# Mesure

30 documents ecrits le 2026-08-30 : 6 dans l'Area, 24 dans les 4 projets.
Controle croise mode North Star ↔ frontmatter : **4/4 concordants**.

```bash
python C:/Users/amado/ASpace_OS_V3/scripts/franchise_ownerbooks.py   # simule
python C:/Users/amado/ASpace_OS_V3/scripts/franchise_ownerbooks.py --appliquer
```

# Comment verifier qu'une instance est prete

```bash
grep -c "A SOURCER" ownerbooks/ownerbook_T1_people_ops_product.md   # doit rendre 0
```

Tant que ce compte n'est pas nul, l'instance est **non verifiee** au sens OKF,
et son runbook s'arrete a la porte G3. Executer un runbook dont l'ownerbook
n'est pas source, c'est batir sur une hypothese en croyant batir sur une mesure.

Voir [[multica-governor-module]] pour la panne que ces portes ne doivent pas
rejouer.

**Lacune assumee** : la porte d'argent (`ASpace_OS_V3/scripts/porte_argent.py`),
qui est le filtre d'entree en V3, n'a **pas** encore de concept dans ce bundle.
Elle est citee ici par son chemin, faute de mieux. Poser un `[[lien]]` vers un
concept inexistant aurait menti a l'avenir ; le nommer comme manquant ne ment
pas.
