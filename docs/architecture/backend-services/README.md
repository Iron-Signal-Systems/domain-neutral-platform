# Backend Services Architecture

<!-- dnp-current-governed-status:start -->
## Current Governed Project Status

- Accepted database boundary: Phase 5 at `phase-5-production-database-security-boundary-complete-v1`, commit `9f8dbf9d909ef157df72b12511b165a689559093`.
- Accepted production Go boundary: Phase 6 Step 7 at `79e9723b2dd12e813de8a8c665d08d4f61cc8fab`; static and complete validation each reported 142 PASS and 0 FAIL.
- Phase 6 Step 8: **rebaseline required** after the governed DNP repository rename and module extraction changed paths frozen by the original candidate. Acceptance is not claimed, and the historical candidate gate is not a current acceptance gate.
- Module ownership: domain-specific operational modules are maintained in the Module Families repository.
- Machine-readable authority: `docs/project-status.json`.
<!-- dnp-current-governed-status:end -->
> **Status:** Architecture area under active refinement.

## Documents

- [Production Go Service Boundary and Runtime Model](production-go-service-boundary-and-runtime-model.md)
- [Phase 6 Step 1 Production Go Service Contract Freeze](phase-6-step-1-production-go-service-contract.md)
- [Phase 6 Step 2 Production Go Workspace and Build Baseline](phase-6-step-2-production-go-workspace-and-build-baseline.md)
- [Phase 6 Step 3 Runtime Bootstrap and PostgreSQL Connectivity](phase-6-step-3-runtime-bootstrap-and-postgresql-connectivity.md)
- [Phase 6 Step 4 Process-Host Integration and Hostile Runtime Validation](phase-6-step-4-process-host-integration-and-hostile-runtime-validation.md)
- [Phase 6 Step 5 Controlled Foundation API Adapter](phase-6-step-5-controlled-foundation-api-adapter.md)
- [Phase 6 Step 6 Authenticated Request and Transport Boundary](phase-6-step-6-authenticated-request-and-transport-boundary.md)
- [Phase 6 Step 7 Integration and Monitoring Delivery Workers](phase-6-step-7-integration-and-monitoring-delivery-workers.md)
- [Phase 6 Step 8 Hostile, Failure, Concurrency, and Resource Validation](phase-6-step-8-hostile-failure-concurrency-and-resource-validation.md)
- [Location Service Architecture](location-service-architecture.md)

Service documents define ownership, interfaces, state, failure behavior, persistence, security, and performance boundaries for the Go modular monolith and any later extracted service.

<!-- PHASE6_STEP1_STATUS -->

## Phase 6 Step 1

- [Production Go Service Boundary and Runtime Model](production-go-service-boundary-and-runtime-model.md)
- [Phase 6 Step 1 Production Go Service Contract Freeze](phase-6-step-1-production-go-service-contract.md)

Step 1 is the historical contract-freeze checkpoint. The production workspace was created in Step 2.

<!-- phase-6-step-2-status:start -->
## Historical Phase 6 Step 2 — Production Go Workspace and Reproducible Build Baseline

At the Step 2 checkpoint, the first production Go module existed at
`go/platform/` with three fail-closed executable skeletons, the exact
`go1.26.5` toolchain, zero third-party modules, and deterministic build
controls. No listener, database connection, credential, protected operation,
or worker loop existed at that checkpoint.

- [Phase 6 Step 2 Production Go Workspace and Build Baseline](phase-6-step-2-production-go-workspace-and-build-baseline.md)
<!-- phase-6-step-2-status:end -->

<!-- phase-6-step-3-status:start -->
## Historical Phase 6 Step 3 — Runtime Bootstrap and Bounded PostgreSQL Connectivity

At the Step 3 checkpoint, the three production Go processes had typed
fail-closed configuration, protected-file PostgreSQL URL loading, exact
service-role verification, bounded pgx pools, PostgreSQL 18 compatibility
checks, loopback-only health/readiness, context cancellation, and graceful
shutdown. Protected business operations and durable worker loops remained
absent at that checkpoint.

Historical gate:

```bash
./tools/validation/phase-gates/validate_phase6_step3.sh
```

- [Phase 6 Step 3 Runtime Bootstrap and PostgreSQL Connectivity](phase-6-step-3-runtime-bootstrap-and-postgresql-connectivity.md)
<!-- phase-6-step-3-status:end -->

<!-- phase-6-step-4-status:start -->
## Phase 6 Step 4 — Process-Host Integration and Hostile Runtime Validation

- [Phase 6 Step 4 Process-Host Integration and Hostile Runtime Validation](phase-6-step-4-process-host-integration-and-hostile-runtime-validation.md)

Step 4 is the accepted process-host checkpoint at
`3e15c8cbb7b666537be6a7ec832800e8f4ca9af0`, validated at 71 PASS and 0 FAIL.
<!-- phase-6-step-4-status:end -->

<!-- phase-6-step-5-status:start -->
## Phase 6 Step 5 — Controlled Foundation API Adapter

Step 5 is accepted at `1aefa613a80c1f5cdaf7807702b1b747d7e77ec5` with
96 PASS and 0 FAIL.

- [Phase 6 Step 5 Controlled Foundation API Adapter](phase-6-step-5-controlled-foundation-api-adapter.md)
<!-- phase-6-step-5-status:end -->

<!-- phase-6-step-6-status:start -->
## Phase 6 Step 6 — Authenticated Request and Transport Boundary

- [Phase 6 Step 6 Authenticated Request and Transport Boundary](phase-6-step-6-authenticated-request-and-transport-boundary.md)

Step 6 is accepted at `ec3c36081c686fa8ec82c8fd94bda421ed6cff42` with
92 PASS and 0 FAIL.
<!-- phase-6-step-6-status:end -->

<!-- phase-6-step-7-status:start -->
## Phase 6 Step 7 — Integration and Monitoring Delivery Workers

- [Phase 6 Step 7 Integration and Monitoring Delivery Workers](phase-6-step-7-integration-and-monitoring-delivery-workers.md)

Step 7 is accepted at commit `79e9723b2dd12e813de8a8c665d08d4f61cc8fab`. Static and complete validation each
reported 142 PASS and 0 FAIL.
<!-- phase-6-step-7-status:end -->

<!-- phase-6-step-8-status:start -->
## Phase 6 Step 8 — Hostile, Failure, Concurrency, and Resource Validation

- [Phase 6 Step 8 Hostile, Failure, Concurrency, and Resource Validation](phase-6-step-8-hostile-failure-concurrency-and-resource-validation.md)

Step 8 is the validation-only candidate over the frozen Step 7 implementation.
Formal Phase 6 acceptance remains Step 9.
<!-- phase-6-step-8-status:end -->
