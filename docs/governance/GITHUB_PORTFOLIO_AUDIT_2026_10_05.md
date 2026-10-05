# Audit GitHub du portefeuille — 5 octobre 2026

Statut : photographie de lecture, pas audit de sécurité exhaustif.
Périmètre : compte connecté Amdkn ; inventaire paginé terminé à 44 dépôts. Aucun organisme renvoyé par la liste d'organisations. `omk-services` apparaît comme compte utilisateur ; son dépôt OMK-DESKTOP-WEB-OS a été examiné séparément.
Retour : [synthèse de session](SESSION_2026_10_05_AUDIT_TO_AUTOMATON.md).

## Inventaire

44 dépôts Amdkn : 29 non archivés, 15 archivés ; 35 publics, 9 privés. Somme des tailles API : 1 936 131 KiB, dont 1 683 737 pour V3 (~87 %). Cette métrique API ne mesure pas la taille d'un checkout ni la qualité d'un projet.

| État | Dépôt | Visibilité |
|---|---|---|
| Actif | Life-OS-2026 | public |
| Actif | 00-Solaris | public |
| Actif | 00-AaaS-Agency-Garden | public |
| Actif | 01-OMK-Service-Landing-Page | public |
| Actif | 01-OMK-Business-OS | public |
| Actif | 02-ABC-OS | public |
| Actif | 03-RILCOT-Members-OS | public |
| Actif | 03-RILCOT-Community-OS | public |
| Actif | 04-Alikaly-Bana-Holding | public |
| Actif | 04-Alikaly-Bana-OS | public |
| Actif | 05-Marina-Landing-Page | public |
| Actif | 05-Marina-BOS | public |
| Actif | alykaly-os-V2 | privé |
| Actif | 02-ABC-FrontEnd | public |
| Actif | 00-omk-nexus-landing-en | public |
| Actif | Aspace_OS_V3 | public |
| Actif | 00-omk-saas-os | public |
| Actif | The-Office-OS-Site | privé |
| Actif | The-OMK-Mobile-Back-Office | public |
| Actif | BusinessOS | public |
| Actif | The-OMK-Office1.0-JaaS | public |
| Actif | JaaS-V1-Mobile-OS | privé |
| Actif | The-OMK-Office-V1-JaaS-Landing-Site-Web | privé |
| Actif | Agent-OS | public |
| Actif | Agent-OS-Desktop | public |
| Actif | Business-Office-3-OS | public |
| Actif | Aspace_OS-V4 | privé |
| Actif | cubefarm | public |
| Actif | codex-chatgpt-web | public |
| Archivé | mspace-v1-offline | privé |
| Archivé | A-Space-OS-V0-Core-Client | privé |
| Archivé | KBS-CORE | public |
| Archivé | aspace_a0_amadeus_cockpit_v0 | public |
| Archivé | Amdkn-aspace-cockpit-vps | privé |
| Archivé | aspace_amiral | public |
| Archivé | aspace-v0.7-ui-core | public |
| Archivé | aspace-ui-core | privé |
| Archivé | business-pulse | public |
| Archivé | Kalibana | public |
| Archivé | a_space_os | public |
| Archivé | aspace_a0_amadeus | public |
| Archivé | RILCOT-OS | public |
| Archivé | RILCOT-OS-V0 | public |
| Archivé | Agency-as-a-Service | public |

« Actif » signifie uniquement non archivé. Hors total : `omk-services/OMK-DESKTOP-WEB-OS`, public, droit push observé, admin faux.

## Constats et suites proposées

| Priorité | Observation | Conséquence / prochaine preuve |
|---|---|---|
| P1 | README BusinessOS : Astra=V3, Sol=AgentOS, Terra=Life, Luna=Business ; registre des worlds : Sol=V3, Tera=AgentOS, Luna=Life | Réconcilier avec le propriétaire du registre ; aucune nouvelle correspondance décrétée ici |
| P1 | Agent-OS renvoie 409 « Git Repository is empty » sur les commits | Vérifier la cible canonique et la reprise de publication ; le registre évoque un ancien blocage secret scanning, sans prouver une fuite actuelle |
| P1 | Trois familles de PR Life convergent sur les mêmes issues ; deux autres paires Mobile/Business-Office | Retour vers #561 ; comparer les patches et choisir une disposition avant merge |
| P2 | Agent-OS-Desktop : branche réelle main, snapshot de registre mentionnant snapshot/tera-5555-2026-09-27 | Dater/corriger la projection du registre ; aucun README racine trouvé |
| P2 | BusinessOS et Business-Office-3-OS contiennent ci.yml, mais API Actions total_count=0 | Vérifier déclencheurs et première exécution ; cela ne prouve pas une désactivation |
| P2 | Taille API de V3 très dominante | Mesurer historique/objets lourds avant toute opération de réduction |
| P2 | Aspace_OS-V4 : taille API 0 mais README présent (« Aspace_OS-V4 », « Stark Jarvis Industry 🏭 ») | Ne pas classifier vide sur la seule taille API |

## PR concurrentes observées

Life-OS-2026 : 9 PR ouvertes, #111 à #119.
- Issue #93 : PR #112, #115, #116 ; recouvrement sur `agents.store.ts` et `src/types/capabilities.ts`, avec répertoires d'adapters River différents.
- Issue #109 : PR #113, #114, #119.
- Issue #105 : PR #111, #117.
- The-OMK-Mobile-Back-Office : PR #30/#31 pour issue #29.
- Business-Office-3-OS : PR #3/#4 pour issue #2.

Ce sont les 13 drafts de la réconciliation [V3 #561](https://github.com/Amdkn/Aspace_OS_V3/issues/561). Dispositions prévues : ABSORBED_IN_MAIN, STILL_VALID_REVIEW, PARTIAL_PATCH_EXTRACT, SUPERSEDED, DUPLICATE, OBSOLETE, UNKNOWN_NEEDS_OWNER. Aucune clôture en masse, relance fournisseur ou fusion n'a été effectuée dans cet audit.

## Preuves CI et limites

- [V3 OKF](https://github.com/Amdkn/Aspace_OS_V3/actions/runs/37294161956), main, 5 octobre 10:04:15 UTC : succès observé.
- [Agent OS CI](https://github.com/Amdkn/Agent-OS-Desktop/actions/runs/36826520072), main, 1 octobre 06:45:50 UTC : succès observé.
- [Life Terra State CI](https://github.com/Amdkn/Life-OS-2026/actions/runs/37209301250), branche PR #115, 4 octobre 14:27:03 UTC : succès observé ; aucune inférence sur main/production.
- Les trois derniers runs consultés de chacun étaient en succès ; échantillon limité.
- V3 rulesets renvoyait une liste vide. Les protections de branche n'ont pas été vérifiées : aucune conclusion globale sur la protection.
- La recherche des PR ouvertes a retourné 22 résultats ; ce nombre n'est pas une garantie d'exhaustivité du portefeuille.

Pas de validation des applications en exécution, de déploiements, de postes locaux ni de secrets. Les constats sont datés, les corrections restent à réaliser. Les liens d'API et les fichiers du dépôt peuvent évoluer : refaire les lectures avant mutation.
