---
type: Concept
title: Purpose et le pourquoi — relier chaque règle au piège qu'elle évite
description: Section 1 du prompt système appliquée au canon : derrière chaque interdit écrit doit vivre le paiement qui l'a rendu nécessaire, sans quoi la règle ne se généralise pas.
tags: [prompt-systeme, purpose, canon, methode]
generated: { by: minimax-m3, at: 2026-08-17T22:00:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T22:00:00Z }
sources:
  - id: indydevdan-extraction
    resource: 60_Implementation_Méthodologiques/_sources/indydevdan-prompt-systeme.md
    title: "IndyDevDan — extraction]
    last_modified: 2026-08-17
  - id: canon-poste
    resource: C:/Users/amado/CLAUDE.md
    title: "Canon du poste — racine du profil"
    last_modified: 2026-08-15
okf_version: "0.2"
---

# Le principe

La première section d'un prompt système pose la relation **et** la raison
d'être de cette relation. IndyDevDan : *« Toi et moi, on entretient une relation
claire, concise, actionnable, sans baratin. »* Puis : *pourquoi* — pour livrer
le meilleur résultat possible à l'équipe, à l'entreprise, aux clients.

Donner la raison, pas seulement la règle. Une règle sans sa raison ne se
généralise pas aux cas non prévus. Le modèle sait reproduire l'interdit
littéral, pas extrapoler à cinq situations voisines.

# L'écart mesuré

Ce poste applique **déjà** la grille, mais en deux temps et sans le dire.

| Côté canon | Forme prise |
|---|---|
| `C:/Users/amado/CLAUDE.md` | directives explicites + anecdotes de pièges payés |
| `C:/Users/amado/.claude/CLAUDE.md` | même structure, focus mémoire canonique |

Chaque interdit du canon est précédé ou suivi d'un paragraphe « **Piège N** »
qui raconte la situation qui l'a rendu nécessaire. C'est exactement la
section *Purpose* d'IndyDevDan, mais distribuée plutôt que concentrée, et
sans l'intituler.

L'écart n'est pas conceptuel — il est éditorial. Le pourquoi est là, mais
éparpillé : il faut lire tout le fichier pour reconstituer la relation, et un
lecteur pressé voit les interdits, pas la relation.

# Le geste

Trois consignes d'écriture, vérifiables au prochain passage de mise à jour :

1. **Chaque nouvelle règle ajoutée au canon doit ouvrir sur son piège Source.**
   Pas un renvoi « voir X », pas un numéro de commit — un paragraphe de deux ou
   trois lignes qui raconte le coût payé. Une règle sans histoire ne résiste
   pas à la première pression pour l'assouplir.
2. **Regrouper les *Pièges N* éparpillés en un sommaire en tête de chaque
   `CLAUDE.md`**, dans l'ordre où ils ont été payés. La table devient
   l'index de la relation — un agent qui lit le sommaire sait ce que le poste
   a déjà appris à ses dépens.
3. **Considérer la section *Purpose* comme un travail de mise en forme, pas un
   travail de contenu.** Le contenu est déjà là. La forme manque.

Vérifiable : ouvrir `C:/Users/amado/CLAUDE.md`, compter les règles qui
ouvrent sur un piège Source, et viser 100 %. Tant qu'une règle n'a pas sa
raison accolée, elle est en attente de paiement.

# Ce qui n'est pas dans ce concept

La section *Purpose* d'IndyDevDan contient aussi un énoncé de ton (« sans
baratin »). Notre canon n'a pas d'instruction de ton explicite — il l'obtient
par les négatifs des concepts voisins. Voir `patterns-positifs-negatifs.md`.
