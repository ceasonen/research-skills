---
name: ml-experiment-planner
description: Plan ML experiments, ablations, hyperparameter sweeps, and resource budgets for research projects in AI, systems, and signal-processing-adjacent work. Use when starting an experiment series, defining baselines, sizing GPU or CPU needs, or turning ideas into a reproducible run plan.
---
# ML Experiment Planner

Use this skill to turn a vague research idea into a bounded experiment program.

## Core Workflow

1. State the research question and the decision rule for success.
2. Pick baselines, sanity checks, and one minimal smoke test.
3. Define the experiment matrix:
   - dataset,
   - model,
   - training setting,
   - seed policy,
   - checkpoint policy.
4. Set budgets for wall-clock time, accelerator hours, storage, and logging volume.
5. Define logging requirements: config snapshot, seed, git revision, environment, metrics, and artifacts.
6. Sequence runs:
   - smoke,
   - baseline,
   - ablation,
   - scale-up.
7. Add kill criteria and rollback conditions before launching expensive jobs.

## Execution Rules

1. Avoid unbounded sweeps.
2. Change one factor at a time in ablations.
3. Always include at least one deterministic or near-deterministic smoke run.
4. State what result would change your mind.
5. Separate research metrics from engineering metrics such as throughput, memory, and cost.

## Output Contract

Return:

1. Experiment matrix.
2. Resource budget.
3. Run order.
4. Logging and artifact plan.
5. Expected failure modes and stop conditions.
