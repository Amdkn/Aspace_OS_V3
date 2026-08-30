# BRIEF — app Dashboard, vague V3 : les 4 pages de plateforme

Tu es developpeur front. Tu ecris **un module de sections autonome** pour l'app
`dashboard` de Coach OS, d'apres l'Enterprise OS de Mark Kashef.

## Cloisonnement — lis ceci en premier

Trois agents travaillent sur cette app **en meme temps**. Pour qu'ils ne se
marchent pas dessus, chacun ecrit dans son dossier et **aucun ne touche a
`DashboardApp.tsx`** : le raccordement est fait ensuite, par l'orchestrateur.

**Ton perimetre exclusif : `src/apps/dashboard/platform/`**

Tu y crees un `index.ts` qui exporte :

```ts
export const PLATFORM_SECTIONS: AppSection[] = [ ... ];
```

Le type `AppSection` vient de `src/components/AppFrame.tsx` — importe-le, ne le
redefinis pas. Regarde comment `DashboardApp.tsx` construit son tableau de
sections aujourd'hui et produis exactement la meme forme : `{ id, label, icon,
render }`. Tes donnees de demonstration vont dans
`src/apps/dashboard/platform/seed.ts`.

**Si tu edites `DashboardApp.tsx`, tu casses le travail de deux autres agents.**

## Le depot

`C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os`

React 19 - TypeScript - Tailwind v4 - Zustand - Vite.
**Reference TS : 75 erreurs preexistantes. Ne la depasse pas.** `npm test` : 60 verts.

## La barre — regarde-la, ne l'imagine pas

`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/barre-jarvis/pages/`

26 images pleine resolution extraites de la video de Mark. Pour toi : `17-integrations.png`, plus les images `z-*` de la seconde moitie de la video.
`06-chat-sidebar-complete.png` montre la barre laterale entiere et lisible.

**Ouvre ces images.** Un agent qui juge sur une description approuve tout — c'est
le mode d'echec numero un de cette methode, dit tel quel par ses auteurs.

## Le fond — les chiffres sont donnes, ne les invente pas

`C:/Users/amado/Downloads/Enterprise_OS_Blueprint_Kit (1)/BLUEPRINT.md`

Document de Mark. Il fixe : **42 coupe-circuits**, **9 motifs DLP** (7 bloquants,
2 avertissements), **~31 tables**, **6 seaux**, **3 cles**, **15 piles**,
**5 roles**, **4 paliers**.

**Adaptation obligatoire.** Coach OS ne tourne pas sur AWS. Tu transposes :
Bedrock vers les modeles reellement utilises ici (Claude Opus/Sonnet/Haiku,
MiniMax-M3, modeles ouverts) ; DynamoDB et S3 vers Supabase ; IAM vers les 5
roles. Les donnees affichees sont de demonstration, credibles pour un cabinet de
coaching. La **structure** est celle de Mark.

## Tes sections

1. **Integrations** — la grille des connecteurs, comme dans
   `17-integrations.png` : une tuile par outil, son etat (`connecte / disponible
   / indisponible`), et ce a quoi il donne acces. Coach OS en a de vrais : les
   MCP passent tous par un gateway unique. Appuie-toi sur ce qui existe plutot
   que d'inventer un catalogue.

2. **Knowledge** — le depot de documents et leur cycle : depose, extrait,
   decoupe, vectorise, interrogeable. Chaque entree porte son etat dans ce cycle.
   On doit pouvoir poser une question a un document, voir la reponse **et sa
   source**.

3. **Memories** — la memoire longue et son hygiene. Chaque souvenir : le fait
   retenu, sa provenance, sa date, son statut (`confirme / contredit / a
   verifier`) et son poids. Une couche partagee entre agents — la ruche — et une
   couche propre a chaque agent. La memoire brute est un depotoir ; ce qui compte
   est ce qui a ete verifie.

4. **Members** — l'equipe et ses roles. **Cinq roles, du plus faible au plus
   fort : viewer, analyst, operator, admin, owner.** Chaque personne : son role,
   ce qu'il lui ouvre, sa derniere activite. Le principe a rendre visible :
   l'interface ne fait que masquer des onglets, **l'autorite est au serveur**.
   Chaque changement de privilege est attribue a une personne reelle.

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
1. Tu ne touches qu'a `src/apps/dashboard/platform/`. **Ni `DashboardApp.tsx`**, ni le dossier d'une autre vague. Pas une autre app, pas
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


## Verification obligatoire

```
npx tsc --noEmit -p tsconfig.app.json 2>&1 | grep -c "error TS"
npm test
grep -rEo "\b(bg|text|border)-(white|black|stone|slate|zinc|gray|neutral)(-[0-9]+)?\b" src/apps/dashboard/platform --include=*.tsx | wc -l
```

Attendu : **au plus 75**, tests verts, **0 classe de palette**.

Tes sections ne sont pas encore raccordees a l'app — c'est voulu, le raccordement
vient apres. Tu ne peux donc pas les photographier toi-meme. Rends un code qui
compile et dont chaque section affiche quelque chose de structure.

## Rapport attendu

Ecris-le dans
`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/RAPPORT_DASHBOARD_V3.md`.

Il contient : les sections livrees avec leur `id`, les fichiers crees, le nom
exact de la constante exportee, les chiffres de verification, les couleurs
semantiques laissees volontairement avec leur raison, et **tout point non fait
avec sa raison**. Un point non fait et signale vaut mieux qu'un point bacle en
silence.

Si tu dois t'arreter avant la fin, ecris quand meme ce rapport avec l'etat exact.
