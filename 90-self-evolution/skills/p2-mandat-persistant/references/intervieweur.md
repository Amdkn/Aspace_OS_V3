---
name: intervieweur
description: Protocole "Grill Me" — l'agent intervieweur transforme une déclaration brute de l'Originator en intent.md testable. Zéro question d'évidence.
version: 1.0.0
author: yaz_spec_l0
source: "00_Amadeus/60_Tape_Specs/2026-09-02-intent-md-contrat-entree.md §4"
metadata:
  hermes:
    tags: [intent, grill-me, spec, ruban-phi]
    category: self-evolution
---

# L'agent Intervieweur (protocole "Grill Me")

Rôle tenu par Yaz (Spec, ruban φ). Ce protocole transforme la déclaration brute
d'un Originator (Amadou, ou un agent en maintenance autonome) en `intent.md`
human-readable et machine-actionable, déposé dans `_INBOX/<couche>/`.

## Le contrat d'entrée

Une intent.md vit dans `_INBOX/`, suit le test du ruban (canon racine §3),
et devient une spec. Son format canonique :

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

Règle : une intent sans critère mesurable retourne à l'Originator. Le test du
ruban s'applique dès l'intent. `Statut: FROZEN` = Yaz peut produire la spec.

## Protocole Grill Me — 5 étapes

1. **Lire la déclaration brute** de l'Originator (message, note DLQ,
   transcription). Extraire : l'irritant, le résultat visé, les contraintes
   déjà exprimées.

2. **Griller** — poser 3 à 5 questions, et rien que sur les edge-cases. Chaque
   question porte sur ce qui n'est PAS déductible de la déclaration :
   - **Persistance** : que se passe-t-il après redémarrage / compaction / reboot ?
   - **Volume** : combien d'items, quelle cadence, quel seuil de saturation ?
   - **Vetos** : qui peut refuser, sur quel critère, et que se passe-t-il alors ?
   - **Coûts** : budget tokens, argent, temps — borne explicite.
   Zéro question d'évidence : si la réponse est déjà dans la déclaration ou le
   canon (AGENTS.md racine §3), la question est interdite. Un constructeur qui
   pose une question d'évidence = ruban incomplet = note refusée.

3. **Compiler** l'intent.md dans `_INBOX/<layer>/intent-<slug>-<date>.md`
   avec le format ci-dessus. Chaque critère du §4 est une **commande
   exécutable** dont la sortie est la preuve (même règle que les rubans :
   review.py exécute et exige la sortie).

4. **FROZEN** : demander au portier (Beth / rick_s1) de changer `Statut:
   DRAFT → FROZEN` si et seulement si les critères sont mesurables. Un
   FROZEN sur critères non mesurables est une fraude au test du ruban.

5. **Passer au cycle** : FROZEN → Yaz produit la spec OKF 0.2 dans
   `60_Tape_Specs/` → gate.py → claim → prédiction antérieure → build →
   evidence → review → done (uc.py uniquement).

## En maintenance autonome (la boucle fermée)

Donna qualifie un échec → rédige son propre intent.md de diagnostic
(famille d'échec + preuve) → dépose dans `_INBOX/S1_Rick/` → Rick tranche →
Yaz spec → cycle. Le protocole Grill Me s'applique à l'agent lui-même :
un agent en maintenance grile son propre diagnostic avant de déposer.

## Pièges

- **Critère non exécutable = intent refusée.** "L'utilisateur est content"
  n'est pas un critère. `python uc.py review --work N` en est un.
- **FROZEN sans mesurabilité = porte murée.** Un statut FROZEN apposé sur une
  intent vague n'est pas un ruban, c'est une dette d'obscurité.
- **Blast radius absent = interdit implicite absent.** Sans périmètre écrit,
  le constructeur décidera seul de ce qu'il touche — c'est un ruban incomplet.
- **Re-scopage ≠ abandon.** Un intent de RE-SCOPAGE remplace le périmètre
  d'un work existant par un périmètre mesurable ; il cite le work, la famille
  d'échec observée, et la preuve de l'échec (path + rc).
