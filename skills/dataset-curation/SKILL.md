---
name: dataset-curation
description: Create and audit datasets for CS and EE research, including schema design, collection pipelines, deduplication, split strategy, leakage prevention, labeling QA, licensing, and provenance tracking. Use when building a dataset, merging corpora, preparing train, validation, and test splits, or validating a benchmark before publication.
---
# Dataset Curation

Use this skill when dataset quality is the hidden variable behind the whole project.

## Core Workflow

1. Define the unit of data and the schema before collection expands.
2. Track provenance and license per source.
3. Deduplicate exact and near duplicates.
4. Freeze the split policy before training.
5. Check leakage across content, metadata, time, device identity, and preprocessing artifacts.
6. Audit labels, class balance, and hardware or environment coverage.
7. Produce versioned manifests for raw data, processed data, and exclusions.

## Execution Rules

1. Keep raw data immutable.
2. Never split after feature engineering if leakage risk exists.
3. Log exclusion rules and uncertain labels.
4. Document annotator instructions and disagreement handling.
5. Make licensing and privacy constraints first-class, not appendix material.

## Output Contract

Return:

1. Schema summary.
2. Provenance ledger.
3. Split policy.
4. Leakage risk list.
5. QA summary and next actions.
