---
name: paper-to-implementation
description: Turn a paper, tech report, benchmark writeup, or architecture figure into an implementation plan for ML, systems, or hardware-software research. Use when reproducing a method, converting equations into modules, extracting pseudocode, filling missing details, or building an MVP from a PDF or spec.
---
# Paper To Implementation

Use this skill when a paper is clear enough to build from, but not clear enough to code directly.

## Core Workflow

1. Extract the objective, inputs, outputs, train path, and inference path.
2. Build a module graph before touching code.
3. Map equations, diagrams, and tables to code objects:
   - tensors,
   - kernels,
   - loops,
   - queues,
   - state machines,
   - interfaces.
4. Use `references/implementation-checklist.md` to find missing details.
5. Propose the smallest testable slice first, then the full reproduction plan.
6. Write a staged implementation order with config, tests, and failure probes.

## Execution Rules

1. Keep an assumption log. Do not hide gaps with confident prose.
2. Distinguish direct paper statements from your fill-ins.
3. Prefer the smallest reproducible vertical slice over a full rewrite.
4. If official code exists, compare paper intent against repo behavior and call out mismatches.
5. When hardware or systems claims depend on undocumented implementation details, make those risks explicit.

## Output Contract

Return:

1. Assumption log.
2. Module breakdown.
3. Data and control-flow summary.
4. Staged implementation plan.
5. Tests, probes, and unresolved questions.
