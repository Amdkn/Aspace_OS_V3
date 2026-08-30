# A'Space OS V3 — les règles de travail

**Ici se fait le travail.** Ce fichier porte le *comment*.

> **Le *pourquoi* est à la racine du profil : `C:\Users\amado\CLAUDE.md`.**
> Il énonce les désirs, besoins, problématiques et intentions mesurés du
> propriétaire, et ce qui est attendu d'un exécutant. **Le lire d'abord** : une
> règle appliquée sans savoir ce qu'elle sert produit un exécutant qui obéit et
> ne réalise rien.
>
> Déplacé ici le 2026-08-30. Le fichier vivait à la racine du profil et n'y
> avait pas sa place : il décrit le dépôt, pas le profil.

> **Version intégrale : `40_Memory_Wiki_OKF/canon/CANON-profil-racine.md`.**
> Toute édition de ce fichier se recopie là-bas. Un instantané qui a divergé
> en silence est pire qu'une absence de sauvegarde.

---

## 0. La cartographie mesurée de A'Space OS V3

**C'est la carte du corpus, pas une table de routage.** Mesure du 2026-08-30
par `scripts/cartographier_v3.py` : **10 784 fichiers, 6 565 `.md`, 2,8 Go**. La version pleine (arborescence 3 niveaux, classements)
se régénère dans `CARTOGRAPHIE.md` — ne pas l'éditer à la main.

### Les étages de premier niveau

| Étage | Fichiers | dont `.md` | Poids | Ce qu'il porte |
|---|---:|---:|---:|---|
| `00_Amadeus/` | 5,132 | 4,705 | 228.9 Mo | Ontologie V2, MEMORY_CORE, cartographie des contradictions, sessions |
| `10_Tech_OS/` | 97 | 71 | 2.2 Mo | Gouvernance Rick, cascade E-Myth |
| `20_Life_OS/` | 361 | 291 | 1.0 Go | Domaines de vie migres depuis V2 |
| `30_Business_OS/` | 3,750 | 538 | 1.3 Go | Projets, blueprints, coach-os |
| `40_Memory_Wiki_OKF/` | 38 | 38 | 259.4 Ko | Bundle OKF v0.2 — integrations, operations, securite, learning |
| `50_Distillation/` | 394 | 321 | 70.3 Mo | Methode, substrat, briefs de distillation |
| `60_Implementation_Méthodologiques/` | 173 | 76 | 1.3 Mo | Verdicts du triptyque par domaine |
| `70_Onthologies/` | 396 | 324 | 6.8 Mo | Sujets, triplets RDF, revue |
| `80_Agent-OS/` | 7 | 2 | 64.3 Ko | Observabilite — tableaux de revue et schema de cadence |
| `90-self-evolution/` | 15 | 8 | 68.5 Ko | Skills d'auto-amelioration — une par problematique mesuree |
| `_ARCHIVE_coach-os-briefs/` | 349 | 154 | 109.2 Mo | Briefs archives de coach-os |
| `_INBOX/` | 9 | 5 | 10.9 Ko | Capture GTD, non trie |
| `_REVIEW_NOTEBOOKLM/` | 26 | 26 | 4.7 Mo | 26 sources consolidees pour la revue humaine |
| `scripts/` | 29 | 0 | 243.1 Ko | Porte d'argent, cartographie, generateurs |
| *(racine)* | 8 | 6 | 79.8 Ko | fichiers de tete |

`openwiki/` est exclu des comptes : clone amont avec son propre `.git`, pas
notre corpus.

### L'arborescence profonde

Elle est dans **`CARTOGRAPHIE.md`**, régénérée en 0,4 s — trois niveaux, poids,
jonctions signalées. La dupliquer ici la condamnerait à vieillir : ce fichier
est un relevé daté, la carte se recalcule.

Les quatre pièges qu'elle ne dit pas d'elle-même :
`03_Resources_Geordi/` est un **miroir** (1,0 Go), donc une Ressource et non
l'Area vivante · `20_Harness/bmad-loop/` tourne **dans WSL** · `10_Observers/`
porte 3 jonctions NTFS · `agentgateway/` pèse 95 Mo à lui seul.

### Où vit réellement la connaissance

- **4 647 `.md` sur 6 565 (71 %) sont des vidages de sessions** dans
  `00_Amadeus/30_MEMORY_CORE/sessions_md/`. Compter ça pour de la
  connaissance, c'est se mentir.
- La connaissance **rédigée** : `70_Onthologies/pulse/domaines/` (259),
  `50_Distillation/domaines/` (161), `_ARCHIVE_coach-os-briefs/` (154),
  `30_Business_OS/09_Blueprints/coach-os-refonte/` (194).
- **Le bundle OKF ne porte que 38 `.md` (0,6 % du corpus).** C'est un index
  de concepts consolidés, pas le corpus. Chercher là et s'arrêter, c'est
  manquer le reste.

### Points d'entrée précis

| Question | Où |
|---|---|
| **Où est quoi dans V3, et combien** | **`CARTOGRAPHIE.md`** |
| Rangs, domaines, horizons, verbes | `00_Amadeus/30_MEMORY_CORE/ONTOLOGIE_V2.md` |
| Cascade E-Myth, S1/S2/S3, Donna | `10_Tech_OS/00_Governance_Rick/CASCADE.md` |
| Contradictions déjà cataloguées (204) | `00_Amadeus/30_MEMORY_CORE/carto/CONSOLIDE.json` |
| Distillation, substrat, méthode | `50_Distillation/METHODE.md` |
| Intégrations récentes, pièges d'outillage | `40_Memory_Wiki_OKF/` |
| **Échecs déjà payés, à ne pas rejouer** | **`40_Memory_Wiki_OKF/learning/`** |

**Lire `CARTOGRAPHIE.md` avant de chercher.** C'est l'arborescence profonde de
V3, **mesurée** et régénérable en 0,4 s — étages, poids, jonctions signalées, et
le classement des dossiers par densité de connaissance rédigée. Sans elle, une
session redécouvre la structure à l'aveugle et facture ça au quota.

```bash
python C:/Users/amado/ASpace_OS_V3/scripts/cartographier_v3.py
```

Les comptes de ce fichier sont ceux d'un relevé daté ; **`CARTOGRAPHIE.md` fait
foi** parce qu'il se régénère. Si les deux divergent, c'est ce fichier-ci qui a
vieilli.

**`grep` le corpus entier avant d'affirmer.** Le bundle seul ne suffit jamais.

### Les gardes exécutables — les lancer, pas les relire

Une skill par problématique mesurée dans
[`90-self-evolution/`](90-self-evolution/README.md). Ces scripts **refusent**
quand la règle n'est pas tenue, au lieu de la rappeler.

```bash
python 90-self-evolution/evolution/portes.py                                # les 8 skills
python 90-self-evolution/skills/p1-anti-rejeu/scripts/deja_vu.py "<brief>"  # deja tourne ?
python 90-self-evolution/skills/p7-memoire-travail/scripts/etat.py voir     # ou en est-on
python 90-self-evolution/skills/p8-forum-agents/scripts/forum.py fils       # qui fait quoi
```

`deja_vu.py` avant tout brief — 42,4 % des sessions rejouent une intention, deux
sur trois en août. `etat.py` sur une tâche longue : un objectif ne passe à
`fait` que contre une **preuve d'environnement**, jamais sur « c'est fait »
*(Recuris)*. `forum.py prendre` avant d'agir à plusieurs — il refuse une tâche
déjà prise. `auditer.py` avant de rapporter un chiffre issu d'un script.

---

## 1. Économie de quotas

Les quotas des modèles Anthropic sont la ressource rare. Tout travail long,
répétitif ou volumineux se délègue.

### Le canal de délégation est `claude-glm`

**`claude -p` n'est plus le canal.** Il consomme le quota Anthropic, c'est-à-dire
exactement la ressource qu'on cherche à épargner. Le canal est
`~/.claude/custom-models/claude-glm.cmd` — GLM 5.3 Flash via OpenRouter, hors
quota Anthropic.

```bash
"C:/Users/amado/.claude/custom-models/claude-glm.cmd" \
  --dangerously-skip-permissions \
  --strict-mcp-config --mcp-config '{"mcpServers":{}}' \
  -p "<brief court, qui POINTE vers un fichier au lieu de le contenir>"
```

**Les deux drapeaux MCP ne sont pas optionnels.** Mesure du 2026-08-30 : le
plancher de démarrage est de ~96k tokens d'outillage (195 outils MCP = 60,2k,
outils système 20,9k) sur une fenêtre de 200k. Sans eux, le délégué rend
**`Prompt is too long` avant même de lire son brief** — payé deux fois ce
soir-là. Avec eux, il passe.

**Ne jamais passer un gros corpus dans le `-p`.** Le brief pointe vers un
chemin ; le délégué lit lui-même. Un corpus de 409 Ko dans l'argument échoue ;
découpé en tranches de ~40 Ko lues depuis le disque, il passe.

### Ce qu'un délégué doit savoir de lui-même

**Si tu lis ceci et que tu tournes sous `claude-glm`, ton mandat est le brief
que tu as reçu.** Tu es maître de la façon de l'accomplir : tu choisis tes
outils, ton ordre d'exécution, ta méthode. Tu tranches tout ce que le brief
laisse ouvert **à l'intérieur de sa portée**, et tu écris ton rapport dans le
fichier demandé — c'est ta livraison, elle t'appartient.

Ta portée s'arrête au bord du brief : le travail de la session parente est
**son** mandat. Le reprendre met deux exécutants sur une tâche — quatre
tranches en double le 2026-08-30. Une tâche hors brief que tu juges nécessaire
**s'écrit dans ton rapport** : c'est une contribution, pas une transgression.
Ce jour-là, la cause n'était pas l'excès d'initiative mais l'absence de portée
écrite.

- **Session courante** — décision, arbitrage, vérification. Pas l'exécution.
- **`claude-glm`** — l'exécution longue, répétitive, volumineuse.
- **Outil `Workflow`** — **non**. Les sous-agents héritent du modèle exporté et
  meurent si `ANTHROPIC_MODEL` pointe ailleurs. Orchestrer par `claude-glm`.

**Se délègue** : scans de corpus, lints, migrations, comptages, réécritures en
masse, toute tâche dépassant ~20 appels d'outils ou ~200 fichiers.

**Reste ici** : l'arbitrage, et la vérification du travail délégué.

**Toute affirmation se vérifie contre l'environnement — la sienne comme celle
d'un délégué.** Ce n'est pas de la défiance envers l'exécutant : c'est la règle
qui vaut pour tout le monde, y compris la session qui arbitre. Un `exit 0` ne
prouve rien, d'où qu'il vienne. Un rapport de délégué **accompagné d'un chemin,
d'un `rc=` ou d'un code HTTP est une preuve recevable** ; c'est ce que
`p7-memoire-travail` exige, sans distinction de qui l'apporte. Le 2026-08-30, un délégué a
affirmé « la duplication domine » — c'était vrai, mais c'est le script qui l'a
établi. L'inférence propose, le script tranche.

**Une seule boucle à la fois.** `pkill` ne prend pas toujours du premier coup :
vérifier par `pgrep -fc` avant de relancer, sinon deux boucles se marchent
dessus et brûlent les tranches en double.

> Détail des cinq pièges d'invocation (précédence d'environnement, `PATH`,
> brief en stdin, outillage du dépôt qui détourne, concurrence) :
> `CANON-profil-racine.md` §1.

---

## 2. Vérifier, c'est regarder

Un rapport, un `exit 0`, un journal vide ne prouvent rien. On regarde le
résultat : le fichier, l'écran, le port, la sortie réelle.

**Quand la mesure contredit l'observation directe, c'est l'observation qui a
raison** — et on répare l'instrument avant de conclure. Une sonde qui ne trouve
rien lève une erreur ; jamais de repli silencieux.

Cette règle a été payée cinq fois. Cas typiques, tous vérifiés :

- un filtre `CommandLine -like '*motif*'` **se compte lui-même** ;
- lancer `powershell` depuis bash pour compter des processus **en crée un** ;
- lire une géométrie **pendant une transition CSS** rend une valeur transitoire ;
- une recherche d'un seul côté de la frontière WSL conclut à tort « absent » ;
- un script sans `$ErrorActionPreference = 'Stop'` **annonce un succès après
  l'échec**.

---

## 3. Ne pas polluer la racine

Aucun fichier de travail, script jetable, capture ou dump ici. Les sorties
temporaires vont dans `%TEMP%`.

---

## 4. Où vivent les choses (hors V3)

| | |
|---|---|
| Base de connaissance V2 | `ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/` |
| Secrets | `.claude/_secrets_local/` — **jamais** dans le dépôt |
| MCP | un seul serveur : l'agentgateway, `http://127.0.0.1:3300/mcp` |

**Ne pas éditer `~/.mcp.json`** : il ne contient que le pointeur vers le
gateway. Source de vérité : `00_Amadeus/20_Harness/agentgateway/mcp_sources.json`,
puis `python build_config.py`, puis relancer.

> Les quatre pièges du gateway (une cible morte abat tout, `${env:VAR}`,
> `.cmd` et `PATH`, secrets en clair dans `config.yaml`) :
> `CANON-profil-racine.md` §3bis.

---

## 5. Deux pièges de ce disque

**Jonctions NTFS** — `os.path.islink()` ne les voit pas ; un `os.walk` naïf a
compté 13,8 millions de fichiers là où il y en a 14 613.

```python
RP = getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0x400)
bool(entry.stat(follow_symlinks=False).st_file_attributes & RP)
```

Pour en supprimer une : **`os.rmdir` uniquement**. `rmtree`, `rm -rf` et
`Remove-Item -Recurse` suivent le lien et détruisent la cible réelle.

**Git à la racine du profil** — désactivé le 2026-08-02
(`.git.DESACTIVE_2026-08-02`) : 53 fichiers suivis pour tout le profil
saturaient le CPU. **Condition de réactivation** : un `.gitignore` qui exclut
`AppData/`, `.cache/`, `node_modules/` et les journaux, vérifié par
`git -C ~ status --porcelain | wc -l` < 200. C'est un seuil mesurable, pas un
interdit. Versionner un projet précis n'exige d'ailleurs pas ce dépôt-racine —
`agent-os` a le sien depuis le 2026-08-30, sans effet sur le profil.

---

## 6. Déplacements de fichiers

Scanner les secrets **avant** tout déplacement vers la KB — motifs `sk-`,
`sbp_`, `vcp_`, `ghp_`, `mul_`, JWT, clés PEM, `.env` hors `.example`. Écrire
un `MANIFEST.json` (`src` → `dst`) qui rend l'opération réversible.
**Déplacer, jamais supprimer.**

---

## 7. Ce que l'exécutant doit savoir de lui-même

**Vérifier le modèle réel de la session avant d'écrire un brief.** Un brief qui
contient `claude -p`, un bloc d'exports `ANTHROPIC_BASE_URL`, ou un
`model: 'haiku'` **exige que la session tourne sur un modèle Anthropic** — un
sous-agent hérite du canal du parent, pas du modèle nommé. Erreur payée le
2026-08-15, et **détectable avant de lancer** : `echo $ANTHROPIC_BASE_URL`
vide signifie canal Anthropic, donc `haiku` passe ; une URL locale
(`127.0.0.1:*`) signifie relais, donc nommer un modèle Anthropic échouera.

```bash
grep -E 'claude -p|ANTHROPIC_BASE_URL|model: .(haiku|sonnet|fable|opus)' mon_brief.md
# -> doit etre vide
```

---

## 8. Rang, outil, cadence — trois choses distinctes

| | Ce que c'est | Exemple |
|---|---|---|
| **Rang** | position dans la cascade, avec un horizon | A1 gatekeeper, **H+3 ans** |
| **Outil** | ce qu'un rang emploie | `spec-loop`, `babysitter`, `gstack`, `Ori`, `Herdr` |
| **Cadence** | fréquence d'exécution | 1 m, 5 m, 25 m |

Les écraser rend l'architecture illisible et fait proposer des remplacements
d'étage là où il ne s'agit que d'outillage. Affectation donnée par le
propriétaire : **gstack → B1, superpowers → B2, GSD → B3**.

**État au 2026-08-30 :** `spec-loop` (cadence 1 m, Beth/Morty) tourne — test :
`type %TEMP%\ordonnanceur\etat_1m.md`, relance : `bash A0.sh 4` via
`claude-glm.cmd`. `babysitter` est configuré mais pas installé ; l'installer
est un chemin ouvert, pas une porte fermée. Détail :
`40_Memory_Wiki_OKF/operations/relance-spec-loop-2026-08-30.md`.
