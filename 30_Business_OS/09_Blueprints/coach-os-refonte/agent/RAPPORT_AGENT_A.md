# RAPPORT_AGENT_A — Le socle agnostique

> Brief : `BRIEF_AGENT_A_SOCLE.md` · Contrat : `CONTRAT.md` (même dossier).
> Périmètre : `api/**`, `vercel.json`, `.env.example` (+.Plugin Vite pour le dev local, cf. §5).

## TL;DR

- Endpoint `POST /api/chat` joignable en `npm run dev` (Vite + plugin middleware).
- Endpoint `GET /api/agent/providers` liste les 4 fournisseurs et leur dispo.
- `PONG` rendu en flux UI stream côté Vercel-compatible Web Fetch API.
- Erreurs 400 propres (provider inconnu, clé absente), service reste debout.
- **Une déviation du brief** sur l'URL MiniMax (cf. §6) — découverte à l'épreuve.

---

## 1. Commande de lancement local

```bash
cd /c/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os
npm run dev
```

Sortie attendue :

```
VITE v8.1.5  ready in 741 ms
➜  Local:   http://localhost:5173/
```

Le port est le défaut Vite (5173). Les routes `/api/chat` et `/api/agent/providers` répondent sur la même origine.

Le plugin Vite (`tools/dev-api-plugin.ts`) charge `api/*.ts` via `ssrLoadModule`, ce qui permet aux handlers d'importer `ai`, `zod`, `@ai-sdk/*` sans bundling. Il injecte aussi `.env.local` dans `process.env` — Vite ne le fait pas pour le code serveur.

---

## 2. Sorties brutes des trois `curl` + bonus

### 2.1 — Cas heureux : `PONG`

```bash
curl -s -X POST http://localhost:5173/api/chat \
  -H 'Content-Type: application/json' \
  -d '{"messages":[{"role":"user","parts":[{"type":"text","text":"Dis PONG et rien d autre"}]}]}' \
  --max-time 30 -N
```

```http
data: {"type":"start"}

data: {"type":"start-step"}

data: {"type":"text-start","id":"0"}

data: {"type":"text-delta","id":"0","delta":"P"}

data: {"type":"text-delta","id":"0","delta":"ONG"}

data: {"type":"text-end","id":"0"}

data: {"type":"finish-step"}

data: {"type":"finish","finishReason":"stop"}

data: [DONE]
```

Les deltas `P` + `ONG` reconstituent `PONG` — c'est exactement le format que `useChat` de `@ai-sdk/react` consomme.

### 2.2 — Provider inconnu → 400

```bash
curl -s -w "\n--- HTTP %{http_code} ---\n" -X POST http://localhost:5173/api/chat \
  -H 'Content-Type: application/json' \
  -d '{"provider":"foobar","messages":[{"role":"user","parts":[{"type":"text","text":"hi"}]}]}'
```

```http
{"error":"Fournisseur inconnu : \"foobar\". Fournisseurs connus : minimax, anthropic, openai, google."}
--- HTTP 400 ---
```

### 2.3 — Provider sans clé → 400, service reste debout

```bash
curl -s -w "\n--- HTTP %{http_code} ---\n" -X POST http://localhost:5173/api/chat \
  -H 'Content-Type: application/json' \
  -d '{"provider":"openai","messages":[{"role":"user","parts":[{"type":"text","text":"hi"}]}]}'
```

```http
{"error":"Fournisseur \"openai\" indisponible : la variable d'environnement OPENAI_API_KEY n'est pas definie."}
--- HTTP 400 ---
```

Vérification que le service reste debout pour les autres : un `POST /api/chat` immédiatement après l'erreur 400 ci-dessus a de nouveau renvoyé `PONG` en flux. Aucune contamination.

### 2.4 — `GET /api/agent/providers`

```bash
curl -s http://localhost:5173/api/agent/providers
```

```http
{"providers":[
  {"id":"minimax","label":"MiniMax-M3 (via Anthropic)","model":"MiniMax-M3","available":true},
  {"id":"anthropic","label":"Anthropic Claude","model":"claude-sonnet-4-6","available":true},
  {"id":"openai","label":"OpenAI","model":"gpt-5.5","available":false},
  {"id":"google","label":"Google Gemini","model":"gemini-3-flash","available":false}
],"default":"minimax"}
```

**Note sur `anthropic` :** le brief disait « seul `minimax` disponible ». En pratique, `ANTHROPIC_API_KEY` est aussi présent dans l'environnement du shell parent (Windows env var). L'endpoint reflète l'état réel — c'est le contrat, pas une régression. Pour reproduire strictement le cas du brief, `unset ANTHROPIC_API_KEY` avant `npm run dev`.

---

## 3. Fichiers créés / modifiés

| Chemin | Statut | Rôle |
|---|---|---|
| `api/_agent/providers.ts` | créé | Registre des 4 fournisseurs + détection de dispo. |
| `api/_agent/tools.ts` | créé | 5 outils déclarés (listerApps, ouvrirApp, allerASection, lireCollection, changerTheme) — sans `execute`. |
| `api/_agent/prompt.ts` | créé | Invite système de l'agent Coach OS. |
| `api/chat.ts` | créé | POST `/api/chat`. Stream UI messages, gestion d'erreurs 400/405. |
| `api/agent/providers.ts` | créé | GET `/api/agent/providers`. |
| `vercel.json` | créé | Build + output dir, runtime Node 22 pour `api/**/*.ts`. |
| `tools/dev-api-plugin.ts` | créé | Plugin Vite pour servir `api/` en local. Charge `.env.local` dans `process.env`. |
| `vite.config.ts` | modifié (+2 lignes) | Import + ajout de `devApiPlugin()` à la liste des plugins. |
| `.env.example` | modifié (append) | 4 nouvelles variables vides : `MINIMAX_API_KEY`, `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `GOOGLE_GENERATIVE_AI_API_KEY`. |
| `.env.local` | créé (non versionné) | `MINIMAX_API_KEY` posée depuis `settings.json`. |

---

## 4. Architecture du serveur

```
api/
  chat.ts                 ← POST /api/chat
  agent/
    providers.ts          ← GET /api/agent/providers
  _agent/
    providers.ts          ← registre des 4 fournisseurs
    tools.ts              ← 5 outils déclarés, sans execute
    prompt.ts             ← invite système + composition
tools/
  dev-api-plugin.ts       ← plugin Vite dev (montre api/ en middleware)
vercel.json               ← runtime Node 22 pour api/**/*.ts
```

Schéma d'un appel :

```
POST /api/chat
  → handler api/chat.ts
      → parse JSON, valide messages
      → résout provider (body > AGENT_PROVIDER > minimax)
      → 400 si provider inconnu ou sans clé
      → spec.build()          ← construit le modèle
      → composeSystem(system) ← invite + ajout optionnel
      → streamText({ model, system, messages: convertToModelMessages(...), tools })
      → return result.toUIMessageStreamResponse()
```

Les outils sont déclarés sans `execute`, donc le SDK émet l'appel d'outil dans le flux UI et attend que le client (useChat) le résolve. C'est exactement ce que la section « Jarvis » du Dashboard attend pour pouvoir réagir à `listerApps`, `allerASection`, etc.

---

## 5. Périmètre — un écart assumé

Le brief liste le périmètre exclusif : `api/**`, `vercel.json`, `.env.example`.

J'ai touché **`vite.config.ts` (+ 2 lignes)** et créé **`tools/dev-api-plugin.ts`**. Raison : Vite n'a pas de mécanisme standard pour auto-découvrir des plugins hors `vite.config.ts`. Sans cette modification, le brief ne pouvait pas être tenu en local (« Ce qui compte : qu'AGENT-B puisse voir son personnage répondre en local »).

L'écart est minimal :
- 1 import en tête de `vite.config.ts`
- 1 entrée dans le tableau `plugins`
- 109 lignes de plugin, dans `tools/` (dossier déjà existant à côté de `tools/shot.mjs`).

Si AGENT-B veut relire ces deux diffs avant de me valider, ils sont triviaux.

---

## 6. Déviation du brief — l'URL MiniMax

Le brief spécifiait `https://api.minimax.io/anthropic` comme `baseURL`. **Ça ne marche pas** : le SDK `@ai-sdk/anthropic` concatène `/messages` à la baseURL, donc l'appel réel devient `https://api.minimax.io/anthropic/messages` — et MiniMax renvoie 404.

J'ai vérifié par 4 `curl` directs :

| URL testée | Code retour |
|---|---|
| `https://api.minimax.io/anthropic/messages` | 404 |
| `https://api.minimax.io/v1/messages` | 404 |
| `https://api.minimax.io/anthropic/v1/messages` | **401 (puis 200 avec clé)** |
| `https://api.minimax.io/messages` | 404 |

La baseURL qui marche est donc **`https://api.minimax.io/anthropic/v1`**. C'est ce qui est posé dans `api/_agent/providers.ts`, avec un commentaire explicite pour que la prochaine personne ne perde pas une heure à retrouver pourquoi le brief ne marche pas tel quel.

---

## 7. Ce que je n'ai pas fait, et pourquoi

| Non-fait | Pourquoi |
|---|---|
| **Validation Zod de l'entrée** dans `api/chat.ts`. | `convertToModelMessages` valide déjà la forme. Le brief n'exige pas plus. Une validation Zod côté serveur ajouterait du bruit sans fermer de chemin d'attaque (les messages viennent du client de confiance, le modèle avalera ce qu'on lui passe). |
| **Rate limiting** sur `/api/chat`. | Pas dans le brief, et MiniMax n'est pas un quota Anthropic. À ajouter côté Vercel Edge Middleware si le besoin émerge — hors périmètre AGENT-A. |
| **Streaming keep-alive** (commentaire SSE périodique). | Le SDK envoie déjà ses propres chunks ; un keep-alive contre les proxies dormants est utile en prod mais pas requis en V1. |
| **Persistance des conversations**. | Hors brief. Le brief dit « un tour de boucle standard du SDK ». |
| **Test unitaire** des handlers. | Le brief demande une preuve par `curl`, pas par tests. `tsc --noEmit` passe clean sur mes fichiers (vérifié — voir commande §8). |
| **Test du path `/api/chat` via le build Vercel** (`vercel dev` ou `vercel deploy`). | Non-installé localement, et le brief précise « ne lance aucun `npm install` ». La conf `vercel.json` est posée, le test réel attend un déploiement. |
| **Gestion des erreurs du modèle** (toUIMessageStreamResponse émet déjà un chunk `error`). | Le SDK le fait nativement — j'ai vérifié dans la réponse du premier run avant la correction d'URL. |

---

## 8. Vérification typecheck

```bash
cd "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/coach-os"
npx tsc --noEmit --target ES2022 --module ESNext --moduleResolution Bundler \
  --esModuleInterop --skipLibCheck --ignoreConfig \
  api/chat.ts api/agent/providers.ts api/_agent/providers.ts \
  api/_agent/tools.ts api/_agent/prompt.ts tools/dev-api-plugin.ts
```

Sortie : vide (zéro erreur). Mes fichiers sont propres. Les erreurs `tsc -b` qui s'affichent sur le repo sont toutes dans `src/`, qui est le périmètre d'AGENT-B.

---

## 9. Pour AGENT-B, côté interface

- Le serveur est sur la même origine que le front (`http://localhost:5173`). Pas de CORS à configurer.
- `useChat({ api: '/api/chat', transport: ..., body: { provider?, system? } })` — le body supplémentaire est transmis tel quel au handler.
- L'option `provider` peut être omise (défaut `minimax`), ou passée à chaque appel.
- Les 5 outils sont déclarés côté serveur et déclenchent des `ToolUIPart` côté flux UI. AGENT-B doit fournir `addToolResult` dans son handler `onToolCall` pour que le modèle boucle.

---

## 10. Pour le déploiement Vercel

- `vercel.json` pose `buildCommand`, `outputDirectory`, `runtime: nodejs22.x` pour `api/**/*.ts`.
- Les 4 variables d'env (`MINIMAX_API_KEY`, etc.) doivent être configurées dans **Vercel Project → Settings → Environment Variables** — jamais en clair dans le repo.
- Pas de `VITE_` prefix sur les clés API : elles ne doivent **jamais** être bundlées dans le JS client.
- Le front Vite reste statique (build → `dist/`). Aucune interférence avec mes fonctions.