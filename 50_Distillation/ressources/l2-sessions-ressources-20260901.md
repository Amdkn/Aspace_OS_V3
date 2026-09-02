---
id: l2-sessions-ressources-20260901
titre: Ressources et outils — ce que les sessions mars→août 2026 utilisent et abandonnent
seau: ressources
okf_version: "0.2"
created: 2026-09-01
type: concept
distillation: work 12 (L2), agent ressources (repris par nardole_build_l2)
sources:
  - "50_Distillation/_substrat/05_Sessions.jsonl (2325 sessions, mars→août 2026)"
  - "50_Distillation/_substrat/03_Resources_Geordi.jsonl (48378 fichiers)"
  - "50_Distillation/_partiels/tranche_01..10.analyse.md (10 tranches d'intentions)"
  - "50_Distillation/METHODE.md"
---

# Ressources — ce que les sessions utilisent et abandonnent (mars→août 2026)

**Couverture déclarée (échantillon, pas inventaire) :** les 48 378 fichiers du
seau Geordi n'ont été vus que par leur extraction frontmatter/titres/plan
(`03_Resources_Geordi.jsonl`, 100 % des lignes chargées en script) — aucun
fichier brut lu en profondeur. Les 2 325 sessions de la carte
`05_Sessions.jsonl` ont été scannées par comptage de motifs sur titre + plan.
Les mentions d'outils sont des **bornes basses** : une session au titre neutre
qui utilise un outil est sous-comptée.

## 1. Mesure — outils les plus cités dans les sessions (sur 2 325)

Comptage motif (titre + plan), mesuré le 2026-09-01 par script :

| Outil | Sessions | Période dominante |
|---|---:|---|
| Multica | 594 | 07-332, 08-264 — puis abandon |
| Fable | 140 | 06→07, s'éteint ensuite |
| OMK | 64 | 06→07 |
| YouTube (ingestion) | 58 | transats + Fable/MiniMax |
| Geordi | 52 | mention réflexive |
| Claude Code | 46 | constant |
| MCP | 37 | constant |
| Hermes | 29 | fin de période |
| Antigravity | 15 | mars seulement |

Dans le seau Geordi lui-même (48 378 fichiers) : Geordi 3 862, Claude Code 868,
YouTube 688, MCP 610, Supabase 396, Hermes 382, OMK 350, Fable 349, Notion 347,
Codex 322, Antigravity 302, Multica 96.

## 2. Le cycle de vie réel d'un outil dans ce corpus

Les 10 tranches montrent un motif récurrent : **arrivée massive → pic de
sessions → crash ou boucle → abandon sans retrait de la doctrine**.

- **Antigravity/Gemini** : abandonné en mars (tranche 1, rollout-2026-03-08),
  mais 302 fichiers Geordi le citent encore et sa doctrine de mandat survit
  telle quelle dans `CLAUDE.md`.
- **Multica** : 594 sessions de juillet, ~45+ stubs qui ne font rien, crashs
  sur compaction (tranches 3-4), 96 fichiers Geordi — le plus gros consommateur
  de sessions de la période, pour le moins de production.
- **Fable/MiniMax** : ingestion YouTube massive en juin (192 sessions en 06),
  éteinte dès août.
- **Hermes** : la seule ressource dont la courbe monte en fin de période (29
  sessions en août, profils séparés, skills) — c'est l'héritier.

## 3. Ce qui reste stable

Trois ressources traversent toute la période sans boucle d'échec : **Claude
Code** (46 sessions, constant, jamais abandonné), **MCP** (37, constant),
**Supabase/Notion** (citées en continu dans Geordi, 396 et 347 fichiers). Les
configurations API (Minimax, Zcode/GLM, OpenRouter) reviennent comme frottement
récurrent (tranches 3, 5) mais jamais comme ressource perdue — A SOURCER pour
un état actuel des clés.

## Contradictions détectées (nommées, non tranchées)

1. Multica : 594 sessions consommées vs ~0 livrable traçable dans le substrat
   Picard — l'outil le plus utilisé de juillet n'a produit aucune entité de
   projet. A SOURCER (liaison session→livrable non faite).
2. Antigravity abandonné en mars vs doctrine de mandat toujours importée dans
   `CLAUDE.md` — l'outil mort et sa règle vivante coexistent.
3. Geordi contient 302 fichiers Antigravity et 96 Multica non purgés — l'archive
   ne reflète pas les abandons réels.
4. Hermes monté en fin de période mais absent des 4 seaux PARA de V2 — la
   ressource active n'est documentée nulle part dans le PARA canonique. A SOURCER.
