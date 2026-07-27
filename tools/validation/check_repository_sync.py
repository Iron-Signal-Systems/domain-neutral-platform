#!/usr/bin/env python3
from __future__ import annotations

import re
import struct
import subprocess
import sys
from pathlib import Path

MODULE_REPO = "https://github.com/Iron-Signal-Systems/module-families"
HEX40 = re.compile(r"^[0-9a-f]{40}$")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


class CheckFailure(RuntimeError):
    pass


def fail(message: str) -> None:
    raise CheckFailure(message)


def png_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        fail(f"Branding asset is not a valid PNG: {path}")
    width, height = struct.unpack(">II", data[16:24])
    if width < 256 or height < 256:
        fail(f"Branding PNG is unexpectedly small: {width}x{height}")
    return width, height


def active_text_files(root: Path) -> list[Path]:
    suffixes = {".md", ".sh", ".py", ".yaml", ".yml", ".json", ".txt"}
    return [
        p for p in root.rglob("*")
        if p.is_file()
        and ".git" not in p.parts
        and p.suffix.lower() in suffixes
    ]


def main() -> int:
    root = Path(
        subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], text=True
        ).strip()
    )

    if (root / "modules").exists():
        fail("DNP must not contain a local modules/ directory")

    if (root / "tools/validation/phase-gates/cad").exists():
        fail("DNP must not contain the CAD phase-gate directory")

    readme = (root / "README.md").read_text(encoding="utf-8")

    layout_match = re.search(
        r"## Repository Layout\n\n```text\n(.*?)\n```",
        readme,
        re.DOTALL,
    )
    if not layout_match:
        fail("README repository-layout block was not found")
    if "modules/" in layout_match.group(1) or "CAD/" in layout_match.group(1):
        fail("README repository layout still contains a local module tree")

    image_match = re.search(
        r'<img\b[^>]*\bsrc="([^"]+\.png)"[^>]*>',
        readme,
        re.DOTALL | re.IGNORECASE,
    )
    if not image_match:
        fail("README does not reference a PNG branding asset")
    image_path = (root / image_match.group(1)).resolve()
    try:
        image_path.relative_to(root)
    except ValueError as exc:
        raise CheckFailure("README branding image escapes the repository") from exc
    if not image_path.is_file():
        fail(f"README branding asset does not exist: {image_match.group(1)}")
    width, height = png_dimensions(image_path)

    integration = (
        root
        / "docs/architecture/foundation/module-family-repository-integration.md"
    )
    if not integration.is_file():
        fail("Module Families integration record is missing")
    integration_text = integration.read_text(encoding="utf-8")
    if MODULE_REPO not in integration_text:
        fail("Integration record does not name the canonical Module Families repo")
    commit_match = re.search(r"(?m)^Commit:\s+([0-9a-f]{40})$", integration_text)
    if not commit_match or not HEX40.fullmatch(commit_match.group(1)):
        fail("Integration record does not pin an immutable 40-character commit")
    if "Path:   modules/" not in integration_text:
        fail("Integration record does not identify the modules/ path")
    if "/modules/CAD/README.md" not in integration_text:
        fail("Integration record does not link to the CAD module")

    malformed: list[str] = []
    local_module_refs: list[str] = []
    local_gate_refs: list[str] = []

    allowed_plain_module_files = {
        "docs/architecture/foundation/module-family-repository-integration.md",
        "docs/module-migration-drift-report.md",
        "docs/architecture/foundation/repository-boundary-synchronization.md",
        "tools/validation/check_repository_sync.py",
        "tools/validation/phase-gates/validate_phase4_step7.sh",
        "tools/validation/phase-gates/validate_phase4_step8.sh",
    }

    for path in active_text_files(root):
        # This validator contains its own forbidden-pattern strings.
        # Exclude the validator source from repository-content scans.
        if path.resolve() == Path(__file__).resolve():
            continue

        relative = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")

        if "./https://" in text or (
            f"{MODULE_REPO}/" in text
            and f"/{MODULE_REPO}/" in text
        ):
            malformed.append(relative)

        for line_no, line in enumerate(text.splitlines(), start=1):
            stripped = line.strip()

            if "modules/CAD" in line:
                external = MODULE_REPO in line
                allowed = relative in allowed_plain_module_files
                deleted_diff_line = stripped.startswith("-")
                if not external and not allowed and not deleted_diff_line:
                    local_module_refs.append(f"{relative}:{line_no}")

            if "tools/validation/phase-gates/cad" in line:
                external = MODULE_REPO in line
                allowed = relative in allowed_plain_module_files
                if not external and not allowed:
                    local_gate_refs.append(f"{relative}:{line_no}")

    if malformed:
        fail("Malformed external URLs remain:\n  " + "\n  ".join(malformed))
    if local_module_refs:
        fail(
            "Local CAD references remain in DNP:\n  "
            + "\n  ".join(local_module_refs)
        )
    if local_gate_refs:
        fail(
            "Local CAD gate references remain in DNP:\n  "
            + "\n  ".join(local_gate_refs)
        )

    for gate in (
        root / "tools/validation/phase-gates/validate_phase4_step7.sh",
        root / "tools/validation/phase-gates/validate_phase4_step8.sh",
    ):
        text = gate.read_text(encoding="utf-8")
        if "'modules/CAD/" in text or "check_contains modules/CAD/" in text:
            fail(f"Accepted gate still requires deleted local CAD files: {gate}")
        if (
            "module-family-repository-integration.md" not in text
            or "Commit: [0-9a-f]{40}" not in text
        ):
            fail(f"Accepted gate does not validate the external module pin: {gate}")

    print("PASS: DNP has no local modules/ tree")
    print("PASS: DNP has no local CAD phase gate")
    print("PASS: README repository layout matches the DNP boundary")
    print(
        "PASS: README branding PNG exists and is valid "
        f"({image_path.relative_to(root)}, {width}x{height})"
    )
    print(
        "PASS: Module Families integration is pinned at "
        f"{commit_match.group(1)}"
    )
    print("PASS: No malformed, local CAD, or local CAD-gate references remain")
    print("PASS: Accepted Phase 4 gates validate the external module boundary")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except CheckFailure as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
