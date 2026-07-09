---
video_id: aaujj-n3ai0
url: https://www.youtube.com/watch?v=aaujj-n3ai0
title: Claude Code Fonctionne ENFIN Pendant Que Vous Dormez
channel: Vision IA
duration: 10:53
views: 40k
language: fr
ingested_at: 2026-06-14
status: ok
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
date: 2026-06-14
type: source
---

# Claude Code Fonctionne ENFIN Pendant Que Vous Dormez

**Chaîne** : Vision IA
**URL** : https://www.youtube.com/watch?v=aaujj-n3ai0
**Durée** : 10:53
**Vues** : 40k

## Transcript brut (concaténé)

6h du matin, personne derrière l'écran.
Le terminal est ouvert et Claude Code
est en train de passer en revue les
commits de la nuit, de vérifier qu'aucun
bug n'a été introduit et de rédiger un
résumé complet de l'état du projet.
Quand le développeur arrive avec son
café à 8h du matin, tout est déjà prêt.
Il n'a rien demandé, il n'a rien lancé.
C'est l'agent ICL Code qui a décidé que
c'était l'heure et ce n'est pas un
scénario effectif. C'est exactement ce
que permettent les deux fonctionnalités
qu'Antropic vient d'ajouter à Clode Code
et elle transforme radicalement la
manière dont on peut utiliser cet outil.
On ne parle plus d'un assistant qui
attend sagement vos instructions. Non,
on parle d'un agent autonome capable de
travailler pendant que vous dormez, de
surveiller vos projets en continu et
même de s'améliorer tout seul d'une
exécution à l'autre. Messieursdames,
dans les prochaines minutes, vous allez
comprendre exactement comment ça
fonctionne, comment le configurer et
surtout pourquoi. C'est probablement le
plus gros changement dans l'univers des
outils de code assistés par IA depuis
l'arrivée de Cloud Code lui-même.
D'ailleurs, si vous avez rejoint la
communauté Vision IA, sachez que j'ai
une très bonne nouvelle pour vous, mais
ça on en reparlera en fin de vidéo.
Commençons par la première brique qui a
été ajoutée au nouveau cloud code, les
tâches [musique] planifiées. Alors, vous
allez voir, le principe est assez simple
à comprendre. Vous allez écrire un
prompt une seule fois. Vous choisissez
une fréquence, donc disons toutes les
heures ou tous les jours ou toutes les
semaines et Cloud Code va l'exécuter
automatiquement. Vous ouvrez
l'application Cloud Code pour le bureau.
Vous allez dans l'onglet schedule, vous
cliquez sur nouvelle tâche et il vous
suffit de remplir quatre champs. Un nom,
un prompt, le modèle que vous voulez
utiliser et la fréquence. Puis c'est
terminé. Chaque exécution démarre une
session fraîche avec un accès complet à
tous vos fichiers, à vos serveurs MCP,
vos skills, vos plugins et cetera avec
de la sécurité tropique. L'agent va lire
le prompt, il va travailler dans votre
projet, il fait ce qu'il a à faire puis
il s'arrête proprement et le lendemain
il recommence. Ce qui rend cette
fonctionnalité fondamentalement
différente d'un simple Chrome Job
classique, c'est que l'exécuteur n'est
pas un script déterministe, c'est un
agent. Dans un script Python classique,
si la ligne 47 plante et bien ça plante
euh il ne cherche pas à comprendre
pourquoi il ne tente pas une autre
approche. Il vous envoie une erreur et
il attend. Clud code au contraire quand
il rencontre un problème il analyse
l'erreur. Il laissait trois autres
stratégies. Il identifie celle qui
fonctionne et il continue. C'est ce
qu'on appelle un workflow
autoréparateur. Et vous allez voir ça
change absolument tout quand on parle
d'automatisation sans supervision. Mais
ayant dit cela, ce n'est pas le plus
impressionnant de cette histoire. La
deuxième fonctionnalité s'appelle les
boucles ou les loops en anglais et elle
répond à un besoin complètement
différent. Les tâches planifiées sont
faites pour le long terme tous les
matins à 8h30, chaque vendredi soir ou
le premier lundi du mois, peu importe.
Les loops, elles au contraire sont
conçues pour le temps réel. Vous êtes en
plein déploiement et vous voulez que
Claud code vérifie toutes les 5 minutes
si tout se passe bien. Une seule
commande suffit. /loop 5 minutes check
if deployment is finished. Cloud va
créer un job intern et toutes les 5
minutes, il va exécuter cette
vérification directement dans votre
session en cours. Vous n'avez même pas
besoin d'utiliser la commande/ash. Vous
pouvez simplement écrire en langage
naturel et en français aussi. Toutes les
10 minutes, vérifie mon clickup pour
voir s'il y a du nouveau sur le projet
et il va le faire. La différence
essentielle avec les tâches planifiées,
c'est que les loops fonctionnent à
l'intérieur d'une seule et même session.
Ça veut dire que chaque itération a
accès au contexte des précédentes.
L'agent voit ce qu'il a vérifié il y a
10 minutes, il voit les résultats d'il y
a 20 minutes et il peut adapter son
comportement en conséquence. C'est un
avantage énorme pour les tâches de
surveillance. Mais attention, c'est
aussi un piège potentiel. Bien sûr, si
votre loupe, votre boucle génère un
rapport détaillé toutes les 10 minutes,
au bout de quelques heures, la fenêtre
de contexte va commencer à saturer. Il
faut donc penser à garder les outputs
concis, les sorties concises. Les loops
sont disponibles partout dans le
terminal, dans VS Code, dans
l'application de bureau et cetera. Elles
prennent en charge les intervalles
réguliers, donc toutes les 5 minutes,
toutes les heures, toutes les 2hures et
cetera, mais aussi les rappels
ponctuels. Vous pouvez dire par exemple
à 15h, rappelle-moi de mettre en
production la branche de la branche
officielle. Et Cloud programme un job
unique qui s'autodétruit après cette
exécution. Chaque session peut contenir
jusqu'à 50 tâches planifiées
simultanément. Et si vous voulez tout
annuler, vous fermez la session ou alors
vous dites tout simplement annule tous
les jobs en cours. Il y a toutefois une
limite importante à connaître. Les loops
expirent automatiquement après 3 jours.
C'est une sécurité mise en place par un
tropic pour éviter que des boucles
oubliées ne tournent indéfiniment. Si
votre besoin dépasse 3 jours, c'est un
signal clair qu'il faut basculer vers
une tâche planifiée classique plutôt que
des loops. Et d'ailleurs, la question à
se poser est très simple. Est-ce que
j'ai besoin d'aide maintenant sur ce
projet pendant quelques heures ou alors
quelques jours ? Si oui, alors c'est une
loupe. Est-ce que j'ai besoin d'une
automatisation qui tourne chaque semaine
indéfiniment ? Si oui, c'est une tâche
planifiée. On arrive maintenant à la
partie qui personnellement me fascine le
plus. Les tâches planifiées sont
statlessess. Ça veut dire que chaque
exécution démarre sans aucune mémoire de
la précédente. Et les loops, donc les
boucles L, partagent le contexte mais
sont éphémères. Alors, comment faire
pour qu'un agent autonome devienne
réellement plus intelligent au fil du
temps ? La réponse tient en un concept
un fichier mémoire partagée. Le principe
c'est le suivant. Vous structurez le
prompt de votre tâche planifiée en trois
phases. Phase numéro 1, avant de
commencer tout travail, vous dites à
votre agent, lis le fichier
dernierrun.md qui contient le résumé de
ta dernière exécution. Phase numéro 2,
vous lui dites fais ton travail
principal. Et phase numéro 3, une fois
que tu as terminé, écrase ce fichier
avec ce nouveau résumé. Ce que tu as
fait, combien de temps ça a pris, les
problèmes rencontrés, les pistes
d'amélioration et cetera. L'agent
suivant, celui qui va se réveiller le
lendemain, commence par lire ce
fichier-là et hérite immédiatement du
contexte de son prédécesseur. On peut
aller encore plus loin. Rien n'empêche
euh d'ajouter dans le promps une
instruction du type euh "Si tu
identifies une façon d'améliorer ce
promp, réécris-le." Vous voyez
l'autoamélioration ici. L'agent peut
donc non seulement corriger son propre
code quand il plante, mais aussi
optimiser les instructions qu'il reçoit.
On entre dans la logique d'un système
auto-améliorant et ce n'est pas de la
science-fiction, c'est littéralement ce
que permet la combinaison de CR de code
avec un accès en écriture à ses propres
fichiers de configuration. D'ailleurs,
cette semaine, André Schpati, l'ancien
directeur IA de Tesla et cfondateur
d'Openai, a rendu public un projet qui
illustre parfaitement cette philosophie.
Il s'appelle Auto Research. Le concept
est assez simple. Vous donnez à un agent
IA un GPU, donc une carte pour faire des
calculs IA, un setup d'entraînement de
modèle de langage et un fichier
d'instruction. Puis vous allez dormir.
L'agent va modifier le code
d'entraînement. Il va lancer un run de 5
minutes, vérifier si le les résultats se
sont améliorés. Il va garder ou rejeter
les modifications et recommencer ainsi
de suite. En une nuit, environ 100
expériences sont réalisées sans aucune
intervention humaine. Et au petit matin,
vous récupérez un modèle optimisé et un
journal complet de tout ce qui a été
testé. Carpati a commenté la chose avec
une phrase qui résume parfaitement
l'époque. Il dit, je cite, "Je n'ai
touché à rien." Voilà ce que ça a fait
le poste AGI. Le parallèle avec code est
frappant. Autosarch utilise une boucle
autonome avec un agent qui modifie, test
et Cloud Code avec ses tâches planifiées
et ses loops offrent exactement la même
architecture mais appliqué à n'importe
quel projet de développement, pas
uniquement à l'entraînement des modèles.
La différence c'est que Cloud Code est
ici accessible à tous, même sans GPU,
donc sans carte graphique pour faire les
calculs d'IA. Parlons maintenant d'un
aspect pratique qui est vraiment
crucial. Comment savoir quand une tâche
automatisée a terminé son travail ?
Parce que si Cloud Code fait tout seul
ses reviews de code à 6h du matin, c'est
bien. Mais si vous ne voyez le résultat
qu'en fouillant dans les logs 3 jours
plus tard, ça perd tout son intérêt,
n'est-ce pas ? Première option,
l'application de bureau affiche toutes
vos tâches de manière organisée avec
l'historique complet de chaque
exécution. Vous pouvez consulter chaque
run, voir ce qu'il s'est passé et
identifier les éventuels problèmes. Mais
soyons honnête, personne ne va vérifier
ça proactivement tous les matins. Euh la
solution, ce sont tout simplement les
hooks. Cloud code permet aussi de
configurer des hooks, donc des actions
qui se déclenchent automatiquement à
certains moments du cycle de vie d'une
session. Vous pouvez par exemple
configurer un hook qui joue un son à
chaque fois qu'une session se termine ou
mieux encore intégreer directement dans
le prompt de votre tâche une instruction
finale du type une fois terminée
envoie-moi un message avec le résumé.
L'argent ont fait son travail et la
dernière chose qu'il fait c'est vous
notifier. Depuis cette semaine Cloud
Code prend également en charge les hooks
http ce qui signifie que vous pouvez
déclencher n'importe quel web hook. Donc
que ce soit Slack, Discord, Telegram et
email, ClickUp et cetera, tout ce que
vous voulez. Et pour ceux qui veulent
aller encore plus loin, il existe une
troisième voie, les GitHub action.
Antropic propose une action officielle
qui permet de programmer Cloud Code
directement dans vos pipelines.
L'avantage est assez considérable. Ça
tourne sur les serveurs de GitHub, donc
pas besoin de laisser votre ordinateur
allumer parce que oui, c'est la
principale limitation actuelle des
tâches planifiées en local. Votre
machine doit être allumée et
l'application doit être ouverte pour que
les tâches s'exécutent. Si votre
ordinateur dort, Cloud code dort aussi.
La bonne nouvelle, c'est que quand vous
rallumez, il vérifie automatiquement les
sept derniers jours et il rattrape les
tâches manquées. Si vous regardez
l'évolution d'entropique ces derniers
mois, la trajectoire est assez limpide.
Clude Opus 4.6 vient de prendre la
première place du classement webdev
arena devant tous les modèles d'openhei
et de Google pour le code informatique.
Cowork est sorti pour les utilisateurs
pro. Les plugin, le marketplace, le
remote control, la mémoire persistante,
tout converge vers un seul et même
objectif. faire de cloud code un
véritable collègue autonome, pas juste
un outil qu'on interroge. Et nous n'en
sommes qu'au début, hein. Les tâches
planifiées ne sont disponibles dans
l'application Cloud Descope, donc Cloud
Bureau que depuis quelques semaines. Les
loops, les boucles viennent tout juste
d'arriver. Alors oui, au rythme actuel
auquel Anthopique livre des mises à
jour, on parle de release quasi
quotidien. Il est probable que les
tâches planifiées soient bientôt
disponibles directement dans le terminal
et dans les extensions VS Code aussi. Et
quand cela arrivera, la barrière entre
outil de développement et agent autonome
permanent aura définitivement disparu.
Alors messieurs dames, si tout ce que
vous venez d'entendre vous donne envie
de maîtriser clot code mais que vous ne
savez pas trop par recommencer ou alors
que ça vous semble un peu compliqué ou
si vous vous l'utilisez déjà mais que
vous sentez que vous n'exploitez qu'une
fraction de son potentiel, alors j'ai
une très bonne nouvelle pour vous.
D'ailleurs, je suis en train de
finaliser un module complet sur Cloud
Cloud dans ma formation qui vous amène
de la toute première installation
jusqu'à la mise en place de ces workflow
automatisés. Tout est en français, tout
est pensé pour être accessible et tout
est mis à jour en permanence pour suivre
le rythme d'anthropique. Je suis en
train d'y travailler en ce moment, mais
vous pouvez vous y abonner dès
maintenant et avoir accès au tout
nouveau module Cloud code dès qu'il sera
dispo et à beaucoup d'autres modules
tout de suite pour 49 €. D'ailleurs, à
tous ceux qui ont acquis la formation,
je sais que vous êtes très très
nombreux. Bonne nouvelle, une très très
grosse mise à jour de celle-ci arrive.
On va tout revoir, on va tout actualiser
et comme je vous l'avais promis, cela ne
vous coûtera rien de plus. Les liens
sont en description.


