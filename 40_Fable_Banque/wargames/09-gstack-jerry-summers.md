# WARGAME 09 — Gstack (B1 Jerry+Summers, Lighting L2) : l'orchestration qui ne code jamais

> Wargamé par Fable 5, 2026-07-06 sous GO Picard (le point faible du shotgun). Exécuteur : **MiniMax M3**
> (rails blind OBLIGATOIRES — c'est précisément le Lighting où la paresse mesurée M3 frappe : le gatekeeper
> qui exécute lui-même au lieu de dispatcher). Roster ADR-CANON-001 strict.

## RECON (fait — D1)
- **Décret Jerry** (CEO_Directives.md, 142b, lu) : « Just keep the lights on and don't make me do math. Let the Justice League handle the heavy lifting. » = la Loi de dispatch en une ligne.
- **Shims sobres posés** (ADR-LD01-014, vérifiés) : `/gstack-ship` (Summers, SHIP gated) · `/gstack-cso` (Aquaman+Cyborg, DLP/OWASP) · `/gstack-autoplan` (signal→plan). `/office-hours` = NATIF au clone `shadow-l1-garrytan-gstack/office-hours/` : 2 modes (brainstorm / « is this worth building »), gbrain (prior ceo-plans, builder-profile, design-doc history).
- **Contexte frais** : cadence Dark Factory **CAP ×4** (GO Picard, task cap-compression-x4) — le Gstack tick hérite du cap.
- Triptyque canon : T1 People/Ops/IT · T2 Product/Growth/Sales · Duo Finance/Legal. 8 B2 → 53 B3.

## MOVES

**M1 — Le Gstack tick (le métronome de Jerry)**
- Action : par WK — Jerry lit (a) le dernier `book-loop-*.json` (dont `mirofish_governor` — l'oreille posée au wargame 08) et (b) les rapports MiroFish projet s'ils existent → détermine le Triptyque actif (cap ×4 : J1-J7 mappés sans accélération) → **dispatche** les B2 du Triptyque (jamais plus de 3 B2 par pass) → collecte leurs sorties → Summers compose le verse.
- Observation attendue : un tick = 1 entrée worklog `[gstack]` listant les B2 dispatchés + le path du verse. **Zéro artefact technique produit par Jerry lui-même.**
- Échec probable : **Jerry exécute au lieu de dispatcher** (THE M3 laziness, 53 % reason / 33 % real-test) → **cause** : dispatcher coûte un raisonnement, exécuter coûte zéro. **Contre-action mécanique** : trigger de détection = un diff montre du code/contenu produit dans le tour de Jerry SANS trace de dispatch B2 → l'item retourne en queue tag `dispatch-violation` + signal à Book. Le B1 qui écrit du code = alarme, pas un rendement.
- Fork : SI aucun B2 du Triptyque actif n'a de squad B3 dispo → route B2 du Triptyque suivant, JAMAIS exécution directe.

**M2 — La Loi en contrat (gatekeeper décide+route, n'exécute jamais)**
- Action : graver dans `loops/domains/w-star/` (et le futur contrat gstack) la triple règle : Jerry DÉCIDE+ROUTE · B2 DISPATCHE sa squad · B3 EXÉCUTE+rapporte. Chaque niveau ne fait QUE son verbe.
- Observation : grep du contrat : les 3 verbes, un par niveau, avec l'anti-pattern nommé.
- Échec probable : la chaîne s'écrase en cascade molle (B2 exécute aussi) → **contre-action** : même trigger qu'en M1, appliqué à chaque niveau — un B2 qui produit du livrable final = `dispatch-violation`.

**M3 — Le verse de Summers (preuve, pas poésie creuse)**
- Action : format verse = 1 fichier/WK/client : (a) ce qui a été livré — **chaque livrable cité par son PATH** ; (b) la valeur en langage client (variant ICP : Nexus ⚖️ conformité) ; (c) la suite. ≤ 300 mots.
- Observation : verification run = `Test-Path` de chaque path cité → 100 % existants.
- Échec probable : narration optimiste (verse écrit depuis le plan, pas les fichiers) → **contre-action** (héritée wargame 03 M4) : `done` = artefact + verse qui le cite — double preuve ou retour queue.

**M4 — Les 4 /office-hours simulées (l'entraînement avant le réel)**
- Action : 4 sessions `/office-hours` du clone natif, mode « is this worth building », UNE par persona+cas : (1) Marcus Vance × Chef de Cabinet Souverain ; (2) Clara Sterling × migration anti-Jevons ; (3) David Kross × SOPs→Skills ; (4) **cas interne** : « le forfait 1000$/mo est-il worth building tel quel ? » (le système se grille lui-même). Chaque session → `ceo-plan` gbrain + résumé en signal `office-hours-sim-N`.
- Observation : 4 signaux produits, chacun avec un verdict et ≥1 objection non résolue (une simulation sans objection = simulation complaisante, à refaire).
- Fork : SI le gbrain du clone ne persiste pas (config `~/.gstack/` absente) → sortie en fichier signal direct, pas de dépendance dure.

**M5 — Économie du tick**
- Action : budget par tick Gstack : ≤ 3 B2 dispatchés, ≤ 9 B3 réveillés (3/squad), sous plan fixe MiniMax. Full sweep 53 B3 = INTERDIT hors WK13 (pipeline, jamais one-shot — canon dispatch).
- Observation : le worklog du tick liste ≤ 12 agents touchés.

## ABORT CONDITIONS
1. `enable_wf1.flag` absent (cascade fermée) → aucun dispatch, signal `gate-closed`.
2. Un dispatch exigerait un envoi client externe → outboard gated (3 cycles verts) → la séquence s'arrête au livrable interne + verse.

## VERIFICATION RUNS
1. Après 1 tick : worklog `[gstack]` avec B2 dispatchés + path verse ; `Test-Path` des paths du verse = 100 %.
2. grep `dispatch-violation` dans signals = 0 (ou chaque occurrence a sa remédiation tracée).
3. Les 4 signaux `office-hours-sim-*` existent, chacun avec verdict + objection.

## RED-TEAM PASS
- **Échouée** : « la Loi des 3 verbes ajoute de la bureaucratie » — non : elle SUPPRIME le travail du mauvais niveau ; le tick coûte moins cher qu'un B1 qui code mal.
- **Réussie → patch** : « M3 contourne le trigger M1 en faisant produire le livrable par un B2 fantôme (dispatch cosmétique : le B2 n'est qu'un nom dans le log) » — patch : le dispatch n'est valide que si la sortie B2/B3 porte un artefact HORODATÉ DISTINCT du tour de Jerry (fichier créé par la sous-session, pas par le tour parent). Dispatch sans artefact enfant = violation.

## SELF-GRADE : 12/12 — Beth-compat ✓ (tick borné ≤12 agents, zéro action A+), canon ✓ (roster exact, Triptyque, cap ×4 hérité).

---

## ADDENDUM v2 — Correction de Picard (chasse proxy-boolean L2, 2026-07-06 ~05:40)

Hunt exécuté sur la stack L2 (D1, sorties collées au run) :
1. **Proie #1 — le consumer L2 est ABSENT** : aucun script loop pour B1 Gstack (grep cron/*.py = rien hors book/zora/wf3/heartbeat). Les « Lights 3/4 » de Jerry = audit one-shot du 05/07, pas une loop. Pire qu'un proxy : le booléen n'existe pas. → MOVE pour l'exécuteur : le tick M1 de ce wargame EST le consumer à créer (gstack_loop) — pré-câbler dès le kickoff son exit_condition chiffrée : `lights 4/4 sur 2 WK consécutives = section Lighting du verse passe en auto`.
2. **Proie #2 — `cadence_alive = days_completed >= 1`** : présence ≠ fraîcheur (True pour l'éternité dès 1 fichier). **CURÉE ce jour** (patch additif `cadence_fresh` <48h, dry-run vérifié `true`). Deuxième instance vivante du pattern, même session.
3. Pattern extrait en **skill transversale `/diagnose-proxy-boolean`** (proposition Hermes, gravée) — les 7 Picard variants (Saru/Culber/Tilly/Stamets/Burnham/Reno/Georgiou) arrivent au kickoff en mode ARME, pas découverte.

Self-grade v2 : 12/12 maintenu — l'addendum ajoute la chasse vécue (2 proies, 1 curée, 1 spécifiée).
