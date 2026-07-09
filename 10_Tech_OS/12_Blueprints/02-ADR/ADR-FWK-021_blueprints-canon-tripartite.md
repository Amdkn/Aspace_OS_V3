# ADR-FWK-021 — Canon Tripartite des Blueprints (L0 / L1 / L2)

**Date de décision :** 2026-05-22
**Auteur :** A0 Amadeus + A2 Claude Code (Architecte)
**Statut :** RATIFIÉ — partiellement amendé par [ADR-FWK-022](ADR-FWK-022_quick-access-summers-and-inbox-pattern.md) (annule la mention de `_SPECS\_INBOX\` § D1, le reste de la doctrine tripartite L0/L1/L2 reste valide)
**Type :** Architecture Decision Record (Framework)
**Portée :** L0 Tech OS · L1 Life OS · L2 Business OS · `_SPECS\` ~~(désormais zone d'inbox)~~ → archivé dans PARA Archives
**Ancré sur :** ADR-007 (Trust Zone V2) · ADR-002 (Portabilité) · `AGENTS.md` (Canon Absolu)

---

## Contexte

`C:\Users\amado\ASpace_OS_V2\_SPECS\` est devenu un fourre-tout. Audit 2026-05-22 :

- **Triple casse** sur les conventions : `ADR/` vs `adrs/` · `PRD/` vs `prds/` vs `02_V1_PRD/` · `SDD/` (1 fichier) coexiste avec 12 SDDs à plat dans la racine `_SPECS\`.
- **Tous les niveaux mélangés** : décisions L0 (`ADR-RICK-*`, SDD-001..010), L1 (`ADR-FWK-PARA/Ikigai/12WY/GTD/DEAL`, PRD-V0.2.6..V0.2.9), L2 (`ADR-MCP`, `ADR-MEM`, `ADR-NET`, `ADR-AGKIT`, `ADR-ALA`) cohabitent sans namespace clair.
- **Canon L0 réel déjà propre** : `10_Tech_OS\12_Blueprints\01-SDD\` contient 13 SDDs `kebab-case` numérotés 000→010. C'est le modèle.
- **Canon L1 et L2 inexistants** : `20_Life_OS\` et `30_Business_OS\` n'ont pas de dossier `Blueprints\` propre — tout fuite vers `_SPECS\` racine.

Conséquences observées :
- Agents A3 perdent du temps à chercher la source de vérité d'une décision
- Risque de drift : un même ADR peut être édité dans `ADR\` et `adrs\` sans détection
- Memory_Core et LLM_Wiki ne savent pas quel **shadow** (L0/L1/L2) doit refléter une décision donnée

## Décision

**Chaque niveau possède son canon Blueprints, structuré identiquement.**

```
10_Tech_OS\12_Blueprints\        ← Canon L0 (Rick / Tech OS)
  ├── 01-SDD\
  ├── 02-ADR\
  ├── 03-PRD\
  └── 04-DDD\

20_Life_OS\28_Blueprints\        ← Canon L1 (Beth & Morty / Life OS)
  ├── 01-SDD\
  ├── 02-ADR\
  ├── 03-PRD\
  └── 04-DDD\

30_Business_OS\09_Blueprints\    ← Canon L2 (Jerry & Summer / Business OS)
  ├── 01-SDD\
  ├── 02-ADR\
  ├── 03-PRD\
  └── 04-DDD\

_SPECS\                          ← DEPRECATED comme canon
  └── _INBOX\                    ← Brouillons en cours, migrés vers L0/L1/L2 une fois mûrs
```

### Règles de routage

Un blueprint vit dans le canon du niveau qu'il **gouverne**, pas celui qui le consomme :

| Préfixe | Niveau cible | Exemple |
|---------|--------------|---------|
| `ADR-RICK-*`, `SDD-000..004`, `ADR-FS-*` | **L0** `10_Tech_OS\12_Blueprints\` | Sovereignty, kernel, filesystem |
| `ADR-FWK-PARA/Ikigai/12WY/GTD/DEAL`, `PRD-V0.2.6..V0.2.9`, `SDD-005`, `SDD-008` | **L1** `20_Life_OS\28_Blueprints\` | PARA, Ikigai, 12WY, GTD, DEAL, Wheel |
| `ADR-MCP-*`, `ADR-MEM-*`, `ADR-NET-*`, `ADR-AGKIT-*`, `ADR-ALA-*`, `SDD-006`, `SDD-007`, `SDD-009` | **L2** `30_Business_OS\09_Blueprints\` | Business Pulse, secteurs DC, intégrations MCP, mémoire L2 |
| `ADR-FWK-021` (ce document) | **L0** (gouverne les 3 niveaux, owner = Rick) | Doctrine transversale |

### Convention de nommage (immuable)

```
<TYPE>-<NAMESPACE>-<NNN>_<kebab-case-slug>.md
```

- `<TYPE>` ∈ {`SDD`, `ADR`, `PRD`, `DDD`}
- `<NAMESPACE>` ∈ {`RICK`, `FWK`, `FS`, `MCP`, `MEM`, `NET`, `AGKIT`, `ALA`, `BIZ`, `SEC`, …} — créé ad-hoc, jamais renommé
- `<NNN>` = compteur 3 chiffres, monotone par namespace
- `<kebab-case-slug>` = obligatoire, lowercase, tirets

Plus jamais : `adrs/` (minuscule), `prds/`, `02_V1_PRD\`, fichiers à plat dans `_SPECS\` racine, suffixe `_V0.X` mélangé au type.

### Migration `_SPECS\` → canons L0/L1/L2

`_SPECS\` n'est **pas supprimé** — il devient `_SPECS\_INBOX\` : zone de **brouillons / drafts** avant ratification. Tout fichier ratifié migre vers son canon de niveau.

La migration des 50+ fichiers existants est traitée en **ADR-FWK-022** séparé (à venir), pour ne pas mélanger doctrine et opération.

## Conséquences

### Positives
- Source de vérité unique par niveau, agents A3 trouvent les specs sans chercher
- `Shadow_L0` / `Shadow_L1` / `Shadow_L2` mappent 1:1 sur les canons Blueprints
- Plus de doublons casse (`ADR/` vs `adrs/`)
- Numérotation par namespace = aucune collision même avec 20 préfixes
- LLM_Wiki peut indexer par niveau via path-prefix

### Négatives
- Migration manuelle des 50+ fichiers existants (ADR-FWK-022)
- Tous les liens internes existants vers `_SPECS\…` deviennent stale → grep+sed massif à prévoir
- Onboarding nouveau agent = doit apprendre la règle de routage

### Neutres
- Le namespace `FWK` reste partagé entre L0 (doctrines transversales comme cet ADR) et L1 (PARA/Ikigai/12WY structures). Distinction par contenu, pas par préfixe.

## Propagation obligatoire

Toute création/édition d'un Blueprint déclenche :

1. **Shadow report** dans `00_Amadeus\30_MEMORY_CORE\Shadow_L<N>\` (NN_topic-YYYYMMDD.md)
2. **Entity wiki** dans `LLM_Wiki\wiki\entities\entity_<slug>.md`
3. **Ligne log** dans `LLM_Wiki\wiki\log.md`
4. **Handoff** si exécution Codex/Gemini requise : `LLM_Wiki\wiki\hand_offs\handoff_<date>_<topic>.md`

## Références

- ADR-007 — Paradigm Shift V2 / Trust Zone (fondateur)
- `AGENTS.md` § Hiérarchie A'Space (L0/L1/L2)
- `10_Tech_OS\12_Blueprints\01-SDD\` (modèle de structure éprouvé)
- ADR-FS-001 — Junction-Based Aliasing (corollaire opérationnel de ce canon)
