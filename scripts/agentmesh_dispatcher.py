#!/usr/bin/env python3
"""AgentMesh runtime dispatcher.

Given a task JSON (docs/task-schema.json), suggests which runtime should execute next
and prints a canonical dispatch payload.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

IMPLEMENTATION_ROLES = {
    "backend-engineer",
    "frontend-engineer",
    "fullstack-developer",
    "platform-engineer",
}
PLANNING_ROLES = {
    "engineering-manager",
    "product-manager",
    "tech-lead",
    "cloud-architect",
}
QA_ROLES = {"qa-automation", "senior-qa"}


def choose_runtime(task: dict) -> str:
    owner = task.get("owner_role", "")
    status = task.get("status", "")

    if status in {"new", "planned"} or owner in PLANNING_ROLES:
        return "claude-code"
    if status in {"ready_for_qa"} or owner in QA_ROLES:
        return "codex"
    if owner in IMPLEMENTATION_ROLES or status == "in_progress":
        return "codex"
    return "claude-code"


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python scripts/agentmesh_dispatcher.py <task.json>")
        return 2

    task_file = Path(sys.argv[1])
    task = json.loads(task_file.read_text())
    runtime = choose_runtime(task)

    result = {
        "task_id": task.get("task_id"),
        "runtime": runtime,
        "owner_role": task.get("owner_role"),
        "status": task.get("status"),
        "next_action": "sync status to GitHub using gh after execution",
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
