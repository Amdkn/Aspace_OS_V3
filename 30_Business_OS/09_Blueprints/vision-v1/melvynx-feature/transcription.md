Quand tu crées un SAS, maintenant que ce
soit un SAS B2B ou B2C ou peu importe,
ce qu'il va falloir et encore plus si tu
es en B2B, c'est de faire en sorte que
ton SAS soit AI natif. C'est exactement
le travail qui m'a pris le plus de focus
quand il s'agit de l'email. App de
newsletter et ça paye parce que des
utilisateurs qui utilisent cette app
quotidiennement sont justement des gens
qui n'ont pas envie de devoir se faire
hein, on va dire. Il
ils se font chier à utiliser une app, à
faire des workflow, à cliquer et cetera
et qui veulent utiliser tout ça en agent
native. Mais faut savoir que pour faire
du agent native, il y a quatre points
très importants qu'on va falloir qu'il
va falloir voir. Alors, la premier point
qu'on voit ensemble, c'est la
documentation et le fait que les gens
doivent savoir que tu peux faire ça en
agent. Donc moi ici, je te montre mon
écran, l'email, run your newsletter on
autopilot with AI agent. Donc c'est la
promesse moi de M SAS hein. Et c'est
comme ça que j'ai aussi construit mon
SAS, c'est que moi envoyer des emails,
gérer les emails, c'est un enfer. Je
fais tout le temps des erreurs et je
dois t'avouer qu'aujourd'hui c'est la
seule fois où j'ai fait un truc à la
main et j'ai fait une connerie. Quand
Lee a fait, elle fait pas de conneries.
Et donc toi, ton but ça va être de
mettre en avant sur ton sas que Lia peut
tout faire. Maintenant, une fois que Lia
peut tout faire dans les agents, tu vas
avoir différentes doc. Donc moi ici,
j'ai euh des docs pour Codex. Run email
marketing from Codex. Et ce qu'il va
falloir faire dans vos sas, c'est faire
en sorte qu'on puisse one shot
l'installation. Donc là, tu scrolles, tu
copies cette ligne dans euh ton dans
dans dans ton dans ton chat. C'est ça
hein. Install plugin pas this into
codex. Tu copies ça, tu l'envoies dans
codex ou dans le terminal juste ici
hein. Donc pou. Alors là, évidemment, on
est avec Cloud. Tu dois pouvoir venir
avec Clude Code te dire "OK, j'ai envie
d'installer." Tu copies cette ligne, tu
viens dans le terminal, tu lui envoies
doit être capable de faire toute
l'installation soi-même. On veut pas que
quelqu'un ait besoin de bosser pour
venir installer quoi que ce soit. Tu
peux voir que l'agent va de manière
autonome fetch la page. Et donc ici, on
peut voir que le plugin a été installé,
environnement de checkin, et cetera et
cetera. Et j'arrive pas à le stopper. Il
ne veut plus s'arrêter de bosser. Mais
ici, on peut voir que on a pu installer
ceci. On peut voir ici, il nous dit il
manque une étape, c'est de venir ouvrir
l'email et de faire en sorte de se
connecter. Ici, je vais lui dire de
continuer. Mais tu peux voir qu'en fait,
on va non seulement onboarder
l'utilisateur dans l'utilisation de
notre outil, on va le mettre en avant et
on va faire en sorte que ce soit le plus
simple possible. Donc en règle générale,
tester et faites en sorte que le setup
des agents IA fasse création du compte,
setup, ajout des autorisations et
cetera. On va aussi pouvoir ajouter
évidemment ça dans les plugins et dans
tout ce que tu veux. C'est pour ça que
tu peux faire des docs surtout dans les
documentations. Moi, j'ai aussi fait ici
AI Integration. Il y a un tutoriel pour
l'installer avec Airmes. Donc on a ici
le skill que tu peux installer
directement depuis l'outil. installer ça
et en clair, tu copies cette page, tu
l'envoies à Hermes. En espace de 10
secondes, tout ton tout ton setup lumil
est fait. OK, c'est magique, c'est
fantastique et c'est comme ça qu'on
vient créer vraiment un outil AI natif
et qui permet à l'agent de fonctionner.
Ça c'est le premier point. Deuxième
point, c'est de gérer deux choses et
c'est ça qui est assez compliqué. Quand
on crée une app comme le mail, on va
vouloir faire en sorte que notre agent
soit à plusieurs endroits. Le premier
endroit, c'est le inup. Alors, où est-ce
que c'est le inap ? C'est tout
simplement quand je viens ici sur une
des organisations que j'ai pour envoyer
des emails. On va se rendre compte que
moi ici, j'ai le ici, on peut demander
ici sur leil par exemple, euh on peut
venir poser la question "Ouvre-moi la
dernière campagne que j'ai créé et ici
ouvre directement un une dialogue comme
ceci, un AI assistant qui vient ici
faire ce que tu veux." Donc ça c'est le
inup. Pour faire du inap, on utilise
certaines technologies, par exemple le
TSTAC AISDK ou le Versel AI SDK.
Ensuite, en plus du INAP, on va avoir le
CLI skill. Donc il faut que depuis
n'importe quelle app juste ici, on
puisse envoyer euh l'email h login. Ça
permet de nous login. On va aussi avoir
l'email euh subscriber getmelvinmal à
gmail et boom. Tu peux voir ici que je
reçois tout la définition de ce que je
peux avoir avec les fields et cetera et
cetera. Donc on a le CLI, on a le skill.
Donc le skill, il est sur euh
github.com/lummailopensource.
Euh on a le cloud plugin, on a le codex
plugin, on a les skills et dans skill on
a l'email plugin, on a le skill pour le
plugin, on a aussi le skill pour euh le
CLI et tout ça est setup juste ici. Donc
ça évidemment va falloir le faire.
Ensuite, il va falloir faire le MCP. Et
le MCP à deux manières hein, c'est soit
MCP et aussi le MCP H. Donc le fait de
pouvoir vous connecter. À quoi ça va
servir le MCP ? Ça va servir ici à faire
en sorte qu'on puisse euh se connecter
via par exemple chat GPT. Donc si on
ouvre chat GPT, on peut voir ici, je
peux lui dire va sur l'email
a reçu melvinmal@gmail.com
en dernier. Et là, tu peux voir que
grâce au MCP, grâce au fait qu'il ait un
système d'authentification via MCP H,
l'agent est capable d'aller sur l'email,
chercher les informations, s'occuper de
tout ce qu'il faut pour venir te
retourner des trucs. Donc
malheureusement et heureusement sûrement
parce que ça marcherait pas en CLI. Le
CLI, c'est bien, c'est bien pour open,
c'est bien pour les trucs locales, c'est
bien pour tout ça parce qu'on a pas
forcément envie que quand on code notre
agent se fasse bouleverser avec 200
milliards de tools qui proviennent
directement de l'email. Mais tu peux
voir ici que je reçois directement ici
le le le message que je viens de
recevoir directement contrôlé par chat
GPT. Pourquoi est-ce que c'est contrôlé
par Chat GPT ? C'est parce que j'ai
setup le MCP MCP H. Et le dernier point
c'est l'PI. Donc évidemment tout doit
être setup. Donc ça c'est le deuxième
point, tout setup comme ceci et que tout
soit complet. Maintenant le troisème
point c'est comment vous construisez vos
skill et vos tools. Faut savoir que dans
tous les cas quand on parle de contrôler
un SAS,
c'est principalement le fait de pouvoir
contrôler et accéder à beaucoup
d'outils. Chacun des outils, moi je les
ai définis. Donc si je touvre ça juste
ici avec le mail, moi j'ai défini ça
dans des description descriptors. Donc
des descriptors.
Hop. Donc on va avoir ici tool et on va
avoir des tools definition. Et ici dans
les tools definition, je vais avoir tous
les tools qui sont juste ici. Donc par
exemple, je vais avoir tag tool et dans
les tag tools, je vais avoir des outils
comme delete tag, get or create tag,
list tag, create tag. Ça ça va être les
tools pour les tags. Ensuite, on va
avoir d'autres tools et cetera. Et ce
que j'ai fait pour rendre l'IA plus
intelligente, surtout quand par exemple
elle doit modifier campagne tool, ici il
y a énormément d'outils dans la campagne
create campagne et cetera qui parle de
comment est-ce qu'on crée une campagne,
quel est le contenu, quel est le style
et cetera et cetera. Tout ça, ça devient
assez compliqué. Elia avait tendente de
faire des des des erreurs. Donc pour
optimiser et maximiser euh Lia, il va
falloir faire plusieurs choses. Donc tu
peux voir qu'ici on a un une peleté de
tools qui sont juste ici euh qu'on ferme
mais on va avoir du coup le campaign, on
va avoir create campaign, get campaign
et cetera et on va avoir un autre tool
qui est un skill juste ici qui va
éduquer lia sur comment utiliser X ou Y
outil. Donc là encore une fois si on
s'amuse à tout fermer, on va avoir des
workflow skill, onboarding, variable,
template et copywriting. Donc c'est
copywriting qui explique comment écrire
les campagnes, quelle partie des
campagnes est intéressante et cetera et
cetera. Ensuite, même dans l'outil qu'on
a vu juste avant, c'est-à-dire campaign
tool, il va falloir optimiser les
tokens. Les campagnes, c'est beaucoup de
gon parce que il y a tout simplement ce
qu'on appelle tip tap. Tip tap, c'est un
outil pour bu la campagne. Et moi, je me
suis retrouvé en fait à quand je
demandais à Lia de mettre à jour ses
campagnes à avoir des choses horribles,
avoir Lia qui travaille beaucoup trop
longtemps parce que elle doit venir
effectuer x ou Y chose. Et c'est pour ça
que j'ai mis dans le edit campaign
normalement. Donc là, typiquement, j'ai
créé un outil qui s'appelle edit
campaign où il a deux modes, il a direct
update ou operation. À quoi ça sert ? Ça
permet au modèle de venir juste ici
quand je vais dans l'application, quand
je suis dans les campagnes ici, si je
lui dit change le texte du bouton par
"Hello mon ami," on va avoir dans
l'optimisation de votre outil le fait
d'avoir des outils qui lui permettent de
faire des actions en prenant le moins de
token et le moins de temps possible. Ça
vous économise de l'argent à vous et ça
vous économise à tout le monde. Donc on
peut voir ici que dans le edit campaign
qu'il a fait juste ici, il a écrit
operation node button attribut hello mon
hello mon ami et ici on peut voir qu'il
a remplacé la node avec une opération
directe sans avoir besoin de réécrire
l'intégralité de l'email. Et tu peux
voir qu'ici ça s'est modifié. Donc là on
va faire de l'optimisation. On va non
seulement éduquer le modèle sur quel
outil il peut utiliser et comment est-ce
qu'il peut créer un email, ce qui va
être intéressant. Mais en plus, on va
lui donner des outil qui lui permettent
d'optimiser son contexte. Au lieu de
devoir tout modifier, il pourra modifier
que des petites parties. C'est
exactement ce que j'ai fait juste ici.
Ensuite, dans l'architecture, tu peux
voir qu'ici chacun des outils utilise
ici define tool. Ce define tool, c'est
des fonctions custom que j'ai créé qui
permettent ici de définir des outils.
Ensuite, quand j'ai ces outils, vu que
en fait ces outils sont utilisés dans
les MCP, dans le skill, dans le
terminal, dans le CLI et cetera, je me
suis dit je peux pas juste avoir ces
outils et être bloqué. Parce que si
j'utilise juste ces outils comme ça et
euh et et que je dois en créer un pour
la PI et du coup tu as une route qui
crée une campagne. Donc si si on reprend
hein, si si on fait ces trucs qu'il y a,
tu as une route euh get pour récupérer
la liste des campagnes. Tu as un
MCP/campaign
pour récupérer les campagnes et tu as
ensuite un skill plus CLI qui doit aussi
récupérer les campagnes. Peut-être via
LAAPPI, on sait pas. Tu te retrouves
avec du code dupliqué x 2 milliards. Tu
te retrouves avec un truc complètement
bloqué et on se dit comment est-ce qu'on
peut faire pour éviter ça. Réponse que
j'ai trouvé, c'est d'utiliser un define
tool qui soit du code custom juste ici.
Et tout ce que je te dis ici, c'est
aussi ce que j'ai setup pour ma boiler
plate que tu peux retrouver sur
mlv.sh/fn
pour formation stack. Donc c'est la
stack que j'ai utilisé dans la majorité
de mes SAS qui permet de faire tout ça.
Mais donc dans ce SAS, j'ai setup
exactement la même chose qu'ici. Donc
des outils qu'on va pouvoir définir. Et
ensuite, on va avoir des adapteurs qui
transformment ces outils, donc ces
description d'outils avec description et
cetera, en des outils réutilisables.
Donc par exemple, on va avoir campaign,
on va avoir adapteur. Ça c'est
l'adapteur qui permet de transformer mes
outils pour qu'il fonctionne dans le
chat. Juste ici, on va avoir API
adapteur qui permet de transformer mes
outils en API routes accessible à tout
le monde et MCP adapteur pour que mes
tools soient aussi disponibles via MCP.
Donc d'une seule définition, je suis
venu extrader euh trois adapteurs qui
permettent en fait de tout connecter. Et
donc ce qui se passe ici, c'est qu'on se
retrouve avec mon application, l'email
qui a des adapteurs qui lui permet de
récupérer donc depuis les tools, ça
permet de transformer les tools ici en
API roots, en MCP et en MCP haute parce
que de toute façon ça s'est géré du
niveau du MCP en l'UMLCLI avec les
skills et inap. Tout ça via une seule
définition. Alors à quoi ça sert ? C'est
que les deux servent un peu des causes
différentes. Le skill plus vont être
perfait pour open cloud cloud open open
clow/mes/cloud
code/codex.
Ça va être juste incroyable pour faire
le setup de tout ça. Et le MCP ça va
être super pour le plugin Cloud et
Codex. Donc typiquement si tu as envie
d'être dans la marketplace de chat GPT.
Alors, si tu vois de quoi je parle,
c'est la liste des plugins qui sont
juste ici. Et ben, tu vas avoir besoin
d'un MCP pour être un plugin juste ici.
Si tu as envie d'être dans la
marketplace aussi de chat GPT comme j'ai
montré juste ici pour chatter juste ici,
tu as aussi besoin d'être en MCP et plus
précisément en MCP au HS. Donc, il va
falloir les deux pour vraiment pouvoir
satisfaire tous tes clients sur toutes
les choses. Et donc, ça c'est le dernier
point. il faut être partout et donc bien
structurer ton agent IA pour qu'il
fonctionne partout. Pour ça, moi du coup
les tips que j'ai à te donner c'est
optimisation du contexte. Donc au lieu
de venir bourrer dans la description des
outils, en sachant que la description
des outils va être lu par le modèle tout
le temps, et ben on va plutôt le bourrer
dans des sortes de skill. Donc moi en
fait si tu regardes quand je mets à jour
ou quand je demande certaines choses, tu
vas voir que ici il vient utiliser des
skills. Get skill gets email templates.
Donc là hop skill copywritter. Et donc
au lieu de venir bourrer le contexte
dans le contexte principal, on va venir
ici utiliser des skills. Donc des skills
ou ce qu'on peut appeler du contexte, ça
permet à l'agent de venir pool du
contexte uniquement quand il en a
besoin. Donc typiquement sur les
workflow, toute la documentation de
workflow, au lieu de la mettre dans la
description et que ça pollue
complètement mon IA, et ben je l'ai créé
dans un skill. Et s'il y a appelle de
manière incorrecte la création de
workflow, je lui dis va lire le skill
parce que là tu fais n'importe quoi. Et
il va lire le skill et ça marche super
bien. Ça fait de l'optimisation de
contexte. Ensuite, on va avoir
l'optimisation des outils. Donc
évidemment, si tu as euh qu'un seul
outil qui permet par exemple de
remplacer toute la campagne, si la
campagne fait 2000 token, c'est-à-dire
que chaque fois que doit remplacer un
mot, il doit venir output 2000 token.
Or, si tu crées un outil comme moi,
update campagne avec une sorte de
syntaxe bulk qui lui permet de faire
replace blabla par je suis cool et ben
en fait là il est en train d'économiser
un nombre de tokens immense juste en
faisant de l'optimisation de d'outils et
en appelant le bon outil au bon moment
au lieu d'appeler le mauvais outil pour
rien. Donc ça ça va être très
intéressant et ça tu peux le pousser sur
plein de choses. Les workflow aussi, moi
j'ai poussé avec plein d'outils dans
tous les sens. l'analyse de données, on
va aussi pouvoir définir des paramètres
dans le CLI. Est-ce que tu as besoin de
détail ? Est-ce que par défaut tu as pas
envie de afficher le minimum syndical
pour éviter le polluer le le contexte de
de l'IA et qu'ensuite il a un paramètre
détaillette pour afficher tous les
paramètres, tous les trucs et cetera et
avoir toutes les données. Tout ça faut
bien réfléchir et faut faire des tests
pour voir quand est-ce que Lia arrive à
réaliser tout ça de la manière la plus
efficace et la plus
consistante possible parce que
évidemment on a un problème c'est que
Lia est parfois aléatoire donc ça va
marcher chez toi, ça va pas marcher chez
quelqu'un d'autre. Typiquement aussi
LIA, elle va pouvoir faire des erreurs.
Donc moi, ça m'arrive des fois que Lia,
en fait, elle se retrouve à mal utiliser
mon app et à faire des bugs alors que
c'est impossible de faire ça avec l'UI.
Donc, il va bien falloir définir dans
les outils des workflow et cetera. Et
ensuite, sécurité. Donc moi, typiquement
sur l'envoi de campagne, il y a une
étape de sécurité. Quand Lia essaie de
d'envoyer une campagne, ça va lui dire
"Attention, donne-moi le code." Ça va
lui dire "Attention, c'est une action
destructive. Euh voici un code et ça
donne un code, par exemple euh un code à
six chiffres et ça lui dit "Renvoie-moi
l'appel avec le code et si je reçois à
nouveau l'appel avec le code,
j'exécuterai l'action. Mais par défaut,
je refuse de d'effectuer l'action parce
que par exemple, si tu me dis euh
supprime une campagne et ben ici, elle
va lui demander ça." Souvent, ça va
permettre à Lia de s'arrêter et de venir
demander à l'utilisateur, tu vois ? Donc
ici, finalement, je me rends compte dans
le chat juste ici, j'ai aucune des
actions qui sont interdites, qui sont
disponibles. J'ai dû tout simplement les
cacher de ce chat, mais ils sont bien
disponibles. Il y a le MCP et plutôt la
logique
directe qui sont ici parce que je vois
que les restes à pia sont pas
disponibles et c'est plus précisément
uniquement dans le MCP qu'il a ce code
de confirmation. Anyway, on peut voir
ici que on a tout ça et je vous
conseille de vraiment faire attention à
tout ça. Dites-moi si vous l'avez déjà
implémenté et partagez votre SAS
agentique comme ça je pourrai l'ajouter
à mon agent parce que j'ajoute tous les
sas et mon agent c'est littéralement
tout faire. On se dit à bientôt. Ciao
ciao.