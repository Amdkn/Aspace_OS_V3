# ============================================================================
# Symphony BRIDGE — DRAFT — Pont vertical L1 (Baserow Rock L2) ↔ L2 (Airtable Growth)
# ----------------------------------------------------------------------------
# Statut    : Shadow A0 — DRAFT — hors-canon SDD, hors-Airlock
# Date      : 2026-05-29
# Hérite    : ./symphony-base.spec.md  +  ./L1/symphony-baserow.spec.md  +  ./L2/symphony-airtable.spec.md
# Concept   : LLM_Wiki/wiki/concepts/concept_shadow_l1_l2_heartbeat_symphony.md (§5 le gap)
# ----------------------------------------------------------------------------
# ⚠ NE PAS ACTIVER avant levée du veto 90j. Ce fichier ESQUISSE le crochet manquant
#   entre l'étage 12WY (L1, Baserow) et l'étage HOW-MUCH (L2, Airtable Growth).
#   Il ne crée AUCUNE écriture, AUCUN bi-sync. C'est une carte de jointure, pas un activable.
# ⚠ Frontière inchangée : Symphony lit, l'agent écrit. Pas d'auto-création de records.
# ============================================================================

## 1. Le problème que ce pont résout

La matriochka L1↔L2 est dessinée mais pas branchée :

- Côté **L1 Baserow** : un objectif Business vit comme un **Rock taggé `Rock L2`**
  (table « The 12 Rocks », table_id 955426), avec colonnes `Linked Plane Tickets`,
  `SLA Max Time`, `SLA Max Cost`.
- Côté **L2 Airtable** : le travail réel du loop Growth vit dans 🦸 Leads & Audits
  (`appmWf5Xm7w9Ae0ky` / `tblj0xmSXLH4Xsd8c`), opéré par le `WORKFLOW.growth-airtable.draft.md`.

Aujourd'hui **rien ne relie les deux**. On voit le Rock « Compléter le loop Growth » dans le
12WY ; on voit les leads dans Airtable ; mais aucune clé de jointure ne dit *« ce Rock-ci EST
ce loop-là »*. Ce pont définit cette clé — **par pointeurs, pas par copie** (règle d'or MESH).

## 2. Les 3 clés de jointure (pointeurs, jamais copies)

```yaml
join_keys:
  # 1. Le Rock L2 pointe vers le RAG doctrine partagé (même urn que le skill + l'Airtable adapter)
  context_pack: "urn:aspace:rag:<project-slug>-growth"
    owner: "skill picard-growth-jtbd-launch (PARA doctrine) → résolu en runtime via 🏮 Supabase URL"
    present_in:
      - "Baserow Rock L2 : nouvelle colonne TEXT 'Context Pack' (pointeur, optionnelle)"
      - "Airtable WORKFLOW soc.resolve_via_lookup.context_pack_url (déjà câblé)"
      - "JTBD-00x frontmatter context_pack (déjà câblé dans le skill)"

  # 2. Le projet PARA pointe vers son Rock 12WY (déjà prévu côté Obsidian)
  rock_baserow: "<baserow_row_id du Rock L2>"
    owner: "Obsidian MANIFEST.md frontmatter (PARA project → 12WY rock)"
    present_in:
      - "Obsidian MANIFEST : rock_baserow: 955426/<row_id>"
      - "Baserow Rock : id natif de la row"

  # 3. La métrique mesurée pointe vers le record Airtable (HOW MUCH = un seul propriétaire)
  airtable_record: "<recXXXX ou URL>"
    owner: "Airtable 🦸 Leads & Audits OU 💸 Sales Pipeline"
    present_in:
      - "Baserow Rock L2 : colonne 'Linked Airtable' (pointeur résultat, optionnelle)"
      - "proof-log JTBD : airtable_record: rec... (une fois mesuré, pas avant)"
```

## 3. Sens de lecture (unidirectionnel, read-only)

Symphony ne « synchronise » pas — il **lit dans un sens** pour donner du contexte, jamais
pour écrire en retour automatiquement.

```
  L1 Baserow Rock L2 "Growth loop"
        │  (lecture seule : Symphony lit le Rock pour connaître l'intention trimestrielle + SLA)
        ▼
  context_pack (urn) ──── clé de jointure ────► WORKFLOW.growth-airtable (L2)
        │                                              │
        │                                              ▼
        │                                    Agent Gardien opère un lead 🦸
        │                                    (écrit le record Airtable courant)
        ▼                                              │
  rock_baserow (pointeur PARA→12WY)                    ▼
        ◄──────── airtable_record (pointeur métrique) ─┘
        (le chiffre mesuré APPARTIENT à Airtable ; le Rock le RÉFÉRENCE, ne le copie pas)
```

- **Baserow → Airtable** : lecture du Rock = contexte (intention 12WY, SLA defaults). Pas d'écriture.
- **Airtable → Baserow** : le record mesuré reste propriété d'Airtable ; le Rock porte un
  **pointeur** `Linked Airtable`, mis à jour par l'agent (write Airtable-side) ou par A0, jamais
  par un bi-sync Symphony.

## 4. Ce que ce pont N'EST PAS (frontières)

- ❌ Pas de bi-sync Baserow ↔ Airtable (interdit base spec §10.3).
- ❌ Pas d'auto-création de Rock depuis un lead, ni de lead depuis un Rock.
- ❌ Pas de duplication de métrique : le chiffre vit dans UN seul tracker (Airtable = HOW MUCH).
- ❌ Pas de nouvelle colonne Airtable (décision A0 option 1 : zéro écriture schéma 🦸).
  Les 3 colonnes optionnelles évoquées sont **côté Baserow uniquement** (Rock L2), et restent
  différées tant que le veto 90j tient.

## 5. Activation (différée, A0-gated)

Pré-requis avant toute activation :
1. Levée du veto 90j Symphony.
2. Sign-off A0 sur l'ajout (optionnel) des colonnes pointeur `Context Pack` / `Linked Airtable`
   sur la table Baserow 12 Rocks — write L1, donc `requires_signoff`.
3. WORKFLOW Airtable Growth déjà activé (lui-même post-veto).

Tant que ces 3 conditions ne sont pas réunies, ce fichier reste une **carte**, pas un connecteur.

---

*Bridge draft — Shadow A0 — pont vertical 12WY↔Growth — 2026-05-29 — hors-canon, ne pas activer.*
