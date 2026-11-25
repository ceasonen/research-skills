# 数据图模板

脚本路径为 `scripts/render-atlas-plot.py`。使用 Python 3、Matplotlib 3.7 或更新版本，以及 NumPy。示例库中的 SVG 使用演示数据，并在图上标注 “Illustrative data”。

```sh
python scripts/render-atlas-plot.py --template compute-envelope --demo --out preview.svg
python scripts/render-atlas-plot.py --template temporal-evidence --data scores.csv \
  --events intervals.csv --x-label 'Time (s)' --y-label 'Score' --out paper-figure.pdf
```

CSV 为 UTF-8，首行使用以下列名。每条曲线在各面板内至少需要两个不同的横轴值。脚本按第一条记录出现的顺序分组，重复的横轴样本先在项目分析代码中明确处理。

| 模板 | 必需列 | 复用时注意 |
| --- | --- | --- |
| `compute-envelope` | `budget,loss,series` | 预算必须为正。下包络只在所有模型均覆盖的区间内计算，按对数预算插值。用相同损失和预算口径。 |
| `training-small-multiples` | `panel,series,step,value` | 共享坐标与线型。每个面板使用相同的横纵轴单位。多随机种子可先汇总并在论文中注明汇总方式。 |
| `mechanism-heatmaps` | `panel,row,column,value` | 每个面板须为完整的数值网格。默认用独立色条。量纲一致、且比较绝对值时使用 `--shared-range`。 |
| `paired-shift-scores` | `group,baseline,comparison` | 每个对比分组一行。右列显示 comparison 减 baseline 的原单位差值。组名与分数定义应跨方法一致。 |
| `temporal-evidence` | `panel,series,time,score`；另用 `--events` 传入 `panel,start,end` | 同一面板的时间戳与标注必须对齐。面板共享时间、分数刻度。图下注明标注窗口和曲线的含义。 |

支持输出 PDF、SVG、PNG。出版前按论文实际插入宽度核对字与轴，检查颜色外的区分线索。保留真实 CSV、预处理代码和出图命令。显著性、置信区间与误差条由实际统计分析决定。

返回 [论文图谱](figure-atlas.md)。
