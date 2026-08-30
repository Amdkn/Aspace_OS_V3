# Le contrat entre les deux chantiers

Deux agents travaillent en parallèle. Ce fichier est la **seule** chose qu'ils partagent.
Il ne se négocie pas : si ton implémentation ne colle pas, c'est ton implémentation qui change.

## Le point de rendez-vous

```
POST /api/chat
```

**Requête** — corps JSON :

```jsonc
{
  "messages": [ /* UIMessage[] du SDK, tel que produit par useChat */ ],
  "provider": "minimax" | "anthropic" | "openai" | "google",  // optionnel
  "system": "…"                                                // optionnel
}
```

Sans `provider`, le serveur prend `AGENT_PROVIDER` de l'environnement, et `minimax` à défaut.

**Réponse** — un flux de messages UI du SDK, produit par `toUIMessageStreamResponse()`.
C'est exactement ce que `useChat` de `@ai-sdk/react` sait consommer. Pas de format maison.

**Erreur** — JSON `{ "error": "<message lisible> " }` avec un code HTTP franc (400, 401, 502).
Jamais un 200 qui contient une erreur : le client doit pouvoir distinguer sans lire le corps.

## Les outils

Ils sont **déclarés côté serveur** (nom, description, schéma des paramètres) et **exécutés
côté client**, parce qu'ils agissent sur le bureau — ouvrir une app, changer de section.
C'est le tour de boucle standard du SDK : le serveur émet un appel d'outil, le client
l'exécute et renvoie le résultat, le modèle continue.

Les cinq outils de la V1, noms figés :

| nom | paramètres | ce qu'il fait |
|---|---|---|
| `listerApps` | — | rend la liste des apps installées et de leurs sections |
| `ouvrirApp` | `appId` | ouvre la fenêtre de l'app |
| `allerASection` | `appId`, `sectionId` | ouvre l'app et se place sur la section |
| `lireCollection` | `collectionId` | rend les items d'une collection du CMS |
| `changerTheme` | `themeId`, `appId?` | change le thème global, ou celui d'une app |

Le serveur les **déclare**. Le client les **exécute**. Aucun des deux n'invente un sixième outil.

## Les versions, déjà posées

Ne lance **aucun** `npm install`. Tout est déjà là, et le verrou a été vérifié par `npm ci` :

```
ai@7.0.56 · @ai-sdk/react@4.0.59 · @ai-sdk/anthropic@4 · @ai-sdk/openai@4 · @ai-sdk/google@4
```

`@ai-sdk/react@2` embarque `ai@5` et parle un autre protocole de flux — c'est le piège de
cette pile, il a déjà été payé. La version 4 est la seule qui s'aligne sur `ai@7`.

## Les fournisseurs

Quatre, dont un compte double.

**MiniMax-M3 passe par le fournisseur Anthropic.** MiniMax expose un point d'entrée
compatible Anthropic : `https://api.minimax.io/anthropic`. Il suffit donc de construire le
fournisseur Anthropic avec cette `baseURL` et le modèle `MiniMax-M3`. Zéro code spécifique,
et c'est la voie qui ne consomme pas les quotas Anthropic — la raison d'être de tout ça.

| id | paquet | modèle par défaut | variable d'environnement |
|---|---|---|---|
| `minimax` | `@ai-sdk/anthropic` + `baseURL` MiniMax | `MiniMax-M3` | `MINIMAX_API_KEY` |
| `anthropic` | `@ai-sdk/anthropic` | `claude-sonnet-4-6` | `ANTHROPIC_API_KEY` |
| `openai` | `@ai-sdk/openai` | `gpt-5.5` | `OPENAI_API_KEY` |
| `google` | `@ai-sdk/google` | `gemini-3-flash` | `GOOGLE_GENERATIVE_AI_API_KEY` |

Un fournisseur dont la clé manque n'est pas une erreur au démarrage : il est simplement
**indisponible**, et le demander rend un 400 qui le dit. Le service ne tombe pas parce
qu'une clé sur quatre est absente — c'est la leçon du gateway MCP, où une cible morte
abattait tout.

## Les secrets

`.env.local` est déjà dans `.gitignore`. **Aucune clé dans le code, aucune clé dans un
fichier versionné, aucune clé dans un message de commit.** Une clé lue depuis
`settings.json` reste dans `.env.local`, jamais ailleurs.
