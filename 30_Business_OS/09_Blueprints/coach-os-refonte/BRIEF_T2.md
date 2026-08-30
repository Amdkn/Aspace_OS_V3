# BRIEF T2 — Memoire, graphe et runtime

Tu es un technicien d'analyse. Tu lis des transcripts de conferences et tu
en extrais de quoi refondre l'architecture d'information de trois apps.

## Le produit qu'on refond

**Coach OS** est un shell type « OS de bureau » dans le navigateur : des fenetres
deplacables, un dock, et 19 apps metier montees dans ces fenetres. React 19,
TypeScript, Tailwind v4, Zustand.

Chaque app a une **barre laterale de sections**, et chaque section ouvre une
**page de detail**. C'est cette structure qu'on veut refondre.

Etat actuel des trois apps visees, mesure sur le depot :

| app | sections aujourd'hui |
|---|---|
| **people** | Overview · Team · Agents · Squads · Content · Cadence · Culture |
| **operations** | Runbooks · Knowledge Base · Incidents |
| **it-rd** | Kernel · Experiments · Deploys |

`operations` et `it-rd` n'ont que **trois sections chacune**. C'est le probleme :
des coquilles generiques dans un projet qui se veut ambitieux. On ne cherche pas
a les decorer, on cherche a leur donner une **architecture d'information** qui
porte un vrai modele de travail.

## Ce qu'on cherche dans ces videos

Pas des resumes. Des **primitives reutilisables** : un concept nomme, defini en
une phrase, qu'on peut transformer en section de barre laterale, en bloc de page
de detail, ou en objet du modele de donnees.

Exemple du type de trouvaille attendue : si une video defend qu'un agent a besoin
d'une couche semantique decrivant les entites du metier, la primitive n'est pas
« il faut une ontologie » — c'est « **registre d'entites metier** : la liste
nommee des objets que l'organisation manipule, leurs attributs et leurs
relations », et la traduction produit est « une section *Ontologie* dans it-rd,
dont la page de detail liste les entites et laisse ouvrir chacune ».

## Ta grappe

**Memoire, graphe et runtime** (3 videos)

- `Q0VkgCyNVUg.md` — CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens
- `khVX_BUnEwU.md` — Active Graph Agent Runtime (BabyAGI 4) - Yohei Nakajima
- `9QebvrrY3KY.md` — Claude for Long-Horizon Tasks - Lance Martin, Anthropic

Tes transcripts sont dans `transcripts/<id>.md`, deja telecharges.
**Ne lis QUE ceux de ta grappe.** Ne va pas sur le web.

## Livrable — `analyses/T2_rapport.md`

### 1. Par video

Pour chacune, dans cet ordre :

- **Ce que la video defend**, en trois phrases maximum. Si tu ne peux pas le dire
  en trois phrases, c'est que tu ne l'as pas compris.
- **3 a 8 primitives**, chacune avec : un nom court en francais, une definition
  d'une phrase, et une citation VERBATIM de moins de 15 mots qui l'ancre.
  Les citations longues sont interdites (droit d'auteur).
- **Ce qui ne s'applique PAS a Coach OS**, et pourquoi. Cette section est
  obligatoire et ne peut pas etre vide : une video dont tout serait applicable
  signale que tu as arrete de reflechir.

### 2. Traduction produit

Un tableau, une ligne par primitive retenue :

| primitive | app visee | section de barre laterale | bloc de page de detail | pourquoi maintenant |
|---|---|---|---|---|

`app visee` est l'une de **people**, **operations**, **it-rd**, ou `aucune` si la
primitive est vraie mais hors de ces trois apps — dans ce cas, dis laquelle des
19 apps la porterait mieux.

### 3. Les trois meilleures idees

Classe tes trois propositions les plus fortes, et pour chacune explique ce qui la
rend meilleure que les deux autres. Un classement sans justification ne vaut rien.

## Interdits

1. **Ne modifie aucun fichier du depot coach-os.** Tu ecris UN fichier :
   `analyses/T2_rapport.md`. Rien d'autre.
2. **Ne cite pas plus de 15 mots d'affilee** d'un transcript.
3. **N'invente rien.** Chaque primitive s'appuie sur un passage reel. Si tu
   hesites sur ce que dit la video, ecris-le plutot que de combler.
4. Pas de recherche web, pas d'installation, pas de commande longue.
5. Ne lis pas les transcripts des autres grappes, meme par curiosite : ton
   rapport doit etre independant pour que la synthese compare des regards
   distincts et non un consensus premature.

## Si tu dois t'arreter

Ecris quand meme le rapport avec ce que tu as etabli, et une section
« **reste a couvrir** » nommant les videos non traitees. Un rapport partiel et
honnete vaut mieux qu'un rapport complet et brode.
