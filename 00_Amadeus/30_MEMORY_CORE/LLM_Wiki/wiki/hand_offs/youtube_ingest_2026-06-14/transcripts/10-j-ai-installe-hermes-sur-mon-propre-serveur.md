---
video_id: aDmGw3zpcJw
url: https://www.youtube.com/watch?v=aDmGw3zpcJw
title: J'ai installe Hermes sur mon propre serveur
channel: Julien Sanson | Automatisation & AI
duration: 27:56
views: 1.1k
language: fr
ingested_at: 2026-06-14
status: ok
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
date: 2026-06-14
type: source
---

# J'ai installe Hermes sur mon propre serveur

**Chaîne** : Julien Sanson | Automatisation & AI
**URL** : https://www.youtube.com/watch?v=aDmGw3zpcJw
**Durée** : 27:56
**Vues** : 1.1k

## Transcript brut (concaténé)

Salut à toi, j'espère que tu vas bien.
Aujourd'hui, on va mettre en place ton
agent qui tourne sur un serveur et que
tu peux accéder partout et pas forcément
sur ton PC. Et tu vas voir, c'est pas si
compliqué. L'objectif, c'est qu'à la fin
de la vidéo, tu es déjà un premier agent
qui tourne et qu'il puisse effectuer
différentes actions pour t'aider toi
dans ton business. Allez, on perd pas de
temps, on voit ça tout de suite.
Alors, le Hermes agent, c'est un agent
IA open source qui est très populaire
dernièrement sur GitHub. Vous avez
sûrement vu des vidéos passées et
contrairement à un chatbot classique, il
vit sur ton infrastructure. Donc ce soit
sur ton PC, que ce soit dans un serveur,
vous avez dû voir sûement passer pas mal
de gens avec leur Mac Mini dernièrement.
Bon, j'en ai pas malheureusement. Et
l'avantage, c'est qu'il garde sa mémoire
entre les différentes sessions et il
écrit aussi ses propres skills à mesure
que tu l'utilises. Donc c'est vraiment
cool pour ça. Juste avant de
l'installer, j'ai envie que tu
comprennes le problème que ça résout
parce que sinon tu vas juste
l'installer, tu vas le tester et après
tu vas arrêter de l'utiliser. Voilà, au
bout de 2 jours. En fait, il faut
vraiment vous voyez ça comme un
stagiaire qui va être au début bah un
peu nul entre guillemets, genre il vous
connaît pas du tout. Il va falloir lui
apprendre petit à petit. En fait, au fur
et à mesure des itérations et des
discussions avec vous, il va progresser
et apprendre notamment les deux fichiers
comme le fichier user ou memory et aussi
va devenir de plus en plus fort entre
guillemets vu qu'il va créer des skills
au fur à mesure de vos discussions et il
va faire ça automatiquement sans que
vous ayez à le faire. Donc vous voyez ça
vraiment comme un un assistant qui va
être sur votre téléphone, qui va être
sur Telegram, sur Slack, sur Discord,
peu importe où vous le connectez et qui
va s'améliorer au fur et à mesure de vos
discussions. L'objectif à terme, c'est
voilà d'avoir un assistant qui puisse
vous aider au quotidien dans votre
business.
Et du coup, comme je vous ai dit, ce
dernier s'améliore grâce notamment à sa
mémoire. Sa mémoire est composée d'un
user. MD et d'un memory. MD. MD signifie
markdown, donc c'est juste un format,
donc c'est du texte globalement. User
MD, on le verra plus tard, mais en gros,
il s'adapte à la personne avec qui il
discute et il note des informations par
rapport à la personne avec laquelle il
discute. Si par exemple, je lui dis que
je sais pas, je suis allergique aux
noisettes, bah dans ces cas-là, il va
ajouter cette information dans
l'utilisateur MD Julien. il va dire c
utilisateur estagi au noisette et comme
ça il s'en souvient la prochaine fois.
Ensuite memory.md. Ça c'est sa mémoire
plus générale on va dire et qui est
rechargée à chaque session pour se
souvenir des précédentes discussions.
Ensuite on a la partie skill. La partie
skill vous connaissez donc ce sont des
fichiers réutilisables concernant des
caractéristiques très précises des
utilisations très précises d'outils par
exemple ou alors de processus.
L'objectif c'est que lorsqu'il se rend
compte qu'il doit répéter plusieurs fois
les mêmes process et bien dans ces
cas-là il cré un skill pour pouvoir
l'optimiser les prochaines fois. La
partie Souol donc le fichier Sou.m MD,
c'est globalement la personnalité de
l'agent. Tu peux dire à ton Hermes, bah
répond toujours en français par exemple,
soit plus direct. En gros, tu peux lui
dire pas mal de choses qui vont définir
sa personnalité. Ensuite, il va
enregistrer ça et donc tous les futurs
messages passeront par ce filtre
initial. Si tu fais par exemple tourner
six différents a messagant sur ton
serveur, et ben ces six agents peuvent
avoir leur personnalité différentes. Les
chron en fait, chron ça signifie tout
simplement une automatisation ou un
process qui est lancé à un ourire
régulier. Tu peux lui dire tout
simplement dans ton chat avec lui tous
les jours, bah fais-moi un recap des
news concernant l'IA par exemple et on
voit moi ce recap directement sur
Telegram. Ça c'est un exemple. Si vous
dirigez une boîte, bah peut-être du coup
tous les jours, fais-moi un recap de mon
pipeline commercial. C'est libre à vous
en fait avec votre imagination de
pouvoir créer bah les automatisations
qui vous êtent dans votre quotidien. Et
ensuite bah Hermes il crée
potentiellement le skill qui va avec, il
génère le crown et il l'exécute. Et
petite info à savoir, c'est que quand le
crown se lance, il tourne vraiment dans
une session isolée et il n'a pas le
contexte de la discussion qui a initié
ce crown. Donc il faut vraiment que tu
sois très précis dans le promte que tu
lui donnes pour qu'il puisse avoir le
plus d'informations possible lorsqu'il
va lancer la tâche en question. Et aussi
bah ça ça paraît plutôt évident mais un
crun ne pas enclencher d'autres chron
pour pas avoir d'action en cascade par
sécurite. Et ensuite la boucle
d'autoamélioration. C'est ce qui relie
euh toutes ses capacités de notre agent.
Tu fais une action, bah l'agent il va
apprendre, il va sauvegarder ça dans sa
mémoire, il va potentiellement créer un
skill rattaché à la tâche. Après, il
faut garder en tête aussi que toutes ces
actions fonctionnent bien uniquement si
vous précisez bien l'agent quand il se
trompe parce que si vous lui dites pas
qu'il se trompe, bah il va continuer
sans forcément retenir bah certaines
actions et donc il est nécessaire de
rester très intransigent entre
guillemets avec lui. Comme ça dès qu'il
se trompe, il va le noter dans sa
mémoire ou dans un skill pour pas
reproduire ça dans le futur et pour pas
rééviter la tendance qu'il aurait à se
tromper.
[musique]
Pour ce qu' de l'installation, bah on va
faire les choses plutôt simples. Je vais
zoomer un petit peu ici. Alors, soit on
peut l'installer directement sur notre
PC, donc on lance la commande ou alors
on peut l'installer sur un VPS, donc sur
un serveur. Et pour moi, c'est la
solution la plus simple et j'utilise
Hostinger pour ça. comme d'habitude pour
un petit peu tout. Donc pour Nintend,
pour du clot code de temps en temps et
surtout bah pour cet agent parce que le
fait d'avoir du coup cet agent sur un
VPS, bah ça permet de l'isoler de mon PC
et ne pas avoir de potentiel danger
parce que oui, votre agent tourne, il
peut lancer des commandes et ça peut
potentiellement être dangereux pour vous
si il lique par exemple des
informations, s'il li des clés à API et
cetera et cetera. Donc c'est pour ça
qu'on a envie de faire attention quand
on l'installe et que pour ça, j'utilise
bah un VPS de Dostinger. Donc voici un
petit schéma pour expliquer un petit peu
l'installation. Votre VPS c'est en gros
un PC globalement qui est à distance et
on peut installer notre air message
agent directement dedans ou on peut
l'installer dans un container d'cker. Un
container d'cker ça va être un
environnement cloisonné globalement. Et
l'avantage de travailler avec un
container Docker, c'est que votre agent
bah du coup il est bloqué dans son petit
container juste ici. Hop, il peut pas se
sortir. Et voilà, si vous créez d'autres
agents après vous pouvez en mettre un
deuxième du coup dans votre docker créer
un nouveau container et euh les agents
ne pourront pas échanger entre eux et
ils travaillent dans des sessions
individuelles chacun. Et ça c'est
facilement géré directement dans
Hostinger. Donc je vais vous montrer ça
tout de suite. Donc je vous montrer
comment faire. Donc c'est plutôt simple
pour ça. Donc vous rendez sur Hostinger,
vous commencez à connaître, vous
choisissez un serveur en question.
Personnellement, j'ai le KVM2 qui
fonctionne très bien. Donc la seule
différence entre les serveurs, c'est
globalement le nombre de CPU et la RAM
ainsi que l'espace disque disponible. En
fait, plus vous avez un serveur qui,
entre guillemets coûte cher par mois et
plus il est intéressant forcément. Donc
là, ça dépend ce que vous voulez faire
tourner. Si vous voulez faire tourner
tourner des modèles DI, si vous voulez
faire tourner beaucoup d'agents par
exemple. En tout cas, avec le KVM2, ça a
toujours bien fonctionné de mon côté.
Vous sélectionnez ça. Ensuite, vous
sélectionnez la durée d'abonnement de
votre serveur. Donc ça va de 1 mois à 12
mois, 24 mois. Euh forcément, plus vous
prenez une durée importante, plus c'est
rentable aussi. Vous descendez un petit
peu, vous choisissez l'emplacement du
serveur en question qui vous donne la
meilleure latence. Donc là, ici la
France par exemple et vous pouvez déjà
choisir des applications à ajouter sur
votre serveur. Donc là, vous pouvez
ajouter un messageon directement ici.
Dans tous les cas, je vous le montre
juste après dans la démo. Et ensuite
dans le code promo, vous mettez le code
promo Julien Sans son. Voilà, vous
faites appliquer et voilà, vous avez un
code promo de 10 % sur tout ce qui est
abonnement annuel. Donc voilà, donc sur
12 mois ou 24 mois, vous faites
continuer et ensuite vous vous connectez
et votre serveur bah va être généré.
Ensuite, une fois que vous avez généré
votre serveur, vous allez arriver dans
cet espace. Donc là, on peut voir ici
mes différents serveurs hostinger. Et
ici, j'ai un serveur donc qui est tout
frame. Donc c'est ce que vous verrez
aussi à la création. Donc je vais gérer
ce serveur. Je vais cliquer sur gérer
tout simplement et j'arrive dans mon
espace un petit peu mon dashboard de
maintenance de [musique] mon serveur.
Donc je peux voir mon utilisation de
CPU, le trafic dessus, l'utilisation du
disque, la mémoire et cetera. Donc voir
globalement s'il est en bonne santé. Je
peux renommer mon serveur juste ici
aussi. Donc plutôt utile si on veut pas
se perdre quand on commence à en avoir
plusieurs. Donc là, je peux donner le
nom par exemple Hermes YouTube.vvbs.
Voilà. Et voilà, mon nom est en train de
se mettre à jour et on le retrouve en
haut à gauche une fois que le nom a été
modifié. Donc voilà, c'est plus facile
pour s'y retrouver. Et ensuite, on a
l'accès route ici qui est la commande à
taper pour pouvoir accéder directement à
notre serveur et le mot de passe route à
indiquer pour pouvoir se connecter à
celui-ci. Ça c'est quand on va le faire
directement depuis un terminal externe à
notre serveur. Donc là, je vais ajouter
un nouveau mot de passe. Hop, ça y est,
j'ai ajouté mon mot de passe. On peut
voir que j'ai la petite partie terminale
en haut à droite pour accéder euh au
terminal du serveur en question. Et ce
que je vais faire tout simplement, c'est
que je vais aller à gauche dans
gestionnaire Docker qui est la partie
qui nous intéresse et je vais pouvoir
ajouter un projet. Je clique sur
composer, déploiement en un clic parce
qu'en fait, on a envie d'ajouter Hermes
dans notre gestionnaire docker comme je
vous ai montré sur le schéma précédent.
Et donc là, on va taper Hermes. Voilà,
on peut voir ici qu'il y a le Hermes
agent juste ici. Il y a aussi d'autres
Hermes sur le côté. Je les ai pas testé.
Dites-moi en commentaire si vous tester
ces autres produits d'Hermes. J'avoue,
je sais pas du tout ce que c'est. Je
connais que le Hermes agent pour
l'instant. Là, je suis je suis un petit
noob. Donc, je sélectionne le Herm
agent. Et ici, on va configurer la
partie environnement de notre agent.
Donc la partie environnement, ce sont ce
sont toutes les variables, les clés API
euh qu' auquel il aura besoin pour
pouvoir se connecter à différents
outils. Donc la partie ami username et
password, donc ce sont les identifiants
mot de passe euh pour lequels on a
besoin pour se connecter à notre agent.
Donc ça c'est pour nous sécuriser pour
pas que tout le monde accède à notre
agent. Et ici, on a d'autres euh clés
API aussi potentielles euh qu'on peut
ajouter si voilà, on souscrit déjà à ces
outils-là euh pour utiliser des
fonctionnalités de recherche web, des
nouveaux modèles. Donc là, je vais
mettre un username, donc je vais
l'appeler euh YouTube par exemple et je
vais mettre un password aussi. Et je
vais cliquer sur déployer. Et ça y est,
j'ai mon agent qui est en train de se
créer directement. Et lorsqu'il sera
prêt, on pourra y accéder directement
via la partie accès. Ici, on a déjà une
partie documentation qui apparaît sur le
côté et si on clique dessus, on arrive
directement sur la documentation de
Hermes. Donc voilà, il y a vraiment pas
mal d'informations à checker. J'avoue,
il y a quand même pas mal de parties
encore que je connais pas. Euh surtout
que je suis pas dev donc il y a plein de
choses, je galère et du coup j'envoie un
message à Claude. Surtout n'hésitez pas
quand vous quand vous discutez avec
Hermes, n'hésitez pas à lui poser des
questions et n'hésitez pas aussi à
pluguer directement Cloud Code
directement sur votre VPS. [musique]
De mon côté, je me suis créé un dossier
sur mon PC, voilà qui s'appelle Hermes.
Globalement, c'est un résumé de tous mes
agents. Donc là, j'en ai qu'un seul.
Donc j'ai mis un mon seul agent qui
s'appelle Merlin d'ailleurs pour ceux
qui ont la ref et ensuite j'ai mis un
fichier de configuration cloud qui
explique globalement le but de ce
dossier. Donc c'est globalement de
manager toute la partie configuration de
mes agents qui sont sur mon VPS. Si vous
voulez je pourrais vous partager ce
prompt dans le school si vous êtes
intéressé. Et j'ai mis aussi une
thématique sécurité avec les bonnes
pratiques pour sécuriser son VPS parce
que vous pouvez mettre notamment des par
feux. Vous pouvez avoir différents
niveaux de sécurité pour VPS [musique]
pour pas que les gens puissent se
connecter à ce dernier. Donc pareil, je
pourrais vous le partager aussi. Voilà
la partie environnement avec les
différentes clés et cetera. Et si je
clique sur mon agent, pareil, il y a une
partie pour environnement avec toutes
les différents identifiants de connexion
de mon agent. Donc là, ce qu'on va
faire, c'est qu'on va directement
utiliser Cloud. Juste petite info pour
vous montrer comment ça marche avec
Visual Studio Code. J'ai créé aussi un
projet Hermes sur le même VPS que celui
que j'utilise actuellement. Ça, je peux
ajouter directement à mon projet Visual
Studio Code et vous montrer comment ça
marche. Donc, ça y est, l'agent est créé
juste ici. Donc là, je peux dire
maintenant euh peux-tu m'ajouter un
nouveau dossier dans ce projet ? J'ai
créé un nouvel agent sur le même VPS.
Son nom est tac dans Hostinger,
tu peux l'appeler Dumbledor. Et donc là,
normalement, il va me l'ajouter
directement dans le projet. Donc là, il
y a un petit peu toutes les informations
qui a dans ce dossier pour pouvoir
reproduire la même chose. Et donc le
fait de pouvoir travailler comme ça, je
trouve que c'est beaucoup plus propre
d'avoir vraiment nos agents qui sont
séparés et ça fait sens aussi du coup de
travailler comme ça par rapport au fait
de travailler aussi sur un docker avec
différents containers un par agent parce
que dans 6 mois quand tu auras un agent
bah pour la finance par exemple un pour
le marketing, un pour la partie
commerciale je sais pas si tu vas avoir
plusieurs agents dans ta boîte ou faire
autre chose mais en gros tu veux qu'il
soit vraiment isolés que chacun ait leur
propre clé à pays pour leurs
utilisations précises et qu'ils aient
aussi chacun bah leur propre mémoire
leur propre skill voit chacun des
containers un peu comme un bureau dans
lequel votre agent travaille et voilà
votre VPS un petit peu de l'immeuble
avec tous les bureaux dedans. Donc là on
peut voir sur le côté qui m'a créé mon
petit fichier, mon petit dossier
Dumblore avec les différents fichiers
environnement dans lequel je peux mettre
bah toutes mes clés API et livre à moi
d'en rajouter par la suite aussi et je
mets aussi mon username et mon password
ici pour ne pas les oublier. Donc c'est
aussi un avantage. Dans tous les cas,
tout est stocké sur mon PC. Et après,
comme vous avez pu le voir, comme j'ai
mis mes identifiants de connexion dans
la partie environnement de mon projet,
Cloud a accès à mon serveur et peut
checker bah les différents agents qui
sont dessus, voir leur statut et cetera.
Et donc comme ça, dès que j'ai la
moindre question sur un agent qui
fonctionne pas ou une question tout
simplement lui poser sur l'état de mon
serveur, faire un els check, donc un
état de la santé euh ou alors ajouter de
la sécurité, j'ai juste à discuter avec
Claude dans cet espace-là et il s'en
occupe. Hop toi, je tout de suite pour
que tu penses à liker et à t'abonner car
tient de ouf la chaîne et on se retrouve
tout de suite dans la suite de la vidéo.
Donc pendant qu'on discutait, ça y est,
notre agent est actif. Voilà juste ici.
Et ce qu'on peut faire maintenant, c'est
qu'on peut directement y accéder soit en
l'ouvrant. Et dans ce cas-là, si on
l'ouvre, on peut se connecter avec nos
identifiants, soit via le terminal. Donc
si j'ouvre le terminal, voilà, juste
ici, juste à taper Hermes. Et donc là,
il me demande de lancer le setup et
j'appuie sur Oui. Donc là, quick setup.
Et donc là, c'est là où ça a changé.
Maintenant, il faut se connecter
directement bah sur le site de Hermes.
Donc, c'est newsresearch.com.
Et voilà, on va cliquer sur le le lien
directement. Donc voilà, une fois qu'on
est connecté, donc là avec la
souscription gratuite pour le coup, on
peut fermer cette page là. Ici, on a
accès à différents outils gratuits. Donc
ça c'est plutôt cool aussi. On peut
faire de la recherche et l'extraction
avec Fireoll. Fireoll qui est un très
bon outil. Euh j'ai même hésité à vous
en faire une vidéo euh parce que
j'utilise pas mal avec Nenamment pour
faire l'extraction euh de différents
sites euh pour tout ce qui est
prospection et enrichissement de lead,
donc de prospect pour les entreprises.
Donc c'est assez intéressant. génération
d'images Fé, vous connaissez aussi, je
l'ai fait pas mal sur la chaîne. Euh
voilà, globalement ici on installe en
local pour le coup parce que c'est déjà
dans un container hostinger. Ensuite, on
setup la messagerie. On a accès à
vraiment beaucoup de channels de
discussion notamment Telegram qui est la
façon la plus simple de se connecter.
Donc là, voilà, j'appuie sur se
connecter avec Telegram et après quand
on appuie sur rentrer, attention, il dit
que tout est bon mais on ne s'est pas
encore connecté avec Telegram. Euh je ne
sais pas pourquoi à chaque fois ça me
fait ça. Après, une chose à savoir, vous
avez vu, on peut choisir du coup une
version payante de la souscription euh
pour Hermes, mais vous pouvez aussi
ajouter un provider externe. Donc si
vous avez déjà une souscription chez
Entropic, déjà des crédits chez Entropic
par exemple ou alors une souscription
chez Open AI, et bien vous pouvez
directement la pluguer. Et l'avantage de
la souscription chez Open AI, c'est que
pour le coup, ça consomme pas de crédit,
ça consomme juste votre usage de votre
usage quotidiennalier
et c'est plutôt pratique. Donc pour ça,
vous allez dans le terminal, vous tapez
Hermes modèle. Voilà comme ça. Et là,
vous voyez, vous pouvez choisir le
provider. Donc là, news portal, c'est
celui par défaut qu'on a dû choisir en
se connectant. Mais si on descend un peu
là, on a open ici par exemple et je vais
appuyer sur entrer. Donc on est avec
Open AI Codex qui est notre abonnement.
Et donc là, on a juste à lancer cette
euh on a juste à cliquer sur ce lien et
se connecter avec notre compte. On
rentre le code qui est indiqué sur le
terminal, on clique sur continuer et on
est connecté à Codex. On dit qu'on
utilise GBT 5.5 qui est le modèle le
plus puissant et ça y est, on
[grognement] a euh notre modèle DIIA euh
qui est voilà puissant sans avoir besoin
d'utiliser bah la souscription de Hermes
[musique] agent. Voilà, on peut lancer
Hermes. Maintenant, on peut bien voir
qu'on est sur GPT 5.5, donc c'est
parfait. On peut lui dire "Hey, comment
vas-tu ?" Et là, il devrait pouvoir nous
répondre. Donc là, l'agent se lance, on
peut voir qu'il raisonne. J'aime bien
les petits emojis sur le côté, c'est
toujours marrant. Ça va bien, merci. Et
toi, comment vas-tu ? Super. Donc ça
c'est bon.
Maintenant, il reste plus qu'à setup
Telegram. Vu qu'on l'a pas fait avant,
ça ne fonctionnait pas.
Donc là, ce qu'on va faire, c'est qu'on
va exit, on va taper Hermes agent Hermes
gateway Setup.
Voilà, on va aller sur Telegram et on va
configurer Telegram. Ici, [musique] on
peut soit se connecter avec un QR code
directement avec Telegram, c'est facile,
ou alors la version manuelle que je vais
vous montrer ici [musique] euh qui est
plus complexe, mais si vous pouvez pas
faire la première version, et bien je
vous montre avec celle-là au moins comme
ça vous êtes setup. Donc là, faut que je
donne le Telegram token. Donc c'est ce
qu'on va faire ensemble. Donc là, je
vais directement dans Telegram et on
peut voir que j'ai je discute avec le
botazer qui est déjà une discussion que
l'on a naturellement dans Telegram et je
vais directement lancer une commande qui
est slash newbot. Voilà, vous faites
slash, vous avez new bot juste ici. Donc
là, il va vous dire de créer un nouveau
bot. On va l'appeler ici YouTube Hermes
test. Il faut toujours que ça finisse
par bot, je crois. Donc pour un bot. OK.
Bon, on va l'appeler la même chose du
coup parce que la première fois, c'était
juste le nom et en fait, on va l'appeler
exactement pareil. Voilà. YouTube bot.
OK. Donc ça va être YouTube euh point
hermes.bot.
Ah attention quand vous créez un pseudo
de votre bot, un username, il faut que
soyez tiré du bas. On recommence.
YouTube Hermes bot. Voilà, c'est bon,
notre bot est créé. Super. Euh donc là,
on a maintenant notre token access qui
est juste ici. Donc on peut cliquer
dessus pour le copier. Et maintenant, je
vais dans Telegram bot token sur mon
terminal et je colle. J'appuie sur
entrer. Ensuite, faut ajouter son user
ID. Donc c'est quelle personne est
autorisée à discuter avec le bot. Donc
en l'occurrence, c'est moi-même. Et pour
ça, faut que je trouve mon ID. Pour
trouver mon ID, il faut que je message
une personne en question. Donc un bot
qui s'appelle user infobot. Donc là, je
ressors Telegram, je retourne et je vais
dans user infobot juste ici. Et je lance
juste la discussion slashstart et je
récupère mon ID. Voilà, je peux le
coller juste ici. Et donc j'indique que
mon utilisateur est donc la source de
confiance. Donc là, je dis oui et ça y
est, Telegram est configurer. J'appuie
sur donne et je peux donc restart la
configuration pour pouvoir appliquer les
changements. Ensuite, on va taper Hermes
gateway pour relancer bah du coup la
gateway, donc l'espace pour pouvoir
interagir entre Hermes et nos
plateformes pour pouvoir être sûr. Donc
là, on peut voir que c'est en train de
démarrer tout simplement. Donc là, on
attend. Bon là, on peut voir que la
Hermateway ne démarre pas. Donc petit
problème euh les allé du direct. Donc ce
qu'on va faire c'est qu'on va stopper
euh press contrôle C tout stop.
Ce qu'on va faire c'est on va carrément
relancer le terminal. On va lancer
Hermes. Voilà donc de retour sur MS et
on va lui dire on a un souci avec la
gateway. Peux-tu investiguer ? Je
n'arrive pas à la démarrer. Donc
toujours quand vous savez pas, vous
discutez avec l'agent et il va trouver
une solution. Méthode la plus simple.
Bon, j'avais trop faim, je suis désolé.
Je me suis fait un petit plat de pasta,
c'est incroyable. Bon, pendant ce temps,
vous pouvez voir ici, il y a Hermes qui
a tout corrigé. Donc, théoriquement, la
connexion avec Telegram est bonne. On va
checker ça. On va ouvrir Telegram. Voilà
notre petit bot qui est juste ici.
Est-ce qu'il va enfin nous répondre ? Je
vais lui envoyer "Hey, comment ça va ?"
On voit le message et on peut voir que
il est en train de taper. Super. Et et
il nous répond. Ça va très bien merci.
Et toi, comment tu vas ? Ça y est, on
est connecté avec notre petit agent qui
est dans un serveur très lointain et on
peut interagir avec lui n'importe où sur
notre téléphone via Telegram. Donc ça
c'est vraiment trop cool. C'est hyper
satisfaisant je trouve. Donc là c'est
super. Et donc maintenant on peut
discuter avec lui, lui lancer des tâches
des cron pour qu'il puisse agir tous les
jours, tous les les semaines et cetera.
On peut faire globalement ce qu'on veut.
On peut donner aussi une personnalité à
notre agent comme je vous ai montré
précédemment avec le fichier sous le
pointm
et par rapport à ça donc j'ai un petit
use case qui est très marrant. J'ai créé
un prompt qui va transformer notre agent
en orc. Je sais pas si vous avez déjà
joué à mais voilà il y a des orcs dans
W. Donc là je vais lui donner le fichier
en question. Voilà. Et je vais lui dire
euh je veux que tu rentres ce prompt
dans ton sou.md.
Voilà, on va voir ce que ça va donner.
Donc là, c'est toujours sympa. On voit
qu'il est en train de checker les skills
en question. Il est en train de trouver
le fichier sous le point MD. Il va lire
notre document et il va s'imprégner du
prompt en question. Donc là, c'est
parfait. Il a imprégné le prompt et
maintenant de mon côté juste à faire
slash restart. Voilà. Et ça va
redémarrer normalement. OK. Donc la
gateway a été relancée et donc là je
peux lui dire hey et on peut voir qu'il
me répond directement ex nouvelle
personnalité. Je suis Troxer Boulon org
de la horde celui qu'on appelle quand
les machines du campement déconnent. Sur
quoi tu veux qu'on travaille aujourd'hui
? Je peux dire là maintenant quelles
sont tes passions ? Et globalement il me
répond avec sa [musique] thématique
propre à lui. Donc ça c'est plutôt cool.
Donc ça c'est pour la partie sous le
pointm. Euh ensuite, je peux lui dire
euh au fait, je suis Julien
AI Automation spécialiste et je euh
déteste les avocats par exemple. Voilà,
on peut dire ça. Et donc là, ce qui est
intéressant c'est qu'on peut voir qu'il
rentre ça dans la mémoire et la mémoire
user comme je vous ai montré
préalablement. Donc on a la mémoire
utilisateur. Donc c'est vraiment adapté
précisément à l'utilisateur en question.
Euh si maintenant je dis je suis euh
Claude par exemple et je suis je sais
pas journaliste, ben dans ce cas-là, il
va créer un autre utilisateur et en
fonction de la personne avec qui il
parle, il va s'adapter. Et ce qui est
très marrant, c'est qu'on peut voir
qu'il garde tout le temps sa
personnalité. Euh le totem des ancêtres
s'en souviendra de donc c'est voilà
classique. Si vous avez joué AO, vous
savez euh ce que c'est. Pour ce qui est
de la partie mémoire, donc là on a pu
voir que notre agent a ajouté
globalement qui on est dans la partie
utilisateur, donc user.md donc c'est qui
je suis. Et il y a aussi donc la partie
mémoire.
MD qui est le contexte de la discussion
générale. Donc il y a à partir de ce
moment-là, il y a un cercle vertueux qui
apparaît [musique]
qui s'enchaîne et parce que ces
informations là sont ensuite chargées
dans le système prompt à chaque
discussion. Donc il se souvient de qui
on est, mais aussi plus on va discuter
avec lui et plus ce dernier va se mettre
à jour euh pour pouvoir enrichir les
informations. Et une autre force pour
moi de ce Hermes messagent, c'est qu'en
fait il y a des limites sur le fichier
user MD et memory MD une limite de
caractère. Donc 1300 environ pour le
fichier user et 2200 pour la partie
mémoire. Ce que ça fait c'est dire que
si un moment on attend bah l'espace de
stockage de ce fichier donc si on le
remplit à 100 % et bien en fait il va
commencer à trier les informations et
garder uniquement les plus pertinentes.
Donc c'est pour ça que plus on va
discuter avec lui plus va remplir les
informations et plus ensuite il va
garder les plus pertinentes pour pouvoir
vraiment avoir un profil qui nous décrit
à 100 %. Donc c'est vraiment la force de
ce message agent je trouve selon moi.
Bref, donc là on voit que notre agent
est setup. On a le souol. MD. Donc il a
sa propre personnalité, il est en train
de construire au fur et à mesure sa
mémoire utilisateur et au fur à mesure
de nos discussions, il va construire ses
skills. Maintenant, ce qu'on va voir,
c'est comment installer une sécurité par
rapport à tes projets parce que Hermes
va générer du contenu, il va travailler
dans des projets et en fait on veut
garder une mémoire de tout ce qu'il a
fait quelque part pour au cas où il
arrive un truc à un autre agent, d'un
coup il débloque, il crème le serveur,
peu importe, on veut pour être capable
de récupérer cette information
directement. Et donc pour ça en fait ce
qu'on va créer un repositories donc un
répertoire sur Github pour stocker
toutes les informations de quand
celui-ci va travailler et on veut qu'il
puisse bah poucher les informations par
exemple tous les soirs à minuit. Voilà,
tu mets les informations de tout ce que
tu as fait aujourd'hui sur Geub comme ça
[musique] il garde la trace. Donc là
directement dans Hermess je peux lui
indiquer ce prompt salut je veux que tu
mettes l'état complet de tout ce que tu
as fait aujourd'hui vers un repository
guitup privé tous les soirs à minuit
hors de Paris. Avant ça tu fais les
recherches dans tes documentations pour
comprendre comment t'y prendre. Tu crées
un point git ignore. Donc ça c'est un
dossier pour pouvoir éviter de push des
informations sensibles et tu m'expliques
ce dont tu as besoin. Voilà, on appuie
ensuite sur entrer. Donc ça y est, après
pas mal de temps à cogiter, je pense
qu'il a cogité pour après 6 7 minutes,
il me donne les informations suivantes.
En gros, il a trouvé globalement comment
il faut faire et donc en gros ce qu'il
veut globalement c'est juste que je lui
donne un token gitub du repos du
repository privé que je veux. Donc
voilà, ça peut être celui-là par exemple
et je lui donne ensuite une autorisation
d'écriture. Une fois que j'ai fait tout
ça, je lui rentre les informations et il
va me créer mon repository sur GitHub et
stocker les informations tous les soirs
à minuit. Donc je pense que c'est
vraiment une bonne pratique à mettre en
place si vous voulez sécuriser bah votre
historique de travail avec votre agent.
Donc vous combinez ça et vous combinez
aussi du coup euh le cloud code qui a
accès du coup globalement à votre
serveur, à votre VPS et vous êtes plutôt
paré en terme d'aide et en terme de euh
et en terme de sécurité tout simplement
pour conserver l'historique de travail.
Et à partir de ce moment-là, ben en
fait, vous pouvez demander n'importe
quoi à votre agent. Dans tous les cas,
il va créer donc le chrome en question
et stocker toutes les informations dans
votre repository au cas où il y a un
souci au niveau du serveur. Donc pour ce
qu'il en est du chron, globalement, tu
écris un langage naturel quand tu
discutes avec lui, tu lui dis tous les
soirs à minuit, bah pousse euh tout ce
que tu as fait de la journée sur le
repository Kitub, il va créer le chrome.
Donc c'est ce qu'on a vu. Euh et donc
faut juste donner les différentes
informations. Donc comme par exemple le
gitub access token, donner les
permissions et cetera. Et on peut
ensuite vérifier notre chron directement
avec la commande Hermes chron list juste
ici. Et ensuite euh à l'heure en
question, il va exécuter la tâche et
potentiellement nous livrer le résultat
sur Telegram si on lui a demandé. Euh
information très importante, c'est
Tesclé API ne les donnent jamais dans le
chat parce que l'information elle est
ensuite envoyée à Open AI dans ce cas-là
par exemple. Euh et euh ces informations
doivent aller uniquement dans le fichier
pour environnement qui est le fichier où
vous stockez toutes euh vos variables.
Et pour euh stocker ça directement, vous
utilisez euh la commande RMS config 7.
Euh vous donnez le nom de la variable en
question. Donc là, c'est le GitHub
access token et vous mettez espace et
vous mettez la variable. Et donc là, ça
va mettre directement l'info dans le
fichier pour environnement sans passer
par le chat et votre message agent
pourra ensuite appeler cette variable là
directement. De mon côté, pour vous
donner un exemple, j'ai déjà créé donc
un chrome qui va checker un petit peu
les vidéos YouTube des gens dans ma
niche et cetera, afin d'identifier bah
les vidéos qui performent le mieux
pourir potentiellement me donner des
idées de vidéos. Donc je trouve ça trop
fun de pouvoir travailler avec un agent
comme ça qui est sur un serveur.
Franchement, j'apprends beaucoup et j'ai
encore beaucoup à apprendre aussi.
J'espère pouvoir vous transmettre des
informations qui vous sont utiles au
travers de mes vidéos. Je pense qu'il y
aura encore pas mal de vidéos autour de
ces agents parce que je vais essayer de
développer pas mal de choses autour.
J'ai fait pas mal d'automatisations
autour de cet agent-là, mais j'aimerais
voilà créer un agent qui soit expert en
trading, plus précisément sur
Polymarket. Je sais pas si vous
connaissez. Alors oui, c'est pas dispo
en France mais ici c'est dispo à
Danemark. Donc je vais me faire plaisir
et je vais tester ça. Et si ça vous
intéresse, je pourrais vous transmettre
les informations peut-être dans une
future vidéo ou directement sur le
school. Voilà, n'hésitez pas à me dire
en commentaire si ça vous intéresse
d'avoir les résultats de cet agent. Donc
le mindset à garder, c'est qu'il faut
vraiment que tu traites cet agent comme
un employé à part entière. Et un employé
à part entière, tu donneris pas tes mot
de passe, tu lui créé ses propre compte.
Donc c'est une bonne sécurité à faire
quand tu travailles avec un agent, c'est
de lui donnerà des identifiants
particuliers pour lui. Si tu veux lui
donner accès à une boîte Gmail, tu lui
donnes tu lui crées une boîte Gmail
particulière. Et si tu veux qu'il traite
tes mails, ben dans ces cas-là, fais en
sorte de forward les emails à cette
nouvelle boîte mail par exemple. C'est
beaucoup plus sécurisé. Pareil, si tu
lui donnes une clé API avec des crédits,
bien mets-li un budget mensuel sur la
clé API pour pas qu'il consomme tout au
cas où. Donc fais vraiment attention à
ça et pense aussi à toutes les choses
qui pourraient mal se passer. Alors
c'est globalement la loi de Murphy. S'il
y a une probabilité que un truc échoue,
bah ça échouera. Donc il a une petite
chance que votre agent bah fasse de la
merde globalement si on peut dire les
termes. Donc c'est à vous d'anticiper
toutes les possibilités afin d'éviter
qu'une catastrophe se produise. Aussi
dans un premier temps, commence par te
familiariser avec son fonctionnement et
se pose la question si à un moment tu
vas te créer un second agent et bien
pose-toi ces questions-là. Est-ce que la
tâche que tu veux lui confier a besoin
de clapé différente de celle de ton
[musique] agent principal ? Si oui ben
potentiellement créer un nouvel agent.
Est-ce qu'elle a besoin de mémoire
séparée ? Dans ce cas-là, tu peux aussi
créer un nouvel agent. Et enfin, est-ce
que c'est un travail récurrent ? Alors,
dans ces cas-là, tu peux aussi
potentiellement créer un nouvel agent.
Enfin, pour finir, j'ai compilé tout ce
qu'on a vu dans cette vidéo dans un seul
et même document qui est complet et je
le mets à disposition dans la communauté
school gratuite. Et si tu as testé MES
ou tu as envie de tester, bah n'hésite
pas à en discuter en commentaire ou dans
la commu. Dans tous les cas, pareil,
j'apprends aussi et je suis sûr qu'on
arrive à faire pas mal de choses en
apprenant les uns des autres. Allez,
c'était Julien et je te dis à la
prochaine pour un autre tuto. Allez, à
plus.


