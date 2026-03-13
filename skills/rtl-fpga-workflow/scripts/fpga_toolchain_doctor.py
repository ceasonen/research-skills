#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
from dataclasses import asdict, dataclass


TOOLS = [
    ("iverilog", "Icarus Verilog compiler and simulator"),
    ("verilator", "Verilog/SystemVerilog lint and simulation compiler"),
    ("yosys", "Synthesis and netlist inspection"),
    ("sby", "SymbiYosys formal driver"),
    ("nextpnr-ice40", "Place and route for Lattice iCE40"),
    ("nextpnr-ecp5", "Place and route for Lattice ECP5"),
    ("icepack", "iCE40 bitstream packing"),
    ("iceprog", "iCE40 programming"),
    ("openFPGALoader", "Board and cable programmer"),
    ("gtkwave", "Waveform viewer"),
]


@dataclass
class ToolStatus:
    name: str
    description: str
    found: bool
    path: str | None


def detect_tools() -> list[ToolStatus]:
    return [
        ToolStatus(name=name, description=desc, found=bool(shutil.which(name)), path=shutil.which(name))
        for name, desc in TOOLS
    ]


def install_hint(statuses: list[ToolStatus]) -> list[str]:
    names = {item.name for item in statuses if item.found}
    hints: list[str] = []
    if {"iverilog", "verilator", "yosys"} <= names:
        hints.append("Core open-source RTL flow is present.")
    else:
        hints.append("Preferred install path on macOS: OSS CAD Suite from YosysHQ.")
        hints.append("Fallback path: Homebrew formulae for at least icarus-verilog, verilator, yosys, and gtkwave.")
    if "openFPGALoader" not in names:
        hints.append("Programming hardware will need openFPGALoader or a vendor-specific cable tool.")
    if not any(name.startswith("nextpnr") for name in names):
        hints.append("Bitstream place-and-route tools are still missing for open FPGA flows.")
    return hints


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect local FPGA and RTL tool availability.")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of text.")
    args = parser.parse_args()

    statuses = detect_tools()
    payload = {
        "cwd": os.getcwd(),
        "tools": [asdict(item) for item in statuses],
        "hints": install_hint(statuses),
    }

    if args.json:
        print(json.dumps(payload, indent=2))
        return 0

    for item in statuses:
        state = "FOUND" if item.found else "MISSING"
        path = item.path or "-"
        print(f"{item.name:16} {state:7} {path}")
    print()
    for hint in payload["hints"]:
        print(f"- {hint}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
