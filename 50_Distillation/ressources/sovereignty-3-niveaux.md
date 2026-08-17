---
type: Concept
title: Souveraineté — trois niveaux (infra, code, mémoire)
description: Le principe directeur de L0 Tech OS, gouverné par Rick. Trois manifestations : infra (Trust Zone ADR-007), code (ADRs immuables), mémoire (TARDIS Protocol). Née de la perte d'A0_Memory du 2026-03-05.
tags: [sovereignty, trust-zone, adr-immutability, tardis, rick, l0, security]
generated: { by: minimax-m3, at: 2026-08-17T20:40:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T20:40:00Z }
sources:
  - id: concept-sovereignty
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/concepts/concept_sovereignty.md"
    title: "Concept: Sovereignty (Souveraineté dans A'Space OS)"
    last_modified: 2026-05-10
  - id: concept-adr
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/concepts/concept_adr.md"
    title: "Concept: ADR (Architecture Decision Records)"
    last_modified: 2026-05-10
  - id: junctions-map
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/00_Index/JUNCTIONS_MAP_2026-08-02.md"
    title: "Cartographie des jonctions NTFS — 2026-08-02"
    last_modified: 2026-08-02
okf_version: "0.2"
---

# Souveraineté — trois niveaux (infra, code, mémoire)

> La capacité de **définir les règles du jeu** sans qu'aucun autre agent puisse les outrepasser.
> Principe directeur de L0 Tech OS, gouverné par Rick.

## 1. Trois niveaux

### Niveau 1 — Infra (Trust Zone, ADR-007 fondateur)

```
C:\Users\amado\  ← Trust Zone
├── A'Space OS V2/
├── .claude/
├── .gemini/
├── .skills/
└── ...
```

**Règle** : rien ne vit à la racine de `C:\`. Tout est dans la Trust Zone.
Née de la **purge de `C:\Aspace00` (2026-03-05)** qui a causé la perte d'`A0_Memory`.
La Trust Zone est née de cette leçon.

### Niveau 2 — Code (ADRs immuables, Rick's Law)

Les ADRs sont **immuables**. Rick est le seul Guardian qui peut les créer. Aucun autre agent
ne peut les modifier rétroactivement. Voir `concept-adr` et `adr-immutability-ricks-law`.

### Niveau 3 — Mémoire (TARDIS Protocol)

Le TARDIS Protocol assure que toute modification d'agent est historisée. **La mémoire = souveraineté.**
La perte d'historique = perte de souveraineté.

## 2. Loi du Checkpoint Profond (D6 doctrine)

Née de la perte d'A0_Memory du 2026-03-05.

> Un technicien automatise. Un Architecte vérifie ce qu'il laisse derrière.

Checklist avant toute purge/migration :

- [ ] Lister TOUS les dossiers exclus
- [ ] Checkpoint obligatoire pour > 100 MB
- [ ] Inventaire avant purge (rapport de ce qui Ne Sera Pas)
- [ ] Commentaire obligatoire : `# EXCLU — validé par Amadeus le [date]`

## 3. Souveraineté ≠ centralisation

| | Souveraineté | Centralisation |
|---|---|---|
| Règles | Définies par le Guardian | Imposées par un système |
| Exceptions | Via nouveaux ADRs | Via overrides |
| Traçabilité | TARDIS Protocol | Audit logs |
| Risque | Fragmentation | Single point of failure |

La souveraineté **n'est pas** centralisation : Rick définit les règles, mais les A2/A3
exécutent librement dans leur domaine.

## 4. Jonctions NTFS — arme de la souveraineté (et piège)

Geordi héberge **159 jonctions NTFS** classifiées en 10 catégories (mesure 2026-08-02).
Les catégories dangereuses pour la souveraineté sont :

- `intra_g` (16) : duplication intra-G (1 195 md ré-joués)
- `cross_para_*` (25) : franchissement de frontière PARA
- `external_*` (36) : franchissement hors ASpace_OS_V2

**Piège** : `os.walk` qui suit les jonctions produit plusieurs fois le volume observé
et franchit les frontières de sovereignty. Toujours détecter via
`stat.FILE_ATTRIBUTE_REPARSE_POINT` (0x400) et dédupliquer par `realpath`.

## 5. ADR fondateur

| ADR | Sujet | Rôle |
|---|---|---|
| **ADR-007** | Trust Zone `C:\Users\amado` | fondateur, sans lui aucune autre décision ne tient |

## Liens entrants

- `constitution-aspace-v1.md` — la Constitution 2026-07-12 rétrograde la sovereignty en jurisprudence
- `adr-immutability-ricks-law.md` — la manifestation code de la sovereignty
- `ntfs-junction-aliasing.md` — l'outillage filesystem de la sovereignty
