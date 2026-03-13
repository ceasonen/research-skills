---
name: codebase-onboarding
description: Rapidly map an unfamiliar research or engineering codebase, identify entry points, execution paths, configuration layers, tests, and risky modules. Use when inheriting a project, preparing a reproduction, reviewing a repo for collaboration, or locating where to modify a model, runtime, compiler, or hardware flow.
---
# Codebase Onboarding

Use this skill to compress the first day of repo reading into a structured map.

## Core Workflow

1. Identify build system, runtime entry points, and test commands.
2. Map the top-level architecture and the config surface.
3. Trace one representative execution path end to end.
4. Separate generated code, vendor code, and owned code.
5. Produce the minimal file list needed for the user's task.

## Execution Rules

1. Prefer concrete paths and functions over vague architecture prose.
2. Distinguish authoritative config from defaults and examples.
3. Call out dead ends, stale docs, and scripts that appear unused.
4. End with the smallest safe edit surface.

## Output Contract

Return:

1. Architecture map.
2. Entry points.
3. Config and dependency map.
4. Highest-risk modules.
5. Recommended reading or edit order.
