---
name: retrieval-rag-systems
description: Design, evaluate, and debug retrieval and RAG systems including indexing, chunking, embedding choice, reranking, context packing, citation grounding, and latency-cost tradeoffs. Use when building or auditing a search, QA, or agent memory stack for research or production.
---
# Retrieval RAG Systems

Use this skill when a retrieval pipeline needs to be treated as a system, not a prompt.

## Core Workflow

1. Define the task and what counts as grounded success.
2. Decompose the pipeline:
   - ingestion,
   - cleaning,
   - chunking,
   - embedding,
   - retrieval,
   - reranking,
   - context construction,
   - generation.
3. Add evaluation at both retrieval and answer levels.
4. Measure recall, precision, latency, cost, and citation faithfulness separately.
5. Audit failure cases by query type and document source.

## Execution Rules

1. Do not judge the system by answer quality alone.
2. Keep retrieval metrics separate from generation metrics.
3. Treat chunking and metadata as major model choices.
4. Check contamination, stale indices, and duplicate passages.

## Output Contract

Return:

1. Pipeline map.
2. Measurement plan.
3. Failure buckets.
4. Ranked interventions.
5. Risks around grounding, cost, and latency.
