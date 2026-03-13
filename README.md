# research-skills

Personal Codex skills for CS/EE research workflows. This repository mirrors the non-system skills from my local Codex setup and keeps them in a clean, installable GitHub layout.

## Repository layout

- `skills/`: shareable skill directories, one installable skill per folder.
- `catalog.json`: machine-readable index of the published skills.
- `scripts/sync_local_skills.py`: sync local skills into this repository.
- `scripts/validate_repo.py`: validate structure, metadata, and publication safety.
- `.github/workflows/validate.yml`: run validation on every push and pull request.

## Install from GitHub

Install a single skill with Codex's `skill-installer` helper:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo ceasonen/research-skills \
  --path skills/codebase-onboarding
```

Install multiple skills in one pass by repeating `--path`:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo ceasonen/research-skills \
  --path skills/codebase-onboarding \
  --path skills/research-paper-writing \
  --path skills/rtl-fpga-workflow
```

You can also copy `skills/<skill-name>` into `~/.codex/skills/<skill-name>` manually. Restart Codex after installation.

## Sync local updates

When the local working set in `~/.codex/skills` changes, refresh this repository with:

```bash
python scripts/sync_local_skills.py --clean
python scripts/validate_repo.py
```

`--clean` removes published skills that no longer exist in the local source. Use `--source` if your local skills live somewhere other than the default Codex directory.

## Skill catalog

### Research workflow

- [`benchmark-error-analysis`](skills/benchmark-error-analysis): Build evaluation plans, slice analyses, and regression diagnosis workflows.
- [`codebase-onboarding`](skills/codebase-onboarding): Map unfamiliar repositories and identify the smallest safe edit surface.
- [`dataset-curation`](skills/dataset-curation): Design datasets, splits, provenance tracking, and leakage checks.
- [`latex-build-camera-ready`](skills/latex-build-camera-ready): Fix LaTeX builds and prepare clean submission artifacts.
- [`literature-review-triage`](skills/literature-review-triage): Compare papers quickly and build evidence tables for a topic.
- [`ml-experiment-planner`](skills/ml-experiment-planner): Turn research ideas into baseline, ablation, and compute plans.
- [`paper-to-implementation`](skills/paper-to-implementation): Convert papers, specs, and diagrams into staged implementation plans.
- [`peer-review-rebuttal`](skills/peer-review-rebuttal): Draft evidence-backed rebuttals and revision plans.
- [`research-direction-scouting`](skills/research-direction-scouting): Rank project directions by novelty, feasibility, and risk.
- [`research-paper-writing`](skills/research-paper-writing): Refine paper structure, flow, and section-level writing quality.
- [`research-reproducibility-audit`](skills/research-reproducibility-audit): Audit papers, code, and artifacts for reproducibility gaps.

### ML and systems

- [`accelerator-kernel-optimization`](skills/accelerator-kernel-optimization): Diagnose kernel throughput, bandwidth, launch, and transfer bottlenecks.
- [`compiler-runtime-analysis`](skills/compiler-runtime-analysis): Analyze compiler lowering, code generation, scheduling, and runtime overhead.
- [`distributed-systems-debugging`](skills/distributed-systems-debugging): Isolate retries, replication, partitions, backpressure, and tail latency issues.
- [`llm-finetuning-stack`](skills/llm-finetuning-stack): Plan and debug SFT, LoRA, QLoRA, preference optimization, and post-training evaluation.
- [`multimodal-evaluation`](skills/multimodal-evaluation): Evaluate vision-language, audio-language, video-language, and document-language systems.
- [`retrieval-rag-systems`](skills/retrieval-rag-systems): Design and debug retrieval, reranking, packing, grounding, and citation workflows.
- [`systems-performance-review`](skills/systems-performance-review): Review latency, throughput, memory, power, and reliability tradeoffs.
- [`training-infra-debugging`](skills/training-infra-debugging): Debug OOMs, hangs, checkpointing, mixed precision, and distributed training failures.

### Hardware and EE

- [`control-systems-state-estimation`](skills/control-systems-state-estimation): Design estimators, observers, and sensor fusion structures.
- [`dsp-algorithm-design`](skills/dsp-algorithm-design): Build DSP pipelines with clear transforms, error budgets, and implementation tradeoffs.
- [`embedded-firmware-debugging`](skills/embedded-firmware-debugging): Debug MCU bring-up, RTOS timing, drivers, DMA, and peripherals.
- [`hardware-formal-verification`](skills/hardware-formal-verification): Derive assertions, proof plans, and stronger correctness checks for RTL.
- [`pcb-schematic-review`](skills/pcb-schematic-review): Audit power trees, clocks, resets, interfaces, and board-level risks.
- [`robotics-perception-planning`](skills/robotics-perception-planning): Review robotics stacks spanning perception, localization, planning, and sim-to-real.
- [`rtl-fpga-workflow`](skills/rtl-fpga-workflow): Review RTL, testbenches, FPGA toolchains, constraints, and timing-closure preparation.
- [`wireless-communications-analysis`](skills/wireless-communications-analysis): Analyze channels, modulation, coding, synchronization, and receiver tradeoffs.

See [`catalog.json`](catalog.json) for the complete machine-readable index.
