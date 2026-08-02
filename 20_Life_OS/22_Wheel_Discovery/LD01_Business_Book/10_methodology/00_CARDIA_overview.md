---
type: methodology
title: CARDIA-TDD — Choix par défaut Autonome Réversible Durable Intégratif Antifragile
description: Méthodologie de décision doctorale pour les zones canoniques A'Space (LD01 et sœurs). Synthèse 12WY + OKF + DOX + D4 + Antifragilité (Taleb) + Kardashev-3 + Discovery crew standards. Verrouillée par ADR-LD01-001.
timestamp: 2026-07-04T12:00:00-04:00
domain: LD01_Career_Business
source_doctrines:
  - plan-meta-memoire-okf-wiki-graphify-dox.md §5 (boucle 12WY)
  - plan-meta-memoire-okf-wiki-graphify-dox.md §P4 (DOX bi-famille)
  - plan-meta-memoire-okf-wiki-graphify-dox.md §3.5 (DOX universal Micro-Index)
  - plan-minimax-l1-book-lune.md §0 (organigrammes Doctrine)
  - plan-strategie-cc-l1-zora-macro.md (cadence Planète)
inherits_from:
  - TDD (Beck) — test avant contenu
  - DDD (Evans) — bounded contexts explicit
  - ADR (Coplien) — append-only decisions
novelty:
  - CARDIA = propriétés time-scale-engineered (An 3000 / Kardashev-3)
  - Auto-Évolutif = boucle 12WY W3→W13
---

# CARDIA-TDD — Choix par défaut Autonome Réversible Durable Intégratif Antifragile

> *« Pour un Citoyen de Civilisation des Types de Kardashev natif de l'An 3000 qui intègre l'équipage de Discovery qui voyage vers le Futur. »*

## 0. Posture de fond

CARDIA-TDD est la **méthode de choix par défaut** appliquée à toute mutation dans l'organigramme `LD01_Business_Book/` (et sisters `LD02..LD08`). Ce n'est pas un framework à invoquer — c'est un *réflexe* que le harness (CC, MC, HA, Shadow) doit avoir avant d'écrire un seul octet.

**Hypothèses de cible** :
- Mission longue durée (décennies, pas sprints)
- Crew multi-agents (≥ 3 simultanément actifs)
- Distance lightyear = pas de « undo » post-déploiement
- Stress ambiant : rotation de modèles, churn de skills, migration de plans

> Les 3 canons canon A'Space — OKF, D4 (append-only), 12WY (5 disciplines) — sont **garantis par construction** par CARDIA, pas par discipline du mainteneur.

## 1. Les 6 propriétés CARDIA

| Lettre | Propriété | Mécanisme | Anti-pattern bloqué |
|---|---|---|---|
| **C** | **C**ontext-first | DOX walk : `00_index.md` → `AGENTS.md`/`CLAUDE.md` → module cible | Edit aveugle sur fichier jamais ouvert |
| **A** | **A**utonomie + Additif | Append-only `.md`, `_TRASH/` pour retrait, jamais de `mv` destructif | Hard-delete, rewrite canon |
| **R** | **R**éversibilité | D4 canon + handoff path dans `99_meta/calendar.md` | Mutation invisiblement irréversible |
| **D** | **D**urabilité | `99_meta/rot-rates.md` déclare la péremption de chaque module | Module « éternel » sans examen périodique |
| **I** | **I**ntégration-par-Doctrine | Frontmatter OKF + alignement `plan-*.md` + boucle 12WY | Module isolé du canon |
| **A** | **A**ntifragilité (Taleb) | Stress test = le système gagne (D1 receipt exposé après rotation de modèle, après compaction de contexte, après migration harn. principle) | Système qui se casse sous stress sans apprendre |

## 2. Mapping TDD / DDD / ADR

Les 3 frameworks canoniques sont **projetés dans CARDIA** :

### 2.1 TDD (Test-Driven Development — Beck)

> « Pas de production code sans un test qui échoue d'abord. »

**Transposition CARDIA** : *« Pas de module canonique sans un **D1 receipt** chiffré d'abord. »*

- Le D1 receipt est dans le `## Verification` du frontmatter/module (cf. `20_skeleton/00_module_template.md`).
- Le test peut être : commande PowerShell, `grep`, présence de fichier, valeur numérique — toujours **vérifiable post-création**.
- Si le test échoue à la relecture 4 semaines plus tard → rot → le module a une cadence déclarée.

### 2.2 DDD (Domain-Driven Design — Evans)

> « Modéliser le **domaine** comme premier artefact. »

**Transposition CARDIA** : *« Bounded contexts explicites + ubiquitous language partagé. »*

Bounded contexts reconnus dans cet organigramme :
1. `BC-A3-Book` — agent A3 Book (rôle, identité, inputs/outputs, boundaries)
2. `BC-Project-OMK-Nexus-Coaching` — Project spearhead Picard (`30_Business_OS/10_Projects/omk-nexus-coaching-premium/`)
3. `BC-Guides-LD01-YouTube` — guides YouTube distillés (les 3 fichiers + futurs batches)
4. `BC-Bibliography-6-Livres` — les 6 livres E-Myth / Built to Sell / Who Not How / etc.
5. `BC-AaaS-Solaris-Variant` — branche Kardashev Type 3 (H90 Legacy 1000T)

Ubiquitous language (à propager entre harnesses) :
- **H1 / H3 / H10 / H90** = échelles temporelles de Book (weekly / monthly / quarterly / 36-month horizon)
- **SHADOW_ACTIVE** = status canon Book = « l'agent existe, pas encore exercé en routine »
- **Twin** = `book.twin.md` sister canon, jamais dupliqué
- **AaaS Solaris** = variant Kardashev-3 à anchor Book LD01

### 2.3 ADR (Architecture Decision Records — Coplien)

> « Toute décision architecturale = 1 fichier append-only, immuable, daté. »

**Transposition CARDIA** : *« Toute décision = 1 fichier dans `30_decisions/` au format ADR-LD01-NNN_slug.md. »*

Format (cf. premier ADR canonique) :
1. **Status** : `PROPOSED` → `RATIFIED` (immuable ensuite) ou `SUPERSEDED` (par ADR-NNN+1)
2. **Context** : ce qui motivait la décision
3. **Decision** : l'option choisie + rationale
4. **Consequences** : tradeoffs, notamment ce qui devient plus difficile
5. **Alternatives considered** : 2-3 options écartées + pourquoi

> **Canon A'Space** : un ADR ratifié = **intouchable** sauf par un ADR successeur. C'est le **D4** local.

## 3. La boucle 12WY — moteur de CARDIA

CARDIA n'est pas un one-shot. C'est un **cycle** calé sur le Q3 (12 Week Year) :

```
W3 — cadrage   : scope l'organigramme, fait le D1 baseline
W4 — premier edit : pose 1 ADRs/1 module avec son D1 receipt
W5 — stress test : mute un module sous contrainte (rot modèle, compaction ctx) — observe CARDIA
W6 — re-mesure : drift = 0 ? rot a-t-il déclencé un signal ? calendar.md audité
W7..W9 — operating : les harnesses opèrent normalement, append-only
W10 — pré-mortem : failure modes de CARDIA lui-même, propose ADR successeur si besoin
W11..W12 — finish : passe finale, archives, _TRASH
W13 — release : archive + Muse DEAL · D11 mesuré par Gwyn (plan-meta-memoire §6)
```

## 4. Calendrier de Review (12WY loop complet)

| W | Discipline 12WY | Livrable CARDIA | Critère sortie |
|---|---|---|---|
| W3 | Vision | `00_index.md` + `AGENTS.md` + `CLAUDE.md` posés | 3 fichiers présents, D1 OK |
| W4 | Planning | 1er ADR + 1er module avec squelette | D1 receipt exposé |
| W5 | Process Control | Stress test migration harness | CARDIA passe sans casse |
| W6 | Measurement | Drift = 0 ; rot-rates alignés | Audit daté |
| W7-W9 | Operating | Append-only opérationnel | Appends comptés |
| W10 | Time Use | Pré-mortem CARDIA | Failure modes consignés |
| W11-W12 | Re-mesure | Passe finale | Archive prête |
| W13 | Release | Muse DEAL D11 | D11 mesuré par Gwyn |

## 5. Anti-patterns que CARDIA bloque

| Anti-pattern | Bloqué par | Comment |
|---|---|---|
| Plan markdown à plat qui se périme | **C**ontext-first (DOX walk) + **I**ntégration (`plan-{slug}/` folder) | Toute migration plan = organigramme Doctrine, pas nouveau `.md` |
| Hard-delete d'un canon | **A**dditif + **R**éversibilité (D4) | `_TRASH/` + ADR |
| Module sans péremption | **D**urabilité | `rot-rates.md` |
| Module orphelin du canon | **I**ntégration | Frontmatter pointe ses sources |
| Système qui se casse sous stress | **A**ntifragilité | Stress test W5 |
| Plan textuel caché derrière un outil | **C**ontext-first filesystem | Source = folder, pas `.claude/CLAUDE.md` |

## 6. Héritages et inspirations

- **TDD** (Kent Beck, 2002) — *Test-Driven Development by Example*
- **DDD** (Eric Evans, 2003) — *Domain-Driven Design*
- **ADR** (Michael Nygard, 2011) — *Documenting Architecture Decisions*
- **Antifragile** (Nassim Taleb, 2012) — *Things That Gain from Disorder*
- **OKF v0.1** (Google Cloud, 2025-2026) — *Open Knowledge Format*
- **DOX** (agent0ai, 2026) — *AGENTS.md bi-famille*
- **12WY** (Moran & Lennington, 2011) — *The 12 Week Year*
- **Discovery crew** (Kubrick, 1968 — *2001: A Space Odyssey*) — esthétique mission longue
- **Kardashev** (Sakharov, 1964 · Kardashev, 1964) — échelles civilisationnelles Type 1/2/3

## 7. Adresses canoniques (chemins de vérité)

| Ressource | Chemin |
|---|---|
| Index racine | `C:\Users\amado\ASpace_OS_V2\20_Life_OS\22_Wheel_Discovery\LD01_Business_Book\00_index.md` |
| AGENTS.md (DOX FS) | `…\LD01_Business_Book\AGENTS.md` |
| CLAUDE.md (DOX harness) | `…\LD01_Business_Book\CLAUDE.md` |
| Squelette-type | `…\LD01_Business_Book\20_skeleton\00_module_template.md` |
| ADR canon | `…\LD01_Business_Book\30_decisions\ADR-LD01-*.md` |
| Manifest cross-harness | `…\LD01_Business_Book\90_manifests\manifest.cross-harness.md` |
| Plan source 1 | `C:\Users\amado\.claude\plans\plan-meta-memoire-okf-wiki-graphify-dox.md` |
| Plan source 2 | `C:\Users\amado\.claude\plans\plan-minimax-l1-book-lune.md` |
| Plan source 3 (matrice Discovery) | `C:\Users\amado\.claude\plans\fancy-hugging-bengio.md` |
| Memory canon mavis | `C:\Users\amado\.mavis\agents\mavis\memory\MEMORY.md` |

---

> **CARDIA-TDD** est verrouillé par `ADR-LD01-001_organigramme_doctrine.md` (2026-07-04, status RATIFIED).
