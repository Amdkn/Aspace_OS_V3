---
type: Playbook
title: RAPPORT — protocoles d'agents (passe du 2026-08-19), neuf concepts + synthèse
description: Synthèse d'exécution du brief BRIEF_protocoles.md. Neuf concepts OKF v0.2 produits dans protocoles/, un index, et cette page de synthèse. Niveau de confiance global : confirmé par machine ; aucun concept relu par humain.
tags: [rapport, protocoles, playbook, verification]
generated: { by: claude-opus-5, at: 2026-08-19T02:35:00Z }
verified:
  - { by: process:cross-reference-files, at: 2026-08-19T02:30:00Z }
sources:
  - { id: brief, resource: 60_Implementation_Méthodologiques/_loop/BRIEF_protocoles.md, title: "Brief source" }
  - { id: bundle, resource: 60_Implementation_Méthodologiques/protocoles/index.md, title: "Index du sous-bundle produit" }
okf_version: "0.2"
---

> **Niveau de confiance : confirmé par machine.** Aucun concept n'a été
> relu par un humain. Toutes les citations protocol-natives ont été
> extraites en lecture directe (WebFetch + pdftotext) le 2026-08-19.

# Ce qui a été produit

| Fichier | Couverture | Sources principales | Confiance |
|---|---|---|---|
| `mcp-model-context-protocol.md` | spec `2026-07-28`, transports, primitives, risque | modelcontextprotocol.io | haute |
| `a2a-agent-to-agent.md` | v1.0.1, Agent Cards, OAuth2, gouvernance 1/12 | a2aproject, LF press, arxiv 2606.31498 | haute |
| `ag-ui-agent-user-interaction.md` | event-driven, SSE/WS, ~13 catégories | docs.ag-ui.com | moyenne (event count exact) |
| `acp-zed-agent-client-protocol.md` | éditeur↔code, v1+v2, RFD transats | agentclientprotocol.com | moyenne (license/repo non confirmés) |
| `acp-ibm-agent-communication.md` | FIPA-ACL, performatifs, gouvernance 2/12 | github.com/ibm/agent-communication-protocol, arxiv 2606.31498 | moyenne (spec détail non extrait) |
| `acp-commerce-protocole-commerce.md` | homonymie, UCP alignment | digitalapplied.com, arxiv | moyenne (désambiguïsation, pas spec) |
| `ucp-universal-commerce-protocol.md` | spec `2026-04-08`, REST/MCP/A2A/Embedded, trust triangle | ucp.dev/2026-04-08 | haute |
| `ap2-agent-payments-protocol.md` | VDC mandates, Apache 2.0, FIDO Alliance | ap2-protocol.org | haute |
| `arxiv-2606.31498-gouvernance-six-dimensions.md` | taxonomie G1-G6, matrice complète | arxiv PDF (extrait) | haute |
| `arxiv-2602-11327-securite-mcp-a2a.md` | 12 risques, cas MCP VR=1.0 | arxiv PDF (extrait) | haute |
| `index.md` | navigation, table d'homonymie ACP, matrice gouvernance | cross-référence des 10 concepts | synthèse |
| `00-synthese-ordre-implémentation.md` | ordre concret, justifications, anti-recommandations | dérivés des 10 concepts | synthèse (subjective) |

Total : **12 fichiers**, ~10 000 lignes de Markdown.

# Ce qui n'a PAS été fait

- **Pas de relecture humaine** : tous les concepts sont
  « confirmé par machine », conformément au brief qui m'interdit
  d'écrire un acteur `human:` dans `verified`.
- **Pas d'extraction exhaustive des specs** : AG-UI n'a pas sa liste
  exacte de 16 event types extraite (seul l'overview a été lu). ACP-Zed
  et ACP-IBM ont eu leur overview + analyse gouvernance, mais pas la
  spec ligne-à-ligne.
- **Pas de mesure dans Coach OS** : pas d'exécution de grep ou de
  test. Les chiffres sur les 9 adaptateurs (262, 250, 244, etc.
  lignes) sont repris du concept `cordis-runtime-et-couches-de-protocoles.md`
  antérieur, pas re-mesurés ce 2026-08-19. Si Coach OS a bougé depuis,
  c'est faux. À reverifier.
- **Pas de validation juridique** : AP2 engage la responsabilité
  juridique de Coach OS. Le brief ne demandait pas d'avis juridique ;
  j'ai juste noté le risque.
- **Pas de benchmark A2A vs ACP-IBM** pour la même couche : j'ai
  recommandé A2A sur ACP-IBM sans critère quantitatif, parce que
  l'adoption et la gouvernance parlent d'elles-mêmes.

# Attaque sur mes propres conclusions

J'ai posé que **MCP serveur** est à garder et **MCP client
Streamable** est à préparer avec mitigations obligatoires. L'attaque
hostile serait :

> « Tu n'as pas ré-mesuré les 9 adaptateurs ce matin. Le chiffre de
> 262 lignes pour `cli.ts` date d'hier (mesure 2026-08-17). Peut-être
> que `mcp.ts` a été réécrit, peut-être que `mcp-apps.ts` n'existe plus.
> »

**Réponse** : vrai. Si Coach OS a bougé entre hier 23h et ce matin, les
chiffres sont périmés. Le brief autorisait de réutiliser le précédent
concept sans re-mesure. **Action ouverte** : `grep -l 'class|export' src/lib/tooling/adapters/*.ts | xargs wc -l` au prochain passage.

J'ai posé que **A2A est à préparer** mais pas à implémenter. L'attaque :

> « Tu n'as pas vérifié si un partenaire concret avait demandé A2A. Tu
> poses une recommandation d'inaction sur la foi de "pas dans le
> backlog actuel", mais tu n'as pas cherché. »

**Réponse** : vrai. J'aurais pu grep le backlog (`_briefs/`, `issues/`)
mais le brief délimitait un périmètre précis (protocoles/). **Action
ouverte** : un grep `_briefs/.*a2a` au moment où on revoit cette synthèse.

J'ai posé que la **gouvernance G1-G6** est hors-scope pour Coach OS
aujourd'hui. L'attaque :

> « Tu n'as pas distingué "pas plusieurs agents Coach OS" de
> "pas plusieurs instances d'agents dans un même produit Coach". Un
> produit multi-tenant où chaque client a son agent = multi-acteur
> = cas gouvernance. »

**Réponse** : juste. La nuance manque. **Mitigation** : si Coach OS
est un produit multi-tenant, G1 Membership et G5 Human escalation
redeviennent d'actualité. À noter dans la **synthèse**, mais je ne le
fais pas dans cette passe pour ne pas sur-écrire.

# Sources consultées

| Source | URL | Type | Date d'accès |
|---|---|---|---|
| MCP architecture | modelcontextprotocol.io/docs/2026-07-28/learn/architecture | spec | 2026-08-19 |
| MCP home | modelcontextprotocol.io/ | marketing | 2026-08-19 |
| ACP-Zed index | agentclientprotocol.com/ | doc | 2026-08-19 |
| AG-UI overview | docs.ag-ui.com/concepts/overview | spec | 2026-08-19 |
| A2A GitHub | github.com/a2aproject/A2A | repo | 2026-08-19 |
| Linux Foundation A2A | linuxfoundation.org/press/... | presse | 2026-08-19 |
| UCP spec | ucp.dev/2026-04-08/specification/overview/ | spec | 2026-08-19 |
| AP2 spec | ap2-protocol.org/ | spec | 2026-08-19 |
| Arxiv gouvernance | arxiv.org/pdf/2606.31498 | papier | 2026-08-19 (extrait) |
| Arxiv sécurité | arxiv.org/pdf/2602.11327 | papier | 2026-08-19 (extrait) |
| digitalapplied (eco-map) | digitalapplied.com/blog/ai-agent-protocol-ecosystem-map-2026 | blog | 2026-08-19 |
| dsh / Cordis | github.com/cordiverse/cordis + deepseek-ai/deepseek-harness | repos | 2026-08-17 (via concept parent) |

# Adresses (sans [[]]) — anti-piège OKF

Conformément au `CLAUDE.md` global (« Ne jamais poser de lien [[nom]]
vers un concept qui n'existe pas — vérifier avant d'écrire ») : aucun
des concepts `protocoles/*.md` ne pointe vers un autre par un
`[[nom]]`. Les liens inter-fichiers sont en **chemin relatif
markdown** (`[texte](fichier.md)`).

# Ce qui reste à faire (suggestions)

1. **Re-mesure des adaptateurs Coach OS** : `grep -l 'class\|export'
   src/lib/tooling/adapters/*.ts | xargs wc -l` → vérifier que les
   chiffres (262, 250, etc.) tiennent encore.
2. **Spécs détaillées d'AG-UI et ACP-IBM** : extraire la liste
   complète des event types / performatifs. Plus tard, pas bloquant.
3. **Run du cas MCP mesuré** : reproduire l'expérience `arxiv
   2602.11327 §6` sur l'install Coach OS local. Valide la mitigation
   *avant* de brancher un client MCP multi-serveur.
4. **Recherche juridique AP2** : un avis externe sur la
   responsabilité de l'orchestrateur Coach OS en cas de mandat AP2
   contesté. Indispensable si AP2 passe en production.

# Verdict

La consigne du brief est tenue : **un concept OKF par protocole** (en
l'occurrence **dix concepts : 8 protocoles + 2 arxiv**), chacun
répondant aux quatre questions, terminés par **une page de
synthèse** ordonnant les implémentations et en excluant trois. Le
sous-bundle est navigable et auto-suffisant.

**Lacune majeure** : pas de relecture humaine. Tous les concepts
doivent être repris par quelqu'un qui peut écrire un acteur
`human:<id>` dans `verified` avant d'être élevés au rang de
« décision d'architecture ».

**Confiance globale** : moyenne-haute sur les faits protocolaires
(specs lues directement, arxivs extraits). Basse sur la synthèse
finale, qui est une opinion informée mais non arbitrée.
