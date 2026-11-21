#!/usr/bin/env bash
# Project root with the concept document and a panel already assembled in panel/.
set -eu
HERE="$(dirname "$0")"
cp -R "$HERE/files/." .
mkdir -p panel
cp -R "$HERE/../run-game-no-stops/files/." panel/
PY="$(command -v python3 || command -v python)"
"$PY" "$HERE/../../scripts/assemble_panel.py" panel
