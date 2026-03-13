# LLM Finetuning Failure Modes

Check these before changing many hyperparameters at once.

## Data

1. prompt and response template mismatch
2. train and eval contamination
3. narrow style overfit
4. weak refusal or safety examples
5. tokenizer or truncation artifacts

## Optimization

1. learning rate too high for PEFT scale
2. warmup too short
3. gradient accumulation or effective batch mismatch
4. mixed precision instability
5. checkpoint resume inconsistency

## Evaluation

1. benchmark fit without capability retention
2. format correctness counted as reasoning gain
3. hidden label leakage in synthetic data
4. prompt template drift between runs
5. judge model bias when using LLM-as-a-judge
