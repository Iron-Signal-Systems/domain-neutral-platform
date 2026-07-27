#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

PHASE5_TAG = 'phase-5-production-database-security-boundary-complete-v1'
PHASE5_COMMIT = '9f8dbf9d909ef157df72b12511b165a689559093'
STEP7_COMMIT = '79e9723b2dd12e813de8a8c665d08d4f61cc8fab'
MODULE_IMPORT = '1e017c7ab874969395fb31e030c0149116bf77cf'
STATUS_START = '<!-- dnp-current-governed-status:start -->'
STATUS_END = '<!-- dnp-current-governed-status:end -->'
CURRENT_INDEXES = ['README.md', 'docs/README.md', 'docs/architecture/README.md', 'docs/architecture/backend-services/README.md', 'docs/architecture/foundation/README.md', 'go/README.md', 'go/platform/README.md', 'tools/validation/README.md', 'tools/validation/phase-gates/README.md']


class CheckFailure(RuntimeError):
    pass


def fail(message: str) -> None:
    raise CheckFailure(message)


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    data = json.loads((root / "docs/project-status.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        fail("project status schema_version must be 1")
    project = data.get("project", {})
    if project.get("name") != "DNP" or project.get("production_ready") is not False:
        fail("project identity or production-readiness status drifted")
    database = data.get("accepted_database_boundary", {})
    if database.get("tag") != PHASE5_TAG or database.get("revision") != PHASE5_COMMIT:
        fail("accepted Phase 5 identity drifted")
    go_boundary = data.get("accepted_go_boundary", {})
    if go_boundary.get("step") != 7 or go_boundary.get("revision") != STEP7_COMMIT:
        fail("accepted Phase 6 Step 7 identity drifted")
    for key in ("static_validation", "complete_validation"):
        result = go_boundary.get(key, {})
        if result.get("pass") != 142 or result.get("fail") != 0:
            fail(f"accepted Step 7 {key} result drifted")
    candidate = data.get("active_candidate", {})
    if candidate.get("step") != 8 or candidate.get("status") != "rebaseline_required":
        fail("Phase 6 Step 8 must be marked rebaseline_required")
    if candidate.get("acceptance_claimed") is not False:
        fail("Phase 6 Step 8 must not claim acceptance")
    if candidate.get("gate_runnable_against_current_dev") is not False:
        fail("historical Step 8 gate must not be presented as current")
    if candidate.get("accepted_predecessor") != STEP7_COMMIT:
        fail("Step 8 rebaseline record lost the accepted Step 7 predecessor")
    boundary = data.get("repository_boundary", {})
    if boundary.get("module_import_revision") != MODULE_IMPORT:
        fail("Module Families import revision drifted")
    if boundary.get("local_modules_allowed") is not False:
        fail("DNP must prohibit a local modules tree")
    if (root / "modules").exists():
        fail("DNP contains a local modules directory")
    primary = root / data.get("branding", {}).get("primary_asset", "")
    retired = root / data.get("branding", {}).get("retired_asset", "")
    if not primary.is_file() or retired.exists():
        fail("branding state drifted")

    gate = "tools/validation/phase-gates/validate_phase6_step8.sh"
    if subprocess.run(
        ["git", "diff", "--quiet", "origin/dev", "--", gate],
        cwd=root,
        check=False,
    ).returncode != 0:
        fail("historical Step 8 gate was modified instead of restored")

    prohibited = (
        "active validation-only candidate",
        "active validation-only gate",
        "### Active Phase 6 Step 8",
        "## Active Phase 6 Step 8",
        "Phase 6 Step 8 remains an unaccepted validation-only candidate",
        "Phase 6 Step 8 remains an implementation candidate",
        "Phase 6 Step 8 remains a validation-only implementation candidate",
        "Phase 6 Step 8 is a validation-only implementation candidate",
        "Phase 6 Step 8 is an active validation-only implementation candidate",
        "Step 8 is a validation-only implementation candidate",
        "Step 8 is the active validation-only candidate",
        "validation-only candidate active",
        "active Step 8 candidate status",
        "may perform hostile-condition and role-race validation",
        "rebaseline-required state gate",
    )
    for relative in CURRENT_INDEXES:
        path = root / relative
        text = path.read_text(encoding="utf-8")
        if text.count(STATUS_START) != 1 or text.count(STATUS_END) != 1:
            fail(f"{relative} is missing the canonical governed-status block")
        if STEP7_COMMIT not in text or "rebaseline required" not in text.lower():
            fail(f"{relative} is not synchronized to Step 7/rebaseline status")
        lowered = " ".join(text.lower().split())
        for phrase in prohibited:
            if phrase.lower() in lowered:
                fail(f"{relative} retains stale current-status text: {phrase}")

    boundary_text = " ".join((root / "docs/architecture/foundation/repository-boundary-synchronization.md").read_text(encoding="utf-8").lower().split())
    for phrase in prohibited:
        if phrase.lower() in boundary_text:
            fail(f"repository-boundary synchronization retains stale status text: {phrase}")

    root_readme = (root / "README.md").read_text(encoding="utf-8")
    if root_readme.count("### Remaining Platform Work") != 1:
        fail("README must contain exactly one Remaining Platform Work heading")

    record = root / "docs/architecture/backend-services/phase-6-step-8-hostile-failure-concurrency-and-resource-validation.md"
    record_text = record.read_text(encoding="utf-8")
    if '<!-- phase-6-step-8-rebaseline-notice:start -->' not in record_text or "rebaseline required" not in record_text.lower():
        fail("Step 8 record is missing its rebaseline notice")
    if "# Iron Signal Platform Production Go Module" in (root / "go/platform/README.md").read_text(encoding="utf-8"):
        fail("current Go README uses the retired public name")

    print("PASS: DNP machine-readable project status is valid")
    print("PASS: Accepted Phase 5 and Phase 6 Step 7 identities are synchronized")
    print("PASS: Phase 6 Step 8 is honestly marked rebaseline-required")
    print("PASS: Historical Step 8 candidate gate remains unchanged")
    print("PASS: Current indexes share one canonical governed-status block")
    print("PASS: DNP and Module Families repository boundaries are synchronized")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (CheckFailure, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
