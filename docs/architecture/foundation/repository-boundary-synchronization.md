# Repository Boundary Synchronization

## Status

Normative repository-maintenance contract.

## Boundary

DNP owns the domain-neutral Platform Foundation. Domain-specific modules,
including CAD, are maintained in Module Families.

The DNP repository must not contain:

- A local `modules/` implementation or documentation tree.
- A local CAD phase-gate directory.
- Validation gates that require deleted local module files.
- Repository-layout documentation that presents modules as DNP-owned paths.

## Branding

The root README selects the current DNP crest or badge through its image path.
The selected file must exist inside `docs/assets/branding/`, be a valid PNG,
and have usable dimensions. Branding changes do not change accepted technical
identifiers, tags, or historical commits.

## Validation

```bash
./tools/validation/check_repository_sync.sh
```

The check validates the repository layout, branding asset, immutable Module
Families integration pin, external CAD references, and accepted Phase 4 gate
synchronization.
