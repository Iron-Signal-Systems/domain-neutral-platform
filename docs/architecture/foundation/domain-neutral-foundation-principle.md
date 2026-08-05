# Domain-Neutral Foundation Principle

> **Document status:** Normative Platform Foundation architecture.

## Principle

The Platform Foundation must remain independent of any single operational
domain.

Operational modules may expose demanding requirements, but no module family
defines the limits of the Platform Foundation.

A requirement discovered while designing any module must be generalized before
it becomes a Foundation concept.

## Foundation Admission Rule

A concept belongs in the Foundation only when at least one of the following is
true:

1. It establishes a shared trust, identity, authorization, accountability,
   governance, resilience, observability, or integration boundary.
2. It is reusable across multiple unrelated module families.
3. It provides a neutral extension point through which modules can define
   domain-specific behavior.
4. It is required to preserve consistent security, integrity, or historical
   guarantees across the platform.

A concept does not belong in the Foundation merely because the first module
requires it.

## Domain-Specific Concepts

Domain records and workflows belong to modules.

This includes module-owned records, transactions, workflows, status models,
schedules, domain taxonomies, user interactions, and acceptance criteria.

The Foundation may provide shared controls used by modules, but it must not
define their operational meaning.

## Neutral Foundation Concepts

Foundation concepts may include:

- Organization
- Organizational Unit
- Platform Service
- Deployment
- Identity
- Device
- Session
- Trust Provider
- Authentication Assertion
- Governed Purpose
- Governed Operation
- Governed Scope
- Protected Resource Target
- Data Classification
- Authority Definition
- Authority Grant
- Approval Policy
- Authorization Policy
- Authorization Lease
- Decision Record
- Lifecycle Event
- Governed Document
- Control
- Risk
- Workload
- Integration Event

Modules may specialize these concepts without changing their Foundation
meaning.

## Governed Scope

The Foundation uses **Governed Scope** for a typed boundary that constrains
authority, eligibility, approval, policy, data handling, or a protected
operation.

A module may define Governed Scope types such as:

- `REGION`
- `SERVICE_AREA`
- `DEPARTMENT`
- `FACILITY`
- `PROGRAM`

The Foundation must not require every Governed Scope to be geographic, legal,
administrative, or specific to one operational domain.

## Review Requirement

When a proposed Foundation term is strongly associated with one domain, the
design must determine whether:

1. The concept belongs entirely inside that module;
2. The concept should be represented by a neutral Foundation abstraction; or
3. The Foundation should provide an extension mechanism through which the
   module defines it.

The burden is on the design to justify why a domain-specific concept belongs
in the shared Foundation.
