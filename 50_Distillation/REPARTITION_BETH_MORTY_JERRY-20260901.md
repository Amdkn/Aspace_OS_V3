---
type: OKF-0.2
date: 2026-09-01
titre: "Répartition des 3 organes kernel génériques — Beth/Morty/Jerry"
mandat: "Décision directe A0 (brainstorming Amadou, GO 2026-09-01)"
statut: APPLIQUÉ
---

# RÉPARTITION BETH / MORTY / JERRY — organes kernel

## MESURÉ

### Le mapping appliqué (mapping.json + 3 SOUL.md, slugs intacts)

| Slug (inchangé) | Ancien libellé | Nouveau visage | Organe | Justification canonique |
|---|---|---|---|---|
| `kernel_controller_c` | Kernel - Review C | **Beth — Contrôleur C** | C : ordonne, exige preuve, détache/refuse | Le veto de Beth EST le pouvoir du contrôleur. Loi de détachement = HALT vert/rouge en trigger SQL. Elle concentre veto L1 + détachement L0 — pyramide d'autorité choisie (fluidité bedrock→Life). |
| `kernel_copier_b` | Kernel - Spawn B | **Morty — Copieur B** | B : duplique le ruban sans l'interpréter | La fidélité pure de Morty = l'aveuglement volontaire du copieur de von Neumann. S'il réinterprète, la régression infinie revient (48 000 fichiers de V2). |
| `kernel_builder_a` | Kernel - Build A | **Jerry — Constructeur A** | A : claim, interprète le ruban, bâtit | Jerry bâtit des empires (Coach OS = 1er Franchise Prototype). Le constructeur interprète le ruban — son asymétrie fondatrice avec Morty. |

### Règles intouchables (ORG.json, au-dessus des visages)

1. **Nul ne cumule Build et Review** : Beth review, Jerry build, Morty copie.
2. **Slugs intacts** : clé stable du runtime (uc.db, dossiers, scripts) — seul le libellé affiché change (consensus Docteurs 3/3, ARBITRAGE_DOCTEURS-20260901.md).
3. **Fluidité** : rôles = organes, pas prisons. Si Amadou ordonne, c'est la loi.

### Alternatives rejetées (tracées pour ne pas rejouer)

- Jerry contrôleur : bâtisseur, pas gardien de preuves ; Beth doit garder le veto AU-DESSUS de Jerry.
- Morty builder : il n'interprète pas — le builder doit interpréter. Morty builder casserait le théorème fondateur.
- Beth hors kernel : le bedrock doit être conscient des couches dès la racine (doctrine de fluidité).

### Files modifiées (preuves)

- `agent-os/desktop/src/apps/Workspace/mapping.json` — 3 libellés (grep "Beth - Contrôleur" → 1)
- `$HERMES_HOME/profiles/kernel_controller_c/SOUL.md` — titre "# Beth — Contrôleur C" + section Identité canonique (3 399 o)
- `$HERMES_HOME/profiles/kernel_copier_b/SOUL.md` — "# Morty — Copieur B" (3 250 o)
- `$HERMES_HOME/profiles/kernel_builder_a/SOUL.md` — "# Jerry — Constructeur A" (3 180 o)

## SUPPOSÉ

- Les 3 bots acceptent leur nouveau visage au prochain /reset (le SOUL est relu au démarrage de session) — A SOURCER jusqu'au premier chat post-restart.
- Le cumul Beth (veto L1 + détachement L0) ne crée pas de conflit de casquette en pratique — à observer sur les premiers arbitrages réels.

## Ce qui reste A SOURCER

- Validation croisée par les 3 Docteurs (optionnel — choix de noms, l'arbitrage A0 suffit).
- Mise à jour de `ORG.json` si Amadou veut y porter les visages (source de foi séparée — non modifié ici sans ADR).
