---
type: Learning
title: Continuité 10D et prévention de la réduction sémantique
description: Conserver le mandat, les capacités et leurs relations à la reprise ; corriger les contradictions du bootstrap qui rejouent la panne Multica.
tags: [continuite, multica, 10d, holons, constructeur-universel, memoire]
generated: { by: codex, at: 2026-10-05T13:16:56Z }
sources:
  - id: demande-fondateur
    resource: "ChatGPT, Solarpunk Kernel, 2026-10-05 : demande de mise à jour de la mémoire V3 contre la simplification destructive"
    last_modified: 2026-10-05
  - id: formulations-10d
    resource: "Source projet Texte collé.txt du 2026-09-27, libfile_3fb288efdd04819190a6021b1b82406e ; formulations utilisateur distinguées des réponses IA"
    last_modified: 2026-09-27
  - id: handover-v4
    resource: "HANDOVER-2026-10-02-A0-KIRBY-V4-TRANSITION-CUBEFARM-AGENT-LIFE-BUSINESS.md ; source projet libfile_c6d1c3979860819196953d74e53b3006"
    last_modified: 2026-10-02
  - id: multica
    resource: "40_Memory_Wiki_OKF/learning/multica-governor-module.md"
    last_modified: 2026-08-31
  - id: canon-v4
    resource: "AGENTS.md ; MEMORY.md ; 10_Tech_OS/00_Governance_Rick/ADR-RICK-FRACTAL-HOLON-V4-ANTI-RIGIDITY-2026-10-02.md ; snapshot ca181133b214661b415aaa9439c332fca80cac2e"
    last_modified: 2026-10-05
  - id: constructeur-generations
    resource: "docs/architecture/BOOTSTRAP_GENERATIONS_R0_R1.md ; issues #512/#514 ; docs/architecture/AUTOMATON_GATEWAY_M0_M1_M2_PROPOSAL.md"
    last_modified: 2026-10-05
  - id: factories
    resource: "13 textes du dossier projet Solarpunk Kernel lus : sources SSSF/IndyDevDan, Archon/Cole, Upstash, validation indépendante, Wargaming Fable et handovers. Ce sont des inspirations, pas des preuves de déploiement A'Space."
    last_modified: 2026-10-05
okf_version: "0.2"
---

> Niveau de confiance : non ratifié pour cette nouvelle synthèse. Les directives utilisateur et règles existantes sont des sources ; les constats de fichiers sont bornés au snapshot indiqué. Aucun fonctionnement runtime n'est certifié ici.

## Cause de la rechute et correction

Le corpus Multica avait déjà identifié la perte du mandat à la compression, les mauvais points d'entrée et le coût de charger trop de contexte. Une nouvelle fiche seule ne corrige pas le problème : les routeurs effectivement lus doivent la rendre accessible et cesser de donner des règles contraires.

Constats du snapshot : `50_Distillation/AGENTS.md` interdisait même la lecture brute, contrairement au routeur racine ; `forge_chain` décrivait une cascade ; `MEMORY.md` présentait un instantané de septembre comme état courant ; la baseline `architecture/kirby_a0_orca_ade_meta_harness_ipbd_factory.md` était référencée mais absente de l'arbre main complet. Absence sur main ne prouve pas absence sur le poste ou dans l'histoire Git. Ne pas inventer ce fichier historique.

## Architecture de mémoire à conserver

| Plan | Fonction et limite |
|---|---|
| `MEMORY.md` + `AGENTS.md` | Bootstrap court, mandat et routage ; pas une seconde mémoire universelle |
| `40_Memory_Wiki_OKF/` | Décisions, raisons, pièges, provenance, confiance ; indexer chaque ajout |
| `50_Distillation/` | Promotion de connaissances vers OKF/ontologie, après analyse ; pas un préalable à toute action |
| `70_Onthologies/` | Sémantique formelle ; ne remplace ni le réel observé ni l'intention |
| `90-self-evolution/` | Apprentissage des incidents et règles de non-régression ; pas de certification par simple existence d'un fichier |
| `_INBOX/handoffs/` | Curseur opérationnel : mandat, travail en cours, preuves, prochaine action, limites d'accès |
| `ASPACE_ACTIVE_INTENTS.yaml` | Projection versionnée du mandat ; IPBD partagés dans Supabase `aspace` |
| WorkGraph / uc.db / Supabase | Continuité du travail, événements, claims, bindings, receipts et reprise ; ni identité entière ni mémoire universelle |
| Registry / GitHub / Linear / GWS | Respectivement coordonnées, artefacts/histoire, gouvernance humaine, opérations de domaine ; autorité par type et fraîcheur |

La compilation de contexte réunit constitution, identité/version, juridiction, mémoire pertinente, voisinage WorkGraph, sources de domaine, état du repo, receipts, pairs, contraintes et `return_to`. Elle conserve les références vers les détails sans recharger tout le corpus. Graham porte cette continuité/replay ; Yaz observe trajectoires, dérives, coûts et fraîcheur ; leur cognition ne se réduit pas au stockage ou à la télémétrie.

## Invariants de fidélité à l'intention

- A'Space articule L0 Bedrock, L1 Life OS et L2 Business OS. Business OS est imbriqué dans LD01 Career & Business de Life OS. Les trois Cores techniques ne remplacent pas cette structure.
- Les six frameworks restent articulés : Ikigai (4 piliers et 5 horizons), Wheel (8 domaines), 12WY (Vision, Planning, Process Control, Measurement, Time Use), PARA (4 composantes), GTD (5 étapes), DEAL (4 composantes). La 10D exprime cette architecture imbriquée ; ne pas la remplacer par une pyramide logicielle à sept niveaux.
- Drive porte le filesystem de Life OS ; Calendar/Agenda, Tasks/Keep, Docs, Sheets, Slides, Script et Opal peuvent matérialiser les fonctions de domaine. Git et les vaults portent les artefacts techniques. Une surface n'est pas un « terminal passif » par définition.
- Prototypes reproductibles de franchises dans Projects, standards dans Areas ; la valeur Life/Business reste la finalité. L'ambition de long terme et la production à court terme doivent coexister.
- Holons cognitivement complets à juridiction bornée ; responsabilités principales non exclusives ; subsidiarité élastique avec restitution ; poly-incarnation ; fencing par effet/ressource, pas un processus unique par identité.
- Distinguer Amadou humain et A0 projection numérique. L'autonomie réduit les interventions requises ; elle n'interdit pas l'intervention du Fondateur.
- Séparer états institutionnel, incarnation, runtime, charge, autorité, ressources et continuité. ONLINE, PR mergée et test vert ne prouvent pas l'effet externe.

## Solutions à conserver lors des intégrations

| Capacité ou inspiration | Intention conservée / preuve à rechercher |
|---|---|
| Constructeur Universel M0/M1/M2 | Organisme, organes, primitives à échelles relatives ; conserver échelle intrinsèque, projection et relations de composition. Ce ne sont pas trois petits jalons séquentiels. |
| Automaton | Préserver l'organisme complet M0 et ses possibilités de composition M1/M2, mémoire, boucle, filiation, reproduction et évolution. Le canary de patch dans la proposition existante est une preuve partielle, pas la définition complète de l'intégration ni un abandon du reste. Les effets restent sous autorité explicite. |
| R0 → R1 | Le système bootstrap construit son successeur ; promotion par preuve, continuité d'identité, coexistence sans conflit, retour arrière ; R0 peut devenir référence, observation, provenance ou recovery. |
| Paperclip | Préserver la demande d'intégration organisationnelle. Ne pas confondre le produit de coordination et la métaphore du paperclip maximizer. La configuration précise à adopter reste à établir depuis la source utilisateur/upstream ; aucune adoption n'est déclarée ici. |
| Prime Agent + DeepSeek Harness | Intention utilisateur : récursivité, interconnexion et coévolution du harness. Ce ne sont pas seulement deux fournisseurs interchangeables ; la skill `/prime` d'un tutoriel n'est pas Prime Agent. Intégration runtime non vérifiée dans cette mise à jour. |
| OpenClaw / Hermes / Gateway | Continuité de session, présence, transport et reprise composables ; Gateway ne remplace ni les capacités ni la mémoire ni les décisions des holons. L'identité traverse les runtimes. |
| OpenShell / Octop | Préserver la piste Secure Agent Society et les frontières d'exécution ; une contrainte de sécurité sur un effet ne réduit pas la cognition ou le programme entier. Statut opérationnel à vérifier. |
| Ryan / CubeFarm / SSSF / Archon | Instruments de construction réutilisables et factories capables de construire des factories : contexte, code, validations déterministes pertinentes, revue indépendante, livraison utilisable, reprise et travail suivant admissible. Ni organigramme figé ni simple générateur de PR. |
| Refill / continuation | Événements et heartbeat réveillent le holon avec contexte ; il peut poursuivre, scinder, fusionner, rechercher, construire, rerouter, suspendre ou conclure. Le circuit breaker d'un fournisseur reste applicable ; il ne devient pas un arrêt universel. |
| Yaz / Graham / Physiology | Observation comportementale, provenance temporelle, contradictions, UNKNOWN, replay et contexte compilé ; Physiology est une projection dérivée. Pas de nouvelle SSOT ou de cerveau scheduler central. |
| Jev / LiDAR / System One + Two | Réflexes typés avec confiance et escalade ; contexte/trajectoires normalisés ; autorité déterministe de l'hôte, cognition et arbitrage du holon. |
| Wargame / validation indépendante | Action, réaction, contre-action, signal attendu, signal d'échec, déclencheur de branche et recovery ; vérifier l'effet avec des scénarios indépendants du raisonnement de construction. |

Les sources vidéo sont des inspirations. Leurs affirmations commerciales, scores et promesses de sécurité ne deviennent pas des faits A'Space. Les seuils et frontières d'une démonstration ne deviennent pas automatiquement ceux du projet.

## Mandat de reprise et prévention de la réduction

1. Reprendre la dernière intention explicite et son autorisation dans les capacités réellement accessibles ; un résumé ne révoque pas ce mandat. Les permissions et limites d'effets applicables restent respectées.
2. Lire le bootstrap et cette fiche, puis seulement les sources utiles au travail actif. Ne pas relancer un audit global si un curseur et ses preuves existent.
3. Conserver l'objectif entier, ses relations et les capacités attendues. Pour chaque livraison partielle, distinguer livré / restant / bloqué / abandonné par décision explicite. Ni silence, ni fenêtre de contexte, ni canary ne vaut abandon.
4. Avant une modification architecturale, comparer les capacités et relations avant/après. Une suppression doit être explicite, justifiée et autorisée. Cette comparaison sert la tâche ; elle ne crée pas un nouveau péage documentaire.
5. Distinguer formulation utilisateur, décision adoptée, proposition IA, observation et hypothèse. Une ancienne réponse d'assistant n'est pas automatiquement du canon.
6. Poursuivre jusqu'au résultat vérifiable ou à une limite réelle. À la reprise : objectif, mandat, références de travail, dernier résultat, prochaine action, blocage réel, `return_to` et dette de restitution suffisent ; ne pas redemander les fondamentaux.
7. Mesurer la réussite par comportement et effet : charge de rappel supprimée, continuité après interruption, résultat utilisable, absence de double effet ; jamais par nombre de fiches ou de PR.

## Limite de cette livraison

Cette correction porte sur les fichiers versionnés de mémoire/reprise, avec application sur le checkout local par Desktop Commander. Elle ne synchronise pas à elle seule Soul.db, Engram, Supabase, les autres worktrees actifs ni les sessions déjà ouvertes. Ne pas annoncer ces synchronisations sans leur preuve. Ne pas écraser un poste divergent : comparer et préserver les modifications locales avant réconciliation.
