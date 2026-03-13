---
name: multimodal-evaluation
description: Evaluate and debug vision-language, audio-language, video-language, document, and embodied multimodal systems. Use when designing benchmark suites, auditing modality balance, analyzing hallucinations, grounding errors, OCR failures, temporal failures, or comparing models across tasks that mix perception and reasoning.
---
# Multimodal Evaluation

Use this skill when a multimodal result mixes perception quality with reasoning quality and the benchmark needs to disentangle them.

## Core Workflow

1. Split the task into modality acquisition, representation, grounding, and reasoning.
2. Build slices by modality, difficulty, corruption, temporal span, and domain.
3. Check whether failures come from sensing, alignment, or reasoning.
4. Evaluate citation or evidence grounding when outputs refer to visual or acoustic facts.
5. Compare closed-form metrics with qualitative audits on paired examples.

## Execution Rules

1. Do not collapse OCR, grounding, and reasoning into one score.
2. Track modality coverage and missing-modality behavior.
3. Audit prompt and input formatting carefully for video and document pipelines.
4. Separate benchmark novelty from annotation noise.

## Output Contract

Return:

1. Task decomposition.
2. Slice plan.
3. Failure buckets.
4. Metric risks.
5. Next evaluation round.
