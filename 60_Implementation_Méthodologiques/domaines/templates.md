---
type: Method
title: Méthode de distillation des kits templates V2 → V3
description: Méthode de lecture et classification des 9 kits templates de `02_Templates/` selon les 4 verdicts (canon / synthese-datee / superseded / orphelin), avec les patterns transversaux et la trace d'utilisation.
tags: [methode, distillation, templates, kits, vague-2, verdict, classification]
generated: { by: minimax-m3, at: 2026-08-19T20:35:00Z }
verified:
  - { by: process:application_sur_9_kits_v2, at: 2026-08-19T20:35:00Z }
sources:
  - id: brief-vague2-templates
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_vague2/BRIEF_templates.md"
    title: "Brief vague 2 — distillation Templates"
    last_modified: 2026-08-19
  - id: garde-fou-canon
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_vague2/GARDE_FOU.md"
    title: "GARDE-FOU vague 2 (vérité source, lecture seule, périmètre)"
    last_modified: 2026-08-19
  - id: rapport-parallele-normatif
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_vague2/RAPPORT_normatif-sdd-prd.md"
    title: "Rapport parallèle vague 2 — distillation SDD/PRD (méthode sœur)"
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Méthode de distillation des kits templates V2 → V3

## Position dans la chaîne des méthodes

Cette méthode est **sœur** de la méthode de distillation normative (cf. `60_Implementation_Méthodologiques/domaines/normatif-sdd-prd.md`). Toutes deux appliquées par la même vague 2.

| Dimension | Distillation normative | Distillation templates |
|---|---|---|
| Corpus | SDD (31) + PRD (51) = 82 docs | 9 kits + racine (~13 entrées) |
| Verdict dominant | `superseded` (45/82 = 55 %) | `synthese-datee` (6/9 kits) |
| Mode lecture | sélective par statut/nom | exhaustive pour les petits kits, sélective pour les gros |
| Trace dans V3 | forte (SDD-006 amendé, 8 domaines) | faible (2 kits seulement avec trace) |
| Pattern central | canonisation + amendement append-only | pattern transversal + moules de référence |

## Pourquoi cette méthode diffère

Un kit template n'est **pas une doctrine** :
- Une doctrine statue : « ceci est la règle ».
- Un kit propose : « voici comment construire un truc qui ressemble à ça ».

La distillation d'un kit pose donc des questions différentes :

```
Pour un kit :
  1. De quoi est-il le moule ?
     (skill, agent, infra, doctrine, brief, configuration, format)
  2. Quelles contraintes impose-t-il ?
     (frontmatter, structure de dossiers, naming, schemas)
  3. A-t-il été utilisé ?
     (chercher des traces dans V3 : références, imports, agents créés)
  4. Si oui, la marque est-elle exacte ?
     (sinon : synthèse-datee — daté sur un point, canon sur le reste)
```

## Le verdict `synthese-datee` typique d'un kit

Un kit template est presque toujours `synthese-datee` plutôt que strictement `canon`, parce qu'il cite :
- Des **noms de produits** qui changent (modèles LLM, providers d'API).
- Des **prix** qui dérivent (Bedrock, NAT gateway, Fargate).
- Des **versions de CLI** qui évoluent (CDK, Node, Claude Code).

Tandis qu'il reste **canon** sur :
- Les **patterns architecturaux** (single chokepoint, kill switches, audit log append-only).
- Les **formats** (frontmatter de skill, structure de dossier agent).
- Les **méthodes** (interview en rounds, wargame en 8 critères).

C'est cette **asymétrie** que `synthese-datee` capture précisément.

## Procédure en 6 étapes

### Étape 1 — Localisation

Le brief Templates pointe `02_Templates/`. Le chemin réel est :
```
C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/
```

C'est le **mapping V2 → V3** implicite. Pour les distillateurs futurs : le chemin canon est `20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/`, pas la racine V3. Le mapping n'est pas explicite — un futur distillateur peinerait.

### Étape 2 — Inventaire brut

Compter les fichiers par kit, **en filtrant le bruit** :

```bash
cd "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/"
for d in */; do
  echo "=== $d ==="
  find "$d" -type f -not -path "*/__MACOSX/*" -not -path "*/__pycache__/*" -not -name "*.pyc" | wc -l
done
```

Bruit à exclure systématiquement :
- `__MACOSX/` (artefacts de décompression ZIP).
- `__pycache__/`, `*.pyc` (Python compilé).
- `.git/` (si jamais inclus).

Le brief Templates annonçait 136 fichiers. **Mon décompte est 203 fichiers utiles** (sans bruit). La différence s'explique par les `.pyc`, `__MACOSX/`, et les miroirs.

### Étape 3 — Lecture stratégique

Pour chaque kit :
- **Petits kits** (≤10 fichiers) : lecture exhaustive de tous les `.md`.
- **Gros kits** (>30 fichiers) : lecture du README + du fichier central (BLUEPRINT.md / SKILL.md / README.md) + inventaire des autres.
- **PDFs** : lecture du PDF s'il est <20 pages ; sinon, lecture de la première page + signalement comme PDF « non-lu intégralement ».

### Étape 4 — Classification par verdict

Pour chaque kit, 4 questions dans l'ordre :

1. **A-t-il été utilisé dans V3 ?** Si oui, chercher la trace (LEDGER.md, fichiers miroirs, agents/skills importés).
2. **Est-il superseded par un autre kit du corpus ?** Si oui, nommer le successeur (sinon, c'est un lien mort).
3. **Le contenu est-il daté sur les références ?** Si oui, identifier ce qui est daté vs ce qui reste canonique.
4. **Se rattache-t-il à quelque chose ?** Si non, c'est un orphelin.

Le verdict tombe mécaniquement :
- Trace + daté sur refs + canon sur patterns → `synthese-datee`.
- Superseded par X → `superseded` (X nommé).
- Aucun rattachement → `orphelin`.
- Strictement valide et utilisé → `canon` (rare).

### Étape 5 — Cross-référence des patterns transversaux

Après la classification kit par kit, **identifier les patterns qui apparaissent dans ≥3 kits**. Ces patterns sont la signature universelle du domaine (cf. [[concept-five-cross-cutting-patterns]]).

Les 5 patterns retenus :
1. **Agents-as-folder** (ClaudeClaw V2, V3, silver-platter, FULL Agentic).
2. **Kill switches** (ClaudeClaw V2, V3, Enterprise).
3. **Audit log append-only** (ClaudeClaw V2, V3, Enterprise).
4. **Three-layer memory** (ClaudeClaw V2, V3, Memory Architect, FULL Agentic).
5. **Exfiltration guard** (ClaudeClaw V2, V3, Enterprise).

### Étape 6 — Production des livrables

Trois livrables en parallèle (cf. brief) :
1. **Concepts OKF v0.2** dans `50_Distillation/domaines/templates/`.
2. **Méthode** dans `60_Implementation_Méthodologiques/domaines/templates.md` (ce fichier).
3. **Triplets JSONL** dans `70_Onthologies/triplets/dom-templates.jsonl`.

Plus le rapport dans `50_Distillation/_briefs_vague2/RAPPORT_templates.md`.

## Pièges observés

1. **Compte de fichiers annoncé sous-estimé** — le brief dit 136 ; la mesure est 203 utiles. Toujours mesurer soi-même.
2. **Bruit ZIP/Python** — `__MACOSX/`, `__pycache__/`, `*.pyc` consomment du quota d'inventaire sans valeur. Toujours filtrer.
3. **Clones upstream déguisés en kits** — `FULL Agentic Patterns Kit/` est un clone GitHub ; le traiter comme un kit original serait une erreur. Le verdict `synthese-datee` sur le contenant + canon sur le contenu gère ça proprement.
4. **Fichiers racine hors kits** — `os-audit-SKILL.md` et `claude-plugins-guide_2026-07-25.md` ne sont **pas** des kits tiers mais des artefacts A'Space. Les classer à part.
5. **Taille ≠ valeur** — `Memory Architect Kit` a 2 fichiers mais est riche ; `Claude Certified Architect Study Guide` a 1 fichier et est orphelin. Toujours pondérer par la qualité du contenu, pas la quantité.
6. **Trace = LEDGER** — le seul kit avec une trace vérifiable et précise est `fable-wargame-kit` (via `LEDGER.md` daté 2026-07-15). Toujours chercher le LEDGER en premier.

## Concepts liés

- [[concept-template-as-moule]] — la distinction template/doctrine qui justifie cette méthode
- [[concept-five-cross-cutting-patterns]] — le résultat central de cette distillation
- [[concept-kits-utilisation-trace]] — le tableau global de trace
