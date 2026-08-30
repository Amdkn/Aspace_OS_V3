# Bascule Claude Code → OpenRouter

Phase d'onboarding : sortir de `MiniMax-M3[1m]` et passer Claude Code sur
OpenRouter, avec des modèles dont la **sortie reste sous 1 $/M**.

## Pourquoi ça marche sans proxy

OpenRouter expose une **Anthropic Skin** : un endpoint qui parle nativement
l'API Messages d'Anthropic. Claude Code s'y branche en direct — ni OmniRoute,
ni 9Router, ni `y-router` dans le chemin. Les blocs de raisonnement étendu et
l'usage d'outils passent tels quels.

## Les trois gestes

### 1. Générer la clé — c'est vous qui la créez

Sur <https://openrouter.ai/settings/keys>, créer une clé `sk-or-v1-…`.
Elle n'a pas à transiter par une conversation, un fichier de travail ou un log.

### 2. Fermer Claude Code

**Non négociable.** CC réécrit `~/.claude/settings.json` en fin de session : une
édition à chaud est écrasée sans avertissement. Le script refusera de le
signaler à votre place — il ne peut pas savoir que CC tourne.

### 3. Lancer le script

```bash
python "C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/openrouter/bascule_openrouter.py"
```

La clé est demandée en **saisie masquée** (`getpass`). Elle n'est jamais passée
en argument de ligne de commande, donc jamais dans l'historique du shell.

Le script sauvegarde `settings.json` dans `backups/` avant toute écriture.

## Ce que le script change

| Variable | Avant | Après |
|---|---|---|
| `ANTHROPIC_BASE_URL` | `https://api.minimax.io/anthropic` | `https://openrouter.ai/api` |
| `ANTHROPIC_AUTH_TOKEN` | *(absent)* | la clé `sk-or-v1-…` |
| `ANTHROPIC_API_KEY` | `sk-cp-…` (MiniMax) | `""` **vide, volontairement** |
| `ANTHROPIC_MODEL` | `MiniMax-M3[1m]` | `deepseek/deepseek-v4-flash` |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | `MiniMax-M3[1m]` | `deepseek/deepseek-v4-flash` |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | `MiniMax-M3[1m]` | `deepseek/deepseek-v4-flash` |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | `MiniMax-M3[1m]` | `inclusionai/ling-3.0-flash` |
| `ANTHROPIC_SMALL_FAST_MODEL` | `MiniMax-M3[1m]` | `inclusionai/ling-3.0-flash` |

Tout le reste — 15 plugins, 32 permissions, les clés Supabase / Vercel /
Composio, `effortLevel`, `enableWorkflows`, les MCP — est préservé à
l'identique. Vérifié par simulation à blanc le 2026-08-21.

## Les modèles retenus

Mesurés sur le catalogue OpenRouter le 2026-08-21 (`/api/v1/models`, endpoint
public). **Tous portent `tools` dans `supported_parameters`** — sans quoi Claude
Code ne peut rien faire.

**Profil CACHE**, arrêté le 2026-08-21 **après mesure au banc**.

| Slot | Modèle | Entrée $/M | Cache lu $/M | Gain | Sortie $/M | Contexte |
|---|---|---|---|---|---|---|
| principal · Opus · Sonnet | `xiaomi/mimo-v2.5` | 0,140 | **0,0028** | **×50** | 0,28 | 1 050 000 |
| Haiku · small-fast | `inclusionai/ling-3.0-flash` | 0,021 | 0,0042 | ×5 | 0,06 | 262 144 |

Repli éprouvé si MiMo déraille en usage réel : `deepseek/deepseek-v4-flash`
(0,081 / 0,0162 / 0,16 / 1 048 576). Il a passé le même banc **3/3** et a tourné
en session le 2026-08-21.

### Le banc, et pourquoi il fait foi

`banc_outils.py` frappe l'Anthropic Skin — le chemin exact de CC. Résultat du
2026-08-21 :

| Modèle | Émission `tool_use` | Boucle `tool_result` | Cache lu | Verdict |
|---|---|---|---|---|
| `xiaomi/mimo-v2.5` | OK | OK | OK | **3/3** |
| `deepseek/deepseek-v4-flash` | OK | OK | OK | **3/3** |

MiMo était écarté du premier profil pour un seul motif : fiabilité en usage
d'outils non mesurée. La mesure l'a levé. **C'est la seule raison légitime de
promouvoir un modèle** — pas son prix affiché.

```bash
python banc_outils.py xiaomi/mimo-v2.5 deepseek/deepseek-v4-flash
```

Rejouer ce banc avant toute promotion future. Un modèle qui échoue l'épreuve 1
ou 2 ne pilote pas Claude Code, quel que soit son tarif.

## Le cache lu compte plus que le prix affiché

Le prix brut est un **mauvais prédicteur** du coût réel en session Claude Code.
À chaque tour, CC renvoie le même préfixe : les deux `CLAUDE.md` plus
`MEMORY.md` pèsent **36 040 octets, ~10 000 tokens**, avant le prompt système,
les schémas d'outils et l'historique. C'est du texte identique octet pour octet.

Sur les deux modèles retenus, **l'écriture de cache est gratuite** — le cache est
automatique, il n'y a aucun `cache_control` à poser. L'économie arrive sans
configuration.

Simulation, 50 tours, ~40 K tokens d'entrée par tour, 1,5 K de sortie :

| | sans cache | 85 % de cache | 95 % de cache |
|---|---|---|---|
| `deepseek/deepseek-v4-flash` | $0,174 | $0,064 | $0,051 |
| `xiaomi/mimo-v2.5` | $0,301 | $0,068 | **$0,040** |

`xiaomi/mimo-v2.5` est **1,7× plus cher au prix affiché et devient le moins cher
dès 95 % de réutilisation** (cache lu ×50, à $0,0028/M, contexte 1 050 000).
Écarté du profil prudent uniquement parce que sa fiabilité en usage d'outils
n'est pas mesurée. **À tester sur une tâche jetable avant de le promouvoir** —
c'est le gain le plus important encore sur la table.

Écarté aussi : `openai/gpt-oss-120b`, dont le cache lu coûte exactement le prix
de l'entrée ($0,030 = $0,030). Bénéfice nul. Choisir un modèle sur son prix
d'entrée sans regarder son prix de cache conduit au mauvais choix.

## Les variantes `:batch`

Remise de **50 % exactement**, uniforme sur tout le catalogue :

| Modèle | Standard | `:batch` |
|---|---|---|
| `openai/gpt-5.6-luna` | $0,20 / $1,20 | $0,10 / **$0,60** |
| `anthropic/claude-opus-5` | $5,00 / $25,00 | $2,50 / **$12,50** |
| `google/gemini-3.7-flash` | $0,375 / $1,88 | $0,188 / **$0,94** |

La contrepartie est l'asynchronisme : soumission d'un lot, traitement quand le
fournisseur a de la capacité, récupération jusqu'à 24 h plus tard.
**Inutilisable pour Claude Code interactif** — mais adapté à une vague de revue
de corpus, qui n'a aucune raison d'être synchrone.

## Quatre pièges

**L'URL n'a pas de `/v1`.** C'est `https://openrouter.ai/api`. Claude Code
ajoute `/v1/messages` lui-même ; écrire `/api/v1` produit un appel à
`/api/v1/v1/messages` et un 404. Plusieurs tutoriels donnent encore l'ancienne
forme.

**`ANTHROPIC_API_KEY` doit être vide, pas supprimé.** OpenRouter authentifie
par bearer, donc via `ANTHROPIC_AUTH_TOKEN`. `ANTHROPIC_API_KEY` part en header
`x-api-key` et serait traité comme une credential Anthropic directe — les deux
en même temps se contredisent.

**Le login en cache écrase tout.** Si un compte Anthropic a déjà servi sur ce
poste, faire `/logout` une fois puis relancer. Sinon les variables sont ignorées
et on obtient des « model not found » qui font accuser le mauvais coupable.

**Les échecs comptent dans le quota journalier.** Une boucle de retry naïve peut
brûler une journée de quota en moins d'une minute. Voir la table des paliers
dans le concept OKF `integrations/routeurs-llm-locaux-autostart.md`.

## Revenir en arrière

```bash
python "C:/Users/amado/ASpace_OS_V3/00_Amadeus/20_Harness/openrouter/bascule_openrouter.py" --revert
```

Restaure le dernier fichier de `backups/`. Relancer CC ensuite.

## Vérifier le palier journalier réel

Une fois la clé en main, depuis un shell (la clé ne passe pas par CC) :

```bash
curl -s -H "Authorization: Bearer $OPENROUTER_KEY" https://openrouter.ai/api/v1/auth/key
```

La réponse donne le quota et la limite. Attendu si les 10 $ ont bien été
déposés une fois : palier **1 000 requêtes/jour** au lieu de 50. Le palier est
acquis à vie, pas conditionné au solde restant.
