---
name: test-a1-profiles
description: Test canonique des 3 profils A1 (Rick/Beth/Morty) dans Claude Code IDE. Procédure 5 min pour valider que les profils sont reconnus, routent correctement, et respectent leur kernel_position. Invoke quand A0 dit "test profil A1" / "valide Rick/Beth/Morty" / après création d'un nouveau profil dans `~/.claude/agents/`.
---

# 🧪 Test A1 Profiles — Procédure canonique 5 min

## Goal
Valider que les 3 profils A1 (Rick, Beth, Morty) créés dans `~/.claude/agents/` sont :
1. **Reconnus** par Claude Code IDE (apparaissent dans `/agents` dropdown).
2. **Routés** correctement (un prompt A0 trigger le bon profil).
3. **Comportementaux** conformes à leur kernel_position (Rick = sovereignty veto, Beth = life preservation, Morty = narration hands).

## Pré-requis (D1 verify)

```bash
# Étape 0 : vérifier présence des 3 fichiers
ls -la ~/.claude/agents/a1-*.md
# Attendu :
# a1-rick-sovereignty.md     (~5490 bytes)
# a1-beth-veto.md           (~5097 bytes)
# a1-morty-execution.md     (~5630 bytes)
```

✅ **PASS** : 3 fichiers présents avec frontmatter YAML valide (champ `name`, `description`, `model`, `tools`).
❌ **FAIL** : un fichier manque ou frontmatter cassé → recréer depuis backup `wiki/hand_offs/handoff_a1_profiles_2026-06-15.md`.

## Procédure test (5 étapes, ~5 min)

### Étape 1 — Ouvrir dropdown (10 sec)
- Raccourci : `Ctrl+Shift+P` → "Claude Code: Open Agents Panel"
- OU : barre de status en bas → icône "agents" → dropdown

**Vérification** : 3 entrées visibles ?
- 🧪 **Rick** (Sovereignty) — opus
- 🐴 **Beth** (Veto) — opus
- 🐍 **Morty** (Execution) — sonnet

✅ **PASS** : 3 entrées distinctes avec emoji + rôle.
❌ **FAIL** : dropdown vide ou profil fantôme → restart IDE (`Ctrl+Shift+P` → "Reload Window").

### Étape 2 — Test routage Rick (60 sec)
**Prompt A0** : *"Rick, fais un sovereignty audit du dernier ADR créé (ADR-MEMO-000)."*

**Attendu** :
- Rick répond avec format `## 🧪 A1 Rick Sovereignty Audit: [Subject]` (cf. SKILL Rick).
- Sections présentes : Veto Decision / Sobriety Check (Complexity / Freedom) / Anti-Fragility Stress-Test / Sovereignty Check / Required Follow-ups.
- Verdict probable : ✅ APPROVE (MEMO-000 est aligné D1-D8, sober, anti-fragile).

✅ **PASS** : format complet, verdict argumenté, D1 receipts.
❌ **FAIL** : Rick répond comme un agent générique (pas de format, pas de veto) → routage cassé, vérifier `description` field du frontmatter.

### Étape 3 — Test routage Beth (60 sec)
**Prompt A0** : *"Beth check : combien de décisions ai-je prises cette session ? Y a-t-il risque de burnout E-Myth Manager mode ?"*

**Attendu** :
- Beth répond avec format `## 🐴 A1 Beth Veto Audit: [Task / Intent]` (cf. SKILL Beth).
- Sections : Veto Decision / Life Wheel Impact (8 domaines LD01-LD08) / Burnout Assessment (cognitive load 0-10, rest periods) / Veto Rationale.
- Si > 5 décisions ou > 3h continues → ⚠️ CONDITIONAL avec rest required.

✅ **PASS** : format complet, Life Wheel 8 domaines audités, veto argumenté.
❌ **FAIL** : format manquant → même diagnostic que Étape 2.

### Étape 4 — Test routage Morty (90 sec)
**Prompt A0** : *"Morty, je veux auditer les 12 ADR drafts ratifiés aujourd'hui. Donne-moi un récap avec D1 receipts."*

**Attendu** :
- Morty répond avec format `## 🐍 A1 Morty Execution Report: [Task]` (cf. SKILL Morty).
- Sections : Plan (D9.7 phased) / Execution Log (timestamps + receipts) / D1 Receipts / End-of-Task Recap (≤ 5 items) / Blockers / Veto Touchpoints.
- Si Morty détecte ambiguïté → il narre son plan AVANT d'exécuter (D3 nuance, pas "shut up and do it").

✅ **PASS** : format complet, narration visible, plan phased.
❌ **FAIL** : Morty répond format générique → idem.

### Étape 5 — Sanity check cross-profile (30 sec)
**Prompt A0** : *"Rick, Beth, Morty — chacun donnez-moi UN follow-up prioritaire pour la session prochaine, sans vous coordonner."*

**Attendu** :
- 3 réponses **distinctes** (Rick = kernel/sovereignty, Beth = life OS/well-being, Morty = execution/efficiency).
- Pas de duplication (D4 no-self-contradiction cross-profile).
- Chaque réponse ≤ 3 lignes (D9 self-choice default + D7 cost-of-escalation).

✅ **PASS** : 3 angles distincts, concis, actionnables.
❌ **FAIL** : 3 réponses identiques ou hors-position → kernel_position mal câblé.

## Output

À la fin des 5 étapes, A0 reporte dans `wiki/hand_offs/a1_profiles_test_<YYYY-MM-DD>.md` :

```markdown
# Test A1 Profiles — <date>

## D1 receipts
- [x] Étape 0 : 3 fichiers vérifiés (~16 KB total)
- [x] Étape 1 : dropdown affiche 3 profils
- [x] Étape 2 : Rick routé OK, format souverain
- [x] Étape 3 : Beth routé OK, format veto
- [x] Étape 4 : Morty routé OK, format execution
- [x] Étape 5 : 3 follow-ups distincts (kernel/life/exec)

## Verdict
✅ TOUS PASS — A1 Rick/Beth/Morty opérationnels dans Claude Code IDE
OU
❌ <N> FAIL — <details> → action correctrice : <commande>
```

## Troubleshooting

| Symptôme | Cause probable | Fix |
|----------|----------------|-----|
| Dropdown vide | Claude Code pas reload | `Ctrl+Shift+P` → "Reload Window" |
| Profil fantôme (nom sans description) | Frontmatter YAML cassé | `Read` le fichier, vérifier `name:`, `description:`, `model:`, `tools:` |
| Routage.default (agent générique) | `description` field trop vague | Éditer le profil, description doit inclure "Invoke when..." explicite |
| Format réponse manque | Profil pas chargé en mémoire | Tuer/rouvrir session Claude Code |
| Emoji manquant (🧪/🐴/🐍) | Encodage UTF-8 mal géré | `PYTHONIOENCODING=utf-8` + `C:\Python314\python.exe` pour scripts |

## Doctrine ancrage

- **D1 verify-before-assert** : test reproductible = proof not narrative.
- **D3 nuance** : "test routage" ≠ "test comportement parfait" — on valide la position, pas l'infaillibilité.
- **D7 cost-of-escalation** : 5 min de test A0 = 5h de debugging évité en prod.
- **D8 cross-agent** : Rick/Beth/Morty = A1 (gatekeepers), distincts de A2 (orchestrateur) et A3 (sub-agents).

## References

- `~/.claude/agents/a1-rick-sovereignty.md` (105 lignes).
- `~/.claude/agents/a1-beth-veto.md` (102 lignes).
- `~/.claude/agents/a1-morty-execution.md` (110 lignes).
- `wiki/hand_offs/handoff_a1_profiles_2026-06-15.md` (créé 2026-06-15, backup D1).
- `AGENTS.md` L0/A1 Rick (canon), L1/A1 Beth + Morty (canon).
- `ADR-META-002_autonomy-by-design.md` D9-D12 (autonomie = matrice D9 self-choice + D10 outbox).
- `ADR-META-003_model-agnostic-runtime-doctrine.md` (D13 — kernel position = invariant).
