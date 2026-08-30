# AGENT-C — Une troupe d'agents, un avatar chacun, branchés sur Buzz et Multica

Lis `CONTRAT.md` et `GARDE_FOU.md` dans ce dossier. Ils font partie de ce brief.

Ton rapport : `RAPPORT_AGENT_C.md`, à côté.

---

## L'état des lieux, mesuré

Ce qui existe déjà dans Coach OS, poussé le 2026-08-07 :

- `src/agent/characters.ts` — les **12 personnages** sont tous là, planches de sprites
  téléchargées dans `public/assets/assistant/<id>/`. Rien à ajouter de ce côté.
- `src/agent/SpriteAgent.tsx` — le moteur qui les anime.
- `src/agent/AssistantOverlay.tsx` — **un seul** personnage à l'écran à la fois.
- `api/_agent/providers.ts` — registre `id → fabrique de modèle` : `minimax` (M3 via
  l'endpoint compatible Anthropic), `anthropic`, `openai`, `google`.
- `src/agent/tools.ts` — cinq outils exécutés côté client.

**Le manque n'est donc pas les avatars. C'est qu'il n'y en a qu'un, et qu'il ne parle qu'à un
modèle brut** — jamais aux agents qui existent déjà ailleurs chez l'utilisateur.

## Ce qui existe ailleurs, et qu'on vient brancher

### Multica — plateforme d'agents, avec un CLI

```
CLI      multica  (dans %LOCALAPPDATA%\Microsoft\WinGet\Links)
config   ~/.multica/config.json  — server_url, workspace_id, token
export   ASpace_OS_V3/00_Amadeus/20_Harness/multica_export_2026-08-02/
```

`multica --help` donne : `agent`, `squad`, `autopilot`, `chat`, `issue`, `project`, `skill`,
`workspace`, `daemon`, `runtime`.

L'export contient **112 agents**, **12 squads**, **7 autopilotes**. Les agents portent déjà un
champ **`avatar_url`** — Multica a donc sa propre notion d'avatar, distincte des sprites.

Squads relevés : `Cerritos-HoloDeck`, `Squad-Orville`, `Squad-Discovery`, `Squad-SNW`,
`Squad-Enterprise`, `Squad-Protostar`, et six autres. **Douze squads, douze personnages** :
la correspondance est trop nette pour ne pas s'en servir comme réglage par défaut.

### Buzz — espace local, avec un CLI

```
CLI    %LOCALAPPDATA%\Buzz\buzz-agent.exe   (aussi buzz-acp.exe, buzz-desktop.exe)
Nest   ~/.buzz/  — AGENTS.md, .agents/skills, GUIDES, PLANS, packs, models, OUTBOX
```

`buzz-agent.exe` sans environnement rend :

```
ERROR buzz_agent: config: BUZZ_AGENT_PROVIDER is required — set it to your provider
(e.g. anthropic, openai, databricks)
```

**C'est exactement la forme du socle déjà posé** : Buzz est lui aussi agnostique du
fournisseur. Il peut donc tourner sur M3 par l'endpoint compatible Anthropic, comme le reste.

## Ce qu'on construit

### 1 · Un registre d'agents

Un agent, c'est trois choses : une **identité**, un **avatar**, un **dos**.

```
{ id, nom, description, personnage: <un des 12>, dos: 'modele' | 'multica' | 'buzz', ... }
```

Le registre vit côté serveur (il connaît les jetons) et s'expose par
`GET /api/agent/roster`. Le client ne voit que ce qu'il a le droit d'afficher.

### 2 · Trois dos, une seule interface

| dos | comment on lui parle |
|---|---|
| `modele` | ce qui existe déjà — `/api/chat` et le registre de fournisseurs |
| `multica` | on lance le CLI `multica` |
| `buzz` | on lance `buzz-agent.exe` avec `BUZZ_AGENT_PROVIDER` |

**Découvre les sous-commandes toi-même** (`multica agent --help`, `multica chat --help`) plutôt
que de deviner : je ne les ai pas explorées et je ne veux pas que tu bâtisses sur une
supposition. Si une commande n'existe pas sous la forme attendue, dis-le dans ton rapport
plutôt que de contourner en silence.

Un CLI, c'est un processus : sortie en flux, code de retour, délai maximum. Un agent qui ne
répond pas doit rendre une erreur lisible dans la bulle, jamais un chargement éternel.

**Rien de tout ça ne tourne dans le navigateur.** Lancer un exécutable local est une opération
serveur. Sur Vercel, ces deux dos seront indisponibles — c'est attendu, et le registre doit le
dire proprement, comme il le fait déjà pour un fournisseur sans clé.

### 3 · Plusieurs personnages à l'écran

Aujourd'hui l'overlay en affiche un. Il doit en afficher **N**, un par agent convoqué : chacun
sa position, sa bulle, sa conversation.

Trois choses à ne pas rater, toutes déjà payées sur ce bureau :

- **Borne chaque position contre la fenêtre**, au montage et au redimensionnement. Une
  position en dur (`x: 1180, y: 700`) rendait le personnage invisible sous le bord bas dans un
  navigateur intégré — présent dans le DOM, animé, et introuvable.
- **Ne charge pas les douze planches d'un coup** : 1,3 Mo chacune. Le chargement reste à la
  demande, personnage par personnage.
- **Un sélecteur Zustand ne rend qu'un scalaire ou une référence stable.** Un tableau construit
  à chaque appel fait boucler React jusqu'à la page blanche. Quatre fois dans cet écosystème.

### 4 · Le réglage

Dans Settings > Assistant : la liste des agents, l'avatar attribué à chacun, et de quel dos il
vient. Attribution par défaut : les douze squads Multica sur les douze personnages, dans
l'ordre. L'utilisateur peut réattribuer.

Si un agent Multica porte une `avatar_url`, montre-la **à côté** de son sprite dans le
réglage — c'est son identité côté plateforme. Le sprite reste sa présence sur le bureau.

## Ton périmètre

```
src/agent/**            (extension)
src/stores/assistant.store.ts
src/apps/settings/AssistantSettings.tsx
api/**                  (extension)
```

Pas de `npm install`, pas de verrou touché : le déploiement Vercel a déjà été cassé une fois
sur ce point.

## Les secrets

Le jeton Multica est **en clair** dans `~/.multica/config.json`, préfixe `mul_`. Il ne doit
apparaître ni dans le code, ni dans un fichier versionné, ni dans un message de commit, ni
dans une réponse de l'API. Il est lu côté serveur et n'en sort pas.

## Preuve attendue

Des captures, pas du code lu :

1. trois personnages différents sur le bureau **en même temps**, chacun sa bulle ;
2. une réponse venue de Multica par le CLI, et une venue de Buzz — sortie brute du CLI dans le
   rapport à côté de la capture ;
3. le cas où un CLI est absent ou échoue : message lisible dans la bulle ;
4. `GET /api/agent/roster` avec les trois dos et leur disponibilité ;
5. le réglage d'attribution dans Settings.

`npx vitest run` reste vert, aucune erreur de console, et la position de chaque personnage
mesurée dans le cadre à 1440×900, 1880×790 et 1280×620.

## Rapport

Fichiers créés, sorties brutes des CLI, captures, et une section **« ce que je n'ai pas fait,
et pourquoi »**. En particulier : si une sous-commande attendue n'existe pas, c'est là qu'elle
se dit.
