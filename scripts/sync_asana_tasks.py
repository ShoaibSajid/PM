#!/usr/bin/env python3
"""Sync Asana project tasks to a local markdown report.

Usage:
  ASANA_PAT=... ASANA_PROJECT_GID=... python3 scripts/sync_asana_tasks.py
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

ASANA_API = "https://app.asana.com/api/1.0"


class AsanaClient:
    def __init__(self, token: str) -> None:
        self.token = token

    def get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        query = f"?{urllib.parse.urlencode(params or {}, doseq=True)}" if params else ""
        url = f"{ASANA_API}{path}{query}"
        req = urllib.request.Request(
            url,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/json",
            },
            method="GET",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            payload = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Asana API error {exc.code} for {url}: {payload}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(f"Network error for {url}: {exc}") from exc

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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync Asana tasks into markdown.")
    parser.add_argument(
        "--project-gids",
        default=os.getenv("ASANA_PROJECT_GID", ""),
        help="Comma-separated Asana project GIDs. Defaults to ASANA_PROJECT_GID.",
    )
    parser.add_argument(
        "--output",
        default="ASANA_TASKS_LIST.md",
        help="Markdown output path.",
    )
    parser.add_argument(
        "--raw-output",
        default="ASANA_TASKS_RAW.json",
        help="Raw JSON output path for debugging/reporting.",
    )
    return parser.parse_args()


def normalize_due(task: dict[str, Any]) -> str:
    return task.get("due_on") or task.get("due_at") or "-"


def due_sort_key(task: dict[str, Any]) -> tuple[int, str]:
    due = normalize_due(task)
    if due == "-":
        return (1, "9999-99-99")
    return (0, due)


SECTION_ORDER = ["Screw Driver", "Rubber Foot", "PCB", "Mobile Printers"]


def infer_sections(task: dict[str, Any]) -> list[str]:
    labels = set()
    for project in task.get("projects", []):
        name = (project.get("name") or "").strip().lower()
        if "screw" in name:
            labels.add("Screw Driver")
        if "rubber" in name:
            labels.add("Rubber Foot")
        if name == "pcb":
            labels.add("PCB")
        if "mobile printer" in name or "mobile printers" in name:
            labels.add("Mobile Printers")
    return [section for section in SECTION_ORDER if section in labels]


def dedupe_tasks(tasks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_gid: dict[str, dict[str, Any]] = {}
    for task in tasks:
        gid = task.get("gid")
        if not gid:
            continue
        existing = by_gid.get(gid)
        if not existing:
            task["source_project_gids"] = {task.get("project_gid")}
            by_gid[gid] = task
            continue
        existing["source_project_gids"].add(task.get("project_gid"))
    deduped = list(by_gid.values())
    for task in deduped:
        task["source_project_gids"] = sorted(
            [gid for gid in task.get("source_project_gids", set()) if gid]
        )
    return deduped


def format_section_table(lines: list[str], title: str, tasks: list[dict[str, Any]]) -> None:
    lines.append(f"## {title}")
    lines.append("")
    lines.append(f"**Total Tasks:** {len(tasks)}")
    lines.append("")
    lines.append("| Task | Assignee | Due | URL |")
    lines.append("|---|---|---|---|")
    for task in sorted(tasks, key=due_sort_key):
        name = (task.get("name") or "").replace("|", "\\|")
        assignee = (task.get("assignee") or {}).get("name") or "Unassigned"
        url = task.get("permalink_url") or "-"
        lines.append(f"| {name} | {assignee} | {normalize_due(task)} | {url} |")
    lines.append("")


def format_tasks_md(projects: list[dict[str, Any]], tasks: list[dict[str, Any]]) -> str:
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    deduped_tasks = dedupe_tasks(tasks)
    pending = [t for t in deduped_tasks if not t.get("completed")]
    completed_count = len(deduped_tasks) - len(pending)

    section_buckets: dict[str, list[dict[str, Any]]] = {name: [] for name in SECTION_ORDER}
    unmapped_count = 0
    for task in pending:
        sections = infer_sections(task)
        if not sections:
            unmapped_count += 1
            continue
        for section in sections:
            section_buckets[section].append(task)

    lines: list[str] = []
    lines.append("# Asana Tasks List - Auto Synced")
    lines.append("")
    lines.append(f"**Last Synced:** {now}")
    lines.append(
        "**Projects:** " + ", ".join(p.get("name", p.get("gid", "unknown")) for p in projects)
    )
    lines.append(f"**Total Pending Tasks (deduplicated):** {len(pending)}")
    lines.append(f"**Completed Tasks Excluded:** {completed_count}")
    lines.append(f"**Unmapped Pending Tasks:** {unmapped_count}")
    lines.append("")

    for section_name in SECTION_ORDER:
        format_section_table(lines, section_name, section_buckets[section_name])

    lines.append("")
    lines.append("---")
    lines.append("Generated by `scripts/sync_asana_tasks.py`.")
    return "\n".join(lines)


def main() -> int:
    args = parse_args()

    token = os.getenv("ASANA_PAT")
    if not token:
        print("Error: ASANA_PAT is required.", file=sys.stderr)
        return 1

    project_gids = [gid.strip() for gid in args.project_gids.split(",") if gid.strip()]
    if not project_gids:
        print("Error: Provide --project-gids or set ASANA_PROJECT_GID.", file=sys.stderr)
        return 1

    client = AsanaClient(token)

    all_tasks: list[dict[str, Any]] = []
    projects: list[dict[str, Any]] = []

    for gid in project_gids:
        project_data = client.get(f"/projects/{gid}", {"opt_fields": "gid,name,permalink_url"})
        project = project_data.get("data", {})
        projects.append(project)

        tasks = client.paginate(
            f"/projects/{gid}/tasks",
            {
                "completed_since": "1970-01-01T00:00:00.000Z",
                "limit": 100,
                "opt_fields": (
                    "gid,name,completed,created_at,modified_at,due_on,due_at,"
                    "assignee.name,assignee.gid,memberships.section.name,"
                    "projects.gid,projects.name,"
                    "permalink_url"
                ),
            },
        )
        for task in tasks:
            task["project_gid"] = gid
            task["project_name"] = project.get("name")
        all_tasks.extend(tasks)

    markdown = format_tasks_md(projects, all_tasks)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(markdown)

    with open(args.raw_output, "w", encoding="utf-8") as f:
        json.dump(
            {
                "synced_at": dt.datetime.now().isoformat(),
                "projects": projects,
                "tasks": all_tasks,
            },
            f,
            indent=2,
        )

    print(f"Synced {len(all_tasks)} tasks across {len(projects)} project(s).")
    print(f"Markdown: {args.output}")
    print(f"Raw JSON: {args.raw_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
