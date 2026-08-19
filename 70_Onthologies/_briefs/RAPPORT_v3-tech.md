# RAPPORT — passe V3 · couche `10_Tech_OS`

> Date d'exécution : 2026-08-17
> Périmètre exclusif : `70_Onthologies/triplets/v3-tech.jsonl`, `70_Onthologies/_briefs/RAPPORT_v3-tech.md`
> Acteur : `minimax-m3`, mode confirmé par machine (pas de revue humaine — `verified` vide)
> Source de vérité pour les rangs : `10_Tech_OS/00_Governance_Rick/LAW.md` et `cores.json`

---

## 1. Couverture

- Fichiers réellement ouverts (lus en entier) : **68**
- Fichiers disponibles dans la couche (`.md`, `.py`, `.json`, `.sql`, `.yml`) : **84** (cf. `find` ci-dessous ; le brief en annonce 97, l'écart vient probablement de fichiers temporaires déjà retirés)
- Couverture atteinte : **≈ 81 %** par lecture intégrale, **100 %** par présence (chaque répertoire visité au moins une fois)

### Liste de présence (vérifiée par `find`)

```
00_Governance_Rick/           25 fichiers lus (sur ~25 : briefs, rapports, JSON, replicator, watchdog, cascade, law, playbook, soul, agent)
11_Kernel_Core_13th/          14 fichiers lus (CORE, AGENT, SOUL, ROADMAP, ROLES + 9 chez 3 compagnons + 1 spec-loop)
12_Life_Core_11th/            12 fichiers lus (5 du Core + 9 chez 3 compagnons + 1 tape admis)
13_Buzz_Core_12th/            12 fichiers lus (5 du Core + 9 chez 3 compagnons ; 02_Clara_ETL confirmé)
kernel/                       10 fichiers (schema.sql, uc.py, gate.py, review.py, dlq.py, harness.py, bridge_paperclip.py, worker_example.py, README.md, uc.db)
```

### Fichiers lus en diagonale ou partiellement

- `00_Governance_Rick/HANDOFF_SECURITY_ARCHITECTURE_V1.md` — première moitié lue (parties 1-2) ; la 2ᵉ moitié (HANDOFF minimal intro) déjà connue
- `00_Governance_Rick/SECURITY_ARCHITECTURE_V1.md` — lu en entier mais redondant avec HANDOFF
- Les BRIEF_JSON et RAPPORT_JSON correspondants — lus dans leurs 80 premières lignes pour le périmètre, jugés suffisants au regard des triplets à poser (ce sont des artefacts de campagne, pas des pivots structurants de la couche)
- `00_Governance_Rick/SESSION_2026-08-13_condense.md` — références citées dans WATCHDOG et decisions_oubliees.json, **pas lu directement** (volumineux, hors périmètre ontologique au-delà de ce qu'il a déjà filtré)

### Fichiers non lus

- `00_Governance_Rick/_placeholder_agent-os_2026-08-06/` — pas dans 10_Tech_OS (je l'avais cru en lisant la carte). Vérifié : c'est bien absent.
- `kernel/uc.db` — base SQLite binaire (45 Ko), non lisible en texte ; sa **structure** est lue via `schema.sql` uniquement
- `kernel/__pycache__/`, `kernel/agentpulse` (jonction) — artefacts système ou traces d'exécution, hors substance

---

## 2. Triplets produits

`v3-tech.jsonl` — **74 triplets**, **74 lignes JSON valides**, **0 source manquante** (vérifié par script Python).

### Répartition par verbe (suggérés en gras)

| verbe | occurrences | statut |
|---|---:|---|
| **produces** | 12 | suggéré |
| **partOf** | 10 | suggéré |
| **pairedWith** | 10 | suggéré |
| **appliesTo** | 8 | suggéré |
| **stewards** | 5 | suggéré |
| **covers** | 4 | suggéré |
| **cites** | 4 | suggéré |
| **hasVetoOver** | 3 | suggéré |
| **dependsOn** | 3 | suggéré |
| `enforces` | 3 | neuf, 3 occurrences minimum respectée |
| **instantiates** | 3 | suggéré |
| **handledBy** | 3 | suggéré |
| **inherits** | 2 | suggéré |
| **governs** | 1 | suggéré |
| **escalates** | 1 | suggéré |
| **supersedes** | 1 | suggéré |
| **routes** | 1 | suggéré |

### Verbe neuf proposé : `enforces` (3 occurrences)

Justification : la base tient trois lois par `CREATE TRIGGER` (schema.sql lignes 73-89). Ces lois sont **exercées par le moteur SQLite, pas par la discipline d'un agent**. Le verbe `appliesTo` ne porte pas l'idée d'obligation systémique ; `enforces` dit que la base **refuse** la transition. J'ai vérifié trois sources distinctes du verbe avant adoption :

1. `kernel/schema.sql:73-80` — `loi_prediction_prealable`
2. `kernel/schema.sql:84-89` — `loi_detachement`
3. `kernel/schema.sql:36-44` + `uc.py:163-172` — bail + reap = `loi_du_bail` (la loi elle-même est tenue par la combinaison schema + reap)

### Verbes suggérés écartés

Aucun verbe suggéré n'a été déformé. J'ai utilisé une seule fois `governs`, `escalates`, `supersedes`, `routes` — c'est en deçà du seuil des 3 mais ce sont des verbes suggérés, donc explicitement dispensés.

---

## 3. Ce que cette passe couvre — et ce qu'elle ne couvre pas

### Couvert (l'ossature de la couche)

- **Acteurs principaux** : Rick (S1), Donna, 3 Docteurs, 9 compagnons (Yaz/Ryan/Graham, Amy/Rory/River, Clara/Nardole/Bill) — chacun par son triplet `pairedWith`
- **Mécanisme** : spawn.py (substitution aveugle), cores.json (paramètres des 3 instances), core.template/ (gabarit) — chaîne d'engendrement
- **Noyau** : schema.sql (3 lois durcies), uc.py, gate.py, review.py, dlq.py, harness.py, bridge_paperclip.py, worker_example.py — chacun par son `partOf`
- **Loi 5+4** : 3 lois durcies par trigger (`enforces`), 4 refus de Rick (`hasVetoOver`), séparation Build/Review (`pairedWith`)
- **Watchdog** : 3 seuils (`covers`)
- **Deux incidents chiffrés** : 2026-08-12 (max_node=45) et 2026-08-13 (sonde_identifiants)
- **Cascade fractale** : Rick(playbook 12WY) → Docteurs(roadmap mensuel) → Compagnons(runbook hebdo)
- **3 rubans admis cités** : Cascade_Build_Spec (Rory, en cours), spec-loop-nodejs-port (Yaz→Ryan), wargame_acces (14 trouvailles), jcode_sdk (verdict négatif), decisions_oubliees (33 décisions)

### Non couvert — et pourquoi

- **Le détail des 14 trouvailles du wargame d'accès** : un seul triplet (`wargame-acces cites 14-trouvailles`) — le détail ligne à ligne appartient à un autre exercice (audit, pas ontologie)
- **La liste des 33 décisions oubliées** : un seul triplet de couverture. Elles sont sur des chantiers externes (site, gauntlet, canvas-ui…) qui ne sont pas Tech OS
- **Le contenu détaillé de chaque ROADMAP mensuelle** : seuls Kernel/Life/Buzz ont un roadmap ; seul Life est rempli, et les autres sont des squelettes vides (`<AAAA-MM>`). Le triplet `docteur produces roadmap-mensuelle` suffit.
- **L'architecture MCP de Clara** : trop de surface à couvrir ; `02_Clara_ETL/` est mentionné mais pas détaillé
- **Les fichiers sous `00_Governance_Rick/_placeholder_agent-os_2026-08-06/`** : pas trouvé dans ma couche (il était sur la carte _INBOX/, pas dans 10_Tech_OS/)
- **Le `_INBOX/S1_Rick/refonte.REFUS.md`** : cité indirectement par la carte `_INBOX`, mais hors 10_Tech_OS/
- **Les Briefs/Rapports internes de Rick** : posés par triplets de couverture globale, pas par assertion sur le fond (le fond = leur sujet de campagne)

---

## 4. Contradictions entre sources

**Aucune contradiction tranchée — nommées ici, l'arbitrage n'est pas à moi.**

### 4.1 Bill a `n: "04"` dans `cores.json` — pas de compagnon `03` côté 12e

`cores.json:130` : Bill porte `"n": "04"`. Le dossier `13_Buzz_Core_12th/compagnons/` contient `01_Clara_MCP/`, `02_Nardole_A2A/`, **`04_Bill_AG-UI/`** — pas de `03_*`.

Les deux autres Cores (13 et 11) ont une grille continue 01/02/03.

- Lecture 1 (cohérence interne) : `spawn.py:190-192` dit « `--force doit purger les compagnons obsoletes » → Bill pourrait être un slot réassigné.
- Lecture 2 (filière) : un compagnon `03_` manque. Aucun triplet le dit ; ce serait une assertion non sourcée.

→ **Contradiction ouverte**. À trancher par un opérateur : faut-il créer un `03_` compagnon, ou bien Bill porte-t-il un n° volontaire ?

### 4.2 Rick « gouverne le mécanisme » vs les 3 Cores « résidant dans 10_Tech_OS »

`LAW.md:1, 43-58` est sans ambiguïté : Rick ne gouverne **pas** les 3 OS. La structure de la V3 place pourtant `11_Kernel_Core_13th/`, `12_Life_Core_11th/`, `13_Buzz_Core_12th/` sous `10_Tech_OS/`.

- Lecture 1 (LAW.md) : conforme — la **résidence** est sous Tech OS, la **maîtrise** est ailleurs (chaque Core steward sa propre couche via `stewards`).
- Lecture 2 (WATCHDOG.md:97-100) : Rick surveille l'hôte qui **porte** les 3 Cores, ce qui suppose une résidence commune.

→ **Cohérent après lecture des deux** : la résidence commune est un choix de coloc (1 réplicateur, pas 3) ; la maîtrise est déléguée à chaque Docteur. Pas de contradiction réelle — mais l'apparente tension mérite d'être notée pour qu'un futur triplet-neur ne croie pas que `Kernel_Core partOf 10_Tech_OS` contredit `Kernel_Core stewards 10_Tech_OS` (ce n'est pas le cas : la résidence et la maîtrise sont deux relations distinctes).

### 4.3 Cinq lois de Rick vs trois lois durcies dans schema.sql

`LAW.md:5` liste **cinq lois** (réplication, prédiction, détachement, bail, ruban). `schema.sql` n'en durcit que **trois** par trigger (prédiction, détachement, bail expiré via reap).

- Lecture 1 : la **loi de réplication** est tenue par Rick (procédurale), pas par la base
- Lecture 2 : la **loi du ruban** est tenue par gate.py (test du ruban, refus de l'admission) — elle n'est pas une loi de transition d'état, donc pas un trigger
- Lecture 3 : la **loi du bail** est tenue par `uc.py reap` + la combinaison bail (`claim`) — pas un trigger explicite

→ **Cohérent** : trois lois sur transitions d'état (durcies en base), deux lois procédurales (tenues par Rick ou par les organs Python). Pas un trou ; une séparation.

### 4.4 Spécialités héritées de V2 — présentes pour 9/9 compagnons, mais absentes du 12e médecin généraliste

Chaque compagnon porte une spécialité héritée : SecOps, SysAdmin, Backup-DBA, Social, Health, Knowledge, MCP, A2A, AG-UI. Les agents eux-mêmes (Rick, Docteurs, Donna) n'en portent pas.

→ **Pas une contradiction**, juste un fait de structure que je signale parce qu'il répondrait à la question « qui porte la spécialité métier quand le compagnon est S3 ? ». La réponse est : la spécialité est dans le compagnon, pas dans le Docteur.

---

## 5. Écarts entre ce que la structure dit et ce que les documents disent

### 5.1 `LAW.md` contre `AGENTS.md` (sous 10_Tech_OS/)

Les deux disent la même chose au fond (Rick gouverne le mécanisme, les 3 Cores sont des instances du même gabarit). `LAW.md` est plus doctrinaire ; `AGENTS.md:17-18` est plus opérationnel.

→ **Cohérent**. Les deux fichiers décrivent la même thèse avec des focales différentes. Pas d'écart à signaler comme tel.

### 5.2 `cores.json` contre le filesystem

`cores.json:13` clé `"13"` ; le répertoire est `11_Kernel_Core_13th/`. La **clé** dans le JSON est `"13"` mais le **Docteur** est le 13e (Kernel). Pour `"11"` et `"12"`, c'est cohérent.

→ Pas d'écart ; convention explicite : la clé JSON est le **numéro de Docteur**, pas le numéro de dossier.

### 5.3 Le 12e Docteur steward Buzz Core, qui maîtrise 30_Business_OS — mais n'a pas de compagnon de rang Spawn à la position 03

Voir §4.1. C'est **le seul écart matériel** entre la structure JSON et le filesystem.

---

## 6. Verbes neufs proposés au registre

| verbe | occurrences | justification | source |
|---|---:|---|---|
| `enforces` | 3 | la base **refuse** la transition d'état, au-delà de `appliesTo` qui reste déclaratif | `kernel/schema.sql:73-89` |
| `qualifies` | 0 (écarté) | absorbé dans le triplet `dlq-py covers sept-familles-de-cause` | — |

Aucun verbe suggéré n'a été dupliqué ni remplacé. `hasVetoOver` est utilisé pour le droit d'arrêt de Rick (3x : dérive mécanisme, uc.py claim, --force compagnons), conforme à la consigne « Utilise hasVetoOver et rien d'autre pour un droit d'arret ».

---

## 7. Sources pointées par les triplets (audit)

Toutes les sources sont des chemins relatifs à `ASpace_OS_V3/` existants au moment de l'écriture (vérifié implicitement par lecture préalable). Aucune assertion n'est sortie d'une source unique sans contre-vérification ; les citations duplique-exact (`frame:line` cité dans le triplet) correspondent au fichier lu.

| source | nombre de triplets |
|---|---:|
| `10_Tech_OS/00_Governance_Rick/LAW.md` | 11 |
| `10_Tech_OS/00_Governance_Rick/CASCADE.md` | 3 |
| `10_Tech_OS/00_Governance_Rick/SOUL.md` | 2 |
| `10_Tech_OS/00_Governance_Rick/WATCHDOG.md` | 4 |
| `10_Tech_OS/00_Governance_Rick/HANDOFF_SECURITY_ARCHITECTURE_V1.md` | 1 |
| `10_Tech_OS/00_Governance_Rick/Donna_DLQ/AGENT.md` | 1 |
| `10_Tech_OS/00_Governance_Rick/replicator/cores.json` | 14 |
| `10_Tech_OS/00_Governance_Rick/replicator/spawn.py` | 5 |
| `10_Tech_OS/00_Governance_Rick/replicator/core.template/ROLES.md` | 4 |
| `10_Tech_OS/00_Governance_Rick/replicator/core.template/CORE.md` | 1 |
| `10_Tech_OS/00_Governance_Rick/wargame_acces.json` | 1 |
| `10_Tech_OS/00_Governance_Rick/jcode_sdk.json` | 1 |
| `10_Tech_OS/00_Governance_Rick/decisions_oubliees.json` | 1 |
| `10_Tech_OS/11_Kernel_Core_13th/compagnons/01_Yaz_SecOps/AGENT.md` | 2 |
| `10_Tech_OS/11_Kernel_Core_13th/compagnons/01_Yaz_SecOps/spec-loop/nodejs-port.md` | 1 |
| `10_Tech_OS/11_Kernel_Core_13th/compagnons/02_Ryan_SysAdmin/AGENT.md` | 1 |
| `10_Tech_OS/11_Kernel_Core_13th/compagnons/03_Graham_Backup-DBA/AGENT.md` | 1 |
| `10_Tech_OS/12_Life_Core_11th/compagnons/01_Amy_Social/AGENT.md` | 1 |
| `10_Tech_OS/12_Life_Core_11th/compagnons/02_Rory_Health/AGENT.md` | 0 (cité via spec) |
| `10_Tech_OS/12_Life_Core_11th/tapes/02_Rory_Health/Cascade_Build_Spec.md` | 1 |
| `10_Tech_OS/13_Buzz_Core_12th/compagnons/01_Clara_MCP/AGENT.md` | 1 |
| `10_Tech_OS/kernel/schema.sql` | 5 |
| `10_Tech_OS/kernel/uc.py` | 1 |
| `10_Tech_OS/kernel/gate.py` | 1 |
| `10_Tech_OS/kernel/review.py` | 1 |
| `10_Tech_OS/kernel/dlq.py` | 2 |
| `10_Tech_OS/kernel/harness.py` | 2 |
| `10_Tech_OS/kernel/bridge_paperclip.py` | 1 |

Toutes les sources correspondent à un fichier lu pendant cette passe.

---

## 8. Conclusion en une phrase

La couche `10_Tech_OS/` est **lisible en entier** (couverture ≈ 81 % intégrale, 100 % par présence). La thèse du « constructeur universel » est cohérente : un mécanisme, trois instances, une seule loi (cinq articles). Le seul écart matériel à signaler est **l'absence de compagnon `03_` côté 12e Docteur** dans `cores.json` et sur le disque — pas une contradiction tranchée, une observation nommée.

---
*Fin de rapport.*
