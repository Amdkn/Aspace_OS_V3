---
id: ADR-SECURITY-001
title: Vault Boundary & Secret Rotation Policy — A'Space OS Security Doctrine
type: ADR (Architectural Decision Record)
status: PROPOSED (A0 sign-off 2026-06-15 via "go for all", à valider scope Templates mission 4)
date: 2026-06-15
author: A0 (Amadeus) via A2 (Claude Code) sub-agent
domain: L0 Tech_OS / Security / Secrets / Rotation
tags: [#ADR #security #vault #secrets #rotation #test-key-pragma #no-cleartext]
doctrine_anchors: [ADR-META-001, ADR-RICK-001, "Test Key Pragma", "Doctrine no-hard-delete"]
related: [AGENTS.md, MEMORY.md, CLAUDE.md, "Test Key Pragma (CLAUDE.md)"]
provenance: |
  Née 2026-06-15 de l'analyse mission 4 (PARA Geordi 02_Templates) : template Tilly
  `04_security_vault_rotation` détecté. Doctrine à formaliser : séparation vault C3 (secrets
  long terme) vs env User scope (test-key transit) vs masked SecureString (production), avec
  rotation 1×/trimestre obligatoire.
sign_off_a0: "A0 Amadeus — Go ADR-SECURITY-001 — 2026-06-15 (via 'go for all' session-level directive, scope à valider)"
sign_off_pending: false
ratification_log_2026-06-15: "A0 batch GO. D4 append-only. D7 = pas d'escalation additionnelle."
---

# ADR-SECURITY-001 — Vault Boundary & Secret Rotation Policy

## Status
**PROPOSED → ACCEPTED via "go for all" A0 2026-06-15** (scope templates mission 4 — A0 priorise
au prochain tour si hypothèse A2 erronée).

## Context

1. **Mission 4 (2026-06-15)** : A2 a identifié 5 templates candidats. Le présent ADR couvre
   template **#2** présumé = "Security Vault Rotation" (Tilly canon tier 1).
2. **Test Key Pragma** (cf. `CLAUDE.md` global) déjà opérationnel : 3 canaux (test-key-in-chat /
   masked SecureString / jamais en clair .md/.json/git), rotation post-test, transit-only.
3. **ADR-INFRA-MCP-001** (déjà DRAFT) couvre le MCP mastery + vault C3 Hostinger/Dokploy.
4. **Manque** = politique **rotation 1×/trimestre** formalisée + tableau récap.

## Decision

**D1 — 3 canaux de stockage secrets** :
| Canal | Usage | Durée | Exemples |
|-------|-------|-------|----------|
| **Test-key-in-chat** | Vérification one-shot, scope discovery | < 1 session | `amdkn777@gmail.com` test PAT |
| **Env User scope Windows** | Transit-only session | 1-90 jours | `ANTHROPIC_API_KEY`, `POSTGRES_PASSWORD` |
| **Masked SecureString (.env gitignored)** | Production long terme | 1+ an | Caddy LE cert, Dokploy API key |

**D2 — Rotation 1×/trimestre obligatoire** : intégrée au checklist bilan 12WY.
- Trimestre 2026-Q3 (cycle 06/15 → 09/07) : rotation `POSTGRES_PASSWORD` VPS + Dokploy API key +
  Hostinger token (cf. MEMORY.md 2026-06-13 "OMK dashboard LIVE" pending).
- Trimestre 2026-Q4 (09/08 → 12/07) : rotation `VERCEL_TOKEN` + `ANTHROPIC_API_KEY` + Telegram
  bot token.

**D3 — Jamais en clair dans .md/.json/.git** : anti-pattern prévenus :
- ❌ Secret dans commit message.
- ❌ Token dans ADR body (utiliser `$(op read op://...)` ou référence vault).
- ❌ Clé API en clair dans `wiki/log.md` (utiliser `***` ou hash court + vault path).
- ✅ Pattern "transit-only" : `[Environment]::SetEnvironmentVariable(..., "User")` puis
  `unset` après usage.

**D4 — Test Key Pragma (CLAUDE.md) reste la doctrine centrale** : A0 peut partager clés en chat
POUR VÉRIFICATION IMMÉDIATE. L'agent teste, log preuve minimale, A0 rotate post-test. Pas de
paranoia pre-test.

**D5 — Audit secrets 1×/an** (intégré bilan annuel 12WY × 4 = annuel) : A2 lance
`gitleaks` ou équivalent sur tout le repo `_SPECS/`, `wiki/`, `00_Amadeus/`. D1 receipts =
0 leak.

## Consequences

- ✅ Rotation maîtrisée = surface d'attaque réduite.
- ✅ Vault C3 (Hostinger/Dokploy) = source unique de vérité long terme.
- ✅ Test Key Pragma opérationnel = pas de paralysie cycle test-fix-test (D7).
- ⚠️ Coût humain : A0 doit penser à rotate chaque trimestre (mitigation : checklist bilan 12WY
  auto-rappel).

## References

- `CLAUDE.md` global section "🔑 Doctrine 'Test Key Pragma'" (canonique).
- `ADR-INFRA-MCP-001_agentic-mcp-mastery-dox-god-mode.md` (sister, MCP vault C3).
- `MEMORY.md` 2026-06-13 "OMK dashboard LIVE" (rotation pending list).
- `Tilly 04_security_vault_rotation` (PARA Geordi mission 4, template source).
