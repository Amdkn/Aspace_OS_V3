# BRIEF QA D — chercher les defauts, ne rien reparer

Tu es testeur. **Tu ne corriges rien.** Tu cherches, tu prouves, tu rapportes.
Un agent qui repare pendant qu'il teste finit par declarer sain ce qu'il vient
de toucher.

**Tes apps : `marketplace`, `onboarding`, `ontology`, `cognition`.**
Quatre testeurs travaillent en parallele sur des groupes disjoints. Tu ne
regardes que les tiennes.

## Le depot

`C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os`

Le serveur de dev tourne deja sur `http://localhost:5173`. Ne le relance pas.

## Ton outil

```
node tools/shot.mjs --app <app> --out /tmp/x.png
node tools/shot.mjs --app <app> --theme <theme> --section "<libelle>" --out /tmp/x.png
```

Il ouvre l'app, pose le theme, capture, **et liste les erreurs de console**.
Le selecteur `--section` fonctionne sur le **libelle affiche**, pas sur
l'identifiant : `--section "Kill Switches"`, pas `--section kill-switches`.

Themes disponibles (`src/lib/themes/tokens.ts`) : `warm-paper`, `dark-oled`,
`cyberpunk`, `editorial`, `brutalism`, `claymorphism`, `glassmorphism`,
`liquid-glass`, `neumorphism`, `trust`, `vibrant-block`, `aurora`.

## Ce que tu dois faire, app par app

1. **Capture chaque section** de la barre laterale. Pas un echantillon : toutes.
2. **Sous deux themes globaux opposes** — un clair (`warm-paper`) et un sombre
   (`dark-oled`). C'est la que sortent les defauts de contraste.
3. **Ouvre les captures et regarde-les.** C'est tout le travail. Une section
   declaree saine sans capture ouverte ne compte pas.
4. **Note les erreurs de console** que l'outil remonte.

## Ce qui est un defaut

- **Texte illisible** : contraste insuffisant, ou couleur qui disparait sur le
  fond du theme.
- **Debordement ou troncature** : un chiffre coupe par le bord de sa carte, un
  libelle qui deborde, une colonne qui sort de l'ecran.
- **Chevauchement** : deux elements l'un sur l'autre.
- **Zone vide** : une section qui n'affiche rien, ou « bientot disponible ».
- **Incoherence de theme** : un fragment qui ne suit pas le theme alors que ses
  voisins le suivent.
- **Erreur de console**, quelle qu'elle soit.
- **Interaction morte** : une carte qui annonce un detail et n'ouvre rien.

## Ce qui n'est PAS un defaut

- Un choix esthetique que tu n'aimes pas. Tu n'es pas designer.
- Une couleur semantique — vert = ok, rouge = incident, orange = avertissement —
  qui ne suit pas le theme : c'est voulu.
- Les previsualisations de theme dans `settings` et `design`, qui affichent
  volontairement les couleurs d'AUTRES themes.
- Un contenu de demonstration que tu trouves invraisemblable.

**Ne remplis pas ton rapport.** Dix defauts reels valent mieux que cinquante
remarques. Un rapport qui signale tout ne signale rien.

## Interdits

0. **Aucun workflow BMAD** : ils ouvrent une porte « [A] Approve » infranchissable
   en session non interactive.
1. **Tu ne modifies AUCUN fichier du depot.** Ni correction, ni refactor, ni
   « petit ajustement au passage ». Lecture seule.
2. Pas de `git commit`, pas de `git push`, pas de `npm install`.
3. Tu ne touches a aucune app hors de ton groupe.
4. Chemins absolus hors depot. Ecris tes captures dans
   `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/qa/D/`.

## Rapport

`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/RAPPORT_QA_D.md`

**Un tableau, une ligne par defaut**, trie du plus grave au plus benin :

| app | section | theme | gravite | ce qui ne va pas | capture |

`gravite` : `bloquant` (on ne peut pas s'en servir) · `visible` (ca se voit et ca
decredibilise) · `mineur` (a corriger un jour).

Chaque ligne doit porter **le chemin de la capture qui le prouve**. Une ligne
sans preuve est une opinion.

Puis, a la fin :

- **La liste des sections que tu as capturees et jugees saines** — pour qu'on
  sache ce qui a ete regarde, pas seulement ce qui a echoue.
- **Ce que tu n'as pas pu tester, et pourquoi.** Une section dont tu n'as pas
  trouve le libelle, un detail que tu n'as pas su ouvrir : dis-le. Un point non
  teste et signale vaut mieux qu'un point declare sain sans preuve.

Si tu dois t'arreter avant la fin, ecris quand meme ce rapport avec l'etat exact.
