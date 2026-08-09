#!/usr/bin/env bash
set -euo pipefail

run_if_script_exists() {
  local manager="$1"
  local script="$2"
  if node -e "const p=require('./package.json'); process.exit(p.scripts&&p.scripts['$script']?0:1)" 2>/dev/null; then
    echo "==> $manager $script"
    "$manager" run "$script"
  fi
}

if [[ -f package.json ]]; then
  manager=npm
  [[ -f pnpm-lock.yaml ]] && manager=pnpm
  [[ -f yarn.lock ]] && manager=yarn

  for script in lint typecheck test build; do
    run_if_script_exists "$manager" "$script"
  done
else
  echo "No package.json detected. Run the repository's native validation commands instead."
fi
