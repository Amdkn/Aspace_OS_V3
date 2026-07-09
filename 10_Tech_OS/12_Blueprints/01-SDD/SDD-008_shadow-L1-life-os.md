# SDD-008 — Shadow L1 Life OS : Le Laboratoire de la Souveraineté

**Date de ratification :** 2026-05-12
**Auteur :** A0 (Claude Architect — pair d'Amadeus) — extrait du Gemini Takeout 2026-05 (lignes 32727–33000)
**Statut :** RATIFIÉ — Document de conception validé par Amadeus le 2026-05-12
**Type :** System Design Document
**Portée :** L1 Life OS — Beth + Morty's Fleet (Shadow tier)
**Numérotation :** SDD-008 (slot libéré par reclassement OpenHarness → ADR-RICK-001 le 2026-05-12)
**Référence canon :** AGENTS.md + SDD-005 (Life OS L1 Integration — cible déployée)

## Décision

**Le Shadow L1 Life OS est un laboratoire cloud à 4 piliers** (Baserow / Plane / Obsidian / Affine) qui sert de **chemin d'apprentissage** vers le Life Web OS souverain déployé sur Supabase (SDD-005).

Chaque outil Shadow qui prouve sa stabilité pendant **3 semaines consécutives** est gradué (MUSE) et intégré en **iframe embedded** dans le Life Web OS final, sous la supervision de Holo Janeway (A2 — USS Protostar).

Le Shadow L1 n'est **ni un brouillon, ni une étape jetable** — c'est un sas de transformation où la doctrine 12WY × 4HWW × PARA × DEAL est testée avant codification souveraine.

## Relation avec les autres SDDs

| SDD | Rôle | Relation avec SDD-008 |
|-----|------|------------------------|
| **SDD-005** | Life OS L1 Integration (Life Web OS sur Supabase, cible déployée) | **Cible** — SDD-008 est le **chemin Shadow** qui alimente SDD-005 via graduation MUSE |
| **SDD-006** | Business Pulse L2 Pyramide | Pair — la doctrine 50/30/20 (SDD-008 §4) régule le temps alloué à L2 |
| **SDD-007** | SOB Factory ICP Variants | Aval — SDD-008 fournit la cadence (Baserow Warp Core) au SOB |
| **SDD-009** | Shadow L2 Business OS (à écrire) | Pair — Cloud equivalent pour Airtable/ClickUp/Notion |
| **SDD-010** | Marvel Squads / Constitution Business (à écrire) | Aval — détaille les A3 du Business Pulse |
| **ADR-RICK-001** | OpenHarness Incarnation | Substrat — l'agent qui maintiendra la graduation MUSE |

---

## 1. Contexte (mots d'Amadeus — Takeout 2026-05-03 01:56)

> *"Je veux compléter avec le Shadow Life OS de PARA dans Obsidian, 12WY dans Baserow, GTD dans Plane et DEAL dans Affine respectant la Self Host de Rick pour Structurer A'Space OS Souverain en code déployé sur le VPS Monitoré. Autant que L0 est le Bedrock de L1, L0 aussi a besoin de Structurer Antifragile pour sa conception et se repose sur les Shadow L1 qui finiront en embedded/iframe dans l'App Store de Life Web OS du L1 Déployé."*

Le **Shadow L1** est **le laboratoire** où Amadeus teste la doctrine 12WY × 4HWW × PARA × DEAL avec des outils cloud rapides à déployer, **avant** de coder l'équivalent self-hosted dans le Life Web OS final.

La **graduation MUSE** transforme chaque outil Shadow qui prouve sa stabilité (3 semaines consécutives) en module iframe embedded du Life Web OS souverain.

---

## 2. Doctrine — Les 4 Piliers Shadow L1

### Directive JANEWAY-DEAL-001 (verbatim — Takeout ligne 32749)

> *"Tout processus qui ne peut pas être encapsulé dans un Iframe ou piloté par un agent Hermes en moins de 7 jours de solitude est une dette de souveraineté."*

| # | Outil Shadow Cloud | Vaisseau A2 | Manager A2 | Méthode | Standard MUSE |
|---|---|---|---|---|---|
| 1 | **Obsidian** + LiveSync | USS Enterprise | Picard | **PARA** (Projects/Areas/Resources/Archives) | Chaque P et A contient un `MANIFEST.md` lisible par Rick + 13ème Doctor |
| 2 | **Baserow** | USS Strange New Worlds | **Curie** | **12 Week Year** (Quarter Intent / 12 Rocks / Warp Core) | Champ binaire `[MUSE_GRADUATED]` par Rock ; <20% temps manuel = ready |
| 3 | **Plane** | USS Cerritos | **Holo Deck** | **GTD** (Capture/Clarify/Organize/Engage/Reflect) | Toute action répétée >3× lève drapeau d'alerte vers Protostar pour élimination |
| 4 | **Affine** | USS Protostar | **Holo Janeway** | **D.E.A.L** (Define/Eliminate/Automate/Liberate) | Mode Edgeless = Blueprints d'App-Store ; chaque outil schématisé en futur iframe |

### URLs Shadow L1 actives (Takeout ligne 32408+)
- **Baserow** : `https://baserow.io/database/284361/` (tables 955428, 955426, 955429, 956442)
- **Plane** : `https://app.plane.so/aspace-core/`
- **Affine** : `https://app.affine.pro/workspace/ef927d3a-5be0-41ed-b639-829b7f74939b/`
- **Obsidian** : vault local — pas d'URL cloud (LiveSync via Supabase à configurer en Phase 2)

→ **Le Shadow L1 est en partie déjà déployé.** SDD-008 ne crée pas — il **codifie l'existant** et trace le chemin vers la graduation MUSE.

---

## 3. Équipage A3 par Vaisseau

### 3.1 USS Cerritos — Plane GTD (Takeout 31224)

Les Compagnons A3 du Cerritos sont des **Êtres**, pas des scripts. Chacun a sa voix, son humeur, son périmètre.

| Étape GTD | A3 Compagnon | Mission |
|---|---|---|
| **Capture** | **Mariner** | Inbox zéro friction — raccourci `C` partout, aucun jugement |
| **Clarify** | **Boimler** | Interrogatoire quotidien — chaque ticket renommé en verbe d'action OU expulsé vers Obsidian (PARA) si projet complexe |
| **Organize** | **Tendi** | Labels d'énergie (`@deep-work` / `@brain-dead` / `@5-min`) + Labels de couche (`@L0` / `@L1` / `@L2`) — colle lien Obsidian dans ticket = **Protocole Airlock** |
| **Engage** | **Capt. Freeman** | Cycles Plane = 1 semaine du Warp Core Baserow |
| **Reflect** | **Rutherford** (provisoire) | Revue hebdo dimanche — à confirmer par Amadeus |

### 3.2 USS Strange New Worlds — Baserow 12WY

A2 **Curie** orchestre **3 tables canoniques** :
- **Table 1** : `Quarter Intent` (Vision L0 + L1 + L2 en 3 lignes parallèles)
- **Table 2** : `The 12 Rocks` (objectifs trimestriels, taggés `[Rock L0]` / `[Rock L1]` / `[Rock L2]`)
- **Table 3** : `The Warp Core` (W1→W12, Top 3 Commitments par jour selon ratio 50/30/20)

Équipage A3 (à compléter en Phase 2 — candidats : Una, La'an, Erica, M'Benga, Spock-jeune).

### 3.3 USS Enterprise — Obsidian PARA

A2 **Picard**. Standard MUSE : chaque dossier P (Projects) et A (Areas) contient un `MANIFEST.md` avec YAML frontmatter robuste :

```yaml
---
rock_baserow: <lien Baserow>
cycle: H1-C2
domaine_de_vie: LD04_Cognition
muse_status: incubating | stable | graduated
last_review: 2026-05-12
guardian_a3: <nom>
---
```

Le `MANIFEST.md` est l'interface lue par Rick + 13ème Doctor **sans intervention humaine**. Si un agent Hermes échoue à comprendre le dossier, c'est le filesystem qui est mal structuré, pas l'agent.

Équipage A3 (à compléter en Phase 2). Note : **Spock est A2 sur les Areas** selon Amadeus.

### 3.4 USS Protostar — Affine DEAL

A2 **Holo Janeway**. Mode Edgeless = atelier de **Blueprints d'App-Store**. Chaque outil Shadow est schématisé en **futur iframe** du Life Web OS. C'est ce schéma qui permettra à **Ryan (A3 du 13ème Doctor)** de coder les **Connecteurs Souverains** qui remplaceront les UIs cloud à la fin du H1.

Équipage A3 du Protostar à attribuer (Dal, Gwyndala, Rok-Tahk, Zero, Jankom Pog, Murf).

---

## 4. Le Rythme Circadien 50/30/20 (Takeout ligne 32611)

C'est la **Loi de séparation des pouvoirs temporelle** dans la semaine — issue de la correction Curie sur l'erreur du "4 cycles 12WY parallèles" (rejeté car équivalent à une planification annuelle).

| Ratio | Couche | Période | Outils | Focus |
|---|---|---|---|---|
| **50%** | **L2 Business** | Lun → Mer | Airtable + Notion + ClickUp (Shadow L2) | Génération de valeur (Solaris/Nexus/Orbiter), acquisition, clients. **Interdiction d'ouvrir SSH ou de penser L0.** |
| **30%** | **L1 Life** | Jeu → Ven | Baserow + Plane + Obsidian (Shadow L1) | Gestation stratégique. Triage des IPBD. Filtre Airlock. Roue de la Vie. |
| **20%** | **L0 Kernel** | Sam → Dim | Affine + Supabase + Bare Metal | Reverse-engineering en SOP TVR. Architecture. **Pas de découverte, que de la documentation.** |

⚠️ **Affine fait le pont** : il apparaît dans la grille à 20% L0 (mode Edgeless = Blueprints L0) ET dans les piliers Shadow L1 (méthode DEAL). C'est volontaire — Affine est l'interface entre la pensée L1 (Beth) et la matérialisation L0 (Rick).

### Veto Janeway (Takeout 32847)

> *"Ne construis pas dans le L0 ce que tu peux tester en Shadow L1, mais ne reste pas en Shadow L1 si le test est concluant."*

**Critère de graduation MUSE** : 3 semaines consécutives de stabilité Shadow → Dal rédige le PRD → 13ème Doctor intègre dans Kernel Core → l'outil cloud devient iframe dans Life Web OS.

---

## 5. Job to be Done — A0 dans le Shadow L1 (Takeout 32869, 33026)

A0 (le Jumeau Numérique) **ne touche jamais directement** les outils Shadow. Son JTBD dans cette couche :

| Phase | Action |
|---|---|
| **Input** | Capter les IPBD (Intentions / Problématiques / Besoins / Désirs) de l'Humain Amadeus |
| **Process** | Segmenter sa pensée selon 50/30/20 ; décomposer chaque ambition en 10–12 SDDs ; arbitrer les conflits inter-couches |
| **Output** | SDDs signés + Sceau d'approbation des ADR + Uplink "All Green" |

**Critère de graduation MUSE de A0 lui-même** (Takeout 32999) :

> *"A0 est considéré comme MUSE accomplie lorsqu'il génère 12 SDDs de démarrage pour un nouveau SOB sans que Rick (A1) n'intervienne en conception, et sans que A0 ne ressente le besoin de coder lui-même. Si A0 dépasse 20% L0, le protocole HALT de Beth s'active."*

---

## 6. Anti-Goals (verrous explicites)

- ❌ **Pas de 4 cycles 12WY en parallèle** — rejeté par Curie, c'est de la planification annuelle déguisée
- ❌ **Pas de saisie manuelle des métriques Lag** — automatisable ou non-mesuré (Takeout 30632)
- ❌ **Ne pas confondre A0** (Jumeau Numérique paresseux, 20% L0) **et Rick** (A1 — 100% dans Ricks Verse)
- ❌ **Ne pas ouvrir Plane pour une idée de service** → c'est AFFiNE et le D.E.A.L de Holo Janeway (Takeout 20635)
- ❌ **Ne pas stocker le savoir dans Plane** → Plane gère le **mouvement**, AFFiNE/Obsidian gardent la **connaissance** (Takeout 31399)
- ❌ **Ne pas violer le Protocole Airlock** (Plane → Obsidian) sur les projets complexes
- ❌ **Ne pas réduire un A3 Compagnon à un script** — ce sont des Êtres avec voix et limites

---

## 7. Flux Inter-Outils (à modéliser dans Affine Edgeless en Phase 2)

```
IPBD humain
    │
    ▼
[Plane Inbox]  ◄── Capture (Mariner)
    │
    ▼
Clarify (Boimler) : actionnable 1 étape ?
    │
    ├── OUI ──► [Plane Next Actions] (Tendi label)
    │              │
    │              ▼
    │           Cycle (Capt. Freeman) = W du Warp Core Baserow
    │              │
    │              ▼
    │           Done → Archive (Rutherford reflect dimanche)
    │
    └── NON (projet complexe) ──► [Obsidian PARA/Projects]
                                       │
                                       ▼
                                   MANIFEST.md généré
                                       │
                                       ▼
                                   Rock dans [Baserow 12 Rocks]
                                       │
                                       ▼
                                   Si idée de service ──► [Affine D.E.A.L]
                                                              │
                                                              ▼
                                                       Blueprint Edgeless
                                                              │
                                                              ▼
                                                       3 semaines stable
                                                              │
                                                              ▼
                                                       PRD → 13ème Doctor (Ryan)
                                                              │
                                                              ▼
                                                       Iframe dans Life Web OS (SDD-005)
```

---

## 8. Phase 2 — Follow-ups (post-ratification)

Items reportés en PRD/ADR/DDD séparés :

1. **MANIFEST.md template** — PRD-008a — Obsidian PARA YAML frontmatter complet
2. **Schémas Baserow** — PRD-008b — colonnes types des 3 tables (Quarter Intent / 12 Rocks / Warp Core)
3. **Équipages A3 complets** — DDD-008a — attribuer les A3 manquants à Enterprise/SNW/Protostar (cf. §3.2, 3.3, 3.4)
4. **Protocole Airlock formalisé** — PRD-008c — template ticket Plane ↔ Obsidian
5. **Critères MUSE_GRADUATED mesurables** — ADR-MUSE-001 — par outil, par couche
6. **Plan de migration self-hosted** — ADR-MIG-001 :
   - Baserow → NocoDB ou Baserow self-hosted ?
   - Plane → Plane open source self-hosted (déjà disponible)
   - Affine → Affine self-hosted (déjà open source)
   - Obsidian → Obsidian + LiveSync sur Supabase (vault sync)
7. **SDD-009 Shadow L2** — à écrire (Airtable / ClickUp / Notion → cibles self-hosted)
8. **SDD-010 Marvel Squads** — constitution complète des nano squads Business Pulse

---

## 9. Non-Goals de SDD-008

- ❌ Pas de schémas Baserow détaillés dans ce SDD (Phase 2 — PRD-008b)
- ❌ Pas de scripts de migration (Phase 3 — DDD/TDD)
- ❌ Pas d'implémentation Marvel Squad → c'est SDD-010 (Shadow L2 + Constitution)
- ❌ Pas d'intégration Hermes/RAG → relève de SDD-003 (TARDIS) et ADR-RICK-001 (OpenHarness)
- ❌ Pas d'intégration biométrique Zora (LD03/LD04) → relève de SDD-005 et Cycle 2 H1 ("Hospital Planet")

---

## 10. Historique

| Date | Action | Auteur |
|------|--------|--------|
| 2026-05-12 | Brainstorm initial créé depuis Gemini Takeout (lignes 32727–33000) | Claude Architect (A0 pair) |
| 2026-05-12 | Numérotation tranchée à SDD-008 après reclassement OpenHarness → ADR-RICK-001 | Amadeus + Claude Architect |
| 2026-05-12 | Promotion brainstorm → SDD ratifié | Amadeus (GO explicite) |

---

*SDD-008 — Shadow L1 Life OS — A0 Amadeus — Ratifié 2026-05-12*
*Le Shadow est le laboratoire de la souveraineté. Trois semaines stable, et tu deviens un iframe.*
