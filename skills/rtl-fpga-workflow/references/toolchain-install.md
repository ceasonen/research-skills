# FPGA Toolchain Install Notes

Preferred path on macOS for an open-source flow:

1. OSS CAD Suite from YosysHQ

Typical install sequence outside a restricted sandbox:

1. Download the current `darwin-arm64` archive from the OSS CAD Suite releases page.
2. Extract it.
3. On macOS, clear quarantine on the downloaded archive if needed.
4. Add `<extract>/oss-cad-suite/bin` to `PATH` or source `<extract>/oss-cad-suite/environment`.

Typical tools included there:

1. `iverilog`
2. `verilator`
3. `yosys`
4. `sby`
5. `nextpnr-*`
6. `openFPGALoader`
7. `gtkwave`

Fallback path when a bundled suite is not available:

1. Install the minimum local review stack:
   - `brew install icarus-verilog`
   - `brew install verilator`
   - `brew install yosys`
2. For a waveform viewer:
   - `brew install --cask gtkwave` if the cask is still usable in your environment
   - otherwise prefer the waveform viewer bundled in OSS CAD Suite, or install `surfer`
2. Add board-specific or architecture-specific tools later:
   - `brew install openfpgaloader`
   - add `nextpnr-*` and architecture-specific packer tools through OSS CAD Suite when possible
   - vendor programmer tools

Before attempting installation on this machine:

1. Ensure Homebrew directories are writable by the current user.
2. Ensure the terminal can resolve external hosts such as GitHub.
3. Run `scripts/fpga_toolchain_doctor.py` after installation to confirm the commands are on `PATH`.
