---
source: Codex Desktop session "Analyser principes B2 Jerry"
date: 2026-06-03
type: session-source
status: ARCHIVE_READY
domain: A'Space OS V2 / Jerry-Summer / Hermes / E-Myth
tags: [#Codex, #Jerry, #Summer, #Hermes, #Symphony, #Solaris, #E-Myth]
---

# Source - Codex Session Jerry/Summer/Hermes E-Myth

Cette page preserve la valeur durable d'une session Codex devenue trop longue et
compressee plusieurs fois. Elle ne remplace pas les artefacts produits; elle sert de
trace source pour les futures reprises.

## Decisions Durables

1. Jerry est la couche macro business dans Spock Areas; Summer est la couche micro
   projet dans Picard Projects.
2. Les projets Summer doivent etre developpes en B1/B2/B3, pas seulement alignes par
   un fichier de synthese.
3. Les 8 domaines transverses doivent produire des preuves: Sales, Product, Ops, IT,
   Finance, People, Legal, Growth.
4. La bonne bascule est de passer de `structure creee` a `preuve produite`.
5. Codex et Claude sont des apps de visionnaires et d'ingenierie; ils ne doivent pas
   devenir les agents autonomes permanents par defaut.
6. Hermes Workspace est la surface locale d'execution durable; Hermes CLI/Agent et
   Hermes Workspace doivent rester distingues.
7. Hermes autonome doit utiliser OpenRouter `z-ai/glm-4.7-flash` comme default exclusif.

## Travaux Jerry / Summer

La session a etendu les projets Summer actifs avec des domaines transverses et des gates
associes:

- Ops Batman
- People Green Lantern
- IT Cyborg
- Growth Superman
- Legal Aquaman
- Finance Wonder Woman
- Sales
- Product Flash

Regle canonique: un gate n'est pas complete par existence de fichier. Il faut executer
le JTBD, produire le packet, puis marquer la decision.

Prochain ordre de preuve recommande:

1. `00 Agency as a Service`
2. `01 OMK Business OS`
3. `05 marina Cleaning BOS & SOP`
4. `04 Alikaly Bana Holding to LLC`
5. `02 ABC OS & Child Care BOS`
6. `03_RILCOT_Members_Space_OS`

Pour `00 Agency as a Service`, Sales/JTBD diagnostic-to-proposal a ete execute et marque
`PASS_INTERNAL`. La prochaine preuve logique reste Product/MVP boundary, puis Ops/Finance/
Legal selon les blocages.

## Solaris Tooling Decision

Le triptyque operationnel Solaris est:

| Surface | Role |
|---------|------|
| Airtable | Clients, pipeline, records, identifiants clients |
| ClickUp | Operations, tasks, statuts, SLA, delegation |
| Notion | SOP, canon, decisions, savoir durable |

Lien de production attendu:

```text
Notion SOP -> ClickUp Task -> Airtable Record
```

Les outils n'ont pas besoin d'etre parfaits pour commencer a deleguer a Hermes. Ils
doivent seulement avoir des boundaries nettes, des champs manquants explicites et une
politique de writeback controlee.

## Symphony Vers Hermes

Symphony reste le routeur conceptuel et local; Hermes execute.

Artefacts de delegation produits:

- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L2\WORKFLOW.solaris-clickup-ops.md`
- `C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L2\WORKFLOW.solaris-airtable-clients.md`
- `C:\Users\amado\hermes-workspace\docs\swarm\HERMES_MISSION_CONTRACT.md`

Politique d'ecriture externe:

- dry-run d'abord;
- mission_result YAML obligatoire;
- writeback externe seulement apres greenlight explicite;
- ClickUp/Airtable/Notion ne sont pas modifies par Hermes sans autorisation.

## Hermes Workspace

Ports canoniques:

```text
Workspace UI  : http://localhost:3000
Gateway API   : http://127.0.0.1:8642
Dashboard API : http://127.0.0.1:9119
Port 3333     : non canonique / a eviter
```

Scripts et configs importants:

- `C:\Users\amado\hermes-workspace\start-hermes.ps1`
- `C:\Users\amado\hermes-workspace\scripts\Set-HermesOpenRouterKey.ps1`
- `C:\Users\amado\hermes-workspace\scripts\Test-HermesStack.ps1`
- `C:\Users\amado\AppData\Local\hermes\config.yaml`
- `C:\Users\amado\hermes-workspace\swarm.yaml`

La cle OpenRouter a ete installee localement par saisie securisee pendant la session.
Aucune valeur de cle ne doit etre reproduite dans les docs ou logs.

Validation documentaire Context7 effectuee pendant l'archivage:

- Source: `/websites/openrouter_ai`
- Confirme: base URL `https://openrouter.ai/api/v1`, endpoint chat completions,
  authentification Bearer, champ `model` comme identifiant de modele, et format general
  `<author>/<slug>` pour les model IDs.
- Risque residuel: la disponibilite effective de `z-ai/glm-4.7-flash` doit etre revalidee
  par healthcheck local Hermes/OpenRouter dans une nouvelle session courte.

## Meta Visionnaire E-Myth

La decision strategique issue de la session:

- Visionnaire / Entrepreneur: A0 Amadeus et les apps Codex/Claude/Gemini pour penser,
  architecturer et verifier.
- Manager: Jerry/Summer B1 et Symphony/Hermes routing pour transformer vision en
  packets executables.
- Technicien: Hermes B2/B3 squads pour produire les preuves.

Formule de reprise:

```text
Vision -> Gate -> JTBD -> Proof Packet -> PASS/BLOCKED/CONDITIONAL -> Next Action
```

## Risques Et Restes A Faire

- Hermes Workspace n'etait pas encore prouve par un test UI complet au moment de
  l'archivage de cette session.
- La documentation OpenRouter confirme l'API et le format des model IDs, mais pas une
  preuve locale finale de reponse Hermes UI pour cette session archivee.
- Les configs Hermes doivent rester sans secrets dans les docs.
- Les prochaines sessions doivent etre courtes, orientees preuve, et ne pas recharger
  toute cette conversation comme contexte actif.
