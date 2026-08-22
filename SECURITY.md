# Security policy

## Supported versions

Relay Society is currently an unsigned beta. Security fixes are evaluated for the latest accepted beta only.

| Version | Supported |
| --- | --- |
| 0.3.77 | Yes |
| 0.3.76 | No; upgrade to the current beta |
| Earlier betas | No; reproduce against the current beta first |

## Report a vulnerability privately

Do **not** open a public issue for a suspected vulnerability.

Use GitHub's private [Report a vulnerability](https://github.com/rookepoole/RelaySociety-Releases/security/advisories/new) flow. Include:

- affected Relay version and platform;
- exact preconditions and trust boundary;
- minimal reproduction steps;
- expected and observed behavior;
- likely impact;
- sanitized logs or evidence;
- whether the issue is already public or under active exploitation.

Never submit live provider keys, Relay tokens, one-time invitation packages, participant bearers, portable recovery material, private task evidence, or unredacted user data. Replace secrets with stable placeholders while preserving the structure needed to reproduce the issue.

This beta does not yet publish a formal response-time SLA. Reports will be assessed against the implemented boundary and coordinated privately when they are actionable.

## Current trust boundary

- Relay listens on loopback by default. Remote mode requires explicit configuration, protected TLS identity, and one exact HTTPS origin.
- Browser launch codes are one-use. Browser sessions are revocable, bearer-based, and limited to 12 hours.
- Relay grants no ambient authentication cookie; mutations enforce the exact Origin and Host.
- The local master key is held by Windows Credential Manager or freedesktop Secret Service. The Relay data directory stores only a random locator and encrypted values.
- Provider keys are sealed and injected only into bounded provider requests. Participants receive normalized results rather than provider credentials.
- Durable state uses SQLite WAL, transactional migrations, exclusive data locking, append-only controls, hash chains, and signed recovery checkpoints.
- Terminal receipts and portable evidence bundles support offline integrity checking. They do not independently provide trusted time or live revocation.

## Explicit non-claims

The current beta does not claim:

- signed packages, notarization, reproducible-build seals, or independent-machine provenance;
- a hostile-code sandbox or protection from same-user malware;
- multi-tenant human identity proof;
- product-wide or external exactly-once effects;
- a hardware or WORM monotonic anchor or trusted time;
- production-certified Vault HA/TLS/seal operations;
- a native macOS package;
- production public reputation, cryptographic council-member identity or broader council governance modes, live-value settlement, full AP2/SD-JWT/delegation, a live payment provider, or society-scale operation.

A report that demonstrates escape from the stated boundary, a failure to enforce the boundary, secret disclosure, unauthorized durable mutation, evidence forgery, recovery rollback, or unsafe external-effect redispatch is in scope.

## If compromise is suspected

1. Stop Relay.
2. Preserve the console output and relevant logs.
3. Do not delete the data directory or credential-service entry.
4. Make a protected copy before troubleshooting.
5. Revoke affected provider credentials through the provider.
6. Avoid publishing task evidence or recovery material while seeking help.
