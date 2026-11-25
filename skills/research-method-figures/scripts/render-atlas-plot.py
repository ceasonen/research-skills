#!/usr/bin/env python3
"""Render a figure-atlas plot from a CSV, or preview with labelled demo data."""

import argparse
import csv
from collections import defaultdict
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

INK = "#23364c"
PALETTE = ["#276f9b", "#b16743", "#3c8778", "#8169a5", "#8b8340"]
STYLES = ["-", "--", "-.", ":", "-"]
CONFIG = {
    "compute-envelope": ("budget,loss,series", "Compute budget", "Validation loss"),
    "training-small-multiples": ("panel,series,step,value", "Training step", "Validation loss"),
    "mechanism-heatmaps": ("panel,row,column,value", "Input coordinate", "Output coordinate"),
    "paired-shift-scores": ("group,baseline,comparison", "Score", ""),
    "temporal-evidence": ("panel,series,time,score", "Time (s)", "Model score"),
}

plt.rcParams.update({
    "figure.facecolor": "white", "figure.dpi": 140,
    "font.family": "DejaVu Sans", "font.size": 9, "text.color": INK,
    "axes.labelcolor": INK, "axes.titlecolor": INK, "axes.titleweight": "semibold",
    "axes.edgecolor": "#b4c1ce", "axes.spines.right": False,
    "axes.spines.top": False, "xtick.color": INK, "ytick.color": INK,
    "axes.grid": True, "axes.axisbelow": True,
    "grid.color": "#e4eaf0", "grid.linewidth": 0.65,
    "legend.frameon": False, "pdf.fonttype": 42, "svg.fonttype": "none",
})


def read_csv(path, required):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        missing = set(required) - set(reader.fieldnames or [])
        if missing:
            raise ValueError("Missing CSV columns: " + ", ".join(sorted(missing)))
        rows = list(reader)
    if not rows or any(not (row.get(field) or "").strip() for field in required for row in rows):
        raise ValueError("The input needs at least one row and no blank required values.")
    return rows


def numeric(value):
    result = float(value)
    if not np.isfinite(result):
        raise ValueError(f"Expected finite number, got {value!r}.")
    return result


def group_by(rows, key):
    groups = defaultdict(list)
    for row in rows:
        groups[row[key]].append(row)
    return groups


def series_xy(rows, xkey, ykey):
    pair = np.array(sorted((numeric(row[xkey]), numeric(row[ykey])) for row in rows))
    if len(pair) < 2 or np.any(np.diff(pair[:, 0]) <= 0):
        raise ValueError(f"Each series needs at least two distinct {xkey} values.")
    return pair[:, 0], pair[:, 1]


def styles(rows):
    return {
        key: {"color": PALETTE[i % len(PALETTE)], "linestyle": STYLES[i % len(STYLES)]}
        for i, key in enumerate(group_by(rows, "series"))
    }


def series_legend(fig, palette, extra=()):
    handles = [Line2D([], [], label=name, **style) for name, style in palette.items()]
    handles.extend(extra)
    fig.legend(handles=handles, ncols=min(4, len(handles)), loc="outside upper center")


def compute_envelope(rows, args):
    palette = styles(rows)
    curves = {
        name: series_xy(group, "budget", "loss")
        for name, group in group_by(rows, "series").items()
    }
    if len(curves) < 2 or any(np.any(x <= 0) for x, _ in curves.values()):
        raise ValueError("Envelope needs at least two series and positive compute budgets.")
    lo = max(x[0] for x, _ in curves.values())
    hi = min(x[-1] for x, _ in curves.values())
    if lo >= hi:
        raise ValueError("Series have no shared compute range for the envelope.")
    grid = np.geomspace(lo, hi, 150)
    best = np.min([np.interp(np.log(grid), np.log(x), y) for x, y in curves.values()], axis=0)
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.2), layout="constrained", sharey=True)
    for name, (x, y) in curves.items():
        axes[0].plot(x, y, marker="o", markersize=3, label=name, **palette[name])
        axes[1].plot(x, y, alpha=0.24, **palette[name])
    axes[1].plot(grid, best, color=INK, lw=2.3, label="Lower envelope")
    axes[1].legend(loc="upper right")
    for ax, title in zip(axes, ["(a) Observed runs", "(b) Shared-budget envelope"]):
        ax.set(xscale="log", xlabel=args.x_label)
        ax.set_title(title, loc="left")
    axes[0].set_ylabel(args.y_label)
    series_legend(fig, palette)
    return fig


def small_multiples(rows, args):
    panels = group_by(rows, "panel")
    palette = styles(rows)
    cols = min(2, len(panels))
    nrows = (len(panels) + cols - 1) // cols
    fig, axes = plt.subplots(nrows, cols, figsize=(8.4, 2.35 * nrows + .6),
                             layout="constrained", sharex=True, sharey=True, squeeze=False)
    for ax, (panel, group) in zip(axes.flat, panels.items()):
        for name, items in group_by(group, "series").items():
            ax.plot(*series_xy(items, "step", "value"), **palette[name], lw=1.55)
        ax.set_title(panel, loc="left")
        ax.label_outer()
    for ax in list(axes.flat)[len(panels):]:
        ax.set_visible(False)
    fig.supxlabel(args.x_label)
    fig.supylabel(args.y_label)
    series_legend(fig, palette)
    return fig


def heatmaps(rows, args):
    matrices = {}
    for panel, group in group_by(rows, "panel").items():
        xs = sorted({numeric(row["column"]) for row in group})
        ys = sorted({numeric(row["row"]) for row in group})
        items = {(numeric(row["row"]), numeric(row["column"])): numeric(row["value"]) for row in group}
        if len(xs) < 2 or len(ys) < 2 or len(items) != len(group) or len(items) != len(xs) * len(ys):
            raise ValueError(f"Heatmap {panel!r} does not have one value per grid position.")
        matrices[panel] = (xs, ys, np.array([[items[y, x] for x in xs] for y in ys]))
    if args.shared_range:
        vmin = min(z.min() for _, _, z in matrices.values())
        vmax = max(z.max() for _, _, z in matrices.values())
    else:
        vmin = vmax = None
    cols = min(3, len(matrices))
    nrows = (len(matrices) + cols - 1) // cols
    fig, axes = plt.subplots(nrows, cols, figsize=(3.1 * cols, 3.35 * nrows),
                             layout="constrained", squeeze=False)
    for ax, (panel, (xs, ys, z)) in zip(axes.flat, matrices.items()):
        ax.grid(False)
        mesh = ax.pcolormesh(xs, ys, z, shading="nearest", cmap="cividis",
                            vmin=vmin, vmax=vmax)
        ax.set(title=panel, xlabel=args.x_label, ylabel=args.y_label, aspect="equal")
        fig.colorbar(mesh, ax=ax, orientation="horizontal", shrink=.83)
    for ax in list(axes.flat)[len(matrices):]:
        ax.set_visible(False)
    return fig


def paired_scores(rows, args):
    names = [row["group"] for row in rows]
    if len(set(names)) != len(rows):
        raise ValueError("Each group must appear exactly once.")
    a = np.array([numeric(row["baseline"]) for row in rows])
    b = np.array([numeric(row["comparison"]) for row in rows])
    y = np.arange(len(names))
    fig, ax = plt.subplots(figsize=(7.3, 1.8 + len(y) * .43), layout="constrained")
    ax.grid(axis="x")
    ax.yaxis.grid(False)
    ax.hlines(y, np.minimum(a, b), np.maximum(a, b), color="#b7c5d2", linewidth=2.3)
    ax.scatter(a, y, s=62, facecolors="white", edgecolors=PALETTE[0], linewidths=1.5,
               marker="o", label="Baseline")
    ax.scatter(b, y, s=26, color=PALETTE[1], marker="D", label="Comparison")
    ax.set(yticks=y, yticklabels=names, xlabel=args.x_label)
    ax.invert_yaxis()
    for i, delta in enumerate(b-a):
        ax.text(1.025, i, f"{delta:+.2f}", transform=ax.get_yaxis_transform(),
                va="center", fontsize=8, color=INK)
    ax.text(1.025, 1.02, "Difference", transform=ax.transAxes, fontsize=8)
    fig.legend(*ax.get_legend_handles_labels(), loc="outside upper center", ncols=2)
    return fig


def temporal_evidence(rows, args, events):
    panels = group_by(rows, "panel")
    ranges = group_by(events, "panel")
    palette = styles(rows)
    if set(panels) != set(ranges):
        raise ValueError("The score CSV and event CSV must name the same panels.")
    fig, axes = plt.subplots(len(panels), 1, figsize=(8.3, 1.65 * len(panels) + 1.05),
                            sharex=True, sharey=True, layout="constrained", squeeze=False)
    for (ax,), (name, group) in zip(axes, panels.items()):
        for event in ranges[name]:
            start, end = numeric(event["start"]), numeric(event["end"])
            if start >= end:
                raise ValueError(f"{name!r} has an interval with start ≥ end.")
            ax.axvspan(start, end, color="#d9ede4", zorder=0)
        for method, items in group_by(group, "series").items():
            ax.plot(*series_xy(items, "time", "score"), **palette[method], lw=1.55)
        ax.set_title(name, loc="left")
    fig.supxlabel(args.x_label)
    fig.supylabel(args.y_label)
    series_legend(fig, palette, [Patch(facecolor="#d9ede4", label="Annotated interval")])
    return fig


def demo_data(template):
    if template == "compute-envelope":
        return [
            dict(series=f"Model {chr(65+j)}", budget=x,
                 loss=1.12 + .16*j + (3.2-.51*j) * (x*9e-16)**(-.3-.05*j))
            for j in range(4) for x in np.geomspace(1e15*(1+j/5), 1e19*(1+j/8), 18)
        ], None
    if template == "training-small-multiples":
        return [
            dict(panel=f"({chr(97+j)}) Setting {j+1}", series=f"Run {i+1}", step=t,
                 value=1.03 + .22*i + .07*j + (2.6-.16*i) / (1+t/(12+j*5)) + .025*np.sin(t/3+i))
            for j in range(4) for i in range(3) for t in range(0, 131, 2)
        ], None
    if template == "mechanism-heatmaps":
        return [
            dict(panel=name, column=x, row=y, value=f(x, y))
            for name, f in [
                ("(a) Interaction", lambda x,y: np.cos((x-y)/2) + .3*np.sin(x*.85)),
                ("(b) Activation", lambda x,y: np.sin(x*.5+y*.65)**2),
                ("(c) Spectral view", lambda x,y: np.exp(-((x-10)**2+(y-13)**2)/6)+.5*np.exp(-((x-15)**2+(y-5)**2)/7)),
            ] for x in range(1, 20) for y in range(1, 20)
        ], None
    if template == "paired-shift-scores":
        return [
            dict(group=f"Domain {chr(65+i)}", baseline=a, comparison=b)
            for i, (a,b) in enumerate([(81,81),(62,68),(57,71),(38,59),(42,52)])
        ], None
    intervals = [("Case A",1.4,3.3),("Case B",2.2,4.5),("Case C",.8,2.3)]
    rows = [
        dict(panel=name, series=key, time=t,
             score=.15+.66*np.exp(-.5*((t-(start+end)/2-shift)/spread)**2)+.035*np.sin(t*5))
        for name,start,end in intervals
        for key,shift,spread in [("Baseline",.47,.92),("Alternative",0.,.56)]
        for t in np.linspace(0,6,40)
    ]
    return rows, [dict(panel=name,start=start,end=end) for name,start,end in intervals]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template", required=True, choices=CONFIG)
    inputs = parser.add_mutually_exclusive_group(required=True)
    inputs.add_argument("--data", type=Path, help="CSV with real input values.")
    inputs.add_argument("--demo", action="store_true", help="Draw labelled illustrative data.")
    parser.add_argument("--events", type=Path, help="Event CSV for temporal-evidence.")
    parser.add_argument("--x-label")
    parser.add_argument("--y-label")
    parser.add_argument("--shared-range", action="store_true", help="Use for heatmap panels with the same units.")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.suffix.lower() not in {".pdf", ".svg", ".png"}:
        parser.error("Output must end in .pdf, .svg or .png.")
    schema, xlabel, ylabel = CONFIG[args.template]
    args.x_label = args.x_label or xlabel
    args.y_label = args.y_label or ylabel
    try:
        if args.demo:
            rows, events = demo_data(args.template)
        else:
            rows = read_csv(args.data, schema.split(","))
            events = None
            if args.template == "temporal-evidence":
                if args.events is None:
                    raise ValueError("Temporal evidence needs --events with panel,start,end.")
                events = read_csv(args.events, ["panel", "start", "end"])
        render = {
            "compute-envelope": compute_envelope,
            "training-small-multiples": small_multiples,
            "mechanism-heatmaps": heatmaps,
            "paired-shift-scores": paired_scores,
        }
        fig = temporal_evidence(rows, args, events) if args.template == "temporal-evidence" else \
            render[args.template](rows, args)
        if args.demo:
            fig.get_layout_engine().set(rect=(0, .05, 1, .95))
            fig.text(.99, .012, "Illustrative data", color="#52637b", ha="right", fontsize=7)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(args.out, bbox_inches="tight", pad_inches=.09, dpi=300)
        plt.close(fig)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
