---
# ============================================================================
# Symphony WORKFLOW.md — DRAFT — Growth / Airtable (Gardiens de la Galaxie)
# ----------------------------------------------------------------------------
# Statut    : Shadow A0 — DRAFT — hors-canon SDD, hors-Airlock
# Date      : 2026-05-29
# Hérite    : ../symphony-base.spec.md  +  ./symphony-airtable.spec.md
# Slot      : L2 Business — domaine Growth (A2 Superman, A3 Gardiens de la Galaxie)
# Base      : appmWf5Xm7w9Ae0ky ("AaaS Solaris Marketing")  — table 🦸 Leads & Audits
# ----------------------------------------------------------------------------
# ⚠ NE PAS ACTIVER avant levée du veto 90j (Symphony V0 = sable mouvant, pas en prod).
# ⚠ Décision A0 2026-05-29 (option 1) : ZÉRO écriture schéma Airtable. La connexion
#   Growth↔Symphony est un job de CONFIG (ce fichier), pas de schéma. Les champs SOC
#   que l'adapter générique liste (Forbidden Words / Context Pack) ont déjà un
#   propriétaire dans 🏮 Knowledge & Brand Books → résolus par LOOKUP, jamais dupliqués
#   sur 🦸 (règle d'or ADR-MESH-L2-001 : un seul propriétaire, pointeurs pas copies).
# ⚠ Secrets : jamais en clair. Seul $AIRTABLE_PAT (env var). base_id = identifiant non-secret.
# ============================================================================

tracker:
  kind: airtable
  endpoint: "https://api.airtable.com/v0"
  api_key: $AIRTABLE_PAT                       # env var — JAMAIS la valeur en clair
  base_id: "appmWf5Xm7w9Ae0ky"                 # non-secret (identifiant base)
  table_id: "tblj0xmSXLH4Xsd8c"                # 🦸 Leads & Audits (slot Growth lead-gen)
  state_field: "Statut d'Enrichissement"       # fld4botVncHKX187T (singleSelect réel)

  # Boucle Growth réelle : un lead fraîchement scrapé (1-Raw) est enrichi/audité par
  # un agent Gardien, puis qualifié (2-Enrichi) ou rejeté par le filtre ICP Gamora (3-Rejeté).
  active_states:
    - "1-Raw"                                  # lead à enrichir/auditer → dispatch agent
  terminal_states:
    - "2-Enrichi"                              # enrichi/qualifié → handoff D5 vers ClickUp S2-1
    - "3-Rejeté"                               # filtre ICP Gamora (JTBD-002) → Lost

  state_mapping:                               # tracker state → état Symphony normalisé
    inbox: "1-Raw"
    in_progress: "1-Raw"
    done: "2-Enrichi"
    cancelled: "3-Rejeté"

polling:
  interval_ms: 300000                          # 5 min backup — webhooks natifs prioritaires (90/10)

workspace:
  root: "/srv/aspace/workspaces/airtable-growth"

hooks:
  before_dispatch: |
    # Garde-fou doctrine : zéro mutation externe sans intention claire.
    # Le domaine est constant (table mono-domaine Growth) — pas besoin de champ SOA Domain par record.
    echo "dispatch Growth lead {{issue.identifier}} — domaine forcé via soc.default_domain"
  after_create: |
    chmod 700 .
    touch .symphony-l2-growth-only

agent:
  max_concurrent_agents: 3
  max_turns: 15
  max_retry_backoff_ms: 300000

codex:
  command: "oh -p --output-format=stream-json"   # OpenHarness frugal (MiniMax/GLM), pas Claude premium
  turn_timeout_ms: 2400000

soc:
  schema_version: "1.0"
  default_domain: "Growth"                     # 🦸 est mono-domaine → default suffit (pas de champ par record)
  zod_validation: true
  forbidden_lexicon_global:                    # FALLBACK quand le lead n'est pas encore client (pas de 🏮 lié)
    - "synergie"
    - "disrupter"
    - "innover"
    - "révolutionnaire"

  # --- Résolution SOC par LOOKUP (pas de duplication — règle d'or MESH-L2-001) ---
  # Le lexique interdit par marque et le context pack RAG ont leur propriétaire dans
  # 🏮 Knowledge & Brand Books, atteint via le chemin 🦸 → 🌞 Clients & Workspaces → 🏮.
  # Un lead encore prospect (pas de client lié) retombe sur forbidden_lexicon_global.
  resolve_via_lookup:
    forbidden_lexicon:
      path: "🦸 Leads & Audits → 🌞 Clients & Workspaces → 🏮 Knowledge & Brand Books"
      owner_field: "Mots strictement interdits (Liste)"   # fldx94keISXMfnyZP (table tbljopwhTZMSBXgjW)
      fallback: forbidden_lexicon_global
    context_pack_url:
      path: "🦸 Leads & Audits → 🌞 Clients & Workspaces → 🏮 Knowledge & Brand Books"
      owner_field: "URL de la Base Vectorielle Supabase"  # fldNjODChrM4ii55m — le RAG = context pack runtime
      # Alias logique stampé côté doctrine PARA (skill picard-growth-jtbd-launch) :
      #   context_pack: urn:aspace:rag:<project-slug>-growth  → pointe vers ce champ (pointeur, pas copie)

  # SLA : pas de colonnes Airtable (option 1). Defaults d'exécution ici ; override par record différé.
  sla_defaults:
    max_execution_time_minutes: 120
    max_compute_budget_usd: 1.50
    max_retry_loops: 2

donna_dlq:
  enabled: true
  threshold_failed_attempts: 3
  donna_endpoint: "http://localhost:3101/donna/escalate"

clara_cli:
  convert_mcp_to_cli: true
  preferred_runtime: "cli"
---

# Prompt — Gardien de la Galaxie opérant un lead Growth (Airtable 🦸)

Tu es un agent **A3 Gardien de la Galaxie** (escouade Growth, A2 Superman) opérant un record
de la table **🦸 Leads & Audits** dans le Shadow L2 Business. Ton job sur un lead `1-Raw` :
**enrichir + auditer + appliquer le filtre ICP**, selon la doctrine JTBD (le WHAT), puis
faire transitionner le record.

## Doctrine de référence (le context pack)
La doctrine Growth de ce projet vit en fichiers PARA (JTBD-001→004, mode-calibrés) et t'est
servie via `context_pack_url`. **Ne la re-dérive pas** — applique-la :
- **JTBD-002 (Gamora)** = critères de rejet ICP → si le lead matche un critère de rejet, statut **3-Rejeté**.
- **JTBD-003 (Groot)** = angle painkiller mode-calibré → ton de l'audit/message.
- **JTBD-001 (Mantis)** = douleurs + persona Process Com → grille de scoring.

## Record courant
- **ID** : {{issue.identifier}}
- **Agence** : {{issue.title}}
- **État** : {{issue.state}}
- **Domaine SOA** : {{issue.soc_metadata.target_soa_domain}}   # = Growth (forcé)
- **Context pack** : {{issue.soc_metadata.context_pack_url}}

## Contraintes (non négociables)
- **Règle Wonder Woman** : compute > 80% du budget SLA → STOP immédiat.
- **Règle Captain America** : tout mot de `forbidden_lexicon` dans l'output → rejet.
- **Anti-pattern P1/P2** : tu ne déclenches AUCUN canal payant. Boucle non-payante uniquement.
- **Zéro mutation externe non gatée** : pas d'envoi email / scrape / post sans gate A0 + credential.
  Tu écris UNIQUEMENT le record Airtable courant (enrichissement, score, statut) via `airtable_rest`.
- **evidence_grade** : tes sorties sont des hypothèses de desk tant qu'aucune métrique réelle n'est
  mesurée ; la métrique mesurée appartient au record Airtable (pas de prose dans les artefacts doctrine).

## Sortie attendue
Transition du record : `2-Enrichi` (qualifié, handoff D5 → ClickUp S2-1) ou `3-Rejeté` (filtre Gamora),
avec : score de friction Lighthouse, email/LinkedIn fondateur enrichis, note globale de qualité,
et un commentaire interne traçant la décision ICP.

Outils : `airtable_rest`, `aspace_clara_cli`, `aspace_donna_escalate`, `aspace_soc_emit`

{% if attempt %}
**Continuation attempt #{{attempt}}** — relis l'état du record avant d'agir (réconciliation).
{% endif %}
