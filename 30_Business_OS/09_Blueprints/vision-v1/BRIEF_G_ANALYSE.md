# BRIEF-G — Lire les quatre sources, et poser l'architecture

Lis `VISION.md` dans ce dossier. Il fait partie de ce brief et en donne le cadre.
Lis `GARDE_FOU.md` dans `coach-os-refonte/correctifs/`.

Ton rapport : `ARCHITECTURE_V1.md`, à côté.

**Tu n'écris aucun code dans ce chantier.** Tu lis, tu regardes, tu tranches, tu écris un
document. Construire sur une supposition coûte plus cher que de lever la supposition.

---

## Les quatre sources

Les images sont déjà extraites dans ce dossier — `<nom>/planches/`. **Ouvre-les.** Trois fois
cette semaine un chantier a été mené à l'aveugle faute de regarder, et trois fois il a fallu
le refaire.

Les transcriptions ne sont pas encore là : récupère-les toi-même avec l'outil
`mcp__transcript-api__get_youtube_transcript`, et **dépose-les à côté des planches** en
`transcription.md`. Elles serviront aux vagues suivantes.

| dossier | vidéo | ce qu'on y cherche |
|---|---|---|
| `shubham-linkedin` | `cT0zEwF39Q0` — Comment j'ai piégé LinkedIn avec une vidéo IA | la chaîne d'acquisition, étape par étape |
| `melvynx-feature` | `-V9VIrwGtSs` — La feature que tu dois mettre dans ton SaaS | ce que « Skills · MCP · CLI · in App » veut dire concrètement |
| `langgraph` | `BwZbdCzmZJc` — LangGraph in 10 Minutes | le modèle de graphe d'état, et ce qu'il apporte qu'un tour de boucle n'a pas |
| `agent-plugins` | `UaeWJK_vv-Y` — Introducing Agent Plugins | le format, et ce qu'il faut pour s'y conformer |

Complète avec la spécification : `https://agent-plugins.org/` — sections *Plugin manifest*,
*Skills*, *MCP servers*, *Client conformance checklist*.

## Les quatre questions à répondre

Ce sont exactement les inconnues listées en fin de `VISION.md`. Une réponse par question, avec
ce sur quoi tu t'appuies.

### 1 · La chaîne de Shubham, décomposée

Son schéma à l'écran donne cinq cercles : *récupérer la liste de contacts · générer la vidéo
personnalisée · enregistrer le site web / LinkedIn · faire le montage · envoyer*.

Pour chacun : **quel service il utilise**, ce qui est automatisé et ce qui reste à la main.
Il mentionne au passage « une API pour faire des screenshots » — nomme-la si elle est visible.

Puis la question qui compte : **lesquels de ces cercles seraient un agent chez nous, et
lesquels un appel de workflow ?** L'utilisateur veut aller au-delà de son implémentation ; dis
en quoi elle est limitée.

### 2 · Melvynx — Skills, MCP, CLI, in App

Qu'entend-il exactement par chacun des quatre ? Donne un exemple concret pour chacun, tiré de
la vidéo, pas de ta culture générale.

Puis : **lequel des quatre Coach OS a-t-il déjà, lequel lui manque ?** Il a un bureau, des
personnages, un socle d'agent agnostique, et cinq outils. Sois précis sur l'écart.

### 3 · LangGraph — et le coût de l'introduire

Explique le modèle : états, nœuds, transitions, persistance, reprise. Ce qu'un graphe permet
et qu'un tour de boucle d'outils ne permet pas.

Puis tranche honnêtement le problème pratique : **LangGraph est du Python ; Coach OS est du
TypeScript déployé sur Vercel.** Trois voies, et le coût de chacune :

- un service Python séparé, appelé par l'API de Coach OS ;
- un équivalent en TypeScript — dis lequel, s'il existe et s'il est mûr ;
- rester sur le tour de boucle et accepter la limite.

**Ne tranche pas par préférence.** Donne les coûts, et une recommandation argumentée qui peut
très bien être « pas maintenant ».

### 4 · Agent Plugins — la conformité

Ce que contient un plugin, la forme du manifeste, ce qu'un client doit savoir faire.

Puis : **que faudrait-il à Coach OS pour publier ses cinq outils sous ce format ?** Liste
concrète, pas une intention. Et : qui saurait les charger aujourd'hui — Claude Code, Hermes,
autre chose ?

## Une cinquième question, que la vision n'a pas posée

**N8N ou Make ?**

Cherche s'il existe un serveur MCP mûr pour l'un ou pour l'autre, et dans quel état. Pèse
l'auto-hébergement — c'est un axe que Coach OS porte déjà dans son app Legal, il ne s'ignore
pas.

Si la réponse est « il faudrait l'écrire », dis-le : c'est une réponse recevable et utile.

## L'ordre, et le droit de le contester

`VISION.md` propose six rangs, de l'écriture jusqu'à Agent Plugins. **Tu as le droit de le
contester** — c'est même une des choses utiles que tu peux faire. Si tu penses qu'un rang est
mal placé, dis-le et argumente.

Ce que tu ne peux pas faire : l'ignorer sans le dire.

## Ce que ton document doit contenir

1. les quatre réponses, plus la cinquième ;
2. **un tableau des écarts** : ce que Coach OS a, ce qui lui manque, pour chaque brique ;
3. un ordre d'exécution, le tien, avec ce qui bloque quoi ;
4. **les risques**, en particulier celui-ci, qui n'est pas théorique : une machine
   d'acquisition automatisée **contacte de vraies personnes au nom de l'utilisateur**.
   L'audit de sécurité vient d'établir qu'un contenu peut donner des ordres à l'agent et qu'un
   résultat d'outil peut être forgé. Dis ce que ça implique avant tout envoi sortant ;
5. **« ce que je n'ai pas pu établir, et pourquoi »** — obligatoire. Une inconnue nommée vaut
   mieux qu'une affirmation confortable.

## Interdits

Aucune modification du dépôt Coach OS. Aucun `npm install`. Aucun commit. Tu produis un
document et quatre transcriptions, rien d'autre.

Et n'invente pas de source. Un rapport de cette campagne a cité une « documentation d'audit
interne » qui n'existe pas, pour habiller un ordre de grandeur. Si tu ne sais pas, écris que
tu ne sais pas.
