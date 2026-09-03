---
name: grill-me-intent
description: "Protocole Grill Me : transformer une déclaration brute de l'Originator en intent.md compilé dans _INBOX/<portier>/, prêt pour FROZEN. Utiliser quand l'opérateur ou un agent de maintenance énonce un irritant, un besoin ou un 'pourquoi maintenant'."
version: 1.0.0
platforms: [windows, linux, macos]
author: yaz_spec_l0
metadata:
  hermes:
    tags: [intent, interview, contrat-entree, ruban]
    category: self-evolution
    requires_tools: [terminal, read_file, write_file]
    source: "00_Amadeus/60_Tape_Specs/2026-09-02-intent-md-contrat-entree.md"
---

# Quand l'utiliser

- L'Originator (Amadou, ou un agent en maintenance autonome) énonce un irritant
  en langage brut : « ça rame », « cette vérif échoue encore », « il faut X ».
- Avant d'écrire une spec : l'intent est le **premier artefact de la chaîne**,
  il précède le ruban OKF dans `60_Tape_Specs/`.

# Pourquoi elle existe

Le contrat d'entrée (INTENT.MD) sépare le « Pourquoi » de la spécification.
Sans interview, une déclaration brute atteint le portier et se fait refuser —
ou pire, passe avec un critère non mesurable et le work meurt au build. Le
protocole Grill Me force la compilation des inconnues **avant** le portier.

# Le format INTENT.MD (contrat d'entrée)

```markdown
# INTENT: [nom-courte-initiative]
**Layer:** L0 | L1 | L2
**Originator:** Amadou | <agent en maintenance>
**Date:** YYYY-MM-DD
**Statut:** DRAFT | FROZEN

## 1. Irritant réel
Pourquoi maintenant ? Quel goulot ? Pourquoi les approches force-brute échouent ?

## 2. Résultat visé (mesurable)
L'état final vérifiable — pas la solution.

## 3. Contraintes non-négociables
- Budget tokens/coût max
- Blast radius (dossiers touchés / interdits)
- Garde-fous souverains (validation humaine si impact $ > 0)

## 4. Definition of Done
- [ ] Critère 1 (commande exécutable)
- [ ] Critère 2 (commande exécutable)
```

**Règle binaire** : une intent sans critère mesurable retourne à l'Originator.
Le test du ruban s'applique dès l'intent. Statut `FROZEN` = Yaz peut produire
la spec.

# Procédure (Grill Me)

1. **Lire la déclaration brute** telle qu'énoncée. Ne pas réécrire, ne pas
   inférer ce qui manque.

2. **Poser 3-5 questions d'edge-cases NON déductibles.** Zéro question
   d'évidence. Les axes portent sur ce qu'aucune lecture du corpus ne peut
   donner :
   - persistance : que se passe-t-il après reboot / compaction / semaine 2 ?
   - volume : combien d'items, à quelle cadence, quel pic toléré ?
   - vetos : qui peut annuler, et à quel seuil d'impact ?
   - coûts : budget tokens, budget temps, plafond $ par cycle.
   - échec : qu'est-ce qui prouve que ça a **échoué**, pas juste « pas fini » ?

3. **Compiler** l'intent au format ci-dessus et déposer :
   `_INBOX/<portier>/intent-<slug>-<date>.md`
   où portier ∈ {S1_Rick (L0), A1_Beth_Morty (L1), B1_Jerry_Summers (L2)} —
   le dossier décide de la couche, pas le frontmatter seul.

4. **Demander FROZEN** à l'Originator. Pas de FROZEN = l'intent reste DRAFT,
   il ne traverse pas le portier.

5. **Relayer** : FROZEN déposé → `gate.py run` admet → Yaz écrit la spec OKF
   dans `60_Tape_Specs/` → cycle von Neumann (claim, prédiction, build, review).

# Vérification

```bash
python 10_Tech_OS/kernel/gate.py check _INBOX/<portier>/intent-<slug>-<date>.md
```

Sortie attendue : `complet: true`, exit 0. Si exit 1, les `manques` listés
sont les questions que l'interview n'a pas fermées — retour à l'étape 2.

# Pièges

- **FROZEN par procuration est interdit.** Seul l'Originator gèle. Un agent de
  maintenance ne gèle pas sa propre intent de diagnostic : Rick tranche.
- **Les questions d'évidence sont une dette.** Si la réponse est lisible dans
  `uc.db`, le ruban ou un fichier daté, elle ne se pose pas.
- **L'intent ne contient pas la solution.** « Résultat visé » décrit l'état
  final vérifiable ; le « comment » appartient à la spec.
