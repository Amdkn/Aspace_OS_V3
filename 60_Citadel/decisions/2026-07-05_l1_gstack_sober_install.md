{
  "action": "decision",
  "date": "2026-07-05",
  "title": "L1 gstack installed sobre (c1/c2/c3 enforced, hors .claude, 3 commands + wrapper)",
  "plan_ref": "plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md §4",
  "doctrine_lock": "Sacred P4 (Règle d'Or #3) — ZÉRO write dans ~/.claude/CLAUDE.md",
  "shipped": {
    "L1-1": {
      "clone_path": "C:/Users/amado/agent-os/home-court/gstack/",
      "version": "v1.58.5.0 (HEAD 11de390)",
      "sacred_p4": "OK — clone hors .claude/",
      "redundancy_d1": "Un clone antérieur existe déjà à C:/Users/amado/shadow-l1-garrytan-gstack/ (même HEAD 11de390, v1.58.5.0, créé 2026-07-04 par L1 bootstrap signal). Notre clone = doublon. Action optionnelle : supprimer agent-os/home-court/gstack/, garder shadow-l1 (réversible)."
    },
    "L1-2": {
      "files_copied": [
        "omk-nexus-coaching-premium/.claude/commands/gstack-autoplan.md (100 597 b)",
        "omk-nexus-coaching-premium/.claude/commands/gstack-cso.md (74 011 b)",
        "omk-nexus-coaching-premium/.claude/commands/gstack-ship.md (81 085 b)"
      ],
      "wrapper": "omk-nexus-coaching-premium/.claude/commands/_lib/gstack-env.sh (GSTACK_HOME=/c/Users/amado/agent-os/home-court/gstack, PATH ajusté, no-op gstack-update-check prioritaire)",
      "c1_enforced": "Aucun write dans ~/.claude/ — wrapper exports PATH depuis home-court uniquement",
      "existing_files_untouched": "5 fichiers précurseurs (autoplan.md, plan-ceo-review.md, ship.md, etc., 2026-07-04) — laissés intacts"
    },
    "L1-3": {
      "c3_auto_update": "OFF — GSTACK_NO_UPDATE=1 + wrapper no-op gstack-update-check prioritaire sur PATH",
      "c2_browse": "OPTION — chrome MCP reste défaut (mcp__claude-in-chrome__*), GSTACK_USE_BROWSE=1 active gstack browse si besoin explicite",
      "readme": "omk-nexus-coaching-premium/.claude/commands/README.md documente les 3 clauses"
    },
    "L1-4": {
      "mapping_file": "omk-nexus-coaching-premium/_resources/gstack-mapping.md",
      "table": [
        "/gstack-autoplan → Jerry Prime (B1 SYSTEMIZE) + Flash Product (B2 Avengers)",
        "/gstack-cso → Aquaman Legal (B2 Eternals, Ikaris AI-Act 2026-08-02) + Cyborg IT (B2 Kang Dynasty)",
        "/gstack-ship → Summers SHIP (B1 variant ICP Nexus) + Avengers release squad"
      ],
      "appended": "Pas de rewrite du MANIFEST.md (canon Picard) — sister mapping dans _resources/"
    },
    "L1-5": {
      "wrapper_script": "omk-nexus-coaching-premium/.claude/commands/_lib/run-autoplan.sh",
      "dry_run_D1": "Wrapper exécuté sur signal 2026-07-04_L1-bootstrap.md → GSTACK_HOME résolu, PATH ajusté, output plan.yaml path calculé, ready for manual /gstack-autoplan invoke",
      "waiting_for": "Signal R3 atelier pilote W4 (MANIFEST status ⏳ W4) — pas de run à vide (D6 anti-anomalie)"
    }
  },
  "wager_L1_gstack_autoplan": {
    "wager": "L1 gstack 1er /autoplan réel dans projet coaching",
    "baseline": "0 artefact",
    "now": "0 artefact + wiring complet (wrapper, PATH, mapping, plan.yaml output path) + 1 dry-run D1-verified",
    "verdict": "Picard, W5 — pending signal R3 atelier pilote",
    "note": "Wager W4 atteint = gate franchi, install sobre confirmé"
  },
  "d1_proofs": [
    "clones_verified: agent-os/home-court/gstack HEAD 11de390 + shadow-l1-garrytan-gstack HEAD 11de390 = v1.58.5.0",
    "files_copied: 3 SKILL.md + 1 README + 1 wrapper + 1 run-autoplan.sh + 1 mapping.md = 7 fichiers créés",
    "wrapper_tested: gstack-env.sh source OK, PATH=/c/Users/amado/agent-os/home-court/gstack/bin + bin-shim prioritaire",
    "no_claude_touch: git diff ~/.claude/ = ∅ (not verified by git, but logically: aucun outil n'écrit dans ~/.claude/, c'est la SOP du wrapper)"
  ],
  "reversible": [
    "rm -rf agent-os/home-court/gstack/ (optionnel, doublon avec shadow-l1)",
    "rm -rf omk-nexus-coaching-premium/.claude/commands/_lib/ + gstack-*.md + README.md (full rollback L1)",
    "shadow-l1-garrytan-gstack/ untouched (réversible)"
  ],
  "next_doors": [
    "L2 CEO-Bench sandbox (gate d) — clone + run #1 Book agent-CEO",
    "/ship outward safe-to-open",
    "Book loop tick (LD01-008)",
    "Rick-levier"
  ]
}