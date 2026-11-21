#!/usr/bin/env bash
set -eu
cp -R "$(dirname "$0")/files/." .
git init -q
git -c user.email=t@t -c user.name=t add .
git -c user.email=t@t -c user.name=t commit -qm "version 1.4"
