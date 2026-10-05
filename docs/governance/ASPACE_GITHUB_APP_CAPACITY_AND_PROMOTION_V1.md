# GitHub Apps — capacités permanentes et promotions organisées

Date : 2026-10-05
Statut : matrice proposée pour finalisation humaine ; NON APPLIQUÉE aux Apps.
Succède au profil initial de canary pour la conception ; ne prétend pas décrire les permissions installées.
Sources : authority_profiles.json ; scripts/github_app_system1.py ; guide v0 ; captures V3/V4 fournies par le Fondateur.
Parent : #555. Aucune nouvelle App requise par cette proposition.

## 1. Décision de conception proposée

Le rang S1/S2/S3 n'est pas une restriction cognitive. La permission est attribuée à une responsabilité et un effet sur une ressource. Les cinq Apps sont des identités techniques d'autorité ; elles ne remplacent pas les holons.

Séparer quatre éléments :
- plafond de permissions déclaré par l'App ;
- plafond effectivement accepté par chaque installation et ses dépôts ;
- habilitation institutionnelle permanente ou temporaire décidée dans A'Space ;
- jeton d'exécution limité aux permissions/dépôts requis et à sa durée native.

Le moindre privilège doit permettre de terminer le mandat. Un manque de droit produit une demande de capacité précise et une route de résolution, pas un abandon ou une réduction silencieuse de mission.

Les captures prouvent que les cinq Apps apparaissent dans les installations V3 et V4. Elles ne montrent ni les permissions acceptées ni les règles de branche ni une exécution réussie.

## 2. Matrice cible — plafonds des Apps, pas jetons par défaut

L = lecture ; E = lecture/écriture ; P = promotion organisée, non accordée par défaut.
Les colonnes portent sur les cinq Apps existantes. Cette matrice est une proposition précise, pas une autorisation d'appliquer des élargissements.

| Permission repository | Gateway | A0 | S1 | S2 | S3 |
|---|---|---|---|---|---|
| Metadata | L | L | L | L | L |
| Contents | L | E | E | E | E |
| Issues | L | E | E | E | E |
| Pull requests | L | E | E | E | E |
| Discussions | L | E | E | E | E |
| Actions | L | E | E | E | E |
| Checks | L | L | E | L | E |
| Commit statuses | L | L | E | L | E |
| Workflows | aucun | P | E | E | E |
| Deployments | L | P | E | E | E |
| Variables | aucun | P | P | E | E |
| Administration | aucun | P | P | P | P |
| Secrets | aucun | P | P | P | P |
| Webhooks de dépôt | aucun | P | P | P | P |
| Projects | route dédiée | route dédiée | route dédiée | route dédiée | route dédiée |

Raisons :
- Contents E pour A0/S2 permet la subsidiarité sans imposer un retour au Fondateur à chaque correction.
- Discussions E pour S1/S3 permet recherche, proposition, coordination et restitution.
- Actions E pour les holons opérationnels permet leurs interventions CI autorisées ; ce droit a plusieurs effets, à filtrer par endpoint.
- Workflows E pour S1/S2/S3 permet de construire et réparer les factories. Ce droit exige une attention aux secrets et au code exécuté par CI ; aucune exception aux protections de branche n'est incluse.
- Checks/statuses E de S3 permet de publier ses mesures. Une mesure de construction n'est jamais une certification indépendante S1.
- Variables E pour S2/S3 vise la configuration opérationnelle non secrète. Les règles d'accès aux environnements restent applicables.
- Gateway reste une surface de réception/lecture. L'exécution sortante utilise l'App autorisée de la mission ; ce choix ne réduit pas les capacités du Gateway comme transport.
- P n'est pas une interdiction. Une mission d'administration, de secrets ou de gestion des webhooks peut être confiée à tout holon compétent avec habilitation appropriée, temporaire ou durable.

Packages, Pages, Codespaces, dépendances et alertes de sécurité suivent des profils de capacités distincts selon les endpoints réellement utilisés. Ne pas cocher ces catégories par analogie ; ne pas déclarer non supportée une capacité avant examen de son API.

Projects doit distinguer projets personnels, organisationnels et anciens projets de dépôt. repository_projects ne vaut pas autorité sur tous les Projects V2. Le chemin utilisateur autorisé et le chemin installation doivent être vérifiés séparément.

## 3. Promotions temporaires

Si le droit est déjà accepté dans l'installation :
1. Retrouver le mandat et l'habilitation existante.
2. Identifier holon, incarnation, mission, dépôts, opérations et permissions nécessaires.
3. Émettre un jeton limité avec repositories/repository_ids et permissions explicites ; aucun fallback au périmètre intégral par omission.
4. Associer une échéance de mission, une raison, une autorité de décision et une preuve de restitution.
5. À expiration/annulation : empêcher tout nouveau jeton ou effet, révoquer le jeton lorsque nécessaire et rapprocher les opérations en vol.

Les jetons d'installation ont une expiration native d'environ une heure ; un bail interne de 15 minutes n'abrège pas magiquement la validité d'un jeton déjà livré. Une limite plus courte exige une révocation ou un exécuteur médiateur effectif. Les agents ne reçoivent pas les clés privées des Apps.

Si le droit dépasse les permissions acceptées : préparer le diff de l'App, le faire approuver, faire accepter la mise à jour d'installation, puis vérifier les droits obtenus. Un changement de rôle ou un --approve local ne crée pas ce droit GitHub.

## 4. Promotions permanentes

Une responsabilité durable justifie une habilitation durable révisable. Documenter capacité, bénéficiaire, périmètre de dépôts, opérations, justification et autorité de décision. Mettre à jour le profil versionné et les installations concernées après approbation. « Permanent » qualifie l'habilitation, jamais la durée d'un jeton.

Ne pas solliciter à nouveau une autorisation qui couvre déjà l'opération exacte ; ne pas étendre une autorisation existante à un nouveau dépôt ou effet par supposition.

La même App applique son plafond par installation, pas un profil d'enregistrement différent pour chaque dépôt. Des jetons limités et une politique d'exécution distinguent V3, V4 et les autres dépôts. Les restrictions de branches/fichiers/opérations ne sont pas fournies par le simple paramètre permissions du jeton.

## 5. Indépendance et provenance

Les identités GitHub App sont partagées par plusieurs holons : un commentaire signé S3 ne suffit pas à identifier Ryan ou Yaz. Les receipts doivent conserver holon, incarnation, mission, App, installation, opération, dépôt, commit et résultat.

Le constructeur ne se certifie pas lui-même par un check vert. Les contrôles exigés doivent être associés à la source indépendante attendue lorsque GitHub le permet. La politique locale seule ne restreint pas un jeton direct : protections GitHub et/ou médiation d'exécution doivent réellement appliquer les limites.

Le service qui détient les clés privées peut émettre des jetons plus puissants : c'est une frontière d'autorité à contrôler. Aucun partage des clés avec tous les harnesses.

## 6. Modifications à effectuer dans le système existant

Constats :
- S2 Contents read contredit la subsidiarité élastique.
- S3 Discussions read empêche une contribution complète.
- Actions read bloque les interventions CI qui nécessitent write.
- validate() interdit workflows, variables et autres clés sans chemin d'exception implémenté.
- Le catalogue de quatorze permissions n'est pas le catalogue GitHub complet.
- A0 est décrit comme human/user boundary alors que Fondateur humain et A0 numérique sont distincts.

Travail requis avant activation :
- Ajouter au compilateur les permissions/endpoints nécessaires, les profils de promotion et des validations par permission.
- Conserver le refus d'élargissement non approuvé ; une exception approuvée doit être représentable et vérifiable.
- Lire la configuration effective de chaque App ET les permissions acceptées de chaque installation.
- Comparer à cette cible, obtenir l'approbation du diff exact, puis appliquer et relire.
- Vérifier la portée des jetons, la révocation/reprise et la séparation des preuves.
- Mettre à jour la mémoire avec les résultats observés.

La présente livraison finalise une proposition de répartition ; elle n'installe pas le service de promotion et ne modifie pas les permissions live.

## Références GitHub officielles vérifiées

- https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app
- https://docs.github.com/en/apps/maintaining-github-apps/modifying-a-github-app-registration
- https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app
