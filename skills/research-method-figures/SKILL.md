---
name: research-method-figures
description: "Design, redraw, and review editable architecture diagrams, method overviews, multimodal pipelines, and module insets for research papers. Use when turning a manuscript, model code, or reference figure into a Draw.io diagram, TikZ source, or publication-ready vector figure. Use a data-plotting workflow for quantitative charts."
license: MIT
---

# Research Method Figures

1. **Map the graph.** Read the method, caption, and relevant code. Identify the figure's main claim, inputs and outputs, module boundaries, and branch provenance. For each unusual connector, record its source, target, direction, and meaning. Distinguish inference data flow, training-only objectives, parameter updates, and reuse. Identify unresolved facts before drawing them.
2. **Choose a layout.** Use parallel lanes for separate modalities, a common column for equivalent stages, and a separate panel for an operator that needs magnification. If the same feature appears across panels, keep its symbol and provenance consistent. An overview should show the mechanism the caption promises, with optional detail in an inset or the text.
3. **Build editable elements.** Use existing project sources and visual conventions first. For a new layout that colleagues will edit by hand, start with the native [Draw.io template](assets/multimodal-method.drawio) ([preview](assets/multimodal-method.svg)). For formula-heavy figures in a TeX project, start with the [TikZ example](assets/residual-gate.tex). Use named text and attached connectors where the format supports them.
4. **Give each visual mark one job.** Use a small palette for branch provenance. Use direct labels for frozen or trainable blocks when status matters. A lighter tint can organize panels. A distinct line style plus legend can identify training-only edges. Reuse notation from the manuscript and retain redundant cues when grayscale matters.
5. **Check the exported figure at its insertion size.** Verify every edge and operator against the method, including shared weights and any train/inference differences. Check for colliding or clipped labels, lost subscripts, disconnected arrowheads, misleading crossings, and excessive blank margins. Reopen or test-edit a representative connector when the format promises editability. Export with the requested formats and report which artifacts were actually rendered or verified.

Deliver the editable source and the requested figure file. For LaTeX, prefer a cropped vector PDF when the venue supports it. Use SVG for vector editing or the web and PNG for a preview or raster-only venue. Keep a source file even when the publication export needs outlined labels. Use only actual experimental examples in an evidence figure and label illustrative inputs accordingly.

Read [templates and sources](references/templates-and-sources.md) for the SAVERA reference, alternatives, and export recipes. Use the reference figure to study layout and visual hierarchy. Derive the actual topology and labels from the current method.
