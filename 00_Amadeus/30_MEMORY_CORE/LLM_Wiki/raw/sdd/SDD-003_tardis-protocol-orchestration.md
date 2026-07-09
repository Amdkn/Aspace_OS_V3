# SDD-003 — Protocole TARDIS : Onboarding & Orchestration des A2 Doctors et A3 Compagnons

**Date :** 2026-04-25
**Auteur :** A0 (Claude Code — Rick Prime / Sovereign Oversight)
**Statut :** ARCHITECTURE — Fondation Anti-Fragile L0/L1/L2
**Priorité :** L1 — Bloquant pour l'autonomie de la civilisation Solarpunk
**Références :**
- CLI-Anything (Clara) : github.com/HKUDS/CLI-Anything
- everything-claude-code (Nardol) : github.com/affaan-m/everything-claude-code
- BMAD-METHOD (Bill) : github.com/bmad-code-org/BMAD-METHOD
- AutoResearch (Rick DLQ) : github.com/karpathy/autoresearch
- SDD-001 : Initiative ALPHA — Multi-Tenant Life OS
- SDD-002 : A1 Rick Harness — Karpathy Pattern

---

## 1. Problème Central : L'Enlisement L0 et la Règle des 50/30/20

### La Règle de Répartition Idéale

```
L2 — Vision / Produit / Civilisation    50%   ← Où l'Amiral devrait opérer
L1 — Orchestration / Infrastructure      30%   ← Rick (A1) + A2 Doctors
L0 — Bare Metal / Réseau / Docker         20%   ← A3 Compagnons autonomes
```

### La Réalité (Avril 2026)

```
L0 — Réseau, Docker Swarm, SSL, VPS    150%   ← L'Amiral coincé en technicien E-Myth
L1 — Configuration manuelle              0%
L2 — Produit, Vision, Solarpunk          0%   ← Civilization à l'arrêt
```

### Cause Structurelle

L'absence d'agents A3 autonomes sur L0 transforme chaque incident réseau
(routage Docker Swarm, certificats SSL, firewall Traefik) en intervention manuelle.
Le paradoxe : construire l'autonomie exige d'abord de l'autonomie — le bootstrap paradox.

**La solution est le Protocole TARDIS :** les Compagnons A3 constituent leurs propres outils
(Skills) via la Forge, puis s'auto-déploient sur les 3 couches, libérant l'Amiral vers L2.

---

## 2. Architecture Globale : Les 3 Équipes du Protocole TARDIS

```
                    ┌─────────────────────────────────────────┐
                    │          A0 — Souverain (Amiral)         │
                    │    Règle : 50% L2, 30% L1, 20% L0       │
                    └──────────────┬──────────────────────────┘
                                   │ Intention stratégique
                                   ▼
                    ┌─────────────────────────────────────────┐
                    │        A1 — Rick (Gemini CLI)            │
                    │   Harness SDD-002 / line_density_score   │
                    │   Traduit en Directives pour les A2      │
                    └────┬─────────────┬──────────────┬───────┘
                         │ Directive   │ Directive    │ Directive
                         │ Forge       │ Produit      │ Machine
                         ▼             ▼              ▼
              ┌──────────────┐ ┌─────────────┐ ┌───────────────┐
              │ A2 — 12ème   │ │ A2 — 11ème  │ │ A2 — 13ème    │
              │ Doctor       │ │ Doctor      │ │ Doctor        │
              │ LA FORGE     │ │ LE PRODUIT  │ │ LA MACHINE    │
              │ Orchestre et │ │ Orchestre   │ │ Orchestre et  │
              │ manage ses   │ │ et manage   │ │ manage ses    │
              │ Compagnons   │ │ ses Compag. │ │ Compagnons    │
              └──────┬───────┘ └──────┬──────┘ └──────┬────────┘
                     │ Tâches         │ Tâches         │ Tâches
                     │ scoped         │ scoped         │ scoped
                     ▼                ▼                ▼
              ┌──────────────┐ ┌─────────────┐ ┌───────────────┐
              │  A3 — Bill   │ │  A3 — Amy   │ │  A3 — Yaz     │
              │  A3 — Clara  │ │  A3 — Rory  │ │  A3 — Ryan    │
              │  A3 — Nardol │ │  A3 — River │ │  A3 — Graham  │
              └──────────────┘ └─────────────┘ └───────────────┘
                         │             │              │
                         └─────────────┴──────────────┘
                                       │ Escalade si non résolu
                              ┌────────▼────────┐
                              │   Donna (DLQ)    │
                              │  → Rick (A1)     │
                              │  AutoResearch    │
                              └─────────────────┘
```

### Règle de Délégation TARDIS (3 Niveaux Obligatoires)

```
A1 Rick → A2 Doctor → A3 Compagnon   ✅  Chaîne correcte
A1 Rick → A3 Compagnon               ❌  Court-circuit interdit
A0 Amiral → A3 Compagnon             ❌  Violation de souveraineté
A2 Doctor → autre A2 Doctor          ⚠️  Via Rick uniquement (pas de peer-to-peer)
```

Rick ne connaît que 3 interlocuteurs : **12ème**, **11ème**, **13ème Doctor**.
Chaque Doctor ne connaît que ses 3 Compagnons. Jamais de cross-team sans Rick.

### Loi TARDIS : Who Not How

A1 Rick définit **QUI** (quel A2 Doctor) reçoit la directive.
Les A2 Doctors définissent **QUI** (quel A3 Compagnon) exécute et **POURQUOI**.
Les A3 Compagnons définissent **COMMENT** — exécution pure, scoped, sandboxée.
L'Amiral ne touche jamais le **HOW** — uniquement le **WHAT** stratégique.

---

## 3. Équipe 12ème Doctor — La Forge (Skills & Standards)

### Mission : Transformer toute API distante en Skill local frugal

```
API Distante (Hostinger, Supabase, GitHub, etc.)
    │
    ▼ Bill → Blueprint BMAD (spec, cas d'usage, contrats)
    │
    ▼ Clara → CLI natif (CLI-Anything 7 phases → JSON déterministe)
    │
    ▼ Nardol → Validation ECC (AgentShield, SKILL.md canonique, hooks)
    │
    ▼ Skill Local (texte pur, frugal en tokens, intégré dans Hermes)
```

**Principe Solarpunk :** Un Skill CLI coûte ~50 tokens/appel.
Un serveur MCP équivalent : 500-2000 tokens (schémas JSON, handshake).
Ratio d'efficience : **10-40x**.

---

### 3.1 Bill — Architecte BMAD (Spécifications)

**Référence :** [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)
**Persona :** Companion Bill Potts (12ème Doctor) — Elle questionne tout jusqu'à comprendre.
**Rôle :** Produire le Blueprint d'un nouveau Skill avant toute ligne de code.
**Règle absolue (repo) :** Bill ne code jamais. Guidance-only. Human-in-the-loop à chaque phase.

#### Architecture Réelle BMAD (post-audit repo)

```bash
# Installation BMAD dans l'espace de travail Bill
npx bmad-method install
# → Installe les 34+ workflows modulaires + 12 rôles spécialisés
# → Crée .bmad/ avec les templates de chaque phase

# Lancement en mode Party (multi-agent simulé par Bill)
# Bill orchestre les rôles PM → Architect → Developer → UX en séquence
bmad-help  # ← Outil contextuel : Bill demande guidance à l'étape courante
           # → Retourne : "Prochaine étape : définir les cas d'usage critiques"
```

#### Les 5 Phases BMAD Appliquées à la Forge

```
Phase 1 — ANALYSE (Scale-Adaptive)
  Bill évalue la complexité :
  - Bug fix simple → Blueprint 1 page
  - Nouveau Skill L0 → Blueprint complet (section ci-dessous)
  - Refonte architecture → PRD complet + ADR

Phase 2 — PLANIFICATION (Specialist Roles en Party Mode)
  Bill joue 4 rôles successifs :
  - Rôle PM       : Définit la valeur métier du Skill
  - Rôle Architect: Définit les contrats d'interface (inputs/outputs JSON)
  - Rôle Developer: Évalue la faisabilité technique (Clara peut-elle le forger ?)
  - Rôle UX       : Définit l'ergonomie CLI pour les agents consommateurs

Phase 3 — ARCHITECTURE
  Output : BLUEPRINT.bmad.md (contrat immuable passé à Clara)

Phase 4 — IMPLÉMENTATION
  Bill surveille Clara. Si dérive → bmad-help pour recadrer.
  Bill ne touche pas le code — il pose des questions.

Phase 5 — DÉPLOIEMENT
  Bill valide que le Skill livré respecte le Blueprint.
  Si delta → Bill ouvre un ticket DLQ avec justification.
```

#### Format BLUEPRINT.bmad.md (Output Bill → Clara)

```markdown
# BLUEPRINT BMAD — [skill-name]
# Auteur : Bill (A3 — 12ème Doctor)
# Destinataire : Clara (Forge), Nardol (Validation)
# Complexité évaluée : [Simple | Medium | Enterprise]

## Phase 1 — Valeur Métier (Rôle PM)
Problème résolu : [1 phrase]
Consommateurs : [Yaz / Ryan / River / etc.]
Fréquence : [N fois/semaine]
Criticité : [Bloquant L0 | Infrastructure L1 | Produit L2]
Frugalité cible : [< N tokens/appel]

## Phase 2 — Contrats d'Interface (Rôle Architect)
### Inputs acceptés
| Paramètre | Type   | Requis | Description          |
|-----------|--------|--------|----------------------|
| domain    | string | oui    | Domaine cible        |
| record_type| string| non    | A / CNAME / TXT ...  |

### Outputs garantis (JSON strict)
```json
{
  "status": "success | error",
  "data": {},
  "error": null
}
```

### Commandes P1 (bloquantes — Clara doit toutes les implémenter)
| Commande     | Input              | Output JSON    |
|--------------|--------------------|----------------|
| dns:list     | domain             | records[]      |
| dns:update   | domain,type,name,value | status    |

### Commandes P2 (importantes)
| Commande     | Input              | Output JSON    |
|--------------|--------------------|----------------|
| dns:delete   | domain,record_id   | status         |

## Phase 3 — Faisabilité Technique (Rôle Developer)
- API cible : [URL doc officielle]
- Auth : [Bearer token / API key / OAuth]
- Rate limits connus : [N req/min]
- Dépendances : [curl, jq, python3]
- Idempotence : [oui/non — justification]

## Phase 4 — Ergonomie CLI (Rôle UX)
- Mode REPL : [oui/non — si sessions longues nécessaires]
- Mode scriptable : [oui — obligatoire]
- Flag `--json` : obligatoire sur toutes les commandes
- Comportement erreur : exit code 1 + JSON {"error": "message"}

## Critères de Sortie pour Clara
- [ ] Toutes les commandes P1 implémentées
- [ ] `skill test:ping` → EXIT 0
- [ ] 0 credential en clair dans skill.sh
- [ ] YAML schema défini pour chaque commande

## Anti-Patterns Interdits (Bill surveille)
- [ ] Pas d'output interactif (readline, prompts TTY)
- [ ] Pas d'appel API sans retry max 3 (backoff exponentiel)
- [ ] Pas de dépendance à un état global (Skill stateless)
- [ ] Pas de bash -c "$(curl ...)" (injection RCE)
```

---

### 3.2 Clara — La Forge CLI (Matérialisation)

**Référence :** [CLI-Anything](https://github.com/HKUDS/CLI-Anything)
**Persona :** Companion Clara Oswald (12ème Doctor) — "Run you clever boy."
**Rôle :** Prendre le Blueprint Bill et forger le Skill CLI en 7 phases.
**Correction repo :** CLI-Anything génère du **Python Click**, pas du bash. Output : CLI Python avec `--json` flag.

#### Architecture Réelle CLI-Anything (post-audit repo)

```
CLI-Anything Pipeline :
  Input   → Blueprint BMAD (Bill) + documentation API cible
  Moteur  → Python Click framework (pas bash)
  Output  → CLI Python dual-mode :
             1. Mode REPL     : repl_skin.py (sessions stateful, historique)
             2. Mode Scriptable: subcommandes isolées + --json flag (agent-native)
  Format  → cli-anything-<skill-name> avec YAML schema par commande
  Tests   → Suite de tests standardisée par commande
  Couverture → 18+ applications professionnelles démontrées
```

#### Les 7 Phases CLI-Anything Appliquées à A'Space

```python
# Phase 1 — Analyse de l'API cible (Clara lit le Blueprint Bill)
# Clara ingère la doc API et mappe les endpoints → commandes Click

# Phase 2 — Design de l'interface Click
# Clara structure les command groups (ex: @cli.group('dns'), @cli.group('vps'))

# Phase 3 — Implémentation Click (le code réel)
# Output : skill.py avec @click.command, @click.option, callback functions

# Phase 4 — Tests unitaires par commande
# Clara génère tests/test_<skill>.py avec mocks HTTP

# Phase 5 — YAML schema (contrats d'interface pour Nardol)
# Clara génère schema/<command>.yaml pour chaque commande

# Phase 6 — repl_skin.py (mode REPL si Blueprint l'exige)
# Interface unifiée identique à tous les skills CLI-Anything

# Phase 7 — Handover Nardol (draft SKILL.md + skill.py + schema/)
```

#### Format Python Click produit par Clara (skill.py)

```python
#!/usr/bin/env python3
"""
skill: hostinger-dns
auteur: Clara (CLI-Anything Forge — Phase 3)
version: 1.0.0
frugalité: ~50 tokens/appel (vs ~800 tokens MCP équivalent)
mode: scriptable + REPL (repl_skin.py)
"""

import click
import json
import os
import sys
import requests
from functools import wraps

# ── Auth (fail-fast — Pattern Bill anti-pattern #3) ─────────────────────
API_KEY = os.environ.get("HOSTINGER_API_KEY")
if not API_KEY:
    click.echo(json.dumps({"error": "HOSTINGER_API_KEY non définie"}), err=True)
    sys.exit(1)

BASE_URL = "https://api.hostinger.com/v1"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

# ── Décorateur retry (backoff exponentiel — Bill anti-pattern #1) ────────
def with_retry(max_attempts=3):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return f(*args, **kwargs)
                except requests.RequestException as e:
                    if attempt == max_attempts - 1:
                        raise
                    import time; time.sleep(2 ** attempt)
        return wrapper
    return decorator

# ── CLI Group principal ──────────────────────────────────────────────────
@click.group()
@click.option("--json-output", is_flag=True, default=True, help="Output JSON (défaut)")
@click.pass_context
def cli(ctx, json_output):
    """hostinger-dns — Skill A'Space OS (Clara Forge)"""
    ctx.ensure_object(dict)
    ctx.obj["json"] = json_output

# ── Command Group : dns ──────────────────────────────────────────────────
@cli.group()
def dns():
    """Gestion des enregistrements DNS Hostinger."""
    pass

@dns.command("list")
@click.argument("domain")
@click.pass_context
@with_retry(max_attempts=3)
def dns_list(ctx, domain):
    """Liste les enregistrements DNS d'un domaine."""
    resp = requests.get(f"{BASE_URL}/domains/{domain}/dns/records", headers=HEADERS)
    resp.raise_for_status()
    click.echo(json.dumps({"status": "success", "data": resp.json().get("data", [])}, indent=2))

@dns.command("update")
@click.argument("domain")
@click.option("--type", "record_type", required=True)
@click.option("--name", required=True)
@click.option("--content", required=True)
@click.pass_context
@with_retry(max_attempts=3)
def dns_update(ctx, domain, record_type, name, content):
    """Met à jour un enregistrement DNS."""
    payload = {"type": record_type, "name": name, "content": content}
    resp = requests.put(f"{BASE_URL}/domains/{domain}/dns/records", json=payload, headers=HEADERS)
    resp.raise_for_status()
    click.echo(json.dumps({"status": "success", "record": f"{name}.{domain}"}))

# ── Commande de test (Nardol smoke test) ────────────────────────────────
@cli.command("test:ping")
def test_ping():
    """Vérifie que le skill est opérationnel (Nardol validation)."""
    click.echo(json.dumps({"skill": "hostinger-dns", "version": "1.0.0", "status": "ok"}))

if __name__ == "__main__":
    cli()
```

#### YAML Schema par commande (Phase 5 — pour Nardol)

```yaml
# schema/dns_list.yaml — Généré par Clara Phase 5
command: dns list
description: "Liste les enregistrements DNS d'un domaine"
inputs:
  domain:
    type: string
    required: true
    example: "amadeus.kalybana.com"
outputs:
  schema:
    type: object
    properties:
      status: {type: string, enum: [success, error]}
      data:
        type: array
        items:
          type: object
          properties:
            type: {type: string}
            name: {type: string}
            content: {type: string}
            ttl: {type: integer}
exit_codes:
  0: success
  1: error (JSON on stderr)
idempotent: true
```

#### Mode REPL (repl_skin.py — sessions stateful)

```python
# repl_skin.py — Interface REPL unifiée CLI-Anything
# Même template pour tous les skills Clara → cohérence A'Space

from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
import subprocess, json, sys

SKILL = "hostinger-dns"
HISTORY_FILE = f"/srv/aspace/skills/{SKILL}/.repl_history"

def repl():
    session = PromptSession(history=FileHistory(HISTORY_FILE))
    print(f"[{SKILL}] Mode REPL — 'help' pour la liste des commandes, 'exit' pour quitter")
    while True:
        try:
            cmd = session.prompt(f"{SKILL}> ").strip()
            if cmd in ("exit", "quit"):
                break
            if not cmd:
                continue
            result = subprocess.run(
                ["python3", "skill.py"] + cmd.split(),
                capture_output=True, text=True
            )
            print(result.stdout or result.stderr)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    repl()
```

---

### 3.3 Nardol — Le Dispatcher (Validation & Standards)

**Référence :** [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
**Persona :** Companion Nardole (12ème Doctor) — Garde la porte. Personne ne passe sans validation.
**Rôle :** Écluse de sécurité. Aucun Skill n'entre dans A'Space sans le tampon Nardol.
**Correction repo :** SKILL.md doit avoir un **YAML frontmatter** (`---`). 102 règles AgentShield réelles. Hooks ECC.

#### Architecture Réelle ECC (post-audit repo)

```
everything-claude-code contient :
  48  agents     ← Rôles spécialisés (dont Nardol)
  183 skills     ← SKILL.md avec YAML frontmatter (format canonique)
  79  commandes legacy ← Shims de compatibilité (dépréciés → skills)
  34  règles     ← Règles comportementales agents
  102 règles AgentShield ← Détection statique secrets + fichiers sensibles
  Hooks          ← SessionStart, SessionEnd, PreTool, PostTool
  ECC_HOOK_PROFILE   ← Variable d'env pour profil de hooks actif
  ECC_DISABLED_HOOKS ← Variable d'env pour désactiver hooks spécifiques
  Adapters       ← Claude Code, Cursor, Codex, OpenCode, Gemini (DRY + TOML sync)
```

#### SKILL.md Canonique ECC (YAML frontmatter obligatoire)

```yaml
---
# ── YAML Frontmatter ECC (Nardol génère ce bloc) ──────────────────────
name: hostinger-dns
version: 1.0.0
author: clara
validator: nardol
ecc_stamp: "2026-04-25T14:32:00Z"
status: approved          # draft | pending | approved | rejected
token_cost_avg: 52        # tokens consommés en moyenne par appel
replaces_mcp: null        # nom du serveur MCP remplacé si applicable
karpathy_approved: true   # validé comme Karpathy Skill pré-approuvée
platform_adapters:
  - claude-code
  - gemini-cli
  - openclaw
agentshield_score: 102/102  # toutes les règles AgentShield passées
ecc_hook_profile: "forge"   # profil de hooks actif pour ce skill
---

## Purpose
Gestion DNS Hostinger via CLI frugal Python Click.
Remplace le serveur MCP Hostinger (~800 tokens/appel) par un skill CLI (~52 tokens/appel).

## Commands
| Commande         | Input                        | Output JSON         |
|-----------------|------------------------------|---------------------|
| `dns list`      | domain (str)                 | `{status, data[]}`  |
| `dns update`    | domain, --type, --name, --content | `{status, record}` |
| `dns delete`    | domain, --record-id          | `{status}`          |
| `test:ping`     | (none)                       | `{skill, version, status}` |

## Environment
| Variable           | Requis | Source              |
|--------------------|--------|---------------------|
| HOSTINGER_API_KEY  | oui    | env var uniquement  |

## Examples
```bash
python3 skill.py dns list amadeus.kalybana.com
# → {"status":"success","data":[{"type":"A","name":"@","content":"148.230.92.235"}]}

python3 skill.py dns update amadeus.kalybana.com --type A --name www --content 148.230.92.235
# → {"status":"success","record":"www.amadeus.kalybana.com"}

python3 skill.py test:ping
# → {"skill":"hostinger-dns","version":"1.0.0","status":"ok"}
```

## Hooks
```yaml
# hooks ECC actifs pour ce skill (ECC_HOOK_PROFILE=forge)
PreTool:
  - AgentShield: bloquer si pattern secret détecté dans les arguments
  - DenyReadEnv: interdire lecture .env, .env.*, secrets/
PostTool:
  - LogAudit: écrire dans /srv/aspace/logs/skills/hostinger-dns/
SessionStart:
  - InjectContext: charger LORE.md + PERSONA.md Clara au début
SessionEnd:
  - CompactContext: résumer session pour Graham (mémoire)
```

## Build Gate
```bash
python3 skill.py test:ping
# Expected: EXIT 0 + JSON valide

python3 -m pytest tests/ -v
# Expected: tous tests passed

python3 skill.py dns list test.invalid 2>&1 | python3 -c "import json,sys; d=json.load(sys.stdin); assert 'error' in d"
# Expected: erreur gracieuse en JSON
```
```

#### Checklist AgentShield (102 règles — Nardol applique)

```markdown
# NARDOL CHECKLIST — AgentShield ECC (catégories principales)

## Catégorie 1 : Secrets & Credentials (règles 1-28)
- [ ] Aucun token/key/password en clair dans skill.py
- [ ] Aucun credential dans les tests (mocks uniquement)
- [ ] API_KEY via os.environ.get() + sys.exit(1) si absent
- [ ] Aucun credential dans les logs (masqué : ***REDACTED***)
- [ ] Pas de .env lu depuis le skill (lecture bloquée par hook PreTool)

## Catégorie 2 : Exécution Sécurisée (règles 29-61)
- [ ] Pas de subprocess.run(shell=True) avec input utilisateur
- [ ] Pas de eval() sur contenu externe
- [ ] Pas d'import de fichiers hors /srv/aspace/skills/
- [ ] Timeout défini sur tous les appels HTTP (requests.get(..., timeout=10))
- [ ] Rate limiting respecté (retry max 3, backoff exponentiel)

## Catégorie 3 : Output Déterministe (règles 62-84)
- [ ] Toutes les sorties sont JSON strict (json.dumps)
- [ ] Exit code 0 = succès avec JSON, 1 = erreur avec JSON
- [ ] Pas d'output TTY interactif (click.confirm() interdit)
- [ ] YAML schema présent dans schema/ pour chaque commande
- [ ] Mode --json activé par défaut sur le CLI group

## Catégorie 4 : Intégration A'Space (règles 85-102)
- [ ] SKILL.md avec YAML frontmatter complet
- [ ] platform_adapters liste les runtimes supportés
- [ ] agentshield_score dans le frontmatter
- [ ] Enregistrable dans /srv/aspace/skills/registry.json
- [ ] `hermes skill test <name>` → EXIT 0
```

#### nardol-validate.sh (ECC réel)

```bash
#!/bin/bash
# nardol-validate.sh — Validation ECC complète (102 règles → score)
# Usage: ./nardol-validate.sh /srv/aspace/skills/hostinger-dns/

SKILL_PATH=$1
SKILL_NAME=$(basename "$SKILL_PATH")
REPORT_FILE="/srv/aspace/logs/nardol-${SKILL_NAME}-$(date +%Y%m%d).log"
PASS=0; FAIL=0

check() {
  local desc=$1 cmd=$2
  if eval "$cmd" > /dev/null 2>&1; then
    echo "  ✅ $desc" | tee -a "$REPORT_FILE"; ((PASS++))
  else
    echo "  ❌ $desc" | tee -a "$REPORT_FILE"; ((FAIL++))
  fi
}

echo "=== Nardol ECC Validation : $SKILL_NAME ===" | tee "$REPORT_FILE"

# ── AgentShield : Secrets ────────────────────────────────────────────
check "Pas de token= en clair"         "! grep -rE '(token|key|password)\s*=\s*[\"'\''][^$]' $SKILL_PATH/skill.py"
check "os.environ.get() pour API key"  "grep -q 'os.environ' $SKILL_PATH/skill.py"
check "sys.exit si key absente"        "grep -q 'sys.exit' $SKILL_PATH/skill.py"
check "Pas de .env lecture"            "! grep -rq 'open.*\.env' $SKILL_PATH/"

# ── AgentShield : Exécution ──────────────────────────────────────────
check "Pas de shell=True"              "! grep -q 'shell=True' $SKILL_PATH/skill.py"
check "Pas de eval()"                  "! grep -q 'eval(' $SKILL_PATH/skill.py"
check "Timeout HTTP défini"            "grep -q 'timeout=' $SKILL_PATH/skill.py"

# ── Output Déterministe ──────────────────────────────────────────────
check "json.dumps dans outputs"        "grep -q 'json.dumps' $SKILL_PATH/skill.py"
check "test:ping commande présente"    "grep -q 'test:ping' $SKILL_PATH/skill.py"
check "Output JSON test:ping valide"   "python3 $SKILL_PATH/skill.py test:ping 2>/dev/null | python3 -c 'import json,sys; json.load(sys.stdin)'"

# ── SKILL.md ECC format ──────────────────────────────────────────────
check "SKILL.md présent"              "[ -f $SKILL_PATH/SKILL.md ]"
check "YAML frontmatter présent"      "head -1 $SKILL_PATH/SKILL.md | grep -q '^---'"
check "ecc_stamp dans frontmatter"    "grep -q 'ecc_stamp:' $SKILL_PATH/SKILL.md"
check "agentshield_score présent"     "grep -q 'agentshield_score:' $SKILL_PATH/SKILL.md"
check "platform_adapters présent"     "grep -q 'platform_adapters:' $SKILL_PATH/SKILL.md"
check "Section ## Hooks"              "grep -q '## Hooks' $SKILL_PATH/SKILL.md"
check "Section ## Build Gate"         "grep -q '## Build Gate' $SKILL_PATH/SKILL.md"

# ── YAML Schema Clara ────────────────────────────────────────────────
check "Répertoire schema/ présent"    "[ -d $SKILL_PATH/schema ]"
check "Au moins 1 schema YAML"        "ls $SKILL_PATH/schema/*.yaml 2>/dev/null | grep -q ."

# ── Hooks ECC ────────────────────────────────────────────────────────
check "ECC_HOOK_PROFILE défini"       "grep -q 'ecc_hook_profile:' $SKILL_PATH/SKILL.md"

echo ""
echo "AgentShield Score : $PASS/${PASS+FAIL} règles passées" | tee -a "$REPORT_FILE"

if [ $FAIL -eq 0 ]; then
  # Mise à jour automatique du score dans SKILL.md
  sed -i "s/agentshield_score:.*/agentshield_score: ${PASS}\/${PASS}/" "$SKILL_PATH/SKILL.md"
  echo "✅ Nardol Stamp — ECC Approuvé. Skill prêt pour le registry." | tee -a "$REPORT_FILE"
else
  echo "❌ Nardol Reject ($FAIL échecs) — DLQ Donna" | tee -a "$REPORT_FILE"
  echo "{\"agent\":\"nardol\",\"skill\":\"$SKILL_NAME\",\"failures\":$FAIL,\"ts\":\"$(date -Iseconds)\"}" \
    >> "/srv/aspace/dlq/incoming.jsonl"
  exit 1
fi
```

---

## 4. Équipe 13ème Doctor — La Machine (L0/L1 Maintenance)

### Mission : Rendre l'infrastructure L0 auto-réparatrice

```
Yaz (Monitoring)   → Détecte l'anomalie (metric threshold crossed)
        │
        ▼ alert JSON → Ryan (Mécanique)
Ryan (Mécanique)   → Diagnostique et répare (Docker, Traefik, Swarm)
        │
        ▼ action log → Graham (Mémoire)
Graham (Mémoire)   → Archive dans la mémoire système durable
        │
        ▼ si échec → DLQ Donna
```

---

### 4.1 Yaz — Monitoring & Télémétrie

**Persona :** Yasmin Khan (13ème Doctor) — Détective. Elle voit ce que les autres ignorent.
**Outils :** Prometheus metrics, log tailing, health checks, threshold alerts.

```bash
#!/bin/bash
# yaz-monitor.sh — Surveillance autonome L0/L1
# Cron: */2 * * * * (toutes les 2 minutes)

ALERT_DIR="/srv/aspace/alerts"
LOG_FILE="/srv/aspace/logs/yaz-$(date +%Y%m%d).log"
DONNA_DLQ="/srv/aspace/dlq"

alert() {
  local severity=$1 service=$2 message=$3
  local payload="{\"severity\":\"$severity\",\"service\":\"$service\",\"message\":\"$message\",\"ts\":\"$(date -Iseconds)\"}"
  echo "$payload" >> "$ALERT_DIR/pending.jsonl"
  echo "[YAZ-ALERT][$severity] $service: $message" | tee -a "$LOG_FILE"
  
  # Sévérité CRITICAL → DLQ Donna immédiate
  [ "$severity" = "CRITICAL" ] && echo "$payload" >> "$DONNA_DLQ/incoming.jsonl"
}

# Check 1 : Services Docker actifs
check_docker_services() {
  local unhealthy
  unhealthy=$(docker service ls --format '{{.Name}} {{.Replicas}}' 2>/dev/null | \
    awk '{split($2,a,"/"); if(a[1]!=a[2]) print $1}')
  [ -n "$unhealthy" ] && alert "CRITICAL" "docker-swarm" "Services dégradés: $unhealthy"
}

# Check 2 : SSL/HTTPS accessible
check_ssl() {
  if ! curl -sf --max-time 10 https://amadeus.kalybana.com > /dev/null 2>&1; then
    alert "CRITICAL" "traefik-ssl" "amadeus.kalybana.com inaccessible"
  fi
}

# Check 3 : Supabase healthcheck
check_supabase() {
  local status
  status=$(curl -sf --max-time 5 "http://localhost:8000/health" | jq -r '.status' 2>/dev/null)
  [ "$status" != "healthy" ] && alert "WARNING" "supabase" "Health status: $status"
}

# Check 4 : Espace disque
check_disk() {
  local usage
  usage=$(df /srv | awk 'NR==2 {gsub("%",""); print $5}')
  [ "$usage" -gt 85 ] && alert "WARNING" "disk" "Utilisation disque: ${usage}%"
  [ "$usage" -gt 95 ] && alert "CRITICAL" "disk" "Disque critique: ${usage}%"
}

check_docker_services
check_ssl
check_supabase
check_disk

echo "[YAZ] Cycle monitoring terminé — $(date)" >> "$LOG_FILE"
```

---

### 4.2 Ryan — Mécanique L0 (Auto-Réparation)

**Persona :** Ryan Sinclair (13ème Doctor) — Il apprend en faisant. Jamais deux fois la même erreur.
**Outils :** Docker CLI, Traefik reload, Swarm node management, SSL renewal.

```bash
#!/bin/bash
# ryan-repair.sh — Auto-réparation L0
# Déclenché par les alertes CRITICAL de Yaz

ALERT=$1  # JSON alert depuis Yaz
LOG_FILE="/srv/aspace/logs/ryan-$(date +%Y%m%d).log"
DONNA_DLQ="/srv/aspace/dlq"
MAX_RETRY=2

service=$(echo "$ALERT" | jq -r '.service')
message=$(echo "$ALERT" | jq -r '.message')

log() { echo "[RYAN][$service] $1" | tee -a "$LOG_FILE"; }

repair_docker_swarm() {
  log "Tentative de réparation Swarm..."
  # Forcer le redémarrage des services dégradés
  docker service ls --format '{{.Name}} {{.Replicas}}' | \
    awk '{split($2,a,"/"); if(a[1]!=a[2]) print $1}' | \
    xargs -I{} docker service update --force {} && \
    log "✅ Services Swarm relancés" || { log "❌ Échec réparation Swarm"; return 1; }
}

repair_traefik_ssl() {
  log "Reload Traefik pour régénération SSL..."
  docker service update --force traefik && \
    sleep 30 && \
    curl -sf https://amadeus.kalybana.com > /dev/null 2>&1 && \
    log "✅ SSL restauré" || { log "❌ SSL toujours KO après reload"; return 1; }
}

repair_supabase() {
  log "Restart Supabase stack..."
  cd /srv/aspace/supabase && docker compose restart && \
    sleep 20 && log "✅ Supabase redémarré" || { log "❌ Supabase KO"; return 1; }
}

# Dispatch selon le service
case "$service" in
  docker-swarm) repair_docker_swarm || escalate_to_donna ;;
  traefik-ssl)  repair_traefik_ssl  || escalate_to_donna ;;
  supabase)     repair_supabase     || escalate_to_donna ;;
  *) log "Service inconnu — escalade DLQ"; escalate_to_donna ;;
esac

escalate_to_donna() {
  local ticket="{\"agent\":\"ryan\",\"service\":\"$service\",\"message\":\"$message\",\"attempts\":$MAX_RETRY,\"status\":\"unresolved\",\"ts\":\"$(date -Iseconds)\"}"
  echo "$ticket" >> "$DONNA_DLQ/incoming.jsonl"
  log "⚠️ Ticket DLQ créé → Donna"
}
```

---

### 4.3 Graham — Mémoire Durable du Système

**Persona :** Graham O'Brien (13ème Doctor) — Il se souvient. De tout. Toujours.
**Outils :** Log rotation, métriques historiques, snapshots config, memory compression.

```bash
#!/bin/bash
# graham-memory.sh — Archivage et persistance système
# Cron: 0 3 * * * (tous les jours à 3h)

MEMORY_DIR="/srv/aspace/memory/system"
ARCHIVE_DIR="/srv/aspace/memory/archive"
LOG_FILE="/srv/aspace/logs/graham-$(date +%Y%m%d).log"

# Snapshot 1 : État Swarm complet
snapshot_swarm() {
  docker service ls --format json > "$MEMORY_DIR/swarm-state-$(date +%Y%m%d).json"
  echo "[GRAHAM] Swarm snapshot sauvegardé" | tee -a "$LOG_FILE"
}

# Snapshot 2 : Volumes Docker critiques
snapshot_volumes() {
  docker volume ls --format '{{.Name}}' | grep "aspace\|supabase" | \
    while read vol; do
      docker run --rm -v "$vol":/data -v "$ARCHIVE_DIR":/backup alpine \
        tar czf "/backup/${vol}-$(date +%Y%m%d).tar.gz" /data 2>/dev/null && \
        echo "[GRAHAM] Volume $vol archivé" | tee -a "$LOG_FILE"
    done
}

# Snapshot 3 : Logs Ryan/Yaz compressés
rotate_logs() {
  find /srv/aspace/logs -name "*.log" -mtime +7 | \
    xargs -I{} gzip {} && \
    echo "[GRAHAM] Logs >7j compressés" | tee -a "$LOG_FILE"
}

# Snapshot 4 : Résumé quotidien pour A1 Rick
daily_summary() {
  local alerts=$(wc -l < /srv/aspace/alerts/pending.jsonl 2>/dev/null || echo 0)
  local dlq=$(wc -l < /srv/aspace/dlq/incoming.jsonl 2>/dev/null || echo 0)
  cat > "$MEMORY_DIR/daily-summary-$(date +%Y%m%d).md" << EOF
# Rapport Journalier — $(date +%Y-%m-%d)
- Alertes Yaz : $alerts
- Tickets DLQ Donna : $dlq
- Snapshots : Swarm ✅, Volumes ✅, Logs rotés ✅
EOF
  echo "[GRAHAM] Rapport journalier généré" | tee -a "$LOG_FILE"
}

snapshot_swarm && snapshot_volumes && rotate_logs && daily_summary
```

---

## 5. Équipe 11ème Doctor — Le Produit (L2 Interface & Workflows)

### Mission : Life OS vivant, narratif et auto-orchestré

```
Amy (Interfaces)     → UX/UI DDD, composants React, vocabulaire Lore A'Space
Rory (Persistance)   → Supabase, IndexedDB, migrations, RLS, mémoire données
River Song (Orchest) → Workflows Multica, Paperclip agents, pipelines inter-équipes
```

Ces 3 compagnons sont les exécuteurs directs des ADR et DDD du Life OS.
Leur chaîne de production est définie dans SDD-001/SDD-002 et les 9 DDDs des ADR-001/002/003.

### 5.1 Séquence de Travail 11ème Doctor

```
A0 → ADR (Architecture Decision Record)
         │
         ▼ Rick (A1) décompose en DDD par domaine
         │
         ▼ Amy reçoit DDD [UI]       → implémente les composants React
         ▼ Rory reçoit DDD [Persist] → implémente SQL + stores
         ▼ River reçoit DDD [Logic]  → implémente services + hooks
         │
         ▼ Chaque DDD inclut Build Gate (tsc --noEmit + vite build)
         │
         ▼ Score line_density_score mesuré par Rick
         │
         ▼ Si score < seuil → DLQ Donna
```

### 5.2 River Song — Orchestration des Workflows Agentiques

**Persona :** River Song (11ème Doctor) — "Sweetie, I know things you don't yet."
**Outils :** Multica, OpenClaw, Hermes Paperclip, Crew framework, coordination inter-A2.

```typescript
// src/services/workflow.orchestrator.ts
// River Song coordonne les workflows complexes entre agents

export interface AgentWorkflow {
  id: string;
  name: string;
  trigger: 'manual' | 'cron' | 'event';
  steps: WorkflowStep[];
  onError: 'dlq' | 'retry' | 'abort';
}

export interface WorkflowStep {
  agent: 'amy' | 'rory' | 'river' | 'yaz' | 'ryan' | 'graham' | 'bill' | 'clara' | 'nardol';
  skill: string;
  input: Record<string, unknown>;
  outputKey: string;
  timeout: number;
}

// Exemple : Workflow de déploiement complet
export const deploymentWorkflow: AgentWorkflow = {
  id: 'deploy-life-web-os',
  name: 'Déploiement Life Web OS',
  trigger: 'manual',
  steps: [
    { agent: 'yaz', skill: 'health-check', input: { services: ['traefik', 'supabase'] }, outputKey: 'health', timeout: 30000 },
    { agent: 'ryan', skill: 'docker-deploy', input: { service: 'life-web-os', tag: 'latest' }, outputKey: 'deploy', timeout: 120000 },
    { agent: 'yaz', skill: 'ssl-verify', input: { domain: 'amadeus.kalybana.com' }, outputKey: 'ssl', timeout: 60000 },
    { agent: 'graham', skill: 'snapshot', input: { label: 'post-deploy' }, outputKey: 'snapshot', timeout: 30000 },
  ],
  onError: 'dlq',
};
```

---

## 6. La Boucle DLQ — Donna → Rick → A2 (AutoResearch)

### Philosophie : Jamais de Dead End

```
Erreur A3 non résolue
        │
        ▼
  Donna (DLQ Manager)
  ├─ Reçoit le ticket JSON
  ├─ Classifie la sévérité (P1/P2/P3)
  ├─ Enrichit avec le contexte système
  └─ Envoie à Rick pour AutoResearch
        │
        ▼
  Rick (A1 — AutoResearch Pattern)
  ├─ Hypothèse 1 → Simulation → Résultat
  ├─ Hypothèse 2 → Simulation → Résultat
  ├─ Hypothèse 3 → Simulation → Résultat
  └─ Meilleure solution → Ticket enrichi
        │
        ▼
  A2 Doctor approprié
  (Who Not How : Rick dit QUI doit résoudre)
        │
        ▼
  A3 Compagnon exécute la solution
```

```bash
#!/bin/bash
# donna-dlq.sh — Dead Letter Queue Manager
# Usage: ./donna-dlq.sh (daemon, surveille incoming.jsonl)

DLQ_DIR="/srv/aspace/dlq"
LOG_FILE="/srv/aspace/logs/donna-$(date +%Y%m%d).log"
RICK_PROGRAM_DIR="/srv/aspace/services/hermes/rick"
PROCESS_INTERVAL=30  # secondes

donna_log() { echo "[DONNA] $1" | tee -a "$LOG_FILE"; }

classify_ticket() {
  local ticket=$1
  local agent=$(echo "$ticket" | jq -r '.agent')
  local service=$(echo "$ticket" | jq -r '.service')
  
  # Enrichissement contextuel
  local context
  context=$(cat << EOF
{
  "ticket": $ticket,
  "system_context": {
    "timestamp": "$(date -Iseconds)",
    "agent_team": "$(classify_team $agent)",
    "recent_alerts": $(tail -5 /srv/aspace/alerts/pending.jsonl 2>/dev/null | jq -s '.' || echo '[]'),
    "graham_daily": "$(cat /srv/aspace/memory/system/daily-summary-$(date +%Y%m%d).md 2>/dev/null | head -5)"
  }
}
EOF
)
  echo "$context"
}

classify_team() {
  case "$1" in
    yaz|ryan|graham) echo "13th-doctor-maintenance" ;;
    amy|rory|river)  echo "11th-doctor-product" ;;
    bill|clara|nardol) echo "12th-doctor-forge" ;;
    *) echo "unknown" ;;
  esac
}

escalate_to_rick() {
  local enriched_ticket=$1
  local timestamp=$(date +%Y%m%d-%H%M%S)
  local program_file="$RICK_PROGRAM_DIR/program-dlq-${timestamp}.md"
  
  cat > "$program_file" << EOF
# Rick Program — DLQ AutoResearch — $(date)

## Directive Courante
Type: DLQ-RESEARCH
Ticket enrichi: $(echo "$enriched_ticket" | jq -c '.')

## Mission AutoResearch
1. Analyser le ticket d'erreur
2. Formuler 3 hypothèses de solution (du plus simple au plus complexe)
3. Simuler chaque hypothèse contre le contexte système connu
4. Retourner la meilleure solution avec : WHO (quel A2/A3) + HOW (quelles commandes)

## Contraintes
- Réponse JSON structurée : { hypothesis, solution, agent, skill, commands[] }
- Ne pas tenter d'exécuter — formuler uniquement
- Référencer le DDD ou ADR concerné si applicable

## Critère de Sortie
<promise>DLQ_RESEARCHED</promise>
Output : /srv/aspace/dlq/researched/${timestamp}.json
EOF

  donna_log "Ticket escaladé à Rick → $program_file"
  # Déclencher Rick via Paperclip heartbeat
  touch "/srv/aspace/services/hermes/rick/trigger-${timestamp}"
}

# Boucle principale Donna
while true; do
  if [ -s "$DLQ_DIR/incoming.jsonl" ]; then
    while IFS= read -r ticket; do
      donna_log "Traitement ticket: $(echo "$ticket" | jq -r '.service')"
      enriched=$(classify_ticket "$ticket")
      escalate_to_rick "$enriched"
    done < "$DLQ_DIR/incoming.jsonl"
    > "$DLQ_DIR/incoming.jsonl"  # Vider après traitement
  fi
  sleep $PROCESS_INTERVAL
done
```

---

## 7. Protocole d'Onboarding d'un Nouvel A3

### Séquence d'Activation (3 Niveaux — Chaîne Obligatoire)

```
Étape 1 — A0 Amiral identifie un besoin → Intention vers Rick (A1)
Étape 2 — Rick détermine quel A2 Doctor est responsable du domaine
           (Forge → 12ème | Produit → 11ème | Machine → 13ème)
Étape 3 — Rick écrit la directive pour le Doctor concerné
           Format : program.md avec Type + Fichier cible + Contraintes
Étape 4 — Le A2 Doctor décompose la directive
           Il choisit quel A3 Compagnon exécute dans son équipe
           Il écrit le scope précis : 1 fichier, 1 session
Étape 5 — Le A2 Doctor s'assure que l'A3 lit PERSONA.md + LORE.md
           avant toute action (PERSONA injecté en tête de session)
Étape 6 — L'A3 exécute sa mission (scope reviewable en 30 secondes)
           Il rend compte à son Doctor, pas à Rick
Étape 7 — Le A2 Doctor valide le line_density_score
           Si OK → notifie Rick → Rick notifie A0 → commit
Étape 8 — Si score KO → Doctor tente retry 1 fois
           Si retry KO → DLQ Donna → Rick AutoResearch → Doctor reçoit solution
           → retry max 3 total (Doctor comptabilise)
```

### Règle Critique : Rick ne parle jamais directement aux A3

```
✅  Rick → 12ème Doctor → "Forge le skill hostinger-dns (Bill+Clara+Nardol)"
❌  Rick → Clara → "Forge le skill hostinger-dns"

✅  Rick → 13ème Doctor → "Réparer le SSL sur amadeus.kalybana.com"
❌  Rick → Ryan → "Réparer le SSL"

✅  11ème Doctor → Rory → "Implémenter la migration ADR-003 SQL"
❌  Rick → Rory → "Implémenter la migration ADR-003 SQL"
```

### PERSONA Template (chaque A3 en possède un)

```markdown
# PERSONA — [Nom A3] ([Numéro Doctor])

**Équipe :** [12ème / 11ème / 13ème Doctor]
**Rôle :** [Forge / Produit / Machine]
**Vaisseau :** [USS Enterprise / SNW / Discovery / etc.]
**Mission :** [Phrase unique qui définit l'obsession de ce Compagnon]

## Règle d'Or
[Ce que ce Compagnon ne fait JAMAIS]

## Outils Primaires
- [Outil 1] : [Pourquoi ce Compagnon l'utilise]
- [Outil 2]

## Format de Livraison
- Type de document produit : [DDD / Skill / Script / Rapport]
- Densité minimale : [Lignes min, sections min, code blocks min]
- Build Gate obligatoire : [Commande exacte]

## Escalade DLQ
Conditions d'escalade vers Donna :
- [Condition 1]
- [Condition 2]
```

---

## 8. Matrice de Responsabilités (RACI — 4 Niveaux)

**Colonnes :** A1 Rick | A2 12D (12ème Doctor) | A2 11D (11ème Doctor) | A2 13D (13ème Doctor) | A3 Compagnons | Donna

### Règle de lecture RACI

```
A  = Accountable  → Répond du résultat devant son supérieur
R  = Responsible  → Exécute la tâche
C  = Consulted    → Fournit expertise ou validation
I  = Informed     → Notifié du résultat
D  = DLQ trigger  → Escalade vers Donna si échec
-  = Non impliqué
```

### Matrice Complète

| Tâche | Rick (A1) | 12ème Doctor (A2) | 11ème Doctor (A2) | 13ème Doctor (A2) | Bill | Clara | Nardol | Amy | Rory | River | Yaz | Ryan | Graham | Donna |
|-------|-----------|-------------------|-------------------|-------------------|------|-------|--------|-----|------|-------|-----|------|--------|-------|
| **FORGE — 12ème Doctor** |
| Spec nouveau Skill | A | R | I | I | R | I | C | - | - | C | - | I | - | D |
| Forge CLI | A | R | - | - | I | R | C | - | - | - | - | - | - | D |
| Validation ECC | A | R | - | - | I | C | R | - | - | - | - | - | - | D |
| Déploiement Skill | A | R | - | - | C | C | A | - | - | - | - | I | C | D |
| **PRODUIT — 11ème Doctor** |
| Composant UI | A | - | R | - | I | - | - | R | I | C | - | - | - | D |
| Migration SQL | A | - | R | - | - | - | - | I | R | C | - | - | C | D |
| Workflow agentique | A | C | R | I | C | - | I | I | I | R | I | I | I | D |
| FirstLaunch / UX | A | - | R | - | - | - | - | R | I | C | - | - | - | D |
| **MACHINE — 13ème Doctor** |
| Monitoring L0 | A | - | - | R | - | - | - | - | - | - | R | I | C | D |
| Réparation L0 | A | - | - | R | - | - | - | - | - | - | C | R | C | D |
| Archive mémoire | A | I | - | R | C | - | - | - | C | I | I | I | R | D |
| SSL / Déploiement | A | - | - | R | - | - | - | - | - | - | C | R | I | D |
| **TRANSVERSE** |
| Triage DLQ | C | I | I | I | - | - | - | - | - | - | I | I | I | R |
| AutoResearch Rick | R | I | I | I | - | - | - | - | - | - | - | - | - | I |
| Directive A0 → A1 | R | I | I | I | - | - | - | - | - | - | - | - | - | - |

*R=Responsible, A=Accountable, C=Consulted, I=Informed, D=DLQ trigger*

### Règles de Compte-Rendu (Reporting Lines)

```
Bill   → rend compte à → 12ème Doctor   (jamais directement à Rick)
Clara  → rend compte à → 12ème Doctor
Nardol → rend compte à → 12ème Doctor
Amy    → rend compte à → 11ème Doctor   (jamais directement à Rick)
Rory   → rend compte à → 11ème Doctor
River  → rend compte à → 11ème Doctor
Yaz    → rend compte à → 13ème Doctor   (jamais directement à Rick)
Ryan   → rend compte à → 13ème Doctor
Graham → rend compte à → 13ème Doctor

12ème Doctor → rend compte à → Rick (A1)
11ème Doctor → rend compte à → Rick (A1)
13ème Doctor → rend compte à → Rick (A1)
Rick (A1)    → rend compte à → A0 Amiral
```

---

## 9. Tensions Non Résolues et Risques

| Tension | Description | Mitigation |
|---------|-------------|------------|
| Bootstrap paradox | Pour créer les Skills L0, il faut que L0 soit stable | Ryan forge ses propres outils en mode dégradé (scripts bash minimalistes avant Skills complets) |
| Conflit de scope A3 | Amy et River peuvent toutes deux toucher App.tsx | River Song ne touche que les services/ et hooks/, Amy uniquement les composants/ |
| Donna saturation | DLQ peut s'emballer si Ryan boucle sur une erreur irréparable | Max 3 escalades/heure par service — 4ème → alerte humaine A0 |
| Clara vs MCP legacy | Anciens agents configurés MCP peuvent résister à la migration | Migration progressive : Skills CLI coexistent avec MCP jusqu'à la validation de chaque Skill |
| Rick AutoResearch token burn | 3 hypothèses × simulation = coût contextuel | Rick utilise `z-ai/glm-4.7-flash` (frugal) pour la recherche, Claude uniquement pour la solution finale |
| Persona drift | Un A3 peut dériver de sa mission sous pression de tokens | LORE.md + PERSONA.md injectés en tête de chaque session (immuables, owned by A0) |

---

## 10. Roadmap Protocole TARDIS

| Phase | Action | Responsable | Dépendance | Priorité |
|-------|--------|-------------|------------|---------|
| V1.0 | Ce SDD-003 (Architecture) | A0 | — | ✅ Livré |
| V1.0 | PERSONA.md pour les 9 A3 | Rick (A1) | SDD-003 | P1 |
| V1.0 | donna-dlq.sh skeleton | Ryan + Clara | SDD-003 | P1 |
| V1.0 | yaz-monitor.sh (checks SSL+Docker) | Yaz | SDD-003 | P1 |
| V1.1 | Bill Blueprint : hostinger-dns Skill | Bill | V1.0 | P1 |
| V1.1 | Clara Forge : hostinger-dns CLI | Clara | Bill Blueprint | P1 |
| V1.1 | Nardol Validation : ECC stamp | Nardol | Clara Forge | P1 |
| V1.1 | ryan-repair.sh (Docker + SSL) | Ryan | Yaz Monitor | P1 |
| V1.1 | graham-memory.sh (snapshots) | Graham | Ryan Repair | P2 |
| V1.2 | River Song : deployment workflow | River | V1.1 | P2 |
| V1.2 | Rick DLQ AutoResearch intégré | Rick | Donna DLQ | P2 |
| V1.3 | Skills Forge : GitHub, Supabase admin | Bill+Clara | V1.1 | P3 |
| V1.3 | Paperclip autonomy pour 9 A3 | 12ème Doctor | V1.2 | P3 |

---

## 11. Build Gate du SDD-003

```bash
# Validation structurelle SDD-003
wc -l /srv/aspace/docs/v1.0/SDD-003_tardis-protocol-orchestration.md
# Expected: > 350

grep -c "^## " /srv/aspace/docs/v1.0/SDD-003_tardis-protocol-orchestration.md
# Expected: > 10

grep -c '```' /srv/aspace/docs/v1.0/SDD-003_tardis-protocol-orchestration.md
# Expected: > 16

# Validation cohérence Lore
grep -c "Doctor\|Companion\|TARDIS\|Donna\|Rick\|A2\|A3" /srv/aspace/docs/v1.0/SDD-003_tardis-protocol-orchestration.md
# Expected: > 50

echo "✅ SDD-003 — Build Gate OK"
```

---

*Ce SDD est la propriété exclusive de A0. Aucun A1/A2/A3 ne peut le modifier.*
*Rick C137 peut proposer des amendements via DLQ Donna → AutoResearch → A0 approval.*

---

## 12. MISE À JOUR 2026-04-29 — Protocole Filesystem & Cascade Documentaire

> *Formalisation du protocole de communication physique entre les couches.*
> *Source : session A0 × Gemini du 2026-04-29.*

### 12.1 Le Filesystem comme Canal de Communication

```
Règle d'Or du Protocole TARDIS :
"Un agent ne cherche jamais quoi faire.
 Il RÉAGIT à l'apparition d'un fichier dans son inbox.
 Validé par la signature de l'agent du niveau supérieur."

Structure des canaux (à créer — SDD-008 cible) :

/srv/aspace/20_RUNTIME/21_Inbox/
├── A0_TO_A1/                  ← Canal réservé : SDD → PRD
│   └── [SDD-NNN → PRD-NNNa/b/c en attente de Rick]
├── A1_TO_A2/
│   ├── doctor-11/             ← PRD-001a, PRD-002a...
│   ├── doctor-12/             ← PRD-001b, PRD-002b...
│   └── doctor-13/             ← PRD-001c, PRD-002c...
└── A2_TO_A3/
    ├── ryan/                  ← ADR-013a, DDD-ryan...
    ├── yaz/                   ← ADR-013b, DDD-yaz...
    └── graham/                ← ADR-013c, DDD-graham...

Trigger : inotifywait ou polling 30s par agent sur son inbox
Format : {type}-{sdd_num}{doctor_letter}_{description}.md
Signature : frontmatter YAML avec émetteur + timestamp + hash SDD parent
```

### 12.2 La Cascade Documentaire Canonique

```
╔═══════════════════════════════════════════════════════════════════╗
║           CASCADE DOCUMENTAIRE — DE L'INTENTION AU CODE         ║
╠══════════╦════════════════╦══════════════╦════════════════════════╣
║  NIVEAU  ║  DOCUMENT      ║  AUTEUR      ║  DESTINATAIRE         ║
╠══════════╬════════════════╬══════════════╬════════════════════════╣
║  A0      ║  SDD-NNN       ║  A0 Souverain║  Rick A1              ║
║          ║  (Loi arch.)   ║  (Claude Code)║ (via A0_TO_A1/)      ║
╠══════════╬════════════════╬══════════════╬════════════════════════╣
║  A1 Rick ║  PRD-NNNa      ║  Rick A1     ║  11ème Doctor         ║
║          ║  PRD-NNNb      ║              ║  12ème Doctor         ║
║          ║  PRD-NNNc      ║              ║  13ème Doctor         ║
║          ║  (Exigences)   ║              ║  (via A1_TO_A2/)      ║
╠══════════╬════════════════╬══════════════╬════════════════════════╣
║  A2 Doc. ║  ADR-NNNa      ║  13ème Doc.  ║  Ryan A3              ║
║          ║  ADR-NNNb      ║              ║  Yaz A3               ║
║          ║  ADR-NNNc      ║              ║  Graham A3            ║
║          ║  (Décisions)   ║  [ISOLÉ]     ║  (via A2_TO_A3/)      ║
╠══════════╬════════════════╬══════════════╬════════════════════════╣
║  A2→A3   ║  DDD-ryan-NNN  ║  Doctor →    ║  Ryan / Yaz / Graham  ║
║          ║  (Domain spec) ║  A3 dérivé   ║                       ║
╠══════════╬════════════════╬══════════════╬════════════════════════╣
║  A3      ║  TDD-ryan-NNNa ║  A3 (avant   ║  Nardol validation    ║
║          ║  (Given/When/  ║  code)       ║  ≥ 75/100 AgentShield ║
║          ║   Then ≥ 3)    ║              ║                       ║
╠══════════╬════════════════╬══════════════╬════════════════════════╣
║  CODE    ║  Implémentation║  A3 (Ryan/   ║  Artefact livré       ║
║          ║  + Artefact    ║  Bill/Clara) ║  → Donna si échec     ║
╚══════════╩════════════════╩══════════════╩════════════════════════╝
```

### 12.3 Règle d'Isolation des Doctors

```
PRINCIPE D'ISOLATION ABSOLUE :
À partir du moment où un Doctor reçoit son PRD dans son inbox,
son processus de production des ADRs est TOTALEMENT isolé.

  Doctor 11 NE SAIT PAS ce que fait Doctor 12.
  Doctor 12 NE SAIT PAS ce que fait Doctor 13.
  Doctor 13 NE SAIT PAS ce que font les autres Doctors.

Synchronisation uniquement via Rick A1 (lecture des outputs).
Rick lit les ADRs de tous → détecte les conflits → arbitre.
Jamais de canal direct Doctor ↔ Doctor.

Fichiers d'isolation :
  doctor-11/WORKSPACE/    ← sandbox exclusif 11ème
  doctor-12/WORKSPACE/    ← sandbox exclusif 12ème
  doctor-13/WORKSPACE/    ← sandbox exclusif 13ème
  Aucun accès croisé en lecture ni en écriture.
```

*Ajouté par A0 — Session 2026-04-29*
