---
title: "Initialiser le module 23_12WY_SNW : dossiers A3 PARA + bus state.json + journal de cycle W13/W0"
layer: L1
---

## Objectif

Compléter l'initialisation du module 12 Week Year SNW (`20_Life_OS/23_12WY_SNW/`), dont les specs A2/A3 existent déjà (5 sous-dossiers discipline Pike/Una/M'Benga/Chapel/Ortegas présents), par les trois pièces manquantes exigées par le canon :

1. Créer les 4 sous-dossiers PARA exigés par `23_12WY_SNW/AGENTS.md` §Rangement (absents du disque, mesuré 2026-09-02) : `01_Projects_Picard/`, `02_Areas_Spock/`, `03_Resources_Geordi/`, `04_Archives_Data/`, chacun avec un `README.md` de 3 lignes minimum indiquant son rôle de rangement (artefact vivant → Picard ; responsabilité continue → Spock ; savoir réutilisable → Geordi ; état révolu → Data).
2. Créer le bus de symphonie `C:/Users/amado/ASpace_OS_V2/00_Amadeus/40_SYMPHONY_BUS/` avec un `state.json` conforme au bloc JSON de `A2_Curie_SNW_Spec.md` §state.json bus : cycle "Q3-2026", week "W1", stage "snw_planning", agent_path "A1:Morty > A2:Curie_SNW > A3:Una", 12wy_discipline "Planning", next_step "A3:MBenga".
3. Créer le journal de cycle `23_12WY_SNW/Cycle_Q3_2026_Calendar.md` matérialisant la table de décomposition de `W1_Item2_13e_Semaine_Rock_Decomposition.md` : lignes W1 à W4 avec dates et owners, ligne W13 = 09/14/2026 (13e semaine, buffer de transition), ligne W0 = 09/21/2026 (Semaine 0 du Cycle 4, kick-off production lundi 09/28), avec la fenêtre SDD-010 §6.1 (veto 90j expiré le 2026-08-11, W13 = première semaine autorisée pour un nouveau SDD).

## Critère d'acceptation

- [ ] `ls C:/Users/amado/ASpace_OS_V3/20_Life_OS/23_12WY_SNW/` liste les 4 dossiers `01_Projects_Picard 02_Areas_Spock 03_Resources_Geordi 04_Archives_Data` (9 entrées au total au lieu de 5 sous-dossiers actuels : les 5 disciplines + les 4 PARA).
- [ ] Chacun des 4 README PARA fait ≥ 3 lignes non vides (vérifiable : `wc -l` sur chaque fichier ≥ 3).
- [ ] `cat C:/Users/amado/ASpace_OS_V2/00_Amadeus/40_SYMPHONY_BUS/state.json | python -m json.tool` retourne 0 et contient les 6 clés : cycle, week, stage, agent_path, 12wy_discipline, next_step — avec stage exactement égal à "snw_planning".
- [ ] `state.json` pèse < 10240 octets (garde-fou rotation §state.json bus de la spec Curie).
- [ ] `grep -c "^| W" C:/Users/amado/ASpace_OS_V3/20_Life_OS/23_12WY_SNW/Cycle_Q3_2026_Calendar.md` retourne ≥ 6 (lignes W1, W2, W3, W4, W13, W0).
- [ ] `grep "09/14" Cycle_Q3_2026_Calendar.md` et `grep "09/21" Cycle_Q3_2026_Calendar.md` trouvent chacun au moins 1 occurrence avec les libellés "13e semaine" et "Semaine 0" respectivement.
- [ ] `grep "2026-08-11" Cycle_Q3_2026_Calendar.md` retourne ≥ 1 occurrence (fenêtre SDD-010 documentée).

## Périmètre

Dedans :
- `C:/Users/amado/ASpace_OS_V3/20_Life_OS/23_12WY_SNW/01_Projects_Picard/` et les 3 dossiers PARA suivants, avec un seul `README.md` chacun.
- `C:/Users/amado/ASpace_OS_V2/00_Amadeus/40_SYMPHONY_BUS/state.json` (répertoire créé si absent).
- `C:/Users/amado/ASpace_OS_V3/20_Life_OS/23_12WY_SNW/Cycle_Q3_2026_Calendar.md` (un fichier nouveau, à la racine du framework).

Dehors :
- Tout contenu des 5 dossiers discipline existants (`01_Vision_Pike` à `05_Execution_Ortegas`) : aucun fichier modifié.
- Les specs `A2_Curie_SNW_Spec.md`, `W1_Quarter_Intent_Q3_2026.md`, `W1_Item2_13e_Semaine_Rock_Decomposition.md`, `W1_Shadow_Tools_Routing.md` : lecture seule, sources des valeurs à matérialiser.
- Tout autre framework 20_Life_OS (21, 22, 24, 25, 26) et tout dossier `00_Gatekeepers_Beth_Morty/`.

## Interdits

- Ne pas écrire dans `20_Life_OS/00_Gatekeepers_Beth_Morty/` (veto A1 Beth) ni dans aucun autre framework que 23_12WY_SNW.
- Ne pas modifier `10_Tech_OS/kernel/` (uc.db, gate.py, schema.sql) — noyau sacré.
- Ne pas toucher aux 5 dossiers discipline existants ni aux 6 fichiers racine du module.
- Ne pas marquer `done` : seul le 11e Docteur détache depuis `review`.
- Ne pas insérer de marqueur de travail non résolus que le portier traque (cf. `gate.py` BLOQUANTS) : le ruban serait refusé.
- Ne pas écrire dans `~/.hermes/` (stub legacy) ni dans un profil Hermes autre que `amy_spec_l1`.
