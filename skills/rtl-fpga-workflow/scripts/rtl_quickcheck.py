#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def run(cmd: list[str]) -> tuple[int, str]:
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return proc.returncode, proc.stdout


def main() -> int:
    parser = argparse.ArgumentParser(description="Run lightweight RTL checks with any locally available tools.")
    parser.add_argument("files", nargs="+", help="Verilog or SystemVerilog source files")
    parser.add_argument("--top", help="Top module name for elaboration-oriented checks")
    args = parser.parse_args()

    files = [str(Path(p)) for p in args.files]
    overall_rc = 0

    if shutil.which("verilator"):
        cmd = ["verilator", "--lint-only", "-Wall", *files]
        rc, out = run(cmd)
        print("$ " + " ".join(cmd))
        print(out.rstrip())
        overall_rc = max(overall_rc, rc)
    else:
        print("verilator not found; skipping lint-only check")

    if shutil.which("iverilog"):
        with tempfile.TemporaryDirectory() as tmpdir:
            out_file = str(Path(tmpdir) / "a.out")
            cmd = ["iverilog", "-g2012", "-o", out_file]
            if args.top:
                cmd += ["-s", args.top]
            cmd += files
            rc, out = run(cmd)
            print("$ " + " ".join(cmd))
            print(out.rstrip())
            overall_rc = max(overall_rc, rc)
    else:
        print("iverilog not found; skipping compile check")

    if shutil.which("yosys") and args.top:
        script = f"read_verilog {' '.join(files)}; hierarchy -check -top {args.top}; proc; check"
        cmd = ["yosys", "-q", "-p", script]
        rc, out = run(cmd)
        print("$ " + " ".join(cmd))
        print(out.rstrip())
        overall_rc = max(overall_rc, rc)
    elif shutil.which("yosys"):
        print("yosys found, but --top was not provided; skipping hierarchy check")
    else:
        print("yosys not found; skipping synthesis sanity check")

    return overall_rc


if __name__ == "__main__":
    raise SystemExit(main())
