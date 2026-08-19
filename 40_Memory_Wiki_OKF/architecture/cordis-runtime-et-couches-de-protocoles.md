---
type: Backend
title: Cordis est le runtime de DeepSeek Harness — et les protocoles d'agents sont des couches, pas des rivaux
description: dsh est bâti sur Cordis (cordiverse/cordis) ; MCP, A2A, AG-UI, ACP et UCP occupent des étages différents de la pile et ne se remplacent pas.
tags: [cordis, deepseek-harness, mcp, a2a, ag-ui, acp, litert, adaptateur, coach-os]
generated: { by: claude-opus-5, at: 2026-08-17T23:30:00Z }
verified:
  - { by: process:web-search, at: 2026-08-17T23:25:00Z }
  - { by: process:grep-coach-os, at: 2026-08-17T23:10:00Z }
sources:
  - id: dsh
    resource: https://thenewstack.io/deepseek-harness-open-source-plugins/
    title: "DeepSeek open sources an agent harness where everything is a plugin"
    last_modified: 2026-08-17
  - id: cordis
    resource: https://github.com/cordiverse/cordis
    title: "Cordis — A Meta-Framework of Spatiotemporal Composability"
    last_modified: 2026-08-17
  - id: couches
    resource: https://www.digitalapplied.com/blog/ai-agent-protocol-ecosystem-map-2026-mcp-a2a-acp-ucp
    title: "AI Agent Protocol Ecosystem Map 2026"
    last_modified: 2026-08-17
  - id: mesure-coach-os
    resource: "grep sur coach-os — src/lib/tooling/adapters/ et api/_agent/, recherche litert|tflite"
    author: process:grep-coach-os
    last_modified: 2026-08-17
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Les faits sur `dsh` et Cordis
> viennent d'une recherche web du 2026-08-17 ; l'état de Coach OS d'un `grep`
> sur le dépôt. **Aucun n'a été vérifié par lecture du code de `dsh` lui-même.**

# Le fait qui répond à la question

**DeepSeek Harness (`dsh`) est bâti sur Cordis.** C'est le runtime « inconnu »
cherché : `github.com/cordiverse/cordis`, un méta-framework de composabilité par
greffons — services, événements typés, effets de bord réversibles sur un
contexte partagé.

`dsh` est publié sous MIT sur `github.com/deepseek-ai/deepseek-harness`, en
Node.js, en **preview développeur** — son README annonce des ruptures d'API.
Sa formule : *« Model + Harness = Agent »*, et son principe : **tout est un
greffon** — l'adaptateur de modèle, le registre d'outils, le journal de session,
et la boucle d'agent elle-même sont tous remplaçables.

# Les protocoles sont des couches, pas des concurrents

C'est le point que la liste des « 10 protocoles » masque en les alignant côte à
côte. Ils n'occupent pas le même étage :

| Couche | Protocole | Ce qu'il relie |
|---|---|---|
| outils | **MCP** (Anthropic) | agent → outils, API, données |
| agent à agent | **A2A** (Google, passé à la Linux Foundation) | agent → agent, par *agent cards* |
| interface | **AG-UI** (CopilotKit) | agent → frontend, en SSE événementiel |
| éditeur | **ACP** (Zed) — agentclientprotocol.com | agent de code → IDE |
| commerce | **UCP / AP2** | flux d'achat, autorisation de paiement |

**`ACP` est ambigu et il faut le désambiguïser à chaque usage** : Agent Client
Protocol (Zed, IDE), Agent Communication Protocol (IBM, négociation FIPA-ACL),
et Agent Commerce Protocol coexistent sous le même sigle.

La gouvernance est **fragmentée** : MCP appartient à Anthropic, A2A à la Linux
Foundation, UCP/AP2 penchent Google, AG-UI appartient à CopilotKit. Aucun
arbitre commun.

# LiteRT ne remplace pas un adaptateur — il n'est pas au même étage

**LiteRT est un runtime d'inférence sur l'appareil.** Un adaptateur d'outils est
une couche d'**exposition**. Les confondre mènerait à un remaniement inutile.

Dans Coach OS, LiteRT s'insérerait dans `api/_agent/backends/` — comme un
fournisseur de modèle local à côté des autres —, **pas** dans
`src/lib/tooling/adapters/`.

Mesure du 2026-08-17 : **aucune trace de `litert`, `tflite` ni
`tensorflow.lite`** dans `src/`, `api/`, `package.json` ni `_briefs/`. La piste
n'a jamais été ouverte dans le code.

# Ce que Coach OS a déjà, et qui ressemble beaucoup à dsh

Neuf adaptateurs, 1 501 lignes, un registre unique exposé sur sept surfaces :

```
cli 262 · harness 250 · rest 244 · mcp 214 · skill 192
mcp-apps 162 · in-app 63 · mcp-schema 60 · zod-introspect 54
```

`mcp.ts` est un serveur JSON-RPC 2.0 stdio sur le SDK officiel, qui **multiplexe
tous les outils** — une connexion, pas N — et branche identité, permission et
journal. `mcp-apps.ts` est la septième surface : elle expose un outil comme une
**interface HTML** rendue en iframe bac à sable, pas comme une fonction.

**Le patron « define once, expose everywhere » est donc déjà en place.** Ce que
Cordis apporterait n'est pas ce patron mais son **hôte** : un démon qui monte
les adaptateurs comme greffons, avec des effets réversibles et un profil par
invité.

# Ce qui manque et qu'il ne faut pas confondre

Coach OS a le **serveur MCP stdio**. Il n'a pas de surface MCP **Web**
(transport HTTP/SSE) : ce serait un dixième adaptateur, pas une évolution des
neuf existants.

# Le risque à ne pas sous-estimer

`dsh` est en preview développeur, avec ruptures d'API annoncées. Cordis se
déclare lui-même *« under active development, the API is not yet stable and may
change without notice »*.

Bâtir le méta-adaptateur d'un produit sur deux socles qui annoncent tous les
deux l'instabilité est un pari. Il peut être bon — la composabilité y est
réelle — mais **il se prend en connaissance de cause, et l'adhérence doit rester
mince** : les neuf adaptateurs actuels ne dépendent d'aucun hôte, et c'est ce
qui les rend portables.
