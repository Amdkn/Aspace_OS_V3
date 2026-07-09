{
  "action": "decision",
  "date": "2026-07-05",
  "title": "L0 Pocock gate (b) ouvert — writing-great-skills installé + strategy-session-meta v1.1.0 auditée",
  "plan_ref": "plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md §3",
  "doctrine": "Portes over Freins (ADR-WARMODE-002) + append-only (D4) + user-invoked skill (Pocock canon)",
  "shipped": {
    "L0-1": {
      "skill": "writing-great-skills",
      "path": ".claude/skills/writing-great-skills/",
      "files": ["SKILL.md (9063 b)", "GLOSSARY.md (17569 b)"],
      "source": "github.com/mattpocock/skills/tree/main/skills/productivity/writing-great-skills",
      "d1_proof": "bytes match GitHub raw verbatim (D1 verified). disable-model-invocation: true honoured.",
      "note": "user-invoked = zero context load. Sister référence, pas auto-trigger."
    },
    "L0-2": {
      "skill": "strategy-session-meta",
      "old_version": "1.0.0",
      "new_version": "1.1.0",
      "fixes_applied": [
        "description front-loaded (canon Pocock: leading word first)",
        "when_to_use fusionné dans description (anti-duplication)",
        "disable-model-invocation: true ajouté",
        "author mis à jour (Mavis → Hermes Agent, HA Picard re-roled)",
        "commentaire anti-Ultron sediment purgé du frontmatter"
      ],
      "kept": ["leading words 'agnostique/persistant/antifragile' (Pocock: triad distribuée)", "73 lignes < sprawl threshold"],
      "sister_link_added": "../writing-great-skills/SKILL.md"
    },
    "L0-3": {
      "skill": "takeout-delta-ingest",
      "action": "sister-link only — audit pending (pas appliqué ce turn, sobrieté)",
      "audit_pendings": ["author Mavis→HA", "anti-Ultron sediment à purger", "when_to_use duplication", "disable-model-invocation missing"],
      "rationale_pending": "Re-audit à programmer après ADR-LD01-009 ratification côté HA (pas anticipé).",
      "sister_link_added": "../writing-great-skills/SKILL.md"
    }
  },
  "wager_L0_pocock_update": {
    "wager": "L0 Pocock gate le Skill Creator Reflex",
    "baseline": "0 skill re-audité",
    "now": "1 skill re-audité (strategy-session-meta v1.1.0) + 1 sister-link (takeout-delta-ingest)",
    "verdict": "Picard, W4 — en cours, audit second skill à programmer"
  },
  "doctrine_lock": "Pocock canon est reference-only (user-invoked, disable-model-invocation=true). Ne JAMAIS auto-trigger sur modification de skill — usage = gate manuel par l'agent quand il édite.",
  "reversible": "delete .claude/skills/writing-great-skills/ + revert SKILL.md edits (strategy-session-meta 1.1.0→1.0.0) + takeout LESSONS append reste en trace historique.",
  "next_doors": ["/ship outward safe-to-open", "Book loop tick (LD01-008)", "Rick-levier"]
}