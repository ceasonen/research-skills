---
name: wireless-communications-analysis
description: Analyze wireless and communication-system research including channel models, modulation, coding, synchronization, detection, equalization, link adaptation, and MIMO tradeoffs. Use when designing communication experiments, debugging BER or throughput behavior, comparing signal-processing and learning-based approaches, or reviewing communication-system papers.
---
# Wireless Communications Analysis

Use this skill when throughput, reliability, and channel assumptions all matter at once.

## Core Workflow

1. Define the channel, bandwidth, latency target, mobility regime, and interference model.
2. Split the link into synchronization, estimation, equalization, coding, and adaptation stages.
3. Compare performance on BER, BLER, throughput, latency, and robustness separately.
4. Check whether claimed gains depend on a narrow channel or SNR regime.
5. End with the next experiment that best separates algorithmic gain from simulation convenience.

## Execution Rules

1. Keep units explicit: SNR, Eb/N0, bandwidth, and symbol rate.
2. Separate channel-model gains from receiver-design gains.
3. Report deployment assumptions such as CSI availability and feedback cost.
4. Treat synchronization and estimation errors as part of system performance, not preprocessing.

## Output Contract

Return:

1. Link model summary.
2. Evaluation regime.
3. Main bottlenecks.
4. Comparison risks.
5. Next experiment or design change.
