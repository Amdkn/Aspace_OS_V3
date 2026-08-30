# BRIEF — l'app Dashboard devient le poste de pilotage Enterprise (vague 1)

Tu es developpeur front. Tu refais **une seule app** : `dashboard`. Tu lui ajoutes
les pages de l'Enterprise OS de Mark Kashef, adaptees a la realite de Coach OS.

Le proprietaire du produit a ete explicite : **toutes ces pages vont dans l'app
Dashboard, exclusivement.** Tu ne crees aucune nouvelle app.

## Le depot

`C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os`

React 19 · TypeScript · Tailwind v4 · Zustand · Vite.
**Reference TS : 75 erreurs preexistantes. Ne la depasse pas.** `npm test` : 60 verts.

## La barre — regarde-la, ne l'imagine pas

`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/barre-jarvis/pages/`

26 images pleine resolution extraites de la video de Mark. Les utiles ici :

| Image | Ce qu'elle montre |
|---|---|
| `02-overview.png` | La page d'accueil : bandeau TLDR, 4 cartes de chiffres, ligne de sante, 3 boutons d'action, colonne Agents + colonne Recent Sessions |
| `03-agents-grille.png` | La grille de fiches d'agents |
| `04-agent-fiche-onglets.png` | La fiche d'un agent et ses onglets |
| `05-agent-connections.png` | Le branchement Telegram / Slack |
| `06-chat-sidebar-complete.png` | **La barre laterale entiere, lisible** — les trois groupes et leurs entrees |
| `07-playground-multimodele.png` | La comparaison multi-modeles, puces par fournisseur |
| `08-jarvis-orbe.png` | Jarvis : l'orbe, les suggestions, les routines |
| `09-sessions.png` · `10-usage-billing.png` · `11-cost-spend.png` · `12-cost-repartition.png` · `13-audit-log.png` | Les quatre pages d'exploitation |

**Ouvre ces images.** Un critique qui juge sur une description approuve tout —
c'est le mode d'echec numero un de cette methode, dit tel quel par ses auteurs.

## Le fond — les chiffres sont donnes, ne les invente pas

`C:/Users/amado/Downloads/Enterprise_OS_Blueprint_Kit (1)/BLUEPRINT.md`

C'est le document de Mark. Il fixe : **42 coupe-circuits**, **9 motifs DLP** (7
bloquants : cles AWS, en-tetes de cle d'API, cles privees PEM, jetons Slack, PAT
GitHub, cartes bancaires, numeros SSN — 2 avertissements : chaines en forme de
cle secrete AWS, JWT), **~31 tables**, **6 seaux**, **3 cles**, **15 piles**,
**5 roles** (viewer, analyst, operator, admin, owner), **4 paliers**.

L'ordre du goulot d'etranglement, a respecter partout ou tu l'affiches :
`limite de debit -> chargement de l'agent -> coupe-circuit modele -> plafond de
cout (echoue ferme) -> commutateur d'outil -> garde-fou -> boucle de conversation
-> repartition des outils -> analyse DLP -> journal`.

**Adaptation obligatoire.** Coach OS ne tourne pas sur AWS. Tu transposes :
Bedrock -> les modeles reellement utilises ici (Claude Opus/Sonnet/Haiku,
MiniMax-M3, modeles ouverts) ; DynamoDB/S3 -> Supabase ; IAM -> les 5 roles.
Les donnees affichees sont des donnees de demonstration credibles, dans un
fichier `seed.ts` a part. La **structure** est celle de Mark ; les **chiffres
d'exploitation** sont plausibles pour un cabinet de coaching.

## Les 9 sections de cette vague

Tu **gardes** les 4 sections actuelles (Overview, CEO Cockpit, Wind Direction,
Client Pipeline) — Overview est refondue, les 3 autres restent intactes.

**CORE**
1. **Overview** — bandeau TLDR d'une phrase (« la depense du jour est X, en
   baisse de Y%, avec 3 agents actifs sur 5 »), puis 4 cartes : depense du jour
   avec sa micro-courbe, agents actifs, sessions sur 24 h, coupe-circuits. Puis
   une ligne de sante (`1 agent en bonne sante · 291 msg / 0 err (24 h)`), trois
   boutons, et deux colonnes : Agents / Sessions recentes.
2. **Agents** — la grille de fiches. Chaque fiche ouvre un detail a onglets :
   invite systeme, conversation, sessions, memoires, connexions, reglages.
3. **Chat** — conversation avec un agent choisi, avec son etat vide soigne.
4. **Playground** — la meme question envoyee a plusieurs modeles, reponses cote
   a cote, cout par appel. Puces groupees par fournisseur.
5. **Jarvis** — le copilote **en lecture seule**. Il lit l'etat, il explique, il
   ne change rien. Coach OS a deja `src/lib/voiceCommands.ts` et
   `voiceIntent.ts`, et un bouton VOIX dans la barre du haut : **branche-toi
   dessus, n'ecris pas un second systeme de voix.** Rends visible que l'ecriture
   est bloquee — c'est le point que Mark insiste le plus.

**OPERATIONS**
6. **Sessions** — le tableau des sessions passees, filtrables.
7. **Usage** — consommation et facturation, plafond journalier, projection.
8. **Cost** — depense a date, projection de fin de mois, mois precedent, et un
   bandeau rouge **quand le budget est depasse** (cf. `11-cost-spend.png`). Plus
   la repartition « ou part l'argent » (cf. `12-cost-repartition.png`).
9. **Audit Log** — le journal en ajout seul. Chaque ligne : horodatage, acteur,
   action, entite. Rien n'y est modifiable.

## Le theme — la doctrine de la maison

L'app `clients` est le modele et il n'est pas negociable :

- La **barre laterale** porte l'identite de l'app (theme fige).
- Les **pages de detail** suivent le theme de la barre du haut : elles se rendent
  dans `AppDetailOverlay` monte en **frere** d'`AppFrame`, jamais dans le corps
  d'une section. Lis `src/apps/clients/ClientsApp.tsx` en entier avant d'ecrire.

Un detail rendu a l'interieur d'`AppFrame` herite du theme de l'app et ne suivra
jamais la barre du haut. Cette erreur a deja ete faite et corrigee deux fois.

## Les deux chiffres durs

1. `node tools/shot.mjs --app dashboard` ne doit remonter **aucune erreur de
   console**. Le script les affiche en fin de sortie.
2. **Zero classe de palette Tailwind en dur** dans `src/apps/dashboard` :
   `bg-white`, `text-stone-900`, `border-stone-100`... Uniquement
   `var(--theme-text)`, `var(--theme-surface)`, `var(--panel-border)`,
   `var(--theme-muted)`. Exception : une couleur qui porte un **sens** (vert =
   sain, rouge = incident ou depassement, orange = avertissement).

La capture d'aujourd'hui montre les fiches du pipeline **blanches sur fond
sombre**. C'est exactement cette dette. Elle doit disparaitre.

## L'outil de capture — tu t'en sers, c'est l'interet du dispositif

```
node tools/shot.mjs --app dashboard --theme cyberpunk --out /tmp/x.png
node tools/shot.mjs --app dashboard --section cost --out /tmp/cost.png
```

Il ouvre l'app, pose le theme, capture, et **liste les erreurs de console**.
Il exige que le serveur de dev tourne (`http://localhost:5173`) et que
`window.__coachos` existe (pose par `src/stores/shell.store.ts`, en DEV seul).

**Tu regardes tes captures.** Trois fois cette semaine, du code casse a ete
valide parce qu'on avait verifie la plomberie au lieu du rendu. Le typage vert
et les tests verts ne prouvent rien sur ce qui s'affiche.

## Interdits

0. **N'invoque AUCUN workflow BMAD** (`bmad-spec`, `bmad-build-auto`,
   `bmad-advanced-elicitation`...). Le depot en contient 51 ; ils ouvrent une
   porte « [A] Approve / [E] Edit » que personne ne peut franchir — la session
   est non interactive et tu resterais bloque jusqu'au delai d'expiration. Tu
   implementes directement.
1. Tu ne touches qu'a `src/apps/dashboard/`. Pas une autre app, pas
   `src/components/AppFrame.tsx`, pas `src/components/cms/AppDetailOverlay.tsx`,
   pas `src/stores/shell.store.ts`, pas `tools/shot.mjs`.
2. Tu ne crees **aucune nouvelle app** et tu n'inscris rien dans
   `src/lib/app-discovery.ts`.
3. Aucune dependance nouvelle. Pas de `git commit`, pas de `git push`.
4. Tu ne supprimes aucune section existante.
5. Chemins **absolus** pour tout fichier ecrit hors du depot. Un brief a chemin
   relatif a deja fait ecrire des agents dans des depots en lecture seule.

## Verification obligatoire

```
npx tsc --noEmit -p tsconfig.app.json 2>&1 | grep -c "error TS"
npm test
node tools/shot.mjs --app dashboard --out /tmp/verif.png
grep -rEo "\b(bg|text|border)-(white|black|stone|slate|zinc|gray|neutral)(-[0-9]+)?\b" src/apps/dashboard --include=*.tsx | wc -l
```

Attendu : **<= 75**, tests verts, **0 erreur de console**, **0 classe de palette**.

## Rapport attendu

Ecris-le dans
`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/RAPPORT_DASHBOARD_V1.md`.

Il contient : les sections livrees, les fichiers crees, les quatre chiffres de
verification, la liste des couleurs semantiques que tu as **volontairement**
laissees avec leur raison, et **tout point non fait avec sa raison**. Un point
non fait et signale vaut mieux qu'un point bacle en silence.

Si tu dois t'arreter avant la fin, ecris quand meme ce rapport avec l'etat exact.
