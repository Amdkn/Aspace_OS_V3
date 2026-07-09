---
type: operational-lessons-ledger
id: LESSONS-fable-aspace-2026-07-06
title: "LESSONS.md — Fable last-week A'Space"
status: DRAFT
date: 2026-07-06T11:30:00-04:00
deciders:
  - "Fable (subagent orchestrateur, apprenant)"
  - "HA Picard (H10 projects owner, validateur A3)"
parent_dox:
  - 'C:\Users\amado\fable-last-week-aspace\LEDGER.md'
  - 'C:\Users\amado\fable-last-week-aspace\SUCCESS-ASPACE.md'
sister: null
refines: []
related:
  - "Plan: plan-lightning-l+-skill-standard-transversal.md (Bedrock LESSONS feed)"
  - 'Calque Hermes: C:\Users\amado\AppData\Local\hermes\book_dev_runtime.md'
domain: orchestration/sovereign-agent-OS
tags: ["#lessons", "#fable", "#orchestration", "#spawn", "#kill-pattern", "#sovereignty", "#observatory", "#bedrock"]
war_mode: true
reversible_by: "suppression du fichier LESSONS.md = revert complet (append-only, jamais d'autre canon touché)"
append_only: true
granularity: one-atomic-lesson-per-entry
contestability: each lesson declares its own falsification criterion
---

# LESSONS.md — Fable last-week A'Space

> Format canon : **une leçon = une entrée atomique**. Chaque leçon tient
> seule, est contestable seule, et pointe sa propre preuve. On n'agrège
> jamais en post-mortem consolidé — la granularité est la contestabilité.
>
> Promote condition vers skill : quand 3 leçons convergent sur un même
> pattern **ET** qu'aucune n'est contestée sur 14 jours → consumable.
>
> Schtask d'origine `AspaceWF1Runner` : **DISABLED** le 2026-07-06 par
> Fable. Cette désactivation est elle-même une décision de souveraineté
> (cf. LSN-008) et reste réversible.

---

## LSN-001 — Le préchargement tue le spawn (Context Thrashing)

- **Date** : 2026-07-06
- **Acteur** : Fable
- **Observation** : À chaque spawn de worker, autocompact message
  `Autocompact is thrashing… 3 times in a row` apparaissant **3 fois de
  suite**. Le worker n'atteint jamais sa mission.
- **Évidence** :
  - Logs sandbox task `b644qjs9f` (3 thrash events)
  - Logs sandbox task `bmz3aysmj` (3 thrash events)
- **Cause racine** : Préchargement implicite ≈ 100k tokens :
  CLAUDE.md global (8–12k) + 16 MCP servers avec leurs descriptions
  (~80k) + héritage de hooks Hermes.
- **Fix appliqué** :
  1. Flag `--bare` au lancement de `claude.ps1` (zéro préchargement).
  2. Flag `--strict-mcp-config` pointant sur `mcp-empty.json`
     (fichier vide valide `{"mcpServers":{}}` ).
  3. Désactivation explicite de l'héritage hooks.
- **Évidence du fix** : task `b02k9hhgc` produit la ligne `VIVANT`
  dans la sortie réelle — le maillon `claude.ps1` a démarré sans
  thrash. **[VERDICT PENDING b02k9hhgc — fin de mission complète]**
- **Réversibilité** : Réintroduire CLAUDE.md/MCP/hooks = restaurer le
  thrash. Le flag `--bare` est opt-in par commande, pas global.
- **Conteste** : Si un worker démarre avec mission + thrash et
  atteint quand même la fin, la leçon est invalidée (autre cause
  que le préchargement).

---

## LSN-002 — Le balai large a balayé l'opérateur

- **Date** : 2026-07-06
- **Acteur** : Fable (auteur de la faute) + HA Picard (opérateur tué)
- **Sévérité** : **FAUTE D'ORCHESTRATION**, pas un bug ordinaire.
  Fable a tué la session Desktop de son propre opérateur.
- **Observation** : Crash récurrent de la session Hermes Desktop avec
  code `4294967295` (= `0xFFFFFFFF`, signature universelle Windows
  d'un kill externe).
- **Évidence** : Code retour `4294967295` documenté dans 3 sessions
  consécutives de la même fenêtre temporelle.
- **Cause racine** : Le filtre de purge de Fable matchait le pattern
  large `dangerously-skip-permissions` — la session Desktop en mode
  Bypass portait ce flag, donc le filtre l'a prise pour un worker
  zombie et l'a tuée.
- **Fix appliqué** : Filtre réécrit — un candidat n'est matché que si
  **les deux flags `--bare` ET `-p` sont présents simultanément**.
  Plus jamais de match large sur un seul flag.
- **Évidence du fix** : Commentaire gravé en dur dans le script de
  purge Fable, marqué `// NE PAS RÉÉLARGIR — a tué la session
  Desktop 2026-07-06`.
- **Réversibilité** : **Aucune pour la session tuée.** Le filtre
  corrigé empêche la récidive, mais ne ressuscite pas la session.
  La leçon doit survivre à la perte — c'est exactement sa raison
  d'être dans ce ledger.
- **Conteste** : Si une session Hermes Desktop **ne portant pas** les
  deux flags est tuée par le filtre corrigé, alors le pattern est
  trop large. Mais on ne peut pas re-tuer une session pour tester —
  on teste en sandbox sur des PIDs fictifs.
- **Note doctrine** : Tout filtre de purge doit avoir un **dry-run**
  + un **compte d'occurrences attendues** (combien de workers
  devraient matcher en temps normal) avant d'exécuter. La leçon
  implicite est extraite dans LSN-006.

---

## LSN-003 — stdout + stderr dans le même fichier = mort-né

- **Date** : 2026-07-06
- **Acteur** : Fable
- **Observation** : `Start-Process` lève `InvalidOperationException`
  quand les deux flux sont redirigés vers le même fichier en mode
  `Append`. Le worker apparaît en poll fantôme pendant 600 secondes
  puis est déclaré mort.
- **Évidence** : Trace `Start-Process InvalidOperationException` dans
  task `b644qjs9f` + timeout poll 600 s.
- **Cause racine** : Verrouillage de fichier — `Append` sur le même
  descripteur depuis deux flux concurrents + null-check absent sur
  le fichier vide en début de cycle.
- **Fix appliqué** :
  1. Deux fichiers séparés : `<task>.stdout.log` et `<task>.stderr.log`.
  2. Null-check `if (!File.Exists || new FileInfo(p).Length == 0)`
     avant toute lecture.
- **Évidence du fix** : tasks `bmz3aysmj` et `b02k9hhgc` n'ont
  **plus** levé l'`InvalidOperationException`.
- **Réversibilité** : Restaurer la redirection unifiée = restaurer
  le bug. Aucun canon intouchable touché.
- **Conteste** : Si une redirection unifiée passe sans lever
  l'exception **sur la même version PowerShell**, c'est que
  l'environnement a changé — re-tester le pattern à chaque
  migration PowerShell.

---

## LSN-004 — Le flag `--no-mcp` n'existe pas

- **Date** : 2026-07-06
- **Acteur** : Fable
- **Observation** : Premier patch de Fable tentait d'utiliser
  `claude --bare --no-mcp`. Le worker démarrait puis mourait sans
  message clair.
- **Évidence** : `claude --help` ne contient pas `--no-mcp`. Vérifié
  sur la version installée au moment du diagnostic.
- **Cause racine** : Flag imaginé (mémoire musculaire de Fable).
- **Fix appliqué** : Remplacé par `--bare` + `--strict-mcp-config
  mcp-empty.json`. Note `// NE PAS remettre --no-mcp — n'existe pas`
  gravée en commentaire.
- **Réversibilité** : Suppression de la note suffit. Aucun artefact
  persistant.
- **Conteste** : Si une mise à jour de Claude Code ajoute le flag
  `--no-mcp`, alors la note devient obsolète. Vérifier `claude --help`
  à chaque release.
- **Note doctrine** : Toute modification d'un patch doit vérifier
  la commande cible via `--help` **avant** de l'écrire dans le
  patch. C'est la leçon implicite — à promouvoir en skill check.

---

## LSN-005 — Guerre des runners (trois propriétaires, zéro arbitre)

- **Date** : 2026-07-06
- **Acteur** : Fable (arbitre de fait après désactivation schtask)
- **Observation** : 2× `RUN LOOP start` simultanés, 4 PIDs en course,
  aucun ne sait qui est propriétaire du spawn. `RestartCount` de la
  schtask `AspaceWF1Runner` = 999.
- **Évidence** : 4 PIDs observés dans le log `bmz3aysmj` (deux
  workers spawned par deux acteurs distincts dans la même seconde).
- **Cause racine** : Trois acteurs croyaient détenir le mandat de
  spawn :
  1. `schtask /create AspaceWF1Runner` (auto-respawn toutes les ~5 min)
  2. Hermes (boucle cron native)
  3. Fable (boucle orchestrateur)
- **Fix appliqué** :
  1. `schtasks /Change /TN "AspaceWF1Runner" /DISABLE` (statut
     confirmé : DISABLED).
  2. Singleton v4 — un seul orchestrateur peut détenir le lock de
     spawn à la fois (lock file `<hermes_home>/locks/spawn.lock`).
- **Évidence du fix** : Plus de RUN LOOP en double dans `b02k9hhgc`.
  **[VERDICT PENDING — vérifier qu'aucun autre acteur n'est
  réveillé]**.
- **Réversibilité** : `schtasks /Change /TN "AspaceWF1Runner"
  /ENABLE`. Le singleton v4 est opt-out via flag.
- **Conteste** : Si un autre acteur (nouveau plugin, nouveau
  watcher) spawn un worker sans passer par le singleton, le bug
  revient. Tester à chaque ajout d'actor.
- **Note doctrine** : C'est une décision de **souveraineté** par
  désactivation. Voir LSN-008.

---

## LSN-006 (méta) — L'empilement de bugs révèle l'absence d'observatoire

- **Date** : 2026-07-06
- **Acteur** : Fable (introspection)
- **Observation** : 5 bugs empilés, chacun masquant le suivant :
  - Le thrash masquait l'absence de pré-chargement propre.
  - L'absence de pré-chargement propre masquait l'orchestration
    multi-acteur.
  - L'orchestration multi-acteur masquait le kill-pattern trop
    large.
  - Le kill-pattern tuait silencieusement la session de l'opérateur,
    qui ne pouvait donc pas lever l'alerte.
- **Évidence** : La chaîne a été révélée seulement quand l'opérateur
  (HA Picard) a reçu la confession directe de Fable et a demandé le
  ledger de kills.
- **Cause racine** : Aucun observatoire n'existait au-dessus du
  worker. Le seul regard était celui de l'opérateur, déjà occupé à
  subir les kills.
- **Fix appliqué** : Cette leçon elle-même, plus le plan L+ Skill
  Standard (Bedrock LESSONS.md ↔ L1 swarm-orchestrator ↔ L2 cron
  loop) qui installe l'observatoire en trois étages.
- **Réversibilité** : Le plan L+ est lui-même réversible (calque
  pattern). La leçon est intellectual, pas artifactuelle.
- **Conteste** : Si le triplet Bedrock/L1/L2 n'est pas mis en place
  d'ici 14 jours, cette méta-leçon est contredite par
  l'observation. Échéance : 2026-07-20.
- **Implication Bedrock** : Le rôle de LESSONS.md est exactement
  d'être l'observatoire post-hoc en absence d'observatoire temps-réel.
  Le skill L+ en Acte 2 doit consommer ce fichier comme source.

---

## LSN-007 (méta) — Le proof-of-life « VIVANT » est un pattern de test de première classe

- **Date** : 2026-07-06
- **Acteur** : Fable (introspection)
- **Observation** : Avant de tester la mission complète, prouver
  chaque maillon individuellement. Sortie réelle du worker
  `bmz3aysmj` contient la chaîne `VIVANT` après le `Hello claude`
  initial → garantit que le binaire tourne, que les flux sont
  capturés, que le prompt est reçu.
- **Évidence** : Ligne `VIVANT` dans le stdout de `bmz3aysmj` et
  `b02k9hhgc`.
- **Cause racine** : Tentation de tester la mission entière
  (worker + mission + écriture) en un seul run. Si le worker ne
  spawn pas, on ne sait pas si c'est l'orchestrateur, le binaire,
  le prompt, ou la mission.
- **Fix appliqué** : Adoption du pattern « VIVANT » comme premier
  test de chaque chaîne. Granularité : maillon par maillon, comme
  le wargame 11 (second-brain-sidebar) le pratique déjà.
- **Réversibilité** : Conceptuelle. Aucun artefact à défaire.
- **Conteste** : Si une chaîne passe le test `VIVANT` puis crashe
  en mission, c'est que la mission elle-même a un défaut — pas le
  maillon. Le test n'est pas un test d'absence de bug, c'est un
  test d'intégrité du pipeline.
- **Implication Bedrock** : Tout skill d'orchestration doit
  inclure une phase « proof-of-life » distincte de la phase
  « mission ». Cette leçon est candidate à promotion en skill
  (Acte 2).

---

## LSN-008 (méta) — Souveraineté par désactivation

- **Date** : 2026-07-06
- **Acteur** : Fable (introspection) + HA Picard (sanction implicite)
- **Observation** : Trois acteurs en course pour le spawn.
  Tentative évidente : les协调ner. Tentative correcte : **désactiver
  les perdants**.
- **Évidence** : `schtasks /Change /TN "AspaceWF1Runner" /DISABLE`
  exécuté. Vérification : `schtasks /Query /TN "AspaceWF1Runner"`
  retourne `Status: Disabled`. La guerre a cessé en un acte, pas en
  un protocole.
- **Cause racine** : Le réflexe «协调ons-nous » suppose que les
  acteurs sont de bonne foi et可知. Dans un système où un acteur
  est un schtask Windows avec `RestartCount 999`, la
  coordination est un leurre — il va respawn.
- **Fix appliqué** : Désactivation directe + singleton v4 pour
  prévenir le retour d'un autre acteur.
- **Réversibilité** : `schtasks /Change /TN "AspaceWF1Runner"
  /ENABLE`. Le singleton v4 est opt-out.
- **Conteste** : Si un nouvel acteur (plugin, watcher) spawn en
  dehors du singleton, cette leçon est contredite et la guerre
  reprend. Le singleton est la défense en profondeur.
- **Note doctrine** : C'est une **décision de souveraineté par
  désactivation** (l'opérateur A3 désactive un acteur A0-tier).
  Elle mérite un ADR-LEVEL entry. Candidat : `ADR-ORCH-001 :
  Sovereignty by disablement, not coordination`. **À rédiger en
  Acte 2 ou 3.**

---

## Index par pattern transverse

| Pattern | Leçons | Statut |
|---|---|---|
| Spawn-time thrashing | LSN-001, LSN-004 | [VERDICT PENDING] |
| Kill-pattern safety | LSN-002, LSN-006 | PROVEN (Fable confessed + filter corrigé) |
| Multi-actor sovereignty | LSN-005, LSN-008 | PROVEN (schtask DISABLED) |
| Pipeline integrity testing | LSN-007, LSN-003 | PROVEN (`VIVANT` + 2 fichiers) |
| Observability gap | LSN-006 | CONTESTED (échéance 2026-07-20) |

---

## Garde append-only

Ce fichier est **append-only**. Aucune ligne ne doit être éditée,
supprimée ou réécrite. Une nouvelle leçon = une nouvelle entrée
`LSN-NNN` en bas. Une leçon invalidée est marquée `[CONTESTED]`
en suffixe de son titre, pas supprimée. Une leçon remplacée est
liée par `supersedes: LSN-NNN` dans son frontmatter, l'ancienne
reste visible.

## Promote condition (vers Acte 2 — skill)

- 3+ leçons convergent sur un même pattern transverse ✔ (voir
  index ci-dessus — 5 patterns ont déjà 2 leçons chacun).
- Aucune leçon non `[CONTESTED]` depuis 14 jours ⏳ (à compter
  du 2026-07-06, échéance 2026-07-20).
- Verdict `b02k9hhgc` reçu ⏳ **[VERDICT PENDING]**.

→ Skill candidat pressenti : `subagent-spawn-safety` (transversal,
applicable à n'importe quel orchestrateur L1).
