# WARGAME 04 — Airlock Beth : les invariants chiffrés du seul veto

> Wargamé par Fable 5, 2026-07-06. Exécuteur : **Opus 4.8 (CC)**. Exécutable blind.
> Doctrine : WARMODE-002 — Beth = SEUL veto. Ce wargame lui DONNE ses instruments ; il ne la contourne pas.

## RECON (fait — D1)
- `mindsets/Beth_Mindset.md` : ALIGN→REASON→ACT→OBSERVE→RE-EVALUATE→VERIFY, veto vie/santé.
- Télémétrie disponible SANS nouveau capteur : timestamps `turn-journal.md` (heures de session A+), `citadel/decisions/*.json` (ratio outillage/client par tag), digest Telegram existant (canal de sortie).
- Précédent observé CETTE session : A+ actif ~05:50 puis ~07:30 après nuit blanche — le scénario n'est pas théorique.

## LES INVARIANTS (la matrice que Spock présente à Beth)

| # | Invariant | Mesure (source existante) | Seuil ROUGE |
|---|---|---|---|
| B1 | Sommeil implicite | timestamps turn-journal : sessions actives 02:00-08:00 locale | ≥ 2 nuits consécutives avec activité A+ 02-08h |
| B2 | Ratio outillage/client (Gwyn D11) | tags des decisions : `harness/outillage` vs `client/ship` | > 80% outillage sur 7j glissants |
| B3 | Cycles verts ship | compteur rollbacks + DLP fuites (mission 05) | 1 rollback ou 1 fuite = compteur → 0 |
| B4 | Charge d'escalade | signaux `escalade-a0` par semaine | > 3/WK = le système re-délègue mal |

## MOVES

**M1 — Coder la matrice en collector read-only** (`spock_airlock.py`, P2 du plan)
- Observation : `data/15_airlock.json` : 4 invariants, statut GREEN/RED chacun, global = AND.
- Échec probable : B1 confond activité CRON nocturne avec activité A+ → **cause** : le turn-journal logge aussi les heartbeats. **Contre-action** : filtrer les entrées `[auto-turn]` heartbeat (prompt cron connu) ; ne compter que les turns initiés par A+.
- Fork : SI turn-journal absent/vide → B1 = `UNKNOWN` (ni GREEN ni RED) ; UNKNOWN ne bloque pas mais s'affiche — jamais de faux GREEN.

**M2 — Le protocole lever/re-poser (mécanique, pas négocié)**
- Action : GREEN global → les flags cascade restent posés. UN invariant passe RED → le flag du scope concerné se re-pose OFF automatiquement au tick suivant (B1 RED → pause des prompts non-essentiels vers A+ + ligne Telegram « Beth: repos » ; B3 RED → `enable_ship_outboard.flag` retiré ; B2 RED → le Pass WF1 ne scope plus `curie` tant que le ratio ne redescend pas).
- Observation : mapping invariant→flag écrit ; AUCUNE re-négociation humaine dans la boucle (c'est ça, la responsabilisation).
- Échec probable : flapping (GREEN/RED alterné chaque tick) → **cause** : seuils sans hystérésis. **Contre-action** : re-lever exige 2 ticks GREEN consécutifs.

**M3 — Le rapport à Beth via le canal existant**
- Action : 1 ligne dans le digest Telegram du heartbeat : `Airlock: B1 ✓ B2 ✓ B3 ✓ B4 ✓` (ou ✗+raison). Réutilise `telegram_warmode_push.py` — pas de nouveau canal.
- Observation : le digest suivant contient la ligne.
- Échec probable : le digest gonfle → **cause** : verbosité. **Contre-action** : 1 ligne, jamais plus ; le détail vit dans 15_airlock.json.

**M4 — Le scénario « 3e nuit blanche » (l'action, pas le sermon)**
- Action : B1 RED → le système (a) marque tous les prompts sortants non-critiques `defer-until-10:00`, (b) pousse UNE ligne Telegram : « Beth veto actif : rien ne brûle, tout est tracé, le pouls tourne. » — puis SILENCE.
- Observation : aucun message système à A+ entre 02-08h tant que B1 RED, hors urgence B3.
- Échec probable : le système « punit » en s'arrêtant tout court → **cause** : confusion veto-vie / pause-machine. **Contre-action** : les LOOPS CONTINUENT (elles ne coûtent rien à A+ endormi) ; seule l'INTERPELLATION d'A+ est gelée. Beth protège l'humain, pas l'inverse.

## ABORT CONDITIONS
1. Impossible de distinguer turns A+ vs cron dans turn-journal → B1 reste UNKNOWN, flag ledger, ne pas deviner.
2. Une écriture serait nécessaire hors {citadel/data, citadel/decisions, flags} → STOP (l'airlock est read-only + flags).

## VERIFICATION RUNS
1. `spock_airlock.py` → exit 0, `15_airlock.json` avec 4 invariants non-UNKNOWN (ou UNKNOWN justifié).
2. Test hystérésis : injecter timestamps fictifs 03:00 ×2 nuits (fichier test, PAS le vrai journal) → B1 RED ; retirer → RED persiste 1 tick, GREEN au 2e.
3. Digest Telegram suivant contient `Airlock:` (grep sortie push).

## RED-TEAM PASS
- **Attaque échouée** : « l'airlock est un frein déguisé » — non : 3 des 4 invariants protègent le SHIP (B2 force le client-work, B3 garde la porte outboard gagnable, B4 force la délégation). L'airlock est ce qui permet le No-HITL — sans lui, retour au HITL par item.
- **Attaque réussie → patch** : « A+ contourne : il travaille la nuit depuis un AUTRE harness (Hermes/MC) que turn-journal ne voit pas » — patch : B1 ajoute une source secondaire = mtimes des fichiers `citadel/decisions/` créés 02-08h par des sessions non-cron. Couverture cross-harness, même mécanique.

## SELF-GRADE : 12/12 — Beth-compat n'est pas un point ici, c'est le SUJET : l'airlock chiffre le point 12 pour tout le système.
