---
name: training-infra-debugging
description: Debug ML training infrastructure including data loaders, distributed training, checkpointing, mixed precision, memory pressure, logging, and experiment orchestration. Use when runs diverge, slow down, OOM, deadlock, or produce inconsistent metrics across nodes, seeds, or restarts.
---
# Training Infra Debugging

Use this skill when the model is not the only system under test.

## Core Workflow

1. Capture the failing run signature:
   - hardware,
   - framework,
   - launcher,
   - world size,
   - precision,
   - checkpoint source.
2. Classify the failure:
   - crash,
   - hang,
   - silent divergence,
   - throughput collapse,
   - nondeterministic restart.
3. Narrow the fault domain:
   - input pipeline,
   - model graph,
   - optimizer,
   - communication,
   - filesystem,
   - orchestration.
4. Reduce to the smallest failing configuration.
5. Add instrumentation before attempting broad fixes.

## Execution Rules

1. Check one-node and one-batch behavior first.
2. Separate correctness from performance.
3. Treat data-order drift, seed handling, and checkpoint resume semantics explicitly.
4. Record environment variables and library versions when distributed systems are involved.

## Output Contract

Return:

1. Failure classification.
2. Fault domain ranking.
3. Minimum reproducer.
4. Highest-value probes.
5. Likely fixes and validation criteria.
