#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
harness_evaluator.py — Rick's Harness Automated Quality Evaluator.

This script parses a batch JSON file, identifies all target Obsidian guide filenames,
and evaluates their quality against strict A'Space OS criteria (line density and blacklist strings).

Usage:
    python symphony_antigravity/harness_evaluator.py <path_to_batch.json>
"""

import sys
import os
import json
import re
from pathlib import Path

# Config
GEORDI_DIR = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides")
MIN_LINES_PER_VIDEO = 50
MIN_SCORE_PER_VIDEO = 80

# Mots ou patterns blacklistés indiquant une paresse ou un placeholder
BLACKLIST_PATTERNS = [
    r"\[Contenu",
    r"\[Technical",
    r"\[Insert",
    r"\[Générer",
    r"\[TBD",
    r"TODO",
    r"placeholder",
    r"\.\.\.\s*$",  # Trois petits points de fin de ligne signifiant troncation
    r"\[\s*\.\.\.\s*\]"
]

def generate_obsidian_filename(title: str) -> str:
    """Generate a slugified filename for the Obsidian resource guide."""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s]', '', slug)
    slug = re.sub(r'\s+', '_', slug.strip())
    slug = slug[:80]
    return f"resource_{slug}.md"

def calculate_score(content: str) -> float:
    """Calculate the line_density_score: lines * (sections + code_blocks + todo_items) / 10"""
    lines = content.splitlines()
    num_lines = len(lines)
    
    # Sections (##)
    sections = len([l for l in lines if l.strip().startswith("##")])
    
    # Code blocks (```)
    code_blocks = content.count("```") // 2
    
    # Todo items (- [ ])
    todo_items = len([l for l in lines if "- [ ]" in l or "- [x]" in l])
    
    score = num_lines * (sections + code_blocks + todo_items) / 10.0
    return score, num_lines, sections, code_blocks, todo_items

def evaluate_file(file_path: Path) -> dict:
    """Evaluate a single markdown file against rules."""
    if not file_path.exists():
        return {"valid": False, "reason": f"File does not exist: {file_path.name}"}
        
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return {"valid": False, "reason": f"Failed to read file: {str(e)}"}
        
    # Check blacklist
    for pattern in BLACKLIST_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            return {
                "valid": False,
                "reason": f"Blacklisted pattern detected: '{pattern}' in {file_path.name}"
            }
            
    # Calculate score
    score, lines, sections, code_blocks, todo_items = calculate_score(content)
    
    if lines < MIN_LINES_PER_VIDEO:
        return {
            "valid": False,
            "reason": f"File too short ({lines} lines < {MIN_LINES_PER_VIDEO}) in {file_path.name}"
        }
        
    if score < MIN_SCORE_PER_VIDEO:
        return {
            "valid": False,
            "reason": f"Score too low ({score} < {MIN_SCORE_PER_VIDEO}) [Lines: {lines}, Sections: {sections}, CodeBlocks: {code_blocks}, Todos: {todo_items}]"
        }
        
    return {
        "valid": True,
        "score": score,
        "lines": lines,
        "sections": sections,
        "code_blocks": code_blocks,
        "todos": todo_items
    }

def main():
    # Force UTF-8 printing for console safety
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')

    if len(sys.argv) < 2:
        print("[FATAL] Usage: python harness_evaluator.py <path_to_batch.json>")
        sys.exit(1)
        
    batch_path = Path(sys.argv[1])
    if not batch_path.exists():
        print(f"[FATAL] Batch file not found: {batch_path}")
        sys.exit(1)
        
    try:
        with open(batch_path, encoding="utf-8") as f:
            videos = json.load(f)
    except Exception as e:
        print(f"[FATAL] Failed to parse batch JSON: {e}")
        sys.exit(1)
        
    errors = []
    successes = []
    
    print(f"\n--- [SHIELD] Evaluating Batch {batch_path.name} ---")
    
    for idx, video in enumerate(videos, 1):
        title = video["title"]
        filename = generate_obsidian_filename(title)
        file_path = GEORDI_DIR / filename
        
        result = evaluate_file(file_path)
        if not result["valid"]:
            errors.append(f"Video {idx}: '{title[:40]}' -> {result['reason']}")
        else:
            successes.append({
                "title": title,
                "file": filename,
                "score": result["score"],
                "lines": result["lines"]
            })
            
    if errors:
        print("\n[!] VALIDATION REJECTED:")
        for err in errors:
            print(f"  - {err}")
        print("\nSummary: Rejections detected. Triggering Ralph Loop Retry.")
        sys.exit(1)
    else:
        print("\n[+] ALL FILES PASSED VALIDATION:")
        for succ in successes:
            print(f"  - {succ['file']} (Lines: {succ['lines']}, Score: {succ['score']:.1f})")
        print("\nSummary: Batch is clean and highly dense.")
        sys.exit(0)

if __name__ == "__main__":
    main()
