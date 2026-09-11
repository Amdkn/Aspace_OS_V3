---
type: Concept
title: Neutralisation de 9Router et OmniRoute et Dédoublement d'Authentification Antigravity
description: Décision de mise hors service définitive des routeurs intermédiaires 9Router (port 20128) et OmniRoute (port 20129) pour préserver l'intégrité de l'authentification native et éviter la cannibalisation Tech OS.
tags: [architecture, tech-os, antigravity, auth, routage, ports]
generated: { by: gemini-antigravity, at: 2026-09-07T08:05:00Z }
verified:
  - { by: human:amdkn, at: 2026-09-07T07:45:00Z }
sources:
  - id: decision-amdkn-20260907
    resource: "Directive propriétaire Amadou Kone — abandon de 9Router et OmniRoute perturbateurs d'auth Antigravity"
    author: human:amdkn
    last_modified: 2026-09-07
okf_version: "0.2"
---

# Neutralisation de 9Router et OmniRoute

## 1. Contexte & Problème Observé
Le 6 et 7 septembre 2026, l'empilement de proxys locaux (Next.js sur le port 20128 `9Router` et le dispatcher `OmniRoute` sur le port 20129) a provoqué des dysfonctionnements majeurs :
- Interception erratique des jetons d'authentification et des redirections HTTP (notamment redirections 307 de la passerelle).
- Altération de la négociation TLS / sessions OAuth de l'assistant Google Antigravity / Gemini.
- Manque de traçabilité opérationnelle (aucune documentation ni mémoire laissée par l'agent Codex).

## 2. Décision d'Architecture & Arbitrage Propriétaire
Sur arbitrage formel d'Amadou Kone :
- **Mise hors service totale et définitive** de `9Router` (port 20128) et `OmniRoute` (port 20129).
- Les processus Node.js / Next.js associés ont été tués de force (`taskkill /F /PID`).
- Les ports 20128 et 20129 sont déclarés **dépréciés et proscrits** dans le canon opérationnel `GEMINI.md`.
- Interdiction formelle de réintroduire des intermédiaires d'inférence non sollicités qui cannibalisent l'attention système et menacent la communication directe avec le runtime Antigravity.

## 3. Règle de Non-Régression
Tout appel LLM doit s'exécuter soit directement via les SDK autorisés (`@google/genai`, Anthropic, OpenAI), soit via des interfaces directes unifiées sans proxy local opaque non audité.
