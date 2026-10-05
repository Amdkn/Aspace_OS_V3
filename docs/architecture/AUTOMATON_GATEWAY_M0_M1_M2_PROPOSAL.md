# Automaton dans l'Universal Constructor via A'Space Gateway

Statut : PROPOSED — aucun adapter, déploiement ou PASS runtime livré par cette documentation.
Return-to : [Gateway G2 #545](https://github.com/Amdkn/Aspace_OS_V3/issues/545), puis [canary souverain G3 #546](https://github.com/Amdkn/Aspace_OS_V3/issues/546).
Contexte : [synthèse de session](../governance/SESSION_2026_10_05_AUDIT_TO_AUTOMATON.md).

## Source examinée et choix d'intégration

[Conway-Research/automaton](https://github.com/Conway-Research/automaton/tree/d8f816881fd24b6f5e3d616e59edec387a447667), snapshot `d8f816881fd24b6f5e3d616e59edec387a447667`. Le README annonce MIT et une poursuite du développement dans un environnement RL interne ; le dépôt public ne prouve pas l'état du produit privé.

Intégrer d'abord des organes M1 et des actions M2 derrière un adapter. Conserver l'option d'un runtime complet M0 borné. Le constructeur A'Space demeure responsable de la composition, certification, promotion et réutilisation ; Automaton fournit une implémentation candidate de certaines capacités.

## Correspondance des échelles

M0/M1/M2 désignent ici la projection relative dans l'Universal Constructor. Ne pas les confondre avec des jalons homonymes de l'AMF.

| Projection | Élément Automaton | Usage dans A'Space | Preuve attendue |
|---|---|---|---|
| M0 — organisme | Runtime complet avec boucle, mémoire, budget et outils | Une incarnation hébergée, bornée par HostPolicy, reliée au Gateway | Identité stable, arrêt propre, reprise sans double effet |
| M1 — organes | Harness, routage d'inférence, mémoire, loop detector, heartbeat sous lease, lineage, self-modification | Adapters Capability Fabric, observabilité et organes composables | Contrat d'entrée/sortie, budget, annulation et politique testés par organe |
| M2 — actions | Exécuter une commande, écrire un fichier, produire un patch, observer, émettre une preuve | Primitives typées, cible explicite, opération/effect_id et reçu durable | Déduplication, fencing, permissions, résultat vérifiable |

Conserver `intrinsic_scale`, `projected_into`, `projected_scale` et `relation_type`. Relations possibles : EXTENDS, COMPOSES_WITH, ACCELERATES, SECURES, RENDERS, OBSERVES, CONTROLS, EMBODIES, VALIDATES. Une projection ne remplace pas l'identité de l'objet.

## Répartition des responsabilités

| Composant | Responsabilité |
|---|---|
| Universal Constructor / Capability Fabric | Décrire, composer, enregistrer et certifier les capacités |
| Gateway | Présence, session, connexion et transport d'enveloppes |
| Nardole | Dispatch, backpressure, retour vers la cellule |
| HostPolicy | Autorité, budget, leases, fencing et limites d'effets |
| Adapter Automaton proposé | Traduire le contrat A'Space vers le harness/runtime, normaliser les reçus |
| AMF et fabrics de domaine | Exécuter les effets autorisés dans leur domaine |
| Graham / Donna | Provenance temporelle ; ambiguïté, reprise et réconciliation |

Le Gateway ne devient ni scheduler, ni registre des capacités, ni mémoire universelle. Aucune seconde file de missions ne doit être créée par le heartbeat Automaton.

## Contrats à réutiliser

- #333 Capability Fabric ; implémentation à examiner dans `80_Agent-OS/capability_fabric` : `capability.py`, `registry.py`, `harness_adapters.py`, `cognitive_treasury.py`, `quarantine.py`.
- #471 InterFabricEnvelope.v1, #448 Temporal Truth, #318 identité/incarnation, #484 Reflex, #485 RecoveryPort.
- [Gateway v0](../governance/ASPACE_GATEWAY_NATIVE_GITHUB_V0.md).
- #560 ExecutionPacket et [provider model v2](../governance/JULES_PROVIDER_OPERATING_MODEL_V2.md), sans durcir le choix du fournisseur dans l'issue.

L'enveloppe transporte les coordonnées existantes : institutional_holon, embodiment, runtime, device/node, surface, session/lineage, mission/work/cell/correlation, capability/version, authority/policy/fencing, resource/budget lease, operation/effect identity, evidence/provenance et return_to. Les noms sérialisés définitifs viennent des contrats existants, pas de cette liste abrégée.

Un ExecutionPacket doit fixer notamment le dépôt, l'issue, le base_sha, allowed_paths, acceptance, effets autorisés, autorité S3, mode fournisseur, clé de déduplication, retry, lease et deadline. Un modèle ou compte disponible n'est pas une autorisation.

## Ce que montre le code amont

| Observation au snapshot | Implication pour l'adapter proposé |
|---|---|
| AgentHarness expose initialize(TaskNode, HarnessContext), execute, getToolDefs et construction de prompts | Point d'adaptation possible ; ce n'est pas une API distante native démontrée |
| HarnessContext porte identité, config, DB, client Conway, inference, budget, signal d'annulation, et champs de politique facultatifs | Traduction explicite des coordonnées et permissions ; présence d'un champ ≠ enforcement de toutes les actions |
| BaseHarness peut appeler directement tool.execute après LoopDetector | Encapsuler les outils avec contrôle d'effets et confinement de l'hôte |
| CodingHarness peut retomber d'une exécution distante vers localExec ; écriture distante vers filesystem local | Interdire le changement implicite de cible ; un timeout ambigu devient UNKNOWN avant toute reprise |
| LocalWorkerPool exécute en processus et termine selon result.success ; identité parent réutilisée | Séparer identité institutionnelle, incarnation et worker ; succès déclaré ≠ acceptation indépendante |
| PolicyEngine a des chemins permissifs par défaut et la journalisation peut absorber une erreur DB | Bornage explicite des outils ; reçu durable hors du seul verdict interne ; pas d'effet non traçable |
| Heartbeat dispose de leases et de retry | Réutiliser l'observation/lease sans concurrencer Nardole ou relancer une mission ambiguë |
| spawnChild provisionne sandbox/fonds/wallet et clone/build ; erreurs de propagation de constitution peuvent être interceptées | Reproduction par artefact versionné et politique validée, jamais héritage implicite de wallet/autorité |
| Self-modification dispose de protections de chemins et de traces Git | Mutation via PR, vérification exacte, promotion et rollback ; pas de réécriture live non certifiée |

Ces observations motivent les frontières de conception ; elles ne constituent pas un rapport d'exploitation de vulnérabilités.

Les valeurs budgétaires par défaut amont (dont limites de tours/coût/temps) ne deviennent pas les budgets A'Space. Une exhaustion suspend l'incarnation ou sollicite un routage autorisé ; elle n'efface pas le holon. Une wallet ne sert pas d'identité institutionnelle. SOUL peut alimenter une proposition de mémoire, pas réécrire directement la constitution.

## Surface de l'adapter — proposition, non API existante

Un sidecar TypeScript est une option pour limiter les changements au runtime amont et préserver les contrats Python A'Space. Le transport exact reste à choisir dans #545.

| Opération proposée | Sémantique |
|---|---|
| discover / observe | Capacités/version, santé, présence horodatée, limites connues |
| execute | Accepter un paquet validé et une cible explicite ; retourner une opération traçable |
| cancel | Demander un arrêt ; distinguer demandé, confirmé et effets déjà produits |
| checkpoint | Exporter une continuité versionnée sans secrets |
| reconcile | Résoudre l'état après timeout, perte de connexion ou arrêt |
| resume | Seulement si la reprise et la déduplication ont été certifiées ; aucune capacité upstream présumée |

État minimal : ACCEPTED → RUNNING → SUCCEEDED / FAILED / CANCELLED / UNKNOWN. SUCCEEDED ne vaut acceptation A'Space qu'après vérification indépendante du résultat et des reçus. Un lease expiré bloque tout nouvel effet ; un ancien writer ne récupère pas son autorité par reconnexion.

## Tranche initiale bornée

1. Choisir dans #545 une seule capacité de production de patch, un dépôt, une cellule, un commit de base et des chemins autorisés. Aucun financement, wallet, provisionnement, réplication ou self-modification live.
2. Enregistrer un adapter expérimental et faire passer l'ExecutionPacket par les contrats existants.
3. Produire un patch/PR et un reçu avec target, base/result SHA, operation/effect IDs, budget consommé et return_to.
4. Faire vérifier le commit exact par une vérification indépendante : résultat fonctionnel, chemins, politique et absence de mutation hors scope.
5. Prouver la réutilisation de la capacité dans une deuxième invocation explicitement autorisée. Cette seconde invocation n'est pas une relance automatique du canary Jules #562.
6. Pour #546, injecter coupure/reconnexion et migration de runtime en conservant identité, travail, autorité, filiation et effect_id ; constater zéro double effet.

Critères bloquants de cette tranche : refus d'un stale fencing token, rejet d'un effet non autorisé, budget épuisé sans nouvel effet, timeout ambigu classé UNKNOWN, pas de fallback distant→local, reçu durable et rapprochement après crash. Ces gates concernent cette intégration, pas l'ensemble du portefeuille Life/Business.

Rollback : désactiver l'adapter dans le registre expérimental et révoquer son lease ; conserver les preuves ; réconcilier les opérations en vol avant un nouveau fournisseur. Le détail du stockage des reçus, l'isolation effective, la propagation d'annulation et la reprise amont restent UNKNOWN jusqu'aux essais.

## Ordre de travail existant

#560 prépare le paquet fournisseur ; #561 réconcilie le stock historique ; #562 limite le canary Jules à une session après les préconditions. Le circuit breaker FAILED_PRECONDITION et l'absence de retry générique doivent être respectés. Aucun remplissage automatique de swarm.

L'Universal Constructor poursuit ses portages vers Projects 5/8 après #388/#512 ; ce document constitue une proposition rattachée à #545, pas un nouvel epic ni une preuve de construction autonome déjà réalisée.
