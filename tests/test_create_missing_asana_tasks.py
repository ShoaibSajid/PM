import importlib.util
from pathlib import Path
import sys


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "create_missing_asana_tasks.py"
spec = importlib.util.spec_from_file_location("create_missing_asana_tasks", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
sys.modules[spec.name] = module
spec.loader.exec_module(module)


SAMPLE = """## Consolidated Missing Tasks (Deduplicated)

## 1) Screw Driver

- Resolve screw fastening quality issues in one grouped effort:
  angle issue (bit coming out of screw head), insufficient depth.
  Owners: Hieu, Ammad, Vision team

## 2) PCB

- Install new vertical sensor and complete the required L-shape bracket workflow.
  Owners: PCB hardware + Mechanical team
"""


def test_parse_consolidated_missing_tasks_extracts_tasks():
    tasks = module.parse_missing_tasks_markdown(SAMPLE)

    assert len(tasks) == 2
    assert tasks[0].section == "Screw Driver"
    assert "angle issue" in tasks[0].description
    assert tasks[0].owners == "Hieu, Ammad, Vision team"


def test_build_task_name_includes_review_prefix_and_section():
    task = module.MissingTask(
        section="Rubber Foot",
        description="Resolve wrinkling and pickup stability issues.",
        owners="Robot + Vision teams",
    )

    name = module.build_task_name(task)

    assert name.startswith("[Missing Review][Rubber Foot] ")
    assert "Resolve wrinkling" in name


def test_plan_creations_skips_existing_names_case_insensitive():
    tasks = [
        module.MissingTask(
            section="PCB",
            description="Install new vertical sensor and complete bracket workflow.",
            owners="PCB hardware team",
        ),
        module.MissingTask(
            section="GUI / Software / Framework",
            description="Complete grouped GUI robustness package.",
            owners="Jalol",
        ),
    ]
    existing_names = {
        "[missing review][pcb] install new vertical sensor and complete bracket workflow"
    }

    planned = module.plan_creations(tasks, existing_names)

    assert len(planned) == 1
    assert planned[0].task.section == "GUI / Software / Framework"
