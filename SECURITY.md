# Security Policy

## Reporting vulnerabilities

Report suspected vulnerabilities privately. Do not open a public issue, pull
request, discussion, or other public disclosure for an unresolved security
report.

Use GitHub private vulnerability reporting or the Security Advisory workflow
for this repository when that private reporting path is available. If GitHub
does not offer a private report form, contact an Iron Signal Systems repository
administrator through an existing private organizational channel.

Include, when available:

- the affected repository, commit, release, and artifact identity;
- the affected component or assurance boundary;
- reproduction steps or a proof of concept;
- expected and observed behavior;
- known impact and required preconditions; and
- whether public disclosure has already occurred.

Do not include credentials, private keys, access tokens, or unrelated sensitive
data in a report.

## Supported releases

DNP is currently pre-alpha and is not approved for production deployment.

Historical accepted phase boundaries identify exact validated engineering
boundaries. They do not make the complete current repository a supported
production release.

Development branches, pull requests, unsigned source snapshots, unpublished
candidates, and unaccepted releases are not accepted production authority.

An exact signed ISRAS testing candidate may perform strict pre-release
assurance. It remains non-authoritative and does not create stable release,
publication, promotion, or acceptance authority.

Previously accepted boundaries remain immutable historical records. A consuming
project remains governed by its exact accepted dependency or project boundary
until an explicit governed consuming-project re-adoption changes that boundary.

## Compromise response

A suspected signing key compromise, release artifact compromise, GitHub account
compromise, or workflow compromise suspends trust in the affected authority
until investigation establishes a safe boundary.

Trust suspension must be explicit and must identify the affected key, account,
workflow, release, artifact, repository, component, or time range.

Unaffected authority must not be revoked merely by assumption, and affected
authority must not remain trusted merely for convenience.

A compromised signing key is retired from active authority. Key retirement
does not rewrite historical records. Replacement authority requires a
separately reviewed key, updated trust material, and the normal governed
validation and acceptance path.

A compromised GitHub account or workflow must be contained before publication,
acceptance, promotion, or deployment resumes. Repository rules, workflow
definitions, credentials, signing configuration, and published identities must
be reviewed against the last trustworthy state.

## Release integrity and recovery

Published release artifacts are immutable. They must never be silently replaced
in place.

If an accepted release, accepted boundary, or release artifact is defective or
compromised, remediation uses corrective immutable releases or a new exact
governed boundary.

The corrective authority must preserve the affected historical record, identify
the superseded or affected authority, and state any required consuming-project
re-adoption boundary.

Consuming projects re-adopt explicitly. DNP must not silently move a dependency,
project pin, accepted boundary, or authority merely because a newer commit,
branch tip, release, or artifact exists.

Recovery must preserve exact source, tag, artifact, workflow, signing, and
acceptance identities sufficient to explain which authority was trusted before,
during, and after an incident.

## Historical preservation

Historical accepted releases, tags, commits, validation records, findings,
compromise records, and remediation records remain preserved.

They are not rewritten to hide an incident, adopt current terminology, or make
prior authority appear different from what was actually accepted.

Security corrections create new governed authority and explicit re-adoption
guidance rather than mutating historical accepted authority.
