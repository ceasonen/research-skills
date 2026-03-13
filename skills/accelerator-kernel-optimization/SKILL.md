---
name: accelerator-kernel-optimization
description: Review and optimize kernels and data movement for CUDA, Triton, Metal, OpenCL, SIMD, and accelerator-style workloads. Use when diagnosing throughput gaps, memory bandwidth limits, launch overhead, occupancy issues, kernel fusion tradeoffs, or host-device transfer bottlenecks in ML and systems research.
---
# Accelerator Kernel Optimization

Use this skill when a compute kernel underperforms and you need a disciplined performance model.

## Core Workflow

1. State the target hardware and workload shape.
2. Build a simple bound:
   - compute,
   - memory,
   - launch,
   - transfer.
3. Identify the main limiter before rewriting code.
4. Inspect memory access patterns, parallelism shape, synchronization, and numerical constraints.
5. Benchmark the smallest kernel that isolates the issue.

## Execution Rules

1. Use a roofline-style mindset even if you do not draw the full plot.
2. Separate compilation issues from runtime bottlenecks.
3. Treat layout, padding, and transfer volume as algorithm choices.
4. Never claim a speedup without the baseline kernel, input shape, and hardware context.

## Output Contract

Return:

1. Bottleneck model.
2. Suspected limiting factors.
3. Microbenchmark plan.
4. Candidate optimizations.
5. Validation risks.
