---
name: control-systems-state-estimation
description: Design and debug state estimation, filtering, system identification, and control-oriented models for robotics, autonomous systems, and embedded control. Use when choosing observers, Kalman variants, sensor fusion structure, stability assumptions, or diagnosing drift, lag, and closed-loop estimation failures.
---
# Control Systems State Estimation

Use this skill when sensing, dynamics, and feedback assumptions determine whether the whole system is stable.

## Core Workflow

1. Define the state, control inputs, measurements, disturbances, and operating regime.
2. Choose the model fidelity needed for the decision at hand.
3. Use `references/estimation-checklist.md` to check observability, noise assumptions, delays, and linearization points.
4. Separate estimation quality from controller quality.
5. Validate in both nominal and failure regimes.

## Execution Rules

1. Make continuous-time versus discrete-time assumptions explicit.
2. Track units and coordinate frames carefully.
3. Treat delay and bias as first-class model components.
4. Do not call a filter stable without the operating regime and assumptions.

## Output Contract

Return:

1. State and measurement model.
2. Estimator choice rationale.
3. Failure modes.
4. Validation plan.
5. Open modeling risks.
