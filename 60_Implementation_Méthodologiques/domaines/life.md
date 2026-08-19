---
type: Method
title: Méthode Life OS — couche L1 distilled
description: Ce que la couche 20_Life_OS enseigne sur la manière de travailler : rituels, garde-fous, cadences, règles chiffrées, pièges documentés. Ne répète pas les concepts, donne les raisons des règles.
tags: [methode, life-os, rituels, garde-fous, cadences, regles-chiffrees, pieges]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: process:read_local_v2, at: 2026-08-19T00:00:00Z }
sources:
  - id: gatekeepers-readme
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/README.md
    title: 00_Gatekeepers_Beth_Morty README — Operating Law
    last_modified: 2026-06-21
  - id: beth-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md
    title: A1 Beth Spec — Anti-patterns
    last_modified: 2026-05-20
  - id: morty-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Morty_Spec.md
    title: A1 Morty Spec — Output Contract
    last_modified: 2026-05-20
  - id: discovery-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/A2_Discovery_ZORA_Spec.md
    title: A2 Discovery Spec — Decision Boundary
    last_modified: 2026-05-20
  - id: orville-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/21_Ikigai_Orville/A2_Orville_Spec.md
    title: A2 Orville Spec — Context7 Boundary
    last_modified: 2026-05-20
  - id: snw-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/23_12WY_SNW/A2_Curie_SNW_Spec.md
    title: A2 Curie SNW Spec — Acceptance Criteria
    last_modified: 2026-05-20
  - id: cerritos-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/25_GTD_Cerritos/A2_HoloDeck_Cerritos_Spec.md
    title: A2 Holo Deck Cerritos Spec
    last_modified: 2026-05-20
  - id: protostar-spec
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/26_DEAL_Protostar/A2_HoloJaneway_Protostar_Spec.md
    title: A2 Holo Janeway Spec — Acceptance Criteria
    last_modified: 2026-05-20
  - id: a0-reasoning-map
    resource: ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/a0_reasoning_map.md
    title: A0 Reasoning Map
    last_modified: 2026-04-07
okf_version: "0.2"
---

# Méthode Life OS — couche L1 distilled

Cette méthode condense ce que la couche `20_Life_OS/` enseigne sur **la manière de travailler**. Elle ne re-décrit pas les frameworks — pour les détails, voir les concepts `50_Distillation/domaines/life/`.

## 1. Rituels

### 1.1 Resume Protocol — toujours commencer par les gatekeepers

Tout agent qui ouvre un dossier de méthode (Ikigai, Life Wheel, 12WY, GTD, DEAL) commence par :

1. Lire `00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md`.
2. Lire `00_Gatekeepers_Beth_Morty/A1_Morty_Spec.md`.
3. Lire l'A2 spec de la méthode.
4. Inspecter seulement le dossier A3 nommé par le Context Pack.
5. Écrire les findings comme **evidence paths**, pas mémoire de chat.

**Pourquoi** : sans lire Beth/Morty en premier, un agent ignore les 5 états Beth (GREEN/ORANGE/RED/HALT_LD03/HALT_LD04) et peut écrire une décision qui viole un HARD SAFETY sans s'en rendre compte. La lecture Beth/Morty est un **filtre sémantique amont**, pas une formalité.

### 1.2 Sunday Uplink — revue hebdomadaire ritualisée

Le Sunday Uplink est l'unique moment de revue de la semaine : Discovery y consolide le ZORA state, Orville y compile les 9 crew findings Ikigai, Chapel y expose le Scorecard.

**Pourquoi** : un système sans revue hebdomadaire dérive. Les drifts LD04 cognition, LD05 isolation, LD06 bond fracture doivent être détectés avant qu'ils ne forcent un HALT Beth. Le Sunday Uplink est le **seul moment toléré** pour escalader à A0 (board observer passif).

### 1.3 Beth Alignment Log — veto durable

Toute décision Beth écrit dans `Beth_Alignment_Log/`. Pas un journal de chat : un fichier canonique dans le filesystem qui survit aux compactions de contexte.

**Pourquoi** : un veto qui n'est pas écrit peut être contesté. Un veto écrit dans le filesystem est une décision traçable, reversible si Beth re-vérifie.

## 2. Garde-fous

### 2.1 HARD SAFETY — Beth veto automatic

```yaml
beth_thresholds:
  LD03_minimum: 4.0
  LD04_minimum: 3.5
  multi_domain_alert: 3
```

LD03 (Culber Health) < 4.0 → `HALT_LD03` automatic. LD04 (Tilly Cognition) < 3.5 → `HALT_LD04` automatic. Cascade LD03→LD04 vérifiée à chaque Sunday Uplink.

**Pourquoi** : sans seuils chiffrés, Beth ne peut pas répondre en <5 minutes. Avec des seuils, Beth peut rejeter mécaniquement et escalader seulement les cas ambigus. Le test des 5 minutes d'A0 Reasoning Map vaut aussi ici : *"si le scoring prend plus de 5 minutes, c'est que l'idée n'est pas assez clarifiée — retourne en Phase CLARIFY"*.

### 2.2 Context Pack obligatoire (9 champs)

```yaml
required_context_pack_fields:
  - ship
  - crew_member
  - next_action
  - framework
  - domain_impact
  - l0_skill_required
  - beth_clearance
  - evidence_paths
  - output_artifact
```

**Pourquoi** : un champ manquant = `BLOCKED_CONTEXT_PACK_INCOMPLETE`. Cette règle transforme un pipeline de bonne volonté en **protocole vérifiable**. La friction du gate est volontaire : elle force l'agent à expliciter ce qu'il fait avant de le faire.

### 2.3 A3 ne compile JAMAIS de décision finale

Verbatim canon :

> *"The A3 domain officers never compile final Discovery reports. They provide LD01-LD08 findings; Discovery/ZORA synthesizes the Life Wheel state and sends the result to Beth or Morty."*
> — `A2_Discovery_ZORA_Spec.md` ligne 66

**Pourquoi** : si un A3 publie directement un verdict, le pipeline A2/A1 est bypasse. Le rôle de chaque niveau est strictement séparé : A3 = findings narrow ; A2 = compile ; A1 = décide ou route. Casser cette séparation = perdre la traçabilité.

### 2.4 Éliminer avant automatiser (DEAL rule)

`A3_Zero_Automation_Spec.md` exige qu'un automation candidate ait un **before/after workflow** ET que `A3_RokTahk_Elimination_Spec.md` ait éliminé ce qui pouvait l'être avant Zero n'intervienne.

**Pourquoi** : automatiser du gaspillage crée un gaspillage automatique. Rok-Tahk est le **premier rempart** contre l'automation du vide. Le Karpathy loop `D→E→A→L` est explicitement séquentiel ; sauter une étape = corruption.

## 3. Cadences

### 3.1 Cycle 12 Week Year Q3 2026 (06/15 → 09/07) + 13e semaine

Quatre semaines d'exécution + une 13e semaine intercalée :

- **W1** (06/15-07/05) — Items 1-2 : SOB Abdaty + 13e semaine → Una + Pike → `snw_planning`.
- **W2** (07/06-07/26) — Items 3-4 : Auto-research IA + TOKEN frugalité → M'Benga → `snw_focus`.
- **W3** (07/27-08/16) — Items 5-6 : YouTube PARA + Hermes → Chapel → `snw_metrics`.
- **W4** (08/17-09/07) — Items 7-12 : Agent OS + Business OS + 36 A3 + Solaris/OMK/ABC + VPS DEAL → Ortegas + Chapel → `snw_execution`.
- **W13** (09/14) — première semaine hors Q3 ; pivot canon ; Life Wheel sync.
- **W0 Cycle 4** (09/21) — semaine tampon du 4e Cycle.

**Pourquoi** : la cadence 12 semaines force à choisir ; la 13e semaine est un **buffer de transition** qui empêche le système de basculer brutalement entre cycles. La conformité SDD-010 §6.1 (veto 90j jusqu'au 2026-08-11) tombe avant W13 — c'est la **première semaine autorisée** pour un nouveau SDD.

### 3.2 Discipline 50/30/20 (SNW load rule)

50 % exécution Rocks / 30 % planification / 20 % buffer-recovery.

**Pourquoi** : sans cette règle, un cycle 12WY devient une to-do list. La discipline 50/30/20 protège contre la surcharge cognitive (LD04) en gardant 20 % du temps pour HALT slots Beth et recovery.

### 3.3 Items 1-2 = terrain A0 (hors session CC)

> *"Items 1-2 = terrain A0 (hors session CC). Items 3-12 = orchestration A1/A2/A3 = scope Morty/Cerritos/Curie/Enterprise/Picard/Spock."*
> — `gatekeepers-readme`

**Pourquoi** : distinguer ce qui relève du board observer A0 (décisions physiques, soirées, rituels) de ce qui relève de l'orchestration scriptable CC. Confondre les deux crée des items fantômes (CC essaie de scripter une rencontre physique) ou des items orphelins (A0 ne traite jamais les items scriptables).

## 4. Règles chiffrées connues

| Règle | Valeur | Source | Sens |
|---|---|---|---|
| LD03 minimum | 4.0 | SDD-005 / `A1_Beth_Spec.md` | Seuil Health ; en-dessous → HALT_LD03 automatic |
| LD04 minimum | 3.5 | SDD-005 / `A1_Beth_Spec.md` | Seuil Cognition ; en-dessous → HALT_LD04 automatic |
| multi_domain_alert | 3 | SDD-005 | ≥3 LD en alerte → escalade A0 |
| max_concurrent_tickets (Morty) | 3 | `A1_Morty_Spec.md` | Pas plus de 3 Context Packs simultanés |
| Load rule SNW | 50/30/20 | `A2_Curie_SNW_Spec.md` | Répartition temps cycle |
| state.json rotation | > 10 KB | `A2_Curie_SNW_Spec.md` | `state.json.prev` |
| Lock backoff retry | 3× (100/300/900ms) | `A2_Curie_SNW_Spec.md` | state_writer.py retry |
| GTD A3 dual conflict | Tendi ≠ Organize, Rutherford ≠ Reflect | `25_GTD_Cerritos/README.md` | D3 nuance critique : canon local actif |
| SDD-010 veto 90j | jusqu'au 2026-08-11 | `W1_Quarter_Intent_Q3_2026.md` | Pas de nouveau SDD avant cette date |
| 13e semaine | 09/14/2026 | Item 2 verbatim A0 | Première semaine hors Q3 |
| W0 Cycle 4 | 09/21/2026 | Item 2 verbatim A0 | Semaine tampon |

## 5. Pièges documentés

### 5.1 Saru 1000T paperclip — 3 garde-fous canon

Voir `concept anti-paperclip-saru.md`. Résumé :

1. **Boundary Book LD01** — Saru ne peut pas overrider la stratégie business.
2. **AREA_STANDARD P1 Work ON not IN** — Scarcity seule ne suffit pas.
3. **Musk pivot = agency over utopia** — Saru évalue si l'intention augmente l'agency ou attend salvation externe.

### 5.2 Règle chiffrée DEAL 3/5 — attendue et non-trouvée

Le brief de cette escouade attendait une règle du type *"3 occurrences pour automatiser, 5 occurrences pour rembourser"*. Cette règle **n'apparaît dans aucun fichier** de `26_DEAL_Protostar/`. Seule mention du comptage : `dal.twin.md` cite *"Pattern detection and recurrence counting"* — Dal compte, mais aucun seuil chiffré 3/5 n'est posé.

À noter pour les futures passes : la règle pourrait exister ailleurs (Gemini_Archive, Memory_Core) ou n'avoir jamais été formalisée.

### 5.3 Lecture Beth/Morty en parallèle des deux ships "responsabilité principale"

Le plan `fancy-hugging-bengio.md §3.5` simplifie "Beth = Ikigai+Life Wheel+DEAL / Morty = 12WY+PARA+GTD". Lecture rapide = exclusivité. Lecture correcte = **responsabilité principale**, pas exclusivité. Le terrain canonique (D4 close 2026-06-21) garde :

- Beth = veto **distribué** sur les 6 ships.
- Morty = routage **distribué** sur les 6 ships.

**Piège** : un agent qui ouvre une intention Life Wheel depuis le dossier GTD (Cerritos) doit quand même passer par Beth si la décision touche LD03/LD04. Lire Beth/Morty **en premier** prévient ce piège.

### 5.4 GTD mapping conflict (Rutherford = Organize)

`fancy-hugging-bengio.md §15.1` mappe initialement **Tendi = Organize / Rutherford = Reflect**. Le canon actif local (résolu 2026-05-20 par A0 sur SDD-008) garde **Rutherford = Organize + Tendi = Review**. Ne PAS escalader A0 pour réécrire §3.2 du plan — terrain canon + twin canon sont cohérents et D4 append-only.

### 5.5 Horizons canon (Saru = H3, Book = H1)

Lecture rapide pourrait inverser (Book = H10, Saru = H1). Le canon verrouille **Saru = H3** (quarterly runway) et **Book = H1** (weekly P&L). Cohérent avec §15.1.3 du plan. **D3 nuance critique**.

### 5.6 "Life Wheel drift" = Tilly + Spock, PAS Saru+Stamets

`fancy-hugging-bengio.md §15.1.4` initialement mappait "Life Wheel drift → A3 Saru + Stamets". Corrigé par `A2_Discovery_ZORA_Spec.md` ligne 80 : drift = **Tilly (LD04) + Spock (Areas)**. Saru+Stamets restent narrow findings seulement.

## 6. Ce que cette méthode n'est PAS

- **Pas un plan markdown plat** — survit aux compactions par l'index `00_index.md` racine de chaque module canonique (méthode CARDIA-TDD).
- **Pas une UI visuelle n8n** — `state.json` est la machine à états partagée.
- **Pas un tool-lock sur un seul harness** — la structure filesystem est lisible par TOUT harness (CC/HA/MC/Shadow L1).

## 7. Raison d'être de la méthode

Le système A'Space existe pour une raison :

> *"Life OS is the fleet that helps A0 live, decide, recover, execute, and review without collapsing into tool maintenance."*
> — `20_Life_OS/Manifesto.md`

La méthode Life OS n'a de sens que si elle sert cet objectif. Toute pratique qui éloigne de cet objectif — tool hoarding, fractal creep, role collapse, conception drift — est un signal d'alerte qui doit déclencher un retour en Phase CLARIFY A0 (3 questions max).

> *"Si le scoring de cette idée prend plus de 5 minutes, c'est que l'idée n'est pas assez clarifiée. Retourne en Phase CLARIFY."*
> — `a0_reasoning_map.md` §4.2