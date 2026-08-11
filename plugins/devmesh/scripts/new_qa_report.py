#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path

TEMPLATE = """# DevMesh QA Report

## Scope

- Task: {task}
- Branch/commit/working-tree context:
- Routes/features reviewed:
- Environment:

## Verification Matrix

| Gate | Status | Evidence |
|---|---|---|
| Build | NOT RUN | |
| Lint / typecheck | NOT RUN | |
| Unit / integration tests | NOT RUN | |
| Regression tests | NOT RUN | |
| Browser QA | NOT RUN | |
| Desktop layout | NOT RUN | |
| Mobile layout | NOT RUN | |
| Console/runtime | NOT RUN | |
| Accessibility | NOT RUN | |
| Security | NOT RUN | |
| Performance | NOT RUN | |
| Code review | NOT RUN | |

Allowed statuses: `PASS`, `FAIL`, `FIXED`, `BLOCKED`, `NOT RUN`.

## Findings and Fixes

## Browser Evidence

- Launch command:
- URL:
- Browser engine:
- Viewports:
- Interactions:
- Console/network notes:

## Artifacts

- Screenshots:
- Traces/logs:
- Test outputs:

## Limitations

## Final Result

- Defects found:
- Defects fixed:
- Remaining blockers:
"""


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value[:48] or "task"


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a DevMesh QA report directory in an opted-in project.")
    parser.add_argument("task", help="Short task/report name")
    parser.add_argument("--path", default=".", help="Target project directory")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    memory = root / ".devmesh"
    if not memory.exists():
        raise SystemExit(".devmesh/ does not exist. Initialize/opt into project memory first.")

    stamp = datetime.now().strftime("%Y-%m-%d-%H%M")
    report_dir = memory / "reports" / f"{stamp}-{slugify(args.task)}"
    report_dir.mkdir(parents=True, exist_ok=False)
    (report_dir / "screenshots").mkdir()
    (report_dir / "artifacts").mkdir()
    (report_dir / "report.md").write_text(TEMPLATE.format(task=args.task), encoding="utf-8")

    print(report_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
