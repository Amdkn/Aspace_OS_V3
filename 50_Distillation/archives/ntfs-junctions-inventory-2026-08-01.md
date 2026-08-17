---
type: Archive
title: NTFS Junctions Inventory — 2026-08-01
description: Le fichier `Backup_01/_manifests/codex_memory_junctions_2026-08-01.json` inventorie les jonctions NTFS actives au 2026-08-01 — un type de lien que `os.walk` ne voit pas et qui a déjà coûté un comptage de 13,8 millions de fichiers là où il y en avait 14 613.
tags: [ntfs, junctions, manifest, walk, comptage, 2026-08-01, anti-piege]
generated: { by: minimax-m3, at: 2026-08-17T23:35:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-17T23:35:00Z }
sources:
  - id: junction-manifest
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/Backup_01/_manifests/codex_memory_junctions_2026-08-01.json"
    title: Inventaire des jonctions NTFS (extrait lu directement)
    last_modified: 2026-08-01
  - id: canon
    resource: "C:/Users/amado/ASpace_OS_V3/40_Memory_Wiki_OKF/canon/CANON-profil-racine.md"
    title: Canon du poste — §4 deux pièges de ce disque (jonctions NTFS, comptage naïf)
    last_modified: 2026-08-17
okf_version: "0.2"
---

# NTFS Junctions Inventory — 2026-08-01

## Fichier source

`C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/Backup_01/_manifests/codex_memory_junctions_2026-08-01.json`

Mesuré à partir du **2026-08-01**, soit la veille du versement V3 du
2026-08-02. C'est un **inventaire machine** d'un type de lien particulier
de Windows : les **jonctions NTFS** (équivalent des liens symboliques
pour les répertoires, mais **opaques** aux outils de parcours naïfs).

## Structure d'une entrée

Chaque entrée a **deux champs** :

```json
{
  "Name": "<nom court>",
  "Target": "<chemin absolu Windows>"
}
```

Exemple (premier échantillon) :

```json
{
  "Name": "amadeus-01-identity",
  "Target": "C:\\Users\\amado\\ASpace_OS_V2\\00_Amadeus\\01_Identity_Core\\graphify-burst"
}
```

**Le nom est court, la cible est profonde** — la jonction **amadeus-01-identity**
se trouve quelque part dans l'arborescence de l'utilisateur et **pointe
vers** un dossier `graphify-burst` qui contient la sortie d'un pipeline
Graphify. C'est un **raccourci structurel** : l'agent qui cherche
`amadeus-01-identity` est dirigé vers le bon sous-dossier.

## Échantillon mesuré (10 premières entrées)

| Nom | Cible (résumée) |
|---|---|
| `amadeus-01-identity` | `00_Amadeus/01_Identity_Core/graphify-burst` |
| `amadeus-02-bio` | `00_Amadeus/02_Bio_Metrics/graphify-out` |
| `amadeus-02-infra` | `00_Amadeus/02_System_Infra/graphify-out` |
| `amadeus-05-oss-tstwin` | `00_Amadeus/05_OSS_TSTwin/graphify-out` |
| `amadeus-05-oss-twin` | `00_Amadeus/05_OSS_Twin/graphify-out` |
| `amadeus-archives` | `00_Amadeus/04_Digital_Memory/Archives/graphify-out` |
| `amadeus-archives-root` | `00_Amadeus/04_Digital_Memory/Archives/graphify-out` |
| `amadeus-memory-continuations` | `00_Amadeus/memory_continuations/graphify-out` |
| `app-.agent` | `C:/Users/amado/.agent/graphify-out` |
| `app-.agents` | `C:/Users/amado/.agents/graphify-out` |

**Pattern visible** : les jonctions s'appellent `amadeus-*` ou `app-*`
et pointent quasi-systématiquement vers des `graphify-out/` ou
`graphify-burst/`. C'est l'infrastructure d'**accès rapide aux sorties
de pipeline** : un agent qui demande `amadeus-01-identity` atterrit
directement sur le bon dump.

## Pourquoi ce manifest est archivé ici

Le canon du poste (CLAUDE.md §4) **a payé le prix** d'un `os.walk` naïf
sur les jonctions NTFS :

> **« Jonctions NTFS — 47 recensées dans la KB. `os.path.islink()` ne les
> voit pas. Un `os.walk` naïf a compté 13,8 millions de fichiers là où
> il y en avait 14 613. »**

Le manifest `codex_memory_junctions_2026-08-01.json` est la **réponse
documentée** à ce piège : un inventaire explicite que tout compteur
d'archivage peut consulter pour **exclure** les jonctions et compter
les **vrais** fichiers uniques.

## Le marqueur technique à utiliser

Le canon du poste documente le **bit NTFS à tester** :

```python
RP = getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0x400)
bool(entry.stat(follow_symlinks=False).st_file_attributes & RP)
```

**`FILE_ATTRIBUTE_REPARSE_POINT`** est le flag qui marque une jonction.
Sans ce test, un `os.walk` entre dans la jonction et **multiplie** le
comptage par la taille du sous-arbre cible.

## La procédure de suppression d'une jonction

> **« Pour supprimer une jonction : `os.rmdir` uniquement. `rmtree`,
> `rm -rf` et `Remove-Item -Recurse` suivent le lien et détruisent la
> cible réelle. »**
>
> — canon du poste

`os.rmdir` supprime **le lien** (la jonction elle-même), pas la cible.
Les autres commandes **détruisent la cible**, ce qui est une perte de
données silencieuse — d'où l'archive.

## Concepts liés

- [[memory-compact-trash-snapshots]] — sibling dans Backup_01, autre archive du 2026-08-01.
- [[data-role-a3-archives-officer]] — la doctrine qui a permis de préserver ce manifest plutôt que de le supprimer comme une jonction orpheline.
