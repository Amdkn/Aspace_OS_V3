# HANDOVER — Certification Hermes Bot Mode dans les worktrees Orca

Date : 2026-09-24. Destinataire : nouvelle session Chat disposant de Desktop Commander (DC) sur Amd-PC.
Mandant : Amadou Koné / A0. Statut au transfert : configuration préparée et vérifiée, orchestration de bout en bout NON CERTIFIÉE.

## 1. Instruction immédiate à la session repreneuse

Lis ce fichier via DC et exécute la certification ci-dessous. Commence par observer le poste et les sessions existantes. Réutilise les profils, conversations et worktrees. Ne reconstruis pas toute la conversation; ne remplace pas l'exécution par un nouveau plan. Progresse sans demander à Amadou de transmettre manuellement les tâches entre agents. Rapporte les preuves, corrections, blocages réels et arbitrages irréductibles.

Amadou veut poursuivre dans une session Chat avec DC, hors consommation du quota Work selon son choix d'interface. Cette préférence est une contrainte d'usage, PAS une propriété garantie par ce fichier ou par DC. Aucun réglage de quota n'a été effectué. Ne promets pas de gratuité et ne déclenche pas une migration vers Work.

Objectif : Doctors S2 effectivement managers des PRD, délégant l'exécution à des Compagnons techniciens S3 et supervisant leurs résultats, sous les gates de Rick S1. Amadou reste A0, propriétaire des finalités. La progression doit libérer son temps vers Life OS et Business OS, sans nouvelle hypertrophie documentaire.

## 2. Sources locales à lire, dans cet ordre

Racine : `C:/Users/amado/ASpace_OS_V3`.
1. `AGENTS.md`, puis les AGENTS.md des seuls sous-arbres concernés.
2. `40_Memory_Wiki_OKF/operations/reprise_hermes_orca_2026-09-24.md` : décisions, limites et pièges.
3. `10_Tech_OS/reports/hermes_bot_worktree_bindings.json` : correspondances exactes, commandes, sauvegarde.
4. `10_Tech_OS/kernel/COMPANIONS_CONSTITUTION.json` : identités, opérateurs, autorités interdites, typed I/O et handoffs.
5. `10_Tech_OS/00_Governance_Rick/WATCHDOG.md` avant intervention runtime/kernel.
6. `10_Tech_OS/reports/ker44_final_acceptance.json` et `ker44_independent_review_final.json` uniquement pour retrouver les preuves déjà acquises.

Pas de scan récursif de tout le disque. Utiliser rg et les chemins bornés. Ne jamais imprimer de secrets, fichiers .env ou tokens.

## 3. Mandat de gouvernance et des trois managers

| Niveau / rôle | Responsabilité attendue | Exécution déléguée |
|---|---|---|
| A0 Amadou / Kirby | Finalités, priorités, contraintes, arbitrages irréductibles | Ne fait pas le relais manuel entre techniciens |
| S1 Rick | Cohérence des mécanismes, gates, arbitrage transversal et promotion | Ne s'attribue pas les trois OS ni la construction routinière |
| S2 Doctor13 — Récursivité / Kernel | Manager des PRD du mécanisme qui construit, observe et mémorise sa propre production | Ryan, Yaz, Graham comme équipe de référence |
| S2 Doctor11 — Interface / Life | Manager des PRD d'interface humain-agent, intégrité et continuité des flux Life | Amy, Rory, River comme équipe de référence |
| S2 Doctor12 — Expansion / Business-Buzz | Manager des PRD de découverte, conception et distribution de capacités/offres | Bill, Clara, Nardole comme équipe de référence |

Ces trois axes opérationnels expriment la demande actuelle d'A0. Le canon existant route Doctor13 vers L0, Doctor11 vers L1 et Doctor12 vers L2. Ne pas confondre ces couches avec les niveaux d'autorité S1/S2/S3. Les libellés historiques home_core sont partiellement incohérents entre eux : ne pas leur inventer une nouvelle numérotation pendant la certification; signaler un conflit sémantique réel et le résoudre explicitement.

Chaque Doctor doit : comprendre le résultat et les critères du PRD; décomposer en tâches bornées; attribuer propriétaire et dépendances; déléguer au Compagnon approprié; suivre l'exécution réelle; débloquer ou réorienter; organiser une revue indépendante; présenter la preuve à la gate; clôturer avec traçabilité. Un titre « Doctor » ou un SOUL lu ne prouve pas cette capacité.

Les Compagnons peuvent intervenir dans les trois Cores selon mandat. Une équipe de référence n'est pas une exclusivité. Harness et modèle sont des moyens remplaçables; l'identité et l'autorité ne changent pas lors d'un changement de modèle.

## 4. Identités et espaces déjà disponibles

Hermes effectif : `C:/Users/amado/AppData/Local/hermes`.
Binaire : `C:/Users/amado/AppData/Local/hermes/bin/hermes.exe`.
Orca CLI : `C:/Users/amado/AppData/Local/Programs/orca/resources/bin/orca.exe`.
Base des worktrees : `C:/Users/amado/orca/workspaces/ASpace_OS_V3/`.

| Rôle | Profil Hermes existant | Dossier du worktree | Opérateur / fonction |
| Doctor11 | `doctor11_review_l1` | `opah` | Manager PRD / supervision S2 |
| Doctor12 | `doctor12_review_l2` | `snook` | Manager PRD / supervision S2 |
| Doctor13 | `doctor13_review_l0` | `scup` | Manager PRD / supervision S2 |
| Ryan | `ryan_build_l0` | `Ryan` | Build of Build |
| Yaz | `yaz_spec_l0` | `Yaz` | Observe of Observe |
| Graham | `graham_spawn_l0` | `Graham` | Memory of Memory |
| Bill | `bill_spawn_l2` | `Bill` | Discover of Discover |
| Clara | `clara_spec_l2` | `Clara` | Design of Design |
| Nardole | `nardole_build_l2` | `Nardol` | Dispatch of Dispatch |
| Amy | `amy_spec_l1` | `Amy` | Interface of Interface |
| Rory | `rory_build_l1` | `Rory` | Integrity of Integrity |
| River | `river_spawn_l1` | `River` | Flow of Flow |

Les identifiants contenant spec/build/spawn/review sont conservés pour compatibilité; ils ne doivent pas enfermer les responsabilités. Nardole est affiché correctement mais son dossier historique s'appelle Nardol. Les Doctors gardent opah/snook/scup; ne pas déplacer un worktree occupé pour une simple harmonisation de nom.

Chaque profil a terminal.cwd fixé et des métadonnées Bot Mode avec nom canonique. Lanceurs : `C:/Users/amado/.aspace/launchers/hermes-bots/<Role>.cmd`. Ils appellent `hermes -p <profil> chat --in <worktree> --continue "Bot Chat" --create-if-missing`.

IMPORTANT : les anciennes sessions ouvertes n'ont PAS été migrées. Vérifier leur profil, cwd et conversation avant réutilisation. Aucun second processus écrivain sur le même profil. Le clic et le rendu Bot Mode, la reprise effective de Bot Chat, les échanges entre bots et l'inférence n'ont pas encore été certifiés. Ne pas présenter un terminal CLI comme preuve de l'interface Bot Mode.

Piège payé : `C:/Users/amado/.hermes/profiles` contient aussi des identités mais n'est pas le home utilisé par le binaire interrogé. Ne pas y écrire seul en supposant configurer les bots actifs. Préserver les mémoires et identifiants; ne pas cloner les tokens OAuth.

Rick n'a pas été reconfiguré. Son espace Orca existant est stickleback, affiché S1 Rick. Vérifier son profil effectif avant toute liaison : le profil nommé rick_governance_l0 portait une description Donna; le profil par défaut était affiché Rick. Ne pas déduire une identité du seul nom de dossier. Donna existe dans l'historique, mais n'est pas l'un des neuf Compagnons de la constitution KER-44; ne pas ajouter une dixième place sans décision A0.

## 5. Ce qui est terminé — ne pas refaire

- WorkGraph 181 : done; gates de propriété et dispatch véridique, revue Hermes PASS, 21 tests; commit V3 8de0a13cd79c337f3536cf5c74949da2372eb108.
- WorkGraph 180 / KER-44 : done; 40 tests, revue indépendante Hermes PASS, constitution et projections bornées exécutables, API GET. Commit V3 038dff0ef2d10e8d485a8f53e5e57485853bc39d; Desktop 6db8908d12a23b2043e4b2be8d8cabc2bce497e9. Bindings 70/71 fermés, claim180 libéré lors de la clôture.
- 96 PR Amdkn/Aspace_OS_V3 fermées explicitement SANS fusion, branches conservées. Zéro ouverte au contrôle de fin d'opération, à rafraîchir si nécessaire. Fermeture PR ne signifie jamais code intégré ni tâche réalisée. Ne pas rouvrir ni fusionner en masse pour cette certification.
- 12 correspondances profil/worktree vérifiées et enregistrées : eb12e2dbd9137a67d6d86697e543ad4f86f10053.
- Mémoire locale et index actualisés : 059ff5c44d2bb9fd555cb3aedd1edfa7763e539e.

Les worktrees des Doctors peuvent être plus anciens que main. Mesurer leurs écarts et leur état sale; ne pas reset/clean, changer de branche ou fusionner par-dessus un agent actif. La configuration d'un profil ne met pas à jour son checkout.

## 6. Protocole de certification à exécuter

A. Observer : inventaire DC disponible, worktrees/terminaux Orca, profils Hermes, sessions actives et claims WorkGraph. Utiliser l'aide locale des CLI avant d'inventer des paramètres. Les PID/handles de l'ancienne session ne sont pas des identifiants durables. Distinguer « disponible », « actif observé », « bloqué » et « terminé avec preuve ».

B. Aligner les mandats : lire les SOUL et règles des profils effectifs; sauvegarder puis corriger les instructions contradictoires avec la constitution et le mandat S2 ci-dessus. Préserver l'historique. Relier explicitement profil, identité, dossier, conversation et work_id. Vérifier les restrictions réelles des outils; un cwd n'est pas un contrôle d'accès.

C. Sélectionner un PRD réel, borné et pertinent par Core dans le backlog actuel. Réutiliser l'item existant et identifier les doublons avant de créer de nouvelles tâches. Si aucun PRD n'est exploitable, créer une tâche de certification clairement étiquetée, sans simuler une valeur métier livrée. Commencer par un Core pilote; étendre après preuve, sans démarrer douze agents à vide.

D. Faire agir le Doctor : lui fournir le mandat et les critères; observer sa décomposition et sa délégation effective à un Compagnon. Le Doctor garde la supervision; la session Chat ne construit pas à sa place pour ensuite lui attribuer le mérite. Le Compagnon reçoit un contexte borné et produit un résultat dans son propre worktree.

E. Tracer le cycle : work_id → claim/lease → prédiction préalable lorsque requise → session réellement active → artifact + hash/commit → contrôle ciblé → revue par un autre agent → gate → scoring/clôture → libération du claim et binding. Enregistrer aussi les erreurs et corrections, pas seulement les succès.

F. Vérifier une reprise non destructive : reconnecter à la même conversation après interruption contrôlée d'un pilote approprié; confirmer identité, contexte utile et absence de double exécution. Ne pas tuer un agent occupé pour satisfaire artificiellement un scénario de test.

G. Valider Bot Mode réellement : bons noms, profil et conversation dans le roster; cwd effectif observé par l'agent; message de délégation effectivement reçu et traité; progression reflétant le vrai worker. Si seule la CLI est validée, certifier « CLI seulement » et laisser la partie Bot Mode non certifiée.

## 7. Critères d'acceptation et livrable final

| Critère | Preuve exigée |
|---|---|
| Mandat S2 compris et appliqué | Un Doctor décompose, délègue et supervise un PRD réel, avec traces |
| Séparation des 12 identités | Profil, worktree, conversation et branche vérifiés pour chaque rôle; état actif honnête |
| Exécution S3 | Résultat borné produit par le Compagnon désigné dans son espace |
| Trois Cores exercés | Un cycle complet accepté par Core, ou verdict partiel nommant précisément le Core bloqué |
| Indépendance de revue | Relecteur différent du producteur, verdict et hash de l'artefact relu |
| Reprise | Conversation persistante retrouvée, aucun doublon d'exécution sur le pilote |
| WorkGraph fidèle | Aucun In Progress sans exécution observée; claims/bindings terminaux libérés |
| Sobriété | Sessions existantes réutilisées et limites Watchdog respectées |

Écrire un certificat horodaté dans `10_Tech_OS/reports/` avec verdict PASS/PARTIAL/FAIL par Core et pour Bot Mode/CLI, identifiants, chemins de preuves, hashes, contrôles et limites. Ne donner PASS global que si tous les critères sont prouvés. Faire une revue indépendante du certificat, actualiser mémoire/index et committer/pousser uniquement les changements de cette intervention. Ne jamais élever « configuration 12/12 » en « orchestration 12/12 ».

## 8. Contraintes et problèmes distincts

- uc.db de production est canonique; utiliser les API/CLI prévues et aucune mutation destructive de schéma.
- Pas de git reset --hard, clean, stash global ni inclusion du travail sale d'autres agents. Les sous-repos ont leur propre historique; ne pas publier une arborescence parent par accident.
- Le serveur de validation API temporaire a été arrêté. L'interface complète Agent OS reste bloquée par une erreur d'optimiseur Vite lisant imports. Traiter séparément si elle empêche la certification; l'API isolée a déjà été testée.
- Les profils historiques peuvent avoir des instructions obsolètes : les lire avant d'envoyer un mandat autonome. Les noms de profils ne certifient ni les permissions ni le modèle réellement utilisé.
- Respecter les limites du Watchdog : population bornée, pas seulement cadence ralentie. Aucun arrêt fondé sur un journal silencieux.
- Ne pas lancer de nouveaux achats, publications externes ou communications humaines au titre de ce handover. La délégation technique aux agents et la certification demandée sont autorisées par A0.

## 9. Première action concrète

Lire le registre des bindings puis relever les sessions actives. Identifier le Doctor pilote disponible, son profil effectif et un PRD borné. Corriger les seules incohérences bloquantes, exécuter son cycle délégué et capturer la preuve avant de passer aux deux autres Cores.
