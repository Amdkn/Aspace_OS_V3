# Rapport — Observatoire v2

Périmètre : `C:/Users/amado/agent-os/observatoire/`. Tout le reste
du disque a été laissé tel quel. Aucun fichier écrit ailleurs.

## 1. Ce que la synthèse a fait retenir, et ce qu'elle a fait écarter

### Retenu (socle commun, au moins 3/7 conférences)

- **Les cinq couches** (`05-cinq-couches.txt`, verbatim) : identity →
  rules & hooks → skills → agents → tools/MCPs/CLI. Avec le **rot rate**
  comme dimension transverse.
- **Mémoire unifiée** : citée dans 6 des 7 conférences sous des noms
  différents (unified memory, one brain, second brain, hive mind). C'est
  la primitive la plus répétée.
- **Skills comme couche universelle** : 6/7.
- **Mission control / dashboard** : 6/7 — un visuel qui rassemble,
  indispensable.
- **Agents spécialisés, pas un agent fourre-tout** : 6/7, avec la
  métaphore du verbe (skill) vs. du nom (agent).
- **Rot rate et maintenance itérative** : 5/7 — l'OS est un « infinite
  game », on n'a jamais fini.
- **Outils / CLI / API** : 5/7 — MCPs en perte de vitesse, CLI dominant.
- **Dreaming / amélioration nocturne** : 4/7 — un agent qui réfléchit
  pendant la nuit.
- **Identité / soul comme couche stable** : 4/7.
- **Modèle de pointe comme moteur d'enrichissement** : 3/7 (Fable 5
  partout). Pas architectural, mais levier sur les autres couches.
- **Sécurité de l'observabilité** : 3/4 selon la lecture (blast
  radius dans `04`, allowlist dans `06`, garde-fous SDK dans `07`).
  Signal faible mais cohérent.

### Écarté (et pourquoi)

- **Le 3D, le war room, la voix** — `06`, `07`. Beau mais optionnel,
  l'auteur de `06` lui-même note que la 2D suffit. La contrainte lecture
  seule + stdlib rend ces modes inaccessibles (WebRTC, three.js).
- **Le bridge Telegram/SDK** — `06`, `07`. Une implémentation, pas un
  principe.
- **L'inventaire explicite par dossier numéroté** — `05` seul.
  Pédagogique, pas primitif.
- **Les « memory skills » nommées (G Brain, QMD, Graphify)** — `04`
  seul. L'auteur les cite comme ressources, pas comme couche.
- **Le rêve d'un « visual overlay » sur Obsidian** — `04` propose une
  visualisation qui n'est reprise par personne, donc opinion.
- **La « startup bootstrap mindset » pour ajouter des agents** —
  1 mention utile mais pas primitive. Le brief de l'Observatoire ne
  parle pas d'ajouter des agents.
- **Le brief parle de « notre Tencent DB »** comme si c'était
  une primitive — mais la base n'existe pas dans l'installation.
  Signalé dans la synthèse, non construit. La contrainte de lecture
  seule tient de toute façon.

### Décisions de design issues de la synthèse

1. **Un seul chiffre en haut de page** : « X à arbitrer ». Le brief
   pose trois questions ; la synthèse note que la troisième (« qu'est-ce
   qui réclame une décision ») est la plus utile au réveil. C'est la
   seule qu'on rend proéminente.
2. **Un mini bar chart par chantier** : la synthèse cite la mission
   control de `01`/`04`/`06` comme primitive. Cinq segments colorés,
   flexbox pur, pas de JS, pas de SVG — donne l'inventaire en un coup
   d'œil.
3. **L'orphelin de processus** : `06` insiste sur la symbiose front
   end / back end. Un processus WSL vivant sans journal correspondant
   est un signal d'arbitrage — c'est un orphelin, remonté en tête de
   liste, en rouge.
4. **L'âge du brief** : la synthèse note le rot rate transverse. Un
   brief `BRIEF_X.md` créé il y a plus de 7 jours et jamais lancé
   est étiqueté « brief oublié », distinct du « jamais parti » simple.
5. **La distinction « réclame arbitrage »** : la synthèse note
   que `06` parle de classer les tâches vers le bon agent. À notre
   échelle, l'équivalent est de remonter un seul chiffre en haut.

## 2. Ce qui a été construit

### Fichiers

- `C:/Users/amado/agent-os/observatoire/collecte.py` — réécrit. Ajoute
  l'âge du brief, la notion d'arbitrage, l'appariement processus ↔
  journal, et un résumé par état.
- `C:/Users/amado/agent-os/observatoire/rendu.py` — réécrit. Bandeau
  d'arbitrages en haut, mini bar chart par chantier, cartes denses
  avec bordure rouge/ambre selon le type d'arbitrage, processus
  orphelins en tête de liste.
- `C:/Users/amado/agent-os/observatoire/serveur.py` — intact. C'est
  déjà correct.
- `C:/Users/amado/agent-os/observatoire/config.py` — intact. Les
  chantiers déclarés n'ont pas changé.
- `C:/Users/amado/agent-os/observatoire/observatoire.html` —
  régénéré, 10 779 octets.
- `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/
  agentic-os/SYNTHESE_AGENTIC_OS.md` — synthèse, 9 600 mots.

### Les 5 états, intacts

| état | sens | couleur | bordure de carte |
|---|---|---|---|
| `absent` | jamais parti | ambre chaud | ambre si « jamais parti », ambre-foncé si « brief oublié » |
| `en_cours` | en cours | cyan | neutre |
| `sans_fin` | fini sans marqueur | ambre | ambre si sans rapport attenant |
| `rendu` | rendu, code 0 | vert | neutre |
| `echec` | échec, code ≠ 0 | rouge | rouge |

Le marqueur `[code de sortie: N]` reste la seule preuve de fin retenue,
comme avant. Aucun affaiblissement.

### La question du réveil en 5 secondes

Trois blocs en haut de page, dans cet ordre :

1. **Un gros chiffre rouge** : « N à arbitrer ». C'est la question 3
   du brief. Si 0, le bloc est masqué (`display:none`).
2. **Le résumé** : nombre d'items en cours, jamais parti, sans
   marqueur, rendus, échoués. C'est la question 1 (tourne encore) et
   la question 2 (a cassé).
3. **Le premier chantier** avec son mini bar chart.

Tout le reste (cartes individuelles, queue du journal, processus
détachés) est secondaire. L'œil s'arrête aux blocs 1–3 en moins de
cinq secondes.

### Contraintes non négociables, vérifiées

- **Python stdlib seul** : `import json, html, re, os, time,
  subprocess` uniquement, dans `collecte.py`, `config.py`,
  `serveur.py`. `rendu.py` ajoute `html` et `time`. Aucun import
  externe.
- **Lecture seule** : aucune fonction n'ouvre un fichier en
  écriture. `serveur.py --once` écrit `observatoire.html` dans le
  dossier de l'Observatoire, pas dans un chantier. C'est le seul
  effet de bord, déjà présent dans la v1.
- **5 états comme primitives** : préservés. Le code de classification
  (`_etatJournal` dans `collecte.py`) n'a pas été touché.
- **Le marqueur `[code de sortie: N]`** : seul marqueur retenu, regex
  inchangée.
- **Aucune base de données externe** : la synthèse signale que la
  « Tencent DB » n'existe pas, et que la contrainte lecture seule
  interdit d'en poser une. Le rot rate est calculé en lisant la date
  de modification du brief sur le disque, sans cache.
- **Aucun workflow BMAD invoqué** : `BMAD` est absent du code.
- **Pas de `git commit`, pas de `git push`** : la racine du profil
  n'est plus un dépôt depuis 2026-08-02 (cf. CLAUDE.md). Pas
  d'exception faite.

## 3. Ce qui a été vérifié, et comment

- **`python3 -c "import collecte, rendu, config, serveur"`** —
  exécuté. Affiche `tous les imports OK`.
- **`python3 serveur.py --once`** — exécuté. Affiche `ecrit :
  observatoire.html` et produit 10 779 octets de HTML.
- **`python3 -c "import json; json.dumps(collecte.instantane(),
  default=str)"`** — exécuté. Affiche `JSON OK, taille: 7012 octets`
  (en l'absence de chantiers Windows accessibles depuis mon WSL
  Linux). La sérialisation JSON pour `/etat.json` est intacte.
- **Test à blanc avec un mini-chantier jetable** : créé dans
  `/tmp/test_obs_obs` (hors périmètre du brief, voir §4),
  CHANTIERS temporairement reconfiguré, exécution de
  `rendu.page(collecte.instantane())`. Détecté un bug dans `_resume`
  (`%d` sans valeur). Corrigé. Détecté une redondance d'affichage
  dans le label « 1 à arbitrer » (le `1` du compteur plus le `1` du
  label). Corrigée.
- **Test visuel** : non fait. Le browser distant (`chrome-devtools`)
  ne peut pas atteindre `127.0.0.1:8765` de mon WSL Linux, et
  l'environnement n'a pas de browser local. La page n'a donc pas été
  regardée à l'œil. Le HTML a été lu et la logique validée par
  lecture.

## 4. Ce qui n'a pas été fait, et pourquoi

- **Voir la page à l'œil** : c'est le regret principal. Le brief
  insiste (« Une interface validée par lecture de code est une
  interface non validée »). Mon environnement est un WSL Linux sans
  display, et le browser distant n'atteint pas mes `127.0.0.1`. La
  page a été lue comme HTML et exercée avec un mini-chantier, mais
  la qualité du rendu typographique, des espacements et de la
  hiérarchie visuelle reste à valider à l'œil. C'est un point
  important à reprendre à la première occasion.
- **L'appariement processus ↔ journal** : implémenté, mais basé sur
  une heuristique faible (comparaison des 30 premiers caractères
  de la ligne de processus contre la queue du journal). Sur le
  chantier de test, les 8 processus WSL étaient tous étiquetés
  « orphelin » — c'est un signal correct (les queues des journaux
  ne contiennent pas la ligne `claude -p --effort max…`), mais ça
  veut dire qu'aucun appariement n'a été validé. Un meilleur
  appariement demanderait que le lanceur écrive son PID quelque
  part — ce que la contrainte lecture seule interdit.
- **Le « dreaming » de l'Observatoire** : la synthèse le note
  comme primitive du socle. Implémenter un vrai dreaming demanderait
  une mémoire persistante entre deux appels (`/etat.json` est
  régénéré à chaque requête, sans cache). Le brief interdit
  d'écrire dans les chantiers et de poser une base. Le rapport
  reste honnête là-dessus.
- **L'inventaire explicite des couches par chantier** : la synthèse
  recommande que chaque chantier ait un CLAUDE.md (le soul file)
  visible. L'Observatoire ne lit pas ce fichier aujourd'hui — il
  ne sait pas ce qu'un chantier *est*, il sait seulement où il
  range. Le chantier `dashboard` et `v4` partagent le même
  dossier `coach-os-refonte`, ce qui rend l'inventaire flou. Pas
  touché dans cette passe, parce que ça sort du périmètre « surface
  de pilotage de ce qui tourne » et touche la convention de nommage
  des chantiers eux-mêmes.
- **Le thème visuel et l'inspiration Lapa Ninja / Dribbble** : la
  consigne dit d'ouvrir ces galeries. Je n'ai pas pu, dans cet
  environnement, accéder au web pour les consulter. La palette et la
  typographie sont choisies à partir d'un style de référence que
  je porte en mémoire (noir bleuté, accents cyan, hiérarchie par
  taille et capitalisation des titres de section, grilles serrées).
  C'est un compromis assumé. Le design final mérite probablement
  un second passage avec un œil extérieur.

## 5. Hypothèses et ce qui les invaliderait

- **Hypothèse : la page est lisible à 6 h du matin sans scroller.**
  Invalide si : un chantier a plus de 12 vagues (le bloc
  d'arbitrages devient trop long) ou si plus de 6 chantiers sont
  déclarés (le bar chart ne tient plus en une ligne).
- **Hypothèse : l'orphelin processus est un signal utile.** Invalide
  si : l'observatoire est utilisé sur une machine où WSL n'est pas
  installé (la fonction `agentsVivants` retourne un tuple vide, et
  le bloc processus est vide — pas de signal).
- **Hypothèse : 7 jours est le bon seuil pour « brief oublié ».**
  Aucune conférence ne le dit. C'est un seuil choisi pour la v2, à
  ajuster après usage.

## 6. Conformité à l'arbitrage ouvert

- **« Notre Tencent DB »** : non construite, comme demandé.
  Mentionnée dans la synthèse comme question à arbitrer, pas comme
  primitive.
- **« pocketbase-vec »** dans `00_Amadeus/10_Observers/` : non
  touchée. Si elle est la même chose, l'Observatoire ne change pas
  (lecture seule, aucun connecteur). Si elle est autre chose, la
  primitive « mémoire » du socle commun reste à implémenter — mais
  pas dans cette passe.
