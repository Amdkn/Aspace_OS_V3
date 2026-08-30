---
name: p1-anti-rejeu
description: Vérifie qu'un brief n'a pas déjà tourné avant de l'exécuter, et propose de le convertir en skill à partir de la 3e occurrence. Répond à P1 — 978 des 2 307 sessions rejouent une intention déjà formulée.
version: 1.0.0
platforms: [windows, linux, macos]
author: amadou-kone
metadata:
  hermes:
    tags: [rejeu, memoire-procedurale, deal, quota]
    category: self-evolution
    requires_tools: [terminal]
    ancrage:
      problematiques: [P1]
      besoins: [B4]
      desirs: [D4]
      mesure: "unicité 80,5 % en juillet → 32,3 % en août ; 978/2307 sessions rejouées"
      source: "50_Distillation/RAPPORT_INTENTIONS_V3.md §0"
---

# Quand l'utiliser

**Avant d'exécuter tout brief de plus de 40 mots.** Systématiquement, pas
seulement quand un doute existe : un système qui ne sait pas qu'il se répète ne
peut pas s'arrêter, et le doute n'arrive jamais au bon moment.

Déclencheurs : un brief collé dans le prompt, une demande qui ressemble à une
consigne déjà vue, toute reprise après compaction.

# Pourquoi elle existe

Mesure du 2026-08-30 sur 2 307 premiers messages de session :

| Mois | Sessions | Uniques | % unique |
|---|---:|---:|---:|
| juillet | 1 123 | 904 | 80,5 % |
| **août** | **879** | **284** | **32,3 %** |

**978 sessions sur 2 307 (42,4 %) portent une intention déjà vue.** Les briefs
les plus rejoués : `GARDE-FOU` 96×, `LES SEPT CADENCES` 69×, `MODE FABLE` 60×,
`multica chat assistant` 132×.

Le coût n'est pas le rejeu lui-même : c'est que **chaque rejeu redémarre à
zéro** un travail dont le résultat existe déjà sur le disque.

# Procédure

1. **Chercher avant d'exécuter.**

   ```bash
   python 90-self-evolution/skills/p1-anti-rejeu/scripts/deja_vu.py "<les 200 premiers caractères du brief>"
   ```

   Le script rend les sessions dont l'intention normalisée coïncide, avec leur
   date et le nombre d'occurrences.

2. **Si le compte est ≥ 1 :** dire au propriétaire *ce brief a déjà tourné N
   fois, la dernière le <date>*, et **montrer ce qui en est sorti** avant de
   proposer de le relancer. Un rejeu conscient est une décision ; un rejeu
   ignoré est une panne.

3. **Si le compte est ≥ 3 :** appliquer la règle D.E.A.L. — *3 occurrences
   automatisent*. Proposer la conversion en skill, et **nommer ce qu'elle
   remplace** (B4 : aucune addition sans soustraction).

4. **Si le compte est ≥ 5 :** la règle D.E.A.L. dit *5 occurrences
   remboursent*. La conversion n'est plus une proposition, c'est une dette.

# Pièges

- **Éliminer avant d'automatiser.** D.E.A.L. commence par E. Automatiser un
  brief rejoué 96 fois sans demander *pourquoi il ne tient pas* fige le
  gaspillage au lieu de le retirer. Pour `GARDE-FOU`, la cause est **P2** — le
  mandat ne survit pas à la compaction — et c'est là qu'il faut corriger.

- **Le seuil de similarité est un choix, pas une vérité.** Le script compare
  les 120 premiers caractères normalisés. Un brief reformulé compte comme
  neuf. Le taux réel de rejeu est donc **au moins** 42,4 %, jamais moins.

- **Ne jamais exécuter en silence après avoir détecté un rejeu.** Le but est
  que le propriétaire voie la répétition, pas que la skill décide à sa place.

# Vérification

```bash
python 90-self-evolution/skills/p1-anti-rejeu/scripts/deja_vu.py --auto-test
```

Le test rejoue la mesure du rapport sur le substrat réel et **échoue si le
taux de rejeu global s'écarte de 42,4 % de plus de 2 points**. Un écart
signifie soit que le corpus a bougé, soit que le script a cessé de mesurer ce
qu'il prétend — et dans ce cas c'est l'instrument qu'on répare (voir
[`p4-instrument-honnete`](../p4-instrument-honnete/SKILL.md)), jamais le chiffre
qu'on ajuste.
