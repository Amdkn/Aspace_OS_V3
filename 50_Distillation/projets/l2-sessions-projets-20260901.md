---
id: l2-sessions-projets-20260901
titre: "Projets — distillation L2 des 2 325 sessions (angle PARA projets), OKF v0.2"
seau: projets
okf_version: "0.2"
created: 2026-09-01
sources:
  - id: methode
    resource: "50_Distillation/METHODE.md"
    title: "Playbook de distillation (extraction scriptée 100 % + délégation)"
    last_modified: 2026-08-17
  - id: sessions-map
    resource: "50_Distillation/_substrat/05_Sessions.jsonl"
    title: "Carte des 2 325 sessions (2026-03-08 → 2026-08-28), traitement scripté 100 %"
    last_modified: 2026-08-31
  - id: picard-map
    resource: "50_Distillation/_substrat/01_Projects_Picard.jsonl"
    title: "Substrat du seau 01_Projects_Picard — 938 entrées (2026-03-24 → 2026-07-15)"
    last_modified: 2026-08-17
  - id: partiels
    resource: "50_Distillation/_partiels/_tous_partiels.md"
    title: "10 analyses de tranches (250 intentions chacune, T10 : 57)"
    last_modified: 2026-08-31
  - id: index-projets
    resource: "50_Distillation/projets/index.md"
    title: "Index du bundle projets — 20 concepts OKF v0.2 existants"
    last_modified: 2026-08-17
verified:
  - { by: process:python-jsonl-aggregation, at: 2026-09-01 }
---

> **Niveau de confiance : mesuré sur les cartes JSONL, supposé pour le contenu
> des sessions.** Aucun `.md` de session brute n'a été ouvert (interdit du
> brief). Toutes les volumétries ci-dessous proviennent d'un traitement
> scripté de `05_Sessions.jsonl` (2 325 lignes) et `01_Projects_Picard.jsonl`
> (938 lignes), exécuté le 2026-09-01 ; les lectures qualitatives viennent de
> `_partiels/_tous_partiels.md` (10 tranches déjà distillées).

# Ce que les 2 325 sessions disent des projets

## 1. La trajectoire V2 → V3, mesurée par mois

Mentions de `ASpace_OS_V2` / `ASpace_OS_V3` dans la carte des sessions
(`05_Sessions.jsonl`, comptage sur titre + plan + frontmatter) :

| Mois | Sessions | V2 | V3 |
|---|---:|---:|---:|
| 2026-03 | 2 | 0 | 0 |
| 2026-04 | 6 | 0 | 0 |
| 2026-05 | 61 | 31 | 0 |
| 2026-06 | 244 | 41 | 0 |
| 2026-07 | 1 124 | 25 | 3 |
| 2026-08 | 888 | 32 | 21 |

Lecture : V3 naît le **2026-07-09** (`_partiels/_tous_partiels.md`, tranche 2 :
« création de `C:/Users/amado/ASpace_OS_V3/` »), mais **V2 reste cité plus
souvent que V3 jusqu'à fin août** — la migration est déclarée, pas terminée.
Les tranches 1-2 confirment : « tout pointe vers `ASpace_OS_V2` » ; les tranches
7-10 montrent les premières explorations V3 (tranches 8-10).

## 2. Chronologie des projets nommés dans les sessions

Première et dernière occurrence du mot-clé dans la carte
(`05_Sessions.jsonl`, traitement du 2026-09-01) :

| Projet | n sessions | Période |
|---|---:|---|
| Wargames (WF1/WF2, lenses, wargame-runner) | 118 | 2026-07-06 → 2026-08-14 |
| OMK (Dashboard, Business OS, Nexus) | 100 | 2026-05-15 → 2026-08-17 |
| Coach OS (refonte, 19 apps) | 50 | 2026-07-25 → 2026-08-24 |
| Summer's Verse fractal | 35 | 2026-05-21 → 2026-08-02 |
| Solaris | 18 | 2026-05-09 → 2026-08-05 |
| ABC OS | 11 | 2026-06-02 → 2026-06-14 |
| 100M Offer / ONK BOS Nexus | 6 (100M) | 2026-06-03 → 2026-07-16 |
| Alykaly / kalybana | 5 + 7 | 2026-04-29 → 2026-07-15 |
| PocketDB | 3 | 2026-08-04 (une seule journée) |
| Bench Studio | 1 | 2026-08-16 |

Attention : ce comptage porte sur les **titres extraits** des sessions, pas sur
leur contenu intégral — un projet traité dans une session au titre neutre est
sous-compté. C'est une borne basse, pas un inventaire.

## 3. Ce que le substrat Picard dit (et ne dit pas)

`01_Projects_Picard.jsonl` : 938 fichiers, 2026-03-24 → 2026-07-15, **0
concept OKF** (`okf: null` partout). Répartition par dossier racine :

- `04 Alikaly Bana Holding to LLC` — 208
- `03_RILCOT_Members_Space_OS` — 201
- `05 marina Cleaning BOS & SOP` — 195
- `02 ABC OS & Child Care BOS` — 193
- `01-omk-business-os` — 137
- `Cerritos_Plane_Onboarding` — 3, `ClaudeClaw Agent` — 1

Les projets de la deuxième vague (coach-os, Bench Studio, PocketDB, wargames,
100M Offer) **n'apparaissent nulle part dans le seau Picard** : ils vivent dans
`30_Business_OS/09_Blueprints/coach-os-refonte/` (194 .md), `_ARCHIVE_coach-os-briefs/`
(154), et hors corpus (`openwiki/`) — cf. cartographie dans `ASpace_OS_V3/CLAUDE.md`.
Le « seau projets » des sessions n'est donc **pas** `01_Projects_Picard` :
Picard s'arrête au 15 juillet, les sessions continuent jusqu'au 28 août.

## 4. Les apprentissages transverses

1. **Le pic de projet date du 21 mai 2026** — instantiation du premier
   Summer's Verse fractal complet (J01-J04 Jerry), bibliographies LD01-LD08,
   projet Alykaly/kalybana le même jour (`_partiels/_tous_partiels.md`,
   tranche 1 ; `05_Sessions.jsonl` : 35 sessions « Summer » dont la première
   le 2026-05-21). Les quatre Summer's Verse sont GRADUATED sur plan le
   2026-05-21 mais zéro client onboardé (`projets/index.md`,
   summers-verse-framework, abc-os-child-care-bos).
2. **La graduation sur plan sans graduation réelle est le motif dominant** :
   ABC OS « armatur architecturale complète, zéro client onboardé », Marina «
   4 SOPs rédigées non exécutées », 12WY « structure Lead_Lag_Logs/ jamais
   peuplée » (`projets/index.md`). Le corpus produit des OS, pas des
   opérations.
3. **Coach OS est le projet le plus dense et le plus douloureux** : 50
   sessions sur un mois (07-25 → 08-24), refonte 19 apps React 19, salves de
   correctifs QA, puis le diagnostic « mon Agent OS est un Fiasco complet »
   (6 917 mots, outlier de la tranche 8, le 2026-08-09). Les briefs datés
   09-17 août sont archivés dans `_ARCHIVE_coach-os-briefs/` (154 .md).
4. **La masse des sessions juillet-août n'est pas du travail de projet** :
   ~45 stubs Multica de 70 mots (tranche 3), ~150 sessions EXPANSION MODE
   tick-cron (tranche 5), « sept cadences » ×28, MODE FABLE ×50 le 19 août
   seul, GARDE-FOU ×~70 au total (tranches 8-10). Sur 2 325 sessions, la
   diversité réelle de juillet tient dans quelques dizaines d'intentions
   uniques — la redondance de briefs est le principal occupant du seau.
5. **Les 938 fichiers Picard portent des structures, pas des concepts** :
   `okf: null` sur 100 % du substrat ; la consolidation OKF (20 concepts,
   `projets/index.md`) a été faite par les distillations précédentes, pas par
   les projets eux-mêmes.

# Contradictions détectées

- **Compte du seau Picard** : `projets/index.md` annonce « 2154 .md » dans le
  seau, le substrat `01_Projects_Picard.jsonl` n'en contient que 938. L'index
  lui-même explique l'écart par 1 208 sorties générées `graphify-out/`
  (≈946 écrits à la main) — mais 938 ≠ 946, l'écart résiduel n'est pas
  expliqué. Non tranché.
- **Frontière du seau** : le brief nomme coach-os, Bench Studio, PocketDB,
  wargames, 100M Offer comme projets du seau ; aucun de ces noms n'apparaît
  dans `01_Projects_Picard.jsonl`. Soit le seau PARA ne capture plus les
  projets après juillet, soit ces projets relèvent d'autres seaux. Non tranché.
- **Trajectoire V2/V3** : V3 est déclaré fondé le 2026-07-09 (`AGENTS.md`,
  canon du 2026-08-02 : « V2 est la mémoire, V3 est le runtime »), mais V2
  reste plus cité que V3 dans les sessions d'août (32 vs 21) et les sessions
  coach-os d'août travaillent sur des dépôts hors des deux (`C:\Users\amado\coach-os`,
  dépôt git imbriqué — tranche 5). Non tranché.
- **Graduation** : Summer's Verse status « GRADUATED 2026-05-21 »
  (`projets/index.md`) alors que la tranche 1 montre le fractal encore en
  développement après cette date (J01-J04 développés fin mai, extensions
  jusqu'au 2026-08-02). Gradué sur plan vs actif en sessions. Non tranché.
- **Sessions vs intentions** : le rapport d'intentions mesure 2 307 sessions
  analysées (`ASpace_OS_V3/CLAUDE.md`), la carte du substrat en compte 2 325
  (`05_Sessions.jsonl`). Écart de 18 non expliqué ici. A SOURCER.

# Couverture réelle déclarée

- **Lu intégralement (scripté)** : `05_Sessions.jsonl` (2 325/2 325 lignes),
  `01_Projects_Picard.jsonl` (938/938 lignes), `METHODE.md`,
  `projets/index.md`, `_partiels/_tous_partiels.md` (digest des 10 tranches).
- **Non lu** : les 2 325 fichiers `.md` de sessions brutes (interdit du brief),
  les 20 concepts existants du bundle un par un, `50_Distillation/index.md`.
- **Portée** : les citations qualitatives des tranches sont de seconde main
  (digests) ; les volumétries sont de première main (script Python sur les
  JSONL, exécuté 2026-09-01). Les comptages par titre sont des bornes basses.