---
name: p2-mandat-persistant
description: Écrit le mandat d'autonomie dans un fichier lu au démarrage plutôt que de le réémettre à chaque session. Répond à P2 — la compaction garde les faits et perd l'autorisation, ce qui cause P1.
version: 1.0.0
platforms: [windows, linux, macos]
author: amadou-kone
metadata:
  hermes:
    tags: [mandat, compaction, autonomie, memoire-procedurale]
    category: self-evolution
    requires_tools: [terminal]
    ancrage:
      problematiques: [P2, P1]
      besoins: [B1]
      desirs: [D1]
      mesure: "GARDE-FOU 96×, LES SEPT CADENCES 69×, MODE FABLE 60× — réécrits parce qu'ils ne tiennent pas"
      source: "50_Distillation/RAPPORT_INTENTIONS_V3.md §2 B1"
---

# Quand l'utiliser

- Quand un brief d'autonomie (`GARDE-FOU`, `MODE FABLE`, `LES SEPT CADENCES`)
  est sur le point d'être réécrit **pour la énième fois**.
- Après une compaction, quand l'agent redevient prudent et redemande une
  autorisation déjà donnée.
- Quand `p1-anti-rejeu` signale un brief d'autonomie à ≥ 3 occurrences.

# Pourquoi elle existe

C'est le besoin **le plus cher du corpus**, et il est mesuré :

| Brief | Réécrit |
|---|---:|
| `GARDE-FOU — vague de revue` | **96×** |
| `LES SEPT CADENCES` | **69×** |
| `MODE FABLE` | **60×** |
| `tu exécutes cette critique toi-même` | **45×** |

Ces briefs disent tous la même chose : *exécute toi-même, n'invoque personne,
voici la table de vérité*. **Ils sont réécrits parce qu'ils ne tiennent pas.**

La cause est mécanique : **la compaction conserve les faits et perd
l'autorisation.** Le résumé retient « l'utilisateur veut X » et laisse tomber
« l'utilisateur a autorisé à agir sans redemander ». L'agent repart prudent,
pose une question dont il connaît la réponse, et le propriétaire réécrit le
mandat. C'est P2, et **c'est ce qui cause P1**.

C'est aussi le *Continual Harness* de Prime Agent : ce qui doit survivre à
l'invocation ne vit pas dans le contexte, il vit **dans un fichier que le
démarrage relit**.

# Procédure

1. **Localiser le mandat courant.**

   ```bash
   python 90-self-evolution/skills/p2-mandat-persistant/scripts/mandat.py --etat
   ```

   Rend ce qui est chargé à chaque session, avec son coût en tokens.

2. **Écrire l'autorisation là où elle est relue**, pas dans le fil. Le fichier
   racine `C:/Users/amado/CLAUDE.md` porte déjà les huit attendus ; une
   autorisation nouvelle s'y ajoute sous forme d'**acte**, jamais d'interdit.

   > Un fichier qui n'énonce que des interdits produit un exécutant qui
   > s'arrête. Le mandat se formule en « fais », pas en « ne fais pas ».

3. **Vérifier que ça tient.**

   ```bash
   python 90-self-evolution/skills/p2-mandat-persistant/scripts/mandat.py --verifier
   ```

   Le script relit les fichiers de démarrage et rend la liste des
   autorisations détectées. Si le mandat n'est pas dans la sortie, **il ne
   survivra pas à la prochaine compaction**, quoi qu'on ait écrit dans le fil.

4. **Nommer ce qui est retiré.** (B4) Un mandat écrit remplace un brief
   réémis : dire lequel, et le supprimer.

# Pièges

- **Écrire le mandat dans le fil de conversation ne compte pas.** C'est
  précisément le défaut : une consigne laissée dans un message meurt à la
  compaction suivante. Seul le disque persiste.

- **Un mandat trop long ne tient pas mieux.** Il coûte à chaque session (P5).
  Le fichier racine fait ~1 840 tokens ; chaque ligne ajoutée est payée à
  chaque démarrage, pour toujours.

- **Un mandat n'est pas une permission de tout faire.** Les portes
  irréversibles restent : CA racine, dépôt divergent, virement, suppression de
  données, et le passage `confiance: machine → humain`. Elles existent parce
  que l'acte est irréversible, jamais parce que la tâche est inconfortable.

- **Ne pas confondre mandat et cadence.** `LES SEPT CADENCES` décrit un
  ordonnanceur ; `GARDE-FOU` décrit une autorisation. Le second va dans le
  mandat, le premier dans une skill dédiée.

# Vérification

```bash
python 90-self-evolution/skills/p2-mandat-persistant/scripts/mandat.py --verifier
```

Sortie attendue : la liste des fichiers lus au démarrage, leur coût réel en
tokens, et les autorisations trouvées. **Le test échoue si un fichier de
démarrage est absent** — un mandat qui pointe vers un fichier disparu est pire
qu'aucun mandat, il donne l'illusion d'une garantie.
