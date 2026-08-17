# Repository Guidelines

## Project Scope

DNP is the Domain-Neutral Platform Foundation for Iron Signal Systems.

The Foundation owns shared trust, identity, authentication, session,
authorization, approval, Decision Record, governance, resilience,
observability, integration, and resource-governance boundaries.

Domain-specific records, workflows, terminology, operational modules, and
user-interface behavior belong outside this repository unless a separately
governed Foundation change establishes otherwise.

## Repository Structure

- `go/platform/` contains the governed Go module and production service code.
- `database/` contains PostgreSQL Foundation implementation material.
- `test-framework/` contains database and deployment validation.
- `docs/architecture/foundation/` contains normative Foundation architecture.
- `docs/project-status.json` records machine-readable governed project status.
- `.isras/` contains the repository's ISRAS declaration and assurance material.
- `.local/` contains local generated validation records and is not authority.

## Go Development

The governed Go module is `go/platform/go.mod`.

Run Go commands from `go/platform`.

Use `go test -count=1 ./...`, `go test -race -count=1 ./...`, and `go vet ./...`
as appropriate to the affected boundary.

Format Go with `gofmt`.

Keep tests beside the packages they validate. Behavioral changes require
deterministic regression tests appropriate to the affected boundary.

## Engineering Rules

Preserve fail-closed behavior at trust, authentication, authorization,
privilege, configuration, transport, database, and lifecycle boundaries.

Do not weaken an accepted boundary merely to make a test pass.

Do not move domain-specific behavior into the Foundation for convenience.

Historical accepted tags, commits, records, identifiers, and validation
results are immutable historical authority and must not be rewritten.

Generated or temporary local validation output does not replace committed
project authority.

## Security-Sensitive Changes

Credential material must not be committed.

Tests should use explicit inert placeholders, runtime-generated ephemeral
values, or structurally safe fixtures that cannot be mistaken for operational
credentials.

Security-sensitive behavior must avoid disclosing protected values through
errors, logs, diagnostics, or test output.

## Commits and Review

Use focused commits with short imperative subjects, commonly prefixed with
`feat:`, `fix:`, `test:`, `docs:`, or `chore:`.

Sign commits.

Keep unrelated remediation, governance, product behavior, and acceptance
changes in separate commits when practical.

Do not claim acceptance, release authority, independent review, or successful
validation unless the exact applicable boundary has actually passed.
