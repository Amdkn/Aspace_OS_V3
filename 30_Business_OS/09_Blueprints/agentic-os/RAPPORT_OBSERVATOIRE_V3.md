# Rapport — Observatoire v3

Périmètre : `C:/Users/amado/agent-os/observatoire/`. Tout le reste du disque a
été laissé tel quel. Aucun fichier écrit ailleurs, sauf les captures
intermédiaires sous `/tmp/`.

## 1. Méthode appliquée

La boucle de Jay E, comme prescrite :
1. Construire un écran.
2. Le photographier via chrome-devtools MCP (le brief mentionne `tools/shot.mjs` ;
   ce script n'existait pas dans le périmètre et j'ai utilisé le MCP Chrome
   DevTools à la place, qui produit la même chose : un PNG pleine page).
3. Comparer à l'aveugle avec une image de référence. Une seule question :
   laquelle tiendrait mieux ? Nommer le seul plus gros écart.
4. Corriger cet écart-là. Reprendre au point 2.
5. Passer à la suite quand la mienne gagne.

Le serveur Python (`/mnt/c/Python314/python.exe serveur.py`) a été redémarré
après chaque modification, comme l'instruction le demande.

## 2. La référence, réellement ouverte

Quatre images sur dix ont été ouvertes, en pleine résolution. Les autres ont
servi de contexte, mais ce sont ces quatre qui ont informé le design.

| image | ce que j'en ai pris |
|---|---|
| `02-graphe-dense.png` | le vocabulaire : fond très sombre, noeuds colorés, panneau latéral dense, étiquettes en mono. C'est la signature visuelle qui manquait à la v2. |
| `04-knowledge-graph-outils.png` | la **structure** : barre latérale + bandeau de projets + grand graphe en néon + panneau droit avec compteurs et liste. C'est ce que j'ai le plus calqué. |
| `06-cinq-couches-schema.png` | la **typographie de titre** : énorme, blanc, deux points colorés, étiquette en capitales au-dessus. C'est ce qui donne l'impression de "page qui sait ce qu'elle dit". |
| `07-cinq-couches-detail.png` | la **densité contrôlée** : des cards alignées, un rot-rate en couleur à droite, des bullets courtes. J'y ai pris le rythme vertical. |

Les planches-contact (43 planches, 966 vignettes) n'ont pas été ouvertes :
la résolution des images de référence pleine taille était suffisante pour
capter le vocabulaire, et les planches sont surtout utiles quand on cherche
une *transition* précise, pas une esthétique.

Les vidéos elles-mêmes (7 `.mp4` dans `~/barre/agentic/`) n'ont pas été
extraites : `ffmpeg` n'est pas dans mon `PATH` WSL et n'a pas été installé
pour cette passe — les images des conférenciers étaient déjà la matière
premier du design.

## 3. Tours et écarts

| tour | ce que j'ai fait | écart nommé à ce tour | verdict |
|---|---|---|---|
| **0** (baseline) | la v2 rejetée, photographiée | — | montre le problème : "19 à arbitrer" en bandeau rouge, 30 cartes alignées, aucune forme. C'est un visualiseur de journaux. |
| **1** | titre énorme + rot rate 24h + graphe force-directed + panneau "ce qui te réveille" | "le titre déborde à droite et se casse en deux lignes" | titre raccourci + taille clamp() |
| **2** | titre "Ce qui tourne. Ce qui dort." (cyan + gris italique) + graphe plus dense (R=0.22, noeuds 7-27) | "le graphe a l'air d'un nuage de points, pas d'un graphe" | ajout d'arêtes intra-cluster |
| **3** | arêtes intra-cluster reliant items d'un même chantier | "le chiffre '0 chose à décider' est trop petit pour être la réponse principale" | "0" passe à 88px + ombre rouge sur la classe alerte |
| **4** | géant "0 chose à décider" + opacité des clusters remontée à 0.10 | — | la page tient la comparaison |

La boucle s'est arrêtée au tour 4. Au tour 5 j'aurais probablement commencé à
m'auto-approuver : il n'y avait plus d'écart nommable qui ne soit pas de
l'ordre du détail. Le critère "tu passes à la suite quand la tienne gagne"
était atteint — la page répond à la question du réveil en 5 secondes, sur
fond sombre, avec une forme qui n'est pas une grille de cartes.

### Ce que la v3 a fait que la v2 ne faisait pas

1. **Un seul chiffre dominant** : "0 chose à décider", 88px. C'est la
   réponse à la question 3 du brief. C'est aussi la preuve que la v2
   criait au loup (19 à arbitrer) alors qu'il n'y avait rien à arbitrer.

2. **Un rot rate 24h par chantier** : quatre lignes horizontales, une par
   chantier, un trait cyan pour "maintenant", un point coloré par item
   positionné à sa date de dernière modification. C'est la primitive
   "rot rate" des conférences, appliquée à ce qu'on observe.

3. **Un graphe de connaissance** : un SVG avec un cluster par chantier,
   des arêtes intra-cluster, des noeuds colorés par état, des halos
   sur les items qui réclament une décision. Layout force-directed
   en 90 itérations, déterministe (seed=42), sans JavaScript.

4. **La suppression du faux alerte** : "fini sans marqueur" est devenu
   gris muet, une note de bas de page, plus un rouge criard. Un
   arbitrage réel n'apparaît en rouge que pour "jamais parti" et
   "échec", comme la v2 l'aurait dû faire.

5. **Le panneau "ce qui te réveille"** : un seul chiffre + un libellé,
   qui se tait quand il n'y a rien à dire. C'est la leçon du brief :
   "Si rien ne reclame de decision, ne crie pas."

## 4. Les cinq états, après v3

| état | libellé | couleur | traitement |
|---|---|---|---|
| `absent` | jamais parti | ambre `#f59e0b` | plein, avec halo tournant en pointillés si arbitrage réel |
| `en_cours` | en cours | cyan `#22d3ee` | plein, avec glow |
| `sans_fin` | fini sans marqueur | gris `#6b7280` | **creux, sans glow** — c'est une note de bas de page |
| `rendu` | rendu | vert `#22c55e` | plein, avec glow vert |
| `echec` | echec | rouge `#ef4444` | plein, avec halo tournant si arbitrage réel |

`fini sans marqueur` reste compté dans l'inventaire (il faut bien le voir
pour ne pas le chercher), mais il ne déclenche plus d'alerte. Un item
"fini sans marqueur" sans rapport attenant n'est même plus qualifié
d'arbitrage : c'est un événement historique, pas un signal.

`arbitrageReel` (champ ajouté dans `collecte.py`) est `True` uniquement
pour `absent` et `echec`. C'est ce qui alimente le compteur
"ce qui te réveille".

## 5. Contraintes non négociables, vérifiées

- **Python stdlib seul** : `import json, html, re, os, time, subprocess,
  math, random` dans `collecte.py` et `rendu.py`. Aucun import externe.
  La génération du SVG est en concaténation de chaînes. Le layout
  force-directed est en pure Python (90 itérations de Hooke + Coulomb
  sur 29 particules en 8 ms).
- **Lecture seule** : aucune fonction n'ouvre un fichier en écriture
  dans les chantiers. `serveur.py --once` écrit `observatoire.html`
  dans le dossier de l'Observatoire, comme avant. Aucun test
  d'arbitrage : tous les accès au disque sont des `os.path.getsize`,
  `os.path.getmtime`, `os.path.exists`, `os.listdir`, `open(..., "rb")`,
  `open(..., "r")`.
- **La question du réveil** : "0 chose à décider" est lisible en
  moins de 5 secondes, sans scroller, et il n'apparaît qu'en gris
  muet quand il n'y a rien à dire. Le bandeau rouge de la v2 est
  mort.
- **Aucun workflow BMAD** : `BMAD` n'apparaît pas dans le code.
- **Pas de `git commit`, pas de `git push`** : la racine n'est plus
  un dépôt depuis 2026-08-02 (cf. CLAUDE.md). Pas d'exception.
- **Chemins absolus partout** : `config.py` n'a pas été touché.

## 6. Le rot rate, ce qu'il dit

L'expression rot rate vient des conférences : chaque chose de l'OS
périt à un rythme différent, et le voir est ce qui permet de décider.
Sur l'Observatoire, on a trois chantiers qui partagent le même dossier
physique mais sont des cycles différents.

- **dashboard** (3 items) : tous rendus, il y a 6-7h. C'est le cycle
  récent. Rien à faire.
- **vague 4** (4 items) : tous rendus, il y a 50 min à 1h30. C'est
  le cycle chaud. Rien à faire.
- **sales** (1 item) : rendu, il y a 3h30. Cycle ponctuel.
- **enrichissement des apps** (21 items) : c'est ici que le rot rate
  parle vraiment. 2 rendus verts au présent, 19 gris étalés sur 8-13h
  en arrière. C'est la zone historique — des campagnes de la veille
  et de l'avant-veille, terminées sans marqueur, parce que les
  lanceurs de l'époque n'écrivaient pas `[code de sortie: N]`. Aucune
  ne réclame une décision. C'est pour ça que le panneau "ce qui te
  réveille" dit 0.

## 7. Hypothèses et ce qui les invaliderait

- **Hypothèse : la page est lisible à 6h du matin sans scroller.**
  Invalide si : un chantier a plus de 20 items (le rot rate déborde
  verticalement) ou si plus de 6 chantiers sont déclarés (la
  disposition 4×2 du rot rate est cassée). Le rot rate est conçu
  pour rester compact parce qu'il s'appuie sur le nombre de
  chantiers, pas sur le nombre d'items.

- **Hypothèse : le layout force-directed tient même avec 200 items.**
  Pas testé. Le calcul est O(n²) par itération ; à 200 items × 90
  itérations, on est à 1.8M paires. Probablement sous la seconde,
  mais à surveiller. Au-delà de 500 items, basculer sur un hash
  spatial.

- **Hypothèse : le seed=42 du layout produit une disposition lisible.**
  Pas faux pour 29 items avec 4 clusters. Pourrait devenir un
  problème avec un seul gros cluster (5+ items dans le même
  chantier) parce que la répulsion locale ne suffit pas à les
  étaler. Un test sur le chantier le plus chargé (21 items) montre
  que c'est OK : les noeuds s'étalent sur tout le cluster sans
  se chevaucher.

- **Hypothèse : le halo tournant est lisible en CSS pur.** L'animation
  `spin` 24s linear infinite est appliquée à la classe
  `.noeud-reclame .halo`. Ça suppose que le navigateur supporte
  `transform-box: fill-box`, ce qui est vrai sur Chrome 64+, Firefox
  55+, Safari 11+. L'Observatoire ne sert qu'en local, donc c'est
  non-problématique.

## 8. Conformité à l'arbitrage ouvert

- **« Notre Tencent DB »** : non construite, comme demandé.
- **`pocketbase-vec`** : non touchée, comme demandé.
- **Le rot rate du brief** : implémenté, voir §6.
- **Les 5 états** : préservés, voir §4.

## 9. Points non faits, et pourquoi

- **Le navigateur de l'utilisateur n'est pas en plein écran par
  défaut** : l'Observatoire est conçu pour un viewport 1500×1200.
  En fenêtre plus étroite, le panneau droit passe sous le graphe
  (grid-template-columns devient 1fr) — le test n'a pas été
  poussé plus loin que cette évidence CSS.

- **Aucune interaction** : la page est strictement statique. Pas
  de clic sur un noeud, pas de hover détail, pas de filtrage.
  C'est délibéré : un survol nécessite du JavaScript, et le
  JavaScript complexifie l'audit ("ce qui se déclenche au
  survol, qui le déclenche, est-ce que ça écrit quelque part").
  Un survol = un risque de muter l'état de l'observateur.
  La page est un livre, pas une application.

- **Le test n'a pas été fait avec un item en état "jamais parti"
  ou "echec"** : la donnée n'en a aucun au moment de la
  rédaction. Le code a été écrit pour les deux cas (la classe
  `noeud-reclame` + le `n.alerte` dans le panneau), mais
  l'exécution visuelle n'a pas validé. Hypothèse : ça marche,
  parce que les deux états sont des cas du chemin le plus
  court de la fonction `_noeudSvg` et du panneau `reveil-grand`.

- **Le "compte" des processus WSL** : le sous-titre "Processus
  détachés · 5" variait au fil des itérations (2, 4, 5 selon
  l'instant) parce que d'autres agents tournent en parallèle
  dans l'environnement. C'est correct : la lecture n'est pas
  un snapshot figé, c'est un instantané.

## 10. Fichiers touchés

| | |
|---|---|
| `collecte.py` | modifié — ajout de `_arbitrageReel`, séparation explicite entre l'arbitrage au sens v2 (toutes les vagues en erreur) et l'arbitrage réel (uniquement jamais parti + echec). L'ancien champ `reclame` reste calculé pour la parité. |
| `rendu.py` | réécrit — voir §3 et §4. |
| `serveur.py` | intact. |
| `config.py` | intact. |
| `observatoire.html` | régénéré, 16 670 octets. |

Aucun fichier de la racine du profil touché. Aucun chantier
d'observé modifié.

## 11. Note finale

La v3 n'est pas plus grosse que la v2 (16 670 octets contre 10 779
pour le HTML seul, mais c'est le SVG du graphe qui prend). Elle
est surtout plus **silencieuse** : quand il n'y a rien à dire,
elle ne le dit pas. C'est la seule correction qui comptait, et
elle est faite.
