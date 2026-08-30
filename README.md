# A'Space OS V3

> **Loi L0 — Rick.** *Un système qui ne sait pas se répliquer n'est pas un système, c'est un
> document.* Von Neumann : ruban + constructeur + copieur + contrôleur.
> Conway : trois règles suffisent, la complexité émerge, jamais déclarée.

**V2 est la mémoire. V3 est le runtime.**

---

## État au 2026-08-02

**165 dossiers, 350 fichiers réels.** Tout ce qui existe ici sert au fonctionnement.

| Zone | Fichiers | État |
|---|---|---|
| `10_Tech_OS/` | 72 | noyau exécutable + réplicateur + 3 Cores engendrés |
| `20_Life_OS/` | 249 | arbre canonique complet, **34 unités A3** équipées |
| `30_Business_OS/` | 204 | structure canonique + **entreprise Coach OS** engendrée (197 f.) |
| `00_Amadeus/` | 71 | Observateur Méta, registres, contrat d'adaptateur |
| `_INBOX/` | 7 | trois portiers |

Les 17 665 fichiers de l'ancienne structuration sont archivés, réversibles, dans
`ASpace_OS_V2\...\04_Archives_Data\_V3_STRUCTURE_2026-08-02\` (manifeste de 471 entrées).

## Arborescence

```
_INBOX/                          admission — S1_Rick · A1_Beth_Morty · B1_Jerry_Summers
00_Amadeus/                      A0 Observateur Méta
  10_Observers/                  opik · agentpulse · aios · agents-observe · phoenix · langsmith · agent-os
  20_Harness/                    ADAPTER.md · ORG.json · registres
  30_Shadow/ 40_Predictions/ 50_Bench/ 60_Tape_Specs/ 70_Skills/ 90_Doctrine/
10_Tech_OS/
  00_Governance_Rick/            LAW · CASCADE · PLAYBOOK · AGENT · SOUL · replicator/ · Donna_DLQ/
  kernel/                        uc · harness · gate · review · dlq · bridge_paperclip
  11_Kernel_Core_13th/           13e — maître de 10_Tech_OS
  12_Life_Core_11th/             11e — maître de 20_Life_OS
  13_Buzz_Core_12th/             12e — maître de 30_Business_OS
20_Life_OS/                      6 frameworks + gatekeepers + blueprints
30_Business_OS/                  8 domaines
  10_Projects/coach-os/          entreprise — Summers CEO · 8 VP DC · 53 techniciens Marvel
```

**Rien ne se crée à la racine.** Ce qui n'est ni Tech, ni Life, ni Business va dans `00_Amadeus/`.

## Les quatre organes — tous exécutables

| Organe | Fichier | Rôle |
|---|---|---|
| Ruban φ | `00_Amadeus/60_Tape_Specs/` | la description |
| Constructeur A | `kernel/harness.py` · `worker_example.py` | bâtit depuis le ruban |
| Copieur B | `00_Governance_Rick/replicator/spawn.py` | duplique sans interpréter |
| Contrôleur C | `kernel/uc.py` · `gate.py` · `review.py` · `dlq.py` | admet, revoit, **détache** |

### Les lois, tenues par la base

| Loi | Mécanisme |
|---|---|
| **Prédiction** | trigger SQL — pas de `review`/`done` sans prédiction préalable |
| **Détachement** | trigger SQL — `done` seulement depuis `review`, preuve par critère |
| **Bail** | `reap` — un agent qui meurt rend son travail |
| **Ruban** | `gate.py` — critère non vérifiable, la note repart avec le motif |
| **Réplication** | `spawn.py` — un Core ne s'écrit pas, il s'engendre |

Les quatre premières sont tenues par la machine. La cinquième par Rick.

### Cycle complet

```bash
python 10_Tech_OS/kernel/gate.py run        # le portier admet ou refuse
python 10_Tech_OS/kernel/worker_example.py --harness cc --layer L2 --max 1
python 10_Tech_OS/kernel/review.py run      # preuves exigées, puis détachement
python 10_Tech_OS/kernel/dlq.py rapport     # ce qui attend Rick
python 10_Tech_OS/kernel/bridge_paperclip.py scan   # échecs L2 → Donna → Rick
```

## Hiérarchie et cascade

`ORG.json` fait foi · détail dans `10_Tech_OS/00_Governance_Rick/CASCADE.md`.

| Rang | Rôle E-Myth | Artefact | Cycle |
|---|---|---|---|
| **S1 Rick** | Entrepreneur | `PLAYBOOK.md` | 12WY |
| **S2 les 3 Docteurs** | Manager | `ROADMAP.md` | mensuel |
| **S3 les 9 compagnons** | Technicien | `RUNBOOK.md` | hebdomadaire |
| **Donna** | Gatekeeper du visionnaire | — | à l'événement |

Un rang ne produit jamais l'artefact du rang voisin. Ce qui remonte n'est jamais une décision :
seulement un fait — un échec avec son motif, une prédiction avec son résultat.

**Cascade amont** — A1 Beth·Morty `H+3 ans` → A2 les 6 frameworks `H+1 an` → A3 les officiers
`12WY` → B1 rocks mensuels → B2 8 VP `4 sprints` → B3 squads Marvel `5 scrums/sprint`.

Trios canoniques : `Doctor_13_Yaz_Ryan_Graham` · `Doctor_11_Amy_Rory_River` ·
`Doctor_12_Clara_Nardole_Bill`.

## Harness

| Couche | Harness | État |
|---|---|---|
| `L0` | **Multica** 0.4.4 | **14 agents · 4 squads** — instructions complètes |
| `L1` | **Buzz** | shim PATH · pack `aspace-life-core` validé — **agents A1/A2/A3 à créer** |
| `L2` | **Paperclip** 2026.722.0 | **en ligne** `127.0.0.1:3100` · garde-fous posés |
| `A0` | Hermes · CC | skill `aspace-orchestrate` |

Contrat commun : `00_Amadeus/20_Harness/ADAPTER.md` — cinq verbes, quatre obligations,
trois épreuves de conformité.

### Garde-fous Paperclip

| | |
|---|---|
| Modèle par défaut | **MiniMax-M3[1m]** — 8 variables sur l'environnement `Local` (`defaultForInstance`) |
| Plafond mensuel | 5 000 ¢ · **hard stop actif** · alerte à 80 % |
| Approbation des nouveaux agents | requise |
| Exposition | `private`, loopback uniquement |
| Échec répété | → `bridge_paperclip.py` → Donna → Rick |

## Life OS — arbre canonique

**34 unités A3**, chacune avec sa spec V2 copiée, son `SOUL.md` et son `AGENT.md` engendrés
depuis cette spec.

| Framework | A2 | Unités A3 |
|---|---|---|
| `21_Ikigai_Orville` | Orville | 4 piliers + 5 horizons |
| `22_Wheel_Discovery` | Discovery ZORA | LD01 → LD08 |
| `23_12WY_SNW` | Curie SNW | Pike · Una · M'Benga · Chapel · Ortegas |
| `24_PARA_Enterprise` | Computer | Picard · Spock · Geordi · Data |
| `25_GTD_Cerritos` | HoloDeck | Mariner · Boimler · Rutherford · Tendi · Freeman |
| `26_DEAL_Protostar` | HoloJaneway | Dal · Rok-Tahk · Zero · Gwyn |

PARA n'existe que dans `24_PARA_Enterprise` — c'est un framework, pas une méta-couche.

### LD01 Book — la distillation des guides

`22_Wheel_Discovery/LD01_Business_Book/01_Guides_Business/` · délégué à **MiniMax-M3**, vérifié
par A0 le 2026-08-02 (`_VERIFICATION_A0.md`).

**15 561 guides** de `03_Resources_Geordi/01_Guides/` indexés mécaniquement
(`_INDEX_GUIDES.tsv`), puis distillés en **8 fichiers**, un par domaine Business.
Classement à **89 % de confiance haute**. 806 guides hors périmètre, aucun supprimé.

Le corpus est à **74,7 % du domaine 7 R&D & IT** — conforme au pivot W40 qui donne la veille à
Cyborg. Deux angles morts documentaires signalés : Sales & Cognition (0,9 %) et Legal (0,4 %).

## Business OS — l'entreprise Coach OS

`30_Business_OS/10_Projects/coach-os/` · engendrée le 2026-08-02 · **196 fichiers**
Canon `ADR-CANON-001` : 8 B2 + 8 squads B3 + **53 B3**.

| Rang | Qui | Rôle E-Myth | Artefact | Cycle |
|---|---|---|---|---|
| **B1** | Summers, CEO | Entrepreneur | `ROCKS.md` | 1 rock/mois, 3/12WY |
| **B2** | les 8 VP (héros DC) | Manager | `SPRINTS.md` | 4 sprints/mois |
| **B3** | les 53 techniciens (squads Marvel) | Technicien | `SCRUMS.md` | 5 scrums/semaine |

| # | Domaine | VP | Squad | B3 |
|---|---|---|---|---|
| 1 | RH & Méta Gouvernance | Green Lantern | X-Men | 8 |
| 2 | Opérations en Loops | Batman | Fantastic Four | 4 |
| 3 | Productization des Besoins | Flash | Avengers | 7 |
| 4 | Sales & Cognition | Martian Manhunter | Illuminati | 6 |
| 5 | People & Brand | Superman | Guardians | 6 |
| 6 | Finance & ROI | Wonder Woman | Thunderbolts | 6 |
| 7 | R&D & IT | Cyborg | Kang Dynasty | 6 |
| 8 | Legal & Compliance | Aquaman | Eternals | 10 · **dormant** |

`coach-os/ORG.json` fait foi. L'arborescence **s'engendre** — le moule est dans
`coach-os/02_Meta_Factory/spawn_coach_os.py`.

Deux statuts particuliers : le domaine **7 R&D & IT** porte le pipeline de veille depuis le
pivot IT→R&D (spec W40, 2026-07-13) — guides YouTube → distillation 8 domaines → Last30days →
**≤3** améliorations/mois. Le domaine **8 Legal** est dormant jusqu'au premier fichier déposé
dans `00_Summers_CEO/03_Master_Agreements/`.

## La mémoire est dans V2

```
ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\
```

Point d'entrée `03_Resources_Geordi/CLAUDE.md`. Les 4 piliers : **OKF** · **Wiki** ·
**Graphify** · **Dox**. Un fichier qui n'exécute rien et contre lequel rien ne s'exécute
appartient à Geordi, pas ici.

## Prochaine étape

**Créer les agents A1, A2, A3 de Life OS dans Buzz**, organisés en **teams par channels** —
A1 Beth·Morty en gatekeepers, A2 les six frameworks, A3 les 34 unités. C'est la couche L1 qui
alimente le playbook de Rick. *Bloqué* : la mise à jour de Buzz a retiré l'import de personas
`.md` au profit de snapshots `.agent.json` dont le schéma n'est pas documenté.

Ensuite : brancher le cycle **Last30days** du domaine 7 de Coach OS sur les 8 distillations —
≤3 améliorations actionnables par mois, candidates au rock de Summers.

## ⚠ Secrets publiés

Ce dépôt a un remote GitHub. Son historique contient au moins 11 fichiers porteurs de
credentials, poussés via le commit `41c19a5`. **Faire tourner ces clés** est prioritaire sur
toute réécriture d'historique — celle-ci ne révoque rien. Ne rien pousser avant.

Licence : **MIT**.
