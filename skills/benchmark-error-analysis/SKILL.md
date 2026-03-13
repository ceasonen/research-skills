---
name: benchmark-error-analysis
description: Build evaluation plans and error-analysis workflows for ML, retrieval, generation, systems benchmarks, and embedded or perception pipelines. Use when adding metrics, checking regressions, designing ablations, interpreting leaderboard changes, or debugging why a model improved on one slice and failed on another.
---
# Benchmark Error Analysis

Use this skill when a metric moved and you need to know whether it means anything real.

## Core Workflow

1. Confirm the unit of evaluation and split definitions.
2. Check metric implementation against the benchmark or paper specification.
3. Add slice-level analysis by class, domain, device, hardware condition, or data source.
4. Compare baseline and candidate on paired examples whenever possible.
5. Run statistical sanity checks when the sample size allows it.
6. Group failures into actionable regression buckets.

## Execution Rules

1. Distinguish metric drift from model improvement.
2. Prefer paired evaluation over separate summary tables.
3. Report confidence intervals, bootstrap ranges, or at least variance across seeds when feasible.
4. Check for prompt leakage, contamination, and benchmark version drift.
5. Separate benchmark-facing metrics from deployment-facing metrics.

## Output Contract

Return:

1. Metric table.
2. Slice breakdown.
3. Top error buckets.
4. Suspected causes.
5. Follow-up experiments.
