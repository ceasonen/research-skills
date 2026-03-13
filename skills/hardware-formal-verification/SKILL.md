---
name: hardware-formal-verification
description: Apply assertion-based and property-driven reasoning to RTL, interfaces, FIFOs, arbiters, and control logic. Use when writing SystemVerilog assertions, planning SymbiYosys checks, proving safety and liveness properties, or strengthening an RTL module beyond simulation-only confidence.
---
# Hardware Formal Verification

Use this skill when simulation is not enough to rule out corner-case protocol or state bugs.

## Core Workflow

1. Define the block contract and environment assumptions.
2. Choose properties:
   - reset safety,
   - protocol safety,
   - ordering,
   - exclusivity,
   - eventual progress.
3. Use `references/formal-checklist.md` to separate assumptions, assertions, and covers.
4. If `sby` or `yosys` exists, run the smallest proof target first.
5. Report proof limits and abstraction assumptions explicitly.

## Execution Rules

1. Do not bury assumptions inside assertions.
2. Prefer a few meaningful invariants over many weak properties.
3. Use simulation counterexamples to refine formal properties and vice versa.
4. State whether a failure is a design bug, a property bug, or an environment-model bug.

## Output Contract

Return:

1. Property set.
2. Assumption set.
3. Proof plan.
4. Results or expected counterexamples.
5. Remaining unproven risks.
