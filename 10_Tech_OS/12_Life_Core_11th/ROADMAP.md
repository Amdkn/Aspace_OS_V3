# ROADMAP — Life Core · 11e Docteur

> Artefact du **11e Docteur**, rang Manager. Cycle : **mensuel**.
> Source amont : `10_Tech_OS/00_Governance_Rick/PLAYBOOK.md` (cycle 12WY).
> Aval : `compagnons/*/RUNBOOK.md` (cycle hebdomadaire).

**Squelette engendré.** Le contenu ci-dessous est à remplir par le Docteur, mois par mois.
`spawn.py --force` réécrit ce fichier : archiver un mois clos avant de ré-engendrer.

---

## Mois en cours — `2026-08`

### Rattachement au playbook

| | |
|---|---|
| Playbook 12WY | `bootstrap-life-os-a1a2a3` (cycle de démarrage — cascade Life OS) |
| Semaines du cycle couvertes | `S1-S2 sur 12` (bootstrap, hors cycle productif) |
| Couche | `L1` — maîtrise `20_Life_OS` |

### Étapes

Chaque étape tient dans **un seul ruban**. Si elle en demande deux, elle n'est pas décomposée.

| # | Étape | Organe | Titulaire | Critère de fin **vérifiable** | Statut |
|---|---|---|---|---|---|
| 1 | Cascade Spec v1 — blueprint A1/A2/A3 + script dry-runnable | Spec | Amy | `cascade_blueprint_v1.md` (19443 B) attache a ASP-890 commentaire 87f13ec9 ; `bash apply_life_os_cascade.sh --dry-run` exit 0, 35 lignes emises ; 16 agents x 6 cles (name/description/instructions sketch <=200 mots/runtime_id/visibility/squad_id cible) ; 3 squads + 3 projets decrits | **DONE — PASS 3/3 (revue 6a8700ff, 11e Docteur)** |
| 2 | Build — materialiser les 22 objets dans A'Space Core via `apply_life_os_cascade.sh --apply` | Build | Rory | `multica agent list` retourne 24 agents (8 existants + 16 nouveaux) ; `multica squad list` retourne 7 squads (4 existantes + 3 nouvelles) avec leaders A2-Enterprise et A3-Picard ; `multica project list` retourne 5 projets (2 existants + 3 nouveaux) ; les 22 IDs sont publies dans le commentaire de retour sur ASP-890 | **IN PROGRESS — ruban admis `tapes/02_Rory_Health/Cascade_Build_Spec.md`, work L1 soumis au noyau UC** |
| 3 | Replication template — derivation d'un rang A futur depuis le ruban Blueprint | Spawn | River | `spawn_a_level.py --config a4_demo.json` produit `agents=5 squads=1 projects=1` ; cles agent normalisees `(name, description, instructions, runtime, visibility, squad_id)` ; runtime herite du blueprint Amy (`19e5593d-44a4-4466-800c-066190bfc2f9`) ; `routing=leader` ; partition 6 agents / 4 par squad produit split 4+2 | **DONE — PASS 4/4 (revue 0571b564, 11e Docteur)** |

Un critère de fin sans chiffre, comparaison, commande ou case à cocher sera **refusé par le
portier**. Le vérifier ici évite un aller-retour.

### Ce que ce mois ne fait pas

- Ne crée aucun second workspace (cloisonnement maintiens : A'Space Core uniquement).
- Ne transfere pas la construction de Life OS au 12e Docteur ni a Buzz-Core-12th (decision Rick, commentaire f03735e3 sur ASP-890).
- Ne produit pas de roadmap ailleurs que dans ce fichier (rang Manager).
- Ne produit pas de playbook 12WY (rang Entrepreneur, c'est Rick).
- Ne modifie pas `cascade_blueprint_v1.md` ni `apply_life_os_cascade.sh` (ruban admis par Amy, en lecture seule).

---

## Mois clos

| Mois | Étapes livrées | Détachées | Échecs remontés à Donna |
|---|---|---|---|
| | | | |

## Contrôle de fin de mois

- [x] chaque étape a un titulaire nommé
- [x] chaque critère de fin est vérifiable
- [x] aucune étape ne dépasse un ruban
- [ ] les échecs répétés sont chez Donna, pas ici (en attente — étape 2 Build)