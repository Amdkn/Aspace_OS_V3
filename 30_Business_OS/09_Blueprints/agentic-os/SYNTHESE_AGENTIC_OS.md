# Synthèse — sept conférences sur l'OS agentique

Lecture des sept transcriptions (`01-self-improving.txt` à
`07-remplace-openclaw.txt`), 28 000 mots, à `C:/Users/amado/ASpace_OS_V3/
30_Business_OS/09_Blueprints/agentic-os/transcriptions/`.

Ce document répond à trois questions et seulement à celles-là. Les points
qui ne reviennent qu'une fois sont signalés comme opinions, pas comme
primitives.

---

## 1. Les cinq couches (`05-cinq-couches.txt`)

`05-cinq-couches.txt` les présente du centre vers l'extérieur, sur le
modèle de la croute terrestre : plus c'est profond, plus c'est stable ;
plus c'est en surface, plus c'est sujet au « rot rate » (le rythme auquel
chaque couche devient obsolète). Mots de l'auteur, pas les miens.

| # | Couche | Ce que c'est | Stabilité |
|---|---|---|---|
| 1 | **Identity** | Le « soul file ». `soul.md`, `agents.md`, `cloud.md`. La personnalité, le ton, le « point of view », l'inventaire des autres couches. Chargé une fois, modifié à la marge. | **La plus stable** — coût initial le plus haut, mis à jour le moins souvent. |
| 2 | **Rules and hooks** | Règles (suggestions fortes au modèle : « only give me feedback about X ») et hooks (la seule partie *déterministe* — attachés à un événement, ils tirent toujours). | Modérée. On les découvre après avoir vu le modèle se tromper. |
| 3 | **Skills** | Workflows / slash commands. Processoriented (« monthly close ») ou functional (« pull latest Fathom transcript »). Le verbe de la couche 3, comme l'agent est le rôle de la couche 4. | Haute, mais pourrit vite — à mettre à jour chaque semaine selon l'auteur, surtout quand le modèle change. |
| 4 | **Agents** | Quand des skills agrègent un rôle, on « materialise » un agent. Senior tax strategist, fractional CFO. Hire slowly, comme une startup bootstrappée : « what is the best absolute first hire? ». | Pourrit *le plus vite* — chaque nouveau modèle a un comportement différent, le prompt devient daté. |
| 5 | **Tools, MCPs, CLI** | La « data layer ». Accès live : CRM, QuickBooks, Google Calendar. APIs et CLIs, parce que les codecs (Claude Code, Codex) sont forts dans ce domaine. MCPs « on their way out » selon l'auteur. | Change quand les APIs changent ou sont dépréciées. |

Une sixième dimension traverse les cinq : le **rot rate** — le rythme
auquel chaque couche devient obsolète. L'auteur recommande un fichier
qui le déclare explicitement (« identity : 6 mois, tools : continu »)
plutôt que de le redécouvrir.

C'est tout. `05-cinq-couches.txt` ne mentionne pas d'autres couches.
`03-fable5-agentic-os.txt` reformule les mêmes cinq couches (« across
five levels »), mais comme niveaux d'enrichissement par Fable 5, pas
comme une réécriture du modèle.

---

## 2. Ce qui revient dans au moins trois conférences

Sept vidéos, 28 000 mots, 27 mentions que je compte comme socle commun
quand elles apparaissent trois fois ou plus. Le reste est une opinion
d'un auteur à un moment — utile mais pas primitif.

### Socle commun (apparait dans au moins 3 des 7 conférences)

**La mémoire unifiée (« one brain », « second brain », « hive mind ») —
6/7.** `01`, `02`, `03`, `04`, `06`, `07`. C'est la primitive la plus
répétée. Le vocabulaire change (« unified memory », « shared memory
state », « one brain », « memory palace »), l'idée ne bouge pas : un
même état accessible depuis tous les points d'entrée (Claude Code,
Hermes, Telegram, dashboard, mobile). `04` lui consacre une vidéo
entière — la mémoire est un graphe du workspace, pas un grep amélioré.

**Les skills comme couche universelle — 6/7.** `01`, `02`, `05`, `06`,
`07`, et mentionnée dans `04`. Skills globaux vs. skills projet, à
graduer (« what deserves to graduate to a global skill »). C'est
l'unité de travail atomique, qu'on assemble ensuite en agents.

**Un dashboard / mission control — 6/7.** `01`, `02`, `03`, `04`,
`06`, `07`. Le visuel importe : on *regarde* l'OS, on ne le tape pas.
`06` le pousse plus loin (Kanban + 3D + war room), `01` insiste sur
« one place to see everything ».

**Les agents spécialisés (vs. un agent fourre-tout) — 6/7.** `01`,
`02`, `03`, `05`, `06`, `07`. Comms, Ops, Research, Main — chacun un
domaine, une CLAUDE.md, un YAML. `06` formalise le « hire slowly »
qu'on retrouve partout. `05` ajoute la métaphore du verbe (skill) vs.
du nom (agent).

**Le rot rate / la maintenance itérative — 5/7.** `01`, `02`, `05`,
`06`, `07` (mentionné aussi dans `03`, `04`). Le système est un
« infinite game » (`05`, `06`), on n'a jamais fini. L'auteur de
`06` résume : « this is an iterative process ».

**Tools / CLI / API comme couche de données — 5/7.** `01`, `02`, `05`,
`06`, `07`. Les MCPs sont sur leur fin (`05`), le CLI domine. L'accès
live aux données est universel.

**Dreaming / amélioration nocturne — 4/7.** `01`, `03`, `06`, `07`.
Un agent qui réfléchit pendant que le propriétaire dort, qui passe
les conversations en revue, qui suggère deux skills à fort ROI.
`03` et `07` en font un pilier explicite ; `01` le rêve d'abord.

**L'identité / soul comme couche stable — 4/7.** `03`, `05`, `06`,
`07`. Toujours l'élément le plus stable, toujours en haut du dossier.

**Le model de pointe (Fable 5 dans ces transcriptions) comme moteur
d'enrichissement — 3/7.** `03` (Fable 5 en cinq niveaux), `04`
(Fable 5 construit le second brain), `05` (Fable 5 cité). Ce n'est
pas une primitive architecturale — c'est un moyen d'élever les
autres. Le détail du modèle changera, la place dans la stack reste.

**La sécurité de l'observabilité — 3/7.** `04` (accès au graph view =
blast radius), `06` (chat ID allowlist, PIN, guard), `07` (sécurité
de l'agent SDK). Signal faible mais cohérent : un OS agentique est un
agent à qui on confie ses données, il faut le borner.

### Apparait une ou deux fois — opinion, pas primitif

- **Le 3D et le war room** — `06`, `07`. Beau, pas primitif. `06` lui-même
  note que la 2D est suffisante.
- **La voix** — `03`, `07`. Bonus, pas socle.
- **Le bridge Telegram/SDK** — `06`, `07`. Une implémentation, pas un
  principe.
- **« Dreaming » automatique avec Fable 5** — `01`, `03`. Fonctionnalité,
  pas architecture.
- **L'inventaire explicite des layers par dossier numéroté** — `05`
  seul. Pédagogique, pas primitif.
- **Le brief demande l'inventaire explicite par couleur / cercle / lien**
  — `04` propose une visualisation qui n'est reprise par personne.

---

## 3. Ce qui manque à l'Observatoire actuel

L'Observatoire (`C:/Users/amado/agent-os/observatoire/`) sait
aujourd'hui faire une seule chose : pour chaque brief connu, regarder
s'il y a un journal, et classer le journal dans l'un des cinq états.
Lecture seule, Python stdlib, sans dépendance. Le brief demande ce
qu'il manque au regard du socle commun — voici une liste courte et
honnête, chaque ligne rattachée à sa conférence fondatrice.

1. **Une vue « réveil en 5 secondes » qui sépare trois questions.**
   Le brief impose : *est-ce que quelque chose tourne encore, est-ce
   que quelque chose a cassé, et qu'est-ce qui réclame une décision*.
   L'Observatoire a un résumé en haut, mais il compte les états
   indifféremment — il n'isole pas ce qui *réclame une décision* (un
   brief sans journal, un journal `sans_fin` de plus de 30 minutes
   sans rapport, un agent déclaré vivant qui n'a pas touché son
   journal depuis le plafond). La distinction « surveillance
   d'exploitation » vs « surveillance d'inventaire » est centrale
   dans `06-runs-my-business.txt` (« the front end should always have
   a perfect symbiosis with the back end »).

2. **La notion de rot rate par chantier, ou au moins par brief.**
   Aucune conférence ne dit « un brief vieux de N jours sans journal
   est un signal ». Mais `05-cinq-couches.txt` introduit le rot rate
   comme dimension transverse, et `06` parle explicitement de
   l'inventaire qui se périme. Un brief `BRIEF_X.md` créé il y a six
   mois et jamais lancé est une donnée, pas un oubli — l'Observatoire
   le sait déjà (« jamais parti »), mais il ne le *remarque* pas
   comme tel. Une ligne d'âge sur le brief rendrait cette primitive
   visible.

3. **Une mémoire de l'Observatoire lui-même.** `01-self-improving.txt`
   et `06-runs-my-business.txt` insistent : un OS qui ne se souvient
   pas de ses propres décisions devient muet. L'Observatoire n'a
   aucun fichier d'état entre deux appels — il redécouvre à chaque
   rafraîchissement ce qu'il a découvert la fois d'avant. C'est la
   primitive la moins chère à ajouter (un fichier JSON local), et
   c'est ce qui rendrait le « dreaming » possible si on le voulait
   un jour.

4. **Une vue mission control / dashboard.** `01`, `04`, `06` placent
   tous la visualisation au centre. L'Observatoire a un bandeau de
   résumé et une grille de cartes — c'est correct, mais ce n'est pas
   une *vision globale*. Le brief demande explicitement un thème
   sombre et sobre (gardé), avec densité, hiérarchie, respiration,
   typographie. La grille de cartes actuelle est lisible à 6 h du
   matin, mais elle ne *raconte* rien : elle montre des états, pas
   une situation.

5. **Un lien explicite entre agents vivants et journaux.**
   `06-runs-my-business.txt` insiste : un agent qui n'a pas de trace
   récente n'existe pas. L'Observatoire liste les processus WSL et
   les journaux côte à côte, mais ne les apparie pas. Quand un
   processus est vivant sans journal correspondant, c'est un signal
   (« agent qui ne sait pas où il logge ») ; quand un journal est
   sans processus correspondant depuis le plafond, c'est un autre
   signal (« agent mort sans rendre la main »). Aucun des deux n'est
   isolé aujourd'hui.

6. **La distinction « ce qui est normal » vs « ce qui réclame un
   arbitrage ».** `06-runs-my-business.txt` parle d'un « meta agent »
   qui classe les tâches vers le bon agent. À l'échelle de
   l'Observatoire, l'équivalent serait de remonter un seul chiffre
   en haut de la page : *nombre d'items qui réclament un arbitrage
   humain*. Aujourd'hui le résumé compte tout.

7. **L'identité de chantier comme donnée visible.** `05-cinq-couches.txt`
   et `06` insistent : un chantier sans « soul file » (un CLAUDE.md
   qui dit ce qu'il est, ce qu'il observe) est un chantier qui ne
   peut pas être auto-amélioré. L'Observatoire ne sait pas ce qu'un
   chantier *est* — il sait seulement où il range ses fichiers.

### Ce qui n'est pas un manque, à la lumière des conférences

- **L'observabilité des agents individuels, leurs logs internes, leur
  état de session** — `06` et `07` la poussent, mais c'est le travail
  d'un *autre* outil (l'OS lui-même, ou un agent de supervision).
  L'Observatoire observe les briefs et leurs journaux, pas les
  agents. C'est sa raison d'être.
- **La gestion de base de données / mémoire centralisée** — `04` la
  pousse, mais le brief dit explicitement : « ne suppose pas que
  c'est la même chose que la Tencent DB », et « construis sans base,
  la contrainte de lecture seule tient ». Pas un manque, un
  non-périmètre.

---

## Ce qui a été écarté, et pourquoi

Pour servir la décision de ce qui suit, la synthèse fait des choix
explicites. Ce qui n'apparait qu'une fois dans les sept conférences a
été écarté des primitives : le 3D, la voix, le bridge Telegram, les
briefs de configuration nommés (« 80 % en un weekend »). Ce qui
apparait trois fois ou plus est une primitive à honorer. Ce qui
revient une ou deux fois mais dans le brief lui-même (durée de
rafraîchissement, contrainte lecture seule, 5 états comme
primitives) reste non négociable.
