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
par `scripts/cartographier_v3.py` : **10 731 fichiers, 6 531
`.md`, 2,8 Go**. La version pleine (arborescence 3 niveaux, classements)
se régénère dans `CARTOGRAPHIE.md` — ne pas l'éditer à la main.

### Les étages de premier niveau

| Étage | Fichiers | dont `.md` | Poids | Ce qu'il porte |
|---|---:|---:|---:|---|
| `00_Amadeus/` | 5 132 | 4 705 | 228,7 Mo | Observateurs, harness, MEMORY_CORE (sessions), doctrine |
| `10_Tech_OS/` | 97 | 71 | 2,2 Mo | Gouvernance Rick, Donna DLQ, noyaux 11/12/13 |
| `20_Life_OS/` | 361 | 291 | 1,0 Go | Ikigai, Wheel, 12WY, PARA, GTD, D.E.A.L |
| `30_Business_OS/` | 3 750 | 538 | 1,3 Go | Blueprints (coach-os, palantir…), projets appliqués |
| `40_Memory_Wiki_OKF/` | 36 | 36 | 239,5 Ko | Bundle OKF v0.2 — index de concepts consolidés |
| `50_Distillation/` | 362 | 299 | 69,9 Mo | Méthode, briefs, substrat `.jsonl`, distillats de domaines |
| `60_Implementation_Méthodologiques/` | 173 | 76 | 1,3 Mo | Verdicts du triptyque, `_loop`, protocoles |
| `70_Onthologies/` | 396 | 324 | 6,8 Mo | Pulse b1/b2/b3/domaines, sujets, triplets RDF, revue |
| `80_Agent-OS/` | 7 | 2 | 64,3 Ko | Observabilité, schéma de cadence |
| `_ARCHIVE_coach-os-briefs/` | 349 | 154 | 109,2 Mo | Briefs datés 08-09 → 08-17 |
| `_INBOX/` | 9 | 5 | 10,9 Ko | Capture GTD — A1/Beth-Morty, B1/Jerry, S1/Rick, admis/refusés |
| `_REVIEW_NOTEBOOKLM/` | 26 | 26 | 4,7 Mo | 26 sources consolidées pour la revue humaine |
| `scripts/` | 27 | — | 235,1 Ko | Porte d'argent, cartographie, générateurs |

`openwiki/` est exclu des comptes : clone amont avec son propre `.git`, pas
notre corpus.

### L'arborescence profonde des six étages qui portent la connaissance

**`00_Amadeus/`** — 4 705 `.md`, soit **72 % de tout le corpus** :
- `30_MEMORY_CORE/` (4 794 fich.) → `carto/` (contradictions, CONSOLIDE.json)
  et **`sessions_md/` 4 647 `.md` — c'est là que vit la masse** ; c'est du
  vidage de sessions, pas de la connaissance rédigée
- `20_Harness/` → **`agentgateway/`** (95 Mo, source MCP), **`bmad-loop/`**
  (225 fich., tourne dans WSL), `openrouter/`, `routers/`
- `10_Observers/` — stubs d'observabilité (agentpulse, opik, phoenix…), 3 jonctions
- `60_Tape_Specs/` (ADR/PRD/REGISTRY) · `90_Doctrine/adr/` · `30_Shadow/`

**`20_Life_OS/`** :
- `00_Gatekeepers_Beth_Morty/` · `21_Ikigai_Orville/` (pillars + horizons)
- `22_Wheel_Discovery/` LD01–LD08 (LD01_Business_Book : 68 `.md`)
- `23_12WY_SNW/` Vision→Planning→Focus→Metrics→Execution
- `24_PARA_Enterprise/` → `01_Projects_Picard/` · `02_Areas_Spock/` ·
  **`03_Resources_Geordi/` (1,0 Go — le miroir)** · `04_Archives_Data/`
- `25_GTD_Cerritos/` (Inbox→Clarify→Organize→Review→Engage) ·
  `26_DEAL_Protostar/` (D.E.A.L) · `28_Blueprints/`

**`30_Business_OS/`** — 1,3 Go, l'étage le plus lourd :
- `09_Blueprints/` (2 784 fich.) : **coach-os-refonte** (794 fich., 194 `.md`,
  497 Mo), **palantir-2.0** (1 055), agentic-os, vision-v1,
  ontologie-trois-couches, ontologie-vocale, outils-micro-saas, gateways
- `10_Projects/coach-os-app/` (959 fich., 303 `.md`) — le projet appliqué

**`50_Distillation/`** :
- `_substrat/` — **65,5 Mo de `.jsonl`** : la matière première des sessions ;
  `_substrat_domaines/` · `_mesures/`
- `_briefs/` + `_briefs_vague2/` + `_briefs_domaines/` — les briefs de distillation
- `domaines/` (161 `.md` : amadeus, business, life, life-wheel, normatif-adr,
  normatif-sdd-prd, tech, templates) · `areas/` · `projets/` · `ressources/`
  · `ontologie/` · `archives/`

**`70_Onthologies/`** :
- `pulse/` (298 `.md`) : `b1/`, `b2/`, `b3/` + `domaines/` (259 `.md`)
- `sujets/` · `triplets/` (RDF) · `_revue/` · `_structure/`
- `verbes/` — **vide (0 fichier)** : lacune assumée de l'ontologie

**`60_Implementation_Méthodologiques/`** :
- `_loop/` (100 fich.) · `domaines/` · `protocoles/` · `frameworks/` ·
  `prompt-systeme/` · `autonomie-agents/` · `primitives/`

### Où vit réellement la connaissance

- **4 647 `.md` sur 6 531 (71 %) sont des vidages de sessions** dans
  `00_Amadeus/30_MEMORY_CORE/sessions_md/`. Compter ça pour de la
  connaissance, c'est se mentir.
- La connaissance **rédigée** : `70_Onthologies/pulse/domaines/` (259),
  `50_Distillation/domaines/` (161), `_ARCHIVE_coach-os-briefs/` (154),
  `30_Business_OS/09_Blueprints/coach-os-refonte/` (194).
- **Le bundle OKF ne porte que 36 `.md` (0,6 % du corpus).** C'est un index
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

### Ce que la distillation a déjà établi — lire avant de refaire

| | |
|---|---|
| **147 rapports d'agents délégués, 35 vagues, 2,6 Mo** | `INDEX_DISTILLATIONS.md` |
| **Intentions, besoins, problématiques, désirs** (2 307 sessions, mars→août) | `50_Distillation/RAPPORT_INTENTIONS_V3.md` |

Mesure du 2026-08-30 : sur 4 625 documents, **520 seulement (11,2 %) étaient
atteignables** depuis ce fichier, et **117 rapports sur 130 étaient hors de
portée** — pas orphelins, ils se citaient entre eux, mais dans une boucle
fermée que rien de lu au démarrage n'atteignait. Les deux index ci-dessus les
ramènent à **un saut**. Régénérables :

```bash
python C:/Users/amado/ASpace_OS_V3/scripts/indexer_distillations.py
```

**Cinq constats qui commandent une décision, pas une lecture :**

1. **Deux sessions d'août sur trois rejouent un brief déjà écrit** (unicité
   80,5 % en juillet → **32,3 %** en août ; `GARDE-FOU` relancé 96×, `LES SEPT
   CADENCES` 69×, `MODE FABLE` 60×). **Avant d'exécuter un brief, vérifier
   qu'il n'a pas déjà tourné.** Un système qui ne sait pas qu'il se répète ne
   peut pas s'arrêter.
2. **Ces briefs sont réécrits parce que le mandat ne survit pas à la
   compaction.** Le résumé garde les faits et perd l'autorisation. C'est la
   cause du point 1, et le besoin non satisfait le plus cher du corpus.
3. **Les applications sont la seule intention qui n'a jamais reculé**
   (18 → 55 → 59 → 62 de mai à août). Coach OS, Life OS, Agent OS. Une surface
   visible est un livrable de premier rang, pas un habillage.
4. **L'ontologie est l'intention la plus récente, pas la plus mûre** — 22
   occurrences uniques, dont la moitié en août. Virage en cours ; ne pas la
   traiter comme un acquis.
5. **Le quota n'est plus le problème** : 53 intentions uniques sur le sujet en
   juillet, **3 en août**. Les routeurs l'ont éteint. Le goulot est désormais
   la **vérification**, pas la production.

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

**Si tu lis ceci et que tu tournes sous `claude-glm`, tu n'es pas Opus.** Tu
exécutes un brief borné, tu écris ton rapport dans le fichier demandé, et tu
t'arrêtes. **Tu ne reprends pas la tâche d'une session parente**, tu ne
t'auto-invoques pas, tu ne décides rien. Incident du 2026-08-30 : un délégué
a lu ce fichier, s'est cru Opus, et a poursuivi le travail du parent.

- **Session courante** — décision, arbitrage, vérification. Pas l'exécution.
- **`claude-glm`** — l'exécution longue, répétitive, volumineuse.
- **Outil `Workflow`** — **non**. Les sous-agents héritent du modèle exporté et
  meurent si `ANTHROPIC_MODEL` pointe ailleurs. Orchestrer par `claude-glm`.

**Se délègue** : scans de corpus, lints, migrations, comptages, réécritures en
masse, toute tâche dépassant ~20 appels d'outils ou ~200 fichiers.

**Reste ici** : les décisions, et la vérification du travail délégué.
**Un agent délégué n'est jamais cru sur parole.** Le 2026-08-30, un délégué a
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

**Git** — la racine n'est plus un dépôt (`.git.DESACTIVE_2026-08-02`). Ne pas
le réactiver : 53 fichiers suivis pour tout le profil, cause d'une saturation
CPU permanente.

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
`model: 'haiku'` est **impossible à exécuter** si la session ne tourne pas sur
un modèle Anthropic. Erreur payée le 2026-08-15.

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

**État au 2026-08-29 : ni `spec-loop` ni `babysitter` ne tournent.** Configurés,
pas fonctionnels. Toute affirmation qui les suppose actifs est fausse.
