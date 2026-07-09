---
id: B3_GUARDIANS_SHARED_CONTEXT_PROOF_LOG
layer: B3_SWARM_EXECUTION
surface: Jerry Area J01 LD01 Business
domain: Growth
b3_swarm: Guardians
canon_source: Notion AGENT_REGISTRY_DB — Guardians of the Galaxy
status: SHADOW_ACTIVE
updated: 2026-05-29
---

# Shared Context & Proof Log — Guardians (artefact collectif)

Mémoire partagée du swarm + journal de preuves. Artefact **collectif** (tous les Guardians y écrivent) : empêche la re-dérivation à chaque cycle (anti-pattern Shadow L0 #7).

> **Note canon** : Groot est, dans le lore Notion, le membre **Content marketing / brand voice** (pas une fonction-mémoire). La cohérence narrative long-terme est sa responsabilité de **brand voice** (§3), mais ce journal de preuves est partagé par les 6 Guardians.

## 1. Contexte partagé (état vivant)

| Champ | Valeur actuelle |
|-------|-----------------|
| North Star Metric (P4) | **ICP-qualified AaaS opportunities generated from non-paid channels** |
| Rock actif | **J01-B2-GROWTH-2026-01** — validate first non-paid AaaS Growth loop |
| Mode growth | Brand/Story-first (Guardians) |
| Offre phare | AaaS (Agency as a Service) — à positionner painkiller (P8) |
| ICP validé ? | **NON — first JTBD assigns VoC + ICP filter to Mantis/Gamora** |
| Backlog | `../04_SUPERMAN_EXTRACTION_QUEUE.md` |

## 2. Journal de preuves (append-only)

> Chaque expérience Growth terminée s'inscrit ici avec sa preuve. Format append-only — ne jamais réécrire l'historique (immutabilité mémoire).

```yaml
# Template entrée
- experiment_id: GRD-EXP-YYYY-NN
  date: YYYY-MM-DD
  guardian_lead: StarLord | Rocket | Gamora | Drax | Groot | Mantis
  principle: P1..P18
  hypothesis: "Si [action], alors [métrique] augmente de [cible]."
  rice_score: { reach: n, impact: n, confidence: n, ease: n, score: calc }
  result: validated | rejected | inconclusive
  metric_delta: "before → after"
  proof: "link/log/screenshot/Airtable id/Supabase query"
  learning: "ce qu'on retient (alimente le prochain cycle)"
```

### Entrées

*(vide — aucune expérience Growth exécutée à ce jour. Première entrée attendue après définition du premier Rock + North Star.)*

## 2.1 JTBD actifs / prêts à lancer

```yaml
- jtbd_id: J01-B3-GROWTH-2026-001
  source_rock_id: J01-B2-GROWTH-2026-01
  status: ready
  lead: Gamora
  support: [Mantis, Star-Lord, Groot]
  source_queue: "../04_SUPERMAN_EXTRACTION_QUEUE.md#lot-1--frameworks-prioritaires-v2-principes--gamorarocket-lead"
  job_statement: "When AaaS needs its first non-paid Growth loop, produce an ICP filter, 5 voice-of-customer pain statements, and 3 painkiller positioning hypotheses so Superman can score the first experiment without guessing."
  input_artifacts:
    - "../03_SUPERMAN_GROWTH_PRINCIPLES.md"
    - "../04_SUPERMAN_EXTRACTION_QUEUE.md"
    - "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/Business_Pulse_B3_Notion_Canon_Lore_Index.md"
  expected_output_artifacts:
    - "03_SHARED_CONTEXT_AND_PROOF_LOG.md#entrees"
    - "C:/Users/amado/ASpace_OS_V2/30_Business_OS/00_Jerry_Business_Pulse/04_Business_Domains/01_Growth_Superman_Guardians"
  proof_required:
    - "5 VOC statements mapped to source or interview note"
    - "3 ICP rejection criteria"
    - "3 painkiller message variants"
    - "RICE score proposal for Superman review"
  lead_indicator: "one ICP/VOC packet completed"
  lag_indicator: "first qualified opportunity or explicit blocked proof"
```

## 3. Mémoire de marque (Groot — content / brand voice canon)

| Élément | État |
|---------|------|
| Brand voice de référence | Groot (canon : content marketing Twitter/LinkedIn/YouTube + brand voice) — sober painkiller clarity, no guru tone, no vanity metric worship |
| Positionnement canonique | Painkiller AaaS (P8) — « élimine le margin bleed des agences » |
| Mots interdits / anti-clichés | "AI magic", "passive income", "growth hack miracle", "set and forget", "guaranteed viral" |
| Promesses de marque actives | Réduire le gaspillage de marge, rendre l'acquisition traçable, créer une boucle non-payante avant scaling payant |

## 4. Hygiène de la mémoire

- **Append-only** sur le journal de preuves (P6 : documenter les apprentissages, jamais effacer).
- **Pas de preuve fabriquée** : une entrée sans `proof` réel = route Donna/DLQ (contrat d'autonomie).
- **Sync mesh** : les apprentissages durables remontent en SOPs Notion (Build_Gate testé) puis sync Supabase via worker `sync-notion-to-supabase`.
- **Anti re-dérivation** : avant toute nouvelle expérience, consulter ce log pour ne pas refaire un test déjà rejeté.

*B3 shared context under Superman (B2). Last sync: 2026-05-29*
