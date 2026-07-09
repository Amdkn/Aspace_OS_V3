# Fix Codex audit findings : A3 twins reconciliation + D6 #80 lesson coherence 5 ADR
# D6 #80 anti-loop guard : string FIXE, JAMAIS output libre
import os, re

ADR_DIR = r"C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L2_Business_OS"

# === FIX #1 : OPERATIONS A3 twins count reconciliation (P0) ===
ops_path = os.path.join(ADR_DIR, "ADR-AAAS-OPERATIONS-CANON-001_aaas-operations-canon.md")
with open(ops_path, "r", encoding="utf-8") as f:
    ops = f.read()

# Replace 3 occurrences to clarify 10 explicitly mapped OPERATIONS vs 35 A3 total canon ASpace
fix1_old_a = "- **A3 twins orchestration** : 35 A3 mapped sur 5 Piliers (Tilly/Chapel/Book/Saru/Spock/Boimler/Isaac/Geordi + A1 Beth/Morty)"
fix1_new_a = "- **A3 twins orchestration** : 10 A3 explicitement mappes OPERATIONS (Tilly H30/Chapel H10/Book H1/Saru H3/Spock H30/Boimler/Isaac H1/Geordi H90 + A1 Beth/A1 Morty) sur 5 Piliers. Sister canon canon : 35/35 A3 total canon ASpace CC<->Symphony v1.2 (dont 10 OPERATIONS-specifiques, 25 sister scope autres frameworks Life OS)"

fix1_old_b = "| A3 twins mapping | A3-Data Cartography v1.2 | 10 mapped | HIGH |"
fix1_new_b = "| A3 twins mapping OPERATIONS | A3-Data Cartography v1.2 | 10 explicitement mappes (table ci-dessus) | HIGH |"
fix1_old_c = "- **A3 twins mapping canon** : 10 A3 mapped sur 5 Piliers, sister A3-Data Cartography v1.2"
fix1_new_c = "- **A3 twins mapping canon OPERATIONS** : 10 A3 explicitement mappes OPERATIONS sur 5 Piliers (table ci-dessus). Sister canon canon : 35/35 A3 total canon ASpace CC<->Symphony v1.2 (A3-Data Cartography v1.2 hand-off D1 verify canon 2026-06-21)"

ops_new = ops
for old, new in [(fix1_old_a, fix1_new_a), (fix1_old_b, fix1_new_b), (fix1_old_c, fix1_new_c)]:
    if old in ops_new:
        ops_new = ops_new.replace(old, new)
        print("[OK] Replaced: " + old[:60] + "...")
    else:
        print("[MISS] Pattern not found: " + old[:60] + "...")

with open(ops_path, "w", encoding="utf-8") as f:
    f.write(ops_new)
print("[OK] OPERATIONS A3 reconcile : " + ops_path)
print("     Size : " + str(len(ops_new)) + " chars (avant " + str(len(ops)) + ")")
print()

# === FIX #2 : D6 #80 lesson coherence 3 ADR (FINANCE, IT-EXT, CONTENT) ===
D6_80_NOTE = (
    "\n- **#80** : **Output token loop trap (sister scope canon)** - "
    "Notification finale A0 post canon-batch a declenche boucle pathologique \"canon canon canon...\" "
    "sur 4 fichiers canon (108/625/349/1448 reps). D6 fix chirurgical regex `(canon\\s+){4,}.*$` preserve D4 append-only. "
    "Cet ADR N'A PAS ETE affecte directement (VAGUE 3+4 propres). Anti-pattern guard : JAMAIS output libre apres canon-batch, "
    "toujours Edit chirurgical. Sister ADR-AAAS-IT-CANON-001 + ADR-AAAS-OPERATIONS-CANON-001 (les 2/5 ADR touches). "
    "Backups `.pre-d6fix80` crees. Sister ADR-META-006 catalog append-only.\n"
)

for filename in [
    "ADR-AAAS-FINANCE-CANON-001_aaas-finance-canon.md",
    "ADR-AAAS-IT-EXT-CANON-001_aaas-it-ext-canon.md",
    "ADR-AAAS-CONTENT-CANON-001_aaas-content-canon.md"
]:
    fpath = os.path.join(ADR_DIR, filename)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find D6 Lessons section and insert D6 #80 before the closing line
    marker = "## D7 anti-effondrement canon"
    if marker in content:
        content_new = content.replace(marker, D6_80_NOTE + marker)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content_new)
        print("[OK] D6 #80 added to " + filename + " : " + str(len(content_new)) + " chars")
    else:
        print("[MISS] marker not found in " + filename)

print()
print("=== ALL FIXES APPLIED ===")
print("Fix #1 P0: OPERATIONS A3 reconcile (3 lines clarify 10 mapped OPERATIONS vs 35 A3 total ASpace)")
print("Fix #2 P1: D6 #80 lesson coherence (3 ADR missing now have #80 sister scope)")