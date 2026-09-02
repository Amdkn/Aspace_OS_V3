# Workflow Inbox - Mariner (Capture)

Workflow applique a `inbox.md` de ce dossier, conforme a la matrice canon
5 stages x 5 A3 twins de `20_Life_OS/25_GTD_Cerritos/README.md`
(Mariner=Capture, Boimler=Clarify, Rutherford=Organize, Tendi=Review,
Freeman=Engage) et a `A3_Mariner_Capture_Spec.md`.

## 1. Capture (Mariner)

Ajouter une ligne dans `inbox.md` :

```
- [ ] [date] <raw> | src: <chemin> | next: A3:Boimler
```

Une ligne = un raw input. Chaque item porte une source citee (`src:`) ;
sans chemin reel, l'item est marque `hypothesis` et refuse.

## 2. Clarify (Boimler)

Assigner un bucket PARA + un tag `@next`/`@waiting`/`@someday`/`@archive`,
cocher l'item `- [x]` et le preparer au deplacement. Boimler ne capture pas :
il tranche actionable / non actionable.

## 3. Organize (Rutherford)

L'item clarifie part dans `24_PARA_Enterprise` (bucket) ou `23_12WY_SNW`
(rock). Jamais en vrac dans l'inbox : l'inbox ne conserve que l'ouvert.

## 4. Review (Tendi)

Vidange hebdomadaire de l'inbox. Inbox vide = vert. Un item coche mais
non deplace est une anomalie de review.

## 5. Engage (Freeman)

La next action est dispatchee vers A1 Morty (mise en file).

## 6. Escalades

- **Beth** : overload ou veto A1 (le "Retour au Vert de Beth" seul debloque).
- **Enterprise** (PARA) : item > 1 session ou > 1 semaine (projet).
- **SNW** (12WY) : item rock.

## Regles de capture (rappel Mariner)

- Pas de secret dans l'inbox.
- 1 ligne = 1 raw input, source citee sinon `hypothesis`.
