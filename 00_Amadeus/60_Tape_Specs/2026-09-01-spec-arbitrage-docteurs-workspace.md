---
titre: Arbitrage Docteurs + application mapping renommages dans l'app Workspace
spec: yaz_spec_l0
date: 2026-09-01
work: L0
---

# Ruban — Arbitrage Docteurs / Workspace V2

## Objectif

Consolider l'arbitrage des 3 Docteurs (L0/L1/L2) en un document OKF 0.2 et
l'appliquer : écrire le mapping slug→libellé dans l'app Workspace
(`C:/Users/amado/agent-os/desktop/src/apps/Workspace/`) en respectant le
cahier des charges fusionné (vues L0/L1/L2, HALT Beth, A SOURCER).

## Critère d'acceptation

- [ ] Arbitrage documenté avec les 3 propositions citées par session : `python -c "print(open(r'C:/Users/amado/ASpace_OS_V3/50_Distillation/ARBITRAGE_DOCTEURS-20260901.md').read().count('session 2026'))"` (>= 3)
- [ ] Mapping JSON slug→libellé présent dans l'app Workspace : `python -c "import json;json.load(open(r'C:/Users/amado/agent-os/desktop/src/apps/Workspace/mapping.json'))"`
- [ ] Le mapping couvre les 17 profils : `python -c "import json;m=json.load(open(r'C:/Users/amado/agent-os/desktop/src/apps/Workspace/mapping.json'));print(len(m))"` (>= 17)
- [ ] Le code Workspace utilise le mapping (aucun nom en dur) : `python -c "s=open(r'C:/Users/amado/agent-os/desktop/src/apps/Workspace/index.tsx').read();print('mapping.json' in s)"`
- [ ] Compilation TypeScript propre : `cd C:/Users/amado/agent-os/desktop && npx tsc --noEmit -p tsconfig.app.json` (exit 0)

## Périmètre

- `50_Distillation/ARBITRAGE_DOCTEURS-20260901.md` (écrit, intégré)
- `agent-os/desktop/src/apps/Workspace/` : mapping.json + index.tsx
- Interdits : renommer un dossier de profil (slug = clé stable), toucher au
  schéma uc.db, cumuler Build et Review.

## Interdits

- Modification de `kernel/schema.sql` sans ADR.
- Passage `confiance: machine` → `confiance: humain` sans Amadou.
