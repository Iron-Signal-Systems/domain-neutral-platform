# Repository Boundary Synchronization

## Status

Normative repository-maintenance contract.

## Boundary

DNP owns the domain-neutral Platform Foundation. Domain-specific operational
modules are maintained in Module Families.

The DNP repository must not contain:

- A local `modules/` implementation or documentation tree.
- A local CAD phase-gate directory.
- Validation gates that require deleted local module files.
- Repository-layout documentation that presents modules as DNP-owned paths.

## Branding

The root README selects the current DNP branding asset through its image path.
The selected crest must exist inside `docs/assets/branding/`, be a valid PNG,
and have usable dimensions. Branding changes do not change accepted technical
identifiers, tags, or historical commits.


## Project Status Registry

Current project status is recorded in `docs/project-status.json`. The registry
must agree with the root README, documentation indexes, accepted Phase 5 tag
and commit, accepted Phase 6 Step 7 commit and validation counts, Step 8
rebaseline-required status, branding asset, and Module Families boundary.

## Validation

```bash
./tools/validation/check_repository_sync.sh
```

The check validates the repository layout, branding asset, machine-readable
project status, immutable Module Families integration pin, external module
references, accepted Phase 4 gate synchronization, and current phase-status
semantics.
