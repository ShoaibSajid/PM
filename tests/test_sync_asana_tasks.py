import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "sync_asana_tasks.py"
spec = importlib.util.spec_from_file_location("sync_asana_tasks", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(module)


class SyncAsanaTasksTests(unittest.TestCase):
    def test_excludes_completed_tasks_from_section_tables(self):
        projects = [{"gid": "1", "name": "Screw Driver"}]
        tasks = [
            {
                "gid": "t1",
                "name": "Pending task",
                "completed": False,
                "assignee": {"name": "A"},
                "due_on": "2026-02-19",
                "projects": [{"gid": "1", "name": "Screw Driver"}],
                "permalink_url": "https://example.com/pending",
                "project_gid": "1",
            },
            {
                "gid": "t2",
                "name": "Completed task",
                "completed": True,
                "assignee": {"name": "B"},
                "due_on": "2026-02-18",
                "projects": [{"gid": "1", "name": "Screw Driver"}],
                "permalink_url": "https://example.com/completed",
                "project_gid": "1",
            },
        ]

        rendered = module.format_tasks_md(projects, tasks)

        self.assertIn("Pending task", rendered)
        self.assertNotIn("Completed task", rendered)
        self.assertNotIn("| Completed |", rendered)


if __name__ == "__main__":
    unittest.main()
