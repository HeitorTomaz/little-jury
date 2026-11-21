#!/usr/bin/env bash
# Assembles a panel with the fictional game inputs in the current folder, with the skill's current method.
set -eu
HERE="$(dirname "$0")"
cp -R "$HERE/files/." .
PY="$(command -v python3 || command -v python)"
"$PY" "$HERE/../../scripts/assemble_panel.py" .
