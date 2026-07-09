# WARGAME 24 — Le Rêve de Beth : dreaming out-of-band pour l'auto-apprentissage de la flotte (24/7, GO triennal)

> **WARGAME ORDER** : Tu n'exécutes pas cette mission, tu la wargames. Intent A+ (D3) : après chaque DEAL de WF1 (Protostar clôt le cycle), **Beth rêve** — un process batch hors-bande qui lit les transcripts récents de TOUTE la flotte, en extrait les patterns qu'aucun agent seul ne voit, et livre un DIFF de mémoire. Orchestré par A0-Amodei, sous le GO triennal WF0 de Spock, au service des 12 itérations 12WY de Morty (Curie/SNW structure), exécution L2 par Picard (WF2) via Symphony Plane (Holo Deck/Cerritos), le tout visible dans Pane (cockpit, wargame 18). Sources : Anthropic Dreaming (research preview, talk Mahesh) + Karpathy (Dwarkesh clip) + 2 commentaires YT.

## Statut recon (D1 — vérifié CE run + sources marquées)

| Fait | Preuve |
|---|---|
| **A'Space rêve DÉJÀ en v0 primitif** | `turn-journal.md` 84 805 B (Stop hook, 1 ligne/tour) · worklog 40 lignes · **45 decisions JSONs** · `_LESSONS_APPLIED.md` (mindsets) · hooks `sessionstart-log-digest` + `stop-log-append` actifs. Ce sont des CAPTEURS — la synthèse hors-bande n'existe pas |
| Le pattern Anthropic Dreaming | talk Mahesh (transcript A+) : batch async hors-bande · lit les transcripts multi-agents · produit un diff de mémoire (dédup, purge stale, note de vérification, backfill) · applicable auto OU review avant merge · Harvey ×6 completion, Rakuten −90 % first-pass mistakes — **chiffres vendeur, non re-vérifiés** |
| Le grain de mémoire Anthropic = le nôtre | mémoire = FILESYSTEM (fichiers + bash + grep) — exactement `.claude/memory/` + wiki + mindsets. Scopes read-only (canon/wiki) vs read-write (working) = notre séparation canon/journaux DÉJÀ en place |
| **L'avertissement Karpathy = LA red-team** | clip Dwarkesh : s'entraîner/écrire sur ses propres samples = **collapse silencieux** (distribution effondrée, « 3 blagues ») ; le rêve biologique = injection d'ENTROPIE anti-overfit ; « seek entropy » = parler à d'autres sources |
| Risque concurrence réel | `MEMORY.md` 18 841 B écrit par plusieurs harness/sessions — AUCUN verrou optimiste chez nous (le clobber est possible aujourd'hui) |
| Quota | Fable 93 % — ce wargame = doctrine ; l'exécution = M3/cron post-reset |

## La thèse (D3 — pourquoi c'est BETH qui rêve)

Le dreaming Anthropic est un process ; A'Space lui donne un **propriétaire de sens**. Beth (Ikigai/veto) est le seul A1 dont le mandat est de juger *ce qui mérite d'être retenu* — Morty exécute, Rick protège le kernel, mais **la curation de la mémoire est un acte de meaning, pas de mécanique**. Le rêve de Beth = l'inverse exact de son veto : le veto retranche l'action sans sens ; le rêve retient l'apprentissage qui en a. Et la cadence suit la hiérarchie : **rêve léger après chaque DEAL WF1** (nightly, mécanique M3) · **rêve profond mensuel** (Beth, synthèse) · **méta-rêve après 4 cycles 12WY** (re-distillation des mindsets eux-mêmes — la seule mémoire qui a le droit de se réécrire, gated).

## L'architecture (mapping complet, isomorphie nommée)

```
CAPTEURS (existants)                RÊVE (à construire)                MÉMOIRE (existante, scopes)
turn-journal · worklog              D1 nightly  : dream-agent M3       read-write : journaux, _LESSONS_APPLIED
decisions/*.json · transcripts  →   D2 mensuel  : Beth (synthèse)  →   read-only  : wiki canon, ADRs, mindsets*
evaluator REJECTS · A+ corrections  D3 4-cycles : méta-rêve (gated)    (*mindsets writable UNIQUEMENT par D3)
        └────────── Pane cockpit : le rêve visible dans un pane dédié ──────────┘
```

## MOVES

### M1 — Le dream-runner nightly (D1, mécanique, 0 Fable)
Script + cron (fenêtre 02:00-05:00, la machine dort — abort Beth wargame 23) : un agent M3 lit les transcripts du jour (sessions + turn-journal + decisions JSONs + verdicts evaluator) et produit `dreams/DREAM-<date>.md` : (a) patterns ≥ 2 occurrences cross-sessions, (b) dédup des leçons redondantes, (c) purge des notes staled (avec preuve), (d) note de vérification (« ce souvenir a été confirmé par le transcript X »). **Le diff ne s'applique PAS seul** : il atterrit en `pending`, appliqué au réveil par le premier agent après revue rapide — le mode « review before land » d'Anthropic, notre défaut.
- **Attendu** : 1 DREAM-file/nuit, grep-able, avec `receipt:` par claim (loi wargame 20).
- **Échec probable** : le rêve paraphrase le journal au lieu de trouver des patterns → **contre-action** : le prompt exige le format « pattern = N occurrences × sessions distinctes », une paraphrase sans compte = REJECT evaluator.

### M2 — Le rêve profond mensuel de Beth (la synthèse qui a un propriétaire)
Chaque mois : Beth (agent a1-beth-veto, contexte frais) lit les ~30 DREAM-files + les entrées `_LESSONS_APPLIED` et rend TROIS verdicts de curation : **promouvoir** (journal → MEMORY.md/wiki, l'apprentissage devient canon) · **fusionner** (N notes → 1) · **retirer** (stale → `_TRASH_<date>`, jamais de hard-delete). Sortie : un diff de mémoire signé Beth, appliqué après review A0-Amodei (pas A+ — l'échelle de décision tient).
- **Attendu** : MEMORY.md cesse de gonfler par accrétion (18,8 KB aujourd'hui) — il respire : promotions IN, staleness OUT.
- **Fork** : SI un pattern touche la santé/capacité d'A+ (Life Wheel) → il remonte en signal Beth-veto immédiat, pas en note de mémoire.

### M3 — L'anti-collapse Karpathy (LA contrainte de design, pas une option)
Trois lois gravées dans les prompts de rêve : (1) **jamais rêver sur des rêves** — les inputs de D1/D2 sont les transcripts PRIMAIRES, jamais les DREAM-files précédents (sinon boucle d'auto-consommation = collapse) ; (2) **quota d'entropie** — chaque rêve profond DOIT inclure ≥ 30 % de sources externes au système (corrections A+, REJECTS evaluator, ingest YouTube/last30days, erreurs D6) : les échecs et l'extérieur sont l'entropie, les succès auto-générés sont le collapse ; (3) **le compteur de diversité** — si 3 rêves consécutifs produisent les mêmes patterns (« les 3 blagues »), le rêve se suspend et signale : la mémoire est saturée, il faut du NOUVEAU réel, pas plus de réflexion.
- **Attendu** : les 3 lois en tête de chaque prompt de rêve + le compteur dans le DREAM-file.

### M4 — Le verrou optimiste (la dette découverte par le recon)
MEMORY.md est écrit par plusieurs sessions SANS verrou — le clobber est possible AUJOURD'HUI, dreaming ou pas. Port du pattern Anthropic : hash du contenu lu en tête de tout write mémoire (`# precond: <sha1-court>`) ; si le hash a changé entre lecture et écriture → re-lire, re-merger, jamais écraser. Implémentation : convention de prompt + check dans le dream-runner (pas de nouveau système, D7).
- **Attendu** : zéro perte de mémoire par écrasement concurrent, vérifiable par le version-log git-like du M5.

### M5 — Attribution & histoire (le contrôle enterprise, version pauvre et suffisante)
Chaque diff de mémoire appliqué logge 1 ligne : `qui (agent) · quand · quoi (fichier) · pourquoi (DREAM-ref)` dans `dreams/dream-ledger.md` (append-only). C'est la version history d'Anthropic au coût d'un echo — et l'auditabilité que le méta-rêve D3 consommera.

### M6 — Le méta-rêve des 4 cycles (gated — la mémoire qui se réécrit)
Après 4 cycles 12WY (~1 an, aligné sur le GO triennal Spock) : le méta-rêve relit les 12 rêves profonds + les baselines v2→vN et propose la **re-distillation des mindsets eux-mêmes** (les gates mimétiques ont-ils dérivé ? le harnais enseigne-t-il encore la bonne chose ?). C'est la SEULE écriture autorisée sur les mindsets (scope read-only sinon) — et elle est **gated A+ ratification** : réécrire l'instrument qui mesure est un acte de kernel (frontière S1 Rick).
- **Attendu** : la cadence Beth-mensuelle ⊂ méta-annuel écrite dans CADENCE_12WY (⚡ append).

## ABORT CONDITIONS
1. **Un rêve n'applique JAMAIS son diff sans review** (agent-réveil pour D1, A0-Amodei pour D2, A+ pour D3) — le mode auto-apply d'Anthropic est refusé tant que le compteur de diversité M3 n'a pas 3 mois d'historique propre.
2. Compteur de diversité en alerte (3 rêves identiques) → suspension du rêve, signal, PAS d'augmentation de fréquence (plus de réflexion sur les mêmes données = collapse, Karpathy).
3. Le rêve tourne 02:00-05:00 exclusivement — jamais pendant les sessions actives d'A+ (CPU + concurrence).
4. Les mindsets/ADRs/wiki canon restent read-only pour D1/D2 — toute tentative d'écriture hors D6-gated = boundary violation, kill + signal.

## VERIFICATION RUNS
1. 3 nuits de D1 → 3 DREAM-files avec ≥ 1 pattern compté (« N× sur M sessions ») chacun → **pass**.
2. Test clobber : 2 écritures mémoire simulées concurrentes avec precond-hash → la 2e re-merge au lieu d'écraser → **pass**.
3. 1er rêve profond Beth : MEMORY.md diff avec les 3 verdicts (promote/merge/retire) ET taille stable ou décroissante → **pass**.
4. Quota d'entropie audité : le DREAM-file mensuel cite ≥ 30 % de sources externes (comptées) → **pass**.
5. La preuve d'utilité (le seul juge) : un agent évite une erreur documentée dans un rêve antérieur — 1 cas tracé (`dream-ledger` ref citée dans un transcript) le 1er mois → **pass**, sinon le rêve est un journal de plus (Gwyn/D11, on coupe).

## RED-TEAM PASS
- **Attaque ÉCHOUÉE** : « c'est un journal de plus — vous avez DÉJÀ turn-journal, worklog, decisions, log digest : le rêve est le 5e capteur redondant » — non : les 4 existants sont des CAPTEURS (write-only, per-turn, aucune synthèse) ; le rêve est le premier organe de SYNTHÈSE cross-sessions hors-bande, et la vérif 5 (un agent évite une erreur grâce à un rêve, tracé) le rend falsifiable : s'il ne paie pas en 1 mois, Gwyn le coupe. La frontière capteur/synthèse est architecturale, pas cosmétique. Rien à patcher.
- **Attaque RÉUSSIE → patch intégré** : « le rêve de Beth va s'effondrer EXACTEMENT comme Karpathy le décrit — pas au niveau des poids, au niveau du CORPUS : les rêves nourrissent la mémoire, la mémoire cadre les agents, les agents produisent des transcripts conformes à la mémoire, que le rêve re-confirme — une chambre d'écho où la flotte devient sûre d'elle et stérile, les "3 blagues" à l'échelle du système ». Patch (M3 durci en boucle FERMÉE de falsification) : l'entropie n'est pas une ligne de prompt mais un BUDGET COMPTÉ (≥ 30 % externe, audité vérif 4) ; le compteur de diversité SUSPEND le rêve au lieu d'itérer ; interdiction structurelle de rêver sur des rêves ; et le méta-rêve D3 inclut un test d'entropie de la mémoire elle-même (diversité lexicale/thématique des patterns promus sur 12 mois — une mémoire qui converge est une mémoire qui meurt). Le rêve biologique injecte du bizarre ; le nôtre injecte de l'EXTÉRIEUR — même fonction, source vérifiable.

## SELF-GRADE /12 (SUCCESS-ASPACE)
1-2 ✅ · 3 ✅ forks · 4 ✅ RECON (organes existants inventoriés CE run, clobber-risk découvert, chiffres vendeur marqués non-vérifiés) · 5 ✅ 4 aborts · 6 ✅ 5 runs dont la falsification d'utilité (vérif 5) · 7 ✅ red-team (5e-journal échouée par frontière capteur/synthèse · écho-Karpathy réussie→budget d'entropie compté) · 8 ✅ blind · 9 ✅ D1 (84 805 B, 45 JSONs, 18 841 B cités) · 10 ✅ append-only (dream-ledger, _TRASH, ⚡ CADENCE) · 11 ✅ mapping canon complet (Beth-sens/Morty-exec/Spock-GO/Curie-structure/Picard-WF2/Holo Deck-Plane/Pane-cockpit/A0-Amodei-review) · 12 ✅ Beth (nuits 02:00-05:00, le rêve sert la vie — et le fork Life Wheel court-circuite vers le veto).

**12/12.**
