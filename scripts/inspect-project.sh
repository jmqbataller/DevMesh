#!/usr/bin/env bash
set -euo pipefail

printf '== DevMesh: project inspection ==\n'
printf '\n-- location --\n'
pwd

if command -v git >/dev/null 2>&1 && git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  printf '\n-- git status --\n'
  git status -sb
  printf '\n-- branch --\n'
  git branch --show-current || true
  printf '\n-- remotes --\n'
  git remote -v || true
fi

printf '\n-- common project files --\n'
for f in AGENTS.md README.md package.json pnpm-lock.yaml yarn.lock package-lock.json pyproject.toml requirements.txt composer.json go.mod Cargo.toml vercel.json; do
  [[ -e "$f" ]] && printf '%s\n' "$f"
done

exit 0
