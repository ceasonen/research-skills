# Templates and sources

## What works in the reference figure

- **SAVERA, Figure 2.** The upper panel introduces vision and text streams and shows alignment at the relevant representation. The lower panel expands the fusion mechanism and a separate legend explains the notation. Use this combination of overview and close-up when a mechanism needs more detail than a single row can carry. Read the training labels carefully. The caption-derived alignment signal and prompt-derived fusion input have different roles. [Paper and Figure 2](https://arxiv.org/html/2611.32828v1#S3)
- **Semantic palettes.** Reuse a modality's color and symbolic label where it reappears. Use the caption for the distinction between training and inference when an arrow style alone would be ambiguous. If color is already encoding modality, distinguish module state with a word, badge, or outline.

## Choose a starting point

| Resource | Useful for |
| --- | --- |
| [Academic Diagram Skill](https://github.com/plbbl/academic-diagram-skill) | Browse the attributed reference atlas and editable examples by layout. The upstream repository documents separate rights for example artwork. |
| [CVPR-Figure templates](https://github.com/ChizkiyahuOhayon/CVPR-Figure/tree/main/templates) | Study dual-branch, gated-module and teacher–student layouts. The project uses a declarative specification and offers native PPTX and Visio export. |
| [draw.io official examples](https://www.drawio.com/docs/diagram-types/) | Find editable connectors, containers, layers, and general architecture examples. Start here when collaborators will move shapes manually. |
| [PlotNeuralNet](https://github.com/HarisIqbal88/PlotNeuralNet) and [PGF/TikZ](https://ctan.org/pkg/pgf) | Use PlotNeuralNet for stacked feature maps in conventional network diagrams. Use TikZ for exact math labels and reproducible LaTeX placement. |
| [SciSketch](https://aclanthology.org/2025.emnlp-demos.28/) and [PaperBanana](https://research.google/pubs/paperbanana-automating-academic-illustration-for-ai-scientists/) | Study automated planning and style retrieval for complex figures. Use their layouts as references when the final figure needs native connectors and verified labels. |

The bundled examples are original teaching assets. Their sample graph is illustrative and contains no reported experimental results.

## Run the bundled examples

**Draw.io.** Open a copy of `assets/multimodal-method.drawio`. The panel frames and labels are on a background layer. Modules, token stacks, notation, and arrows are on the editable diagram layer. To adapt the sample, replace input, branch, and output labels and reconnect the training and residual paths to the actual architecture. Enable mathematical typesetting for TeX labels when needed. [Draw.io math typesetting](https://www.drawio.com/docs/manual/text/math-typesetting/)

The desktop executable is usually `drawio` on PATH or `/Applications/draw.io.app/Contents/MacOS/draw.io` on macOS. Replace `drawio` below with the available executable and run inside an output directory using a copy of the source.

```sh
drawio --export --crop --border 8 --output method.pdf method.drawio
drawio --export --border 8 --svg-theme light --output method.svg method.drawio
```

The template uses plain labels with explicit line breaks to preserve native SVG text. For MathJax or rich-text labels, check the export in the target PDF or SVG renderer. A web SVG can show text that another editor fails to render. When editing needs to survive exchange, send the native source alongside the export. [Draw.io SVG export](https://www.drawio.com/docs/manual/export/export-to-svg/) · [Draw.io PDF export](https://www.drawio.com/docs/manual/export/export-to-pdf/)

**TikZ.** Copy `assets/residual-gate.tex` into the figure directory. Compile with `pdflatex -halt-on-error residual-gate.tex`. The TeX file holds the formula, node anchors and edge routes. The cropped output can go into `\includegraphics`. Replace the sample notation throughout, including caption and labels.

## Review before delivery

Compare solid flow and dashed objectives to the method, then inspect the exported graphic at the manuscript's intended figure width. In the bundled examples, the visual feature has two destinations and the residual path re-enters the sum from above. Move a node in the source and verify that its connectors follow. Re-render after any manual changes that affect labels, routes, or cropping.
