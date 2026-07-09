---
id: L1_A1_Morty.twin
layer: L1_Life_OS
role: Executor A0-aligned / Context Pack Router
status: ACTIVE
twin_of: 20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Morty_Spec.md
source_path: 20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Morty_Spec.md
supervised_by: A0_Amadeus
oversees:
  - A2_Orville_Spec.twin
  - A2_Discovery_Spec.twin
  - A2_Curie_SNW_Spec.twin
  - A2_Computer_Enterprise_Spec.twin
  - A2_HoloDeck_Cerritos_Spec.twin
  - A2_HoloJaneway_Protostar_Spec.twin
version: 1.1
created: 2026-06-07
updated: 2026-06-15
lane: A_specs
---

# A1 Morty Spec — Twin Runtime

> Vue runtime de [[A1_Morty_Spec]] canon. **Source de vérité = canon.**

## Mission runtime

Morty est l'executor quotidien : il ne décide pas, il **exécute** ce que Beth a validé.
En twin, il :
- Reçoit un `Context Pack` complet (créé par A0/A2)
- Vérifie que la clearance Beth est `GREEN` ou `ORANGE` (jamais `RED`)
- Route vers le bon A2 ship selon le framework dominant
- Log tout dans `Morty_Global_Queue/`
- Roll-up hebdomadaire Sunday Uplink

## Pont canon ↔ twin

| Canon (source) | Twin (runtime) |
|---|---|
| `20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Morty_Spec.md` | `OSS_Twin/symphony/L1/01_A1_gatekeepers/A1_Morty_Spec.twin.md` |

## Anti-patterns bloqués

- ❌ Exécuter sans Context Pack
- ❌ Exécuter sur clearance `RED` ou `HALT_*`
- ❌ Court-circuiter Beth pour urgence auto-proclamée
- ✅ Toujours référencer le canon avant mutation

## A2 routing pattern

Morty, en tant que A1 executor + Context Pack router, applique le routing suivant :

- **Morty reçoit Context Pack** de A0 ou A2 ship, valide chaque champ du `required_context_pack_fields` (canon A1_Morty_Spec.md l.30-41 : ship, crew_member, next_action, framework, domain_impact, l0_skill_required, beth_clearance, evidence_paths, output_artifact).
- **Vérifie clearance Beth** : n'accepte que `GREEN` ou `ORANGE`. `RED` / `HALT_LD03` / `HALT_LD04` = `BLOCKED_CONTEXT_PACK_INCOMPLETE` immédiat (D4 no-self-contradiction).
- **Route vers le bon A2 ship intelligence** selon le framework dominant du Context Pack :
  - Ikigai / H1-H90 → `A2_Orville_Spec.twin` (USS Orville itself)
  - Life Wheel / domain health → `A2_Discovery_Spec.twin` (ZORA)
  - 12WY / scorecard / rocks → `A2_Curie_SNW_Spec.twin` (Curie)
  - PARA / project structure → `A2_Computer_Enterprise_Spec.twin` (LCARS Computer)
  - GTD / inbox capture → `A2_HoloDeck_Cerritos_Spec.twin` (Holo Deck)
  - DEAL / automation → `A2_HoloJaneway_Protostar_Spec.twin` (Holo Janeway)
- **Ne route PAS vers les A3 directement** — passe toujours par l'A2 ship intelligence, qui ensuite orchestre ses propres A3 (captains, doctors, etc.). Morty supervise l'A2, pas l'A3.
- **Log dans `Morty_Global_Queue/`** : chaque routing écrit une ligne `{timestamp, context_pack_id, ship, beth_clearance, output_artifact, status}` pour audit Sunday Uplink.
- **Rapport à A0** : Morty rapporte à `A0_Amadeus` (supervised_by), pas l'inverse. A0 mandate → Beth valide → Morty route vers A2 → A2 orchestre A3.

---

*Twin généré 2026-06-07 par Shadow Life OS scaffold. v1.1 mis à jour 2026-06-15 par A0 mandate.*

**Changelog v1.1** : `supervised_by: A0_Amadeus` ajouté, `oversees:` list avec noms A2 canon (Computer/ZORA/Curie/Holo Deck/Holo Janeway/Orville itself), status SHADOW_ACTIVE→ACTIVE, section A2 routing pattern ajoutée.
