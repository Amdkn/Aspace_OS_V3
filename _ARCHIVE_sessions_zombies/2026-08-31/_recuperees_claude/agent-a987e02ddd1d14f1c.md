---
session: agent-a987e02ddd1d14f1c
origine: claude
chemin_source: C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\06_Claude_Code_Bare\projects\C--Users-amado\441d3dbe-6b5b-4f20-a37b-9f8ca8e44bbe\subagents\agent-a987e02ddd1d14f1c.jsonl
debut: 2026-07-31T11:09:18.240Z
fin: 2026-07-31T11:28:19.599Z
messages_utilisateur: 2
reponses_assistant: 1
titre: "You are implementing Task 2 of the Cognition Memory Unification plan: walk_scatter_sources.py — walks 6 source…"
---

## >>> UTILISATEUR #1

You are implementing Task 2 of the Cognition Memory Unification plan: walk_scatter_sources.py — walks 6 source buckets, computes SHA256, dedupes, emits canidates YAML.

## Task Description

Read your task brief first: `C:/Users/amado/.superpowers/sdd/task-2-brief.md`
It contains the full task text from the plan (steps, exact code, expected output).

## Context

This is the second task in the Cognition Memory Unification pipeline (sister spec: `ASpace_OS_V2/docs/superpowers/specs/2026-07-31-cognition-unification-design.md`). Task 1 (scaffold + b1_filter.yaml + pytest) is DONE and APPROVED — you can import from `cognition` package. Downstream Tasks 3 (classify), 4 (migrate), 5 (verify) will consume the YAML you produce.

You are working in `C:/Users/amado/ASpace_OS_V2/`. Task 1 created:
- `ASpace_OS_V2/scripts/cognition/__init__.py`
- `ASpace_OS_V2/scripts/cognition/b1_filter.yaml`
- `ASpace_OS_V2/scripts/cognition/tests/__init__.py`
- `ASpace_OS_V2/scripts/cognition/tests/conftest.py` (fixtures: tmp_source_dir, tmp_geordi_dir, tmp_trash_dir)

## Before You Begin

If you have questions, ask now. Otherwise proceed.

## Your Job

Per the brief:
1. Write the failing test file first (`test_walk_scatter_sources.py`)
2. Run it to verify FAIL (RED)
3. Implement `walk_scatter_sources.py`
4. Run test, verify PASS (GREEN)
5. Run full pytest suite — Task 1 tests + your new tests must all pass
6. Commit your work
7. Self-review
8. Write full report
9. Report back

## Important Notes

- Pre-flight Minor F2: `compute_sha256` is duplicated in walk_scatter_sources (this task), migrate_with_sha256 (Task 4), verify_migration (Task 5). The plan accepts this for now — Tasks 4+ will create a shared `cognition._sha256` utility. Stay with the plan's duplication for Task 2; do NOT pre-emptively refactor unless tests require it.
- The brief specifies `click` for CLI. If `click` is not installed, install it with `pip install click`.
- The brief specifies `PyYAML`. Verify installation: `python -c "import yaml"` — if fails, install.
- Tests use `click.testing.CliRunner`. Verify `click` test utilities available.

## Code Organization

Follow the file structure defined in the plan. `walk_scatter_sources.py` has one responsibility: walk + hash + dedup.

## When You're in Over Your Head

Escalate with BLOCKED or NEEDS_CONTEXT. Do not silently produce work you're unsure about.

## Before Reporting Back: Self-Review

- Did you implement TDD (test first, fail, then implement)?
- Are the 6 tests passing (per brief)?
- Is the script idempotent (--dry-run support)?
- Are SHA256 computations correct (hexdigest, length 64)?
- Does dedup work (same SHA256 → single entry)?

## Report Format

Write your full report to `C:/Users/amado/.superpowers/sdd/task-2-report.md`:
- What you implemented
- TDD Evidence: RED (command + failing output) and GREEN (command + passing output)
- Files changed (with line counts)
- Self-review findings
- Any concerns

Then report back with ONLY:
- **Status:** DONE | DONE_WITH_CONCERNS | BLOCKED | NEEDS_CONTEXT
- Commits created (short SHA + subject)
- One-line test summary (e.g. "11/11 passing, output pristine")
- Your concerns, if any
- The report file path

## >>> UTILISATEUR #2

Base directory for this skill: C:\Users\amado\.claude\plugins\cache\claude-plugins-official\superpowers\6.0.3\skills\test-driven-development

# Test-Driven Development (TDD)

## Overview

Write the test first. Watch it fail. Write minimal code to pass.

**Core principle:** If you didn't watch the test fail, you don't know if it tests the right thing.

**Violating the letter of the rules is violating the spirit of the rules.**

## When to Use

**Always:**
- New features
- Bug fixes
- Refactoring
- Behavior changes

**Exceptions (ask your human partner):**
- Throwaway prototypes
- Generated code
- Configuration files

Thinking "skip TDD just this once"? Stop. That's rationalization.

## The Iron Law

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Write code before the test? Delete it. Start over.

**No exceptions:**
- Don't keep it as "reference"
- Don't "adapt" it while writing tests
- Don't look at it
- Delete means delete

Implement fresh from tests. Period.

## Red-Green-Refactor

```dot
digraph tdd_cycle {
    rankdir=LR;
    red [label="RED\nWrite failing test", shape=box, style=filled, fillcolor="#ffcccc"];
    verify_red [label="Verify fails\ncorrectly", shape=diamond];
    green [label="GREEN\nMinimal code", shape=box, style=filled, fillcolor="#ccffcc"];
    verify_green [label="Verify passes\nAll green", shape=diamond];
    refactor [label="REFACTOR\nClean up", shape=box, style=filled, fillcolor="#ccccff"];
    next [label="Next", shape=ellipse];

    red -> verify_red;
    verify_red -> green [label="yes"];
    verify_red -> red [label="wrong\nfailure"];
    green -> verify_green;
    verify_green -> refactor [label="yes"];
    verify_green -> green [label="no"];
    refactor -> verify_green [label="stay\ngreen"];
    verify_green -> next;
    next -> red;
}
```

### RED - Write Failing Test

Write one minimal test showing what should happen.

<Good>
```typescript
test('retries failed operations 3 times', async () => {
  let attempts = 0;
  const operation = () => {
    attempts++;
    if (attempts < 3) throw new Error('fail');
    return 'success';
  };

  const result = await retryOperation(operation);

  expect(result).toBe('success');
  expect(attempts).toBe(3);
});
```
Clear name, tests real behavior, one thing
</Good>

<Bad>
```typescript
test('retry works', async () => {
  const mock = jest.fn()
    .mockRejectedValueOnce(new Error())
    .mockRejectedValueOnce(new Error())
    .mockResolvedValueOnce('success');
  await retryOperation(mock);
  expect(mock).toHaveBeenCalledTimes(3);
});
```
Vague name, tests mock not code
</Bad>

**Requirements:**
- One behavior
- Clear name
- Real code (no mocks unless unavoidable)

### Verify RED - Watch It Fail

**MANDATORY. Never skip.**

```bash
npm test path/to/test.test.ts
```

Confirm:
- Test fails (not errors)
- Failure message is expected
- Fails because feature missing (not typos)

**Test passes?** You're testing existing behavior. Fix test.

**Test errors?** Fix error, re-run until it fails correctly.

### GREEN - Minimal Code

Write simplest code to pass the test.

<Good>
```typescript
async function retryOperation<T>(fn: () => Promise<T>): Promise<T> {
  for (let i = 0; i < 3; i++) {
    try {
      return await fn();
    } catch (e) {
      if (i === 2) throw e;
    }
  }
  throw new Error('unreachable');
}
```
Just enough to pass
</Good>

<Bad>
```typescript
async function retryOperation<T>(
  fn: () => Promise<T>,
  options?: {
    maxRetries?: number;
    backoff?: 'linear' | 'exponential';
    onRetry?: (attempt: number) => void;
  }
): Promise<T> {
  // YAGNI
}
```
Over-engineered
</Bad>

Don't add features, refactor other code, or "improve" beyond the test.

### Verify GREEN - Watch It Pass

**MANDATORY.**

```bash
npm test path/to/test.test.ts
```

Confirm:
- Test passes
- Other tests still pass
- Output pristine (no errors, warnings)

**Test fails?** Fix code, not test.

**Other tests fail?** Fix now.

### REFACTOR - Clean Up

After green only:
- Remove duplication
- Improve names
- Extract helpers

Keep tests green. Don't add behavior.

### Repeat

Next failing test for next feature.

## Good Tests

| Quality | Good | Bad |
|---------|------|-----|
| **Minimal** | One thing. "and" in name? Split it. | `test('validates email and domain and whitespace')` |
| **Clear** | Name describes behavior | `test('test1')` |
| **Shows intent** | Demonstrates desired API | Obscures what code should do |

## Why Order Matters

**"I'll write tests after to verify it works"**

Tests written after code pass immediately. Passing immediately proves nothing:
- Might test wrong thing
- Might test implementation, not behavior
- Might miss edge cases you forgot
- You never saw it catch the bug

Test-first forces you to see the test fail, proving it actually tests something.

**"I already manually tested all the edge cases"**

Manual testing is ad-hoc. You think you tested everything but:
- No record of what you tested
- Can't re-run when code changes
- Easy to forget cases under pressure
- "It worked when I tried it" ≠ comprehensive

Automated tests are systematic. They run the same way every time.

**"Deleting X hours of work is wasteful"**

Sunk cost fallacy. The time is already gone. Your choice now:
- Delete and rewrite with TDD (X more hours, high confidence)
- Keep it and add tests after (30 min, low confidence, likely bugs)

The "waste" is keeping code you can't trust. Working code without real tests is technical debt.

**"TDD is dogmatic, being pragmatic means adapting"**

TDD IS pragmatic:
- Finds bugs before commit (faster than debugging after)
- Prevents regressions (tests catch breaks immediately)
- Documents behavior (tests show how to use code)
- Enables refactoring (change freely, tests catch breaks)

"Pragmatic" shortcuts = debugging in production = slower.

**"Tests after achieve the same goals - it's spirit not ritual"**

No. Tests-after answer "What does this do?" Tests-first answer "What should this do?"

Tests-after are biased by your implementation. You test what you built, not what's required. You verify remembered edge cases, not discovered ones.

Tests-first force edge case discovery before implementing. Tests-after verify you remembered everything (you didn't).

30 minutes of tests after ≠ TDD. You get coverage, lose proof tests work.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Test takes 30 seconds. |
| "I'll test after" | Tests passing immediately prove nothing. |
| "Tests after achieve same goals" | Tests-after = "what does this do?" Tests-first = "what should this do?" |
| "Already manually tested" | Ad-hoc ≠ systematic. No record, can't re-run. |
| "Deleting X hours is wasteful" | Sunk cost fallacy. Keeping unverified code is technical debt. |
| "Keep as reference, write tests first" | You'll adapt it. That's testing after. Delete means delete. |
| "Need to explore first" | Fine. Throw away exploration, start with TDD. |
| "Test hard = design unclear" | Listen to test. Hard to test = hard to use. |
| "TDD will slow me down" | TDD faster than debugging. Pragmatic = test-first. |
| "Manual test faster" | Manual doesn't prove edge cases. You'll re-test every change. |
| "Existing code has no tests" | You're improving it. Add tests for existing code. |

## Red Flags - STOP and Start Over

- Code before test
- Test after implementation
- Test passes immediately
- Can't explain why test failed
- Tests added "later"
- Rationalizing "just this once"
- "I already manually tested it"
- "Tests after achieve the same purpose"
- "It's about spirit not ritual"
- "Keep as reference" or "adapt existing code"
- "Already spent X hours, deleting is wasteful"
- "TDD is dogmatic, I'm being pragmatic"
- "This is different because..."

**All of these mean: Delete code. Start over with TDD.**

## Example: Bug Fix

**Bug:** Empty email accepted

**RED**
```typescript
test('rejects empty email', async () => {
  const result = await submitForm({ email: '' });
  expect(result.error).toBe('Email required');
});
```

**Verify RED**
```bash
$ npm test
FAIL: expected 'Email required', got undefined
```

**GREEN**
```typescript
function submitForm(data: FormData) {
  if (!data.email?.trim()) {
    return { error: 'Email required' };
  }
  // ...
}
```

**Verify GREEN**
```bash
$ npm test
PASS
```

**REFACTOR**
Extract validation for multiple fields if needed.

## Verification Checklist

Before marking work complete:

- [ ] Every new function/method has a test
- [ ] Watched each test fail before implementing
- [ ] Each test failed for expected reason (feature missing, not typo)
- [ ] Wrote minimal code to pass each test
- [ ] All tests pass
- [ ] Output pristine (no errors, warnings)
- [ ] Tests use real code (mocks only if unavoidable)
- [ ] Edge cases and errors covered

Can't check all boxes? You skipped TDD. Start over.

## When Stuck

| Problem | Solution |
|---------|----------|
| Don't know how to test | Write wished-for API. Write assertion first. Ask your human partner. |
| Test too complicated | Design too complicated. Simplify interface. |
| Must mock everything | Code too coupled. Use dependency injection. |
| Test setup huge | Extract helpers. Still complex? Simplify design. |

## Debugging Integration

Bug found? Write failing test reproducing it. Follow TDD cycle. Test proves fix and prevents regression.

Never fix bugs without a test.

## Testing Anti-Patterns

When adding mocks or test utilities, read [testing-anti-patterns.md](testing-anti-patterns.md) to avoid common pitfalls:
- Testing mock behavior instead of real behavior
- Adding test-only methods to production classes
- Mocking without understanding dependencies

## Final Rule

```
Production code → test exists and failed first
Otherwise → not TDD
```

No exceptions without your human partner's permission.

### assistant

**Status:** DONE_WITH_CONCERNS  
**Commits created:** `61ea372 feat(cognition): walk_scatter_sources.py with SHA256 + dedup + dry-run`  
**Test summary:** 11/11 cognition tests passing, including Task 1 and Task 2; output clean.  
**Concerns:** Repository-wide pytest collection exceeded 120 seconds; the scoped cognition suite passes completely. An unrelated pre-staged `.agentsroom` change remains outside the commit.  
**Report:** `C:\Users\amado\.superpowers\sdd\task-2-report.md`
