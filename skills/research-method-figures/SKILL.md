---
name: research-method-figures
description: "Design, redraw, and review editable paper figures, including method overviews, model architectures, pipelines, schedules, qualitative comparisons, diagnostics, and data-driven plots. Use the paper-figure atlas to choose a layout, then produce Draw.io, TikZ, or data-backed vector output from the current manuscript, code, or evidence."
license: MIT
---

# Research Method Figures

1. **Identify the job of the figure.** Read the caption and the relevant method, code, or results. For a schematic, identify inputs, outputs, module boundaries and branch provenance. Check ambiguous arrows against the implementation. For evidence, identify the comparison condition, unit, cases, and what should share a scale.
2. **Choose a structure.** Open the [paper-figure atlas](references/figure-atlas.md), choose one or two entries that answer the same visual question, and inspect the relevant original. The atlas covers architectures, workflows, execution schedules, evidence grids, diagnostic views, training curves, heatmaps and paired comparisons.
3. **Build with the right source.** Retain existing project sources when suitable. Copy the selected native Draw.io template for an editable schematic or evidence layout. Use the [TikZ example](assets/residual-gate.tex) for exact LaTeX notation. For quantitative figures, follow [the plot recipes](references/atlas-plot-recipes.md) and pass measured data as CSV. Preserve the source alongside the export.
4. **Give each visual mark one job.** Use a small palette for branch provenance. Use direct labels for frozen or trainable blocks when status matters. A lighter tint can organize panels. A distinct line style plus legend can identify training-only edges. Reuse notation from the manuscript and retain redundant cues when grayscale matters.
5. **Check the exported figure at its insertion size.** Verify every edge and operator against the method, including shared weights and any train/inference differences. Check for colliding or clipped labels, lost subscripts, disconnected arrowheads, misleading crossings, and excessive blank margins. Reopen or test-edit a representative connector when the format promises editability. Export with the requested formats and report which artifacts were actually rendered or verified.

Deliver the editable source and the requested figure file. For LaTeX, prefer a cropped vector PDF when the venue supports it. Use SVG for vector editing or the web and PNG for a preview or raster-only venue. Keep a source file even when the publication export needs outlined labels. Use only actual experimental examples in an evidence figure and label illustrative inputs accordingly.

Read [templates and sources](references/templates-and-sources.md) for drawing tools and export options. Use cited figures to study layout and visual hierarchy. Derive the actual topology, evidence and labels from the current work.
