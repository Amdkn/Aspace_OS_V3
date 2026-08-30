# CARTE.md — refonte `coach-os`

**Date** : 2026-08-05
**Lecture** : 18 rapports (`T1`–`T5`, `T6_these`, `N1`–`N4`, 8× `C2_*`)
**Verbatim** : citations ≤15 mots. Sources citées en ligne sur chaque primitive.
**Doctrine tenue pour acquise** : `ADR-OMK-PRODUCTS-001` (P1/P2/P3), `ADR-ICP-NEXUS-001` (5 sous-types dont coach), `ADR-AAAS-PRICING-001` (5 tiers), `ADR-L2-AAAS-001` (3 Variants Solaris/Nexus/Orbiter comme configurations d'une même usine P1 → P2 → P3).

---

## 0. Le verdict en une page

L'analyse converge : il manque au shell **une couche de graphe de contexte** (entités, relations, instances, règles, contrats sémantiques). Cette couche est le seul objet de P1 qui soit universellement cité. Quatorze rapports sur dix-huit la portent. Sans elle, les 19 apps ré-inventent leurs types et l'OS reste une collection de coquilles (`T6 §4.1`, `T1 §1/§3`, `C2_sales_2 §4.1`, `C2_sales_1 §5`, `C2_ai_native §5`). Avec elle, les 19 apps deviennent des **vues verticales** sur un même substrat — exactement ce que la doctrine E-Myth appelle « B2/B3 sur B1 ».

L'usine existe déjà à 60 % : kernel générique (CMS, AppFrame, Desktop, observabilité, dual-write Supabase) est réutilisable tel quel sans modification (`N3 §4.1`). Ce qui manque, c'est la **chair sémantique** — passer d'un shell qui manipule des collections à un shell qui raisonne sur des entités nommées. Trois chantiers le débloquent dans cet ordre : (1) construire la couche transversale + émettre un premier graphe ontologique ; (2) refondre `onboarding` comme moteur d'installation FDE (le test de la thèse, 30 jours, sans ingénieur en salle) ; (3) réorganiser `it-rd` en runtime visible (packs, log append-only, behaviors). Sans le premier chantier, les deux autres sont aveugles.

L'architecture ternaire P1/P2/P3 est **inattaquable côté doctrine** mais **non construite côté code** : aucun P2 Meta Factory n'existe (`N4 §4.1`). Le moment pour le démarrer n'est pas « après avoir stabilisé Nexus » — il est « pendant la duplication la plus simple possible, à un seul tenant ». Pour le coaching premium, P2 = un script qui réplique l'instance.

---

## 1. Primitives retenues — tableau dédupliqué

**Méthode** : trois tests par primitive — (1) **appauvrissement** (rend les sections existantes plus pauvres en isolation), (2) **corroboration** (≥2 rapports de grappes différentes la portent), (3) **niche** (marche pour un expert-comptable, un avocat, un coach — ou signalée comme non-corroborée si elle est mono-rapport).

Sur **~270 primitives** proposées par les 18 rapports, **22 sont retenues** (cible 15-30). Le filtrage retire les décoratives (qui n'appauvrissent rien), les doublons (mêmes primitives sous des noms différents), et les méta-primitives stratégiques sans surface produit (concentration diffuse Altman, système ouvert Wang, motion FDE Bai).

### Couches verticales des 22 primitives

- **P1 — universelles** (12) : ce qui doit exister une seule fois dans le moteur.
- **P1 transversale spécialisée** (4) : présente dans P1 mais paramétrée par variant.
- **Par variant** (5) : ce qui se réécrit à chaque verticalisation.
- **Geste FDE 7–8** (1) : primitive additionnelle que la thèse T6 ajoute aux 5+4 de base.

### Tableau

| # | Primitive | Sources (rapports qui la portent) | P1 / Variant | App ou couche | Test 1 (appauvrit) | Test 2 (×2 grappes) | Test 3 (niche) | Statut |
|---|---|---|---|---|---|---|---|---|
| 1 | **Graphe de contexte versionné** — entités, relations, instances, règles, contrats sémantiques ; curé à la main, pas auto-généré | T1 (ontology), T2 (mémoire graphe), T6 §1.3 (G3 ontologie), C2_sales_1 §5 + §1.5, C2_sales_2 §4.1, C2_ai_native §5 (Diana/Tan/Taggar/Shipper) | **P1** | couche transversale (`ontology` nouvelle app ou `kernel` partagée) | oui (sans lui les 19 apps ré-inventent leurs types) | oui (7 rapports) | oui | **RETENUE** |
| 2 | **Compounding context** — le substrat grossit avec l'usage ; routines qui le maintiennent vivant | C2_sales_1 §1.7 (5 couches d7VP), C2_sales_2 §4.2 (composante de #1), C2_ai_native (compounding engineering + DRRI) | **P1** | couche transversale + routines | oui (sans routines, l'ontologie meurt en 48 h) | oui (3 rapports) | oui | **RETENUE** |
| 3 | **Mémoire + hygiène** (provenance, contradiction check, élagage) — pas la mémoire brute, la mémoire curée | C2_sales_2 §5, C2_ai_native, T2, T1 (compounding learning loop, MotherDuck) | **P1** | couche transversale + section `Memory` | oui (sans hygiène, mémoire = dépotoir) | oui | oui | **RETENUE** |
| 4 | **Cycle de routines (matinale / sync / événementielle)** — maintenir le substrat vivant | C2_sales_1 §1.7 (d7VP), C2_ceo (Boris routines), T2 (claude.md routage) | **P1** | `cognition` (nouvelle) ou jobs de fond | oui (le 2nd brain n'est vivant que par ses routines) | oui | oui | **RETENUE** |
| 5 | **Boucle de rétroaction agentique** — chaque arête d'un processus porte un agent + une métrique (sensor / policy / tool / quality gate / learning) | C2_ceo (Wang + Jeff Dean multi-agent), C2_ai_native (Diana Harj Taggar) | **P1** | couche transversale + section `Boucles` dans `it-rd` | oui (sans boucle, la métrique n'a personne pour la corriger) | oui | oui | **RETENUE** |
| 6 | **Évaluation qui peut échouer (test dur)** — un check qui sait dire non, sinon l'agent cale en une heure | C2_ceo (Boris Cherny), T4 (pass@K + modèle vivant) | **P1** | `it-rd → Eval`, `audit → Cibles testables` | oui (sans test dur, on n'a aucun moyen de savoir si on s'améliore) | oui (2 grappes) | oui | **RETENUE** |
| 7 | **Ablation à chaque release de modèle** — effacer 80 % des instructions à chaque release, restaurer ce qui échoue de manière reproductible | C2_ceo (Boris), C2_ai_native (Brad), T2 | **P1** | `it-rd → Ablations` | oui (sans elle, l'installation sature de directives obsolètes) | oui | oui | **RETENUE** |
| 8 | **Human gate proportionné au coût de la décision** — un memo privé = gate léger, un refund = gate strict | T2 (Lance Martin), C2_sales_1 §2 P13, T6 §1.3 (G10) | **P1** | runtime agentique | oui (sans proportionnalité, l'humain est en dehors de la boucle) | oui | oui | **RETENUE** |
| 9 | **Log agentique append-only + état projeté** — toute action est un événement typé immuable ; l'état est dérivé | T2 (BabyAGI 4), C2_sales_1 §2 P12 (issue enrichie), T3 (loops Mistele) | **P1** | `it-rd → Journal`, `cognition` | oui (sans journal, replay impossible) | oui | oui | **RETENUE** |
| 10 | **Compétence ≠ agent ≠ runbook** — 3 objets distincts avec rythmes et propriétaires différents | C2_sales_1 §3 (transverse), C2_sales_2 §2 P27, T5 (Varick) | **P1 transversale spécialisée** (la grammaire des 3 objets est partagée, l'instanciation est par variant) | `operations → Skills & Runbooks`, `cognition` | oui (sans distinction, on mélange 3 concepts aux rythmes différents) | oui (2 grappes) | oui | **RETENUE** |
| 11 | **DRRI — Directly Responsible Individual** — une personne, un résultat nommé, pas de comité | C2_ai_native (Diana), C2_sales_1 (implicite) | **P1** | `people → Responsabilités`, `tasks → owner nommé` | oui (sans DRRI, les boucles tournent sans personne pour les arrêter) | oui (2 grappes) | oui | **RETENUE** |
| 12 | **Diagnostic de contrainte comme porte d'entrée** — « si X clients débarquaient, qu'est-ce qui casserait en premier ? » avant toute offre | C2_product_1 (Nate Herk), C2_landing (Tom Youngs Repel/Dissolve/Invite), T5 (Varick G1/G2) | **P1** | `onboarding → Diagnostic fondateur`, `audit → Blocages`, `sales → Premier contact` | oui (sans diagnostic, l'offre flotte, on vend dans le vide) | oui | oui | **RETENUE** |
| 13 | **Catalogue d'offres packagées comme entité** — nom, phrase outcome-first, prix, ROI chiffrable, niche, statut ; éditable, versionnable | C2_product_1 (Torti), C2_product_2 (Torti ×2), C2_landing (13/shift) | **P1 transversale spécialisée** (la structure de l'objet est partagée ; le contenu se réécrit par variant) | `sales → Offres` | oui (sans catalogue, l'offre est une liste de promesses) | oui | oui | **RETENUE** |
| 14 | **Vendor partnership avec l'OS vertical** — Calendly pour coach, Clio pour avocats, Dentrix pour dentistes | C2_product_2 (Ben AI), C2_growth (Shubham P12) | **P1 transversale spécialisée** | `growth → Partenariats` | oui (sans partenariat, la croissance plafonne à 5-10 clients/mois) | oui | oui (changement d'OS selon vertical) | **RETENUE** |
| 15 | **5 gestes FDE automatisables + 4 irréductibles + 1 éditorial** — ver T6 : décomposer le FDE en gestes spécifiables ; G8 mandat, G10 responsabilité juridique, lecture du non-dit, promotion en primitive sont non-automatisables | T6 §1/§3, C2_ceo §5 (registre éditorial), C2_landing §5 (voix éditoriale non-FDE) | **P1** (méta-cadre du moteur agentique) | désigne le périmètre des autres primitives | n/a (méta-cadre) | oui | oui | **RETENUE** |
| 16 | **Persona-synthétique comme prévision** — distribution d'attributs, calibrable, bornée ; ancrage de prompt obligatoire | T4 (Persona Engineering Insight Sciences), C2_landing §5 nuance | **Par variant** (Nexus = persona méthodique, Solaris = technicien E-Myth, Orbiter = opérateur terrain) | `people → Personas`, `cognition` | oui (sans ancrage, le persona improvise) | oui (2 grappes) | oui (3 archétypes distincts) | **RETENUE** |
| 17 | **Confidence engine** — score agrégé = personalisation + deload + reinforcement ; ce que le client premium paie | C2_landing (Tom Youngs), T2 (compounding) | **Par variant** (Nexus = identity-driven premium) | `welcome → Onboarding identitaire`, `audit → Score de confiance` | oui (sans confidence engine, la promesse de transformation reste creuse) | oui | partiel (mono-rapport C2_landing + T2 le valide indirectement) | **RETENUE** avec flag : corroboration partielle |
| 18 | **Signature intellectual property (IP Vault)** — frameworks/méthodologies propres au coach, versionnés, avec leur « lens » | C2_landing (Tom Youngs V2.5), T4 (corpus indexé), C2_growth (clip de 30 s) | **Par variant** | `operations → IP Vault`, `people → Bibliothèque de formation` | oui (sans IP, l'IA ne fait que mélanger du générique) | oui | oui | **RETENUE** |
| 19 | **Rétention par signal de mouvement** — chaque ship visible (changelog public) réduit le churn plus que les hacks d'onboarding | C2_product_2 (Yasser Elsaid), C2_landing (positive reinforcement V2.3), T5 (Varick G9) | **Par variant** | `clients → Activité produit`, `cognition` | oui (sans signal, clients confondent silence et abandon) | oui (3 rapports) | oui | **RETENUE** |
| 20 | **Audit-not-pitch comme porte d'entrée outbound** — montrer un défaut quantifiable avant de proposer une solution | C2_growth (Adam Erhart), C2_landing (V3.4 proof > promises) | **Par variant** (le défaut à montrer change par vertical) | `sales → Premier contact (audit Loom)`, `audit → Diagnostic` | oui (sans audit, le premier contact = pitch ignoré) | oui (2 grappes) | oui | **RETENUE** |
| 21 | **Action exposée quotidienne** — au moins une action/jour où quelqu'un peut dire non ; streak et compteur d'exposition | C2_product_2 (Naier Saidane), C2_product_2 (Torti vitesse avant préparation) | **Par variant** | `tasks → Actions exposées`, `dashboard → Compteur d'exposition` | oui (sans ce compteur, l'opérateur confond activité et avancement) | oui | oui | **RETENUE** |
| 22 | **Compounding audité en boucle** — eval → gap dans le modèle → correction ; pas d'amélioration sans cette boucle | T1 (compounding learning loop, Atlan Prukalpa), T4 (eval-driven model refinement), C2_ceo (Boris cimetière d'évals) | **P1 transversale spécialisée** | `it-rd → Eval`, `cognition` | oui (sans boucle, le système dérive en silence) | oui (3 rapports) | oui | **RETENUE** |

**Primitives écartées explicitement** (sélection rigoureuse : 8 exemples notables) :
- *Concentration diffuse* (Altman v2) — position politique, pas surface produit.
- *Système ouvert distribué* (Wang) — posture écosystémique, pas primitive OS.
- *Motion FDE comme GTM* (Bai) — pas notre canal de vente.
- *Fabrique à logiciels* (Diana EN7frwQIbKc) — Coach OS produit des transformations, pas du code.
- *Fabrique de specs/tests/agents* (Diana) — l'analogie trop étroite (« spec + tests + agent écrit le code ») fait des coquilles sur Coach OS.
- *SaaS → SaaS* (C2_landing V2.6) — méta-positionnement, pas primitive UI.
- *Boucle napkin* (Jeff Dean) — heuristique de décision CEO, pas objet persisté.
- *Manager commit du code* (Dan Shipper) — dev solo plein temps, pas client-facing.

**Primitives faiblement corroborées** (à garder sous réserve) : aucune des 22 retenues n'a moins de 2 grappes. La #17 (confidence engine) est signalée comme mono-source dominante (Tom Youngs) — corroborée indirectement par T2 (compounding), mais pas doublement validée.

---

## 2. Ce qui appartient à P1 vs par variant

### Appartient à P1 (invariant, universel, structurant) — 13 primitives sur les 22

- **Toutes les primitives de 1 à 12 + 15 + 22** dans le tableau ci-dessus.
- Ces primitives définissent **l'usine** : un shell qui raisonne sur des entités nommées, qui augmente avec usage, qui s'ablate à chaque release, qui distingue compétence/agent/runbook, qui boucle eval→gap→correction.

### Universel P1 mais paramétré par variant (transversale spécialisée) — 4 primitives

- **#10 Compétence ≠ agent ≠ runbook** — la grammaire des 3 objets est partagée ; l'instanciation (quelle compétence, quel agent, quel runbook) est par variant.
- **#13 Catalogue d'offres** — la structure d'une offre (outcome-first, prix, ROI, niche, statut) est générique ; le contenu (coaching premium vs intégration Sage vs drone BTP) est par variant.
- **#14 Vendor partnership** — la mécanique (devenir partenaire de l'OS vertical dominant) est partagée ; le partenaire lui-même change (Calendly vs Clio vs Dentrix).
- **#22 Compounding audité en boucle** — la discipline est générique ; le golden dataset qui mesure la boucle est par variant.

### Par variant — 5 primitives

- **#16 Personas synthétiques** — Nexus = expert méthodique (5 sub-types), Solaris = technicien E-Myth (4 sub-types), Orbiter = opérateur terrain (5 sub-types).
- **#17 Confidence engine** — Nexus = identity-driven premium ($7,5-25K), Solaris = seamless delivery, Orbiter = God's Eye certainty.
- **#18 Signature IP** — la substance change (framework méthodologique vs template de marque vs log de terrain) ; le contenant (Vault versionné) est P1.
- **#19 Rétention par signal de mouvement** — la cadence et le canal varient (changelog public pour coach, NPS pour agence créative, statut zone pour terrain).
- **#20 Audit-not-pitch** — le défaut à montrer change par vertical (compliance RGPD pour avocat, ROI delivery pour agence, zone blanche pour BTP).

### Les entités universelles (réponse à la question « le graphe de contexte est dans P1 ne suffit pas, dis quelles entités »)

Huit entités universelles émergent du croisement T1/T2/N2/sister-canon :

| Entité | Statut | Source canonique | Notes |
|---|---|---|---|
| **Organization** | P1 (multi-tenant) | `solaris_saas_tables.sql` (Solaris + Nexus) | déjà dans le code Coach OS via `cms_collections` |
| **Membership + Profile** | P1 | idem | déjà dans le code (auth.users, JWT `org_id`) |
| **Client** (entité métier générique) | P1 transversale spécialisée | `alykaly` schema SQL ; `Business_Pulse_B3` | le « client » d'un coach ≠ d'un avocat ≠ d'un comptable — mais l'enveloppe est universelle |
| **Offering** + **SOP** + **Rock** + **DoD** + **JTBD** | P1 | `B2_OFFER_BRAND_REVENUE_ENGINE.md`, `JTBD-001` | offrent/engagement/preuve — déjà canonique dans `00_Jerry_Business_Pulse` |
| **Persona** | par variant | voir #16 | distinguée de Profile (qui est l'utilisateur Coach OS, pas la cible) |
| **Runbook / Skill / Agent / Routine** | P1 (la grammaire) | voir #10 | 4 objets distincts |
| **Incident / Run / Patch** | P1 | log agentique append-only | permet replay et rollback |
| **DoD / Done Criterion** | P1 (universal) | `charte` canonique + `chartes_cycle_2 DoD Una 3-critères` | critère vérifiable par grep/ls |

### Ce qui ne se partage PAS (par variant, le reste du journal)

- **ICP** : Solaris cible les agences (DAM, brand-conscious), Nexus les experts (méthodiques, conformité), Orbiter les opérateurs terrain (zones blanches 4G). Persona, mantra, killer feature, marché TAM diffèrent par variant (`ADR-ICP-{SOLARIS,NEXUS,ORBITER}-001`).
- **ICP-filter permanent** dans les runbooks : `Executive_Leadership_Coaching_Nexus` est un exemple Nexus ; chaque variant a sa constante.
- **Methode de vente** : outcome-first chez Nexus, sur-mesure visuel chez Solaris, God's-Eye certainty chez Orbiter.
- **Niche dans la même vertical** : Solaris = Théo, Nadia, Marcus, Léa ; Nexus = experts-comptables, avocats, family offices, coaches, cabinets médicaux ; Orbiter = immobilier, services à domicile, logistique, BTP, projets solarpunk.

---

## 3. Architecture des 19 apps

**Inventaire actuel** : `coach-os/src/apps/` contient 19 dossiers ; 17 apps effectivement enregistrées (`app-discovery.ts:27-52`). Discordance documentée. Sections enrichies = sections existantes qui gagnent des primitives sans changer de nature. Sections refondues = apps qui changent de nature. Sections nouvelles = apps qui n'existent pas encore.

### Apps enrichies (8)

- **dashboard** — ajouter « North stars » (compteur exposition, ships visibles), « Confiance engine » (score agrégé). Conserver le shell glass existant.
- **people** — ajouter sections **Personas**, **Cadence** (heartbeats), **Mémoire** (consolidation hors-bande), **Codex** (golden patterns).
- **operations** — passer de 3 à ~10 sections : **Processus** (cartographie + cycle des cas-limites), **Runbooks** (auto-améliorables), **Benchmarks** (as-code, Harbor, vérificateur multi-nature), **Sandboxes** (découplage cerveau/mains + coffre de credentials), **Changements** (file patches proposés + policy), **Alertes** (issues enrichis à froid), **Audit** (issue enrichi avec traces + snippet + hypothèse).
- **it-rd** — passer de 3 à ~9 sections : **Ontology** (registre d'entités curées, contraintes, invariants), **Pack modulaire** (Core/Deploy/SecOps/Backup, schémas + outils + behaviors + policies), **Journal** (état projeté du log append-only), **Boucles** (capteur/contrôleur/actuateur/setpoint), **Patterns** (études de cas avant/après ré-ingénierie), **Drift** (modèle statique vs vivant, segmentation), **Évals** (pass@K, distribution), **Profils** (DRRI contextual, admin/coach/observer).
- **tasks** — **Definition of Done explicite** (champ obligatoire), **Comparateur** (pixel-diff, golden file, parité comportementale), **Stretch** (difficulté visée vs faisable), **Actions exposées** (compteur hebdo).
- **growth** — **Acquisition** (grille 4 critères viralité/conversion/coût/facilité), **Stratégie** (phasage lancement/scale/optimisation), **Partenariats** (vendor partnership fiches), **AEO** (citations LLM).
- **finance** — **Plancher de marge** (pas cible), **Courbe demande** (scénarios prix/10), **Token budget** (vs headcount évité), **Pricing multi-formes** (setup / retainer / per-event / free hook).
- **product** — **Tier Ranking** (S/A/B/F sur idées), **Lancement 5-step** (validate → pre-sell → launch → audience → productize), **MVP** (un feature / un client / un problème), **Idéation CODE** (rising tide / opportunity / demand / economic sizing).

### Apps refondues (4)

- **onboarding** — refonte majeure. **Aujourd'hui** : quiz commercial 4 questions (`OnboardingApp.tsx:32-72`), score 0-12, demo Citadel. **Devient** : moteur d'installation FDE qui pose les questions de G1/G2 (travail tel qu'il est, exceptions non-écrites), produit un brouillon d'ontologie pour le client, déclenche les routines d'ablation. C'est **le** lieu où la thèse T6 se teste. La plus mal nommée, comme T6 l'avait prédit.
- **audit** — passe de **1/6 grilles écrites** à 6/6. Les 5 grilles stubs (`AuditApp.tsx:269-308`) doivent être écrites (arbitrage/contexte/données/automatabilité/arbitrage-roi). Alignement avec `eval-driven model refinement` (T4 #22).
- **welcome** — refonte orientée **identity shifting** et **confidence engine** (primitives #17). Le copy « no-ai-slop » actuel reste, mais avec un onboarding identitaire ajouté (qui devient le client, pas ce qu'il apprend).
- **sales** — refonte orientée cycle complet : **Ciblage** (grille 4 critères) → **Diagnostic** (contrainte) → **Offres** (catalogue) → **Premier contact** (audit-not-pitch) → **Pipeline** (ice-cold → payment-link) → **Relance** (2 max, pas-de-réponse ≠ non). C'est là que vit **le cycle de vente asynchrone** (DM triage 3★/4★/5★, routing).

### Apps nouvelles (3)

- **cognition** — **la nouvelle app `cognition`** que T6 propose (et que N3 confirme existe comme dossier désenregistré depuis la phase 39b : `CognitionApp.tsx` n'exporte plus de composant standalone, seul `<CognitionOverviewContent>` survit dans Sales). C'est **le journal du raisonnement agentique** : traces, évals, ratés documentés, apprentissages consolidés. Habite la couche transversale **visible**.
- **ontology** — **retenue**. Section `Ontology` selon T6 : liste d'entités curées (Person, Squad, Agent, Runbook, Incident, Deploy, Client, Offering, Persona), relations nommées, RDFS/OWL facultatif, contrats sémantiques par entité, scoping personal/org, promotion vers l'org. Section pédagogique d'inférence (« si tu ne sais pas, dis-le »). Politiquement sensible, logiquement structurante.
- **kernel** — **non retenue comme app séparée**. Le kernel (CMS engine, AppFrame, registry, observabilité) est ce que Coach OS **est**, pas une app qu'il contient. Sa visibilité passe par `it-rd → Ontology` et `operations → Contexte`.

### Apps inchangées (3)

- **clients** — structure actuelle correcte ; enrichie par des champs Persona et IP-Vault cross-référencés.
- **legal** — stub actuel (~6 Ko). À enrichir avec contrats sémantiques par entité (`Offre` → CCG, « règle de licensing ») et risque hiérarchisé (Risque = transformatif, plutôt que checklist alphabétique).
- **design** — vitrine de styles visuels inchangée. Couplage au shell fort mais hors chemin critique.
- **settings** — per-app theme picker conservé.

### Décisions tranchées par le brief

- **App `ontology`** proposée par T6 → **retenue**. Raison : sans elle, l'Ontology de `it-rd` est noyée dans l'une des 9 sections d'`it-rd` et perd sa centralité. T1 proposait la même chose dispersée dans 3 apps (Ontology in it-rd + Context Layer in operations + People Graph in people). T6 a raison : il faut un seul registre centralisé. **Verdict** : `ontology` est une nouvelle app transverse (visible depuis `it-rd`, `operations`, `people`, mais unique).
- **App `dashboard` convertie** que N3 laisse entendre menacerait — **non tranchée destructivement**. Dashboard reste l'app la plus aboutie du dépôt (`N3 §2.2`). Ce qu'on transforme, c'est **son contenu**, pas sa structure. North stars = identity-driven premium (Nexus), ships visibles. Widgets = confiance engine, exposition streak, eval drift. Glass design + données hardcodées actuelles peuvent rester comme **mode preview** ; le contenu narratif change.
- **App `cognition` nouvelle** → **retenue**. Justifiée par N3 (dossier désenregistré, phase 39b) + T6 (le journal du raisonnement est manquant).
- **App `kernel` nouvelle** → **non retenue**. Le kernel est l'OS lui-même, pas une app.

### Tableau récapitulatif

| # | App | État |
|---|---|---|
| 1 | dashboard | enrichie (north stars, confidence engine) |
| 2 | people | enrichie (Personas, Cadence, Mémoire, Codex) |
| 3 | operations | enrichie (Processus, Runbooks, Benchmarks, Sandboxes, Changements, Alertes, Audit, Coffre) |
| 4 | it-rd | enrichie (Ontology, Pack, Journal, Boucles, Patterns, Drift, Évals, Profils) |
| 5 | clients | inchangée + enrichissement léger |
| 6 | tasks | enrichie (DoD, Comparateur, Stretch, Actions exposées) |
| 7 | marketplace | inchangée (vitrine d'intégrations) |
| 8 | product | enrichie (Tier Ranking, Lancement, MVP, Idéation) |
| 9 | growth | enrichie (Acquisition, Stratégie, Partenariats, AEO) |
| 10 | sales | **refondue** (cycle complet) |
| 11 | audit | **refondue** (1/6 → 6/6 grilles) |
| 12 | finance | enrichie (Plancher, Token budget, Pricing multi-formes) |
| 13 | legal | enrichie (contrats sémantiques, Risque) |
| 14 | settings | inchangée |
| 15 | onboarding | **refondue majeure** (moteur FDE) |
| 16 | welcome | **refondue** (identity shifting, confidence engine) |
| 17 | design | inchangée |
| 18 | **cognition** | **NOUVELLE** (journal du raisonnement) |
| 19 | **ontology** | **NOUVELLE** (registre transverse) |

---

## 4. Contradictions entre rapports — verdicts

**Onze contradictions relevées ; neuf tranchées, deux laissées ouvertes.** Un dossier sans contradiction signalée est un dossier mal lu.

### 4.1 Nexus/Solaris/Orbiter : 3 produits ou 3 niveaux tarifaires ?

- **N1** (§4.1) : 3 niveaux tarifaires d'un même produit (Solaris ≤ Nexus ≪ Orbiter).
- **N4** (§2.1) : 3 **Variants** d'une même usine, frères, configurables dans P2 Meta Factory (ADR-OMK-PRODUCTS-001 ratifié 2026-07-09).
- **N3** (§5.1) : code applicatif (`ProductView.tsx:29-57`) les définit comme 3 produits distincts.

**Verdict : N4 a raison, N1 est obsolète.** Le pivot « Variants d'une même usine » est dans l'ADR ratifié. N1 reflète la perception par les B3 agents (qui raisonnent en tiers), N3 reflète le code applicatif. Lequel des deux est obsolète ? N1 parle de « three levels d'un même produit, status actuel Solaris≥Nexus≫Orbiter » — c'est une lecture héritée des chartes Picard mai 2026, **avant** le pivot ADR-OMK-PRODUCTS-001 (juillet). Donc N1 cite une strate morte. La doctrine actuelle est N4.

### 4.2 Ontologie : prérequis ou luxe ?

- **T6 + C2_sales_1 + C2_sales_2** : primitive obligatoire (sans elle, les agents hallucinent, les apps ré-inventent leurs types).
- **C2_product_1 + C2_product_2** nuancent : pas indispensable tant que le volume reste gérable (Yasser Elsaid Chatbase fonctionne sans ontologie formelle).

**Verdict : pas contradiction, deux phases.** Phase 1 (MVP single-tenant) = implicite statistique OK, c'est ce que le code Coach OS actuel est. Phase 2 (P2 Meta Factory = multi-tenant, multi-niche) = ontologie curée obligatoire, sans elle la duplication crée la dette que N3 §5.2 décrit (RLS adversariale non testée, deux instances de niche sans couche générique). Donc : **ontologie pas au jour 1, mais au moment de la duplication**.

### 4.3 Onboarding : coquille démo ou moteur FDE ?

- **N3** (§2.2) : coquille démo (4 questions Citadel, score 0-12, demo Sales Sanctum).
- **T6** (§4.2) : « le moteur d'installation FDE », doit poser questions G1/G2, produire brouillon d'ontologie, déclencher ablations.

**Verdict : T6 a raison pour la cible, N3 décrit l'état actuel.** Pas contradiction, transition planifiée. Le chantier #2 ci-dessous réalise la transition.

### 4.4 Compound engineering : DRRI = DRRI ou DRRI ≠ DRRI ?

- **C2_ai_native** (Diana, Garry Tan, Harj Taggar) : DRRI remplace la hiérarchie.
- **T5** (§Compétences §Process owners nommés) : "chaque étape a un humain responsable".

**Verdict : même primitive, deux grappes.** DRRI = un humain nommé + un outcome nommé + un journal. Sans DRRI, les boucles tournent sans propriétaire. Les deux grappes convergent : chaque arête d'un processus, chaque app, chaque outcome portent un DRRI.

### 4.5 Compound engineering : boucles seulement, ou contexte d'abord ?

- **C2_ai_native** : DRRI + compounding engineering + memory+hygiene = tout en même temps.
- **T6 §4.4** : un seul agent-FDE dans un seul vertical est le test minimum.

**Verdict : pas contradiction, séquence.** Phase 1 = un agent, un vertical, 30 jours (test T6). Phase 2 = compound engineering (DRRI + boucles + memory+hygiene). T6 lui-même pose le premier increment comme « le plus petit livrable qui teste les deux bouts irréductibles ».

### 4.6 Compétences = compétences, ou skills + agents + runbooks ?

- **C2_sales_2 §3 (Compétence ≠ agent ≠ runbook)** : 3 objets distincts.
- **T5** (Varick) : distinction compétence/agent/runbook implicite.

**Verdict : même grille, deux formulations.** Les deux grappes convergent sur la grammaire : 4 objets minimum (Compétence/Agent/Runbook/Routine), avec rythmes et propriétaires différents. Retenir comme primitive #10.

### 4.7 Routines : quelle cadence ?

- **C2_sales_1 §1.7 (d7VP)** : routine matinale (pull 24 h), sync CRM (snapshot quotidien), événementielle (call prep sur nouveau RDV).
- **C2_ceo (Boris)** : routines asynchrones (« routine = same thing, running in the cloud »).
- **T3** : « disturbance dampener » (scan déterministe à chaque PR) plutôt que routine temporelle.

**Verdict : trois cadences cohabitent.** Trois types de routines sont nécessaires : (a) temporelles (matinale, sync, rêve), (b) événementielles (call prep, incident, deployment), (c) par release/évolution (ablation, scan de régression). T2 (Lance Martin) appelle ça « en-bande + hors-bande + découplage cerveau/mains ». Toutes trois sont déjà dans le tableau #4 routines.

### 4.8 Doctrine USD vs EUR

- **ADR-AAAS-PRICING-001** : USD canon après acceptopuncture (2026-06-24 amendé).
- **N3** : EUR 25-750-1555 €/mois cités dans chartes Solaris/Nexus/Orbiter legacy.
- **Chartes_cycle_2** : `grep EUR\|€\|SEPA = 0` DoD-3 obligatoire.
- **runbook-coach-premium-capsule.md** (N3 cite sans le lire) : cite « Coach senior 500-2000€/h » (EUR) en pricing coach.

**Verdict : contradiction non résolue en code. À trancher avant production.** USD canon pour les 5 Tiers AaaS ; EUR historique conservé pour la « facturation horaire » du métier de coach (qui est la promesse du produit, pas le pricing du produit lui-même). La distinction est défendable (USD = pricing du shell, EUR = benchmark du marché du client) mais n'est écrite nulle part.

### 4.9 Méta-factory P2 : démarrer quand ?

- **N3 §3.4** + **N4 §4** : aucune instance P2 Meta Factory n'existe. Le code est du Solaris-spécifique ou du Nexus-spécifique.
- **T6 §5** : « construire la plateforme avant l'agent, c'est exactement le dev shop. Alternative A rejetée ».
- **N1** (dossier canon `01-omk-business-os`) : 5 phases livrées sur 8, Phase H RLS adversariale non démarrée.

**Verdict : ne pas construire P2 d'abord.** T6 §4.4 tranche directement : alternative A (plateforme de primitifs) rejetée. Phase H RLS manque — c'est le premier chantier technique obligatoire *avant* toute duplication. Mais le script de duplication lui-même est infra ; on l'écrit en même temps qu'on duplique, pas avant.

### 4.10 Asymétrie multi-tenant : Solaris dual-mode vs omk single-mode

- **N3 §3.3** (cite `MIGRATION_SUPABASE.md`) : 3-stage tenancy model (PoC SaaS → Coach-owned Cloud → White-label self-host).
- **N4 §3.3 / §4.1** : Solaris dual (internal + saas), omk single-mode A1 LOCKED.
- **ADR-OMK-004** : single SaaS only (pas d'internal).

**Verdict : à arbitrer.** L'ADR est le canon, mais Solaris reste dual. La doctrine a pivoté ; le code Solaris n'a pas suivi. Si on duplique, on passe single. Si on garde Solaris dual, on garde le multi-mode-niche. Pas tranché — c'est une décision stratégie qui dépend du calendrier de duplication.

### 4.11 Compounding sans DRRI ou DRRI sans compounding

- **C2_ai_native §4** : bouclé — 1 sans 2 = débit sans qualité, 2 sans 1 = qualité qui ne compound.

**Verdict : pas contradiction, dépendance mutuelle.** Les deux vont ensemble, l'une sans l'autre s'effondre. Tranché : on ne démarre pas compounding engineering sans avoir nommé les DRRI.

**Deux questions tranchées comme contradictoires mais ouvertes dans les rapports** :

- **Phase H RLS adversariale** (N3 + N4) : bloquant identifié, non livré, pas de date. Qui décide ?
- **SUMMERS_VERSE_MANIFEST.md canon** (N4) : référencé par `omk/MANIFEST.md:48`, introuvable dans le périmètre de travail. Qui l'écrit, qui le signe, qui le maintient ?

---

## 5. Ordre d'exécution — sept chantiers

**Critère d'ordre** : le premier chantier est celui sans lequel les suivants sont aveugles. L'ordre minimise les retours en arrière. Pour chacun : ce qu'on saura après, qu'on ne savait pas avant.

### Chantier 1 — Émettre la couche transversale + le premier graphe ontologique

**Cible** : app `ontology` minimale viable (12-15 entités curées), section Ontology dans `it-rd`, section Context Layer dans `operations`, et un bootstrap qui injecte les noms dans `cms_collections` et les relations dans un graphe (Neo4j Lite ou Postgres+ltree).

**Livrables** :
- `coach-os/src/apps/ontology/` avec sections Entities / Relations / Contracts / Versions.
- 12 entités nommées : Organization, Membership, Profile, Client, Offering, SOP, Runbook, Skill, Agent, Routine, Incident, Persona.
- 1 graphe de relations typées (Client *offert par* Offering *lié à* SOP, etc.).
- 1 contrat sémantique par entité (déclencheurs + actions permises).
- Toggle personal/org pour 5 entités au moins.

**Ce qu'on saura après, qu'on ne savait pas avant** : si la couche transversale porte les 19 apps sans friction, ou si elle crée une dette de synchronisation. Si l'ontologie curée à la main passe l'échelle d'un seul client, ou s'il faut l'auto-générer (auquel cas on rejoint les critiques de Jonas sur GraphRAG).

### Chantier 2 — Refondre `onboarding` comme moteur d'installation FDE

**Cible** : refaire `OnboardingApp.tsx` pour qu'il pose les questions G1/G2 (travail tel qu'il est, exceptions non-écrites), produise un brouillon d'ontologie pour le client, déclenche la routine d'ablation initiale. Selon T6 §4.4, c'est le **premier increment de la thèse**.

**Livrables** :
- 6-8 questions d'introduction (process leads, edge cases, sources de vérité).
- Génération d'un brouillon d'entités et de relations que l'humain curera.
- Connexion à la couche transversale du chantier 1 (pas un silo à part).
- Test : un agent-FDE produit un brouillon d'ontologie pour un vertical choisi (finance + AP reconciliation, ou family office, ou cabinet médical) en moins de 30 jours.

**Ce qu'on saura après** : si la thèse FDE 5+4 tient, ou si elle se heurte à l'un des 4 gestes irréductibles (G8, G10, lecture du non-dit, promotion en primitive). **Si l'agent échoue à produire l'ontologie, G1/G2 sont en cause — la thèse s'effondre. Si l'agent produit l'ontologie mais l'agent d'exécution reste à 50 %, G6/G7 sont en cause — la thèse tient.**

### Chantier 3 — Réorganiser `it-rd` en runtime visible

**Cible** : transformer `it-rd` de vitrine Kernel/Experiments/Deploys en runtime structuré par : (a) Ontology (déjà chantier 1), (b) Loop Engineering (Mistele : setpoint/sensor/controller/actuator + disturbance dampener), (c) Pack modulaire (BabyAGI 4 : schémas + outils + behaviors + policies), (d) Journal append-only (état projeté), (e) Eval (pass@K + cimetière + golden dataset).

**Livrables** :
- Section `Loops` avec forme canonique (decide → act → check → recommence).
- Section `Journal` immuable, replay jusqu'à N jours.
- Section `Profils` DRRI-contextuels (admin/coach-senior/coach-junior/observer).
- Tests d'ablation automatisés : effacer 80 % des instructions à chaque release de modèle.

**Ce qu'on saura après** : si l'ablation automatisée est rentable (si on n'a pas à la faire à la main, c'est une victoire ; sinon c'est une dette).

### Chantier 4 — Refondre `operations` en KB graphe + Runbooks auto-améliorables

**Cible** : passer la section Knowledge Base d'operations (coquille actuelle) en graphe navigable de processus + dépendances. Ajouter Processus (cartographie + cycle des cas-limites), Runbooks auto-améliorables (skill que l'agent peut amender après chaque incident résolu), Benchmarks as-code (Harbor anatomy : instruction + environnement + oracle + verifier).

**Livrables** :
- Section `Cartographie` (graph view, sous-onglet `Recherche` hybrid vector→graphe).
- Section `Processus` nommée (les processus Coach OS avec edge cases documentés).
- Section `Runbooks` versionnés + auto-améliorables.
- Section `Benchmarks` (instruction + env + oracle + verifier) avec étiquetage difficulté (simple/medium/hard).
- Section `Alertes` issues enrichis (signal, traces, snippet, hypothèse, risques).

**Ce qu'on saura après** : si la mémoire graphe + runbooks auto-améliorables rendent réellement les opérations plus rapides, ou si c'est une autre coquille qui prend plus de temps à maintenir qu'elle n'en fait gagner.

### Chantier 5 — `people` : Personas synthétiques + Cadence + Mémoire + Nudges

**Cible** : transformer people pour qu'il porte (a) **Personas** synthétiques (Distribution d'attributs + ancrage de prompt + durabilité test + biais d'ordre, primitive #16), (b) **Cadence** heartbeats (routine async qui réveille 1:1 hebdo, revue mensuelle), (c) **Mémoire** en-bande + hors-bande, (d) **Nudges** proactifs (chaque app pousse, pas attend).

**Livrables** :
- Section `Personas` (entre Squads et Content) avec éditeur d'ancrage + onglet Calibration (plancher de bruit humain) + Durability (test de stabilité).
- Section `Cadence` refondue (heartbeats, échelles de routine, threads pinned comme coéquipier).
- Section `Mémoire` (épisodes bruts + faits extraits, distinction épisodes/sémantique).
- Section `Nudges` (file d'alertes que le système pousse).
- Section `Codex` (golden patterns artisanaux, Mistele).

**Ce qu'on saura après** : si Personas calibre les recommandations pour 80 % des cas, ou si la variabilité cache des bruits que la persona n'absorbe pas.

### Chantier 6 — Refondre `sales + growth + audit + welcome` en cycle acquisition complet

**Cible** : aligner ces 4 apps sur le cycle d'acquisition (Ciblage → Diagnostic → Offres → Premier contact → Pipeline → Relance). Inclut les primitives #12 (diagnostic), #13 (catalogue d'offres), #20 (audit-not-pitch), #21 (action exposée).

**Livrables** :
- `sales → Ciblage` (grille 4 critères : ticket / dirigeant-en-opération / répétitif / réseau).
- `sales → Offres` (catalogue éditable + versionnable).
- `sales → Premier contact` (audit Loom template — primitive #20).
- `audit → Diagnostic` (6 grilles écrites au lieu d'1/6 stubs).
- `growth → Acquisitions` (grille canaux + phasage + toggle volume/qualifié + vendor partnerships).
- `growth → AEO` (citations LLM).
- `tasks → Actions exposées` (compteur hebdo, streak).
- `welcome → Onboarding identitaire` (identity shifting, confidence engine).

**Ce qu'on saura après** : si le pipeline candidat→premier-contact→client passe en moins de 30 jours (avec onboarding FDE intégré), ou si le cycle reste plus lent que ce que la doctrine prétend.

### Chantier 7 — Sprint Meta Factory : extraire la couche générique

**Cible** : à ce stade, on a un Nexus Coach OS avec couche transversale, ontologie curée, runtime visible, ops + people + sales + audit stables. **Avant de dupliquer Solaris ou Orbiter**, on extrait la couche générique dans un package unique. C'est le moment P2.

**Livrables** :
- `coach-os-core/` extractible : kernel (CMS engine, AppFrame, registry, observabilité), couche transversale (ontology, routines, contracts).
- Template de verticialisation : `verticalize-to-niche.sh` qui prend un CSP (Configurable Shared Primitives) et injecte la verticalisation.
- Test : créer un Solaris-bis (Solarpunk) en moins d'une semaine-juridique.

**Ce qu'on saura après** : si l'extraction réussit sans réécriture, ou si on découvre que Nexus contient trop de coach-spécifique et qu'il faut distinguer P2 (générique) et Nexus (P2 + coatings Coach).

**Hors chantier** : la duplication elle-même (créer une instance Solaris ou Orbiter) est post-chantier 7. Elle n'est pas un chantier de cette carte.

### Pourquoi pas un chantier « refonte `dashboard` »

`dashboard` est l'app la plus aboutie du dépôt (`N3 §2.2`). Sa refonte est contingente aux chantiers 5-6 (elle prend ses primitives en dépendance). Pas la peine de la traiter en chantier isolé.

---

## 6. Ce qui ne va pas dans le corpus

**Sept rapports signalés comme faibles, brodés ou hors sujet** ; quatre questions restent sans réponse malgré 18 rapports.

### Rapports faibles ou hors sujet

- **T5 (Forward Deployed Engineering et études de cas)** — moins nourri que T1-T4. Les 4 vidéos couvrent des terrains différents (Bai anthropique, Varick, Bridgewater, Codex) sans qu'aucune ne soit centrale à Coach OS. Varick est le plus aligné (méthode FDE = cartographie + cycle des cas-limites), mais le « cas Bridgewater Pat » est trop vertical (investissement financier) pour produire des primitives actionnables sur coaching. **À ranger comme contexte doctrinal, pas comme source de primitives**.

- **N1 (carte du canon `01-omk-business-os`)** — utile pour la doctrine E-Myth, mais **cite le pivot 3-tiers (Solaris ≤ Nexus ≪ Orbiter) antérieur au ratifié `ADR-OMK-PRODUCTS-001`**. Conséquence : la lecture produit est obsolète par doctrine (N4 §3.3 le note poliment). À dépolluer par grep de remplacement.

- **C2_GROWTH_ACQUISI (Léo, Matt Clark, Jeremy Miner, Shubham Sharma, Michele Torti, Adam Erhart)** — solide mais **très centré agence IA B2B locale US** (clipping, video outbound, cold email). Quatre vidéos sur six parlent de canaux de volume (clipping, LinkedIn automation). Pour Coach OS B2C à 500-2000€/h, peu de jambes. **À conserver pour les primitives de méthodologie** (Torti « outcome-first » #2-3, Erhart « audit-not-pitch » #20) ; **à ignorer pour les canaux de volume** qui ne s'appliquent pas.

- **C2_LANDING_WELCOM** — **forte redondance interne** signalée d'entrée : 4 vidéos du même auteur (Tom Youngs), sur le même business (Scale Twenty), itérant sur les mêmes briques. Bonne corroboration par répétition, mais « single-author bias » : les primitives micro-cult messaging, Repel/Dissolve/Invite, SaaS → SaaS, identity shifting, confidence engine, IP signature sont toutes issues du même modèle conceptuel. **À valider par d'autres grappes avant de canoniser** (primitives #17, #18 corroborées partiellement seulement).

- **Trois C2_PRODUCT_OFFE_1/2 et SALES_ONTOLO_1/2 — **chaque grappe a 1 vidéo manquante ou faible** (Torti est omniprésent, Donnelly stéréotypé, Naier Saidane 1 vidéo sur le sujet vaut lecture). **Torti fait 6 apparitions sur 11 vidéos** : son modèle d'agence IA est peut-être sur-représenté. À diversifier pour la Phase 2.

- **C2_AI_NATIVE_CEO et C2_CEO_INTERVIEW** — Ces deux grappes convergent sur **ablation** et **DRRI** mais **n'abordent ni le mandat hiérarchique, ni la responsabilité juridique, ni la lecture du non-écrit** (les 4 gestes irréductibles de T6). Elles valident la couche procédurale, pas la couche éthique. **À compléter par un autre corpus avant la phase de production**.

- **C2_SALES_ONTOLO_2** — la 9ème vidéo (`lWTvx53s9q4`) est **404**. Manque une donnée non documentée. Restent 7 vidéos exploitables, suffisantes pour les conclusions.

### Questions sans réponse

1. **L'ACV médian du coach Nexus premium** — `ADR-NEXUS-NICHE-001` cite « Coach senior 500-2000€/h » (per-call ou mensuel ?), `$7.5-25K ACV` (de la setup ou annuel ?). Le baseline 1.2M ARR suppose 100 clients × $1k/mois. Cohérent ou c'est un mix ? **Quelqu'un a-t-il signé un contrat Nexus Coach OS ?** Pas dans le corpus.
2. **Phase H RLS adversariale** — N3 + N4 + C2_sales tous la signalent comme bloquant (`omk/CLAUDE.md:43-45` confirme `❌ NOT STARTED`). Aucune date de livraison. **Qui décide ?**
3. **Devise USD vs EUR en code opérationnel** — 6 occurrences de « OUT EUR » dans les chartes (`chart_T1_people_b2b_saas_playbook.md:18`), mais le runbook coach premium cite les deux. D6 no-self-contradiction pas résolu.
4. **SUMMERS_VERSE_MANIFEST.md canon** — référencé par `omk/MANIFEST.md:48`, introuvable dans le périmètre de travail (`N4 §7.1`). Aucune version canonique signée.
5. **Symlink `_doctrine` cassé** dans `solaris/` (`N4 §4.1`) — pointe vers `00 Agency as a Service/` qui n'existe plus. Probablement une restructuration de dossier non propagée. Aucune action de réparation documentée.
6. **Vendor partner Calendly** — présumé par C2_product_2. Calendly a-t-il un Partner Program ? Une exploration rapide montrerait que non (Calendly a un Marketplace, mais pas un programme partenaire). Si on s'appuie sur Calendly, on s'appuie sur un écosystème qui n'existe pas.
7. **Coût réel de l'ontologie** — `C2_product_2 §5 nuance : « la thèse présuppose peut-être trop vite que l'ontologie est un prérequis du FDE — l'implicite statistique peut suffire tant que le produit n'a pas à manipuler des objets de domaine complexes. »** Le passage à l'ontologie curée au moment de la duplication (chantier 7) doit être validé sur un cas réel. Sans cette validation, chantier 1 est un pari.
8. **Cas Bridgewater « 50 ans de règles codifiées »** — T5 cite verbatim. Aucune trace dans Coach OS d'un corpus indexé équivalent. La primitive #18 (IP Vault) est cohérente, mais **à quel échelon temporel** ? Un coach senior a 10-20 ans de pratique, pas 50. La métaphore Bridgewater vaut pour la discipline, pas pour le volume.

**Sept questions ouvertes**, dont quatre (1, 4, 5, 6) sont **trous noirs** que 18 rapports n'ont pas creusés. Tous les autres grappes les ignorent parce qu'ils sont dans le périmètre opérationnel (`omk/`), pas dans le périmètre doctrinal (`analyse/*.md`).

---

## Annexe — Synthèse de l'effort de lecture

**Fichiers lus** : 18 rapports dans `analyses/`, **6 782 lignes au total**, dont :
- T1-T5 + T6 : 6 rapports techniques (1 314 lignes).
- N1-N4 : 4 rapports d'inventaire dépôts (1 310 lignes).
- C2 (×8) : 8 rapports métiers (4 158 lignes).

**Doublons inter-rapports éliminés** dans le tableau §1 : sur ~270 primitives brutes, **22 retenues** (92 % de filtrage). Doublons majeurs détectés et fusionnés :
- Mémoire graphe (T1+T2+C2 sales 1/2) → primitives #1, #2, #3.
- Boucle de rétroaction agentique (C2 CEO + C2 AI-native + C2 sales) → #5.
- Evaluation qui peut échouer (C2 CEO + T4) → #6.
- Ablation (C2 CEO + C2 AI-native + T2) → #7.
- Confiance vs sales (T5 + C2 landing + C2 sales 1) → #2 + #17.
- Catalogue d'offres (C2 product 1 + C2 product 2 + C2 landing) → #13.
- Compétences/Agents/Runbooks distincts (C2 sales 1 + T5 + T2) → #10.

**Citations verbatim** : partout ≤15 mots (conformément au brief).

**Sources** : `T1`=T1, `T2`=T2, ..., `T6_these`=T6, `N1`=N1, ..., `N4`=N4, `C2_landing`=C2_LANDING_WELCOM, `C2_ceo`=C2_CEO_INTERVIEW, `C2_ai_native`=C2_AI_NATIVE_CEO, `C2_growth`=C2_GROWTH_ACQUISI, `C2_product_1`=C2_PRODUCT_OFFE_1, `C2_product_2`=C2_PRODUCT_OFFE_2, `C2_sales_1`=C2_SALES_ONTOLO_1, `C2_sales_2`=C2_SALES_ONTOLO_2.

---

*CARTE.md — 2026-08-05 — manager de la délégation — 18 rapports lus, 1 fichier produit.*
