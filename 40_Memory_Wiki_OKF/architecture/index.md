---
type: Bundle index
title: architecture — décisions de structure et leurs raisons
description: Sous-bundle en attente de sa première page. Il portera les décisions d'architecture, l'option retenue et celle qui a été écartée.
tags: [okf, architecture, index]
generated: { by: claude-opus-5, at: 2026-08-17T15:10:00Z }
okf_version: "0.2"
---

Ce sous-bundle porte les **décisions de structure** : ce qui a été choisi, et
surtout ce qui a été écarté.

Une décision consignée sans son option rejetée ne se relit pas. Six mois plus
tard, personne ne sait si l'alternative avait été examinée ou simplement pas
vue — et la question se rouvre à zéro.

# Files

- [CEO-BENCH et SpecLoop — ce que les sources disent vraiment](ceobench-specloop-ce-que-disent-les-sources.md) - Une affirmation sur onze du briefing D.E.A.L est sourcée. CEO-BENCH est un banc d'essai, pas une méthode ; son résultat principal est un avertissement contre l'autonomie lights-out — la plupart des agents font faillite, un script à base de règles bat la majorité des LLM, et envelopper un modèle dans un harnais l'a rendu moins performant. La règle de bascule en mode préservation reprend la mesure avec le signe inverse.
- [La couche B n'existe plus dans le runtime Multica](couche-b-absente-du-runtime.md) - L'API vivante rend 57 agents et zéro B1/B2/B3, contre 26 dans l'export du 2 août : le Conseil B2 n'est pas dormant, il a disparu. L'ontologie (5 TTL, ~2 520 triplets) et les 258 concepts des 8 domaines sont intacts. Deux défauts du graphe : Product/Flash sans triplet `instantiates`, et le nœud Avengers dédoublé. Contient l'anti-piège John Jones / Martian Manhunter, qui produit un faux négatif.
- [Cordis est le runtime de DeepSeek Harness](cordis-runtime-et-couches-de-protocoles.md) - `dsh` est bâti sur Cordis. Les protocoles d'agents (MCP, A2A, AG-UI, ACP, UCP) sont des couches distinctes, pas des rivaux. LiteRT n'est pas au même étage qu'un adaptateur : il va dans les backends de modèle, pas dans la couche d'exposition.
- [Bloquer une app par son registre, pas par ses boutons d'entrée](bloquer-une-app-par-le-registre.md) - Remplacer le composant dans le manifeste ferme toutes les portes d'un coup, retire la sidebar sans traitement séparé, et sort le code du bundle livré. Contient l'anti-piège : quand l'interaction scriptée résiste, mesurer l'artefact plutôt que le geste.
