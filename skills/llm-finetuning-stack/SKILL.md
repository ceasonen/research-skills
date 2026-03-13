---
name: llm-finetuning-stack
description: Plan, debug, and evaluate LLM adaptation pipelines including continued pretraining, SFT, LoRA or QLoRA, preference optimization, reward modeling, and post-training evaluation. Use when building a finetuning stack, diagnosing collapse, choosing data mixtures, or deciding whether a method improved capability or only benchmark fit.
---
# LLM Finetuning Stack

Use this skill when an LLM training run needs to be treated as a research program rather than a recipe.

## Core Workflow

1. Lock the adaptation objective:
   - domain adaptation,
   - instruction following,
   - preference alignment,
   - tool use,
   - reasoning.
2. Separate data curation, tokenizer effects, optimization, and evaluation.
3. Use `references/failure-modes.md` when loss curves, style drift, or capability regressions look suspicious.
4. Compare full finetuning, parameter-efficient finetuning, and prompting against the same task definition.
5. Evaluate on both target tasks and capability retention tasks.

## Execution Rules

1. Never judge a finetune by training loss alone.
2. Track base model, tokenizer, template, and chat format exactly.
3. Distinguish behavior change from memorization or formatting overfit.
4. Keep safety regressions and hallucination rates visible even when task metrics improve.

## Output Contract

Return:

1. Objective and stack summary.
2. Data and optimization risks.
3. Evaluation plan.
4. Likely failure modes.
5. Recommended next experiment.
