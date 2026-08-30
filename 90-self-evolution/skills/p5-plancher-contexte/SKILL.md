---
name: p5-plancher-contexte
description: Mesure et réduit ce qui est chargé avant le premier mot. Répond à P5 — ~96k tokens d'outillage sur une fenêtre de 200k, qui a fait échouer un délégué avant qu'il lise son brief.
version: 1.0.0
platforms: [windows, linux, macos]
author: amadou-kone
metadata:
  hermes:
    tags: [contexte, quota, mcp, delegation, plancher]
    category: self-evolution
    requires_tools: [terminal]
    ancrage:
      problematiques: [P5]
      besoins: [B4]
      mesure: "195 outils MCP = 60,2k tokens ; outils système 20,9k ; plancher ~96k sur 200k"
      source: "50_Distillation/RAPPORT_INTENTIONS_V3.md §3 P5"
---

# Quand l'utiliser

- **Avant toute délégation** — c'est là que le plancher tue, pas seulement
  qu'il coûte.
- Quand un délégué rend `Prompt is too long` sans avoir lu son brief.
- Avant d'ajouter quoi que ce soit à un fichier chargé au démarrage.

# Pourquoi elle existe

Mesure sur une fenêtre de 200k :

| Poste | Tokens | Part |
|---|---:|---:|
| Outils MCP (195) | 60,2k | 30,1 % |
| Outils système | 20,9k | 10,4 % |
| Prompt système | 6k | 3,0 % |
| Fichiers de mémoire | 7,5k | 3,8 % |
| Skills | 2k | 1,0 % |
| **Plancher total** | **~96k** | **~48 %** |

**Ce n'est pas qu'une ligne de facture : c'est ce qui rend le travail
impossible.** Le 2026-08-30, un délégué a rendu `Prompt is too long` **deux
fois** — d'abord sur un corpus de 409 Ko, puis sur des tranches de 42 Ko. La
taille du corpus n'y était pour rien : le plancher ne laissait pas la place.

# Procédure

1. **Déléguer avec les deux drapeaux. Ils ne sont pas optionnels.**

   ```bash
   "C:/Users/amado/.claude/custom-models/claude-glm.cmd" \
     --dangerously-skip-permissions \
     --strict-mcp-config --mcp-config '{"mcpServers":{}}' \
     -p "<brief court qui POINTE vers un fichier>"
   ```

2. **Le brief pointe, il ne contient pas.** Un corpus dans l'argument `-p`
   échoue ; découpé en tranches de ~40 Ko lues depuis le disque, il passe.

3. **Mesurer avant d'ajouter.**

   ```bash
   python 90-self-evolution/skills/p5-plancher-contexte/scripts/plancher.py
   ```

4. **Distinguer démarrage et à la demande.** Le coût de démarrage n'est pas la
   somme de tout ce qui est atteignable : ~5 819 tokens contre ~20 724
   annoncés avant correction. Un total gonflé pousse à couper ce qu'il faut
   garder. (P4)

# Pièges

- **Sans les drapeaux MCP, le délégué ne lit même pas son brief.** L'erreur
  ressemble à un problème de taille de corpus. Elle n'en est pas un.

- **Chaque ligne ajoutée à un fichier de démarrage est payée à chaque
  session, pour toujours.** `CLAUDE.md` est passé de 162 à 320 lignes :
  ~2 000 tokens × chaque session à venir.

- **Un délégué n'est pas Opus.** Le brief doit lui dire ce qu'il est, ce qu'il
  écrit, où il s'arrête. Le 2026-08-30, `claude-glm` a lu le `CLAUDE.md`
  racine, s'est cru Opus, et a repris la tâche de la session parente pendant
  que le quota Anthropic était épuisé.

- **Une seule boucle à la fois.** `pkill` ne prend pas toujours du premier
  coup ; vérifier par `pgrep -fc`. Deux boucles concurrentes ont brûlé quatre
  tranches en double.

# Ce que cette skill remplace

- **Les relances de délégation par `claude -p` nu.** Elles consommaient le
  quota Anthropic — exactement la ressource qu'on épargne — et sont retirées
  au profit de `claude-glm`.
- **Le diagnostic « le corpus est trop gros »**, remplacé par la mesure du
  plancher. Le 2026-08-30, ce faux diagnostic a coûté deux échecs consécutifs :
  ce n'était pas le corpus, c'était l'outillage.
- **L'outil `Workflow`** pour orchestrer : ses sous-agents héritent du modèle
  exporté et meurent. Retiré au profit de briefs sur disque.

# Vérification

```bash
python 90-self-evolution/skills/p5-plancher-contexte/scripts/plancher.py --auto-test
```

Le test **échoue si le coût de démarrage des fichiers dépasse 8 000 tokens**.
Ce n'est pas une limite technique : c'est le point au-delà duquel le mandat
coûte plus qu'il ne rapporte, et où il faut déplacer du contenu vers un
fichier lu à la demande.
