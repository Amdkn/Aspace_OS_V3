# V3-INIT — Bootstrap A'Space OS V3 sur le VPS (H24/7)

> Ce guide explique comment cloner V3 sur le VPS, câbler la config Claude Code **sans jamais
> committer de secret**, lancer le moteur WF0 Citadel, et raccorder les MCPs.
> Doctrine : **No secrets in the repo.** Toute clé/token est fournie par l'opérateur à l'exécution
> (variables d'environnement User scope), jamais dans un fichier suivi par git.

---

## 0. Pré-requis

| Outil | Version min | Vérif |
|---|---|---|
| Node.js | ≥ 22 | `node -v` |
| Python | ≥ 3.10 | `python3 --version` |
| git | ≥ 2.40 | `git --version` |
| Claude Code CLI | latest | `claude --version` |

## 1. Cloner

```bash
git clone <REMOTE_URL> aspace-os-v3
cd aspace-os-v3
bash scripts/install.sh
```

`install.sh` : vérifie Node/Python, scaffold `50_Claude_Code_Config/settings.json` depuis un
**template placeholder** (aucun token réel), puis lance `scripts/verify_structure.sh`.

## 2. Câbler `.claude/settings.json` (NON commité)

Le repo ne contient **jamais** `settings.json` (voir `.gitignore`). L'opérateur le crée localement :

```bash
# Le harness Claude Code lit ~/.claude/settings.json (User scope).
# install.sh en génère un squelette dans 50_Claude_Code_Config/settings.example.json.
cp 50_Claude_Code_Config/settings.example.json ~/.claude/settings.json
$EDITOR ~/.claude/settings.json   # y coller VOS tokens (jamais dans le repo)
```

Les skills / rules / agents / hooks sont, eux, versionnés dans `50_Claude_Code_Config/` :
```bash
mkdir -p ~/.claude
cp -r 50_Claude_Code_Config/skills ~/.claude/skills
cp -r 50_Claude_Code_Config/rules  ~/.claude/rules
cp -r 50_Claude_Code_Config/agents ~/.claude/agents
cp -r 50_Claude_Code_Config/hooks  ~/.claude/hooks
```

## 3. Variables d'environnement (Test Key Pragma — User scope, jamais dans le repo)

Exportez vos propres valeurs (exemples de clés attendues par la stack) :

```bash
export SUPABASE_URL="https://<project>.supabase.co"      # set your own
export SUPABASE_ANON_KEY="<your-anon-key>"               # set your own
export SUPABASE_SERVICE_ROLE_KEY="<your-service-key>"    # set your own
export AIRTABLE_BEARER_AUTH="<your-airtable-pat>"        # set your own
export GH_TOKEN="<your-github-pat>"                      # set your own
export VERCEL_TOKEN="<your-vercel-token>"                # set your own
export HOSTINGER_API_TOKEN="<your-hostinger-token>"      # set your own
```

> Rotation post-usage recommandée (doctrine "Test Key Pragma" : share → set → test → rotate).

## 4. Lancer le moteur WF0 Citadel (Spock)

```bash
cd 60_Citadel
cat README.md          # runbook de l'orchestrateur
# entrypoint typique (voir README Citadel pour la commande exacte) :
python3 cron/<entrypoint>.py
```

## 5. Câbler les MCPs

Les serveurs MCP (Supabase, Airtable, Hostinger DNS, Telegram, etc.) se déclarent dans
`~/.claude/settings.json` (ou `.mcp.json`) — **avec vos propres tokens en variables d'env**.
Aucun token n'est présent dans ce repo. Redémarrer Claude Code après ajout (le registre d'outils
est statique au boot).

## 6. Vérifier

```bash
bash scripts/verify_structure.sh   # arborescence OK
grep -rIl "sk-\|sbp_\|SECRET" .    # doit ne rien renvoyer (0 secret)
```

---

**Rappel sobriété (ADR-SOBER-002)** : V3 = V2 + ajouts. On n'écrase pas le canon, on ne re-dérive pas.
Le fondateur `AGENTS.md` est immuable.
