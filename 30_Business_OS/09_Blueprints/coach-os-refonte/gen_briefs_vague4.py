# -*- coding: utf-8 -*-
"""Vague 4 : pages de detail systemiques, Legal souverainete, Welcome landing."""
import pathlib

P = pathlib.Path(__file__).parent
REPO = ("C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/"
        "05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os")

SOCLE = """
## Le depot

`%s`

React 19 - TypeScript - Tailwind v4 - Zustand - Vite.
**Reference TS : 71 erreurs. Ne la depasse pas.** `npm test` : 60 verts.

## La regle de theme — c'est le coeur de cette vague

Un seul motif est correct dans ce depot, celui de `src/apps/clients/ClientsApp.tsx` :

- La **barre laterale** porte l'identite de l'app : theme fige, choisi par l'app.
- La **page de detail** suit le theme de la **barre du haut**, celui que
  l'utilisateur change globalement.

Le mecanisme, a comprendre avant de toucher quoi que ce soit :

`AppFrame` ecrit les jetons du theme de l'app sur **son propre `div`**. Tout ce
qu'il contient en herite. `AppDetailOverlay` est monte **en frere** d'`AppFrame`,
pas dedans : il ne voit pas ces variables, retombe sur `:root`, que
`ThemeApplier` regle sur le theme global. C'est exactement ce qu'on veut.

**Consequence directe : un detail rendu dans le corps d'une section herite du
theme de l'app et ne suivra JAMAIS la barre du haut.** C'est le defaut a
corriger. Il a deja ete corrige deux fois sur d'autres apps ; le motif est connu.

La structure de retour attendue :

```tsx
return (
  <>
    <AppFrame ... sections={sections} />
    {detail ? (
      <AppDetailOverlay appId="<app>" accent={ACCENT} onBack={...}>
        <...DetailPage item={detail} onBack={...} />
      </AppDetailOverlay>
    ) : null}
  </>
);
```

Lis `ClientsApp.tsx` en entier avant d'ecrire une ligne.

## Ce qu'est une bonne page de detail

Le proprietaire du produit est explicite : les anciennes pages de detail sont
**trop basiques pour rester en l'etat**. On ne les met pas a jour, on les
**refait**. Une page de detail digne de ce nom, pour un element d'une collection :

1. **Un en-tete qui situe** — le nom, son etat, son fil d'Ariane, et la date de
   derniere mise a jour. On doit savoir *ou on est* sans lire le corps.
2. **Les attributs structures**, pas un bloc de texte : des paires
   libelle/valeur groupees par sens, lisibles en diagonale.
3. **L'historique** — ce qui s'est passe sur cet element, date par date. Un
   element sans histoire est une fiche morte.
4. **Les relations** — a quoi il est lie, et un lien pour y aller. C'est ce qui
   transforme une collection en systeme.
5. **Ce qu'on peut en faire** — les actions possibles, meme si elles ne sont pas
   toutes cablees. Une page qui ne mene nulle part est une image.

`src/apps/clients/ClientsDetailPage.tsx` est la reference vivante.

## Les deux chiffres durs

1. `node tools/shot.mjs --app <app> --out /tmp/x.png` ne remonte **aucune erreur
   de console**. Le script ouvre l'app, pose le theme, capture, et liste les
   erreurs. Le selecteur `--section` fonctionne sur le **libelle** affiche.
   **Regarde tes captures.** Le typage vert et les tests verts ne prouvent rien
   sur ce qui s'affiche : trois fois cette semaine du code casse a ete valide
   pour cette raison exacte.
2. **Zero classe de palette Tailwind en dur** dans ton perimetre :
   `bg-white`, `text-stone-900`... Uniquement `var(--theme-text)`,
   `var(--theme-surface)`, `var(--panel-border)`, `var(--theme-muted)`.
   Exception : une couleur qui porte un **sens** (vert = ok, rouge = incident,
   orange = avertissement).

## Interdits

0. **N'invoque AUCUN workflow BMAD** (`bmad-spec`, `bmad-build-auto`...). Le
   depot en contient 51 ; ils ouvrent une porte « [A] Approve » que personne ne
   peut franchir — la session est non interactive et tu resterais bloque.
1. **Ne modifie AUCUN fichier sous un dossier `_TRASH_*`.** Ce sont des archives,
   c'est le chemin de retour arriere. Un agent a vide l'une d'elles pour faire
   tomber un compteur a zero : la mesure est devenue verte parce que la preuve
   avait disparu. Les comptages excluent ces dossiers, tu n'as rien a y gagner.
2. **N'ecris jamais dans le magasin de themes** (`setAppTheme`, `setGlobalTheme`).
   Cela ecrase le choix de l'utilisateur dans Settings. Le defaut d'une app se
   declare dans `CANONICAL_APP_THEMES` (`src/lib/themes/tokens.ts`), et un choix
   explicite de l'utilisateur doit toujours gagner.
3. Tu ne touches pas a `src/components/AppFrame.tsx`, ni a
   `src/components/cms/AppDetailOverlay.tsx`, ni a `tools/shot.mjs`.
4. Aucune dependance nouvelle. Pas de `git commit`, pas de `git push`.
5. Tu ne supprimes aucune section existante.
6. Chemins **absolus** pour tout fichier ecrit hors du depot.

## Verification obligatoire

```
npx tsc --noEmit -p tsconfig.app.json 2>&1 | grep -c "error TS"
npm test
grep -rEo "\\b(bg|text|border)-(white|black|stone|slate|zinc|gray|neutral)(-[0-9]+)?\\b" src/apps/<app> --include=*.tsx | grep -v _TRASH | wc -l
```

Attendu : **au plus 71**, tests verts, **0 erreur de console**, **0 classe de
palette hors corbeille**.
""" % REPO

RAPPORT = """
## Rapport attendu

Dans `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/%s`.

Par app : la structure de retour finale, les pages de detail refaites, les
captures que tu as prises et ce que tu y as vu, les chiffres de verification, et
**tout point non fait avec sa raison**. Un point non fait et signale vaut mieux
qu'un point bacle en silence.

Si tu dois t'arreter avant la fin, ecris quand meme ce rapport avec l'etat exact.
"""

BRIEFS = {}

BRIEFS["THEME_A"] = """# BRIEF — pages de detail, groupe A : operations, product, growth, it-rd, tasks

Tu es developpeur front. **Deux agents travaillent en parallele sur des apps
differentes.** Ton perimetre exclusif : `src/apps/operations/`,
`src/apps/product/`, `src/apps/growth/`, `src/apps/it-rd/`, `src/apps/tasks/`.
Tu ne touches a aucune autre app.

## Le defaut, mesure

Ces cinq apps rendent encore un `DynamicPageView` **dans le corps d'une
section**, donc a l'interieur d'`AppFrame`. Leurs details heritent du theme de
l'app au lieu de suivre la barre du haut.

Le proprietaire le decrit ainsi : « les anciennes pages de Product et Growth
s'adaptent au theme de la sidebar mais pas les nouvelles » — c'est le meme
defaut, vu de l'autre cote.

## Ta tache

1. Fais passer **tous** les details de ces cinq apps par `AppDetailOverlay`
   monte en frere d'`AppFrame`.
2. **Refais** les pages de detail trop basiques selon les cinq points ci-dessous.
   Ne te contente pas de les deplacer : une fiche qui n'affiche qu'un titre et
   deux lignes est un echec de cette tache.
3. Verifie chaque app en capture, avec **deux themes globaux differents** (un
   clair, un sombre) : le detail doit changer, la barre laterale non.
""" + SOCLE + (RAPPORT % "RAPPORT_THEME_A.md")

BRIEFS["THEME_B"] = """# BRIEF — pages de detail, groupe B : audit, finance, people, dashboard, sales

Tu es developpeur front. **Deux agents travaillent en parallele sur des apps
differentes.** Ton perimetre exclusif : `src/apps/audit/`, `src/apps/finance/`,
`src/apps/people/`, `src/apps/dashboard/`, `src/apps/sales/`.
Tu ne touches a aucune autre app.

## Le defaut, mesure

- `audit` rend un `DynamicPageView` dans une section et **n'a aucun
  `AppDetailOverlay`** : ses details ne peuvent pas suivre la barre du haut.
- `finance` et `people` ont encore un `DynamicPageView` dans une section.
- `dashboard` et `sales` : le proprietaire signale que leurs pages de detail ne
  s'adaptent pas au theme de la barre du haut. Verifie **en capture**, sous deux
  themes globaux differents, avant de conclure — puis corrige ce que tu constates.

## Ta tache

1. Fais passer **tous** les details de ces cinq apps par `AppDetailOverlay`
   monte en frere d'`AppFrame`.
2. **Refais** les pages de detail trop basiques selon les cinq points ci-dessous.
3. Verifie chaque app en capture, avec **deux themes globaux differents** (un
   clair, un sombre) : le detail doit changer, la barre laterale non.
""" + SOCLE + (RAPPORT % "RAPPORT_THEME_B.md")

BRIEFS["LEGAL"] = """# BRIEF — l'app Legal, refaite autour de la souverainete

Tu es developpeur front. Ton perimetre exclusif : `src/apps/legal/`.

## Deux choses a faire

**1. Les anciennes pages de detail sont a refaire, pas a retoucher.** Elles
suivent deja le theme de la barre du haut — c'est le seul point acquis. Le
proprietaire les qualifie de « mega basiques ». Applique les cinq points de la
section « Ce qu'est une bonne page de detail ».

**2. Ajoute la couche souverainete.** Elle vient d'une conference d'IndyDevDan,
« Is Anthropic STEALING Your Data? ». La these, resumee sans la trahir :

> Les laboratoires de modeles ne volent pas vos donnees — leurs conditions
> l'interdisent et leurs incitations les en dissuadent. Mais ils les utilisent
> **agregees et anonymisees**, et cet agregat est une **carte du marche**. Quand
> un domaine devient rentable, ils y entrent. Vous payez deux fois : en argent,
> et en savoir-faire.

Le test qu'il propose, et qui doit apparaitre tel quel dans l'app :
**« si un concurrent pouvait lire la trace complete de mon agent, est-ce que ca
changerait quelque chose ? »**

Ajoute ces sections, en gardant les existantes :

- **Echelle de souverainete** — les six niveaux, du moins au plus souverain :
  *Niveau 0* abonnement grand public (Claude, ChatGPT) ;
  *Niveau 1* API commerciale (moins de collecte, agregat seulement) ;
  *Niveau 2* nuage de modeles (Bedrock, Vertex, Foundry — le fournisseur
  s'interpose, plus d'echantillonnage) ;
  *Niveau 3* plan de controle possede (petite machine, passerelle LLM, on possede
  toutes les traces et on change de modele a volonte) ;
  *Niveau 4* hybride prive (poids ouverts sur des GPU loues, on possede le
  modele) ; *Niveau 5* materiel possede.
  Chaque niveau : ce qu'on gagne, ce qu'on garde, ce que ca coute, et pour quelle
  taille d'organisation. **Marque le niveau ou se trouve Coach OS aujourd'hui.**
  L'auteur note lui-meme qu'il hesite sur l'ordre 2 / 3 ; garde son ordre et
  signale l'hesitation plutot que de trancher a sa place.

- **Commodite ou propriete intellectuelle** — un classement des travaux. Le
  travail de commodite (prototypes, CRUD, glue) n'a pas besoin d'etre defendu.
  Le travail d'IP — invites, traces, logique metier, evaluations construites a la
  main, donnees d'usage — est rare, asymetrique, et se cumule. Chaque entree
  porte le verdict du test de la trace.

- **Registre des dependances** — de quels modeles, fournisseurs et services
  depend l'activite, et ce qui tombe si l'un disparait. C'est du risque
  d'homme-cle, applique a la technologie.

- **Clauses et retention** — ce que disent reellement les conditions de service
  qu'on a acceptees : ce qui est conserve, combien de temps, ce qui est exclu de
  l'entrainement, et quelles classes de compte ont quelles protections. L'auteur
  insiste : les classes de clients ne sont pas egales, le commercial est mieux
  protege que le grand public.

**Ne transforme pas ceci en pamphlet.** Le ton de la source est explicitement
non alarmiste : les faits, leurs sources, et la decision laissee au lecteur.
Rends visible ce qui est **verifie** (conditions de service) et ce qui est
**speculation** — l'auteur separe les deux avec soin, fais-en autant.
""" + SOCLE + (RAPPORT % "RAPPORT_LEGAL.md")

BRIEFS["WELCOME"] = """# BRIEF — l'app Welcome, la page d'arrivee qui invite

Tu es developpeur front. Ton perimetre exclusif : `src/apps/welcome/`.

## Le principe directeur : inviter, pas convaincre

Il vient d'une conference de Tom Youngs sur le message de micro-culte. La these,
resumee sans la trahir :

> On ne convainc plus au telephone : **le contenu convertit, la conversation
> n'est plus que de l'administratif.** Sept mots coutent cher — « je dois juste y
> reflechir » — et sept mots rapportent — « peux-tu m'envoyer le lien de
> paiement ». La difference se joue avant le contact.

La distinction operatoire, celle qui doit gouverner **chaque ligne** de la page :

- **Message generique** = decrire la situation du lecteur **de l'exterieur**.
  Exemple donne : « la plupart des coachs peinent a trouver des clients ».
- **Message magnetique** = ecrire le **dialogue interieur** du lecteur, avec ses
  mots a lui. Exemple donne : « j'en ai assez d'envoyer cent messages par jour
  pour m'entendre dire *je dois juste y reflechir* ».

Sa formule : **« ton mot est ton sifflet »** — les bons mots agissent comme un
sifflet a ultrasons, inaudible pour les autres, evident pour le client ideal.

Le cadre en trois temps, a incarner dans la structure de la page :

1. **Repousser** — par le langage interieur. Ce n'est pas de la qualification
   commerciale, c'est ecarter ceux pour qui l'offre n'est pas faite. Une page qui
   ne repousse personne n'attire personne.
2. **Dissoudre** — les peurs, pas les objections. Une objection est toujours la
   meme chose deguisee : le lecteur ne croit pas qu'il obtiendra le resultat.
   Montre que ca marche, ne l'affirme pas.
3. **Inviter** — depuis le pied arriere. « Alors, on y va ? » et on rend la main.
   Jamais de pression, jamais de compte a rebours, jamais d'urgence fabriquee.

**Ce que ca interdit** : les formules qui decrivent le lecteur de l'exterieur,
les preuves sociales sans substance, les appels a l'action pressants. Si une
phrase pourrait figurer sur n'importe quelle page de n'importe quel concurrent,
elle est generique : reecris-la de l'interieur.

## L'inspiration visuelle

Un serveur MCP **Mobbin** vient d'etre ajoute a la passerelle. S'il repond, sers-
t'en pour chercher des references de pages d'arrivee. **S'il ne repond pas** —
son autorisation est interactive et n'a peut-etre pas encore ete faite —
**ne bloque pas, ne le mentionne pas comme un echec bloquant** : construis avec
ton jugement et signale-le dans ton rapport.

## Ta tache

Refais la page d'arrivee de `welcome` selon ce cadre. Elle est integree au bureau
web, ce n'est pas un site separe : elle vit dans une fenetre d'app, avec la barre
laterale qui liste ses pages.

`welcome` porte **74 classes de palette en dur**, le pire score du depot. Elles
doivent disparaitre — l'app doit suivre le theme.
""" + SOCLE + (RAPPORT % "RAPPORT_WELCOME.md")

for cle, texte in BRIEFS.items():
    f = P / ("BRIEF_V4_%s.md" % cle)
    f.write_text(texte, encoding="utf-8")
    print("%-24s %6d caracteres" % (f.name, len(texte)))
