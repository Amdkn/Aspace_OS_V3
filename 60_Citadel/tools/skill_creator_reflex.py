"""
skill_creator_reflex.py — L0 Pocock Skill Creator Reflex (gate b).

Implémente la checklist Pocock comme gate automatique avant log de tout
skill canonique. Inspiré par le canon upstream mattpocock/skills/writing-great-skills
capturé localement dans LD01/10_methodology/00_Pocock_quality_canon.md.

Per Plan Lightning §3 L0-2 :
  "En faire le **gate qualité du Skill Creator Reflex** : tout skill créé
  (Phase 2 autonome) passe la checklist Pocock avant log"

Doctrine :
  - LECTURE SEULE sur les SKILL.md audités (rien n'est muté)
  - APPEND-ONLY dans skill_creator_reflex_log.md (jamais d'écrasement)
  - IDEMPOTENT : re-run safe (déterminisme des résultats)
  - L0 = checklist consultée, JAMAIS agent qui écrit (anti-Ultron §S5)

Usage:
  python skill_creator_reflex.py <skill_path>            # audit 1 skill
  python skill_creator_reflex.py --batch <paths_file>   # audit batch depuis un fichier
  python skill_creator_reflex.py --canon-dir <dir>      # audit tous les skills d'un dossier
  python skill_creator_reflex.py --report               # affiche rapport global (canonical)

Date : 2026-07-04 · Auteur : Mavis (MC/L1) — Plan Lightning L0 gate b
Source : ~/.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md §3 L0-2
Sister : LD01/10_methodology/00_Pocock_quality_canon.md (canon upstream capturé local)
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path

LOG_PATH = Path(r"C:\Users\amado\agent-os\citadel\logs\skill_creator_reflex_log.md")

REQUIRED_FRONTMATTER = ["name", "description", "allowed-tools", "when_to_use",
                        "version", "author", "license"]
DESCRIPTION_MAX_CHARS = 1024
NAME_PATTERN = __import__("re").compile(r"^[a-z][a-z0-9-]*$")
XML_BRACKET = __import__("re").compile(r"[<>]")


@dataclass
class SkillAudit:
    skill_path: str
    timestamp: str
    ok: bool
    issues: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    frontmatter_present: dict[str, bool] = field(default_factory=dict)
    frontmatter_values: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)


def parse_frontmatter(content: str) -> tuple[dict[str, str], str]:
    """Parse YAML frontmatter (between --- markers). Returns dict + body."""
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    fm_raw = parts[1]
    body = parts[2]
    fm = {}
    for line in fm_raw.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if ":" in s:
            k, v = s.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, body


def audit_skill(skill_md: Path) -> SkillAudit:
    """Applique la checklist Pocock sur un SKILL.md. Lecture seule."""
    if not skill_md.exists():
        return SkillAudit(skill_path=str(skill_md),
                          timestamp=time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                          ok=False, issues=[f"SKILL.md not found at {skill_md}"])

    try:
        content = skill_md.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return SkillAudit(skill_path=str(skill_md),
                          timestamp=time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                          ok=False, issues=[f"read error: {e}"])

    fm, body = parse_frontmatter(content)
    issues = []
    warnings = []

    # 1.1 Frontmatter obligatoire
    fm_present = {}
    for field_name in REQUIRED_FRONTMATTER:
        present = field_name in fm
        fm_present[field_name] = present
        if not present:
            issues.append(f"missing required frontmatter field: {field_name}")

    fm_values = {k: v for k, v in fm.items()}
    name = fm.get("name", "")
    description = fm.get("description", "")
    allowed_tools = fm.get("allowed-tools", "")
    when_to_use = fm.get("when_to_use", "")
    version = fm.get("version", "")
    author = fm.get("author", "")
    license_field = fm.get("license", "")

    # 1.2 Champs vides = refus
    if not name:
        issues.append("field 'name' is empty (refused per §1.2 canon)")
    elif not NAME_PATTERN.match(name):
        issues.append(f"field 'name'='{name}' does not match pattern lowercase-kebab")

    if not description:
        issues.append("field 'description' is empty (refused per §1.2 canon)")
    elif len(description) > DESCRIPTION_MAX_CHARS:
        issues.append(f"field 'description' has {len(description)} chars > {DESCRIPTION_MAX_CHARS} cap")
    elif XML_BRACKET.search(description):
        issues.append("field 'description' contains XML angle brackets (anti-XML rule)")
    elif "\n" in description.strip():
        warnings.append("field 'description' spans multiple lines — Pocock expects single sentence")

    if not allowed_tools:
        issues.append("field 'allowed-tools' is empty → dangerously-permissive (refused)")
    elif allowed_tools == "[]":
        warnings.append("field 'allowed-tools' is empty list — confirm intention")

    if not when_to_use:
        issues.append("field 'when_to_use' is empty — skill won't auto-trigger (refused)")

    if not version:
        issues.append("field 'version' missing — semver required")
    elif not version[0].isdigit():
        warnings.append(f"field 'version'='{version}' should start with digit")

    if not author:
        warnings.append("field 'author' missing — recommended for traceability")

    if not license_field:
        warnings.append("field 'license' missing — recommended (MIT/Apache-2.0)")

    # 1.4 Body sanity
    if not body.strip():
        issues.append("body empty — skill has no instructions beyond frontmatter")

    # 1.5 Anti-doublon heuristique (ne pas bloquer, juste warn)
    if "tutorial" in (name + " " + description).lower() and "skill" in body.lower():
        warnings.append("potential overlap with 'tutorial' archetype — verify no existing similar skill")

    return SkillAudit(
        skill_path=str(skill_md),
        timestamp=time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        ok=len(issues) == 0,
        issues=issues,
        warnings=warnings,
        frontmatter_present=fm_present,
        frontmatter_values=fm_values,
    )


def append_log(audit: SkillAudit) -> None:
    """APPEND-ONLY log (jamais d'écrasement)."""
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    status = "PASS" if audit.ok else "FAIL"
    line = f"\n### {audit.timestamp} — `{Path(audit.skill_path).name}` — {status}\n"
    line += f"- skill_path: `{audit.skill_path}`\n"
    line += f"- ok: {audit.ok}\n"
    line += f"- frontmatter_present: {audit.frontmatter_present}\n"
    if audit.frontmatter_values:
        line += f"- frontmatter_values: `{json.dumps(audit.frontmatter_values, ensure_ascii=False)}`\n"
    if audit.issues:
        line += f"- issues: {'; '.join(audit.issues)}\n"
    if audit.warnings:
        line += f"- warnings: {'; '.join(audit.warnings)}\n"
    line += "\n---\n"
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(line)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("skill_paths", nargs="*", help="paths to SKILL.md files")
    ap.add_argument("--batch", type=Path, help="file listing skill paths (one per line)")
    ap.add_argument("--canon-dir", type=Path, help="dir containing skills (auto-detect SKILL.md)")
    ap.add_argument("--report", action="store_true", help="print full canonical report JSON")
    args = ap.parse_args()

    paths: list[Path] = []
    if args.skill_paths:
        paths = [Path(p) for p in args.skill_paths]
    if args.batch:
        if args.batch.exists():
            paths.extend([Path(line.strip()) for line in args.batch.read_text(encoding="utf-8").splitlines() if line.strip()])
    if args.canon_dir and args.canon_dir.exists():
        for child in sorted(args.canon_dir.iterdir()):
            sm = child / "SKILL.md" if child.is_dir() else (child if child.name == "SKILL.md" else None)
            if sm and sm.exists():
                paths.append(sm)

    if not paths:
        print("usage: skill_creator_reflex.py <skill.md> [<skill2.md>...] [--batch file] [--canon-dir dir]")
        return 2

    audits = [audit_skill(p) for p in paths]
    for a in audits:
        append_log(a)

    # Display
    print(f"Pocock Skill Creator Reflex — {len(audits)} skill(s) audited")
    print()
    ok = sum(1 for a in audits if a.ok)
    warnings_only = sum(1 for a in audits if a.ok and a.warnings)
    failed = len(audits) - ok
    print(f"  ok:        {ok}/{len(audits)}")
    print(f"  warn-only: {warnings_only}/{len(audits)}")
    print(f"  failed:    {failed}/{len(audits)}")
    print()
    for a in audits:
        status = "PASS" if a.ok else "FAIL"
        print(f"  [{status}] {Path(a.skill_path).name}")
        for i in a.issues:
            print(f"     ✗ {i}")
        for w in a.warnings:
            print(f"     ! {w}")

    if args.report:
        print()
        print("CANONICAL JSON:")
        print(json.dumps([a.to_dict() for a in audits], indent=2, ensure_ascii=False))

    print()
    print(f"log appended → {LOG_PATH}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())