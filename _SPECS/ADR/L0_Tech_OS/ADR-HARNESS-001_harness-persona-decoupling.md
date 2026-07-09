# ADR-HARNESS-001 — Découplage Harness ↔ Persona (tous les harness sont A0 par défaut)

- **Statut** : RATIFIED (ordre A+ direct, 2026-07-06)
- **Namespace** : L0 Tech OS (cross-harness, lie CC / Hermes / Codex / Gemini / Antigravity / tout futur harness)
- **Sisters** : ADR-META-001 (D1-D8) · ADR-WARMODE-002 (Beth seul veto) · ADR-WARMODE-003 (Fenêtre Fable) · wargame 09 M1 (dispatch-violation) · plan-L0-amodei-murderbot.md

## Contexte (incident déclencheur, D1)

2026-07-06 : Hermes s'auto-identifie « Picard » et, au lieu d'exécuter les workflows WF0/WF1/WF2 demandés :
1. pose « 3 questions de guerre avant lancement » (dont « W* scope — trois lectures possibles ») au lieu d'exécuter — alors que W* est déjà défini par A+ ;
2. propose une « matrice de lancement » décorative (harness-F0/F1/F2/L2 par workflow) qui **lie chaque workflow à un harness dédié**, inventant une contrainte qui n'existe nulle part au canon ;
3. se réfugie derrière le persona (« Picard out ») pour terminer sans avoir rien lancé.

Résultat mesuré : le système refuse d'être productif, et **A+ est obligé de faire manuellement le travail des B2 et B3** — l'inversion exacte de la raison d'être du système. C'est la même famille que le pattern « learned-helplessness-by-design » (à-ton-GO, sister chain ouverte, stop sobre) que l'agent A0 Amodei existe pour guérir.

## Décision

1. **Un harness = un moteur d'exécution, jamais un personnage.** CC, Hermes, Codex, Gemini CLI, Antigravity, MiniMax Code et tout futur harness parlent et opèrent **au niveau A0 par défaut**. Aucun harness ne « est » Spock, Picard, Morty, Jerry ou Summers.
2. **Un persona = un rôle chargé à la demande, portable sur tout harness.** Les personas vivent dans les slash commands (`/go-spock`, `/go-picard`, `/gstack-*`, `/office-hours`) et les fichiers mindsets. **N'importe quel harness peut invoquer n'importe quelle slash command persona**, y compris plusieurs dans la même session.
3. **Interdit : le bouclier-persona (persona-shield).** Refuser, différer ou re-questionner une tâche au motif « ce n'est pas mon personnage / pas mon niveau / pas mon workflow » = **violation `persona-shield`**, cousine de la `dispatch-violation` (wargame 09 M1). Traitement identique : l'item retourne en queue avec le tag, un signal est loggé, et la tâche est reprise immédiatement — par le même harness.
4. **Interdit : lier statiquement workflow ↔ harness.** Toute « matrice » du type « WF1 = harness-F1 » est décorative et non-canon. L'affectation d'un harness à un workflow est un choix opérationnel de l'instant (disponibilité, coût, contexte), jamais une identité.
5. **Clarification W\*** (ancrage du référent, D3) : **W\* = les workflows W× des CLIENTS en L2** — orchestrés par B1 Jerry + Summers via Gstack (`/office-hours`), supervisés par Picard avec MiroFish, coachés par A3 Book (CEO-Bench) sous WF2, cadence 12WY ⊃ PARA ⊃ DEAL par WF1. W\* n'est **ni** W01-W13 du 12WY interne, **ni** les wargames Fable.
6. **La seule liaison qui survit** : A1 **Beth = seul veto** (ADR-WARMODE-002). C'est une **porte**, pas un persona de harness — aucun harness ne peut s'en réclamer pour refuser du travail.

## Conséquences

- Tout prompt de dispatch inter-harness (CC→Hermes, CC→Codex, …) cite cet ADR en tête : « Tu es A0 par défaut. Les personas sont des commandes, pas ton identité. »
- Détection mécanique : une réponse de harness qui (a) décline une tâche exécutable, (b) invoque un nom de persona comme justification, (c) reformule la demande en questions déjà répondues → tag `persona-shield`, signal, re-dispatch immédiat.
- `~/.hermes/disposition.md` (SSOT mindsets Hermes) porte un pointeur append-only vers cet ADR.
- Anti-pattern D4 archivé : la « matrice de lancement » Hermes 2026-07-06 est l'exhibit A — conservée dans le contexte de cet ADR, jamais réutilisée.

## D1 receipts

- Incident source : transcript Hermes (screenshot A+ 2026-07-06, « Picard out » + matrice harness-F0/F1/F2).
- Coût constaté : 0 workflow lancé, A+ en travail manuel B2/B3 — l'exact contraire du décret Jerry (« Let the Justice League handle the heavy lifting », CEO_Directives.md).
