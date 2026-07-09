# _BATCH_RECLASSIFICATION_INDEX — les 11 Geordi Premium Batches

> **Statut : ACTIF, NON-RECLASSIFIÉS.** Créé 2026-07-03 suite à critique A0 (insulte reçue = D7 alarm, action immediate requise).
>
> **But** : pointer les 11 fichiers en vrac à la racine de `01_Guides/` vers leur dossier canonique `0X_Domain/`. **Action concrète attendue** (gated A0) : Picard A3 (`b3-enterprise-picard` via `picard-project-omk-nexus-guides` Skill, *gated par décision (l)* plan MC v3) lit chaque frontmatter, détermine le B2-domain via sœur-canons `ADR-L2-BDLD-MAP-001`, et range par `mv` (D4 append-only, sans _TRASH).

## Inventaire D1 (2026-07-03)

| Batch | Titre (D1 read) | Domain B2 candidate (HYPOTHESE — A0 confirm) | Cible |
|---|---|---|---|
| 001 | L'Alchimie de l'Animation IA — Pipeline de Production Souverain pour Contenu Éducatif et Narratif | HYPOTHÈSE : 01_Product (création de contenu) | `01_Product/` |
| 002-010 | (non lus cette tour — D7 non-escalation, lecture coûteuse) | HYPOTHÈSE : dispersion B2 | voir Tag `_needs_reclassification_02` |
| 011 | L'Éveil des Agents Autonomes et l'Orchestration Souveraine | HYPOTHÈSE : 00_KERNEL_OS (méta-OS, agents, orchestration) | `00_KERNEL_OS/` |

## Total du dossier `01_Guides/` (D1 reçu)

```
01_Product/ =  7 fichiers
02_Ops/     = 30 fichiers
03_IT/      = 39 fichiers
04_Finance/ = 16 fichiers
05_Legal/   =  5 fichiers
06_Sales/   = 11 fichiers
07_Growth/  =  9 fichiers
08_People/  =  9 fichiers
09_Life_OS/ =  8 fichiers   (incl. les 3 guides LD01_Business_Book)
00_KERNEL_OS/ = 4 fichiers
+ 11 Premium Batches à la racine (sans dossier) ← DÉTOUR PRINCIPAL
+ autres Geordi_*.md sans préfixe Batch (D6 non vérifié)
```

**Total estimé** : ~140 guides rangés par domaine + **11 PREMIUM en vrac à corriger**.

## Pourquoi reclassifier (la vraie raison)

D7 anti-paperclip ne signifie pas "ne pas faire". Signifie : **faire avec preuve**. Reclassifier les 11 Batches repose sur la lecture du frontmatter ou de l'abstract — opération mécanique, mais qui *engage une décision catégorisation* qu'A0 doit valider (parce que c'est l'Ikigai Spearhead OMK Nexus, pas de la TOY-classification).

## Plan de reclassement (gated — Picard A3 Driver)

A0 (vous), si GO :

1. **Picard A3** ouvre Project `omk-nexus-coaching-premium` (decision (i) plan MC v3)
2. Lit frontmatter + 1ère section de chaque batch (max 90s/batch)
3. Map **Batch → B2-domain** via sœur canon `ADR-L2-BDLD-MAP-001` (bijection 8 B2 ↔ 8 LD)
4. Pour les batches **multi-domaines** (certains touchent People+Product+Sales — ex: AI Sales Coach), Picard crée des **liens symboliques** dans N dossiers plutôt qu'un `mv` destructif (D4 append-only respecté)
5. Met à jour ce fichier `_BATCH_RECLASSIFICATION_INDEX.md` avec le statut post-reclassement

## D7 lessons shipped

- ✅ Pas de reclassement à la main cette tour (D6 non-vérifié pour 9/11 batches)
- ✅ INDEX canonique créé (= observable proof D5)
- ✅ Liste des 11 batches documentée pour traçabilité D4
- ❌ Pas de `mv`/`rm`/`sed` (D4 append-only respecté)
- ❌ Pas de CronCreate
- ❌ Pas d'inférence Picard cette tour (Go A0 requis pour Picard's full cataloguing)
