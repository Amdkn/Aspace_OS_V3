# BRIEF SYNTHESE — fusionner 18 rapports en une carte de refonte

Tu es le **manager** de cette délégation. Dix-huit agents ont travaillé sur des
périmètres disjoints, sans se lire. Ton travail n'est pas de résumer leurs
rapports : c'est de les **confronter**, d'écarter ce qui ne tient pas, et de
produire une carte utilisable.

## Le cadre doctrinal — vérifié, ne le redécouvre pas

Ces faits ont été lus dans les ADR ratifiés et vérifiés ligne à ligne. Tu les
tiens pour acquis. Si un rapport les contredit, c'est **le rapport** qui a tort,
et tu le signales.

**La ligne produit** (`ADR-OMK-PRODUCTS-001`, ratifié 2026-07-09) :

- **P1 — OMK BOS** : le moteur interne, l'usine. Non vendu tel quel.
- **P2 — OMK Meta Factory** : le white-label vendu aux agences. **C'est ici que
  vivent les 3 Variants**, Solaris / Nexus / Orbiter, comme trois configurations
  d'une même usine. Verbatim : « l'agence cliente achète une usine logicielle à
  haute marge, revendable (Built to Sell), pas des tokens ».
- **P3 — R&D souverain** : alimente P1 et P2, horizon lointain.

Donc **Nexus n'est pas la base de Solaris et Orbiter — ils sont frères.** La base
est P1.

**Nexus** (`ADR-ICP-NEXUS-001`) vise **cinq sous-types** : experts-comptables,
avocats, family offices, **coachs**, cabinets médicaux. Le coaching est un
cinquième d'un tiers d'un étage. Positionnement : « la Citadelle du Savoir » —
donnée froide, critique, confidentielle ; le chaos vient d'un **débordement
informationnel**, pas d'un manque de créativité.

**Partagé entre variants** : les 8 domaines B2 (Growth, Sales, Product, Ops, IT,
Finance, People, Legal), les 53 agents B3, le format de charte, la cadence 12WY,
le format JTBD, la grille tarifaire à 5 paliers.
**Par variant** : persona, mantra, marché/TAM, killer feature, filtre d'ICP.

**Le produit logiciel** : `coach-os`, un shell type OS de bureau (React 19,
TypeScript, Tailwind, Zustand), 19 apps montées dans des fenêtres déplaçables.
Chaque app a une barre latérale de sections, chaque section une page de détail.
La plupart sont des coquilles génériques. Une divergence est déjà signalée : la
doctrine impose Vercel + Supabase Cloud, Solaris tourne sur Dokploy self-host.

## Ce que tu dois lire

Tous les fichiers de `analyses/` :

- **`T1`–`T5`** — 18 conférences sur l'ingénierie d'agents : ontologie, mémoire
  de graphe, boucles, évals, Forward Deployed Engineering.
- **`T6_these.md`** — la thèse : le métier de FDE se décompose en gestes, cinq
  automatisables, quatre irréductibles. **Lis-le en premier**, il porte la
  direction.
- **`N1`–`N4`** — l'exploration des dépôts : canon doctrinal, pouls métier,
  projets réels, ligne de produits.
- **`C2_*`** — 58 conférences sur les métiers : direction, vente, offres, flux,
  croissance, acquisition.

## Livrable — `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/CARTE.md`

### 1. Les primitives, dédupliquées

Les rapports proposent des centaines de primitives, dont beaucoup sont la même
chose sous des noms différents. **Fusionne-les.**

Une primitive retenue doit passer trois tests :

1. **Le test d'appauvrissement** — elle rend les sections existantes plus pauvres
   en isolation. Si l'ajouter ne dévalorise rien, c'est décoratif.
2. **Le test de corroboration** — au moins deux rapports issus de grappes
   différentes la portent. Une primitive isolée peut être géniale ; dis-le, mais
   marque-la comme non corroborée.
3. **Le test de niche** — marche-t-elle pour un expert-comptable et un avocat,
   ou seulement pour un coach ?

Tableau :

| primitive | rapports qui la portent | P1 ou par variant | app ou couche | passe les 3 tests ? |

Vise **entre 15 et 30 primitives retenues**. Moins, tu as sur-filtré ; plus, tu
n'as pas arbitré.

### 2. Ce qui appartient à P1

**La question centrale.** Qu'est-ce qui doit exister **une seule fois** dans le
moteur, et qu'est-ce qui se configure par variant ?

Sois précis : « le graphe de contexte est dans P1 » ne suffit pas. Dis quelles
entités sont universelles et lesquelles sont propres à une verticale.

### 3. L'architecture des 19 apps

Pour chacune : son rôle dans P1, ses sections de barre latérale, et pour chaque
section ce que porte sa page de détail. Distingue trois états :

- **refondue** — l'app existe et change de nature ;
- **enrichie** — l'app existe et gagne des sections ;
- **nouvelle** — l'app n'existe pas encore.

Un rapport a proposé une app `ontology` absente aujourd'hui. Tranche : la
retiens-tu, et pourquoi ?

Un rapport a proposé de convertir `dashboard`, qui est l'app la plus aboutie du
dépôt. Tranche aussi, en pesant la perte certaine contre le gain hypothétique.

### 4. Les contradictions entre rapports

**Section obligatoire.** Où deux rapports se contredisent-ils, et lequel a
raison ? Donne ton verdict et ta raison. Un dossier de 18 rapports sans aucune
contradiction signalée est un dossier mal lu.

### 5. L'ordre d'exécution

Cinq à huit chantiers, ordonnés, chacun avec ce qu'il débloque. Le premier doit
être celui sans lequel les autres sont impossibles.

Pour chaque chantier : ce qu'on saura après, qu'on ne savait pas avant.

### 6. Ce qui ne va pas dans le corpus

Quels rapports sont faibles, brodés, ou hors sujet ? Nomme-les. Quelles questions
restent sans réponse malgré 18 rapports ?

## Interdits

1. Tu écris **un seul fichier**, à ce chemin absolu exactement :
   `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/CARTE.md`
2. Tu ne modifies aucun dépôt, aucun rapport existant, aucun code.
3. **Ne recopie pas les rapports.** Une synthèse qui fait la taille de la somme
   de ses sources n'est pas une synthèse. Vise 400 à 700 lignes.
4. **N'invente aucune primitive.** Chacune vient d'un rapport, que tu cites.
5. Pas de recherche web, pas de code, pas de plan d'implémentation détaillé.
6. Pas plus de 15 mots d'affilée cités d'un transcrit.

## Si tu dois t'arrêter

Écris la carte avec ce que tu as établi et une section « reste à couvrir ». Les
sections 1, 2 et 4 priment : si le temps manque, livre-les complètes et tronque
le reste.
