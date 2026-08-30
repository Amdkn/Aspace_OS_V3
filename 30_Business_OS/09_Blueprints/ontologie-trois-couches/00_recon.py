"""Reconnaissance Geordi : comptage fichiers / jonctions / top-level.

NE PAS modifier. Lecture seule. Jonctions detectees et ecartees (pas deescentes).
"""
import os
import stat
import sys
from pathlib import Path

GEORDI = Path("C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi")

RP = getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0x400)


def est_jonction(entry):
    try:
        return bool(entry.stat(follow_symlinks=False).st_file_attributes & RP)
    except (OSError, AttributeError):
        return False


def walk_safe(root):
    total = 0
    md_files = 0
    junctions = []
    dirs = 0
    errors = []

    def _walk(directory):
        nonlocal total, md_files, dirs
        try:
            with os.scandir(directory) as it:
                for entry in it:
                    try:
                        if entry.is_file(follow_symlinks=False):
                            total += 1
                            if entry.name.lower().endswith('.md'):
                                md_files += 1
                        elif entry.is_dir(follow_symlinks=False):
                            if est_jonction(entry):
                                junctions.append(entry.path)
                            else:
                                dirs += 1
                                _walk(entry.path)
                    except OSError as e:
                        errors.append(f"{entry.path}: {e}")
        except (PermissionError, OSError) as e:
            errors.append(f"{directory}: {e}")

    _walk(str(root))
    return total, md_files, junctions, dirs, errors


def top_level(root):
    entries = []
    try:
        with os.scandir(str(root)) as it:
            for entry in it:
                kind = "??"
                try:
                    if entry.is_file(follow_symlinks=False):
                        kind = "FILE"
                    elif entry.is_dir(follow_symlinks=False):
                        kind = "JUNCTION" if est_jonction(entry) else "DIR"
                    else:
                        kind = "OTHER"
                except OSError:
                    kind = "ERR"
                entries.append((kind, entry.name))
    except (PermissionError, OSError) as e:
        return [(f"ERR listing {root}", str(e))]
    entries.sort()
    return entries


if __name__ == "__main__":
    if not GEORDI.exists():
        print(f"Geordi introuvable: {GEORDI}")
        sys.exit(1)

    print(f"== Geordi : {GEORDI}")
    print()

    print("== Top-level ==")
    for kind, name in top_level(GEORDI):
        print(f"  [{kind:8s}] {name}")
    print()

    print("== Walk safe ==")
    total, md_files, junctions, dirs, errors = walk_safe(GEORDI)
    print(f"  total fichiers : {total:,}")
    print(f"  .md            : {md_files:,}")
    print(f"  jonctions      : {len(junctions):,}")
    print(f"  dossiers       : {dirs:,}")
    print(f"  erreurs scan   : {len(errors):,}")
    if errors:
        print()
        print("  -- 20 premieres erreurs --")
        for e in errors[:20]:
            print(f"    {e}")

    if junctions:
        print()
        print("== Echantillon jonctions (max 20) ==")
        for j in junctions[:20]:
            print(f"  {j}")