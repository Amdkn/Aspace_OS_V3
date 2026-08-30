# BRIEF — l'Observatoire devient une vraie surface de pilotage agentique

Tu travailles sur `C:/Users/amado/agent-os/observatoire/`. Perimetre exclusif :
ce dossier. Tu ne touches a rien d'autre sur le disque.

## Ce qui existe aujourd'hui

Une page locale qui liste l'etat des agents MiniMax delegues, lancés detaches
dans WSL — invisibles de tout gestionnaire de taches, d'ou son existence.
Quatre fichiers Python, bibliotheque standard seule, aucune dependance,
**lecture seule**. Lis `README.md` puis les quatre fichiers avant d'ecrire.

Elle fonctionne, mais elle ne fait qu'une chose : afficher des etats de journaux.
C'est un visualiseur de logs. On veut une surface de pilotage.

## Ta premiere tache : lire, puis synthetiser

`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/transcriptions/`

Sept conferences, 28 000 mots, deja sur disque en texte brut :

| fichier | sujet annonce |
|---|---|
| `01-self-improving.txt` | un OS agentique qui s'ameliore lui-meme |
| `02-graphify.txt` | Graphify — le code et le schema en un seul graphe |
| `03-fable5-agentic-os.txt` | un OS agentique bati sur Fable 5 |
| `04-second-brain-fable5.txt` | construire un second cerveau |
| `05-cinq-couches.txt` | **les cinq couches de tout OS agentique** |
| `06-runs-my-business.txt` | une installation qui fait tourner une entreprise |
| `07-remplace-openclaw.txt` | remplacer OpenClaw et Hermes |

**Lis-les vraiment.** Puis ecris une synthese dans
`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/SYNTHESE_AGENTIC_OS.md`.

Elle doit repondre a trois questions, et seulement a celles-la :

1. **Quelles sont les cinq couches** que `05-cinq-couches.txt` decrit ? Nomme-les
   avec les mots de l'auteur, pas les tiens.
2. **Qu'est-ce qui revient dans au moins trois des sept conferences ?** C'est
   ca, le socle commun. Ce qui n'apparait qu'une fois est une opinion, pas une
   primitive — signale-le comme tel plutot que de le retenir.
3. **Que manque-t-il a l'Observatoire actuel** au regard de ce socle ? Une liste
   courte et honnete, chaque manque rattache a la conference qui le fonde.

Ne resume pas les sept videos une par une. La synthese sert a decider quoi
construire, pas a prouver que tu as lu.

## Ta seconde tache : refaire l'Observatoire

Ce que tu construis se decide **a partir de ta synthese**, pas de ce brief. Mais
trois exigences ne se negocient pas :

**1. La contrainte technique reste entiere.** Python, bibliotheque standard
seulement, **zero dependance a installer**, **lecture seule** : l'Observatoire
n'ecrit jamais dans ce qu'il observe. C'est ce qui le rend sur a lancer a tout
moment. `python serveur.py` doit continuer de suffire.

**2. La question du reveil.** Le proprietaire ouvre cette page apres une nuit.
Il doit savoir en cinq secondes, sans scroller : **est-ce que quelque chose
tourne encore, est-ce que quelque chose a casse, et qu'est-ce qui reclame une
decision.** Tout le reste est secondaire.

**3. Les cinq etats existants sont justes, ne les affaiblis pas.**
`jamais parti` · `en cours` · `fini sans marqueur` · `rendu` · `echec`.
Le premier est le plus important : il a revele deux briefs jamais lances que
personne n'avait vus. Un journal qui grossit ne prouve rien ; un processus
vivant non plus. Le seul marqueur de fin retenu est `[code de sortie: N]`.

## Le soin visuel

`C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/coach-os-refonte/barre-welcome/`

Captures de galeries reelles — Lapa Ninja, Dribbble, Awwwards, One Page Love.
Ouvre-les. Elles ne sont pas un modele a copier : elles montrent le niveau de
soin attendu sur une page qu'on regarde tous les jours. Densite, hierarchie,
respiration, typographie.

Le theme actuel est sombre et sobre. Garde cette famille — cette page se lit a
6 h du matin — mais elle merite mieux qu'un tableau.

## Ce que tu ne fais pas

1. **N'ajoute aucune dependance.** Ni Flask, ni FastAPI, ni React, ni Tailwind.
   Si tu penses en avoir besoin, tu as mal compris la contrainte : elle est
   deliberee.
2. **N'ecris jamais dans les chantiers observes.** Pas de fichier de cache, pas
   de base, pas de journal. Si tu veux persister un etat, dis-le dans ton rapport
   et attends l'arbitrage — ne le fais pas.
3. **N'invoque aucun workflow BMAD.** Ils ouvrent une porte « [A] Approve » que
   personne ne peut franchir : la session est non interactive.
4. Pas de `git commit`, pas de `git push`.
5. Chemins **absolus** partout.

## Un point ouvert que tu ne dois PAS trancher seul

Le proprietaire a mentionne « notre Tencent DB » a propos de Graphify. **Je n'ai
trouve aucune base de ce nom** dans l'installation. Il existe `pocketbase-vec`
dans `C:/Users/amado/ASpace_OS_V3/00_Amadeus/10_Observers/` — PocketBase compile
en Go avec l'extension vectorielle `sqlite-vec`. **Ne suppose pas que c'est la
meme chose.** Signale la question dans ton rapport et construis sans base :
la contrainte de lecture seule tient de toute facon.

## Verification

```
python serveur.py --once      # doit ecrire observatoire.html sans erreur
python -c "import collecte, rendu, config, serveur"   # aucun import externe
```

Puis **ouvre la page et regarde-la.** Une interface validee par lecture de code
est une interface non validee : c'est l'erreur qui a coute le plus cher cette
semaine.

## Rapport attendu

Dans `C:/Users/amado/ASpace_OS_V3/30_Business_OS/09_Blueprints/agentic-os/RAPPORT_OBSERVATOIRE_V2.md`.

Ce que ta synthese a fait retenir et ce qu'elle a fait ecarter — **avec les
raisons d'ecarter**, c'est la partie interessante. Puis ce que tu as construit,
ce que tu as verifie et comment, et tout point non fait avec sa raison.

Si tu dois t'arreter avant la fin, ecris quand meme ce rapport avec l'etat exact.
