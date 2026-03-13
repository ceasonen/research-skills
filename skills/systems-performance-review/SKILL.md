---
name: systems-performance-review
description: Review CS and EE system designs for latency, throughput, memory, power, reliability, and concurrency risks. Use when designing distributed systems, edge pipelines, compilers and runtime stacks, accelerators, or hardware-software co-design, and when debugging bottlenecks in data or inference pipelines.
---
# Systems Performance Review

Use this skill to reason about bottlenecks before the project burns time on blind optimization.

## Core Workflow

1. State the workload, SLOs, hardware targets, and failure envelope.
2. Draw the critical path and concurrency model.
3. Build a budget table for latency, bandwidth, memory, storage, and power.
4. Identify queueing, serialization, synchronization, and data-movement hotspots.
5. Propose measurement points before proposing optimizations.
6. Rank fixes by expected impact, risk, and implementation cost.

## Execution Rules

1. Do not optimize without a budget.
2. Separate steady-state behavior from tail behavior.
3. Check batching, caching, affinity, backpressure, retries, and failure recovery.
4. For accelerators and edge systems, include host-device transfer and power or thermal constraints.
5. Be explicit about whether a claim is analytical, measured, or inferred.

## Output Contract

Return:

1. Budget table.
2. Bottleneck list.
3. Measurement plan.
4. Ranked interventions.
5. Risks and open assumptions.
