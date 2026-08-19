---
type: Fact Check
title: CEO-Bench — ce que le brief affirmait vs ce que la source publie
description: Vérification ligne par ligne du tableau « Modèle | Résultat | Coût » du brief BRIEF_frameworks.md contre la home ceobench.com et les trajectoires publiées.
tags: [ceo-bench, fact-check, brief, source-verification]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: minimax-m3, at: 2026-08-19T00:00:00Z }
sources:
  - id: brief-frameworks
    resource: "60_Implementation_Méthodologiques/_loop/BRIEF_frameworks.md"
    title: "Brief source — tableau Modèles CEO-Bench (lignes 23-28)"
    last_modified: 2026-08-19
  - id: ceobench-home
    resource: "https://ceobench.com"
    title: "ceobench.com — trajectoires publiées et stats agrégées"
    last_modified: 2026-08-19
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Toutes les lignes
> comparées ici ont été relues dans le brief et la home.

# Le tableau du brief (citation)

> | Modèle | Résultat | Coût |
> |---|---|---|
> | Claude Opus 4.8 | survit 500 j, 1 511 actions | **2,40 M$** |
> | Kimi K3 | survit 500 j, 2 213 actions | **22,15 M$** |
> | Claude Fable 5 | survit 500 j, 818 actions, 6 129 subs | 12,67 M$ |
> | GPT-5.6 Sol | **faillite à 190 j** | — |

# Vérification

## Claude Opus 4.8 — survit 500j, 1 511 actions, $2.40M

**Vérifié**. Run `e2cbe2de`, 504j, 1511 actions, 0 subs, $2.40M, statut
survécu. Le brief donne 500j (arrondi). Le nombre d'actions et le cash
sont **verbatim** depuis la home ceobench.com.

⚠️ **Mais** : c'est le **meilleur de 3 runs**. Les 3 runs agrégés :
- e2cbe2de : 504j, 1511 actions, 0 subs, $2.40M ✅
- aad782be : 504j, 714 actions, 0 subs, $605.6K ✅
- 3f8f3efd : **134j, 374 actions, 73 605 subs, BANKRUPTED** ❌

**1/3 faillite, durée moyenne 378,0 ± 172,5 j.** Le brief présente le
meilleur run comme LE résultat du modèle. **C'est inexact** : c'est un
résultat sur trois.

## Kimi K3 — survit 500j, 2 213 actions, 22,15 M$

**Cash vérifié** : best cash $22 148 357 publié sur la home.

**Mais** :
- "2 213 actions" **non vérifié** dans la home. Le brief ne cite pas de
  source pour ce chiffre ; il n'apparaît pas dans le tableau agrégé
  public. **Suspect** — soit chiffre mémoire, soit issu d'une trajectoire
  précise non citée.
- "survit 500j" : c'est la **meilleure des 3 trajectoires**. Kimi K3 a
  **1/3 faillite**. Durée moyenne 386,0 ± 161,2 j.
- Kimi K3 finit avec 14,81 tours/semaine.

Le brief confond best-run et comportement général. **Factuellement
imprécis**.

## Claude Fable 5 — survit 500j, 818 actions, 6 129 subs, 12,67 M$

**Vérifié** sur le run `2c0aeba9` : 504j, 818 actions, 6 129 subs, $12.67M,
survécu. Le best cash agrégé est **$12.63M** (cohérent à $40K près,
probablement différence cash de départ vs cash final).

⚠️ Idem : c'est le **meilleur de 3 runs**. Les 3 runs agrégés :
- 2c0aeba9 : 504j, 818 actions, 6 129 subs, $12.67M ✅
- 3def3647 : 504j, 787 actions, 0 subs, $277.4K ✅
- 4f03ddc9 : **385j, 421 actions, 0 subs, BANKRUPTED** ❌

**1/3 faillite, durée moyenne 461,7 ± 54,2 j**, 9,86 tours/semaine. Fable
5 est le plus stable (écart-type le plus bas sur la durée).

## GPT-5.6 Sol — faillite à 190j

**Vérifié pour ce run précis** : `63f6b1fb`, 190j, 1372 actions,
274 996 subs, BANKRUPTED.

⚠️ **Mais** : 2/3 faillite sur ce modèle, **et** un run `d1834c32`
survit à 504j avec $11.31M (3 115 actions, 0 subs). Le brief présente
GPT-5.6 Sol comme « faillie à 190j » — c'est **une trajectoire**, pas
le modèle. Le modèle a aussi une trajectoire de succès.

# Conclusion factuelle

1. **Le brief est partiellement vérifié** : les chiffres sont réels pour
   la trajectoire citée. La formulation laisse entendre un résultat
   typique, alors que chaque modèle est joué 3 fois et la métrique utile
   est l'**agrégat** (best cash + taux de faillite + durée moyenne).
2. **"2 213 actions" pour Kimi K3** n'est pas vérifiable sur la source
   publique. **Marqué comme suspect** — soit mémoire, soit trajectoire
   non indexée.
3. **L'insight central tient** : un modèle peut survivre en dépensant
   ~10× plus qu'un autre. Kimi K3 finit à $22M, Opus à $2.4M — c'est un
   ratio 10× pour la même survie.
4. **Le banc mesure bien l'efficacité de décision** : cash final / cash
   initial / durée / actions = proxy du coût de survie.

# Conséquence pour la lecture du brief

À chaque fois qu'il cite un chiffre CEO-Bench comme « verdict », le
lire comme **« sur 3 runs, ce modèle a fait au moins une fois ça »**,
pas comme **« ce modèle fait toujours ça »**. La métrique utile est
l'agrégat publié par la home, pas la trajectoire unique.

# Source canonique à citer

Pour toute décision Business OS qui s'appuierait sur CEO-Bench :
- Page agrégée : https://ceobench.com (homepage, stats par modèle)
- Trajectoire précise : https://ceobench.com/trajectory-viewer/run?run=<id>
- Code source : https://github.com/zlab-princeton/ceobench-src

Ne JAMAIS citer un chiffre CEO-Bench sans préciser le run_id ou sans
citer l'agrégat 3-runs.