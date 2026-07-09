#!/usr/bin/env node
/**
 * super-router.js — Super Router for Harness Engineering Workflows (A'Space canon)
 *
 * Comble Pike's "snw_w28 de curie qui n'existe pas" gap + route any task to the
 * right workflow pattern. Implementation of the Dynamic Workflows PATTERN
 * (per code.claude.com/docs/en/workflows) — native CC 2.1.154+ Workflow tool is
 * NOT available in this runtime (CC v2.1.143 < 2.1.154), so this is a faithful
 * JS re-implementation of the routing/orchestration logic.
 *
 * D1 receipts (2026-07-09):
 * - CC version 2.1.143 (verified via `claude --version`)
 * - Node.js v24.12.0 available (verified via `node --version`)
 * - Convention: scripts in ~/.claude/workflows/ (CC doc)
 * - Sister skill: /multi-session (13 sessions canon)
 *
 * Usage:
 *   node super-router.js "<task description>"
 *   node super-router.js --list                          # list all patterns
 *   node super-router.js --pattern snaw-w28-gaps-combler # show pattern details
 *   node super-router.js --gap-filling snw_w28          # run the gap-filling workflow
 *
 * D6 honest: this is the PATTERN, not the runtime. Each pattern outputs a
 * dispatch script that the orchestrator (me, A0) executes via the Agent tool.
 */

const fs = require('fs');
const path = require('path');

const WORKFLOWS_DIR = path.join(process.env.HOME || process.env.USERPROFILE, '.claude', 'workflows', 'patterns');
const HANDOFFS_DIR = path.join(process.env.HOME || process.env.USERPROFILE, 'ASpace_OS_V2', '00_Amadeus', '30_MEMORY_CORE', 'LLM_Wiki', 'wiki', 'hand_offs');

// ===== Pattern registry (CC Dynamic Workflows pattern: meta + script body) =====
const PATTERNS = {
  // Workflow 1: Comble Pike's snw_w28 gap (the user's literal ask)
  'snaw-w28-gaps-combler': {
    meta: {
      name: 'snaw-w28-gaps-combler',
      description: 'Read a sub-agent handoff (e.g., pike_W28), find gaps, dispatch sub-agents to fill them, aggregate results.',
      horizon: 'H1-H10',
      triggers: ['gap', 'snw', 'curie', 'combler', 'fill gaps', 'pike', 'una', 'chapel', 'morty', 'w28'],
      inputs_required: ['handoff_path', 'gaps_to_fill'],
      outputs: ['filled handoffs in wiki/hand_offs/', 'coordination handoff'],
    },
    script: async (args) => {
      const handoffPath = args.handoff_path;
      const gaps = args.gaps_to_fill || [];
      console.log(`[snaw-w28-gaps-combler] Reading handoff: ${handoffPath}`);
      console.log(`[snaw-w28-gaps-combler] Gaps to fill: ${JSON.stringify(gaps)}`);
      // Returns the dispatch plan — the orchestrator (A0) executes via Agent tool
      return {
        workflow: 'snaw-w28-gaps-combler',
        handoff_path: handoffPath,
        gaps,
        dispatch_plan: gaps.map(gap => ({
          subagent_type: gap.subagent_type || 'general-purpose',
          prompt: gap.prompt || `Fill gap: ${gap.name} — see ${handoffPath}`,
          isolation: 'worktree',
          run_in_background: true,
        })),
        aggregation: 'await all dispatches → write coordination handoff → /multi-session update',
      };
    },
  },

  // Workflow 2: WF1 12WY 5-Disciplines dispatch (canonical Curie)
  'wf1-12wy-dispatch': {
    meta: {
      name: 'wf1-12wy-dispatch',
      description: 'Trigger the canonical 12WY weekly dispatch — 5 A3-SNW sub-agents (Pike, Una, Ortegas, M\'Benga, Chapel) // in parallel.',
      horizon: 'H12WY',
      triggers: ['12wy', 'curie', 'snw', 'weekly', 'dispatch', '5 disciplines'],
      inputs_required: ['week_number'],
      outputs: ['5 curie_<discipline>_W<##>_<ts>.md handoffs'],
    },
    script: async (args) => {
      const week = args.week_number || new Date().getWeek();
      console.log(`[wf1-12wy-dispatch] Week: W${week}`);
      return {
        workflow: 'wf1-12wy-dispatch',
        week,
        command: `pwsh -File C:\\Users\\amado\\.claude\\bin\\a2-curie-12wy-dispatch.ps1 -Week ${week}`,
        dispatch_plan: [
          { subagent_type: 'a3-snw-pike', prompt: `W${week} north star anchor → pike_W${week}_<ts>.md`, isolation: 'worktree', run_in_background: true },
          { subagent_type: 'a3-snw-una', prompt: `W${week} 7-day plan → una_W${week}_<ts>.md`, isolation: 'worktree', run_in_background: true },
          { subagent_type: 'a3-snw-ortegas', prompt: `W${week} daily standup → ortegas_W${week}_<ts>.md`, isolation: 'worktree', run_in_background: true },
          { subagent_type: 'a3-snw-mbenga', prompt: `W${week} 4h deep work → mbenga_W${week}_<ts>.md`, isolation: 'worktree', run_in_background: true },
          { subagent_type: 'a3-snw-chapel', prompt: `W${week} scorecard → chapel_W${week}_<ts>.md`, isolation: 'worktree', run_in_background: true },
        ],
      };
    },
  },

  // Workflow 3: Artifact creator by delegation (the user's literal ask #2)
  'artifact-builder-delegation': {
    meta: {
      name: 'artifact-builder-delegation',
      description: 'Create canonical artifacts (ADR, handoff, skill, doctrine) via orchestration delegation. Discovery → drafting → peer review → publish.',
      horizon: 'H1-H10',
      triggers: ['create artifact', 'adr', 'handoff', 'skill', 'doctrine', 'delegation', 'orchestration'],
      inputs_required: ['artifact_type', 'topic', 'output_path'],
      outputs: ['published artifact at output_path', 'review trail'],
    },
    script: async (args) => {
      const { artifact_type, topic, output_path } = args;
      console.log(`[artifact-builder-delegation] Type: ${artifact_type}, Topic: ${topic}`);
      return {
        workflow: 'artifact-builder-delegation',
        artifact_type,
        topic,
        output_path,
        dispatch_plan: [
          { subagent_type: 'general-purpose', prompt: `Discovery: research ${topic} for ${artifact_type} canon`, isolation: 'worktree', run_in_background: false },
          { subagent_type: 'general-purpose', prompt: `Draft ${artifact_type} for ${topic} → write to ${output_path}`, isolation: 'worktree', run_in_background: false },
          { subagent_type: 'code-reviewer', prompt: `Peer-review draft at ${output_path}`, isolation: 'worktree', run_in_background: false },
          { subagent_type: 'general-purpose', prompt: `Apply review feedback → publish`, isolation: 'worktree', run_in_background: false },
        ],
      };
    },
  },

  // Workflow 4: Super Router classifier (this script itself)
  'super-router-classifier': {
    meta: {
      name: 'super-router-classifier',
      description: 'Take a task description, classify it to the right workflow pattern, output the dispatch plan.',
      horizon: 'H1',
      triggers: ['route', 'classify', 'which workflow', 'super router'],
      inputs_required: ['task_description'],
      outputs: ['selected workflow name + dispatch plan'],
    },
    script: async (args) => {
      const task = (args.task_description || '').toLowerCase();
      // Naive keyword classifier (D1 honest: not LLM-based, deterministic)
      const scores = {};
      for (const [name, pattern] of Object.entries(PATTERNS)) {
        if (name === 'super-router-classifier') continue;
        scores[name] = 0;
        for (const trigger of pattern.meta.triggers) {
          if (task.includes(trigger)) scores[name] += 1;
        }
      }
      // Pick highest
      const ranked = Object.entries(scores).sort((a, b) => b[1] - a[1]);
      const winner = ranked[0];
      console.log(`[super-router-classifier] Task: "${args.task_description}"`);
      console.log(`[super-router-classifier] Scores: ${JSON.stringify(scores)}`);
      console.log(`[super-router-classifier] Winner: ${winner[0]} (score=${winner[1]})`);
      return {
        workflow: winner[0],
        score: winner[1],
        runner_up: ranked[1] ? ranked[1][0] : null,
        dispatch_plan: PATTERNS[winner[0]].script(args),
      };
    },
  },
};

// ===== CLI =====
async function main() {
  const args = process.argv.slice(2);

  if (args.length === 0 || args.includes('--help')) {
    console.log(`super-router.js — Super Router for Harness Engineering Workflows`);
    console.log(`Usage:`);
    console.log(`  node super-router.js "<task description>"`);
    console.log(`  node super-router.js --list`);
    console.log(`  node super-router.js --pattern <name>`);
    console.log(`  node super-router.js --gap-filling <handoff_name>`);
    process.exit(0);
  }

  if (args.includes('--list')) {
    console.log('Available workflow patterns:');
    for (const [name, pattern] of Object.entries(PATTERNS)) {
      console.log(`  - ${name}: ${pattern.meta.description}`);
    }
    process.exit(0);
  }

  if (args.includes('--pattern')) {
    const name = args[args.indexOf('--pattern') + 1];
    const pattern = PATTERNS[name];
    if (!pattern) {
      console.error(`Unknown pattern: ${name}`);
      console.error(`Available: ${Object.keys(PATTERNS).join(', ')}`);
      process.exit(1);
    }
    console.log(JSON.stringify(pattern.meta, null, 2));
    process.exit(0);
  }

  if (args.includes('--gap-filling')) {
    const handoffName = args[args.indexOf('--gap-filling') + 1];
    const handoffPath = path.join(HANDOFFS_DIR, `${handoffName}.md`);
    if (!fs.existsSync(handoffPath)) {
      console.error(`Handoff not found: ${handoffPath}`);
      process.exit(1);
    }
    const handoffContent = fs.readFileSync(handoffPath, 'utf8');
    // Naive gap detection: look for "TODO", "BLOCKED", "TBD", "doesn't exist"
    const gapKeywords = ['TODO', 'BLOCKED', 'TBD', "doesn't exist", 'PENDING', 'GAP', 'snaw_w28'];
    const gaps = [];
    for (const line of handoffContent.split('\n')) {
      for (const kw of gapKeywords) {
        if (line.includes(kw)) {
          gaps.push({ name: kw, line: line.trim().slice(0, 200) });
          break;
        }
      }
    }
    console.log(`[gap-filling] Found ${gaps.length} gap markers in ${handoffName}:`);
    for (const g of gaps) {
      console.log(`  - ${g.name}: ${g.line}`);
    }
    const result = await PATTERNS['snaw-w28-gaps-combler'].script({
      handoff_path: handoffPath,
      gaps_to_fill: gaps,
    });
    console.log('\n[gap-filling] Dispatch plan:');
    console.log(JSON.stringify(result, null, 2));
    process.exit(0);
  }

  // Default: classify the task
  const taskDescription = args.join(' ');
  const result = await PATTERNS['super-router-classifier'].script({ task_description: taskDescription });
  console.log(JSON.stringify(result, null, 2));
}

main().catch(err => {
  console.error('Error:', err.message);
  process.exit(1);
});