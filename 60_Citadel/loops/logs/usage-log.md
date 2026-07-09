# USAGE LOG — Source tokens MiniMax pour le Collecteur Beth-capacité (wargame 26 cat.2 #3)
#
# FORMAT OBLIGATOIRE (parsing regex strict, le script plante si mal formaté) :
#   - [<ISO 8601 timestamp>] [usage-snapshot] 5h=X% weekly=Y% monthly=Z% — preuve: <note>
#
# Où :
#   - ISO = aaaa-mm-jjTHH:MM:SS-04:00 (Eastern offset = GMT-4) ou +00:00
#   - X = % du quota 5h utilisé (5h limit Used N% sur dashboard)
#   - Y = % du quota hebdomadaire (Weekly Used N%)
#   - Z = % du quota mensuel 30j (Last 30 days tokens / 5.1B)
#   - preuve = chemin screenshot ou note manuelle ("vu dashboard 23:30", etc.)
#
# WORKFLOW (A+ manuel, ~30 sec) :
#   1. Ouvrir https://platform.minimax.io/console/usage (ou Token Plan page)
#   2. Lire 3 chiffres : 5h Used, Weekly Used, Last 30 days tokens / 5.1B
#   3. Convertir tokens/30j en % : (Last30days_tokens / 5_100_000_000) * 100
#   4. Append une ligne ici-bas, format strict
#   5. Run .\collecteur_beth_capacity.ps1 (le verdict bascule)
#
# PAS d'auto-scrape (login requis, fragile, mensonge sur la mesure). M3 lit CE fichier,
# A+ le nourrit. Le verdict GREEN/RED dépend de la FRAÎCHEUR de la dernière ligne.
#
# AMENDEMENT 2026-07-07 : adopté combo A+B (proxy worklog + dashboard manuel).
# Source canon = https://platform.minimax.io/console/usage + https://platform.minimax.io/subscribe/token-plan
# Plan actif (vérifié 2026-07-07 23:30) = Token Plan Monthly Max, $50/mois, ~5.1B tokens.

# ====================================================================================
# SEED ENTRY (1ère entrée du carnet, posée par A+ après confirmation source)
# ====================================================================================- [2026-07-07T23:32:00-04:00] [usage-snapshot] 5h=4% weekly=9% monthly=81% — preuve: A+ screenshots platform.minimax.io/console/usage (4.15B/5.1B Last 30 days, 696.27M Last 7 days, 0 today 08 Jul 03:00 UTC, 5h limit Used 4%, Weekly Used 9%, 4.85B total tokens, 381.09M peak tokens, 48 active days, Token Plan Monthly Max $50/mois)
- [2026-07-07T23:55:00-04:00] [usage-amend] AMENDMENT 81%->100% (A+ ratifié 2026-07-07 23:50): les 81% brulés = MOIS PRECEDENT (plan Plus $20), pas le plan courant. Interface dashboard pas mise a jour car upgrade vers annuel imminent (2 jours). Plan annuel = renouvellement 100% chaque mois. 4B tokens = UTILISATION MANUELLE A+ (sans ADE pane), pas agent waste. RunPane = orchestrateur indispensable qui previent le gaspillage (mais venu tard dans wargames Fable). Verdict Collecteur revu : GREEN si RAM > 6GB free (apps fermables donnent marge, calibration A+ au ressenti).
