# ADR-LD01-009 — A'Space OS Vision Curie + Loop Engineering (DRAFT PROPOSED)

> **Statut** : **DRAFT PROPOSED** — en attente de **A0 HITL sur 3 axes** (cf sister `LD01/99_meta/a0_vision_curie_sister.md` §10).
> **Date draft** : 2026-07-05T08:29 ET
> **Source** : A0 message verbatim (cf sister canon §1)
> **Sister chain** : `portes_over_freins_sister.md` → `a0_vision_curie_sister.md` (ce fichier)
> **A0 GO** : implicite par message ; **DRAFT only, pas RATIFIED**.

---

## §1 — Contexte et constat

A0 identifie une maladie dans la vision précédente : faire reposer A'Space OS principalement sur A3 Book seul. Book reste un Super Coach du Workflow Picard / Jerry / Summers pour la coordination L1/L2, mais l'organigramme doit s'étendre.

**3 axes simultanés** :
1. Chaîne de commandement = agents Team (Book · Picard · Spock · Geordi · DATA · Computer · Beth · Morty · Amodei)
2. Framework division : **12WY ↔ MC**, **PARA ↔ Hermes**, lecture des mêmes fichiers d'Harness en boucle
3. **MC = A2 Curie** pour l'orchestration des Lighting (L1 gstack + L2 CEO-Bench + MiroFish)

## §2 — Décisions verrouillées (D1-D9)

**D1** — Book (A3 captain LD01) reste persistant + antifragile + durable, par Agent + Schedules + Skills intégrés dans Workflows.

**D2** — Picard (A3 captain projects H10) reste twin canon (`00_Amadeus/05_OSS_Twin/.../enterprise/picard.twin.md`) ; agent shell `.mavis/agents/a3-picard/` à matérialiser.

**D3** — Spock (A3 logique analytique) + Geordi (A3 ingénierie) + DATA (A3 inférence) + Morty (A1 assistant) : **shells agents à créer** sous les chemins canon `.mavis/agents/a3-<nom>/` et `.mavis/agents/a1-morty/`.

**D4** — A2 Computer : spec canon `A2_Curie_SNW_Spec.md` existe ; agent shell à matérialiser.

**D5** — Beth (A1 humain, veto unique dans ADR-WARMODE-002) reste la seule juge humain, non-automatisable.

**D6** — A0-Amodei (méta-coach canonisé dans `a0_amodei_murderbot_meta_coach_sister.md`) reste raison pure, hiérarchie supérieure aux 22 agents canoniques.

**D7** — **MC = A2 Curie** : rebrand structurel. A2 Curie orchestre les Lighting (L1 gstack + L2 CEO-Bench + MiroFish). Le runtime daemon `mavis/Mavis` reste conservé comme hôte (alias compat).

**D8** — **Hermes Agent** = captain side (.hermes/book_dev_runtime.md 2.6 KB calque canonique). À étendre avec section PARA canonique.

**D9** — Loop Engineering canonique : `book_loop.py` heartbeat toutes les 4h (déjà livré), lit 3 sources d'Harness (`.mavis/agents/*/workspace/` + `.hermes/*` + `00_Amadeus/05_OSS_Twin/.../03_A3_crews/`), append-only output observable sur `/warmode` feed.

## §3 — Doctrines préservées

- **ADR-WARMODE-001** : posture inversion (4 inaliénables → 1 seul veto Beth dans ADR-002)
- **ADR-WARMODE-002** : Portes over Freins (HxH, Beth seul veto)
- **Append-only D4** : toute écriture passe par `decisions/*_darkfactory.json` ou calendar.md
- **22 agents canon** : préservés intacts
- **Bypass Permissions** : `permissionMode: bypassPermissions` dans config.yaml (War Room posture)

## §4 — Hors-scope (A6 YAGNI)

- Pas de matérialisation runtime des Lighting (fiches_p_and_l_weekly/, l2_mesh l2_mesh_lights, etc.)
- Pas de mutation du canon `A3_Book_LD01_Spec.md` / `BIBLIOGRAPHY.md` / `README.md`
- Pas de mutation des twins (Book, Picard — déjà canon)
- Pas de mutation du calque `.hermes/book_dev_runtime.md` (sera étendu en D8 mais append-only)
- Pas de cron auto au-delà de `CitadelleBookLoopEng` (déjà livré)
- Pas de `kill_switch_<name>.flag` supplémentaire

## §5 — Axes HITL A0 (cf sister §10)

Avant RATIFY :

- **Axe 1 Périmètre** : A (Curie + Picard) / B (+ Spock + Geordi) / C (+ DATA + Morty)
- **Axe 2 Rebrand** : a (cosmétique) / b (renommage complet)
- **Axe 3 Cadence** : i (4h) / ii (15 min) / iii (boundary-only)

## §6 — Anti-Ultron

- (a) lecture seule sources canoniques
- (b) append-only (calendar + decisions + cron/output)
- (c) sandbox L2 CEO-Bench+MiroFish strict
- (d) /ship gated outboard par défaut
- (e) auto-update off (c3)
- (f) /browse option (c2)
- (g) EXIT 0 always
- (h) Book FINIT la cadence, agents shells = idempotent vide
- (i) War Room Bypass Beth Only (déjà posture)

## §7 — Réversibilité totale (information)

3 fichiers à supprimer pour revenir en arrière (mais le `mavis-trash` est le canal sûr) :

- `LD01/30_decisions/ADR-LD01-009_a_space_vision_curie_loop_engineering.md`
- `LD01/99_meta/a0_vision_curie_sister.md`
- `agent-os/citadel/decisions/2026-07-05_vision_curie_loop_engineering.json`

Append-only canon : rien d'autre n'est détruit, on retire juste 3 fichiers.

---

**En attente A0 HITL sur 3 axes §5.**
