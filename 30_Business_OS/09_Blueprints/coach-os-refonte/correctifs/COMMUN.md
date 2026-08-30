# Socle commun aux cinq correctifs QA

Ce bloc est repris en tête de chaque brief. Il ne se discute pas.

## Le dépôt

```
C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os
```

Branche `main`, HEAD `df6941b`. Tu travailles directement dedans.

## Quatre agents travaillent en parallèle sur le même arbre

**Tu ne touches qu'aux fichiers listés dans ton périmètre.** Un fichier hors périmètre
appartient à un autre agent : le modifier écrase son travail sans que ni lui ni toi ne le
voyiez. C'est arrivé lors de la campagne précédente.

Corollaire mesuré la dernière fois : **les compteurs d'erreurs TypeScript que tu lis pendant
que les autres écrivent sont faux.** Quatre agents ont rapporté « 94 erreurs » et « 83
erreurs » en mesurant chacun les éditions en vol des trois autres. Ne rapporte pas un
chiffre global de typage. Rapporte uniquement : « `npx tsc -b` ne signale aucune erreur
**dans mes fichiers** », ou la liste des erreurs qui portent sur tes fichiers.

## Vérifier veut dire regarder

Un correctif visuel se prouve par une capture, jamais par la lecture du code.

```bash
node tools/shot.mjs --app <app> --section "<Section>" --theme <theme> --out <chemin.png>
```

L'outil pose le thème dans `localStorage`, ouvre l'app, capture, **et liste les erreurs de
console**. Si tu ne peux pas produire la capture qui montre le défaut disparu, ton correctif
n'est pas vérifié — dis-le, ne le maquille pas.

Le serveur de dev tourne déjà sur `http://localhost:5173`. Ne le relance pas, ne le tue pas.

## Interdits

1. **Aucune suppression de fichier.** Rien dans `_TRASH_*`, rien d'archivé, rien de « mort ».
   Un agent a vidé une archive de 184 lignes pour faire tomber un compteur à zéro. Si un
   compteur te gêne, le compteur a tort ou ton périmètre est mal compris — tu le signales,
   tu ne le forces pas.
2. **Aucun `setAppTheme` appelé au montage d'un composant.** Ça écrase le choix que
   l'utilisateur a fait dans Settings, à chaque ouverture. Le thème d'une app se déclare
   dans `CANONICAL_APP_THEMES` (`src/lib/themes/tokens.ts`), et seul l'utilisateur le change.
3. **Aucune modification de `CANONICAL_APP_THEMES`** sauf si ton brief te le demande
   nommément.
4. **Aucun `npm install`**, aucun ajout de dépendance, aucune régénération de verrou.
   Le déploiement Vercel vient d'être réparé sur ce point précis ; un verrou touché le
   recasse.
5. **Aucun commit, aucun push.** L'orchestrateur commite.

## Une erreur de diagnostic à ne pas reproduire

Le rapport QA C conclut que « le canvas de Finance / Growth / Product / Legal / Audit ne suit
pas le thème global » et qualifie ça de défaut systémique.

**C'est faux, et c'est une fonctionnalité.** `CANONICAL_APP_THEMES` attribue à chaque app son
thème de domaine : `finance → trust`, `growth → vibrant-block`, `product → brutalism`,
`legal → trust`, `audit → glassmorphism`. Ces cinq thèmes sont `lightMode: true`. Une app en
thème clair sous un thème global sombre, **c'est le comportement voulu** — l'utilisateur a
explicitement demandé de pouvoir régler ce thème par app depuis Settings.

Ne « corrige » pas ça. Ce qui se corrige, c'est le **contraste à l'intérieur** d'un thème :
un titre gris foncé sur fond gris foncé est illisible dans son propre thème, et ça, c'est un
vrai défaut.

## Rapport

Tu écris ton rapport dans le fichier indiqué par ton brief, **même si tu t'arrêtes en cours
de route**. Un rapport partiel qui dit où tu en es vaut infiniment mieux que rien.

Structure :

| défaut (repris du rapport QA) | cause trouvée | fichier:ligne | correctif | capture avant | capture après |

Puis une section **« ce que je n'ai pas corrigé, et pourquoi »**. Elle n'est pas
optionnelle : un défaut que tu laisses en silence coûte plus cher qu'un défaut annoncé.
