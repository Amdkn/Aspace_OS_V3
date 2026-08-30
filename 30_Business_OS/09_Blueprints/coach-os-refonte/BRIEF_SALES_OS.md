# BRIEF — l'app Sales devient un Sales OS Control Center

Tu es developpeur front. Tu refais **une seule app** : `sales` (« Sales Sanctum »).
Tu la reconstruis d'apres le Sales OS de Ben AI, adapte a Coach OS.

Tu travailles en **boucle constructeur / critique** : tu construis une section,
puis tu la juges contre l'image de reference, a l'aveugle, et tu recommences
jusqu'a ce que la notre gagne. Le detail du protocole est en fin de brief — il
n'est pas optionnel, c'est le coeur de la tache.

## Le depot

`C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os`

React 19 · TypeScript · Tailwind v4 · Zustand · Vite.
Fichier principal : `src/apps/sales/SalesApp.tsx`. Accent de l'app : `#ea580c`.
**Reference TS : 73 erreurs. Ne la depasse pas.** `npm test` : 60 verts.

## La barre — regarde-la, ne l'imagine pas

`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/barre-sales/pages/`

15 images pleine resolution extraites de la video de Ben AI.

| Image | Ce qu'elle montre |
|---|---|
| `01-today-tldr-et-appels.png` | Onglet Today : le bandeau noir de synthese, puis « Today's calls » |
| `02-today-fiches-leads.png` | Les fiches de leads du jour, avec score de qualification |
| `03-today-taches-et-changements.png` | « Top tasks » et « What changed today » |
| `04-pipeline-snapshot.png` | **La plus importante** : les 5 onglets visibles, et le Snapshot chiffre |
| `05-pipeline-tendances.png` | Les courbes : reunions par semaine, revenu et commission |
| `06-pipeline-scores-rep.png` | Taux de closing, score du commercial par dimension |
| `07-context-documents.png` · `08-context-icp.png` | Onglet Context et la fiche « ICP, the buyer » |
| `09-stack-connecteurs.png` · `10-stack-complet.png` | Onglet Stack, les outils groupes par role |
| `11-rapport-mensuel-scorecard.png` | Le rapport mensuel et la note du commercial |
| `12-fiche-appel-score.png` | La fiche d'un appel avec sa notation detaillee |
| `13-second-cerveau-dossiers.png` · `14-doc-icp.png` · `15-fiche-deal-historique.png` | Le second cerveau : dossiers, document ICP, fiche de deal |

**Ouvre ces images.** Un critique qui juge sur une description approuve tout.

## Le ton visuel — il est a l'oppose du Dashboard

Le Sales OS de Ben est **clair, creme, editorial** : fond ivoire, larges chiffres
en tres gros, etiquettes en petites capitales espacees, cartes a filet colore en
bas, typographie a chasse fixe pour les libelles. Rien a voir avec le sombre du
Dashboard. Ne transpose pas l'esthetique du Dashboard ici.

## Les 5 onglets

L'app garde ses sections existantes. Tu ajoutes ces cinq-la, dans cet ordre :

**1 · Today** — ce sur quoi se concentrer aujourd'hui.
- Un bandeau de synthese en une phrase dense, ecrit comme un briefing, pas comme
  un titre. Modele reel : « Get Tim De La Salle's proposal, one-pager, and
  information checklist out the door today. #12 still unsent, he reviews with his
  partner and decides this week. Then run three live calls, opening with the
  12:20 Ray rebook you owe him, followed by Louis at 16:45 and Anish at 18:00. »
- « Today's calls » : une fiche par appel avec le nom, la societe, l'heure, un
  **score de qualification automatique**, un brief de preparation deja redige, et
  les liens utiles.
- « Top tasks » et « What changed today », en deux colonnes.

**2 · Pipeline** — l'etat commercial. Le Snapshot d'abord, six cartes :

| carte | valeur | sous-titre |
|---|---|---|
| PIPELINE VALUE | $486k | 54 open deals |
| WON THIS QUARTER | $612k | 31 deals closed |
| WIN RATE, DECIDED | 36% | of qualified meetings |
| AVG DEAL SIZE | $6.4k | $4k floor, $10k ceiling |
| MEETINGS THIS WEEK | 44 | +22% on last week |
| REP SCORE | 7.5 | demo strong, close the gap |

Puis **CRM snapshot, deals by stage** : Meeting booked 24 · Next call qualified 18
· Proposal sent 12 · Won this quarter. Puis les **tendances** : reunions reservees
par semaine, revenu et commission par semaine, courbe de closing, et le **score du
commercial par dimension**.

Adapte les libelles au metier du coaching, garde les chiffres et la structure.

**3 · Context** — les documents permanents, ceux que tout commercial doit pouvoir
ouvrir : **ICP** (le profil du client ideal, avec ses signaux de disqualification),
**offre**, **positionnement et objections**, **processus de vente**, **ton de
voix**. Chaque document ouvre une page de detail lisible.

**4 · Capabilities** — les competences et routines qui tournent.
- Huit competences : preparation d'appel, one-pager client, generation de leads,
  extraction LinkedIn, prise de contact, revue de pipeline, relance, generation de
  proposition.
- Six routines, avec leur declencheur et leur derniere execution : **routine du
  matin** (parcourt les 24 dernieres heures — agenda, courriels, appels — et met a
  jour le second cerveau), **synchronisation CRM**, **notation des appels**,
  **rapport mensuel**, **rapport trimestriel**, **metriques de campagne**.

Rends visible la difference entre ce qui se declenche seul et ce qu'on lance.

**5 · Stack** — les outils, groupes par role, comme dans `09` et `10` :
« Core and system of record » (CRM, generateur de propositions, transcription de
reunions), « Prospecting and lead-gen » (extraction, bases de leads, plateformes
de prise de contact), et les outils de travail (messagerie, agenda, tableur,
telephonie, hebergement). Chaque tuile : l'outil, son role en une ligne, son etat.

Coach OS a de vrais connecteurs — les MCP passent par un gateway unique.
Appuie-toi dessus plutot que de recopier la liste de Ben.

## L'idee de fond, a ne pas perdre

Ben le dit en une phrase : la vente, c'est **rassembler du renseignement**, puis
**agir dessus**. Presque tout le monde automatise l'action sans avoir construit le
renseignement, et les resultats sont mauvais. Le Control Center n'est pas un
tableau de bord de plus : c'est la couche qui sait, en permanence, ou en est
chaque affaire — « regenere chaque jour apres les routines du matin ».

Ce cadrage doit se sentir dans l'app : chaque page dit **d'ou vient sa donnee** et
**quand elle a ete rafraichie**.

## Le theme — la doctrine de la maison

L'app `clients` est le modele, il n'est pas negociable :

- La **barre laterale** porte l'identite de l'app (theme fige).
- Les **pages de detail** se rendent dans `AppDetailOverlay` monte en **frere**
  d'`AppFrame`, jamais dans le corps d'une section, et suivent le theme de la
  barre du haut. Lis `src/apps/clients/ClientsApp.tsx` en entier avant d'ecrire.

Un detail rendu a l'interieur d'`AppFrame` herite du theme de l'app et ne suivra
jamais la barre du haut. Cette erreur a deja ete faite et corrigee deux fois.

## Les deux chiffres durs

1. `node tools/shot.mjs --app sales` ne remonte **aucune erreur de console**.
2. **Zero classe de palette Tailwind en dur** dans `src/apps/sales`. Uniquement
   `var(--theme-text)`, `var(--theme-surface)`, `var(--panel-border)`,
   `var(--theme-muted)`. Exception : une couleur qui porte un **sens** (vert =
   gagne, rouge = perdu, orange = a relancer). L'app en porte 20 aujourd'hui :
   elles doivent disparaitre.

## Le protocole de boucle — le coeur de la tache

Pour **chaque** onglet, dans cet ordre :

1. **Construis** la section.
2. **Photographie-la** :
   `node tools/shot.mjs --app sales --section "<libelle de l'onglet>" --out /tmp/s-<onglet>.png`
   Le selecteur fonctionne sur le **libelle** affiche, pas sur l'identifiant.
3. **Juge**, avec un regard neuf, en oubliant l'effort que tu viens de fournir :
   pose ta capture a cote de l'image de reference et reponds a **une seule
   question** — laquelle des deux est la meilleure ? Pas de note sur dix : les
   notes derivent vers le haut a chaque tour. Un choix, et **le seul plus gros
   ecart restant**, nomme.
4. Si la reference gagne, **corrige cet ecart-la** et reprends au point 2.
5. Passe a l'onglet suivant seulement quand la notre gagne.

Sois dur avec toi-meme. L'eloge ne sert a rien ici. Si tu ne peux pas dire
laquelle est la meilleure, c'est que la reference gagne.

## Interdits

0. **N'invoque AUCUN workflow BMAD** (`bmad-spec`, `bmad-build-auto`,
   `bmad-advanced-elicitation`...). Le depot en contient 51 ; ils ouvrent une
   porte « [A] Approve / [E] Edit » que personne ne peut franchir — la session
   est non interactive et tu resterais bloque jusqu'au delai d'expiration.
1. Tu ne touches qu'a `src/apps/sales/`. Pas une autre app, pas
   `src/components/AppFrame.tsx`, pas `src/components/cms/AppDetailOverlay.tsx`,
   pas `tools/shot.mjs`, pas `src/lib/themes/`.
2. Tu ne crees aucune nouvelle app, tu n'inscris rien dans `app-discovery.ts`.
3. Aucune dependance nouvelle. Pas de `git commit`, pas de `git push`.
4. Tu ne supprimes aucune section existante.
5. Chemins **absolus** pour tout fichier ecrit hors du depot.

## Verification obligatoire

```
npx tsc --noEmit -p tsconfig.app.json 2>&1 | grep -c "error TS"
npm test
node tools/shot.mjs --app sales --out /tmp/sales.png
grep -rEo "\b(bg|text|border)-(white|black|stone|slate|zinc|gray|neutral)(-[0-9]+)?\b" src/apps/sales --include=*.tsx | wc -l
```

Attendu : **au plus 73**, tests verts, **0 erreur de console**, **0 classe de palette**.

## Rapport attendu

Dans
`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/RAPPORT_SALES_OS.md`.

Pour **chaque onglet** : le nombre de tours qu'il a fallu, et a chaque tour
l'ecart que le critique a nomme. C'est la partie la plus utile du rapport — elle
dit ce que la boucle a reellement corrige. Puis les chiffres de verification, les
couleurs semantiques laissees volontairement, et tout point non fait avec sa
raison.

Si tu dois t'arreter avant la fin, ecris quand meme ce rapport avec l'etat exact.
