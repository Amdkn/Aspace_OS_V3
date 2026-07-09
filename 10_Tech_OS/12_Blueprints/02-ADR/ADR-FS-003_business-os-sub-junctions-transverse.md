# ADR-FS-003 — Sub-Junctions Business OS Links (Resources / Archives / 12WY / GTD / DEAL)

**Date :** 2026-05-22
**Auteur :** A0 Amadeus + A2 Claude Code
**Statut :** RATIFIÉ — EXÉCUTÉ
**Type :** Architecture Decision Record (Filesystem / L2 view)
**Portée :** Vue Business OS sur les ressources/archives PARA + frameworks transverses Life OS
**Ancré sur :** ADR-FS-001 § Couche 3 · ADR-FS-002 (script porteur)

---

## Contexte

ADR-FS-001 § Couche 3 prévoyait 5 sub-junctions transverses dans `30_Business_OS\…\04_Business_Domains\00_Links\` pour exposer côté Business OS les frameworks de productivité Life OS + les Resources/Archives PARA, **sans copie**. Elles n'avaient pas encore été créées.

## Décision

5 junctions ajoutées dans `00_Links\` (Business OS) :

| Source | Cible (SoT) | Justification |
|--------|-------------|---------------|
| `00_Links\res` | `PARA\03_Resources_Geordi` | Templates/SOPs partagés entre tous les secteurs DC |
| `00_Links\arch` | `PARA\04_Archives_Data` | Artefacts gelés (legacy specs, projets archivés) |
| `00_Links\snw` | `20_Life_OS\23_12WY_SNW` | Cadence 12-Week Year accessible par les Squad Managers |
| `00_Links\gtd` | `20_Life_OS\25_GTD_Cerritos` | Inbox GTD pour A3 quand chaos > capacity |
| `00_Links\deal` | `20_Life_OS\26_DEAL_Protostar` | Pipeline DEAL pour libération projets |

### Pourquoi pas par secteur

Une junction unique par framework à la racine `00_Links\` plutôt que 8 junctions par framework (1 par secteur DC) :

- Évite la pollution × 8 dans chaque secteur
- Une seule vérification d'intégrité
- Source de vérité unique côté Life OS (le framework Life), pas dupliquée par contexte business

Les A3 Marvel/DC accèdent à leur 12WY via `<biz>\…\04_Business_Domains\00_Links\snw\…`, qui résout sur le même contenu que `<para or short>\snw\…`.

## Conséquences

### Positives
- 5 nouvelles junctions = 5 chemins courts cross-domain (Biz ↔ Life)
- Pas de duplication
- Cohérent avec sentinelles racine `_\{res, arch, snw, gtd, deal}` (3 voies vers la même SoT — choisir selon contexte)

### Négatives
- Junctions multiples vers la même cible peuvent perturber un outil naïf (rare ; les outils respectent les junctions modernes)

## Audit post-exécution

`00_Links\` contient maintenant 8 junctions :
- 3 historiques : `02_alykaly-os-v2`, `20_Life_OS_PARA_Portal`, `alykaly-front`
- 5 nouvelles : `res`, `arch`, `snw`, `gtd`, `deal`

Total junctions Business OS = 14 (8 dans 00_Links + 6 dans 00_Summers_QuickAccess).

## Références

- ADR-FS-001 § Couche 3
- ADR-FS-002 — script `Setup-ASpace-Junctions.ps1` (porteur opérationnel)
