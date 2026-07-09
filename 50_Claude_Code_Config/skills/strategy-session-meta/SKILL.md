---
name: strategy-session-meta
description: Generate or execute the weekly Strategy Session — D1-measured, blunt, gap-correcting. Use when the user says "strategy session", pastes a "RAPPORT STRATEGY SESSION" block, or on Monday cadence. Two phases: GENERATE (collect_metrics.py → questions.json → render_session.py) and EXECUTE (parse → D1-locate avoided task → fix → receipts → WEEK_CONTRACT.md).
allowed-tools: [Bash, Read, Write, Edit]
disable-model-invocation: true
version: 1.1.0
author: Hermes Agent (HA, A3 Picard in PARA, 2026-07-05 re-roled; original Mavis 2026-07-04)
license: MIT
# Pocock canon applied 2026-07-05 (see LESSONS.md §Pocock-audit)
---

# strategy-session-meta

## Ce que ce skill mécanise (né des 2026-07-03/04)

La boucle complète mesure → confrontation → correction :
la session W3 a mesuré "Sobriété méta 3/10 + Takeout évité" → le workflow d'exécution
a extrait le Takeout, trouvé un bug D6 (cap lockout), ingéré 87 ressources, et produit
le contrat de semaine. Ce skill rend cette boucle **répétable chaque lundi**.

## PHASE 1 — GENERATE (lundi, ou sur demande)

```bash
# 1. Sweep D1 mécanique (agnostique, aucun LLM)
PYTHONIOENCODING=utf-8 "C:/Python314/python.exe" scripts/collect_metrics.py
# -> sessions/metrics-<date>.json : handoffs semaine, ADR par statut, GOs ouverts,
#    plans touchés, ressources Geordi, historique sessions

# 2. L'agent (n'importe quel harness) AUTEURE sessions/questions-<date>.json
#    RÈGLE DURE : chaque question scorée cite un FAIT MESURÉ du metrics.json ou du
#    rapport précédent. Zéro question de coaching générique. 4 zones : client /
#    finance / meta / cadence. 3 moves par zone + blunt_line par zone.

# 3. Render + validation intégrée (offline pur, intégrité structurelle)
PYTHONIOENCODING=utf-8 "C:/Python314/python.exe" scripts/render_session.py sessions/questions-<date>.json
# -> ASpace 00_Amadeus/strategy_sessions/<date>_W<n>_strategy_session.html
#    exit 2 si lien externe ou zone sans moves — jamais de faux succès
```

## PHASE 2 — EXECUTE (quand A+ colle le rapport)

Runbook de correction des gaps — ordre STRICT, distillé de l'exécution réelle du 04/07 :

1. **Parse** : zone la plus faible + "CE QUE TU ÉVITES (tes mots)" + focus. Les mots de A+ priment sur toute interprétation.
2. **D1-locate la tâche évitée** : elle est presque toujours localisable sur le filesystem (un zip, un dossier, un fichier non traité). La localiser AVANT tout discours.
3. **Exécuter avec l'outillage EXISTANT** (compatible moratoire ; un ordre explicite A+ prime sur le moratoire).
4. **0-résultat sur matière non vide = ANOMALIE, pas succès** — root-cause D6 obligatoire (précédent : cap lockout qui a bloqué 2 semaines d'ingestion en silence).
5. **Fixer le bug trouvé + `LESSONS.md`** du skill concerné (append-only).
6. **Receipts D5** : chiffres réels + ligne wiki/log.md.
7. **`contracts/WEEK_CONTRACT.md`** : les 3 moves du rapport + statut (fait / gated A0 / à toi) + suivi dans la semaine. Lundi suivant → PHASE 1 avec les nouvelles métriques.

## Les 3 couches

| Couche | Mécanisme |
|---|---|
| **Agnostique** | 2 scripts pur stdlib, env-vars, aucun appel harness. Le questions.json est le contrat agent↔script : n'importe quel LLM peut l'auteurer. |
| **Persistant** | `sessions/` (metrics + questions + HTML datés), `contracts/WEEK_CONTRACT.md`, historique complet des rapports collés (append dans `sessions/report-<date>.txt`). |
| **Antifragile** | Validation post-render (offline, moves par zone) = exit 2 sur défaut. Étape 4 du runbook = le détecteur d'anomalie silencieuse. `LESSONS.md` append-only. |

## Règles dures (anti-dérive)

- Une question sans fait mesuré derrière = interdite. Le template Fable dit : viser "là où ce que tu fais contredit ce que tu dis important" — ça exige des données, pas des platitudes.
- Le rapport généré garde le FORMAT EXACT (`═══ RAPPORT STRATEGY SESSION...`) — la PHASE 2 dépend de ce format pour parser.
- La zone faible du rapport = le focus de la semaine. Pas de renégociation par l'agent.
- Blunt ≥ 7 → la blunt_line s'affiche. L'agent n'adoucit jamais un rapport que A+ a calibré dur.

## Sisters

- `2026-07-03_W3_strategy_session.html` — l'artefact fondateur (questions hardcodées, v1 manuelle)
- `takeout-delta-ingest` — premier skill né d'une PHASE 2 (la tâche évitée de W3)
- Geordi `02_Templates` Fable Use Case #4 — le template source
- `contracts/WEEK_CONTRACT.md` — le contrat vivant de la semaine courante
- `../writing-great-skills/SKILL.md` — canon qualité (Pocock). À consulter **avant** toute modif du SKILL.md (audit sister). Ne pas répliquer les règles Pocock ici — référence par pointeur.
