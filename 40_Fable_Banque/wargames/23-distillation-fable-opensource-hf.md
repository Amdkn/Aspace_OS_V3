# WARGAME 23 — Distiller Fable vers l'open-source : le mini-Fable souverain d'A'Space (brainstorm armé)

> **WARGAME ORDER** : Tu n'exécutes pas cette mission, tu la wargames. Contexte : Anthropic retire Fable/Mythos de l'abonnement (vidéo source) — le risque de dépendance que le canon nomme depuis juin. Mission : cartographier la distillation Fable → modèles open-source HF pour A'Space, en intégrant les axes A+ (Looped Transformers, RecursiveMAS, Skill-to-LoRA, JEPA, self-evolving RL) — SANS répéter l'erreur du plan Mistral archivé, et SUR le matériel réel.

## Statut recon (D1 — tout vérifié CE run)

| Fait | Preuve |
|---|---|
| **PAS de GPU NVIDIA sur cette machine** | `Win32_VideoController` = Intel UHD Graphics 1 GB. RAM 31,8 GB. LM Studio **non installé**. → le « RTX 4090, 5 h pour un 4B » de la vidéo est IMPOSSIBLE localement. Inference CPU seule envisageable (4B-12B Q4, lent) |
| Les 11 sources existent | 7 arXiv titres confirmés par curl : Loop-Think-Generalize (2604.07822) · Parcae scaling laws looped LMs (2604.12946) · Fully Looped Transformer (2605.18797) · DSpark spec-decoding (2607.05147) · **Skill-to-LoRA (2606.16769)** · JEPA World Models (2606.27014) · Self-Evolving Agents RL (2607.01120). HF ×2 + GitHub ×2 = HTTP 200 (gemma-4-12B-coder-fable5-GGUF · Qwen3-4B-Instruct-2507 · RecursiveMAS · DeepSpec) |
| Précédent D4 : le local-LLM a DÉJÀ été tenté et archivé | `project_mistral_selfhosting_plan_2026_06_15.md` → ARCHIVÉ `_TRASH_2026-06-15_legacy_v0` (MEMORY.md). Wargame 10 (localai-minimax) couvre le versant M3 local |
| La distillation SANS poids est déjà LIVRÉE et mesurée | `_DISCIPLINE_BASELINES.md §v2` : M3 harnaché ≥ Fable réel sur 3 métriques/4. `/fable-mode` (wargame 21) = la méthode en un fichier. `project_fable_to_minimax_distillation_2026_06_15.md` = 12/12 patterns portés |
| Le dataset souverain existe déjà | **1 504 beats Fable-5 RÉELS** (tes sessions, comptés 2026-07-07) + 913 armand0e (24,5 MB `_fable_dl/`) + 22 wargames + traces M3-PASS-evaluator = corpus A'Space-spécifique que PERSONNE d'autre n'a |
| Quota | Fable 90 % utilisés, reset dim. 18:59 — ce wargame = geste Fable de classe « doctrine », exécution → M3/cloud |

## La thèse (D3 — la nuance qui évite le piège de la vidéo)

La vidéo vend « le modèle chez toi » ; la réalité mesurée d'A'Space est **la pyramide des distillations** — chaque étage se paie SEULEMENT si l'étage du dessous plafonne :

```
N3 — POIDS   : LoRA/fine-tune sur traces (la vidéo)      ← GATED : GPU cloud, coût, Rick
N2 — DATASET : curer NOS traces en corpus SFT             ← LE différentiel réel (personne n'a nos traces)
N1 — HARNAIS : /fable-mode + mindsets + gates + evaluator ← FAIT, prouvé ≥ Fable (baselines v2)
```

**Le renversement honnête** : N1 a déjà donné la parité. N3 ne se justifie QUE pour ce que N1 ne peut pas faire — tourner **hors-ligne, souverain, gratuit, sur du matériel banal** (la couche L0 de sobriété : un cerveau de secours si MiniMax OU Anthropic coupe). C'est un hedge de souveraineté, pas une course de performance.

## MOVES

### M1 — La pyramide gravée en doctrine (rien ne saute d'étage)
Écrire la règle : aucune dépense N3 tant que le cas d'usage n'est pas prouvé insoluble en N1/N2. Le précédent Mistral (archivé pour cette raison exacte : complexité sans cas d'usage) devient le garde-fou cité.
- **Attendu** : §pyramide appendé à `project_fable_to_minimax_distillation` (D4 append-only).

### M2 — Le dataset souverain A'Space (N2 — le vrai trésor, coût quasi-nul)
Curer le corpus SFT : (a) 1 504 beats Fable réels, (b) 913 armand0e, (c) les 22 wargames (format rail = exemples de « comment structurer »), (d) **traces M3-harnaché PASS-evaluator uniquement** — la loi de curation : *seules les traces vérifiées entrent* (une trace non-auditée qui entre au training = le mensonge devient un poids). Format : JSONL messages standard HF, script d'extraction M3.
- **Attendu** : `datasets/aspace-fable-traces/` versionné local + carte de provenance par trace (`receipt:` obligatoire, loi wargame 20).
- **Fork** : SI le corpus > 5 000 traces propres → il devient un actif franchise vendable (la « due diligence comportementale » du harnais), gated A+.

### M3 — Skill-to-LoRA : le papier qui EST notre cas d'usage (N3, gated cloud)
arXiv 2606.16769 décrit exactement notre situation : une bibliothèque de skills (77) consommée en tokens à chaque session → apprise en COMPORTEMENTS LoRA = économie de tokens massive. Cible : Qwen3-4B-Instruct-2507 (vérifié HF 200) + LoRA sur le dataset M2. **Pas de GPU local → GPU cloud loué** (RunPod/Vast, ~5-20 $ le run 4B, `assumed:` à deviser). Livrable : `aspace-mini-fable-4B-LoRA`.
- **Attendu** : devis chiffré AVANT tout lancement (abort 2) ; 1er run = 1 seul skill distillé (fable-mode) pour prouver le pipeline bout-en-bout (Gate 2 : passe fine avant d'échelonner).
- **Échec probable** : le LoRA récite sans juger → voir red-team (c'est LE risque du wargame).

### M4 — Le runner local CPU (inference only — ce qui est possible AUJOURD'HUI)
Sans GPU : LM Studio (ou llama.cpp) en CPU, Qwen3-4B Q4 (~2,5 GB, tourne dans 31,8 GB RAM) ou gemma-4-12B-fable5 Q4 (~7 GB, lent mais utilisable). Rôle dans la flotte : **worker B4-tier hors-ligne** — triage, résumés, drafts de nuit — branché à Hermes comme dans la vidéo (endpoint local + clé). PAS un remplacement de M3.
- **Attendu** : test des 7 jours (règle wargame 18 M5) : < 3 usages réels → dormant, désinstallé. L'installation ne crée AUCUNE obligation.
- **Fork** : SI le CPU-inference est trop lent pour tout usage réel → N3 local meurt honnêtement, le hedge devient « dataset prêt + LoRA cloud on-demand » (souveraineté = capacité de reconstruire, pas possession du runtime).

### M5 — Les Looped Transformers & RecursiveMAS : l'isomorphie, pas le build (veille armée)
Lecture D3 : les papiers loop (2604.07822/12946, 2605.18797) font en LATENT ce que notre loop engineering fait en EXPLICITE (wf1 runner, heartbeat, evaluator = un « looped transformer » au niveau système). RecursiveMAS = notre dispatch A1→A2→A3 en librairie. Verdict Rick par défaut : **NO-GO build, GO veille** — on n'importe pas une architecture de recherche dans le kernel ; on vérifie trimestriellement si un checkpoint looped open-source dépasse Qwen à taille égale (alors M3 du wargame se re-évalue).
- **Attendu** : 3 lignes/papier dans la veille `/last30days` + trigger de re-évaluation nommé.

### M6 — JEPA + Self-Evolving RL : le fondement théorique de MiroFish (gated Rick)
2606.27014 (JEPA world models) = la théorie de généralisation dont les sims WF3 sont l'artisanat ; 2607.01120 (self-evolving agents) = la Phase 2 Hermes-style formalisée. Usage : ANCRER les ADR existants (WF3, ADR-LOOP-003) avec ces références — pas de nouveau système. Un agent qui s'auto-modifie au niveau POIDS = anti-paperclip trigger, S1 Rick territoire (~1×/an).
- **Attendu** : 2 renvois ⚡ (plan WF3 + ADR-LOOP-003), 0 nouveau runtime.

## ABORT CONDITIONS
1. **Aucun achat matériel** (GPU) sans GO A+ explicite — le hedge ne justifie pas un capex.
2. **Aucun run cloud N3 sans devis affiché** et plafond accepté (l'échec Mistral = complexité avant cas d'usage ; ici : dépense avant devis).
3. Le mini-Fable ne rejoint JAMAIS la boucle de décision sans passer les MÊMES gates que M3 (evaluator externe, baselines) — un modèle local n'a pas de passe-droit de souveraineté.
4. Beth : le training/inference local ne cannibalise pas la machine de travail d'A+ (le CPU-inference de nuit seulement, jamais pendant les sessions actives).

## VERIFICATION RUNS
1. Dataset M2 : `wc -l` du JSONL + 100 % des traces avec `receipt:` de provenance → **pass**.
2. Pipeline N3 : 1 LoRA 1-skill entraîné cloud, chargé, et le marqueur `[fable-mode on]` + gates apparaissent SANS le skill en contexte → **pass** = le comportement est dans les poids.
3. Baselines v4 : le mini-Fable mesuré au MÊME analyzer (`analyze_discipline_real.py`) vs M3-nu et M3-harnaché → **pass** = position chiffrée, pas déclarée.
4. Runner local : 7 jours, compteur d'usages réels → verdict keep/dormant honnête.
5. Économie Skill-to-LoRA : tokens/session AVANT vs APRÈS (le skill en contexte vs le comportement en poids) → **pass** = réduction mesurée, sinon le papier ne tient pas chez nous.

## RED-TEAM PASS
- **Attaque ÉCHOUÉE** : « c'est le plan Mistral bis — il finira dans _TRASH comme l'autre » — non : trois différences structurelles prouvées. (1) Mistral n'avait pas de cas d'usage ; ici le cas est nommé et borné (hedge souveraineté + Skill-to-LoRA token-économie, chacun avec sa vérif chiffrée). (2) Mistral visait le runtime local comme fin ; ici la pyramide subordonne N3 à l'échec prouvé de N1/N2 — et N1 est déjà livré. (3) Le test des 7 jours + les aborts de dépense rendent la mort honnête et bon marché. L'attaque est en fait ABSORBÉE comme garde-fou (M1 cite l'archive Mistral). Rien à patcher de plus.
- **Attaque RÉUSSIE → patch intégré** : « le student model apprend les GESTES sans le JUGEMENT — un mini-Fable 4B exécutera le théâtre des 5 gates avec l'assurance de Fable : c'est le proxy-boolean descendu au niveau des POIDS, incurable par prompt puisque le prompt est devenu le modèle ». Patch (triple verrou M2+M3+aborts durci) : (a) **curation d'entrée** — seules les traces PASS-evaluator entrent au dataset : on ne distille jamais un mensonge bien formaté ; (b) **le mini-Fable est un B4 permanent** — jamais evaluator, jamais juge, toujours jugé (abort 3) : ses sorties passent l'evaluator M3/Fable comme n'importe quel worker ; (c) **la mesure comportementale v4** (vérif 3) note la STRUCTURE réelle des tours, pas les marqueurs — un théâtre de gates sans re-décision réelle score bas exactement comme M3-nu scorait. Le jugement reste dans le SYSTÈME (harnais + evaluator), les poids ne portent que les réflexes — c'est la définition assumée du student model.

## SELF-GRADE /12 (SUCCESS-ASPACE)
1-2 ✅ · 3 ✅ forks (corpus-actif-franchise · mort-honnête-du-local) · 4 ✅ RECON (GPU/RAM/LM-Studio vérifiés, 11 sources curlées, 2 mémoires précédent lues) · 5 ✅ 4 aborts · 6 ✅ 5 runs chiffrables · 7 ✅ red-team (Mistral-bis échouée→absorbée en garde-fou · gestes-sans-jugement réussie→triple verrou) · 8 ✅ blind · 9 ✅ D1 (le fait matériel brutal EST la colonne vertébrale du plan) · 10 ✅ append-only (pyramide appendée, renvois ⚡) · 11 ✅ mapping canon (pyramide N1-N3, B4-tier, S1 Rick, wargames 10/18/20/21 cités) · 12 ✅ Beth (abort 4 : la machine d'A+ n'est jamais cannibalisée).

**12/12.**
