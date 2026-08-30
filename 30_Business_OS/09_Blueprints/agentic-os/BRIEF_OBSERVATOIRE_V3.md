# BRIEF — l'Observatoire, deuxieme tentative : les images d'abord

Tu travailles sur `C:/Users/amado/agent-os/observatoire/`. Perimetre exclusif.

## Pourquoi on recommence

Une premiere version a ete produite ce matin. **Elle a ete rejetee par le
proprietaire du produit**, en un mot : « c'est toujours aussi moche ».

La cause est connue et elle n'est pas de l'agent precedent : **les images
n'existaient pas encore quand il a travaille.** Il n'a eu que les
transcriptions. Le proprietaire avait pourtant dit, textuellement, que les
images sont « presque plus importantes que les transcriptions ». Elles sont la
maintenant.

Le defaut concret du resultat actuel, pour que tu saches quoi ne pas refaire :

- C'est **un visualiseur de journaux avec un meilleur CSS**. Des cartes sombres
  alignees, chacune avec un extrait de journal en chasse fixe. Il y en a
  trente. On ne lit rien.
- Le bandeau **« 19 a arbitrer »** est du bruit : ce sont d'anciennes campagnes
  terminees normalement, dont les lanceurs de l'epoque n'ecrivaient simplement
  pas de code de sortie. Rien a arbitrer. Une alerte qui crie sans raison
  apprend a etre ignoree.
- Aucune **forme**. Pas de graphe, pas de courbe, pas de rythme, rien qui
  distingue un chantier de vingt lignes d'un chantier de trois.

## Les images — regarde-les AVANT d'ecrire une ligne

**Les references retenues**, pleine resolution :
`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/references/`

Dix images tirees des conferences. Les plus importantes :
`01-graphe-connaissance`, `02-graphe-dense`, `03-graphe-panneau-lateral`,
`04-knowledge-graph-outils` — des vues de **graphe de connaissance** sur fond
sombre, points colories par type, panneau lateral de filtres. C'est un
vocabulaire visuel entier, et c'est ce qui manque a l'Observatoire.
`06-cinq-couches-schema` et `07-cinq-couches-detail` montrent comment ces
auteurs representent une architecture en couches.

**Les planches-contact**, 43 planches, 966 vignettes horodatees :
`.../agentic-os/images/<video>/planches/planche-N.png`

Chaque vignette porte sa seconde. Si une planche te montre quelque chose
d'interessant, extrais-le toi-meme en pleine resolution :

```
ffmpeg -ss 00:04:48 -i ~/barre/agentic/02-graphify.mp4 -frames:v 1 -q:v 2 /tmp/x.png
```

Les sept videos sont dans `~/barre/agentic/` cote WSL. Les transcriptions
restent dans `.../agentic-os/transcriptions/` — utiles pour le fond, pas pour
la forme.

## Le protocole — la boucle de Jay E, appliquee pour de bon

C'est la methode du skill `gauntlet-loop` (technique de Matt Shumer, skill de
Jay E chez RoboNuggets), installe dans `coach-os/.claude/skills/gauntlet-loop/`.
Lis-le. Son principe tient en une phrase : **la boucle ne produit de la qualite
que si la chose contre laquelle on compare est reelle.**

La barre est reelle maintenant. Applique la boucle :

1. **Construis** un ecran.
2. **Photographie-le.** Le serveur tourne sur `http://127.0.0.1:8787`.
   Depuis le depot coach-os :
   `node tools/shot.mjs --url "http://127.0.0.1:8787" --out /tmp/o.png --w 1500 --h 1200`
   Le script liste aussi les erreurs de console.
3. **Juge a l'aveugle.** Pose ta capture a cote d'une image de reference,
   etiquettes retirees. **Une seule question : laquelle des deux tiendrait
   mieux ?** Pas de note sur dix — les notes derivent vers le haut a chaque
   tour. Un choix, et **le seul plus gros ecart**, nomme.
4. Corrige cet ecart-la. Reprends au point 2.
5. Tu passes a la suite quand la tienne gagne.

**Sois dur.** L'eloge ne sert a rien. Si tu ne peux pas dire laquelle est
meilleure, c'est que la reference gagne.

Et **redemarre le serveur apres chaque modification** : Python fige ses modules
a l'import, un serveur lance avant ton edition sert l'ancien code. Cette panne
est tombee deux fois aujourd'hui.

## Les trois contraintes qui ne bougent pas

1. **Python, bibliotheque standard seule, zero dependance**, `python serveur.py`
   doit suffire. Si tu penses avoir besoin d'une bibliotheque, tu as mal compris
   la contrainte : elle est deliberee. Un graphe se dessine tres bien en SVG
   genere a la main.
2. **Lecture seule.** L'Observatoire n'ecrit jamais dans ce qu'il observe.
3. **La question du reveil.** Le proprietaire ouvre cette page apres une nuit.
   En cinq secondes, sans scroller : ce qui tourne, ce qui a casse, ce qui
   reclame vraiment une decision. **Si rien ne reclame de decision, ne crie
   pas.** Le bandeau rouge actuel est le contre-exemple.

Les cinq etats restent justes — `jamais parti` · `en cours` ·
`fini sans marqueur` · `rendu` · `echec` — mais **`fini sans marqueur` n'est
pas une alerte**, c'est une note de bas de page sur d'anciennes campagnes.
Traite-le comme tel.

## Ce que tu ne fais pas

1. Aucune dependance. Ni Flask, ni FastAPI, ni React, ni bibliotheque de
   graphes.
2. Aucune ecriture dans les chantiers observes.
3. **Aucun workflow BMAD** : ils ouvrent une porte « [A] Approve » infranchissable
   en session non interactive.
4. Pas de `git commit`, pas de `git push`. Chemins absolus partout.

## Rapport

`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/RAPPORT_OBSERVATOIRE_V3.md`

**Pour chaque ecran : le nombre de tours, et l'ecart nomme a chaque tour.**
C'est la partie qui dit si la boucle a corrige quelque chose ou si elle s'est
approuvee au premier passage. Puis quelles images tu as reellement ouvertes, ce
que tu leur as pris, et tout point non fait avec sa raison.

Si tu dois t'arreter avant la fin, ecris quand meme ce rapport.
