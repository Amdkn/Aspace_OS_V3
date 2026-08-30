# Coach OS V1 — de la vitrine à la machine d'acquisition

Écrit le 2026-08-08, d'après l'énoncé de l'utilisateur. Ce document dit **où l'on va** ; il
ne dit pas encore comment. Les quatre analyses de vidéos qui l'accompagnent le préciseront.

---

## La phrase

> Pouvoir implémenter l'acquisition automatisée par clone de jumeau numérique, en utilisant
> N8N ou Make pour les workflows mais **pilotés par des MCP d'agents**.

Cinq briques, et l'ordre entre elles est ce qui compte.

## L'écart avec aujourd'hui

Coach OS affiche dix-neuf apps de données de démonstration. Il n'a **aucune surface
d'écriture** — vérifié : le magasin CMS ne connaît que `updateItem`, l'app Tasks n'a pas un
bouton de création, et l'agent a cinq outils dont un seul écrit. Un agent à qui l'on demande
d'agir ment, faute d'autre réponse possible.

**Une machine d'acquisition qui ne sait pas écrire une ligne n'existe pas.** Tout ce document
présuppose donc BRIEF-F, qui pose la couche d'écriture.

## Les cinq briques

### 1 · Le clone de jumeau numérique — l'acquisition

Réf. Shubham Sharma, *Comment j'ai piégé LinkedIn avec une vidéo IA* (`cT0zEwF39Q0`).

Sa chaîne, lue sur son propre schéma à l'écran :

```
récupérer la liste de contacts → générer la vidéo personnalisée
→ enregistrer le site web / LinkedIn → faire le montage de la vidéo → envoyer
```

Une capture d'écran automatisée du profil de la cible, incrustée dans une vidéo où un clone
parle — puis l'envoi. *« Tout ça fonctionne sous le capot parce que c'est juste incroyable »*,
dit-il. Ce qui compte pour nous n'est pas la prouesse : c'est que **chaque cercle de son
schéma est un outil**, au sens de la vidéo Hermes — une table, un pipeline, un agent qui le
tient.

L'utilisateur veut **aller au-delà** de son implémentation. À préciser dans l'analyse : ce
qu'il fait à la main et qui devrait être un agent, ce qu'il fait avec un service tiers et qui
devrait être un MCP.

### 2 · Les workflows — N8N ou Make, mais pilotés

Le point à ne pas manquer : **N8N et Make ne sont pas l'orchestrateur.** Ils sont l'exécutant.
L'orchestrateur, ce sont les agents, qui les appellent par MCP.

C'est l'inverse du réflexe habituel — construire le workflow puis y greffer une IA. Ici
l'agent décide, et le workflow exécute la partie déterministe. Ça rejoint exactement la
distinction que fait Palantir entre **flux déterministes et non déterministes**, et le socle
de Coach OS est déjà agnostique du fournisseur.

Question ouverte, à trancher dans l'analyse : N8N (auto-hébergeable, un MCP existe) ou Make
(hébergé) ? La souveraineté est un axe déjà porté par l'app Legal ; elle devrait peser.

### 3 · Le bureau web natif-IA

Réf. Melvynx, *La feature que tu dois mettre dans ton SaaS maintenant* (`-V9VIrwGtSs`).

Son titre à l'écran énumère : **Skills · MCP · CLI · in App**. Autrement dit, un SaaS moderne
n'expose pas qu'une interface : il expose des compétences, un serveur MCP, une ligne de
commande, et l'agent vit dans l'app.

Coach OS a déjà le bureau, les personnages, et un socle d'agent. Ce qui manque : que chaque
app **expose ses capacités** au lieu de les garder pour son interface.

### 4 · LangGraph en production

Réf. *LangGraph in 10 Minutes* (`BwZbdCzmZJc`).

Ce que ça apporte et que le tour de boucle actuel n'a pas : des **graphes d'état** — des
étapes nommées, des transitions explicites, un état qui persiste entre elles, et la reprise
après interruption.

Le socle actuel de Coach OS fait un tour de boucle d'outils par requête. Une chaîne
d'acquisition en cinq étapes qui tourne sur plusieurs minutes, avec une approbation humaine au
milieu, ne tient pas dans un tour de boucle. **Il faut un graphe.**

À trancher : LangGraph est du Python. Coach OS est du TypeScript sur Vercel. Soit un service
séparé, soit l'équivalent en TS. L'analyse doit poser le coût des deux, pas trancher par
préférence.

### 5 · Agent Plugins — le format portable

Réf. `agent-plugins.org`, spécification 1.0.0. Vérifié à la source :

> Un standard ouvert et neutre pour empaqueter des composants réutilisables en plugins
> portables. La spécification 1.0.0 définit un format partagé pour les **Agent Skills** et les
> **serveurs MCP**, que les clients compatibles peuvent découvrir et charger de façon
> cohérente.

Le problème qu'il résout est exactement le nôtre : *« les clients d'agents ont développé leurs
propres formats de plugins, même quand ces plugins contiennent les mêmes composants
sous-jacents. »*

Coach OS parle déjà à MiniMax, Anthropic, OpenAI, Google, Multica et Buzz. Empaqueter ses
outils au format Agent Plugins, c'est ce qui évite de les réécrire pour chaque client — et
c'est ce qui rendrait un Business OS en marque blanche réellement livrable.

## L'ordre qui tient debout

Chaque étage suppose le précédent. Sauter un rang, c'est bâtir sur du vide.

| rang | ce qu'on pose | pourquoi maintenant |
|---|---|---|
| 0 | **l'écriture** (BRIEF-F) | sans elle tout le reste est du théâtre |
| 1 | **les scénarios et l'approbation** (BRIEF-D) | un agent qui agit sans garde-fou sur une machine d'acquisition envoie de vrais messages à de vraies personnes |
| 2 | **le graphe d'état** | une chaîne en cinq étapes ne tient pas dans un tour de boucle |
| 3 | **les workflows par MCP** | l'agent décide, N8N exécute |
| 4 | **les capacités exposées** — Skills, MCP, CLI | l'app cesse d'être une interface et devient un outil |
| 5 | **Agent Plugins** | pour que ça se livre à d'autres |

Le rang 1 n'est pas un luxe. Une machine d'acquisition automatisée qui se trompe **contacte de
vraies personnes en ton nom**. L'audit de sécurité vient de montrer qu'un contenu peut donner
des ordres à l'agent, et qu'un résultat d'outil peut être forgé. Brancher ça sur un envoi
sortant sans file d'approbation serait la faute la plus coûteuse de ce projet.

C'est d'ailleurs la leçon de la démo Palantir : la fusion déclenche les appels sortants, mais
**seulement après qu'un humain a arbitré**.

## Ce que je ne sais pas encore

- Ce que fait Shubham exactement, étape par étape, et ce qui s'automatise vraiment.
- Ce que Melvynx entend précisément par Skills / MCP / CLI / in App.
- Le coût réel d'un LangGraph à côté d'un déploiement Vercel TypeScript.
- Si un MCP N8N mûr existe, ou s'il faut l'écrire.

Ces quatre points sont l'objet de l'analyse déléguée. **Rien ne se construit avant qu'ils
soient répondus** — construire sur une supposition coûte plus cher que de la lever.
