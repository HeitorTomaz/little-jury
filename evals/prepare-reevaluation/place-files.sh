#!/usr/bin/env bash
# Project root with a revised concept (v0.2) and a panel/ that already holds a completed v0.1 run.
set -eu
HERE="$(dirname "$0")"
cp -R "$HERE/files/." .
PY="$(command -v python3 || command -v python)"
"$PY" "$HERE/../../scripts/assemble_panel.py" panel
cp -R "$HERE/../run-game-no-stops/files/." panel/
mkdir -p panel/rounds/v0.1/inputs-used
cp -R "$HERE/../run-game-no-stops/files/input" panel/rounds/v0.1/inputs-used/
cp "$HERE/../run-game-no-stops/files/personas.md" "$HERE/../run-game-no-stops/files/config.md" panel/rounds/v0.1/inputs-used/
