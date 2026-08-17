---
type: Format spec
title: OKF v0.2 — le format des concepts de ce bundle
description: Frontmatter minimal, provenance par sources, et les trois niveaux de confiance qui se déduisent mécaniquement du champ verified.
tags: [okf, format, provenance, confiance]
generated: { by: claude-opus-5, at: 2026-08-17T15:10:00Z }
verified:
  - { by: human:amdkn, at: 2026-08-17T15:05:00Z }
sources:
  - id: canon-local
    resource: "~/.claude/CLAUDE.md — section « Mémoire canonique — OpenWiki + OKF »"
    title: Canon du poste
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Le frontmatter minimal

Chaque concept de ce bundle ouvre sur ce bloc YAML :

```yaml
---
type: <Integration | Security Model | Vulnerability | Backend | Playbook | …>
title: <titre lisible>
description: <une phrase>
tags: [<…>]
generated: { by: <acteur>, at: <ISO 8601> }
verified:
  - { by: <acteur>, at: <ISO 8601> }
sources:
  - id: <clé stable>
    resource: <URL, chemin, ou description de portée>
    title: <libellé>
    last_modified: <YYYY-MM-DD>
okf_version: "0.2"
---
```

`description` n'est pas décoratif : c'est le **critère d'indexation**. Un
concept sans description ne se retrouve pas. Un placeholder générique est pire
que rien — il pollue l'index en prétendant l'enrichir.

# Les trois niveaux de confiance

C'est tout l'intérêt du format. Le niveau ne se déclare pas, il **se déduit**
du champ `verified` :

| `verified` | Niveau |
|---|---|
| absent | **non vérifié** |
| acteurs non-`human:` uniquement | **confirmé par machine** |
| au moins un `human:<id>` | **revu par un humain** |

Un acteur est soit une machine (`claude-opus-5`, `process:curl-head`,
`process:supabase-management-api`), soit une personne (`human:amdkn`).

**Une affirmation mesurée et une affirmation supposée ne doivent jamais se
ressembler.** C'est ce qui a coûté six tables appliquées au mauvais projet
Supabase, et une sonde de test qui accusait le mauvais coupable pendant trois
campagnes.

Convention de ce bundle : ouvrir le corps par une ligne de citation qui énonce
le niveau, pour qu'un lecteur pressé ne rate pas le frontmatter.

> **Niveau de confiance : confirmé par machine.** Chaque ligne vient d'un appel
> HTTP réel.

# La provenance

`sources` répond à « d'où sort cette affirmation ». Une `resource` peut être
une URL, un chemin de fichier, ou la **description d'une portée de mesure** —
par exemple `"information_schema.columns sur ndvqwcapwcnpdvknxcjw, avant/après
migration"`. Cette dernière forme est souvent la plus honnête : elle dit ce qui
a été regardé, pas seulement où.

# Après avoir écrit un concept

1. Ajouter une ligne dans l'`index.md` du sous-bundle, sous `# Files`.
2. Ne **jamais** poser de lien — forme `[[nom]]` ou forme Markdown — vers un
   concept qui n'existe pas. Vérifier avant d'écrire.

**Un lien mort ment à l'avenir.** Il fait croire qu'une connaissance a été
consignée alors qu'elle a été perdue, et le lecteur suivant cherchera un
fichier qui n'a jamais existé.

# Ce qui ne va pas dans ce bundle

- **Les secrets.** Jamais, ni valeur ni fragment. Le préfixe suffit (`ck_…`,
  `sbp_…`) et permet d'identifier la famille de clé sans l'exposer.
- Ce que le dépôt raconte déjà : structure du code, historique git, contenu
  d'un `CLAUDE.md` versionné.
- Ce qui n'intéresse que la conversation en cours.
