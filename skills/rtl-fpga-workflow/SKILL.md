---
name: rtl-fpga-workflow
description: Design, review, and debug Verilog or SystemVerilog and FPGA work including interfaces, testbenches, reset strategy, clock-domain crossings, synthesis constraints, and timing-closure preparation. Use when writing RTL, planning an FPGA prototype, reviewing a testbench, or turning a hardware paper or spec into simulatable modules.
---
# RTL FPGA Workflow

Use this skill for RTL and FPGA tasks where interface discipline matters more than clever syntax.

## Core Workflow

1. Start with the interface contract and timing assumptions.
2. Pick one clock and reset story and document it.
3. Write the smallest useful testbench first.
4. Use `references/rtl-checklist.md` for resets, CDC, FSMs, RAMs, and synthesis hazards.
5. Run `scripts/fpga_toolchain_doctor.py` when tool availability is unclear.
6. Use `references/toolchain-install.md` when the task is to install or repair the toolchain.
7. If `iverilog`, `verilator`, or `yosys` exists, run the lightest valid check. `scripts/rtl_quickcheck.py` is the preferred wrapper.
8. Report design gaps separately from simulation or toolchain gaps.

## Execution Rules

1. Avoid mixed blocking and nonblocking assignments in sequential logic.
2. Make width, sign, and handshake behavior explicit.
3. Never hand-wave CDC, async resets, or initialization semantics.
4. Prefer small composable modules with testable interfaces over monolithic RTL.
5. Distinguish synthesizable logic from testbench-only convenience code.

## Output Contract

Return:

1. Module contract.
2. Design notes.
3. Testbench plan.
4. Tool results if any.
5. Unresolved timing, reset, CDC, or synthesis risks.
