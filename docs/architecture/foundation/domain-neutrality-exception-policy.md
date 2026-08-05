# Domain-Neutrality Exception Policy

> **Status:** Normative repository-maintenance policy.

## Rule

Current-facing DNP documentation must describe only the domain-neutral Platform
Foundation. Operational module priorities, workflows, data models, user
interfaces, requirements, validation, and acceptance belong in the Module
Families repository.

## Permitted Exceptions

A domain-specific name may remain in DNP only when it is necessary to identify:

- an immutable historical acceptance record;
- a frozen migration or validation fixture;
- a compatibility identifier that has not completed a governed migration;
- the actual path or module involved in the repository extraction;
- an immutable cross-repository link or synchronization assertion.

The exception must be historical, compatibility-related, or required to prove
the repository boundary. It must not be used as current DNP product scope,
roadmap, architecture, or positioning.

## Current-Facing Files

The current-facing documentation scan covers the root project description,
Foundation indexes and principles, project naming, PostgreSQL architecture,
compliance terminology, and current status wording.

## Validation

Run:

```bash
python3 tools/validation/check_current_domain_neutrality.py
./tools/validation/check_repository_sync.sh
```

The check intentionally uses a narrow file list. It does not rewrite accepted
migrations, acceptance records, historical gates, or extraction records.
