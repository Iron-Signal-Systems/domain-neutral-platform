#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


CURRENT_FACING_FILES = (
    "README.md",
    "docs/architecture/foundation/README.md",
    "docs/architecture/foundation/domain-neutral-foundation-principle.md",
    "docs/architecture/foundation/foundation-terminology-and-domain-neutrality.md",
    "docs/architecture/foundation/dnp-project-naming-and-identity-transition.md",
    "docs/architecture/postgresql.md",
    "docs/compliance-profiles/README.md",
    "docs/architecture/foundation/control-implementation-and-assurance-artifact-model.md",
    "docs/architecture/backend-services/production-go-service-boundary-and-runtime-model.md",
)

PROHIBITED_PHRASES = (
    "Computer Aided Dispatch",
    "Records Management",
    "RMS cases",
    "CAD incidents",
    "Evidence and Property",
    "Fire and EMS",
    "Fire/EMS",
    "public safety",
    "public-safety",
)

PROHIBITED_PATTERNS = (
    re.compile(r"\bCAD\b"),
    re.compile(r"\bRMS\b"),
)

DIRECT_MODULE_PATH = "modules/" + "CAD/"


def main() -> int:
    root = Path(
        subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], text=True
        ).strip()
    )

    failures: list[str] = []
    for relative in CURRENT_FACING_FILES:
        path = root / relative
        if not path.is_file():
            failures.append(f"missing current-facing file: {relative}")
            continue

        text = path.read_text(encoding="utf-8", errors="replace")
        lowered = text.lower()

        for phrase in PROHIBITED_PHRASES:
            if phrase.lower() in lowered:
                failures.append(f"{relative}: prohibited phrase: {phrase}")

        for pattern in PROHIBITED_PATTERNS:
            if pattern.search(text):
                failures.append(
                    f"{relative}: prohibited current-facing term: {pattern.pattern}"
                )

        if DIRECT_MODULE_PATH in text:
            failures.append(
                f"{relative}: direct module-owned path remains: {DIRECT_MODULE_PATH}"
            )

    if failures:
        print("FAIL: current-facing DNP documentation is not domain-neutral", file=sys.stderr)
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        return 1

    print("PASS: current-facing DNP documentation contains no module-specific roadmap or workflow terms")
    print("PASS: direct module-owned documentation paths are absent from DNP indexes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
