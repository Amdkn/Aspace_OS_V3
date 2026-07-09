# WARGAME 21 — /fable-mode : le Standard Classe Fable en artefact agnostique, priorité MiniMax-M3

> **WARGAME ORDER** : Tu n'exécutes pas cette mission, tu la wargames — SAUF M1 (création du skill, réversible, intent A+ explicite « je veux la création », dernières heures de quota Fable). Mission : distiller le Standard Classe Fable en UN artefact portable (`/fable-mode`) que TOUT agent intégrant le Harness peut charger — M3 d'abord, puis Hermes/Codex/Gemini/B4 jetables/futurs clients franchise — sans dépendre du modèle Fable ni du harnais complet A'Space.

## Statut recon (D1 — preuves de CE run)

| Fait | Preuve |
|---|---|
| Le skill source existe (Nate/AI Foundations) | fourni intégral par A+ : 5 gates (scope→evidence→attack→verify→report) + standing habits + smells. Vidéo `XTBWVVcF3Pk` |
| Les 6 habitudes de prompting Anthropic | `Downloads/Prompting Fable 5 - Lesson.html` lu CE run (8 169 chars) : why · not-to-do · act-when-enough · prove-it · **no-show-reasoning (Fable-only, fallback silencieux → Opus 4.8)** · say-less. Sources : docs Anthropic officielles |
| `fable-mode` n'existe pas chez nous | `ls .claude/skills/` = 58 skills, `fable-mode` absent (vérifié CE run) |
| **Le harnais A'Space fait DÉJÀ le travail** | `_DISCIPLINE_BASELINES.md §v2` (2026-07-07, TES sessions) : M3 harnaché = reason 78% · before-act 99% · read-edit 49% — **à égalité ou devant Fable réel** (64/92/16). Gap restant : re-eval 48% < Opus 65% |
| Quota Fable | 85 % utilisés, reset dim. 19:00 — ce wargame + M1 = dernier gros geste Fable de la fenêtre |
| Chaîne d'injection existante | WORKER_PROMPT (wargame 19 M3, `citadel/cron/wf1_runner.ps1`) + gates mimétiques dans 17 dispatch mindsets (wargame 17) |

## La nuance qui cadre tout (D3 — sinon on construit un doublon)

**/fable-mode n'ajoute PAS de discipline à M3-dans-CC** — les baselines v2 prouvent que le harnais complet (mindsets + hooks + CLAUDE.md) tient déjà M3 au niveau Fable. Sa valeur est ailleurs, triple :
1. **Format de distribution** : le harnais A'Space = 17 fichiers dispatch + hooks + CLAUDE.md, non-portable. `/fable-mode` = UN fichier, chargeable par n'importe quel agent/harness (la « persona portable » d'ADR-HARNESS-001 appliquée à la discipline).
2. **Couverture des nus** : Hermes, Codex, Gemini, les B4 jetables, les futurs harness clients franchise (PRD-HARNESS-FRANCHISE) ne chargent PAS les mindsets. Eux sont encore au M3-nu 53/50/33.
3. **Le gap re-eval** : la seule métrique encore ouverte (48%) — le skill la durcit avec le « re-decide after every result » du Gate 3, absent en trigger explicite de nos gates actuels.

## MOVES

### M1 — Créer `/fable-mode` adapté M3-first (EXÉCUTÉ ce run)
Adapter le skill Nate avec 4 corrections souveraines (pas un copier-coller) :
- **(a) Habit 5 INVERSÉE pour M3** : « stop asking to show reasoning » est Fable-specific (fallback silencieux → Opus 4.8, lesson §5). Pour M3 c'est le CONTRAIRE : le raisonnement visible est LA métrique mimétique #1 (51→78% sous harnais). Le skill route par modèle : Fable = think privately · M3/autres = raisonne 1 ligne avant chaque action, grep-able.
- **(b) Gate 3 durci re-eval** : « re-decide after every result » devient un marqueur obligatoire `re-eval:` (le gap 48% est LE levier restant, baselines v2).
- **(c) Effort dial mappé** (vidéo 3:18-4:25) : Fable a un paramètre `effort` ; M3 n'en a pas → l'équivalent = longueur d'itération courte + routing table wargame 19 M1 (Fable pense · M3 exécute · petits modèles pour le mécanique). Le skill POINTE la table, ne la duplique pas.
- **(d) Ancrage canon** : chaque gate cite son jumeau A'Space (G1=DoD Una · G2=D1/D2 · G3=refute-first evaluator · G4=real-test hook · G5=D5 receipts) — le skill est le pont, pas un canon concurrent.
- **Attendu** : `~/.claude/skills/fable-mode/SKILL.md` + ligne SKILL_REGISTRY (gate d'intake wargame 16 M3).
- **Échec probable** : le skill récite les gates sans les exécuter (proxy-boolean niveau prompt) → voir red-team.

### M2 — Le contrat côté APPELANT (les 6 habitudes Anthropic)
Les 6 habitudes ne vivent pas dans le skill (elles s'adressent à celui qui PROMPTE, pas à l'agent) → elles s'injectent dans le format TICKET du wargame 19 M2 : contexte 3 lignes = **le why** (habit 1) · abort conditions = **le not-to-do** (habit 2) · « act when enough » anti-survey (habit 3) · verification runs = **prove-it** (habit 4) · consignes courtes = **say-less** (habit 6). Habit 5 : ne JAMAIS mettre « explain your reasoning » dans un prompt destiné à Fable (fallback silencieux) — flag dans le template ticket.
- **Attendu** : template ticket amendé, 1 ligne de renvoi ⚡ dans wargame 19 (pas de réécriture).

### M3 — Câblage dispatch (le skill devient standard d'intégration)
`WORKER_PROMPT v3` : étape (1bis) « charge /fable-mode si la tâche est dure (définition Gate 0 du skill) ». Pour les agents NON-CC (Hermes/Codex/Gemini) : le fichier SKILL.md se colle en préambule système — c'est le test d'agnosticité réel.
- **Fork** : SI Hermes refuse encore d'exécuter derrière une persona (le vice ADR-HARNESS-001) → /fable-mode devient le préambule OBLIGATOIRE de ses dispatches, le standard remplace le personnage.

### M4 — Export franchise (la Méta-Productisation)
`/fable-mode` = le premier artefact du tier PRD-HARNESS-FRANCHISE vendable tel quel : un client qui achète le harnais reçoit d'abord LE fichier de discipline (zéro dépendance à notre canon interne — les ancres A'Space du M1d passent en appendice détachable).
- **Attendu** : version `fable-mode-PORTABLE.md` sans références internes, dans le repo franchise quand il ouvre. GATED : aucune publication sans GO A+.

### M5 — La MESURE (baselines v3, cible chiffrée)
À M+1 : re-run `analyze_discipline_real.py` sur les transcripts des agents ayant chargé /fable-mode. **Cibles : re-eval ≥ 60 %** (48 → vers Opus 65) sur M3-CC ; sur un agent NU (Codex/Hermes + skill seul) : before-act ≥ 80 % (test de la thèse « un seul fichier suffit »). Append `§v3` aux baselines, jamais de réécriture.
- **Échec probable** : impossible d'isoler les sessions « avec skill » → **contre-action** : le skill impose un marqueur d'ouverture `[fable-mode on]` en 1re ligne de réponse — grep-able, c'est le sélecteur d'échantillon.

### M6 — Veille de source (les docs bougent)
Les 4 docs Anthropic cités (prompting-fable-5, effort, refusals-fallback, migration) entrent dans la veille `/last30days` (wargame 15) : si le comportement fallback change, l'habit 5 du skill se ré-évalue — le skill porte sa date de source (2026-07-07).

## ABORT CONDITIONS
1. Le skill dépasse ~250 lignes → il devient un rulebook, exactement ce que la lesson §6 (« say less ») interdit — couper, renvoyer au canon.
2. Un agent utilise /fable-mode pour JUSTIFIER une lenteur (sur-planification d'une tâche triviale) → Gate 0 du skill fait foi : travail simple = pas de gates.
3. M4 export : aucune diffusion externe du fichier sans GO A+ explicite (outward-facing).
4. Habit 5 mal routée (un « show reasoning » injecté à Fable) → risque de réponse Opus silencieuse en croyant payer Fable — le template ticket porte le garde-fou, violation = fix immédiat.

## VERIFICATION RUNS
1. `ls ~/.claude/skills/fable-mode/SKILL.md` + ligne SKILL_REGISTRY → **pass** = les deux existent (M1).
2. 1 ticket WF1 exécuté par M3 avec `[fable-mode on]` + marqueurs `re-eval:` grep-ables dans le transcript → **pass**.
3. 1 dispatch Hermes/Codex avec le fichier en préambule → **pass** = les 5 gates visibles dans SA sortie (agnosticité prouvée).
4. M+1 : baselines §v3 append avec re-eval M3 ≥ 60 % ou l'écart expliqué avec données → **pass**.
5. Compteur d'usage : ≥ 5 chargements réels à J+14 sinon règle Gwyn/D11 (wargame 18 M5) — un skill dormant est un échec honnête, pas un trophée.

## RED-TEAM PASS
- **Attaque ÉCHOUÉE** : « c'est un doublon des mindsets — 79e outil, bloat » — non : périmètres disjoints prouvés par les baselines v2. Les mindsets couvrent M3-dans-CC (déjà à parité) ; /fable-mode couvre les agents NUS (Hermes/Codex/B4/franchise, encore à 53/50/33) + le gap re-eval + le format export. La ligne SKILL_REGISTRY documente cette frontière. Rien à patcher.
- **Attaque RÉUSSIE → patch intégré** : « M3 va RÉCITER les gates au lieu de les exécuter — le proxy-boolean remonte au niveau prompt : `re-eval: ok` collé mécaniquement à chaque tour, les baselines v3 mesureront la présence du marqueur, pas la discipline réelle ». Patch (M5 durci, loi du marqueur substantiel) : un marqueur ne compte que s'il porte du CONTENU spécifique au résultat qu'il suit (`re-eval: le grep retourne 0 → l'hypothèse X tombe, je pivote vers Y`), jamais un token seul ; l'evaluator refute-first (wargame 19 M4) échantillonne les marqueurs et déclasse les vides ; et la mesure v3 croise marqueurs ET métrique comportementale (le re-eval se détecte dans la STRUCTURE des tours, pas dans les labels) — le même double-verrou que l'audit-échantillon Fable du wargame 19 M6.

## SELF-GRADE /12 (SUCCESS-ASPACE)
1-2 ✅ · 3 ✅ forks · 4 ✅ RECON (lesson HTML lue intégralement, 58 skills inventoriés, baselines v2 citées) · 5 ✅ 4 aborts · 6 ✅ 5 runs mesurables · 7 ✅ red-team (doublon échouée par frontière de périmètre · proxy-boolean-prompt réussie→patch marqueur substantiel) · 8 ✅ blind · 9 ✅ D1 (chaque fait sourcé CE run) · 10 ✅ append-only (baselines v3 = append, wargame 19 amendé par renvoi ⚡) · 11 ✅ mapping canon (HARNESS-001 persona portable, gates↔D1-D8, routing wargame 19) · 12 ✅ Beth (abort 2 anti-sur-planification : la discipline ne devient jamais une taxe sur le trivial).

**12/12.**
