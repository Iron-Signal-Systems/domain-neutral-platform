# Module Family Repository Integration

## Repository Boundary

DNP owns the domain-neutral Platform Foundation.

Domain-specific operational modules are maintained in:

```text
https://github.com/Iron-Signal-Systems/module-families
```

## Integrated Module Revision

```text
Commit: 1e017c7ab874969395fb31e030c0149116bf77cf
Path:   modules/
```

## Migrated Modules

- [CAD](https://github.com/Iron-Signal-Systems/module-families/blob/1e017c7ab874969395fb31e030c0149116bf77cf/modules/CAD/README.md)

## Integration Rule

DNP documentation and future integration work must reference immutable Module
Families revisions. DNP must not restore domain-specific records or workflows
to the Foundation repository without a separately governed repository-boundary
decision.


## Status Synchronization

DNP current project status is recorded in `docs/project-status.json`. Module
Families records the accepted DNP database and Go contract revisions in its
`module-families.yaml` catalog. The initial module-import revision remains
immutable and is not replaced by later documentation synchronization commits.
