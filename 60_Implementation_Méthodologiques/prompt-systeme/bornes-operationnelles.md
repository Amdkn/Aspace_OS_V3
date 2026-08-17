---
type: Concept
title: Bornes opérationnelles — les interdits consolidés
description: Section 4 du prompt système appliquée au poste : transformer les interdits dispersés du canon en une liste unique, vérifiable, qui pose la différence entre « livré » et « fait ».
tags: [prompt-systeme, bornes, perimetre, interdits]
generated: { by: minimax-m3, at: 2026-08-17T22:15:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T22:15:00Z }
sources:
  - id: indydevdan-extraction
    resource: 60_Implementation_Méthodologiques/_sources/indydevdan-prompt-systeme.md
    title: "IndyDevDan — extraction"
    last_modified: 2026-08-17
  - id: canon-d6
    resource: C:/Users/amado/CLAUDE.md
    title: "Canon du poste — section §6 anti-piège claude -p"
    last_modified: 2026-08-15
okf_version: "0.2"
---

# Le principe

IndyDevDan : *« Le défaut visé : le modèle fait ce qu'on ne lui a pas
demandé. »* Les bornes opérationnelles sont **strictes** et **dures** —
elles fixent où s'arrête le travail, indépendamment de la qualité.

Les cinq bornes de la source :

1. livrer **uniquement** ce qui est demandé, au périmètre demandé ;
2. ne pas élargir en nettoyage, remaniement, documentation ou fonctionnalité
   adjacente ;
3. ne pas spéculer sur des besoins futurs ;
4. ne pas déclarer terminé sans preuve ;
5. ne pas ajouter de co-auteur à un message de commit.

# L'écart mesuré

Le canon du poste applique déjà la borne 1 — chaque brief nomme un
**périmètre exclusif en écriture** et plusieurs agents travaillant en
parallèle le respectent. La borne 4 est partiellement tenue : « Un agent
délégué n'est jamais cru sur parole : son résultat se vérifie », mais la
preuve exigée varie d'un brief à l'autre.

Les bornes 2, 3 et 5 sont **partiellement couvertes** mais dispersées. La
borne 2 ressort en creux dans plusieurs pièges (un agent qui nettoie un
fichier hors périmètre, ou qui ajoute un commit « bonus ») ; la borne 3
apparaît dans le piège n°4 du canon (« un prompt au format OKF ouvre sur un
frontmatter YAML » — l'agent a bâti une abstraction pour un besoin futur) ;
la borne 5 est respectée par défaut, sans être nommée.

Le déficit est donc **éditorial** : les interdits existent mais
dispersés. Aucun agent qui découvre le canon ne reconstitue la liste des
bornes en lisant les anecdotes.

# Les bornes consolidées pour ce poste

Reporter dans une section unique **« Bornes opérationnelles »** du canon, à
placer juste après les Patterns (voir `patterns-positifs-negatifs.md`) :

1. **Périmètre strict.** Tu écris **uniquement** dans les fichiers nommés
   par le brief. Un fichier hors liste est intouchable, même pour « corriger
   une typo ».
2. **Pas d'extension latérale.** Pas de refactor, pas de formatage, pas de
   réorganisation, pas de documentation ajoutée, pas de test écrit à
   proximité. Pas de nettoyage « puisque j'y suis ».
3. **Pas de design pour un besoin futur.** Une abstraction à trois
   utilisateurs potentiels est une abstraction à zéro utilisateur.
4. **Livré ≠ fait.** Un changement est livré quand la commande d'examen
   (voir `examen-prealable.md`) renvoie zéro erreur. Pas avant.
5. **Pas de co-auteur ajouté au commit.** Le commit reflète l'auteur
   humain. Les `Co-Authored-By: Claude` introduits en boilerplate sont
   interdits.
6. **Un secret n'apparaît jamais en clair.** Ni en valeur, ni en fragment.
   Le préfixe suffit (`sk-…`, `sbp_…`, `ck_…`). Sortie, brief, log, capture :
   partout.
7. **Une section qui n'a pas de source est une invention.** Si tu n'as pas
   lu, écris que tu n'as pas lu. Une couverture partielle déclarée vaut
   mieux qu'une couverture totale prétendue.

# Le geste

Ajouter la section **« Bornes opérationnelles »** au canon en sept points
numérotés (ci-dessus). Une note de bas de section rappelle que cette liste
est le négatif de la section *Patterns* et qu'elle prévaut sur toute
consigne orale plus permissive.

Vérifiable : prendre un brief récent, lire le travail de l'agent, et
cocher les sept bornes une à une. Une seule borne non tenue révèle un trou
dans la liste ou dans son application.

# Pourquoi cette section est plus efficace que les anecdotes

Les anecdotes de pièges sont **post-hoc** : elles racontent ce qui est
arrivé. Les bornes sont **prospectives** : elles disent ce qui ne doit pas
arriver. Les deux se complètent, mais sans la liste prospréctive, l'agent
qui ouvre un nouveau brief n'a que les archives des précédentes défaites
pour anticiper la suivante — ce qui suppose qu'il les ait lues.

La section bornes, elle, se lit en une fois, et oblige à l'application
immédiate.
