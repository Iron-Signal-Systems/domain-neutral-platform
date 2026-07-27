# DNP Foundation Documentation

<!-- dnp-current-governed-status:start -->
## Current Governed Project Status

- Accepted database boundary: Phase 5 at `phase-5-production-database-security-boundary-complete-v1`, commit `9f8dbf9d909ef157df72b12511b165a689559093`.
- Accepted production Go boundary: Phase 6 Step 7 at `79e9723b2dd12e813de8a8c665d08d4f61cc8fab`; static and complete validation each reported 142 PASS and 0 FAIL.
- Phase 6 Step 8: **rebaseline required** after the governed DNP repository rename and CAD extraction changed paths frozen by the original candidate. Acceptance is not claimed, and the historical candidate gate is not a current acceptance gate.
- Module ownership: CAD and other domain modules are maintained in the Module Families repository.
- Machine-readable authority: `docs/project-status.json`.
<!-- dnp-current-governed-status:end -->
> **Current cross-boundary status:** Phase 5 production database security
> boundary formally accepted; Phase 6 Steps 3 through 7 production Go
> checkpoints accepted; Phase 6 Step 8 validation-only candidate active.
>
> **Boundary:** This Foundation index records downstream consumption
> status without moving service-host, transport, or module behavior into
> the domain-neutral Foundation.

> **Architecture status:** Normative and under active refinement.
>
> **SQL status:** Initial Foundation migrations `000–099` exist. Selected
> controls are database-enforced and tested; structural presence does not imply
> complete runtime, deployment, or operational enforcement.
>
> **Current status:** Phase 4 approval independence and separation of duties
> formally accepted at `phase-4-approval-independence-and-separation-of-duties-complete-v1`.

## Purpose

The Platform Foundation is a domain-neutral layer for trust, identity,
authentication inputs, sessions, authorization, approvals, accountable
Decision Records, governance, compliance, lifecycle, resilience, resource
governance, observability, and integration intent.

Potential consumers include public safety, municipal administration, finance,
human resources, records management, permitting, fleet and asset systems,
utilities, education, and future integrated services.

The Foundation does not contain CAD incidents, RMS cases, evidence custody,
payroll, procurement, Fire or EMS workflow, student records, permits, utility
accounts, or other module-owned business records.

## Non-Negotiable Principles

1. Trust must be established before protected identity or authority is
   accepted.
2. A certificate, password, MFA result, Authentication Assertion, session,
   role, approval, network location, or lease secret does not independently
   grant access.
3. Authentication establishes identity context; authorization establishes
   bounded authority.
4. Future Go services will collect typed supporting records, coordinate
   workflows, and call controlled APIs; PostgreSQL will independently
   verify selected protected operations and controlled state transitions.
5. No ordinary identity, application account, administrator, or accumulated
   role set may provide unrestricted platform authority.
6. Required decision stages fail closed on `FAIL` or `NOT_EVALUATED`.
7. Material decisions and lifecycle transitions must retain attributable,
   reviewable records.
8. Policies, agreements, controls, rules, and governed documents used in
   decisions must be versioned and integrity-verifiable.
9. Current state must not silently overwrite historical state.
10. Shared infrastructure does not create centralized organizational
    authority.
11. Authorization is bounded by identity, organization, Platform Service,
    Governed Purpose, Governed Operation, Protected Resource Target, Governed
    Scope, Data Classification, policy, and authoritative time.
12. External monitoring, integration, and delivery providers remain
    replaceable.
13. Workloads and resource consumption must be attributable and bounded.
14. Availability, recovery, degraded operation, and compromise recovery must
    be governed before production use.
15. Domain-specific concepts belong in modules; the Foundation uses neutral
    shared concepts and extension points.

## Accepted Phase 1 Boundary

Phase 1 is accepted at:

```text
phase-1-authentication-assertion-complete-v1
```

Accepted evidence:

```text
31 manifest migrations
31 registered migrations
10 sequential test files
1 concurrency test file
135 PASS
0 FAIL
3 understood WARN
```

Phase 1 established controlled local Authentication Assertion verification,
rejection, expiration, revocation, exact-context consumption, terminal-state
enforcement, and concurrent single-use behavior.

See:

- [Authentication Assertion Verification and Consumption Model](authentication-assertion-verification-and-consumption-model.md)
- [Phase 1 Authentication Assertion Acceptance](phase-1-authentication-assertion-acceptance.md)

## Accepted Phase 2 Boundary

Phase 2 is accepted at:

```text
phase-2-session-control-complete-v1
```

Accepted evidence:

```text
32 manifest migrations
32 registered migrations
12 sequential test files
4 concurrency test files
213 PASS
0 FAIL
3 understood WARN
```

Phase 2 established atomic session establishment, step-up, current-trust
revalidation, controlled activity, lock and administrative unlock, absolute
and inactivity expiration, revocation, termination, terminal-state
enforcement, same-transaction session events, and independent-connection
concurrency proofs.

See:

- [Session Establishment, Step-Up, and Lifecycle Model](session-establishment-step-up-and-lifecycle-model.md)
- [Phase 2 Session Establishment, Step-Up, and Lifecycle Acceptance](phase-2-session-establishment-step-up-and-lifecycle-acceptance.md)

## Accepted Phase 3 Boundary

Phase 3 is accepted at:

```text
phase-3-authorization-control-complete-v1
```

Accepted evidence:

```text
33 manifest migrations
33 registered migrations
16 sequential test files
9 concurrency test files
408 PASS
0 FAIL
3 understood WARN
```

Phase 3 established deterministic Authorization Policy Version selection,
controlled policy binding, required-stage closure, supporting-record
enforcement, finalization-once Decision Records, controlled Authorization
Lease issuance, exact-context verification and use, fail-closed current
state revalidation, and independent-connection concurrency proofs.

See:

- [Authorization Decision and Lease Issuance Model](authorization-decision-and-lease-issuance-model.md)
- [Authorization Evaluation Contract](authorization-evaluation-contract.md)
- [Phase 3 Authorization Decision and Controlled Lease Acceptance](phase-3-authorization-decision-and-controlled-lease-acceptance.md)

The formal acceptance record was committed after the annotated tag. The tag
identifies the exact accepted SQL and test tree; later documentation commits
must not alter that accepted implementation without Phase 3 revalidation.


## Accepted Phase 4 Boundary

Phase 4 approval independence and separation of duties is formally accepted at:

```text
phase-4-approval-independence-and-separation-of-duties-complete-v1
```

Accepted result:

```text
34 manifest migrations
34 registered migrations
21 sequential test files
16 concurrency test files
734 PASS
0 FAIL
3 understood WARN
Correctness result: PASS
Resource observation: RECORDED
Performance thresholds: NOT_EVALUATED
159 phase-gate PASS checks
0 phase-gate FAIL checks
```

The accepted scope includes controlled Approval Action recording, requester and
directly affected identity independence, effective-actor uniqueness,
organization and Authority Grant origin independence, reciprocal-request
protection, delegated-grant lineage, incompatible-authority and prohibited-duty
enforcement, current stage satisfaction, finalization-once Approval Requests,
Decision Record stage linkage, later-use approval continuity, and seven
independent-connection concurrency proofs.

The Platform Foundation remains domain-neutral. Location services,
communications, GIS rendering, operational workstations, user interfaces, and
module-specific workflows remain downstream architecture areas.

See:

- [Approval Independence and Separation of Duties](approval-independence-and-separation-of-duties-model.md)
- [Phase 4 Approval Independence and Separation of Duties Acceptance](phase-4-approval-independence-and-separation-of-duties-acceptance.md)
- [Resource Telemetry and Performance-Regression Testing](resource-telemetry-and-performance-regression-testing-model.md)
- [Foundation Migration Timeout and Execution Performance Standard](foundation-migration-timeout-and-execution-performance-standard.md)

## Documentation Groups

### Boundaries, Trust, Authentication, and Database Enforcement

- [Foundation Terminology and Domain Neutrality](foundation-terminology-and-domain-neutrality.md)
- [Platform Boundaries](platform-boundaries.md)
- [Authentication and Authorization Evaluation](authentication-and-authorization-evaluation-model.md)
- [Authentication Assertion Verification and Consumption Model](authentication-assertion-verification-and-consumption-model.md)
- [Phase 1 Authentication Assertion Acceptance](phase-1-authentication-assertion-acceptance.md)
- [Session Establishment, Step-Up, and Lifecycle Model](session-establishment-step-up-and-lifecycle-model.md)
- [Database Security](database-security-model.md)
- [Schema Naming Conventions](schema-naming-conventions.md)
- [SQL Migration Map](sql-migration-map.md)

### Organizations, Services, Identity, and Eligibility

- [Organization and Governed Scope](organization-and-governed-scope-model.md)
- [Service Participation and Federation](service-participation-and-federation-model.md)
- [Organizational Attestation and Access Eligibility](organizational-attestation-and-access-eligibility-model.md)

### Approval and Authorization

- [Approval Independence and Separation of Duties](approval-independence-and-separation-of-duties-model.md)
- [Authorization Evaluation Contract](authorization-evaluation-contract.md)
- [Authorization Decision and Lease Issuance Model](authorization-decision-and-lease-issuance-model.md)
- [Approval Framework](approval-framework.md)
- [Authority and Authorization](authority-and-authorization-model.md)
- [Authorization Lease](authorization-lease-model.md)
- [Decision Record Repository](decision-record-repository.md)

### Governance, Classification, and History

- [Data Classification and Information Governance](data-classification-and-information-governance-model.md)
- [Governed Document and Policy Versioning](governed-document-and-policy-versioning-model.md)
- [Lifecycle Versioning and Historical Lineage](lifecycle-versioning-and-historical-lineage-model.md)

### Compliance, Assurance, Findings, and Risk

- [Compliance and Control Framework](compliance-and-control-framework.md)
- [Common Security Control Catalog](common-security-control-catalog.md)
- [Compliance Profile Versioning](compliance-profile-versioning-model.md)
- [Control Implementation and Assurance Artifact Model](control-implementation-and-assurance-artifact-model.md)
- [Security Finding, Exception, and Remediation](security-finding-exception-and-remediation-model.md)
- [Risk Assessment and Treatment](risk-assessment-and-treatment-model.md)
- [Threat and Abuse Case](threat-and-abuse-case-model.md)

### Resilience, Performance, Experience, and Observability

- [Resilience, Availability, and Recovery](resilience-availability-and-recovery-model.md)
- [Performance, Efficiency, and Resource Governance](performance-efficiency-and-resource-governance-model.md)
- [Resource Telemetry and Performance-Regression Testing](resource-telemetry-and-performance-regression-testing-model.md)
- [Foundation Migration Timeout and Execution Performance Standard](foundation-migration-timeout-and-execution-performance-standard.md)
- [Client Experience and Accessibility](https://github.com/Iron-Signal-Systems/module-families/blob/1e017c7ab874969395fb31e030c0149116bf77cf/modules/CAD/docs/architecture/user-interface/client-experience-and-accessibility-model.md)
- [Accessibility and Inclusive Interaction](https://github.com/Iron-Signal-Systems/module-families/blob/1e017c7ab874969395fb31e030c0149116bf77cf/modules/CAD/docs/architecture/user-interface/accessibility-and-inclusive-interaction-model.md)
- [Observability, Health, and Operational Telemetry](observability-health-and-operational-telemetry-model.md)

## Current Implementation Boundaries

The Foundation SQL and deployment boundaries are current through formal Phase 5
acceptance. Production Go consumption is current through accepted Phase 6 Step
7. Phase 6 Step 8 requires a governed rebaseline; acceptance is not claimed.

The Foundation remains domain-neutral. CAD, RMS, workstation, interface,
mapping, and other domain-specific records and workflows remain in Module
Families.

## Accepted Phase 5 Production Database Security Boundary

Phase 5 is formally accepted at:

```text
phase-5-production-database-security-boundary-complete-v1
```

The accepted implementation targets `9f8dbf9d909ef157df72b12511b165a689559093` and includes production
role topology, ownership, least-privileged runtime grants, controlled service
APIs, investigation and validation roles, disabled-at-rest break-glass,
credential lifecycle controls, and hostile-condition role-race validation.

- [Phase 5 Production Database Security Boundary Acceptance](phase-5-production-database-security-boundary-acceptance.md)

## Accepted Phase 6 Step 7 Downstream Consumption Boundary

Phase 6 Step 7 is accepted at `79e9723b2dd12e813de8a8c665d08d4f61cc8fab` with 142 PASS and 0 FAIL
in both static and complete validation. The Go layer consumes accepted
Foundation decisions through bounded process identities, controlled database
operations, authenticated transport, and two service-specific delivery workers.
It does not move service-host, transport, or module behavior into the
Foundation.

- [Phase 6 Step 7 Integration and Monitoring Delivery Workers](../backend-services/phase-6-step-7-integration-and-monitoring-delivery-workers.md)

## Phase 6 Step 8 — Rebaseline Required

Step 8 adds hostile, failure, concurrency, redaction, privilege, lease-race, and
observation-only resource validation. Acceptance is not yet claimed, and the
accepted production boundary remains frozen at Step 7.

- [Phase 6 Step 8 Hostile, Failure, Concurrency, and Resource Validation](../backend-services/phase-6-step-8-hostile-failure-concurrency-and-resource-validation.md)

## Remaining Foundation and Platform Work

The following remain incomplete until separately implemented, validated, and
accepted:

- Complete Decision Record cryptographic integrity and later review or
  supersession controls.
- Stronger append-only mutation protection where required.
- Migration-checksum population and enforcement.
- Trust-Provider-specific verifier-role and credential boundaries.
- Additional controlled Foundation API operations after separate review.
- External-System Adapters beyond the accepted delivery-worker boundary.
- Off-host integrity anchoring and protected export.
- Backup protection and restoration validation.
- Trusted rebuild and compromise recovery.
- Shared Resources and additional operational modules.

## Foundation Migration Execution Contract

Every ordinary migration listed by `sql/schema/manifests/foundation.manifest`
uses transaction-local limits of:

```sql
SET LOCAL lock_timeout = '5s';
SET LOCAL statement_timeout = '1min';
SET LOCAL idle_in_transaction_session_timeout = '1min';
```

Ordinary DDL should finish within a few seconds. An individual statement
observed above ten seconds requires investigation. The one-minute statement
limit is a hard execution-safety ceiling, not an expected duration or a general
performance-regression budget.

```bash
./tools/validation/validate_foundation_migration_timeouts.sh
```

## Change Discipline

A Foundation change should normally update:

1. The governing architecture document.
2. The applicable SQL migration or a new migration.
3. The authoritative manifest when migration order changes.
4. The SQL migration map.
5. Positive and negative automated tests.
6. Concurrency tests when state can be consumed or changed simultaneously.
7. Operational or deployment documentation when the change crosses the database
   boundary.
8. `docs/project-status.json` and the current documentation indexes when project
   status changes.

Historical phase records remain authoritative for their own checkpoints. They
must not be rewritten to imply that later capabilities existed at the time of
the earlier acceptance.
