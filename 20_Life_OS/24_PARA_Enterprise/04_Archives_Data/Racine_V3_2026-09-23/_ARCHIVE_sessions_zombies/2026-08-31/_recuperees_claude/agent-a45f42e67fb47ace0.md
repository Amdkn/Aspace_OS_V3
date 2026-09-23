---
session: agent-a45f42e67fb47ace0
origine: claude
chemin_source: C:\Users\amado\.claude\projects\C--Users-amado-ASpace-OS-V2-20-Life-OS-24-PARA-Enterprise-03-Resources-Geordi-05-From-V2-Domains-30-Business-OS-10-Projects-omk-repos-coach-os\ca97fbde-12a3-4ef8-ad54-76889373f863\subagents\agent-a45f42e67fb47ace0.jsonl
debut: 2026-08-17T17:05:19.797Z
fin: 2026-08-17T17:06:06.796Z
messages_utilisateur: 1
reponses_assistant: 4
titre: "Je prépare un document d'architecture sur Coach OS (apps embarquées, multi-tenant). Pour la section OAuth, j'a…"
---

## >>> UTILISATEUR #1

Je prépare un document d'architecture sur Coach OS (apps embarquées, multi-tenant). Pour la section OAuth, j'ai besoin de faits précis et CITÉS sur trois services SaaS. Réponds en français, sous format tableau, en citant l'URL source pour chaque fait.

Pour CHAQUE service (Notion, Airtable, ClickUp), trouve :

1. **Unité d'isolation du compte utilisateur** : un workspace = un client ? Y a-t-il plusieurs workspaces par utilisateur ? Comment l'API distingue-t-elle ?

2. **Couverture de l'OAuth utilisateur** : Quand un utilisateur autorise une intégration OAuth, l'application tierce a-t-elle accès à :
   - TOUT le workspace / toutes les bases / tous les espaces, ou
   - Une sélection (ex. : pages Notion choisies une par une, bases Airtable choisies, équipes ClickUp choisies) ?
   - Y a-t-il un sélecteur à l'écran lors du consentement ?

3. **Portée des tokens (scopes)** : Liste les scopes OAuth typiques. Sont-ils granulaires (par page/base) ou globaux (par workspace) ?

4. **Limites de taux d'API (rate limits)** :
   - Sont-elles par **compte utilisateur** ou par **application OAuth** ou par **workspace** ?
   - Donne les chiffres exacts (ex. : 3 req/s par workspace, X req/min par user).
   - Indique la fenêtre de temps.

5. **Révocation** : L'utilisateur peut-il révoquer l'accès OAuth depuis l'UI du service ? À quelle granularité ?

Sources à consulter prioritairement :
- Notion : https://developers.notion.com/docs/authorization et https://developers.notion.com/reference/request-limits
- Airtable : https://airtable.com/developers/web/api/oauth-reference et https://airtable.com/developers/web/api/rate-limits
- ClickUp : https://clickup.com/api/developer-portal/authentication/ et https://clickup.com/api/developer-portal/rate-limits/

Pour chaque fait, cite l'URL exacte. Si tu ne TROUVES PAS une réponse dans la documentation, écris « NON TROUVÉ » — n'invente pas.

Réponse sous 800 mots. Pas de blabla, des faits et des citations.

### assistant

Je vais consulter la documentation officielle de chaque service en parallèle, puis synthétiser les faits avec citations.

### assistant

Je relance les deux URLs ClickUp redirigées, plus une page complémentaire Notion pour les scopes, et la page des scopes Airtable.

### assistant

J'ai assez de matière. Je clôture la tâche ci-dessus et je rédige la réponse livrable.

### assistant

# OAuth multi-tenant — Notion · Airtable · ClickUp

## 1. Notion

| # | Question | Réponse | Source |
|---|---|---|---|
| 1 | Unité d'isolation | Un compte = un ou plusieurs workspaces. L'API identifie l'installation par `bot_id` + `workspace_id` (retournés dans la réponse OAuth). | https://developers.notion.com/docs/authorization |
| 2 | Couverture OAuth | **Sélection explicite, page par page.** « The user selects which workspace pages to share », « a page picker interface opens », « only displays pages or databases to which a user has full access ». Pas d'accès au workspace entier. | https://developers.notion.com/docs/authorization |
| 3 | Scopes | Capacités granulaires (pas des scopes nommés au sens OAuth classique) : **Read content**, **Update content**, **Insert content**, **Read comments**, **Insert comments**, **User information (with / without email) / No user information**. Combinables. | https://developers.notion.com/reference/capabilities |
| 4 | Rate limits | **3 req/s en moyenne par connexion**, avec bursts autorisés, plus une limite par workspace scalée au plan. Erreurs : 429 (`rate_limited`), 529 (`service_overload`). Header `Retry-After` (secondes). | https://developers.notion.com/reference/request-limits |
| 5 | Révocation | L'utilisateur peut « return to this view at a later time to update access settings » (ajouter/retirer des pages). Ré-autorisation émet un nouveau couple `access_token` / `refresh_token`. | https://developers.notion.com/docs/authorization |

## 2. Airtable

| # | Question | Réponse | Source |
|---|---|---|---|
| 1 | Unité d'isolation | « Tokens act as the account of the authorizing user, with additional limitations according to its scopes and the bases and workspaces that were granted to it. » L'isolation est **par base / par workspace accordé**. | https://airtable.com/developers/web/api/oauth-reference |
| 2 | Couverture OAuth | **Sélecteur explicite au consentement.** « Tokens can only access the bases and workspaces that the user granted to the OAuth integration. » « Users can add or revoke resources for an access token at any time. » L'utilisateur peut ajouter/révoquer des bases individuellement. | https://airtable.com/developers/web/api/oauth-reference |
| 3 | Scopes | Format `resource:action` : `schema.bases:read`, `data.records:read`, `data.records:write`, `data.recordComments:read`, `data.recordComments:write`, `webhook:manage`, etc. « Scopes define what actions can be performed on behalf of the user » et « only applicable to resources that a user has granted your integration access to ». | https://airtable.com/developers/web/api/oauth-reference + `/api/scopes` |
| 4 | Rate limits | **5 req/s par base** (OAuth). **50 req/s** pour les personal access tokens / service account. Pénalité : 429 + « wait 30 seconds before subsequent requests ». | https://airtable.com/developers/web/api/rate-limits |
| 5 | Révocation | Granularité **par ressource** (base/workspace) : « Users can add or revoke resources for an access token at any time. » + révocation par disable de scope côté développeur (caduque pour tous les tokens). Refresh token expiré ⇒ re-consentement. | https://airtable.com/developers/web/api/oauth-reference |

## 3. ClickUp

| # | Question | Réponse | Source |
|---|---|---|---|
| 1 | Unité d'isolation | **Workspace** = unité atomique. « Allowing users to authorize Workspaces for your app. » Un utilisateur peut appartenir à plusieurs Workspaces ; un Workspace = un client. | https://developer.clickup.com/docs/authentication |
| 2 | Couverture OAuth | **Granularité Workspace uniquement.** « Users can authorize one or more Workspaces. » Pas de sélection Space/List/Task au consentement — le token a accès à **tout** le workspace autorisé. Pour modifier : redirection vers l'URL d'autorisation. | https://developer.clickup.com/docs/authentication |
| 3 | Scopes | **NON TROUVÉ** dans la page authentication. Le doc ne mentionne ni paramètre `scope` ni liste de scopes. La granularité affichable se limite au Workspace. | https://developer.clickup.com/docs/authentication |
| 4 | Rate limits | **Par token** (et non par user / workspace / team) — couvre personnel et OAuth. Valeurs : Free/Unlimited/Business = 100 req/min ; Business Plus = 1 000 req/min ; Enterprise = 10 000 req/min. Headers en cas de 429 : `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset` (Unix ts). | https://developer.clickup.com/docs/rate-limits |
| 5 | Révocation | **NON TROUVÉ** explicitement. Seul indice : « Redirect users to the authorization URL to modify Workspace permissions. » Note : « The access token currently does not expire. This is subject to change. » | https://developer.clickup.com/docs/authentication |

## Synthèse pour Coach OS

- **Notion** : isolation fine, scope = page par page, idéal multi-tenant granulaire. Rate limit le plus contraignant (3 req/s).
- **Airtable** : isolation fine (base par base), scopes `resource:action` propres à l'API. 5 req/s/base — budgétiser par client.
- **ClickUp** : isolation **grossière** (workspace entier = tout ou rien). Si un client a plusieurs Workspaces, prévoir N consentements. Pas de scopes fins documentés publiquement. Tokens non expirants aujourd'hui (à surveiller).
