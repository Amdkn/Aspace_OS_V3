# C:\Users\amado — racine du profil

Ce dossier est un **profil utilisateur**, pas un projet. Aucun travail ne s'y fait.

> **Version intégrale : `ASpace_OS_V3/40_Memory_Wiki_OKF/canon/CANON-profil-racine.md`.**
> Ce fichier-ci est chargé dans **chaque** session : il ne garde que les règles
> qui commandent une décision. Tout le détail — les mesures datées, les pièges
> déjà payés, les procédures d'invocation — vit dans le canon et se lit **à la
> demande**, pas à chaque démarrage.
>
> Dégraissé le 2026-08-29 : 479 lignes → ~120. Le fichier chargé coûtait
> ~5 900 tokens par session, avant le moindre travail. Une consigne qu'on ne
> lit qu'une fois sur cinquante n'a pas sa place dans le contexte permanent.

---

## 0. Où lire avant de répondre

**Le point d'entrée n'est pas ce fichier, et ce n'est pas non plus
`40_Memory_Wiki_OKF/`.** Mesure du 2026-08-29 : **688 concepts OKF** dans
`ASpace_OS_V3`, dont **30 seulement** dans le bundle mémoire. Chercher là et
s'arrêter, c'est manquer 96 % du corpus et conclure « non documenté » sur ce
qui est écrit ailleurs, en volume.

| Question | Où |
|---|---|
| Rangs, domaines, horizons, verbes | `00_Amadeus/30_MEMORY_CORE/ONTOLOGIE_V2.md` |
| Cascade E-Myth, S1/S2/S3, Donna | `10_Tech_OS/00_Governance_Rick/CASCADE.md` |
| Contradictions déjà cataloguées (204) | `00_Amadeus/30_MEMORY_CORE/carto/CONSOLIDE.json` |
| Distillation, substrat, méthode | `50_Distillation/METHODE.md` |
| Intégrations récentes, pièges d'outillage | `40_Memory_Wiki_OKF/` |

**`grep` le corpus entier avant d'affirmer.** Le bundle seul ne suffit jamais.

---

## 1. Économie de quotas

Les quotas des modèles Anthropic sont la ressource rare. Tout travail long,
répétitif ou volumineux se délègue.

- **Sub-agents via Workflow** — défaut pour tout travail non trivial en session.
- **`claude -p`** — batchs sans session active (cron, CI), ou rotation de modèle.
  **Jamais** comme canal général : friction ingérable.
- **Session courante** — décision, arbitrage, vérification. Pas l'exécution.

**Se délègue** : scans de corpus, lints, migrations, comptages, réécritures en
masse, toute tâche dépassant ~20 appels d'outils ou ~200 fichiers.

**Reste ici** : les décisions, et la vérification du travail délégué.
**Un agent délégué n'est jamais cru sur parole.**

> Détail des cinq pièges d'invocation (précédence d'environnement, `PATH`,
> brief en stdin, outillage du dépôt qui détourne, concurrence) :
> `CANON-profil-racine.md` §1. Les recopier ici coûterait 2 000 tokens par
> session pour une procédure lancée une fois par semaine.

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

## 4. Où vivent les choses

| | |
|---|---|
| Corpus et ontologie | `ASpace_OS_V3/` — voir §0 |
| Base de connaissance V2 | `ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/` |
| Secrets | `.claude/_secrets_local/` — **jamais** dans le dépôt |
| MCP | un seul serveur : l'agentgateway, `http://127.0.0.1:3300/mcp` |

**Ne pas éditer `~/.mcp.json`** : il ne contient que le pointeur vers le
gateway. Source de vérité : `20_Harness/agentgateway/mcp_sources.json`, puis
`python build_config.py`, puis relancer.

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
