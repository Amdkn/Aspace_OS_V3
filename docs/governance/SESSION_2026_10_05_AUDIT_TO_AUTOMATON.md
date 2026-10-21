# Continuité du 5 octobre 2026 — audit GitHub → Automaton

Statut : synthèse de session proposée à revue. Aucune installation Automaton ni activation de fournisseur ne découle de ce document.
Base V3 examinée : `b5be578952beed6f25a526f2484bd318961ab1e9`.
Return-to : [Gateway #542](https://github.com/Amdkn/Aspace_OS_V3/issues/542), particulièrement [G2 #545](https://github.com/Amdkn/Aspace_OS_V3/issues/545).

## Parcours et documents

1. [Audit du portefeuille](GITHUB_PORTFOLIO_AUDIT_2026_10_05.md) : inventaire, incohérences, limites de preuve.
2. Présent document : décisions humaines, économie des surfaces et assimilation des sources.
3. [Automaton / Universal Constructor M0–M2](../architecture/AUTOMATON_GATEWAY_M0_M1_M2_PROPOSAL.md) : correspondance architecturale et tranche testable.
4. [Handover opérationnel](../../_INBOX/handoffs/HANDOVER-2026-10-05-AUDIT-GATEWAY-AUTOMATON.md) : reprise sans reconstruire toute la conversation.

Ces documents prolongent [Gateway v0](ASPACE_GATEWAY_NATIVE_GITHUB_V0.md) et [Jules provider model v2](JULES_PROVIDER_OPERATING_MODEL_V2.md). Ils ne créent pas un second registre, WorkGraph ou espace de mémoire certifiée.

## War Room 10D — atelier inter-dépôts

La continuité ne doit pas se réduire à `#545 → adapter → #546 → canary`. Cette séquence est une voie de preuve dans un **atelier de conception inter-dépôts** qui conserve l'objectif entier.

Avant un brainstorming majeur, charger une carte du portefeuille plutôt que relire intégralement chaque dépôt. Pour chaque dépôt/capacité, la carte doit porter au minimum :

- finalité Tech/Life/Business et bénéficiaires ;
- capacités présentes, proposées et réellement vérifiées ;
- relations `CONSUMES / COMPOSES_WITH / EMBODIES / EXTENDS / VALIDATES / OBSERVES / CONTROLS` et projections M0/M1/M2 ;
- interfaces, dépendances, travaux ouverts et possibilités de réutilisation ;
- provenance, fraîcheur et niveau de preuve.

Le Workspace Registry fournit les coordonnées ; Graham compile le contexte pertinent et la vérité temporelle ; Yaz renseigne observations/fraîcheur ; GitHub conserve sources, mutations et preuves ; Agent OS/CubeFarm peut rendre cette carte navigable sans devenir SSOT.

Les instruments de brainstorming sont composables, non exclusifs :

| Instrument | Contribution privilégiée |
|---|---|
| BMAD | développer l'intention, explorer plusieurs architectures, préserver les exigences complètes |
| Gstack | challenger valeur, hypothèses produit, bénéficiaires et leviers d'expansion |
| Superpowers | approfondir les choix techniques avec le contexte des dépôts concernés |
| GSD | transformer les décisions mûres en travail exécutable et faire remonter les résultats |
| CEO Bench | tester des stratégies dans la durée, comme banc d'essai et non doctrine de management |
| Wargame / MiroFish | explorer réactions, blocages, effets secondaires, reprise ; simulation ≠ preuve réelle |

Une séance doit produire : **carte des possibilités → architectures comparables → scénarios difficiles → décision exploitable**, en conservant explicitement les branches d'exploration non retenues.

Question d'amorçage canonique :

> **Comment composer les dépôts existants pour que le Constructeur Universel fabrique et fasse évoluer des organismes Life/Business, avec mémoire, observation et continuité — jusqu'à construire son successeur ?**

Automaton, Paperclip, Gateway, Prime Agent, DeepSeek Harness et Ryan Factory sont donc des objets à **composer et comparer**, pas une file séquentielle de tickets. Cette capacité War Room reste partiellement câblée : sources, inventaire et mécanismes existent ; leur consultation coordonnée et leur actualisation effective restent à construire.

## Qualification des informations

| Marqueur | Sens |
|---|---|
| OBSERVED | Source ou résultat d'API examiné à la date de l'audit |
| USER_DECISION | Choix exprimé par l'utilisateur dans la session |
| USER_REPORTED | Information fournie, sans vérification indépendante |
| PROPOSED | Design ou travail à valider, pas une capacité installée |
| UNKNOWN | Preuve insuffisante ; ne signifie ni succès ni échec |

Une issue fermée, un contrat écrit, un quota disponible ou une CI verte ne prouve pas une exécution en production.

## Répartition souhaitée des surfaces

| Surface / outil | Choix utilisateur | Limite d'interprétation |
|---|---|---|
| Doc Astra dans Work | Visionnaire : stratégie, synthèse, architecture, arbitrage des inconnues | Une responsabilité privilégiée, pas une limite cognitive |
| Chat avec 5.6 Sol | Conduite opérationnelle avec Desktop Commander, plugin GitHub, GitHub App et primitives GitHub | Disponibilité effective de chaque outil à vérifier dans chaque session |
| Jules, Hermes, Claude Code et autres harnesses | Travail technique borné, mutations, vérification et retour de preuves | Le runtime et le modèle ne définissent pas l'identité institutionnelle |
| Autres comptes Jules | Quatre comptes annoncés disponibles lorsque le principal est à 100/100 | USER_REPORTED ; accès et quotas non vérifiés ; aucun dispatch ou roulement automatique autorisé par ce constat |

Ces rôles n'imposent aucun renommage des holons existants. Chaque niveau conserve sa cognition complète ; l'autorité se borne par opération, effet et ressource.

## Quotas et économie de l'attention

Le problème initial était un compteur semblant s'appliquer à Work/Codex mais pas à Chat avec 5.6 Sol. La capture examinée pendant la session indiquait un usage partagé Codex/Work/workspace agents/Excel, excluant les conversations Chat, avec 98 % restants et une réinitialisation annoncée dans 6 jours et 23 heures. C'est un constat ponctuel d'interface, pas une garantie générale sur les offres, modèles, outils ou plafonds actuels. La capture n'est pas embarquée dans Git.

Conséquences retenues :
- ne pas confondre quota Work/Codex, limite Chat, budget API et quota propre à un fournisseur ;
- vérifier capacité, autorité, état de santé et coût avant de choisir un runtime ;
- investir le raisonnement coûteux dans des contrats, tests réutilisables et expériences qui réduisent les inconnues ;
- mesurer les résultats Life/Business et l'attention humaine libérée ; le repère 20/30/50 Tech/Life/Business reste une aspiration, pas un ordonnanceur ;
- ne jamais remplir les quotas par création automatique de tâches.

## GitHub comme système de travail natif

| Primitive | Usage retenu |
|---|---|
| Discussions | Exploration, questions, RFC et alternatives |
| Wiki / docs | Doctrine durable et modes opératoires |
| Projects | Portefeuille, possibilités, séquencement |
| Milestones | Convergence bornée |
| Issues | Cellules exécutables ou blocages précis |
| PR | Mutation exacte et revue |
| Actions / Checks | Vérification déterministe et preuves |
| Releases | Promotion versionnée et référence de retour arrière |
| GitHub App / webhooks | Authentification, transport et événements ; aucune autorité institutionnelle implicite |

Une branche conversationnelle n'est pas une branche Git. Le Gateway fédère présence, sessions et transport ; les domaines gardent leurs vérités et leurs capacités.

## Solarpunk Kernel : provenance et couverture réelle

Source de session : dossier « Solarpunk Kernel ». Treize documents textuels inventoriés ; les images et conversations n'ont pas fait l'objet d'un examen exhaustif. Les sources originales ne sont pas copiées dans ce dépôt public.

| Source | Couverture | Usage |
|---|---|---|
| `Markdown collé.md` — 1 octobre | Lecture intégrale, 575 lignes | Récapitulatif de fondation ; snapshots historiques, pas état courant |
| `HANDOVER-2026-10-02-A0-KIRBY-V4-TRANSITION-CUBEFARM-AGENT-LIFE-BUSINESS.md` | Lecture intégrale | Invariants et continuité A0/Kirby/CubeFarm/Agent/Life/Business |
| `Texte collé(1).txt` — 5 octobre | Examiné | Transcription autour de Gemini/Argon ; allégations externes non vérifiées |
| `Texte collé(2).txt` — 5 octobre | Examiné | Transcription Higgsfield/« Xfield » ; résultats et méthode plutôt que marketing du modèle |
| `Texte collé.txt`, puis `Texte collé (2).txt` à `Texte collé (9).txt` — 1 octobre | Neuf transcriptions parcourues par extraits | Usines logicielles, harnesses, SDLC, sécurité déterministe, économie ; assimilation exhaustive non revendiquée |

Ces titres assurent la traçabilité dans le dossier d'origine ; ils ne constituent pas des liens publics vérifiables par un lecteur GitHub.

Invariants retenus :
- échelle relative et holons poly-incarnés ; humain A distinct de son incarnation numérique A0 ;
- identité ≠ harness ≠ modèle ; subsidiarité élastique ;
- stewardship et responsabilité n'emprisonnent pas la cognition ;
- capabilities sémantiques dans leurs domaines, Gateway comme membrane ;
- effets bornés, provenance temporelle, reprise explicite et réduction du babysitting ;
- auto-hébergement R0/R1 et reproduction exigent des preuves, pas seulement un récit.

Les anciennes suggestions de remplissage de swarm sont supersédées pour l'exécution par #560–#562 et le modèle fournisseur v2. Les benchmarks et promesses commerciales des transcriptions restent UNKNOWN tant qu'ils ne sont pas vérifiés.

## Continuité canonique

| Sujet | Ancrage existant | Suite |
|---|---|---|
| Gateway | #542 ; G0 #543, G1 #544, G2 #545, G3 #546 | Adapter Automaton via G2, puis preuve souveraine G3 |
| Capabilities / enveloppe / contexte | #333, #471, #448 | Réutiliser, ne pas dupliquer |
| Incarnation / réflexes / reprise | #318, #484, #485 | Préserver identité et filiation ; UNKNOWN vers Donna |
| Universal Constructor | #388 et #512 fermées not_planned après migration de scope | Conserver la doctrine ; reprendre Projects 5 et 8, sans rouvrir un méga-epic |
| R0/R1 | #514 | Contrat/lifecycle ; preuve live distincte à retrouver |
| ExecutionPacket | #560 | Précondition de dispatch Jules borné |
| Réconciliation du stock | #561 | Revue des doublons et dispositions traçables |
| Canary Jules | #562 | Exactement une session après passage des conditions #560 |

La clôture migratoire de #388/#512 ne prouve ni abandon du constructeur ni implémentation complète. Cette synthèse n'attribue aucun PASS runtime supplémentaire.
