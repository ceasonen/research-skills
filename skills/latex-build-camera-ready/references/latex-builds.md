# LaTeX Build Triage

## Common Build Orders

Use the project's existing flow when it exists. Otherwise try the smallest likely order:

1. `pdflatex main.tex`
2. `bibtex main` or `biber main`
3. `pdflatex main.tex`
4. `pdflatex main.tex`

If `latexmk` is present and the repo already uses it, prefer the repo command.

## Log Triage Order

1. missing file or package
2. undefined control sequence
3. bibliography backend mismatch
4. encoding or font issue
5. float overflow or margin problem
6. cross-reference warnings

## Common Failure Modes

1. `\cite` unresolved because the wrong backend was used
2. conference class requires a specific option set
3. figures or PDFs are in the wrong relative path
4. stale `.aux`, `.bbl`, or `.bcf` files from a different build flow
5. overfull boxes hide the real layout problem

## Cleanup Rule

Only remove generated files when you know the project's intended build flow. Do not delete source `.bib`, `.sty`, template files, or conference macros.
