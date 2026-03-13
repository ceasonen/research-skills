---
name: latex-build-camera-ready
description: Build and debug LaTeX research papers, posters, and reports; fix bibliography, figures, tables, reviewer-mode toggles, and camera-ready packaging. Use when a paper compiles poorly, references break, margins overflow, anonymization must be restored, or a submission artifact needs cleanup.
---
# LaTeX Build Camera Ready

Use this skill for build, packaging, and template hygiene. Use `research-paper-writing` for prose.

## Core Workflow

1. Identify the build system: pdflatex and bibtex, pdflatex and biber, latexmk, or conference wrapper.
2. Run the first real failing command and inspect the log.
3. Use `references/latex-builds.md` for common build orders and log triage.
4. Fix one error class at a time:
   - missing files,
   - package conflicts,
   - floats,
   - bibliography,
   - encoding,
   - overfull boxes.
5. Keep content edits separate from build fixes.

## Execution Rules

1. Preserve conference template constraints and macros.
2. Prefer minimal reproducible compile commands.
3. Track generated files separately from source files.
4. Do not remove required anonymization or camera-ready toggles without explaining the consequences.
5. Report remaining warnings even when the PDF builds.

## Output Contract

Return:

1. Failing command.
2. Root cause.
3. Concrete fix.
4. Rerun command.
5. Remaining warnings or style risks.
