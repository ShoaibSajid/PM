#!/usr/bin/env python3
"""Create review tasks in Asana from TASKS_MISSING_IN_ASANA_RAW_REVIEW.md.

Usage:
  ASANA_PAT=... python3 scripts/create_missing_asana_tasks.py --dry-run
  ASANA_PAT=... python3 scripts/create_missing_asana_tasks.py
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any


ASANA_API = "https://app.asana.com/api/1.0"
DEFAULT_PROJECT_GID = "1213338742027940"
DEFAULT_INPUT_PATH = "TASKS_MISSING_IN_ASANA_RAW_REVIEW.md"


@dataclass
class MissingTask:
    section: str
    description: str
    owners: str


@dataclass
class PlannedCreation:
    task: MissingTask
    name: str


class AsanaClient:
    def __init__(self, token: str) -> None:
        self.token = token

    def _request(self, method: str, path: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        url = f"{ASANA_API}{path}"
        body = None
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
        }
        if payload is not None:
            body = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json"

        req = urllib.request.Request(url, data=body, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            details = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Asana API error {exc.code} for {url}: {details}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(f"Network error for {url}: {exc}") from exc

    def get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        query = f"?{urllib.parse.urlencode(params or {}, doseq=True)}" if params else ""
        return self._request("GET", f"{path}{query}")

    def post(self, path: str, payload: dict[str, Any]) -> dict[str, Any]:
        return self._request("POST", path, payload)

    def paginate(self, path: str, params: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        params = dict(params or {})
        items: list[dict[str, Any]] = []
        offset = None
        while True:
            if offset:
                params["offset"] = offset
            data = self.get(path, params)
            items.extend(data.get("data", []))
            next_page = data.get("next_page")
            if not next_page or not next_page.get("offset"):
                break
            offset = next_page["offset"]
        return items


def parse_missing_tasks_markdown(text: str) -> list[MissingTask]:
    in_consolidated = False
    current_section = ""
    tasks: list[MissingTask] = []

    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]

        if line.strip() == "## Consolidated Missing Tasks (Deduplicated)":
            in_consolidated = True
            i += 1
            continue

        if in_consolidated and line.startswith("## ") and not re.match(r"## \d+\) ", line):
            break

        section_match = re.match(r"## \d+\)\s+(.+)$", line.strip())
        if in_consolidated and section_match:
            current_section = section_match.group(1).strip()
            i += 1
            continue

        if in_consolidated and current_section and line.startswith("- "):
            desc_parts = [line[2:].strip()]
            owners = ""
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if nxt.startswith("## ") or nxt.startswith("- "):
                    break
                if nxt.strip().startswith("Owners:"):
                    owners = nxt.strip().split("Owners:", 1)[1].strip()
                elif nxt.strip():
                    desc_parts.append(nxt.strip())
                i += 1

            description = " ".join(desc_parts).strip()
            if description and owners:
                tasks.append(MissingTask(section=current_section, description=description, owners=owners))
            continue

        i += 1

    return tasks


def build_task_name(task: MissingTask) -> str:
    description = task.description.rstrip(".").strip()
    name = f"[Missing Review][{task.section}] {description}"
    return name[:250]


def build_task_notes(task: MissingTask, source_file: str) -> str:
    return "\n".join(
        [
            "Created automatically for review from missing-task tracker.",
            "",
            f"Source: {source_file}",
            f"Section: {task.section}",
            f"Suggested owners: {task.owners}",
            "",
            "Review flow:",
            "1) Reassign to responsible person, or",
            "2) Mark complete if no longer required.",
        ]
    )


def normalize_name(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip()).lower()


def plan_creations(tasks: list[MissingTask], existing_names: set[str]) -> list[PlannedCreation]:
    planned: list[PlannedCreation] = []
    seen = set(existing_names)
    for task in tasks:
        name = build_task_name(task)
        normalized = normalize_name(name)
        if normalized in seen:
            continue
        seen.add(normalized)
        planned.append(PlannedCreation(task=task, name=name))
    return planned


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create Asana tasks from missing-task markdown.")
    parser.add_argument("--input", default=DEFAULT_INPUT_PATH, help="Input markdown file path.")
    parser.add_argument(
        "--project-gid",
        default=DEFAULT_PROJECT_GID,
        help=f"Asana project GID (default: {DEFAULT_PROJECT_GID}).",
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview tasks without creating them.")
    parser.add_argument("--limit", type=int, default=0, help="Optional max number of tasks to create.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    token = os.getenv("ASANA_PAT")
    if not token:
        print("Error: ASANA_PAT is required.", file=sys.stderr)
        return 1

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        return 1

    text = input_path.read_text(encoding="utf-8")
    tasks = parse_missing_tasks_markdown(text)

    client = AsanaClient(token)
    existing = client.paginate(
        f"/projects/{args.project_gid}/tasks",
        {
            "completed_since": "1970-01-01T00:00:00.000Z",
            "limit": 100,
            "opt_fields": "name",
        },
    )
    existing_names = {normalize_name((t.get("name") or "")) for t in existing if t.get("name")}

    planned = plan_creations(tasks, existing_names)
    if args.limit > 0:
        planned = planned[: args.limit]

    if not planned:
        print("No new tasks to create (all already exist or none parsed).")
        return 0

    print(f"Parsed tasks: {len(tasks)}")
    print(f"Existing project tasks checked: {len(existing)}")
    print(f"New tasks to create: {len(planned)}")

    if args.dry_run:
        for item in planned:
            print(f"DRY RUN: {item.name}")
        return 0

    created = 0
    source_file = str(input_path)
    for item in planned:
        payload = {
            "data": {
                "name": item.name,
                "notes": build_task_notes(item.task, source_file),
                "projects": [args.project_gid],
                "assignee": "me",
            }
        }
        client.post("/tasks", payload)
        created += 1
        print(f"Created: {item.name}")

    print(f"Done. Created {created} task(s) in project {args.project_gid}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
