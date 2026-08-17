---
type: Concept
title: Points de référence — codes courts partagés par tout le bundle
description: Section 3 du prompt système : assigner des codes D1…Dn, R1…Rn, F1…Fn aux éléments énumérés d'une conversation longue, pour fabriquer un langage commun en une ligne de prompt système.
tags: [prompt-systeme, reference, codes, conversation]
generated: { by: minimax-m3, at: 2026-08-17T22:10:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T22:10:00Z }
sources:
  - id: indydevdan-extraction
    resource: 60_Implementation_Méthodologiques/_sources/indydevdan-prompt-systeme.md
    title: "IndyDevDan — extraction"
    last_modified: 2026-08-17
  - id: canon-d4
    resource: C:/Users/amado/CLAUDE.md
    title: "Canon du poste — section §6"
    last_modified: 2026-08-15
okf_version: "0.2"
---

# Le principe

IndyDevDan : *« Assigner des codes courts aux éléments énumérés : `D1…Dn`
pour les décisions, `R1…Rn` pour les risques, `F1…Fn` pour les constats. Les
conserver dans toute la conversation ; ne pas en créer pour une réponse
courte. »*

L'effet est immédiat : on dit « parle-moi de R6 » et l'agent sait de quoi
il s'agit. **On fabrique un langage commun en une ligne de prompt système**,
et l'agent cesse de se répéter pour se faire comprendre.

# L'écart mesuré

Le canon contient déjà un embryon de cette convention, sous une autre forme.
La section §6 du canon (`C:/Users/amado/CLAUDE.md`) utilise des codes
**D4** (un identifiant de section) sans définir ce que la lettre désigne.
L'usage réel est : *« D4 append-only 2026-08-15 »* — ce n'est pas un code
par élément, c'est un nom de version.

L'écart est double :

1. **L convention de codes par élément n'existe pas.** Une conversation
   longue doit aujourd'hui répéter le nom complet de chaque piège, chaque
   décision, chaque constat. Au bout de vingt tours, l'agent fatigue et
   paraphrase — sans le code, on ne peut pas savoir de quoi il parle.
2. **Le canon ne demande pas à l'agent de tenir une liste.** Sans
   l'obligation explicite, un agent qui démarre une session longue peut
   réinventer la convention ou s'en passer.

# Le geste à poser

Une convention de codes courts, à déclarer une fois dans le canon :

| Préfixe | Catégorie | Exemple |
|---|---|---|
| `D` | Décision tranchée | `D3` = « les secrets restent en clair dans `config.yaml` sur machine de dev » |
| `R` | Risque identifié | `R6` = « un agent réécrit un autre en mesurant les éditions en vol » |
| `F` | Fait mesuré | `F1` = « 47 jonctions NTFS recensées dans la KB » |

Règles d'usage :

- **L'agent tient la liste lui-même** dans la première réponse longue d'une
  session. Format tabulaire, une ligne par code, conservé dans la suite.
- **Pas de code pour une réponse courte.** Convention activée seulement
  quand la conversation compte au moins trois éléments énumérés.
- **Codes stables** : un `D3` ne change pas de signification en cours de
  session. Si la décision est révisée, l'ancienne reste en liste barrée et
  la nouvelle prend un nouveau numéro.
- **Référence réciproque** : citer le code (« R6 ») plutôt que le nom long
  (« le risque que deux agents se réécrivent »). C'est l'usage qui rend
  l'outil rentable.

# Vérification

Au lancement de toute session longue, demander : *« liste tes D et R actifs »*.
Si l'agent ne tient rien, ou paraphrase, la convention n'est pas en place
dans son contexte.

Vérifiable a posteriori : ouvrir une session longue récente, compter les
tours intermédiaires où un piège est re-nommé en clair. Viser zéro au-delà
du premier énoncé.

# Risque à surveiller

Un code trop nombreux devient une taxonomie à entretenir. La règle
*« pas pour une réponse courte »* est ce qui protège la convention de
l'obésité. Résister à la tentation de coder tout ce qui est dit — seuls
les éléments **référencés plus d'une fois** méritent un code.
