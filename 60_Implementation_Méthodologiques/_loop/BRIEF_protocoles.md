# BRIEF — les protocoles d'agents, version approfondie

## Ton perimetre EXCLUSIF en ecriture

```
C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/protocoles/
C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_protocoles.md
```

## Le point de depart, deja etabli

Une premiere recherche a pose ces faits, **verifies** :

- **DeepSeek Harness (`dsh`)** est bati sur **Cordis**
  (`github.com/cordiverse/cordis`). MIT, Node.js, preview developpeur,
  principe « tout est un greffon ».
- Les protocoles sont des **couches**, pas des rivaux : MCP (outils), A2A
  (agent a agent, Linux Foundation), AG-UI (interface, SSE), ACP-Zed
  (editeur), UCP/AP2 (commerce).
- **`ACP` est ambigu** : Zed (Agent Client Protocol), IBM (Agent
  Communication Protocol, heritage FIPA-ACL), et un protocole de commerce
  partagent le sigle.

Le concept complet est dans
`C:/Users/amado/ASpace_OS_V3/40_Memory_Wiki_OKF/architecture/cordis-runtime-et-couches-de-protocoles.md`.
**Lis-le d'abord** : il te dit ce qui est deja acquis, donc ce qu'il ne faut
pas refaire.

## Sources a exploiter

```
https://github.com/cordiverse/cordis
https://github.com/deepseek-ai/deepseek-harness
https://agentclientprotocol.com/
https://modelcontextprotocol.io/
https://thenewstack.io/deepseek-harness-open-source-plugins/
https://www.digitalapplied.com/blog/ai-agent-protocol-ecosystem-map-2026-mcp-a2a-acp-ucp
https://arxiv.org/pdf/2606.31498      (Governance Gaps in Agent Interoperability Protocols)
https://arxiv.org/pdf/2602.11327      (Security Threat Modeling for Emerging AI-Agent Protocols)
```

**Si tu n'as pas d'acces web**, dis-le en tete de rapport et travaille
uniquement sur ce que le poste contient deja. **N'invente aucune
specification.** Un protocole decrit de memoire est un protocole faux.

## Ce qu'on attend

Des concepts OKF v0.2 dans `protocoles/`, un par protocole traite, chacun
repondant a quatre questions :

1. **Quelle couche** occupe-t-il, et que reliet-il exactement ?
2. **Quel transport et quel format** — JSON-RPC ? SSE ? HTTP ? stdio ?
3. **Que faudrait-il pour l'implementer dans Coach OS**, sachant qu'il a deja
   neuf adaptateurs dont un serveur MCP stdio et une surface MCP Apps ?
4. **Quel risque** — gouvernance, surface d'attaque, instabilite d'API ?

Traite au minimum : MCP, A2A, AG-UI, ACP (les trois sens), UCP, AP2, et les
deux arxiv sur la securite et la gouvernance.

Termine par **une page de synthese** qui repond a : *dans quel ordre les
implementer, et lesquels ne pas implementer du tout.*
