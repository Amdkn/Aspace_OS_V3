# BRIEF — l'app Welcome : dix pages d'arrivee, dix designs differents

Tu es developpeur front. Ton perimetre exclusif : `src/apps/welcome/`.
Tu ne touches a aucune autre app.

Une premiere version de ce brief a ete lancee puis **arretee** : elle ne disait
pas ce qui suit. Ce document la remplace entierement.

## Ce qui ne va pas aujourd'hui

L'app `welcome` porte dix pages d'arrivee dans sa barre laterale — Arrivee,
OMK RH, OMK Operations, OMK Growth, OMK Cognition, OMK People, OMK Finance,
OMK IT, OMK Legal, OMK Coach Demo.

**Elles ont toutes exactement la meme structure de sections** : Top, Trusted by,
Features, By the numbers, Testimonials, Pricing, FAQ, Get started. Seul le texte
change. C'est un gabarit rempli dix fois, pas dix pages.

Le proprietaire du produit est clair : **chaque page doit etre unique et
speciale.** Une page d'exploitation ne ressemble pas a une page de finance, qui
ne ressemble pas a une page juridique. Le rythme, l'ordre des sections, la
densite, la place de l'image, le type de preuve : tout doit differer. Deux pages
qui se ressemblent sont un echec de cette tache.

## La regle de theme — Welcome est un cas a part, lis bien

Dans toutes les autres apps, la barre laterale porte l'identite de l'app et la
**page de detail** suit le theme de la barre du haut. Welcome **n'a pas de pages
de detail** : ses pages d'arrivee *sont* le contenu principal.

Donc, pour cette app et pour elle seule :

- la **barre laterale** garde l'identite de l'app, comme partout ;
- le **contenu de la page** suit le **theme de la barre du haut**.

Aujourd'hui il ne le fait pas : le contenu est rendu dans le corps d'une section,
donc a l'interieur d'`AppFrame`, qui ecrit les jetons du theme de l'app sur son
propre `div`. Tout ce qu'il contient en herite.

**La correction.** Le conteneur du contenu doit **reappliquer les jetons du theme
global sur lui-meme**. `src/lib/themes/store.ts` expose deja tout le necessaire :

```ts
import { useThemeStore, applyThemeTokens } from '../../lib/themes/store';
import { THEMES } from '../../lib/themes/tokens';

const globalTheme = useThemeStore((s) => s.globalTheme);   // LECTURE seule
const ref = useRef<HTMLDivElement>(null);
useEffect(() => {
  if (ref.current) applyThemeTokens(ref.current, THEMES[globalTheme] ?? THEMES['warm-paper']);
}, [globalTheme]);
```

Trois pieges, chacun deja paye dans ce depot :

1. **Selectionne un scalaire, jamais un objet ni un tuple.** Un selecteur Zustand
   qui construit une nouvelle valeur a chaque appel renvoie une reference
   differente a chaque rendu ; `useSyncExternalStore` compare par identite,
   conclut que l'etat a change, et reboucle. Une app a plante au montage pour
   cette raison exacte, avec 60 tests verts.
2. **N'ECRIS JAMAIS dans le magasin de themes** — ni `setAppTheme`, ni
   `setGlobalTheme`. Cela ecrase le choix de l'utilisateur dans Settings. Un
   agent l'a fait hier ; il a fallu l'annuler.
3. Les variables CSS heritent **vers le bas**, jamais lateralement. Poser les
   jetons sur le conteneur suffit : tous ses descendants suivent.

**Verifie en capture, sous deux themes globaux opposes** (un clair, un sombre) :
le contenu doit changer entierement, la barre laterale ne doit pas bouger.

## Le principe editorial : inviter, pas convaincre

Il vient d'une conference de Tom Youngs sur le message de micro-culte.

> Le contenu convertit, la conversation n'est plus que de l'administratif. Sept
> mots coutent cher — « je dois juste y reflechir » — et sept mots rapportent —
> « peux-tu m'envoyer le lien de paiement ». Tout se joue avant le contact.

La distinction qui gouverne **chaque ligne** que tu ecris :

- **Generique** = decrire la situation du lecteur **de l'exterieur**. Son
  exemple : « la plupart des coachs peinent a trouver des clients ».
- **Magnetique** = ecrire le **dialogue interieur** du lecteur, avec ses mots.
  Son exemple : « j'en ai assez d'envoyer cent messages par jour pour m'entendre
  dire *je dois juste y reflechir* ».

Sa formule : **« ton mot est ton sifflet »** — inaudible pour les autres, evident
pour celui a qui l'offre est destinee.

Le cadre en trois temps, a incarner dans la **structure** de chaque page :

1. **Repousser** par le langage interieur. Une page qui ne repousse personne
   n'attire personne. Dis explicitement pour qui ce n'est pas.
2. **Dissoudre** les peurs, pas les objections. Une objection est toujours la
   meme chose deguisee : le lecteur ne croit pas qu'il obtiendra le resultat.
   Montre que ca marche, ne l'affirme pas.
3. **Inviter** depuis le pied arriere. « Alors, on y va ? », et on rend la main.
   Jamais de compte a rebours, jamais d'urgence fabriquee, jamais de pression.

**Interdit editorial** : toute phrase qui pourrait figurer sur la page d'un
concurrent sans changer un mot. Si tu peux remplacer le nom du produit et que la
phrase tient encore, elle est generique — reecris-la de l'interieur.

La page « Arrivee » actuelle fait deja cela correctement (« Encore un *je dois
juste y reflechir* cette semaine ? »). **C'est le niveau a tenir sur les dix.**

## L'inspiration visuelle

`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/barre-welcome/`

Captures de galeries reelles : Lapa Ninja, Dribbble, Awwwards, One Page Love.
Des dizaines de mises en page differentes par image. **Ouvre-les.** Sers-t'en
pour varier les structures — pas pour copier une maquette, mais pour voir a quel
point deux pages d'arrivee peuvent etre differentes.

Tu peux en capturer d'autres toi-meme :

```
node tools/shot.mjs --url "https://www.lapa.ninja/" --out /tmp/ref.png --full
```

## Le protocole de boucle — le coeur de la tache

Pour **chaque page**, dans cet ordre :

1. **Construis** la page, avec sa structure propre.
2. **Photographie-la** :
   `node tools/shot.mjs --app welcome --section "<libelle de la page>" --out /tmp/w.png`
   Le selecteur fonctionne sur le **libelle** affiche, pas sur l'identifiant.
3. **Juge**, contexte neuf, en oubliant l'effort que tu viens de fournir. Deux
   questions, deux seulement :
   - **Est-ce que cette page ressemble aux precedentes ?** Si oui, elle a echoue.
   - Posee a cote d'une reference de galerie, **laquelle des deux tiendrait mieux
     la comparaison ?** Un choix binaire, pas une note sur dix : les notes
     derivent vers le haut a chaque tour.
4. Nomme **le seul plus gros ecart**, corrige-le, reprends au point 2.
5. Page suivante seulement quand la notre gagne.

Sois dur. L'eloge ne sert a rien ici.

## Le depot

`C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os`

React 19 - TypeScript - Tailwind v4 - Zustand - Vite.
**Reference TS : 71 erreurs. Ne la depasse pas.** `npm test` : 60 verts.

## Les deux chiffres durs

1. `node tools/shot.mjs --app welcome` ne remonte **aucune erreur de console**.
   **Regarde tes captures.** Le typage vert et les tests verts ne prouvent rien
   sur ce qui s'affiche : trois fois cette semaine du code casse a ete valide
   pour cette raison exacte.
2. `welcome` porte **74 classes de palette Tailwind en dur**, le pire score du
   depot. Elles doivent tomber a **zero** : c'est ce qui empeche l'app de suivre
   le theme. Uniquement `var(--theme-text)`, `var(--theme-surface)`,
   `var(--panel-border)`, `var(--theme-muted)`. Exception : une couleur qui porte
   un **sens**.

## Interdits

0. **N'invoque AUCUN workflow BMAD** (`bmad-spec`, `bmad-build-auto`...). Le
   depot en contient 51 ; ils ouvrent une porte « [A] Approve » que personne ne
   peut franchir — la session est non interactive et tu resterais bloque.
1. **Ne modifie AUCUN fichier sous un dossier `_TRASH_*`.** Ce sont des archives.
   Un agent en a vide une pour faire tomber un compteur a zero : la mesure est
   devenue verte parce que la preuve avait disparu. Les comptages excluent ces
   dossiers, tu n'as rien a y gagner.
2. **N'ecris jamais dans le magasin de themes.** Voir plus haut.
3. Tu ne touches pas a `src/components/AppFrame.tsx`, ni a `tools/shot.mjs`,
   ni a `src/lib/themes/`.
4. Aucune dependance nouvelle. Pas de `git commit`, pas de `git push`.
5. Tu ne supprimes aucune page de la barre laterale. Il y en a dix, il en reste
   dix.
6. Chemins **absolus** pour tout fichier ecrit hors du depot.

## Verification obligatoire

```
npx tsc --noEmit -p tsconfig.app.json 2>&1 | grep -c "error TS"
npm test
node tools/shot.mjs --app welcome --out /tmp/welcome.png
grep -rEo "\b(bg|text|border)-(white|black|stone|slate|zinc|gray|neutral)(-[0-9]+)?\b" src/apps/welcome --include=*.tsx | grep -v _TRASH | wc -l
```

Attendu : **au plus 71**, tests verts, **0 erreur de console**, **0 classe de
palette hors corbeille**.

## Rapport attendu

Dans `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/RAPPORT_V4_WELCOME.md`.

**Un tableau des dix pages**, avec pour chacune : l'ordre de ses sections, ce qui
la rend differente des neuf autres, le nombre de tours de boucle, et l'ecart
nomme a chaque tour. C'est la partie la plus utile — elle dit si la boucle a
vraiment corrige quelque chose ou si elle s'est approuvee au premier passage.

Puis les chiffres de verification, la preuve que le contenu suit la barre du haut
(deux captures, deux themes), les couleurs semantiques laissees volontairement,
et **tout point non fait avec sa raison**.

Si tu dois t'arreter avant la fin, ecris quand meme ce rapport avec l'etat exact.
