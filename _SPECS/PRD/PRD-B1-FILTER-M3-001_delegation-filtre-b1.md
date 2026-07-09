# PRD-B1-FILTER-M3-001 — Délégation du B1-filter au modèle M3 (CC)

- **Statut** : ACTIVE (ordre A+ 2026-07-06 : « Crée tous les PRD et Skills nécessaires pour déléguer le B1-filter au Model M3 de CC »)
- **Sisters** : ADR-L2-BDLD-MAP-001 (bijection 8↔8 RATIFIED — la table de vérité) · `/youtube-to-guide` §6 (amendé ce jour) · skill `/b1-filter` (créée ce jour) · PRD-PORTFOLIO-B1-FRANCHISE (consommateur : les 7 PRD héritent de guides bien classés) · ADR-META-001 D1-D8

## 1. Problème (D1, constaté sur les 4 indexes + 1 fichier)

Chaque distillation `/youtube-to-guide` sans contexte B1 produit un mapping LD **aléatoire** (exhibit : `_kIxjlEf_0U.md` avec `ld: LD06_Family_Burnham` + `domain: 06_Sales` — la bijection canon dit Sales=LD05_Stamets). Pire, constaté ce jour : **les `_INDEX.md` eux-mêmes ont dérivé** :

| Index | Dit (faux) | Canon D3 (ADR-L2-BDLD-MAP-001) |
|---|---|---|
| `02_Ops/_INDEX.md` | « LD02_Finance_Saru mirror » | **LD01_Book** (Ops=Operation=Business) |
| `06_Sales/_INDEX.md` | « LD01_Business mirror » | **LD05_Stamets** (Sales=Social) |
| `07_Growth/_INDEX.md` | « LD07_Creativity_Reno mirror » | **LD08_Georgiou** (Growth=Impact) |

D6 root cause : le filtre était une consigne humaine (« B1 Jerry lit l'INDEX ») jamais mécanisée — exactement la laziness M3 mesurée que les mindsets existent pour compenser, sauf qu'ici la solution est encore plus sobre : **une table de lookup n'a pas besoin d'un LLM**.

## 2. Décision d'architecture — déterministe d'abord, M3 ensuite

Le B1-filter se décompose en 2 étages :

| Étage | Nature | Exécutant | Coût |
|---|---|---|---|
| **E1 — Cohérence** `domain ↔ ld ↔ b2_owner ↔ squad` | Lookup pur (bijection D3 = 8 lignes) | `b1_filter_sweep.py` (script, zéro token) | 0 |
| **E2 — Classification** (fichier SANS `domain:` exploitable) | Jugement de contenu → 1 des 8 domaines | **Agent M3** (effort low, 1 fichier = 1 agent, prompt court) | ~2-5k tokens/fichier |

Règle : **E2 ne se déclenche que sur le résidu d'E1.** Un fichier dont le dossier parent est `0X_<Domain>/` a déjà son domaine — le script corrige `ld`/`b2_owner` sans réveiller aucun modèle. M3 ne classifie que les orphelins (fichiers plats hors dossiers domaine, frontmatter absent).

## 3. La table de vérité embarquée (copie conforme ADR-L2-BDLD-MAP-001 §D3)

| Dossier | LD canon | Officier A3 | B2 owner | Squad B3 |
|---|---|---|---|---|
| 01_Product | LD04_Cognition | Tilly | b2-03-flash-product | Avengers |
| 02_Ops | LD01_Business | Book | b2-02-batman-ops | Fantastic Four |
| 03_IT | LD07_Creativity | Reno | b2-06-cyborg-it | Kang Dynasty |
| 04_Finance | LD02_Finance | Saru | b2-07-wonderwoman-finance | Thunderbolts |
| 05_Legal | LD03_Health | Culber | b2-08-aquaman-legal | Eternals |
| 06_Sales | LD05_Social | Stamets | b2-05-johnjones-sales | Illuminati |
| 07_Growth | LD08_Impact | Georgiou | b2-04-superman-growth | Guardians |
| 08_People | LD06_Family | Burnham | b2-01-greenlantern-people | X-Men |

Toute divergence entre un fichier/index et cette table → **la table fait foi** (D4 de l'ADR bijection).

## 4. Livrables (créés ce jour)

1. **Skill `/b1-filter`** (`~/.claude/skills/b1-filter/`) — 3 modes : `audit` (rapport, zéro mutation) · `fix` (corrections déterministes E1) · `classify` (résidu E2 via agents M3). Frontmatter enrichi append-only : jamais de suppression de champs existants.
2. **Script `b1_filter_sweep.py`** — le moteur E1 : parse frontmatter, vérifie contre la bijection, rapporte/corrige. Idempotent, re-run safe.
3. **Amendement `/youtube-to-guide` §6** — le gate à la source : toute NOUVELLE distillation doit produire le bloc `b1_filter` complet (la table est DANS le skill, plus besoin de deviner) ; sinon le guide naît `status: UNFILTERED` et le sweep le rattrape.
4. **Ce PRD** — le contrat.

## 5. Workflow cible (boucle fermée)

```
/youtube-to-guide (nouveau guide) ──§6──► frontmatter b1_filter complet à la naissance
                                              │
guides legacy (~156) ──► /b1-filter audit ──► rapport violations
                              │                    │
                              ├── E1 fix (script, déterministe, 0 token)
                              └── E2 classify (agents M3, orphelins seulement)
                                              │
                              WF1 worker (backlog §2b) peut exécuter le sweep en loop
```

## 6. Critères d'acceptation (D1)

1. `b1_filter_sweep.py --audit` produit un rapport : N fichiers OK / N violations E1 / N orphelins E2.
2. Après `--fix` : re-run audit → 0 violation E1 (idempotence prouvée par le 2e run).
3. 1 orphelin classifié par agent M3 avec justification 1 ligne dans le frontmatter (`b1_reason:`).
4. Les 3 `_INDEX.md` dérivés corrigés (⚡ÉVOLUTION append, pas de réécriture d'historique).
5. Zéro mutation d'un fichier RATIFIED ou d'un intouchable (le script ne touche QUE `01_Guides/`).

## 7. Anti-patterns interdits

- ❌ Envoyer les 156 guides à M3 « pour être sûr » — la bijection est un lookup, pas un jugement (Sobriété).
- ❌ Réécrire le frontmatter entier — patch additif des champs manquants/faux uniquement.
- ❌ Corriger `ADR-L2-AAAS-001` (RATIFIED) là où ses tags divergent — la supersession D4 est déjà gravée, on n'édite pas le canon.
- ❌ Cron automatique sans A0 GO (ADR-SOBER-002 Posture C) — le sweep est on-demand ou via backlog WF1 existant.
