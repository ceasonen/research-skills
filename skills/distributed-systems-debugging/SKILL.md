---
name: distributed-systems-debugging
description: Debug distributed systems behavior including consistency issues, queue backlogs, retries, partitions, replica divergence, tail latency, and backpressure. Use when a service mesh, stream processor, storage system, scheduler, or multi-node research system behaves differently under scale than in local tests.
---
# Distributed Systems Debugging

Use this skill when concurrency and partial failure make the bug disappear in single-node reasoning.

## Core Workflow

1. Define the topology, workload, failure model, and correctness expectations.
2. Build a timeline across nodes and queues.
3. Separate control-plane from data-plane failures.
4. Check retries, idempotency, timeouts, leases, and clock assumptions.
5. Reproduce on the smallest cluster that preserves the bug.

## Execution Rules

1. Treat tail latency as a separate problem from median latency.
2. Distinguish consistency bugs from observability gaps.
3. Make message ordering and dedup assumptions explicit.
4. Check whether autoscaling, rebalancing, or GC changed the system state.

## Output Contract

Return:

1. Failure timeline.
2. Ranked fault domains.
3. Minimal reproducer.
4. Highest-value probes.
5. Fix validation plan.
