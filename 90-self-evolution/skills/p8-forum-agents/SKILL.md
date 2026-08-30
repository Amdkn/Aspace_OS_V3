---
name: p8-forum-agents
description: Fait collaborer plusieurs agents par un espace partagé asynchrone plutôt que par des chaînes séquentielles, avec réservation de tâche pour éliminer les doublons. Répond à P1 et au plafond de concurrence mesuré du poste.
version: 1.0.0
platforms: [windows, linux, macos]
author: amadou-kone
metadata:
  hermes:
    tags: [forum, blackboard, stigmergie, multi-agents, asynchrone]
    category: self-evolution
    requires_tools: [terminal]
    ancrage:
      problematiques: [P1, P5, P6]
      besoins: [B2, B4]
      desirs: [D1, D4]
      mesure: "103 node.exe → STATUS_COMMITMENT_LIMIT le 12 août ; 4 tranches brûlées en double le 30 août ; MAX_CADENCES_VIVES=2"
      source: "50_Distillation/RAPPORT_INTENTIONS_V3.md §1 I1"
---

# Quand l'utiliser

**Dès qu'une tâche demande plus d'un agent.** Pas quand la coordination
devient difficile — avant, parce que c'est le choix d'architecture qui décide
si elle le devient.

# Pourquoi elle existe

Lors de tests OpenAI, **plus de 1 200 agents ont spontanément utilisé un forum
interne** pour échanger plus de 70 000 messages, se répartir les tâches et
coordonner une stratégie. Ils n'ont choisi ni la chaîne séquentielle ni le
point-à-point : ils ont choisi **l'espace partagé asynchrone**.

Le poste a payé l'absence de ce modèle, deux fois mesurées :

| Date | Fait |
|---|---|
| 12 août | 103 `node.exe` simultanés → `STATUS_COMMITMENT_LIMIT` |
| 30 août | Deux boucles concurrentes ont brûlé **4 tranches en double** |

Le second cas est exactement ce que `forum_claim_task` empêche : deux
exécutants ont pris le même travail parce que rien ne permettait de dire
« celui-là est pris ».

**Trois propriétés qu'aucune chaîne séquentielle ne donne :**

1. **Découplage temporel.** Une cascade d'appels synchrones meurt au premier
   *timeout*. Un agent qui poste dans un fil peut se mettre en veille ; un
   autre reprend quand il a les ressources.
2. **Stigmergie.** Les agents communiquent par dépôt de traces — fichiers,
   synthèses, journaux d'erreur. Chacun lit l'historique du fil **sans
   recalculer ni redemander le contexte**, ce qui attaque directement P5.
3. **Collaboration opportuniste.** Un analyste diagnostique, un exécutant
   propose un correctif, un auditeur valide — dans le même fil, sans
   séquence imposée.

# Procédure

1. **Lire avant d'agir.**

   ```bash
   python 90-self-evolution/skills/p8-forum-agents/scripts/forum.py fils
   python .../forum.py lire <fil>
   ```

2. **Réserver, sinon deux agents font le même travail.**

   ```bash
   python .../forum.py prendre <fil> --agent <nom>
   ```

   La réservation **échoue** si le fil est déjà pris. C'est la garde qui
   manquait le 30 août.

3. **Poster une contribution, avec son artefact.**

   ```bash
   python .../forum.py poster <fil> --agent <nom> --texte "..." --artefact <chemin>
   ```

   **Règle du résumé contextuel :** tout message se termine par une ligne
   d'état et l'action attendue. Sans elle, le fil devient un journal que
   personne ne relit.

4. **Clore et archiver.** Un fil conclu est compilé en synthèse puis fermé.
   Un forum qui n'archive jamais redevient un historique qui grossit — la
   panne que [`p7-memoire-travail`](../p7-memoire-travail/SKILL.md) corrige.

5. **Taguer ce qui engage.** Toute décision touchant de l'argent ou une
   structure porte `#humain` et attend le propriétaire.

# Ce que cette skill remplace

- **Les chaînes séquentielles A → B → C**, retirées : elles échouent en entier
  au premier *timeout* d'un maillon.
- **Le passage de contexte par recopie** d'un agent à l'autre — remplacé par
  la lecture du fil, ce qui économise le contexte au lieu de le dupliquer.
- **Le lancement en parallèle sans réservation**, qui a produit les 4 tranches
  en double et les 103 processus.

# Pièges

- **Le forum ne lève pas le plafond de concurrence.** `MAX_CADENCES_VIVES=2`
  reste. Il évite le travail *dupliqué*, pas la surcharge : deux agents qui ne
  se marchent pas dessus consomment quand même deux fois.

- **Une réservation sans expiration bloque le fil pour toujours** si l'agent
  meurt. Le script pose une péremption ; sans elle, un crash gèlerait le
  travail des autres.

- **Un fil sans résumé contextuel coûte plus qu'il ne rapporte.** Le gain
  vient de ce qu'on lit l'état sans relire tout le fil.

- **Ce forum est local, sur fichiers.** Pas de Supabase, pas de Zulip, pas de
  Matrix : ils ne sont pas câblés ici, et une implémentation qui suppose une
  infrastructure absente ne tourne pas. Le schéma `channels / threads /
  messages / artifacts` est repris tel quel et migrable.

# Vérification

```bash
python 90-self-evolution/skills/p8-forum-agents/scripts/forum.py --auto-test
```

Le test vérifie qu'une **double réservation est refusée** — la garde qui
manquait le 30 août — que les artefacts survivent à la relecture, et qu'un
message sans résumé contextuel est signalé.
