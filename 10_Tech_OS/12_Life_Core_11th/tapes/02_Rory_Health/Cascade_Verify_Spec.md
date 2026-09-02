# Cascade Verify Spec — Vérification de l'état matérialisé de la cascade Life OS A1/A2/A3

> Ruban φ — Spec executable. Aucune question à l'opérateur. Suite du work ASP-890
> (see review evidence). Écrit par Amy — Spec (ruban φ), L1 Life Core, 2026-09-01.

## Contexte

Le work ASP-890 (bâtisseur : `rory_build_l1`, 2026-09-01) a restauré la cascade
Life OS A1/A2/A3 dans A'Space Core via `apply_life_os_cascade.sh`. Le review du
work 10 exige une preuve d'état matérialisé, non pas des intentions.

État réel observé le 2026-09-01 (mesuré par Amy Spec avant rédaction de ce ruban,
via `multica agent list`, `multica squad list`, `multica project list`) :

- **16 agents actifs** A1/A2/A3, restaurés avec IDs originaux :
  A1-Beth, A1-Morty ; A2-Orville, A2-Discovery, A2-SNW, A2-Enterprise,
  A2-Cerritos, A2-Protostar ; A3-Pike, A3-Dal, A3-Mercer, A3-Mariner,
  A3-Picard, A3-Spock, A3-Geordi, A3-Data (tous `idle`, runtime `local`).
- **3 squads** :
  - `Squad-A3-Officiers` (id `7db85a3f-cc0d-402d-8018-ab917d48ca23`),
    leader `ea5784f0` = A3-Picard, **8 membres** (brief initial disait 7 :
    la valeur mesurée du 2026-09-01 fait foi) ;
  - `Squad-A2-Frameworks` (id `3fba8411-9214-4f85-a273-d6c002d751a8`),
    leader `4b9489db` = A2-Enterprise, **6 membres** ;
  - `Squad-A1-Beth-Morty` (id `2de55c7d-6423-4173-b844-f69c5217e8ee`),
    leader `ba488363` = A1-Beth, **2 membres**.
- **3 projets cibles existent** (statut `in_progress`) :
  `321de019` — A1 — Vision ; `9dc2df84` — A2 — Frameworks ;
  `e13a4401` — A3 — Officiers.

## Périmètre

- **Lecture seule sur A'Space Core** : `multica` en commandes de consultation
  uniquement (`agent list`, `squad list`, `squad get`, `project list`).
  Aucune création, mutation, ni suppression d'agent/squad/projet.
- **`apply_life_os_cascade.sh` ne doit PAS être modifié.** Aucune écriture sur
  ce fichier, ni sur tout autre artefact de build de la cascade.
- **Évidences** : chaque critère ci-dessous est une commande executable dont la
  sortie est la preuve. Le reviewer exécute ces commandes telles quelles.
- **Transitions kernel uniquement** : passer le work au statut `review` via
  `uc.py` (prédiction enregistrée avant vérification, puis `review`). Aucune
  écriture directe dans `uc.db` hors `uc.py`.

## Critere d'acceptation

Le reviewer review.py exécute chaque commande et exige la sortie listée.

- [ ] `multica agent list` retourne les 16 agents cibles : A1-Beth, A1-Morty, A2-Orville, A2-Discovery, A2-SNW, A2-Enterprise, A2-Cerritos, A2-Protostar, A3-Pike, A3-Dal, A3-Mercer, A3-Mariner, A3-Picard, A3-Spock, A3-Geordi, A3-Data
- [ ] `multica agent list` montre les 16 lignes en statut `idle`, runtime `local` (aucun agent manquant ni archivé)
- [ ] `multica squad get 7db85a3f-cc0d-402d-8018-ab917d48ca23` retourne Name `Squad-A3-Officiers` et Leader ID `ea5784f0-c1de-4c34-b95b-ca3785b8e5ec` (A3-Picard)
- [ ] `multica squad list` retourne `Squad-A3-Officiers` avec 8 membres
- [ ] `multica squad get 3fba8411-9214-4f85-a273-d6c002d751a8` retourne Name `Squad-A2-Frameworks` et Leader ID `4b9489db-1863-47d5-ac6a-702630a5c5c3` (A2-Enterprise)
- [ ] `multica squad list` retourne `Squad-A2-Frameworks` avec 6 membres
- [ ] `multica squad get 2de55c7d-6423-4173-b844-f69c5217e8ee` retourne Name `Squad-A1-Beth-Morty` et Leader ID `ba488363-d5cd-45eb-9fdf-a037ef17b77a` (A1-Beth), 2 membres
- [ ] `multica project list` montre les 3 projets cibles existants : `321de019` (A1 — Vision), `9dc2df84` (A2 — Frameworks), `e13a4401` (A3 — Officiers), tous `in_progress`
- [ ] `git -C C:/Users/amado/ASpace_OS_V3 status --porcelain -- 10_Tech_OS/12_Life_Core_11th/tapes/02_Rory_Health/apply_life_os_cascade.sh` (ou, si hors git, `multica` inchangé) prouve que `apply_life_os_cascade.sh` n'a pas été modifié
- [ ] `python C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel/uc.py status` retourne le work de cette vérification en statut `review` avec ses critères prouvés
- [ ] `python C:/Users/amado/ASpace_OS_V3/10_Tech_OS/kernel/uc.py review --work 19` retourne les critères prouvés (19 = id du work de cette vérification)
