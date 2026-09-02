---
type: Architecture
title: La cartographie mesurée de V3 — un instrument régénéré, pas un document écrit
description: Pourquoi `CARTOGRAPHIE.md` et le §0 du CLAUDE.md racine sont générés par `scripts/cartographier_v3.py`, ce que la mesure a révélé (71 % de vidages de sessions, OKF à 0,6 %), et les deux pièges du comptage.
tags: [cartographie, arborescence, jonction-ntfs, quota, sessions_md, mesure]
generated: { by: claude-sonnet-4-6, at: 2026-08-30T01:00:00Z }
verified:
  - { by: human:amdkn, at: 2026-08-31T21:28:13Z }
  - { by: claude-sonnet-4-6, at: 2026-08-30T01:00:00Z }
sources:
  - id: generateur
    resource: "ASpace_OS_V3/scripts/cartographier_v3.py"
    title: Le générateur de la carte
    last_modified: 2026-08-30
  - id: carte
    resource: "ASpace_OS_V3/CARTOGRAPHIE.md"
    title: La carte pleine (arborescence 3 niveaux), régénérable
    last_modified: 2026-08-30
  - id: mesure
    resource: "Mesure du 2026-08-30"
    title: 10 731 fichiers, 6 531 .md, 2,8 Go, en 0,3 s
    last_modified: 2026-08-30
okf_version: "0.2"
---

# Pourquoi cet instrument existe

Le CLAUDE.md racine ne portait aucune carte. Conséquence mesurée : chaque
session redecouvrait l'arborescence à l'aveugle, au prix du quota, et
concluait « non documenté » sur ce qui existe. Une carte écrite à la main
vieillit et ment ; celle-ci se régénère en 0,3 s.

# Ce que la mesure a révélé

- **4 647 `.md` sur 6 531 (71 %) sont des vidages de sessions** dans
  `00_Amadeus/30_MEMORY_CORE/sessions_md/` — de la matière première, pas de
  la connaissance rédigée.
- **Le bundle OKF ne porte que 36 `.md` sur 6 531 (0,6 %)**. Chercher là et
  s'arrêter, c'est manquer le reste ; le CLAUDE.md racine porte désormais la
  carte complète, structurée autour d'elle.
- La connaissance rédigée vit dans `70_Onthologies/pulse/` (298), le
  `_ARCHIVE_coach-os-briefs/` (154), `50_Distillation/domaines/` (161),
  `30_Business_OS/09_Blueprints/coach-os-refonte/` (194).

# Les deux pièges du comptage

## Jonction NTFS

`os.path.islink()` ne voit pas les jonctions ; un `os.walk` naïf suit le lien
et recompte la cible (13,8 millions de fichiers pour 14 613 réels). Le garde
est `FILE_ATTRIBUTE_REPARSE_POINT` :

```python
RP = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
bool(entry.stat(follow_symlinks=False).st_file_attributes & RP)
```

La carte **signale** une jonction sans la suivre : la taire ferait croire à
une lacune, la suivre ferait exploser le compte.

## Le compte direct contre le cumul

La première version de « Le point qui compte » cherchait le dossier OKF dans
la liste aplatie et prenait son compte **direct** : 4 `.md` — les seuls à la
racine du bundle (`index.md`, `OKF.md`, `quickstart.md`…). Les concepts
vivent dans `architecture/`, `operations/`, `integrations/`, `learning/` :
le compte direct disait **0,1 %** et mentait. Le cumul du nœud dit **36
(0,6 %)** et colle au CLAUDE.md. Règle : pour un pourcentage de part, c'est
le cumul du nœud, jamais le compte direct du dossier.

# Vérifier que la carte dit vrai

```bash
python C:/Users/amado/ASpace_OS_V3/scripts/cartographier_v3.py
```

Si un compte diffère d'un `find` sur le corpus, c'est l'instrument qu'il faut
réparer, pas le chiffre qu'il faut ajuster.

Voir aussi [[porte-argent-triptyque-filtres]], qui partage le garde de jonction.
