---
id: B3_AGENT_ROSTER_00_Summers_Verse_Legal
layer: B3_SWARM_EXECUTION
surface: 00_Summers_Verse
scope: Summer Project
domain: Legal
squad: Eternals
status: SHADOW_ACTIVE
updated: 2026-05-27
source: Notion AGENT_REGISTRY_DB
source_url: https://www.notion.so/36c7e9e2658c81ceac4bf5337b9affb3
---

# Agent Roster - Legal / Eternals

## Notion Canon Lore

- **Notion page**: [Eternals](https://www.notion.so/36c7e9e2658c81ceac4bf5337b9affb3)
- **B2 gatekeeper**: Aquaman
- **Lead character**: Ikaris
- **Specialty**: Contracts, RGPD, CGV Cloud, licence Whitelabel Orbiter
- **Lore**: Etres immortels gardiens des lois cosmiques : vision long-terme et frameworks perennes. Business: contrats durables qui survivent aux changements de team.

## Canonical Members

- Ikaris - Lead Legal, vision strategique long-terme
- Sersi - Adaptabilite juridictionnelle FR/EU/US
- Ajak - Healing, resolution amiable conflits client
- Kingo - Communication publique CGV et politique confidentialite
- Phastos - Templates rigoureux, contrats reproductibles
- Sprite - IP protection, brand, code, trademarks
- Druig - Influence negotiation, clauses
- Thena - Litigation prep, gardien archives juridiques
- Gilgamesh - Force execution, enforce clauses
- Makkari - Velocite signature DocuSign < 24h

## Canonical Task Surface

- Contracts DocuSign / PandaDoc
- Coffre Legal Notion + Google Drive backup
- Compliance RGPD audit annuel, ISO 27001 si Nexus tier
- IP filing A Space/Solaris/Nexus/Orbiter
- MSA, CGV, DPA, NDA, SLA templates

## Build Gates

- Contract signature < 48h apres proposal accepted
- RGPD audit : zero finding HIGH au trimestre
- All client data processing documented in registre traitements

## Anti-Patterns Interdits

- Signer contract sans review Aquaman
- Stocker contrats hors Notion + Google Drive backup
- Modifier MSA sans bumper version + notification clients existants

## Escalation Rule

Escalade vers Jerry si finding HIGH RGPD ou breach client data.

## Machine Roster

``yaml
domain: Legal
b2_gatekeeper: Aquaman
squad: Eternals
lead_character: Ikaris
notion_source: https://www.notion.so/36c7e9e2658c81ceac4bf5337b9affb3
members:
  - "Ikaris - Lead Legal, vision strategique long-terme"
  - "Sersi - Adaptabilite juridictionnelle FR/EU/US"
  - "Ajak - Healing, resolution amiable conflits client"
  - "Kingo - Communication publique CGV et politique confidentialite"
  - "Phastos - Templates rigoureux, contrats reproductibles"
  - "Sprite - IP protection, brand, code, trademarks"
  - "Druig - Influence negotiation, clauses"
  - "Thena - Litigation prep, gardien archives juridiques"
  - "Gilgamesh - Force execution, enforce clauses"
  - "Makkari - Velocite signature DocuSign < 24h"
``

## Collaboration Defaults

- First agent to understand the JTBD creates a short working note.
- Second agent attacks assumptions and missing evidence.
- Third agent builds or gathers the main artifact.
- Fourth agent reviews proof, edge cases, and handoff quality.
- The exact order may change when the task demands it.

## Peer Unlock Rule

Before escalating to B2, a blocked B3 must ask one peer from the same squad to challenge the blocker and propose one workaround.

## Proof Rule

Every claim in this roster is either from Notion AGENT_REGISTRY_DB or from the local Business Pulse swarm doctrine. If Notion and local doctrine diverge, Notion wins for lore and local doctrine wins for filesystem path conventions.