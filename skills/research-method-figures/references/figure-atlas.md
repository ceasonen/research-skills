# 论文图谱

按图要回答的问题选初稿，再对照对应论文原图。图谱收录 24 篇、24 个可编辑起点。示例框架使用原创内容，绘图脚本的演示数据有明确标记。

[打开图谱预览](../assets/atlas/index.html) · [图表输入格式与导出](atlas-plot-recipes.md) · [常用工具与导出](templates-and-sources.md)

本地参考图片缓存位于 `~/.local/share/research-method-figures/originals/`。其中的 INDEX.md 记录具体论文、图号、原文和本地文件。

## 用法

1. 选择表达任务相近的结构，读取原图与图注，写出这一张图最需要讲清楚的关系。
2. 把模板另存到项目目录。先核对数据流、训练阶段、输入输出和符号，再套版式。定性图替换为匹配条件的真实样例，定量图用原始数据运行脚本。
3. 在实际论文列宽预览。检查箭头端点、线型语义、色条、轴单位、图例、字号、裁切及空白。交付源文件和插稿版本。

## 图例与交付

方法类的实线用于主数据流。虚线的含义应在图例或标签中明示，例如训练目标、历史状态回流或返工。颜色可随分支来源保持一致，冻结或可训练等状态尽量用文字标注。

`.drawio` 中的面板边界与主要对象可单独编辑。遇到数学或富文本的标签，检查目标渲染器中的 SVG/PDF。定量图从脚本和 CSV 重生成。

## 架构与机制

| 选用场景 | 论文原图 | 编辑与预览 | 借鉴点 |
| --- | --- | --- | --- |
| 双分支对齐与融合 | [SAVERA · Fig. 2](https://arxiv.org/html/2611.32828v1#S2.F2) | [源文件](../assets/multimodal-method.drawio) · [SVG](../assets/multimodal-method.svg) | 输入来源用并行轨标清。把训练约束画为虚线，再单开一块放大融合算子。 |
| 有状态记忆回路 | [SAM 2 · Fig. 3](https://arxiv.org/html/2408.00714v2#S4.F3) | [源文件](../assets/atlas/diagrams/stateful-memory.drawio) · [SVG](../assets/atlas/previews/stateful-memory.svg) | 当前步数据流走主线，历史状态读取与下一步写回走回路。分别标明时刻。 |
| 多任务 Token 序列 | [Show-o · Fig. 2](https://arxiv.org/html/2408.12528v7#S2.F2) | [源文件](../assets/atlas/diagrams/token-grammar.drawio) · [SVG](../assets/atlas/previews/token-grammar.svg) | 同一底层模型上方并列展示任务输入，使用固定色和位置表示视觉、文本与控制 token。 |
| 独立编码与共享核心 | [Janus · Fig. 2](https://arxiv.org/html/2410.13848v1#S3.F2) | [源文件](../assets/atlas/diagrams/split-encoders-shared-core.drawio) · [SVG](../assets/atlas/previews/split-encoders-shared-core.svg) | 让专用编码器各自成列，共享骨干横跨两列。出口在各列上方与实际任务匹配。 |
| 冻结主干与残差适配器 | [ControlNet · Fig. 2](https://arxiv.org/html/2302.05543v3#S3.F2) | [源文件](../assets/atlas/diagrams/residual-adapter.drawio) · [SVG](../assets/atlas/previews/residual-adapter.svg) | 用改动前后两面板隔离新模块。保留原来的直通路径，把新增条件支路接到实际求和点。 |
| 两阶段训练桥接 | [BLIP-2 · Fig. 1](https://arxiv.org/html/2301.12597v3#S1.F1) | [源文件](../assets/atlas/diagrams/two-stage-bridge.drawio) · [SVG](../assets/atlas/previews/two-stage-bridge.svg) | 两阶段复用模块的颜色与位置。分别标出训练目标和新增解码器，区分权重传承与特征流。 |
| 共享解码器与并行预测头 | [DETR · Fig. 2](https://arxiv.org/html/2005.12872v3#S3.F2) | [源文件](../assets/atlas/diagrams/query-parallel-heads.drawio) · [SVG](../assets/atlas/previews/query-parallel-heads.svg) | 先编码图像，再从独立入口注入查询。右侧用平行输出明确预测的是一个集合。 |

## 流程与调度

| 选用场景 | 论文原图 | 编辑与预览 | 借鉴点 |
| --- | --- | --- | --- |
| 并行工作流时间轨 | [FlashAttention-3 · Fig. 1](https://arxiv.org/html/2407.08608v2#S3.F1) | [源文件](../assets/atlas/diagrams/overlap-schedule.drawio) · [SVG](../assets/atlas/previews/overlap-schedule.svg) | 在统一时间轴上交错画两条工作轨。只在定义了真实时间单位时按实际长度比较。 |
| 重排前后对照 | [PaperBanana · Fig. 6](https://arxiv.org/html/2601.23265v2#S6.F6) | [源文件](../assets/atlas/diagrams/visual-restyle.drawio) · [SVG](../assets/atlas/previews/visual-restyle.svg) | 并排展示同一组模块与连接的两种构图，便于核对视觉调整是否保留拓扑。 |
| 资源提取、整理与重组 | [Crafter · Fig. 2](https://arxiv.org/html/2605.30611v1#S3.F2) | [源文件](../assets/atlas/diagrams/asset-reassembly.drawio) · [SVG](../assets/atlas/previews/asset-reassembly.svg) | 按交付物划分处理阶段，用可替换的中间对象清单说明各段如何交接。 |
| 几何采样与聚合 | [NeRF · Fig. 2](https://arxiv.org/html/2003.08934v2#S2.F2) | [源文件](../assets/atlas/diagrams/ray-sampling.drawio) · [SVG](../assets/atlas/previews/ray-sampling.svg) | 把几何示意接到求值和聚合链路。用有序采样点表达读序，让示意与运算能直接对照。 |
| 观测、预测与执行窗口 | [Diffusion Policy · Fig. 2](https://arxiv.org/html/2303.04137v5#S1.F2) | [源文件](../assets/atlas/diagrams/receding-horizon.drawio) · [SVG](../assets/atlas/previews/receding-horizon.svg) | 三条时间轨共享同一时刻原点。分别标出已观测片段、预测范围及实际执行的前缀。 |
| 可检查的中间表示 | [DeepYOLO · Fig. 1](https://doi.org/10.1109/IJCNN69854.2026.11729294) | [源文件](../assets/atlas/diagrams/symbolic-interface.drawio) · [SVG](../assets/atlas/previews/symbolic-interface.svg) | 把报告字段放在感知与推理之间的独立面板。用真实字段展示局部接口，问题走额外输入端。 |
| 规划、实现与定点复核 | [LiveFigure · Fig. 2](https://arxiv.org/html/2605.23527v1#S3.F2) | [源文件](../assets/atlas/diagrams/feedback-review-loop.drawio) · [SVG](../assets/atlas/previews/feedback-review-loop.svg) | 采用分区工作流表达产物交接和返工。审查结果分成批准与带修订项返回两条路径。 |

## 定性与诊断

| 选用场景 | 论文原图 | 编辑与预览 | 借鉴点 |
| --- | --- | --- | --- |
| 等条件结果矩阵 | [AnyDoor · Fig. 5](https://arxiv.org/html/2307.09481v2#S3.F5) | [源文件](../assets/atlas/diagrams/matched-comparison-grid.drawio) · [SVG](../assets/atlas/previews/matched-comparison-grid.svg) | 每行固定一个样例，每列固定方法或条件。保持裁剪、视角、比例与放大框位置一致。 |
| 原图与特征成对展示 | [DINOv2 · Fig. 1](https://arxiv.org/html/2304.07193v2#S1.F1) | [源文件](../assets/atlas/diagrams/source-feature-pairs.drawio) · [SVG](../assets/atlas/previews/source-feature-pairs.svg) | 每组样例紧邻放置输入和特征图。横向比较时保持投影或归一化方案可解释。 |
| 共享提示与多种有效输出 | [Segment Anything · Fig. 3](https://arxiv.org/html/2304.02643v1#S2.F3) | [源文件](../assets/atlas/diagrams/ambiguity-alternatives.drawio) · [SVG](../assets/atlas/previews/ambiguity-alternatives.svg) | 单独展示共同输入和提示，候选图保持相同视角。正文说明多种结果为何都成立。 |
| 同图归因矩阵 | [OrthKD · Fig. 2](https://doi.org/10.24963/ijcai.2026/774) | [源文件](../assets/atlas/diagrams/attribution-comparison.drawio) · [SVG](../assets/atlas/previews/attribution-comparison.svg) | 每行复用同一输入，列按模型排齐。图注交代归因方法、目标类别、颜色范围及可比性。 |
| 图像证据下接两行指标 | [DreamBooth · Fig. 11](https://arxiv.org/html/2208.12242v2#Sx4.F11) | [源文件](../assets/atlas/diagrams/images-with-metric-rows.drawio) · [SVG](../assets/atlas/previews/images-with-metric-rows.svg) | 图像和量化指标同列对齐。展示度量有分歧的实例时，同时列出两个指标。 |

## 定量与消融

| 选用场景 | 论文原图 | 编辑与预览 | 借鉴点 |
| --- | --- | --- | --- |
| 算力预算与最优包络 | [Chinchilla · Fig. 2](https://arxiv.org/html/2203.15556v1#S3.F2) | [源文件](../scripts/render-atlas-plot.py)（`compute-envelope`） · [SVG](../assets/atlas/previews/compute-envelope.svg) | 用一面板展示原始运行，另一面板展示共同预算区间内的下包络。标注横轴单位及插值定义。 |
| 共享刻度的训练曲线 | [DiT · Fig. 13](https://arxiv.org/html/2212.09748v2#A1.F13) | [源文件](../scripts/render-atlas-plot.py)（`training-small-multiples`） · [SVG](../assets/atlas/previews/training-small-multiples.svg) | 将训练配置拆为子图，颜色和线型代表相同角色。共享坐标方便比较趋势和收敛速度。 |
| 并排机制热图 | [Progress Measures for Grokking · Fig. 4](https://arxiv.org/html/2301.05217v3#S4.F4) | [源文件](../scripts/render-atlas-plot.py)（`mechanism-heatmaps`） · [SVG](../assets/atlas/previews/mechanism-heatmaps.svg) | 同一坐标系统各面板可排齐。量纲不同各用独立色条，量纲相同才考虑共享色域。 |
| 分布变化下的配对比较 | [CLIP · Fig. 13](https://arxiv.org/html/2103.00020v1#S3.F13) | [源文件](../scripts/render-atlas-plot.py)（`paired-shift-scores`） · [SVG](../assets/atlas/previews/paired-shift-scores.svg) | 把相同数据域的两个方法配成一行。连接两点后显示原单位差值，避免仅看单项绝对分。 |
| 时间响应与真值区间 | [OV-OrthKD · Fig. 3](https://arxiv.org/abs/2609.23376) | [源文件](../scripts/render-atlas-plot.py)（`temporal-evidence`） · [SVG](../assets/atlas/previews/temporal-evidence.svg) | 小图共用时间和分数刻度。用真实标注区间做背景，曲线与原始视频按同一时间戳对齐。 |

## 增补与更新

新增条目时记录论文版本、图号、直接来源、借鉴点、模板源和实际预览。优先补充当前没有的证据结构。更新模板时重新导出同名预览，在图谱和本地索引中补齐条目，并检查旧链接仍可打开。
