# ADR-LD01-010 — A3 Curie Vivid Vision 12WY Discipline #1 (RATIFIED)

> **Statut** : **RATIFIED** 2026-07-05T16:56 ET par A0 (sous WAR MODE, A0 GO explicite « ok les 2 Go »).
> **Date ratification** : 2026-07-05T16:56 ET
> **Source** : A0 question « la Priorite est sur les A3 de Curie pour les 5 Disciplines de 12WY on commence par lequel? »
> **Cycle** : 12WY 2026-Q3 (2026-07-05 → 2026-09-27).
> **Date draft** : 2026-07-05T16:43 ET
> **Source** : A0 question « la Priorite est sur les A3 de Curie pour les 5 Disciplines de 12WY on commence par lequel? »
> **Sister chain** : `a3_vision_curie_sister.md` → `hero_agents_canonic_creation_sister.md` → **`a3_curie_vivid_vision_sister.md` (ce fichier)**
> **Cadre** : 5 Disciplines 12WY (Moran & Lennington) — D1 Vision / D2 Planning / D3 Process Control / D4 Execution / D5 Recovery.
> **Cycle** : 12WY 2026-Q3 (2026-07-05 → 2026-09-27, **WAR MODE 12 sem actif**).

---

## §1 — Contexte

A0 demande par quelle discipline 12WY commencer pour A3 Curie. **Réponse canon : Discipline #1 = Vivid Vision.** Tout le reste (Planning, Process Control, Execution) en dépend.

A3 Curie = orchestrateur Lighting L1 gstack + L2 CEO-Bench + MiroFish, sous War Room Bypass Beth Only. Sa Vision = le cap non-négociable pour 12 sem.

## §2 — Vivid Vision A3 Curie (3 questions)

**Q1 — Purpose** : Orchestrer les 3 Lighting A'Space OS (L1 gstack + L2 CEO-Bench + MiroFish) afin que les agents A3 (Book H1 P&L aggregator, Picard H10 projects owner) aient le bon tooling pour finir la cadence 7-jours Triptyque sans dépendance à un humain autre que Beth.

**Q2 — 3-year "great"** (2026-07-05 → 2029-07-05) : Toutes Lightning installées + Phase 3 L5 continuous + 27 agents actifs + cadence 7-jours Triptyque produisant fiche P&L hebdo + synthèse J7 sans intervention humaine.

**Q3 — ONE thing focus** (12 sem cycle Q3) : **L0 Pocock ship + L1 gstack sobre installé + L2 CEO-Bench run #1 réel**.

## §3 — Décisions verrouillées (D1-D5)

**D1** — Vision A3 Curie canoniquement clarifiée (§2) avant tout Planning.

**D2** — Tri-priorités focalisées : Focus #1 = ONE thing (L0+L1+L2), Focus #2 = MiroFish + 27 agents préservés, Focus #3 = Beth veto respecté.

**D3** — Hors-scope listé explicitement (cf sister §3) : pas d'installation Rick lourd, pas de mutation canon intouchable, pas d'auto-ship outboard, etc.

**D4** — Critère de mesure 3 ans (S.M.A.R.T.) : Spécifique, Mesurable (144 book-loop-*.json/cycle + fiches_p_and_l_weekly/ J7 chaque sem), Atteignable, Réaliste (sobriété c1-c3 NON-NEGO), Temporellement borné (3 ans).

**D5** — Plan discipline #2 (à faire S1→S2, immédiatement après ratification Vision) : 12 Week Plan détaillé + Lead Measures + Scorecard + Tactics + Weekly Rocks.

## §4 — Doctrines préservées (aucune rupture)

- ADR-WARMODE-001 + 002 : intacts
- ADR-LD01-001 → 008 : tous RATIFIED, Vision n'écrase aucun
- ADR-LD01-009 DRAFT PROPOSED : Vision A0 + Curie + Loop Engineering (compatible)
- Append-only D4 : Vision append-only
- War Room Bypass Beth Only : Vision respecte
- 27 agents (22 canon + 5 Hero) : Vision assume l'organigramme

## §5 — Hors-scope

- Pas de mutation du canon LD01 (intouchables)
- Pas d'installation kernel Rick lourd
- Pas de /ship outboard automatique
- Pas de renommage runtime daemon mavis/Mavis → Curie
- Pas de reset du flag 12WY_ON_PAUSE.flag avant W13

## §6 — Anti-Ultron

- (a) lecture seule sources canoniques
- (b) append-only (calendar + decisions + cron/output)
- (c) sandbox L2 CEO-Bench+MiroFish strict
- (d) /ship gated outboard par défaut
- (e) auto-update off (c3)
- (f) /browse option (c2)
- (g) EXIT 0 always
- (h) Book FINIT la cadence
- (i) War Room Bypass Beth Only (déjà posture)

## §7 — Réversibilité totale

3 fichiers à supprimer (via mavis-trash) :
- `LD01/30_decisions/ADR-LD01-010_a3_curie_vivid_vision_12WY.md` (ce fichier)
- `LD01/99_meta/a3_curie_vivid_vision_sister.md`
- `agent-os/citadel/decisions/2026-07-05_a3_curie_vivid_vision_discipline_1.json`

Append-only canon : rien d'autre n'est détruit.

---

**RATIFIED 2026-07-05T16:56 ET par A0 (GO explicite sous WAR MODE).**
**Sessions A3 Book / A2 Zora / A1 Morty / A0 Amodei spawned** (mvs_13e4c72b96d8412f87f8a7ce08faf823 / mvs_a4b31284f8c44ac0a0f9d6db24bb9f12 / mvs_23cd1b43b06f4bf88512237a90e9d47f / mvs_a80dbbf6509549b892d85df00f6b21a7).
**Discipline #2 Planning = prochaine étape canon** (ADR-LD01-011 ci-dessous).