# ⚡ÉVOLUTION 2026-07-03 — TSTwin ≠ Twin (harmonisation staging, pas destruction)

**D1 verdict** : `05_OSS_TSTwin` et `05_OSS_Twin` ne sont PAS la même version.
- TSTwin md5 (INDEX_capsules.md): `270e1fbfdbcc7a3409408e1bc8c9217b`
- Twin md5 (INDEX_capsules.md): `7c9a56875cfbcbe4c76a0f639aaa9f74`

**Twin contient en exclusivité** (non-réversible — donc pas de TRASH) :
- `L0/open-hermes-runtime.md`, `L0/SDD-010_shadow-L0-IA.md`, `L0/shadow-ai-capability-routing.md`
- `L2/symphony-airtable.spec.md` + `WORKFLOW.solaris-*`, `WORKFLOW.growth-*`, `symphony-clickup.spec.md`, `symphony-notion.spec.md`, `symphony-sheets.spec.md`
- `loops/b1-solaris-loop.draft.md`
- `scripts/symphony-tick-demo.{ps1,sh}`, `scripts/symphony-ui-server.py`, `scripts/ui`
- `agent-os/.claude/commands/agent-os/{discover,index,inject,plan,shape}-standards.md`
- `BRIDGE.rock-l2-to-growth.draft.md`

**Action GO A0 2026-07-03** : TRASH annulé.
- TSTwin = staging figé (précédente livraison avant L0 SDD + B1 Solaris loop)
- Twin = canon vivant

**Conventions** : TSTwin sert de **miroir archivé** pour rollback ponctuel ; Twin est la source canonique des L0/L1/L2. Les opérations d'écriture symphony → Twin uniquement.

**REFUSE de hard-delete** : action refusée par D1 + risque de perte d'anciennes capsules de référence (bkp prod).
