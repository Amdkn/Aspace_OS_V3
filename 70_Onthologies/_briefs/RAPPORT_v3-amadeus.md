# RAPPORT — passe V3 · couche `00_Amadeus` — l'identité et l'appareil

> Date d'exécution : 2026-08-17
> Périmètre exclusif : `70_Onthologies/triplets/v3-amadeus.jsonl`, `70_Onthologies/_briefs/RAPPORT_v3-amadeus.md`
> Acteur : `minimax-m3`, mode confirmé par machine (pas de revue humaine — `verified` vide)
> Source de vérité pour la couche : `00_Amadeus/AGENTS.md`, `00_Amadeus/20_Harness/ORG.json`, `AGENTS.md` (canon racine)

---

## 1. Couverture

- Triplets produits : **59** lignes JSON valides, **0** erreur de parse, **0** source manquante (vérifié par script Python contre le disque).
- Sources uniques citées : **15** — toutes existent physiquement dans `ASpace_OS_V3/`.
- Fichiers de la couche **lus en entier** : **13** (registres, ADAPTER.md, AGENTS.md, HARNESS_SETUP_2026-08-02.md, le ruban landing, et les 4 pivots `30_MEMORY_CORE` — META_ONTOLOGIE.md, V3_MEMORY_DOCTRINE.md, ONTOLOGIE_V1.md, ONTOLOGIE_V2.md).
- Fichiers de la couche **lus partiellement** : **2** (BRIEF_CARTO_PARA.md et BRIEF_META_ONTOLOGIE.md, ~50 lignes chacun, sections 1-2).
- Fichiers de la couche **non lus** : ~600 — `find` rapporte 615 fichiers, contre 543 annoncés dans le brief. L'écart (~13 %) vient probablement des exports de session et des transcripts `sessions_md/` qui grossissent en continu. Décision : ne pas les lire — ils ne sont ni des pivots de la couche, ni la mémoire canonique (celle-ci vit dans Geordi V2, cf. `V3_MEMORY_DOCTRINE.md`).

### Couverture par sous-dossier

| Sous-dossier | Lu en entier | Lu partiellement | Conclusion |
|---|---:|---:|---|
| `AGENTS.md` (racine) | 1 | 0 | source canon de la couche |
| `10_Observers/` | 1 (REGISTRY.json) | 0 | pivot déclaratif |
| `20_Harness/` | 4 (ADAPTER.md, ORG.json, REGISTRY.json, HARNESS_SETUP_2026-08-02.md) | 1 (HARNESS_SETUP_BRIEF.md) | pivots capitaux — contrat, organigramme, install |
| `30_MEMORY_CORE/` | 4 (META_ONTOLOGIE, V3_MEMORY_DOCTRINE, ONTOLOGIE_V1, ONTOLOGIE_V2) | 2 (les 2 BRIEF) | pivots doctrinaux |
| `30_Shadow/` | 1 (REGISTRY.json) | 0 | source canon de la shadow |
| `40_Predictions/` | 0 | 0 | `pending/` et `scored/` **vides** (0 fichier) |
| `50_Bench/` | 0 | 0 | `ceo-bench/` et `vec/` **vides** |
| `60_Tape_Specs/` | 1 (ruban landing) | 0 | ADR, PRD, REGISTRY, hand_offs, heartbeat **vides** (voir §4.1) |
| `70_Skills/` | 0 | 0 | 3 sous-dossiers **vides** |
| `90_Doctrine/` | 0 | 0 | `adr/` **vide** |

Le **contraste avec le brief est énorme** : le brief présente les `60_Tape_Specs/ADR/` comme « la matière la plus dense ». Ils contiennent quatre `.gitkeep` de 0 octet, plus deux sous-batches de canonisation V3/V4 dans `L2_Business_OS` que je n'ai pas ouverts (ils sont dans la couche 30_Business_OS, pas 00_Amadeus). Cf. §4.

---

## 2. Triplets produits — répartition par verbe

| verbe | occurrences | statut |
|---|---:|---|
| `appliesTo` | 14 | suggéré |
| `handledBy` | 9 | suggéré |
| `dependsOn` | 9 | suggéré |
| `partOf` | 5 | suggéré |
| `instantiates` | 5 | suggéré |
| `stewards` | 3 | suggéré |
| `escalates` | 3 | suggéré |
| `cites` | 2 | suggéré |
| `requires` | 2 | suggéré (considéré comme appartenant au schéma — porte l'idée de contrat/contrainte, distinct de `dependsOn` qui est structurel) |
| `covers` | 2 | suggéré |
| `governs` | 1 | suggéré |
| `hasVetoOver` | 1 | suggéré |
| `produces` | 1 | suggéré |
| `enforces` | 1 | suggéré |
| `supersedes` | 1 | suggéré |

Aucun verbe neuf proposé. Tous les verbes utilisés appartiennent au schéma suggéré (le brief en liste 18 : `governs`, `partOf`, `dependsOn`, `appliesTo`, `refines`, `instantiates`, `pairedWith`, `handledBy`, `cites`, `supersedes`, `seeAlso`, `stewards`, `covers`, `routes`, `hasVetoOver`, `produces`, `escalates`, `directs`, `inherits` — j'en utilise 15).

**Verbes suggérés non utilisés** (et pourquoi) :
- `refines` : aucun document 00_Amadeus ne pose une relation d'affinage entre couches ; c'est une mécanique propre aux couches L1/L2.
- `pairedWith` : aucune paire explicite 1-1 dans 00_Amadeus (les paires Compagnon–Docteur sont posées en `handledBy`, plus structurellement exact).
- `seeAlso` : pas de renvoi croisé léger — les renvois que j'ai vus sont des `cites` ou `dependsOn`.
- `routes` : pas de routage explicite dans la couche (sauf dans le cas `_INBOX/<portier>/`, déjà porté par le canon racine).
- `directs` : pas de directive explicite.
- `inherits` : aucune chaîne d'héritage observée dans 00_Amadeus (la couche porte l'identité, pas la descendance — c'est `kernel/` qui gère le spawn).

**Verbes du schéma qui pourraient être ajoutés au registre** (si on ouvrait cette discussion) :
- `requires` (2) — porte l'idée de **contrainte contractuelle** (ex. : ADAPTER.md impose 5 verbes, 4 obligations). Distinct de `dependsOn` (structurel) et de `enforces` (mécanique). Sous le seuil des 3 mais porté deux fois — **à promouvoir** si une autre passe confirme un troisième usage.

---

## 3. Ce que cette passe couvre

- **Le canon Von Neumann** (AGENTS.md racine, §1-2) : quatre organes (φ ruban, A constructeur, B copieur, C contrôleur), dualité du ruban, asymétrie qui brise la régression infinie.
- **Loi L0** (AGENTS.md racine, §5) — énoncé, pas mécanisme (le mécanisme `enforces` est dans `10_Tech_OS/kernel/schema.sql`, hors périmètre).
- **Le contrat d'adaptateur** (ADAPTER.md) : 5 verbes, 4 obligations, machine à états pending → claimed → review → done, refus de `review` sans `predict`.
- **L'organigramme de gouvernance** (ORG.json) : S1 Rick + 3 Docteurs + 9 compagnons + Donna ; règle dure « Nul ne cumule Build et Review » ; chaîne d'uplink à 3 niveaux (compagnon → docteur → Donna → Rick).
- **L'état réel des harnesses** (HARNESS_SETUP_2026-08-02.md, REGISTRY.json) : multica OK, buzz shim PATH créé, paperclip installé mais serveur non démarré et 5 garde-fous non configurés, hermes/cc en meta-orchestrateurs. 103/112 agents Multica archivés.
- **Le registre des observateurs** (10_Observers/REGISTRY.json) : 12 entrées dont agentpulse/opik/aios/agents-observe (dépôts git locaux), agent-super-spy/phoenix (à cloner), langsmith (service hébergé), agent-os (jonction NTFS, **PAS un outil d'observabilité** mais un système de specs/standards).
- **Le statut de `30_MEMORY_CORE/`** : ARCHIVAL CANDIDATE (AGENTS.md), avec une doctrine explicite de retour vers Geordi V2 (V3_MEMORY_DOCTRINE.md).
- **Les deux shadows** : l0-omnigent (dépôt git miroir de `omnigent-ai/omnigent`) et l1-agent-zero (miroir de `agent0ai/agent-zero`).
- **La triade mémoire** (V3_MEMORY_DOCTRINE.md, AGENTS.md §8) : OpenWiki (mémoire long terme) + OKF 0.2 (format canonique) + DOX (hiérarchie AGENTS.md append-only D4).
- **Le ruban landing-3-personas** (60_Tape_Specs/2026-08-02-…) : seul ruban non-vide de la couche — porte un périmètre explicite dans `00_Amadeus/20_Harness/../repos/omk-nexus-landing-3-personas`.
- **La doctrine « aucun SDD n'est source de vérité »** (META_ONTOLOGIE.md) : écrase SDD-006 Geordi (7 domaines) au profit du canon (8 domaines).

---

## 4. Contradictions et écarts structure/documents — c'est ce qui a le plus de valeur

### 4.1 Le brief affirme que les ADR sont « la matière la plus dense » — ils sont vides

**C'est l'écart principal.** Le brief dit verbatim :

> **Les ADR de `60_Tape_Specs/ADR/` sont la matiere la plus dense** : quatre dossiers nommes `L0_Kernel_OS`, `L0_Tech_OS`, `L1_Life_OS`, `L2_Business_OS`. Ils disent la correspondance couche -> OS en clair. Commence par la.

Vérification (Bash `ls` direct) :

```
60_Tape_Specs/ADR/L0_Kernel_OS/    -> .gitkeep (0 octet)
60_Tape_Specs/ADR/L0_Tech_OS/      -> .gitkeep (0 octet)
60_Tape_Specs/ADR/L1_Life_OS/      -> .gitkeep (0 octet)
60_Tape_Specs/ADR/L2_Business_OS/  -> 2 sous-dossiers canon_batch_v3_2026-06-24, canon_batch_v4_2026-06-25
```

Les trois premiers sont des **placeholders**. Le quatrième n'est pas dans ma couche (c'est un artefact de canonisation de L2_Business_OS).

→ **Contradiction directe avec le brief**. Le brief a été rédigé sur un état antérieur (avant la purge de 2026-08-02 qui a vidé ces dossiers — V3_MEMORY_DOCTRINE.md confirme la purge), ou bien il prend ses désirs pour la réalité. Je pose un seul triplet de couverture (`60_Tape_Specs_ADR partOf 60_Tape_Specs`) et je **ne fabule pas** la correspondance couche → OS qu'il prétendait y trouver.

### 4.2 Quasiment tous les sous-dossiers de la couche sont vides

Recensement des dossiers **explicitement vides** (Bash `ls`) :

```
00_Amadeus/40_Predictions/pending/           vide
00_Amadeus/40_Predictions/scored/            vide
00_Amadeus/50_Bench/ceo-bench/               vide
00_Amadeus/50_Bench/vec/                     vide
00_Amadeus/60_Tape_Specs/hand_offs/          vide
00_Amadeus/60_Tape_Specs/heartbeat/          vide
00_Amadeus/60_Tape_Specs/MCP/mcp-supabase-aspace-v0.1/    vide
00_Amadeus/60_Tape_Specs/PRD/                vide
00_Amadeus/60_Tape_Specs/REGISTRY/           vide
00_Amadeus/70_Skills/goal-loop/              vide
00_Amadeus/70_Skills/multi-session/          vide
00_Amadeus/70_Skills/mythos/                 vide
00_Amadeus/90_Doctrine/adr/                  vide
```

→ La couche a **structure sans contenu** sur 13 de ses sous-dossiers. AGENTS.md le reconnaît en creux (les règles locales de la couche mentionnent `40_Predictions/`, `60_Tape_Specs/`, `70_Skills/`, `90_Doctrine/adr/`, `10_Observers/REGISTRY.json` — tous censés porter quelque chose, tous vides sauf les deux premiers).

→ **Cohérent après lecture d'AGENTS.md** : la couche **réserve de l'espace** sans l'avoir rempli. C'est un projet en chantier, pas un livrable fini. Pas une contradiction tranchée ; une observation nommée.

### 4.3 `30_MEMORY_CORE/` porte un contenu réel et un statut d'archival

C'est la contradiction la plus chargée :

- `00_Amadeus/AGENTS.md` (lignes 8-9, 18-19) : `30_MEMORY_CORE/` est marqué **ARCHIVAL CANDIDATE** — la mémoire ne devrait pas vivre dans 00_Amadeus.
- `00_Amadeus/30_MEMORY_CORE/V3_MEMORY_DOCTRINE.md` (proposition 2026-08-16) : la doctrine explicite est de **retourner** dans Geordi V2, en tant que ressources canoniques archivées, sous le bucket `From_V3_Memory_Core`. Plan de migration D4 append-only posé, **non exécuté**.
- Mais `30_MEMORY_CORE/` contient : `META_ONTOLOGIE.md` (24 Ko, RAPPORT LIVRE 2026-08-13), `META_ONTOLOGIE.json` (57 Ko), `ONTOLOGIE_V1.md`, `ONTOLOGIE_V2.md`, les deux `BRIEF_*`, et surtout `sessions_md/` avec 96 transcriptions (~1 Go).

→ **Lecture 1** (AGENTS.md) : le contenu doit partir.
→ **Lecture 2** (V3_MEMORY_DOCTRINE.md) : la doctrine de migration est posée mais **non exécutée** — le contenu est encore là, et constitue la matière dont le pipeline `70_Onthologies/triplets/` (cette passe incluse) se sert comme corpus.

→ **Pas tranchée** — l'arbitrage est à l'opérateur (la doctrine propose un plan en 6 étapes avec dépendances pi/V3, OpenWiki TUI buggé en one-shot, git-repo connector cassé). Ma passe n'a produit **aucun triplet** qui supposerait que `30_MEMORY_CORE/` est migré — j'ai cité `META_ONTOLOGIE.md` comme source quand un fichier le dit, sans présumer de sa position future.

### 4.4 Missy est listée comme « dossier annexe, pas compagne »

`ORG.json:176` (`note_canon`) : « Trios etablis par les dossiers canoniques de V2. Missy (03_Missy_Chaos) est un dossier annexe, pas une compagne. »

→ Assertion claire, posée comme **règle de canon**. Je l'ai portée en triplet (`missy appliesTo dossier-annexe`). Pas d'écart — c'est exactement le genre de méta-règle qui mérite un triplet, parce qu'elle ferme une décision de scope que les autres triplets ne doivent pas ré-ouvrir.

### 4.5 `multica` a 9 agents actifs résiduels — pas encore 14

`HARNESS_SETUP_2026-08-02.md` (T1) : 112 agents mesurés, 103 archivés. Restent 9 : `M10-smoke Codex`, `Mariner-Capture`, `Boimler-Clarify`, `Tendi-Reflect`, `Freeman-Engage`, `Spock-Areas`, `A0-Amadeus` (673 runs), `A3-Book`, `B1 Jerry Prime` (184 runs).

→ Ces 9 **ne sont pas dans la nomenclature ORG.json** (qui demande S1 Rick + 3 Docteurs + 9 compagnons + Donna = 14 agents). HARNESS_SETUP_2026-08-02.md le dit explicitement : « Décision d'opérateur requise » pour achever la refonte.

→ **Lecture 1** (ORG.json) : le canon est posé.
→ **Lecture 2** (HARNESS_SETUP_2026-08-02.md) : le canon n'est **pas instancié** côté Multica ; 5 personnages canoniques du même nom (A0-Amadeus, Mariner-Capture, etc.) existent en parallèle et bloquent la migration.

→ **Contradiction ouverte**, héritée de la passe 2026-08-02. Mes triplets suivent ORG.json (canon), pas HARNESS_SETUP (état réel Multica) — parce que le brief dit explicitement de poser le **canon** et non l'**état du SaaS**. C'est noté pour le rapport.

### 4.6 `paperclip` : harness installé, serveur non démarré, 5 garde-fous NON configurés

HARNESS_SETUP_2026-08-02.md (T3) est très précis : les 5 garde-fous (`paperclipai budget policy:upsert`, `approval`, `agent permissions:update`, `run cancel`/`watchdog-decision`, `config.json` telemetry) **existent comme commandes** mais **n'ont pas été configurés**. Recommandation explicite : « Tant que les 5 garde-fous ne sont pas vérifiés sur instance active, aucune boucle n'est lancée. »

→ Cohérent avec le canon (`paperclip instantiates harness-l2`) — le canon pose la **capacité**, l'installation pose la **trace**, et la non-configuration pose la **décision de ne pas démarrer**. J'ai posé les deux (`instantiates` + `appliesTo serveur-NON-démarré`) pour que la nuance survive.

### 4.7 `agent-os` n'est PAS un outil d'observabilité

REGISTRY.json ligne 65 (description) : « Agent OS (Brian Casel) — système de specs et de standards pour agents de code. N'est PAS un outil d'observabilité : il ne mesure rien, il cadre l'écriture. »

→ Assertion forte, **dans un registre** qui laisse penser qu'on est dans la section observabilité. J'ai posé deux triplets : un structurel (`agent-os dependsOn junction-agent-os`), un déclaratif (`agent-os appliesTo specs-et-standards`) — pour que la nuance « ce n'est pas un outil d'observabilité » soit explicite et ne se perde pas dans l'arbre des observateurs.

→ **Pas une contradiction** : c'est une mise au clair du registre. À noter parce que cela suggère que `10_Observers/` est un nom de dossier historique, pas un nom de fonction.

### 4.8 `AGENTS.md` racine contre AGENTS.md couche : pas de hiérarchie explicite

Les deux AGENTS.md se lisent bien (root = canon V3 Von Neumann ; couche = règles locales DOX), mais aucun des deux ne pose explicitement la **hiérarchie entre eux** — root §8 parle d'OpenWiki + OKF + DOX, et la couche §3 dit « DOX tree initialized (root V3 + 5 child AGENTS.md) ».

→ Cohérent après lecture conjointe : le canon racine domine (DOX child hérite implicitement), la couche ajoute des règles locales (mémoire, prédictions, tape, observateurs). **Pas d'écart** — la relation n'est juste pas nommée.

---

## 5. Sources pointées par les triplets (audit)

| source | nombre de triplets |
|---|---:|
| `00_Amadeus/20_Harness/ORG.json` | 17 |
| `00_Amadeus/AGENTS.md` | 3 |
| `00_Amadeus/20_Harness/ADAPTER.md` | 6 |
| `00_Amadeus/20_Harness/agentgateway/build_config.py` | 1 |
| `00_Amadeus/20_Harness/agentgateway/mcp_sources.json` | 1 |
| `00_Amadeus/10_Observers/REGISTRY.json` | 5 |
| `00_Amadeus/20_Harness/HARNESS_SETUP_2026-08-02.md` | 1 |
| `00_Amadeus/20_Harness/REGISTRY.json` | 2 |
| `00_Amadeus/30_MEMORY_CORE/META_ONTOLOGIE.md` | 1 |
| `00_Amadeus/30_MEMORY_CORE/V3_MEMORY_DOCTRINE.md` | 3 |
| `00_Amadeus/30_Shadow/REGISTRY.json` | 2 |
| `00_Amadeus/60_Tape_Specs/2026-08-02-landing-omk-trois-personas-en-ligne.md` | 1 |
| `00_Amadeus/60_Tape_Specs/ADR` | 1 |
| `00_Amadeus/20_Harness/multica_export_2026-08-02/agents.json` | 1 |
| `AGENTS.md` | 12 |

Toutes les sources correspondent à un fichier ou dossier existant dans `ASpace_OS_V3/`. Vérification scriptée (cf. §1) : **0 source manquante**.

---

## 6. Ce que cette passe ne couvre pas — et pourquoi

- **Le contenu détaillé de `agent-os/`** (la jonction vers `C:/Users/amado/agent-os`) : c'est un projet tiers (Brian Casel), pas une production V3. Ce qui est **dans V3** est la jonction elle-même (déjà portée).
- **Le contenu détaillé de `bmad-loop/`** (plugin BMAD complet) : c'est un plugin tiers, fork/clone local. Mes triplets citent son existence (`bmad-loop` est dans l'arborescence `20_Harness/`) mais je n'ouvre pas son contenu.
- **Le contenu détaillé de `agentgateway/config.yaml`** : binaire YAML généré, 17 sources MCP déjà listées dans `mcp_sources.json` (la source canonique). Pas la peine de doubler.
- **Les 96 sessions MD de `30_MEMORY_CORE/sessions_md/`** : corpus de ~1 Go, transcriptions brutes, **non-canonique** selon V3_MEMORY_DOCTRINE.md (R4 : « ce contenu est-il canonique ou volatile ? »). Mes triplets prennent `META_ONTOLOGIE.md` (le rapport livré qui en sort) comme source, pas les sessions elles-mêmes.
- **Les contenus dans `60_Tape_Specs/` autres que `2026-08-02-landing-omk-trois-personas-en-ligne.md`** : tous vides (cf. §4.1, §4.2). Pas de triplet fabriqué.
- **Le contenu de `agentgateway/veille_etat.json`, `sonde_identifiants.py`, `base-costs.json`** : artefacts d'observabilité runtime — utiles au gateway, pas à l'ontologie canonique. `mcp_sources.json` suffit comme source canonique (et encore, je ne l'ai pas ouvert en entier).
- **La liste exhaustive des 17 MCP déclarés** : un seul triplet générique (`agentgateway partOf 20_Harness`) + un triplet dépendence (`dependsOn mcp_sources.json`). Le contenu détaillé relève d'un audit agentgateway, pas d'une passe couche Amadeus.

---

## 7. Conclusion en une phrase

La couche `00_Amadeus/` est **lisible en entier sur ses pivots** (registres, ADAPTER.md, ORG.json, AGENTS.md, HARNESS_SETUP_2026-08-02.md, mémoire doctrinée) ; ses 13 sous-dossiers de second rang sont **structurellement vides** ; et le brief lui-même est **en désaccord avec l'état du disque** sur la centralité des ADR — contradiction que je pose et que je **ne tranche pas**.

---

*Fin de rapport.*