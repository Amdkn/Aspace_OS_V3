---
type: OKF-0.2
id: "gtd-cerritos-intent-capture"
layer: "L1"
created: "2026-09-01"
statut: APPLIQUÉ
source: "Brainstorming Amadou (transcription video Rob Shocks — Anthropic AI-native SDLC) + arbitrage A0"
---

# INTENT.MD — le contrat d'entrée de la chaîne d'artefacts

## 1. Ce que c'est

`intent.md` = **le premier artefact de la chaîne** : capture du "Pourquoi" à la
source (l'Originator = Amadou, ou tout agent en maintenance autonome). Il est
human-readable et machine-actionable. Il vit dans `_INBOX/` (file d'émergence
existante) et suit le test du ruban jusqu'à devenir une spec.

## 2. La chaîne complète A'Space (mesurée — réutilisée, pas réinventée)

```
[ Originator / Maintenance autonome ]
        │ (interview agent / auto-diagnostic)
   intent.md   ── dans _INBOX/<couche>/ ── le "Pourquoi" + contraintes non-négociables
        │ (Yaz/amy/clara = Spec, transforme ou refuse)
   spec.md     ── dans 60_Tape_Specs/ (format OKF existant: Objectif+Sources+Artefacts+Critères+Périmètre)
        │ (Beth teste au portier — gate.py, 4 contrôles binaires)
   claim       ── ryan/nardole/rory (uc.db: claim + bail + prédiction ANTÉRIEURE)
        │
   build       ── preuve par critère (evidence)
        │
   review/done ── doctor13/11/12 + Beth détache
        │
   eval        ── Donna (dlq.py) ramasse les échecs, escalade; les leçons -> learning/
```

**Ce qui existe déjà (ne pas re-créer)** : spec.md en OKF 0.2 avec critères
d'acceptation exécutables (preuve: `2026-09-01-spec-distillation-l2-bornee.md`),
uc.db avec lois SQL, Kanban observabilité, Herdr visibilité, Donna DLQ, crons
Docteurs. **Ce qui manquait**: le formate INTENT standardisé + l'agent
intervieweur.

## 3. Format INTENT.MD (contrat d'entrée)

```markdown
# INTENT: [nom-courte-initiative]
**Layer:** L0 | L1 | L2
**Originator:** Amadou | <agent en maintenance>
**Date:** YYYY-MM-DD
**Statut:** DRAFT | FROZEN

## 1. Irritant réel
Pourquoi maintenant ? Quel goulot ? Pourquoi les approches force-brute échouent ?

## 2. Résultat visé (mesurable)
L'état final vérifiable — pas la solution.

## 3. Contraintes non-négociables
- Budget tokens/coût max
- Blast radius (dossiers touchés / interdits)
- Garde-fous souverains (validation humaine si impact $ > 0)

## 4. Definition of Done
- [ ] Critère 1 (commande exécutable)
- [ ] Critère 2 (commande exécutable)
```

**Règle**: une intent sans critère mesurable retourne à l'Originator (test du
ruban s'applique dès l'intent). Statut FROZEN = Yaz peut produire la spec.

## 4. L'agent Intervieweur (protocole "Grill Me")

Rôle tenu par **Yaz** (Spec, spécialité SecOps — il écrit déjà les rubans).
Protocole : lit la déclaration brute de l'Originator → pose 3-5 questions
d'edge-cases (persistance, volume, vetos, coûts) → compile dans
`_INBOX/<layer>/intent-<slug>-<date>.md` → demande FROZEN. Zéro question
d'évidence : les questions ne portent que sur ce qui n'est pas déductible.

**En maintenance autonome** (la boucle fermée Anthropic): Donna qualifie un
échec → rédige son propre intent.md de diagnostic (famille d'échec + preuve)
→ le dépose dans `_INBOX/S1_Rick/` → Rick tranche → Yaz spec → cycle.

## 5. Mapping des outils (corrigé du brainstorming Gemini — réel, pas supposé)

| Étape | Artefact | Outil RÉEL A'Space | (Gemini supposait — faux) |
|---|---|---|---|
| Capture | intent.md | Herdr pane Yaz / Hermes Desktop / maintenance autonome | Google Chat, Talon |
| Spécification | spec.md OKF 0.2 | `60_Tape_Specs/` + gate.py | Notion PARA |
| Découpage | work + claim + prédiction | uc.db + Kanban Hermes | ClickUp, Airtable |
| Exécution | build + evidence | Compagnons Herdr visibles + Git | MCP/n8n |
| Audit | dlq.py + certificats | Donna + 50_Distillation OKF | Supabase Sentinel |
