# Mémoire canonique — OpenWiki + OKF

> **Ce fichier est sauvegardé dans le dépôt.** Sa copie vit dans
> `ASpace_OS_V3/40_Memory_Wiki_OKF/canon/CANON-home-claude.md`.
> **Toute édition de ce fichier se recopie là-bas dans le même commit.**
> Un instantané qui a divergé en silence est pire qu'une absence de
> sauvegarde : il inspire confiance sans la mériter.

> **Source de vérité locale : `C:\Users\amado\ASpace_OS_V3\40_Memory_Wiki_OKF\`**
>
> Bundle OKF v0.2. C'est la mémoire du poste. Pas les notes de session, pas
> `~/.claude/projects/*/memory/`, pas un fichier de travail — **ce bundle**.
>
> **`ASpace_OS_V3\openwiki\` n'est PAS la mémoire** (correction du 2026-08-17).
> C'est un clone du dépôt amont `langchain-ai/openwiki` — l'outil qui *génère*
> des wikis. Il a son propre `.git`, il est invisible depuis le statut du dépôt
> parent, et son unique remote ne nous appartient pas. Un concept écrit là ne
> se pousse nulle part et meurt avec le disque.

## Deux obligations, à chaque session

### 1. Chercher ici AVANT de chercher ailleurs

Toute question sur une intégration, une décision passée, un piège déjà payé,
une configuration : **lire le bundle d'abord**. Point d'entrée
`40_Memory_Wiki_OKF/index.md`, puis les sous-bundles (`architecture/`,
`integrations/`, `operations/`, `security/`).

Le format est décrit dans `40_Memory_Wiki_OKF/OKF.md`, les gestes de lecture et
d'écriture dans `40_Memory_Wiki_OKF/quickstart.md`.

Redécouvrir à l'aveugle ce qui est déjà écrit coûte du quota et produit des
réponses moins sûres que le document.

### 2. Écrire ici À LA FIN de chaque tâche

Une tâche terminée qui a produit une connaissance durable — une intégration
câblée, une cause racine trouvée, un piège payé, une décision d'architecture —
**se consigne dans le bundle avant de clore**.

Le format est OKF v0.2. Le frontmatter minimal :

```yaml
---
type: <Integration | Security Model | Vulnerability | Backend | Playbook | …>
title: <titre lisible>
description: <une phrase>
tags: [<…>]
generated: { by: <acteur>, at: <ISO 8601> }
verified:
  - { by: <acteur>, at: <ISO 8601> }
sources:
  - id: <clé stable>
    resource: <URL, chemin, ou description de portée>
    title: <libellé>
    last_modified: <YYYY-MM-DD>
okf_version: "0.2"
---
```

**Le niveau de confiance se déduit de `verified`** et cette distinction est
tout l'intérêt du format :

| `verified` | Niveau |
|---|---|
| absent | **non vérifié** |
| acteurs non-`human:` uniquement | **confirmé par machine** |
| au moins un `human:<id>` | **revu par un humain** |

Une affirmation mesurée et une affirmation supposée ne doivent jamais se
ressembler. C'est ce qui a coûté six tables appliquées au mauvais projet
Supabase et une sonde de test qui accusait le mauvais coupable.

### Après avoir écrit un concept

1. Ajouter une ligne dans l'`index.md` du sous-bundle (convention `# Files`).
2. Ne **jamais** poser de lien `[[nom]]` vers un concept qui n'existe pas —
   vérifier avant d'écrire. Un lien mort ment à l'avenir.

## Ce qui ne va PAS dans le bundle

- Les secrets. Jamais. Ni valeur, ni fragment. Le préfixe suffit (`ck_…`).
- Ce que le dépôt raconte déjà (structure du code, historique git).
- Ce qui n'intéresse que la conversation en cours.

---

# MCP Composio branché en direct

## Ce qui est en place

Composio For You est configuré comme gateway MCP Cloud personnel, à la
racine de `~/.mcp.json`, **pas** dans le gateway local (port 3300). La
raison est donnée dans le concept OKF
`ASpace_OS_V3/40_Memory_Wiki_OKF/integrations/composio-mcp-as-gateway.md` :
l'agentgateway tombe dès qu'un seul MCP échoue, et c'est inacceptable pour
une clé cloud personnelle.

## Fichiers touchés

| Fichier | Contenu |
|---|---|
| `~/.claude/settings.json` | `env.COMPOSIO_CONSUMER_KEY` (gitignoré) |
| `~/.mcp.json` | entrée `composio` HTTP vers `https://connect.composio.dev/mcp` avec header `x-consumer-api-key: ${COMPOSIO_CONSUMER_KEY}` |

Aucun fichier versionné, aucun `.env.local`, aucun brief. La clé n'apparaît
que dans `settings.json`, jamais ailleurs.

## Comment ça marche

`~/.mcp.json` est lu au **démarrage** de Claude Code, pas à chaud. Toute
modification exige un quit/relaunch de CC. C'est un comportement de la
plateforme, pas un défaut.

Le MCP expose 8 outils meta ; les 250+ outils d'apps (Gmail, Slack,
GitHub, Notion, etc.) s'accèdent via `COMPOSIO_SEARCH_TOOLS` puis
`COMPOSIO_MULTI_EXECUTE_TOOL`. Workflow type documenté dans le concept OKF.

## Confusions evitees

- **`ak_…` (Platform) ≠ `ck_…` (For You)**. L'utilisateur avait d'abord
  collé une `ak_…`. Platform n'expose pas d'endpoint MCP statique (MCP
  est session-scope via SDK). Le pivot vers For You était inévitable.
- **« clé AI » = clé API Composio**, pas un autre secret. Le mot « AI » dans
  la demande désignait la clé, pas l'API Anthropic.

## Comment retirer le cablage

1. `~/.mcp.json` → retirer l'entrée `composio`
2. `~/.claude/settings.json` → retirer `COMPOSIO_CONSUMER_KEY`
3. Redémarrer CC

Réversible, sans migration, sans script de deploy.

## Comment verifier que ça marche

Test Key Pragma validé le 2026-08-17 : `POST
https://connect.composio.dev/mcp` avec header `x-consumer-api-key`,
méthode MCP `tools/list` → HTTP 200, 8 outils rendus. Si le test passe,
la clé est valide et l'endpoint répond.

## Anti-pieges

- **Ne JAMAIS recopier la clé** `ck_…` dans une sortie, un brief
  versionné, ou un log. Le concept OKF ne contient que le préfixe, jamais
  la valeur.
- **L'installateur officiel de Composio refuse Windows.** Si on a besoin
  du CLI, passer par npm : `npm i -g composio`. Le binaire peut
  nécessiter un `npm link` ou un ajout au PATH sous Windows.
- **Le `~/.mcp.json` racine et `agentgateway` sont deux canaux
  indépendants.** Modifier l'un ne touche pas l'autre.
