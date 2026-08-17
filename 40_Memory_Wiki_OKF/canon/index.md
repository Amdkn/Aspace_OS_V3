---
type: Bundle index
title: canon — sauvegarde des fichiers d'instructions hors dépôt
description: Copies versionnées des deux CLAUDE.md qui pilotent le comportement de l'agent et qui vivent hors de tout dépôt git. Ce sont des instantanés, pas la source.
tags: [okf, canon, sauvegarde, claude-md]
generated: { by: claude-opus-5, at: 2026-08-17T16:05:00Z }
verified:
  - { by: human:amdkn, at: 2026-08-17T16:00:00Z }
sources:
  - id: source-home
    resource: "C:\\Users\\amado\\.claude\\CLAUDE.md — 145 lignes au moment de la copie"
    title: Canon global de l'utilisateur
    last_modified: 2026-08-17
  - id: source-profil
    resource: "C:\\Users\\amado\\CLAUDE.md — 472 lignes au moment de la copie"
    title: Canon du profil racine
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Pourquoi ce dossier existe

Deux fichiers pilotent le comportement de l'agent à chaque session. Aucun des
deux n'était sauvegardé nulle part :

| Original | Lignes | Pourquoi il n'était pas suivi |
|---|---|---|
| `C:\Users\amado\.claude\CLAUDE.md` | 145 | `~/.claude/` n'est pas un dépôt |
| `C:\Users\amado\CLAUDE.md` | 472 | git désactivé à la racine du profil depuis le 2026-08-02 |

Le second contient l'essentiel du savoir opérationnel du poste : hiérarchie de
délégation, cinq pièges d'invocation déjà payés, doctrine de vérification par
capture, règles de parallélisme entre agents. Une réinstallation de Windows
l'effaçait sans trace.

# Ce sont des instantanés, pas la source

**La source reste l'original.** Ces copies sont datées et ne se mettent pas à
jour toutes seules.

Le risque réel de ce dossier n'est pas de perdre les fichiers — c'est de croire
qu'ils sont à jour alors qu'ils ont divergé. D'où la règle inscrite en tête des
deux originaux : **toute édition d'un canon se recopie ici dans le même
commit.** Un instantané muet qui date de six mois est pire qu'une absence de
sauvegarde, parce qu'il inspire confiance.

Pour rafraîchir les deux copies :

```bash
cp "C:/Users/amado/.claude/CLAUDE.md" "C:/Users/amado/ASpace_OS_V3/40_Memory_Wiki_OKF/canon/CANON-home-claude.md" && cp "C:/Users/amado/CLAUDE.md" "C:/Users/amado/ASpace_OS_V3/40_Memory_Wiki_OKF/canon/CANON-profil-racine.md"
```

# Pourquoi les noms changent

Les copies ne s'appellent pas `CLAUDE.md`. Un fichier portant ce nom dans un
dépôt est **chargé automatiquement comme instruction active** par Claude Code.
Sauvegarder le canon sous son nom d'origine l'aurait donc mis en concurrence
avec lui-même : deux exemplaires chargés, dont un périmé, sans que rien ne le
signale.

# Ce qui n'est PAS sauvegardé ici, et ne le sera pas

`~/.claude/settings.json` contient des valeurs de clés en clair —
`ANTHROPIC_API_KEY`, `COMPOSIO_CONSUMER_KEY`. Il ne rentre pas dans un dépôt,
même privé. Même raison pour `settings.local.json` et `mcp-servers.backup.json`.

Les deux canons sauvegardés ici ont été scannés avant commit : aucune valeur de
secret, seulement des **noms** de variables et des préfixes.

# Files

- [Canon global de l'utilisateur](CANON-home-claude.md) - Copie de `~/.claude/CLAUDE.md`. Déclare la mémoire OKF comme source de vérité locale, les deux obligations de session, et le câblage Composio.
- [Canon du profil racine](CANON-profil-racine.md) - Copie de `C:\Users\amado\CLAUDE.md`. Économie de quotas et hiérarchie de délégation, vérification par capture, pièges du disque, gateway MCP, orchestration.
