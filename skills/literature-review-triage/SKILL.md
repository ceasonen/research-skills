---
name: literature-review-triage
description: Find, filter, and compare CS/EE papers across arXiv, OpenReview, Semantic Scholar, OpenAlex, venue pages, and code repos. Use when building a reading list, surveying a subfield, checking novelty, mapping SOTA, or extracting datasets, metrics, baselines, and limitations from papers.
---
# Literature Review Triage

Use this skill for fast, evidence-first literature review in computer science and electronic engineering.

## Core Workflow

1. Lock the scope before searching: task, modality, hardware setting, years, venues, and constraints.
2. Search broadly first, then narrow using citations, benchmarks, and official code repos.
3. Build a paper matrix with `references/review-matrix.md`.
4. Split papers into three buckets:
   - core,
   - adjacent,
   - discard.
5. For each kept paper, extract:
   - problem,
   - method,
   - datasets,
   - metrics,
   - baselines,
   - strengths,
   - limitations,
   - reproduction risk.
6. End with a gap analysis and a recommended reading order.

## Source Priorities

1. Paper PDFs, venue pages, arXiv, and OpenReview.
2. Official project pages and code repositories.
3. Benchmark and dataset pages.
4. Blog posts only for orientation, never as sole evidence.

## Execution Rules

1. Prefer the last 2 to 3 years unless the user asks for historical context.
2. Label every important statement as one of:
   - paper claim,
   - code observation,
   - your synthesis.
3. Track negative signals explicitly: missing code, unclear hyperparameters, weak baselines, limited significance testing, or narrow hardware assumptions.
4. When the user wants a polished survey section or related work prose, hand the outline and evidence table to `research-paper-writing`.
5. Avoid calling something SOTA unless the benchmark, split, and metric match.

## Output Contract

Return:

1. Query framing.
2. A compact paper matrix.
3. Trend synthesis.
4. Gap or opportunity list.
5. Recommended next reads or reproduction targets.
