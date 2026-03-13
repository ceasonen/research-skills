# Implementation Checklist

When a paper or spec is underspecified, check these areas before writing code.

## Model Or Algorithm

1. tensor shapes or signal dimensions
2. normalization and initialization
3. ordering of operations
4. masking, padding, or boundary conditions
5. training versus inference differences

## Data

1. exact input format
2. preprocessing order
3. split definition
4. augmentation or corruption policy
5. filtering and dedup rules

## Training Or Optimization

1. optimizer and scheduler
2. warmup, clipping, regularization
3. batch sizing and gradient accumulation
4. mixed precision details
5. stopping criteria and checkpoint selection

## Evaluation

1. metric implementation details
2. decoding, thresholding, or post-processing
3. seed policy and number of runs
4. error bars or confidence intervals
5. baseline reproduction assumptions

## Systems Or Hardware

1. target device and memory limits
2. latency or throughput measurement method
3. queueing, caching, or batching policy
4. host-device transfer assumptions
5. synchronization or timing constraints

Any missing item stays in the assumption log until it is resolved or explicitly accepted as risk.
