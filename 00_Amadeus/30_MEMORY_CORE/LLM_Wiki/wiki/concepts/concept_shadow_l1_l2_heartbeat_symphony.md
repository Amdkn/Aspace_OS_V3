---
source: LLM_Wiki_A0
date: 2026-05-29
type: concept
domain: Shadow_Stack / L1_Life_OS / L2_Business_OS / Symphony / Heartbeat
tags: [#concept #Symphony #Shadow_L1 #Shadow_L2 #matryoshka #PARA #12WY #GTD #DEAL #Airtable #ClickUp #Notion #Baserow #Plane #Obsidian #Affine #ADR_MESH_L2_001]
---

# Concept: Shadow L1 / L2 Heartbeat — la colonne vertébrale 4-méthodes de Symphony

> **Thèse centrale** : Shadow L2 (Business) n'est pas un système distinct de Shadow L1 (Life).
> C'est **la même colonne vertébrale à 4 méthodes**, projetée sur des outils cloud/payants au
> lieu d'outils souverains. La matriochka n'a qu'une seule grammaire ; elle change d'instrument
> selon l'étage.

⚠️ **Statut** : Symphony = Shadow A0, **hors-canon SDD, hors-Airlock, sous veto 90j**. V0 =
sable mouvant, PAS en prod. Ce concept documente une **homologie observée**, il ne ratifie rien.

---

## 1. L'homologie 4-méthodes (le cœur)

Chaque méthode L1 a un **jumeau L2**, et le rôle [[concept_adr|ADR-MESH-L2-001]] colle exactement :

| Méthode | L1 (souverain) | A2 / Vaisseau | L2 (cloud) | Squad A2 | Rôle MESH |
|---|---|---|---|---|---|
| **PARA** (structure / doctrine) | Obsidian | Enterprise (Picard) | **Notion** | People/Legal (X-Men/Eternals) | **WHAT** — source de vérité |
| **12WY** (objectifs chiffrés) | Baserow | SNW (Curie) | **Airtable** | Growth/Sales/Finance | **HOW MUCH** — quantitatif |
| **GTD** (flux opérationnel) | Plane.so | Cerritos | **ClickUp** | Ops/Product/IT | **WHEN/WHO** — exécution |
| **DEAL** (automatiser / libérer) | Affine | Protostar (Janeway) | *(pas de 4e tracker)* | — | **méta-couche de libération** |

### Pourquoi ce n'est pas une coïncidence

Les specs des adapters Symphony l'écrivent noir sur blanc :
- **Obsidian §10** : *« graduation Notion → Obsidian = migration one-way »* → Notion **est** le
  jumeau cloud d'Obsidian. Tous deux PARA, document-first, WHAT.
- **Baserow** = un Airtable sans frais : Single-Select states, tables structurées, colonnes
  `SLA Max Time/Cost`. Même grammaire que l'Airtable 🦸 (HOW MUCH).
- **Plane ↔ ClickUp** = deux trackers d'issues à state-machine (to do → in progress → review →
  done). Plane est le ClickUp souverain.

---

## 2. Pourquoi L2 a 3 trackers et L1 en a 4

Parce que **DEAL n'est pas un tracker — c'est la méta-couche de libération**, partagée par les
deux étages. Affine (mode Edgeless) produit des **Blueprints** que Ryan (L0 / 13e Docteur) code
en connecteurs souverains.

> Conséquence directe : **les `WORKFLOW.*.draft.md` de Symphony SONT des artefacts DEAL.**
> Ce sont les sorties « Automate » d'un loop métier, prêtes pour « Liberate »
> (graduation MUSE → connecteur souverain sur VPS).

Le 4e tracker du L2 n'est donc pas un outil SaaS de plus : **c'est Symphony lui-même**.
DEAL/Affine schématise → WORKFLOW.md matérialise → Rick souverainise. La pyramide se referme.

---

## 3. Le pont vertical L1↔L2 (déjà spécifié à 80%)

Les specs L1 contiennent déjà les crochets vers L2 :

1. **Baserow `Layer Tag` = `Rock L2`** (table « The 12 Rocks », table_id 955426). Un objectif
   Business est un Rock taggé L2, avec `Linked Plane Tickets` + colonnes SLA. → Un loop métier
   (ex. Growth) = un Rock L2.
2. **Warp Core ratio 50/30/20** (table 955429) : *« Top 3 Mon-Tue-Wed = 3 Commitments L2 (50%) »*.
   → Le Business reçoit **la majorité** de l'engagement hebdomadaire. C'est la pointe cashflow
   de la matriochka.
3. **Obsidian Areas = `8 Domaines Roue de Vie + 8 Domaines Business`** (prompt §3). → Les 8 SOA
   (dont 05_Growth) vivent comme **PARA Areas dans le vault**. C'est *littéralement* là
   qu'atterrissent les artefacts JTBD du skill `picard-growth-jtbd-launch` — et le skill
   s'appelle **picard** (= Enterprise = PARA). Le nom n'était pas innocent.
4. **MANIFEST `rock_baserow:`** relie chaque projet PARA à son Rock 12WY.
5. **Lexique interdit vertical partagé** : `innover / disrupter / synergie` est le
   `forbidden_lexicon_global` partout en L1 — et c'est le **même trio** que le fallback du
   WORKFLOW Growth L2. Une seule doctrine de langue, deux étages.

---

## 4. Growth, déroulé sur les 4 méthodes (cas concret)

| Méthode | Instance Growth |
|---|---|
| **PARA** | Doctrine Growth (JTBD-001..004) = Area Obsidian, jumelée à Notion (provenance du `context_pack` RAG via X-Men/People). |
| **12WY** | « Compléter le loop Growth » = un **Rock L2** dans Baserow ; ses chiffres réels (leads, CPQL) = l'Airtable 🦸 (HOW MUCH). |
| **GTD** | Les handoffs D5 (lead enrichi 🦸 → tâche) = le flux **ClickUp** (S2-1, S2-4), jumeau du Plane inbox→today. |
| **DEAL** | Le loop stabilisé → Blueprint Affine → `WORKFLOW.growth-airtable.draft.md` → connecteur souverain (graduation). |

---

## 5. Le gap honnête

Le pont **L1→L1 est spécifié** : Cycle Plane = Semaine Warp Core Baserow ; projet complexe Plane
→ note PARA Obsidian (règle Boimler). Mais **aucun WORKFLOW ne lit un Rock L2 Baserow pour
dispatcher dans le slot Airtable Growth** — le lien vertical L1↔L2 reste conceptuel
(tag `Rock L2`, Areas Business, `rock_baserow`).

C'est le **seul vrai trou** : la matriochka est dessinée, pas encore branchée bout-à-bout.
Le draft `symphony/BRIDGE.rock-l2-to-growth.draft.md` esquisse ce crochet (clés de jointure
`rock_baserow` ↔ `context_pack` ↔ record Airtable) sans rien activer.

---

## 6. Frontières (non négociables, héritées du base spec)

- **Symphony lit, l'agent écrit.** Pas de bi-sync, pas d'auto-création de records, à aucun étage.
- **L2 = `read_only` par défaut** ; write uniquement sur Build Gate + sign-off A0.
- **Un datum = un propriétaire.** Si dupliqué = pointeur (URL/ID), jamais copie (règle d'or MESH).
- **Pas d'ADR pour Symphony** tant que veto 90j actif. Ce concept est mémoire, pas loi.

---

*Last updated: 2026-05-29*
*Sources : `symphony/L1/symphony-{baserow,plane,obsidian,affine}.spec.md` · `symphony/L2/symphony-{airtable,clickup,notion}.spec.md` · skill `picard-growth-jtbd-launch`*

---

## Inbounds

- [[concept_life_os]] — les 6 vaisseaux L1 et leurs 4 frameworks d'exécution
- [[concept_adr]] — ADR-MESH-L2-001 (WHAT/WHEN/HOW MUCH, un propriétaire par datum)
- [[concept_sovereignty]] — graduation MUSE = libération vers le connecteur souverain (DEAL Lock)
