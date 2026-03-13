---
name: robotics-perception-planning
description: Design and debug robotics pipelines spanning perception, localization, mapping, planning, control interfaces, and sim-to-real transfer. Use when evaluating a robot stack, diagnosing failures in closed-loop behavior, planning experiments, or comparing perception-driven versus policy-driven system designs.
---
# Robotics Perception Planning

Use this skill when robot behavior emerges from multiple coupled modules and a single metric hides the real failure.

## Core Workflow

1. Define the robot task, sensing stack, actuation limits, and success criteria.
2. Map the closed loop:
   - sensing,
   - state estimation,
   - world model,
   - planning,
   - control interface,
   - safety interlocks.
3. Use `references/sim2real-checklist.md` when simulation results do not transfer.
4. Separate open-loop module quality from closed-loop task success.
5. End with the next experiment that most cleanly isolates the failure source.

## Execution Rules

1. Track latency and synchronization between sensors and control decisions.
2. Treat calibration, frame transforms, and state estimation drift as first-class suspects.
3. Separate planner weakness from perception error and actuator saturation.
4. Keep safety and fallback behavior explicit.

## Output Contract

Return:

1. Closed-loop map.
2. Failure decomposition.
3. Measurement plan.
4. Sim-to-real risks.
5. Best next experiment.
