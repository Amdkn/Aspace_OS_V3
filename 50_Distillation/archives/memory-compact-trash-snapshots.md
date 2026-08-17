---
type: Archive
title: Memory Compact Trash Snapshots — 4 sauvegardes `_TRASH_2026-07-XX_mem_compact`
description: Le dossier `Backup_01/memory_duplicates/` contient 4 instantanés `_TRASH_2026-07-02_mem_compact` à `_TRASH_2026-07-26_mem_compact`, témoins des compactions de mémoire successives de juillet 2026 ; seul le premier contient un `MEMORY_pre.md` mesuré.
tags: [backup, mem-compact, trash, memory, snapshots, 2026-07]
generated: { by: minimax-m3, at: 2026-08-17T23:30:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-17T23:30:00Z }
sources:
  - id: backup-root
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/Backup_01/"
    title: Annuaire Backup_01 (6 fichiers, 2 sous-dossiers)
    last_modified: 2026-08-01
  - id: trash-snapshots
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/Backup_01/memory_duplicates/"
    title: 4 instantanés _TRASH_2026-07-XX_mem_compact
    last_modified: 2026-07-26
  - id: memory-pre
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/Backup_01/memory_duplicates/_TRASH_2026-07-02_mem_compact/MEMORY_pre.md"
    title: Premier snapshot — MEMORY_pre.md (seul fichier du dossier 1)
    last_modified: 2026-07-02
  - id: junction-manifest
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/Backup_01/_manifests/codex_memory_junctions_2026-08-01.json"
    title: Manifest de jonctions NTFS mesuré
    last_modified: 2026-08-01
okf_version: "0.2"
---

# Memory Compact Trash Snapshots — 4 sauvegardes `_TRASH_2026-07-XX_mem_compact`

## Périmètre mesuré

Le dossier `Backup_01/` (date de création **2026-08-01**, soit la veille
de l'archivage V3) contient **2 sous-dossiers** :

| Sous-dossier | Contenu |
|---|---|
| `_manifests/` | `codex_memory_junctions_2026-08-01.json` (inventaire des jonctions NTFS) |
| `memory_duplicates/` | 4 dossiers `_TRASH_2026-07-XX_mem_compact/` |

Total : **6 fichiers** mesurés par `ls -la`.

## Les 4 instantanés de compaction

Liste exhaustive, ordonnée par date :

| # | Dossier | Date | Contenu mesuré |
|---|---|---|---|
| 1 | `_TRASH_2026-07-02_mem_compact/` | 2026-07-02 | `MEMORY_pre.md` (1 fichier) |
| 2 | `_TRASH_2026-07-10_mem_compact/` | 2026-07-10 | (non détaillé dans ce brief) |
| 3 | `_TRASH_2026-07-15_mem_compact/` | 2026-07-15 | (non détaillé dans ce brief) |
| 4 | `_TRASH_2026-07-26_mem_compact/` | 2026-07-26 | (non détaillé dans ce brief) |

**Périodicité** : 8 / 5 / 11 jours — non régulière, déclenchée par
**événement** (probablement quand la taille de la mémoire active
dépassait un seuil, pas un cron).

## Le pattern `_TRASH_`

Le préfixe `_TRASH_` est explicite : ce sont des **artefacts destinés à
la suppression**, mais **préservés par la procédure `archive-and-document`**
d'A3 Data.

Citation de `A3_Data_Archives_Spec.md` :

> **« Data does not delete by default. »**

Les 4 instantanés sont la **preuve matérielle** de cette doctrine :
même ce qui s'appelait `_TRASH_` n'a pas été supprimé — **déplacé** dans
le périmètre archive.

## Le `MEMORY_pre.md` du 2026-07-02

C'est le **seul fichier** explicitement mesuré dans cette archive
(même si d'autres peuvent exister dans les dossiers 2/3/4, le brief
ne les a pas énumérés). Le nom `MEMORY_pre.md` suggère un **état
pré-compaction** : la mémoire **avant** qu'elle soit compactée, sauvegardée
pour ne pas perdre le contexte antérieur.

C'est un **garde-fou contre la compaction destructive** : si la compaction
introduit une régression, l'état pré-compaction est consultable.

## Le manifest de jonctions NTFS — sibling

Dans le même `Backup_01/_manifests/`, le fichier
`codex_memory_junctions_2026-08-01.json` est un **inventaire de jonctions
NTFS** (entrées `Name` + `Target` pointant vers des chemins
`graphify-out/` ou `graphify-burst/`).

Extrait (premier échantillon) :

```json
{
  "Name": "amadeus-01-identity",
  "Target": "C:\\Users\\amado\\ASpace_OS_V2\\00_Amadeus\\01_Identity_Core\\graphify-burst"
}
```

Ce manifest est le **complement** des snapshots : il documente la
**structure technique** (jonctions) qui sous-tend la **mémoire** que les
snapshots capturent.

## Concepts liés

- [[data-role-a3-archives-officer]] — la doctrine `Data does not delete by default` qui explique la préservation.
- [[ntfs-junctions-inventory-2026-08-01]] — le manifest sibling dans Backup_01.
- [[adr-sober-002-anti-paperclip-doctrine]] — la doctrine qui interdit la destruction.
