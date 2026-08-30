# AGENT-A — Le socle agnostique

Lis `CONTRAT.md` dans ce même dossier. Il fait partie de ce brief et prime sur lui.

Ton rapport : `RAPPORT_AGENT_A.md`, à côté de ce brief.

---

## Ce qu'on construit, et pourquoi

Coach OS n'a **aucun** appel à un modèle aujourd'hui : la section « Jarvis » du Dashboard est
une maquette, et il n'y a ni dossier `api/`, ni serveur. C'est une application Vite purement
cliente, déployée en statique sur Vercel.

Tu poses la moitié serveur : une fonction sans serveur qui parle aux modèles, avec un
**registre de fournisseurs** derrière une seule interface. L'intention est nommée : demain on
branchera Hermes Agent, Claude Code, les SDK OpenAI et Anthropic, l'ADK Gemini. Aucun de ces
branchements ne doit obliger à rouvrir le reste du code — ils se posent dans le registre.

**La clé ne doit jamais atteindre le navigateur.** C'est la raison d'être de cette fonction :
un appel direct depuis le client exposerait la clé à quiconque ouvre l'inspecteur, et serait
de toute façon bloqué par CORS. Ce point n'est pas négociable, y compris « juste pour tester ».

## Ton périmètre exclusif

```
api/**                    (à créer)
vercel.json               (à créer)
.env.example              (à créer ou compléter)
```

Rien d'autre. **En particulier : rien dans `src/`** — c'est le périmètre d'AGENT-B, qui
travaille en même temps que toi. Et **rien dans `package.json` ni dans les verrous** : tout
est déjà installé et vérifié, y toucher recasserait le déploiement Vercel, qui vient d'être
réparé sur ce point précis.

## Le travail

### 1 · La fonction

`api/chat.ts`, une fonction sans serveur Vercel (runtime Node). Elle applique le contrat :
elle lit `messages`, choisit le fournisseur, déclare les outils, et rend
`toUIMessageStreamResponse()`.

Ajoute un `vercel.json` si le projet en a besoin pour servir `api/` à côté d'un build Vite
statique — vérifie ce qui est nécessaire, n'ajoute pas de configuration décorative.

### 2 · Le registre de fournisseurs

Un module à part, `api/_agent/providers.ts` : une table `id → fabrique de modèle`, plus une
fonction qui dit lesquels sont **disponibles** (clé présente). Le tableau des quatre est dans
`CONTRAT.md`, avec le détail qui compte : MiniMax passe par le fournisseur Anthropic muni
d'une `baseURL`.

Sépare bien deux choses : *quels fournisseurs existent* (statique) et *lesquels sont
utilisables ici et maintenant* (dépend de l'environnement). Expose la seconde par
`GET /api/agent/providers`, pour que l'interface puisse afficher le choix sans deviner.

### 3 · Les outils

`api/_agent/tools.ts` : les cinq outils du contrat, déclarés avec leur schéma de paramètres.
**Déclarés seulement** — pas d'`execute` côté serveur : c'est le client qui agit sur le
bureau. Un outil déclaré sans `execute` est exactement ce que le SDK attend pour un tour de
boucle côté client.

### 4 · L'invite système

`api/_agent/prompt.ts`. L'agent est le personnage de Coach OS, pas un assistant générique.
Il connaît le bureau, il tutoie, il répond court. Il sait qu'il peut ouvrir des apps et
naviguer — et qu'il vaut mieux *faire* que décrire comment faire.

Prévois que l'appelant puisse ajouter des instructions (champ `system` du contrat) sans
écraser la base.

### 5 · Le développement local

Vite ne sert pas `api/`. Trouve la manière la plus simple de rendre `/api/chat` joignable en
`npm run dev` — un plugin Vite qui monte la fonction en middleware est probablement le
chemin le plus court, `vercel dev` en est un autre. **Ce qui compte : qu'AGENT-B, qui ne
touche pas à ton périmètre, puisse voir son personnage répondre en local.** Documente la
commande exacte dans ton rapport.

Pose la clé MiniMax dans `.env.local` (jamais versionné) en la lisant depuis :

```bash
python -c "import json;print(json.load(open('C:/Users/amado/.claude/settings.json',encoding='utf-8'))['env']['ANTHROPIC_API_KEY'])"
```

Et écris un `.env.example` avec les quatre variables, **valeurs vides**.

## Preuve attendue

Le code qui compile ne prouve rien. Ce qui prouve :

```bash
curl -s -X POST http://localhost:5173/api/chat \
  -H 'Content-Type: application/json' \
  -d '{"messages":[{"role":"user","parts":[{"type":"text","text":"Dis PONG et rien d autre"}]}]}'
```

doit rendre un flux qui contient `PONG`. Colle la sortie réelle dans ton rapport.

Prouve aussi les deux cas d'erreur, parce qu'ils comptent autant que le cas heureux :

- un `provider` inconnu → 400 avec un message lisible ;
- un fournisseur sans clé → 400 qui le dit, **et le service reste debout** pour les autres.

Enfin : `GET /api/agent/providers` doit lister `minimax` disponible et les trois autres
indisponibles, puisque seule la clé MiniMax est posée.

## Rapport

Structure libre, mais il contient : la commande exacte de lancement local, la sortie brute
des trois `curl`, la liste des fichiers créés, et une section **« ce que je n'ai pas fait, et
pourquoi »**. Un manque annoncé coûte moins cher qu'un manque découvert.
