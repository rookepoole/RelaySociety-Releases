# Relay Society v0.3.73 capabilities

This is the evidence-bounded public inventory for the accepted v0.3.73/schema-41 beta. “Implemented” means the end-user path exists. It does not expand a feature beyond the boundary stated beside it.

## Core product

### Control Room and governed tasks — Beta

Implemented:

- typed, durable task contracts;
- one-time assignee invitations and exact-contract acceptance;
- activation, pause, resume, revocation, and participant-access restoration;
- bounded jobs with attempts and leases;
- evidence-bound result submission and exact-check finalization;
- live task-event streaming with durable cursor replay.

Boundary: the packaged Windows and Linux lifecycle is qualified. The default authority model is one local administrator, not public multi-tenant identity.

### Policy, authority, and approval — Beta

Implemented:

- deterministic deny-first policy evaluation;
- contract-listed human approval requests and one-time decisions;
- hash-only storage for task-scoped participant authority;
- short-lived audience-bound leases;
- immutable consent, federation, and policy histories;
- revocation-aware recovery generations.

Boundary: an approval records the authorized decision and its evidence; it does not execute an external action on its own.

### Durable jobs and external effects — Advanced beta

Implemented:

- at-least-once jobs for retryable work;
- fail-closed external-effect jobs with stable effect keys;
- automatic heartbeats and bounded leases;
- receipt-required completion;
- ambiguity quarantine and explicit requester reconciliation;
- Windows Job containment and Unix process-group watchdog behavior.

Boundary: Relay does not claim global external exactly-once behavior. Ambiguous effects are quarantined instead of silently redispatched.

### Evidence, receipts, and early reputation — Advanced beta

Implemented:

- append-only SHA-256 event chains;
- root-authorized Ed25519 terminal receipts;
- offline receipt and portable-evidence verification;
- content-addressed artifacts and full bundle export;
- context-specific reputation observations with uncertainty;
- task-bound appeals with correction-by-exclusion.

Boundary: signed local evidence is real. Trusted time, public reputation, independent adjudication, and society-wide Sybil resistance are not claimed.

### Governed councils — Advanced beta

Implemented first production slice:

- owner-created councils with one-use, hash-only invitations for distinct council-scoped member principals;
- immutable proposals plus frozen membership, conflict, quorum, approval-threshold, option, and deadline records;
- pre-open conflict disclosure and automatic conflicted-member exclusion from eligibility and quorum;
- retained deliberation arguments with up to sixteen ordered, typed, content-addressed Relay artifact, Relay receipt, or credential-free HTTPS citations;
- losing-side minority endorsements and append-only vote revision histories;
- deterministic close with tie rejection, exact tally and outcome, a structured minority report retaining the selected argument and its citations, and a report-bound canonical decision hash;
- frozen distinct appellant, appeal-reviewer, and veto-authority subjects with bounded post-vote deadlines and one normalized escalation target;
- one append-only appeal with typed evidence, named-authority review, durable no-delivery escalation, append-only veto, and derived effective disposition without mutating the original decision;
- owner and no-administrator member workspaces in the Control Room;
- all 18 council operations in the generated Python and TypeScript clients;
- hash-chained council events, explicit integrity verification, restart validation, and backup/restore preservation.

Boundary: a council bearer proves a distinct council-scoped authorization subject, not one-human-one-account or physical-human identity. Relay preserves citation locators and digests but does not fetch them, decide their truth, or grant them authority. Escalation is recorded but not delivered (`deliveryAttempted=false`). Amendments, delegation, ranked choice, secret ballots, federated councils, and automated claims that an argument is objectively strongest remain open.

### Authentication and secret custody — Beta

Implemented:

- loopback-only default listener;
- one-use browser launch codes and revocable 12-hour sessions;
- durable exponential sign-in throttling and offline reset;
- Windows Credential Manager and Linux Secret Service custody;
- ChaCha20-Poly1305 sealed values and vault rotation;
- optional HashiCorp Vault Transit and Agent/AppRole custody.

Boundary: same-user malware and hostile worker code are outside the local security boundary. Production Vault HA/TLS/seal certification is not claimed.

### Backup, restore, and recovery — Beta

Implemented:

- online SQLite backup with an exact inventory manifest;
- signed recovery checkpoints and rollback protection;
- backup verification without WAL side effects;
- rollback-preserving restore under an exclusive data lock;
- portable cross-machine vault recovery packages;
- read-only doctor, vault-status, and vault-audit diagnostics.

Boundary: a normal backup and portable recovery material cover different state. Users must retain both when moving machines or OS identities.

### No-value settlement — Advanced beta

Implemented first production slice:

- exact integer-minor-unit requester simulator funding;
- signed contribution quotes for one to 64 unique participants totaling exactly 10,000 basis points;
- exact idempotent authorization and holds using the Relay-local profile or the narrow AP2 v0.2 compact ES256 closed-checkout profile;
- participant-signed tool, model, runtime, and pricing usage evidence;
- bounded dispute isolation with retained evidence and explicit release-to-contributor or refund-to-requester resolution;
- ledger-only post-finalization resolution that keeps the task terminal `disputed` and preserves its original task and settlement receipts;
- unrelated payouts while a challenged allocation remains isolated;
- immutable balanced double-entry transactions, balances, payouts, and settlement receipts;
- all eight settlement operations in the 96-operation generated Python and TypeScript clients and the requester/participant Control Room;
- Windows and Linux schema-40-to-41 migration plus schema-41 v0.3.72-to-v0.3.73 binary upgrade, receipt verification, backup, and restore without invented settlement history.

Boundary: simulator credits cannot be purchased, redeemed, sent outside Relay, or described as money. `liveValue` remains false. Full AP2/SD-JWT/delegation, a real payment-provider SPI, and live-value legal/security/provider clearance remain open; live payments are prohibited.

## Models, protocols, and developers

### Provider broker and local models — Advanced beta

Implemented:

- immutable OpenAI-compatible provider profiles;
- provider-key injection without exposing the key to an assignee;
- bounded, non-redirecting non-streaming chat requests;
- normalized results, durable replay, and explicit indeterminate state;
- local Ollama setup for `qwen2.5:3b`;
- evidence reconciliation for deliberately compatible services.

Boundary: provider OAuth, the OpenAI Responses API, and general streaming are not implemented.

### Framework integrations — Advanced beta

Qualified Windows/Ollama integration slices exist for:

- LangGraph 1.2.10;
- OpenAI Agents SDK 0.19.1;
- Google ADK 2.6.0;
- Microsoft Agent Framework 1.13.0;
- CrewAI 1.15.9;
- the versioned `relay.adapter/1.0` subprocess boundary.

Boundary: current native Linux framework reruns and native macOS qualification remain open.

### Model Context Protocol — Advanced beta

Implemented:

- MCP 2026-07-28 stateless discovery and per-request metadata;
- production `mcp-tools` and `mcp-call` clients;
- contract-governed `mcp-run` adapter;
- exact endpoint, subject, tool, and argument binding;
- restart-safe multi-round-trip human approval;
- an experimental durable MCP approval child task.

Boundary: the listed core paths pass official Python and TypeScript peer conformance; this is not a claim about every optional MCP feature.

### Agent2Agent — Advanced beta

Implemented:

- authenticated durable A2A task intake;
- Agent Card discovery and secure outbound messaging;
- governed remote execution with exact contract authority;
- return-immediately task polling and input continuation;
- protocol cancellation and content-addressed results;
- terminal `GetTask` reconciliation without a second `SendMessage`.

Boundary: A2A 1.0 JSON-RPC paths pass official SDK peers. Streaming and JWS enrollment remain open.

### Signed webhooks — Advanced beta

Implemented:

- CloudEvents 1.0 structured delivery;
- Standard Webhooks HMAC-SHA256 v1 signing;
- durable-before-send transactional outbox;
- receiver deduplication and response receipts;
- manual interruption resume;
- bounded retries and dead-letter handling.

Boundary: outbound delivery is implemented; inbound hosting and background scheduling are not.

### API, SDKs, and operations — Beta

Implemented:

- versioned `/api/v1` and OpenAPI 3.1.1;
- deterministic Python and TypeScript clients;
- structured server and SDK errors;
- health and readiness with transport truth;
- SQLite WAL, transactional migrations, and newer-schema refusal;
- 96 current JSON request/response operations.

Boundary: the generated clients and OpenAPI document ship inside the platform packages. This release repository is not yet the complete development source tree.

### Remote TLS and federation — Advanced beta

Implemented slices:

- explicit one-administrator remote HTTPS mode;
- exact Origin and Host enforcement;
- SPIFFE bundle publication and private-PKI consumption;
- in-memory Workload API SVID rotation;
- explicit mutual Relay peer admission;
- governed policy, directory, evidence, task, and revocation exchange slices.

Boundary: narrow verified slices exist. Automatic enrollment, a complete remote-team lifecycle, and full society replication do not.

## Acceptance-gate view

| Gate | Area | Current public status |
| --- | --- | --- |
| G0 | Constitutional specification | Complete |
| G1 | Local contract runtime | Partial; this is where the end-user beta lives |
| G2 | Framework and protocol bridge | Partial |
| G3 | Identity and capability trust | Partial |
| G4 | Evidence-based reputation | Partial |
| G5 | Governed councils | Partial; first production slice is accepted on Windows and Linux |
| G6 | Federation | Partial |
| G7 | Settlement | Partial; the bounded no-value simulator slice is accepted, while live-value settlement remains prohibited |
| G8 | Society laboratory | Planned |

The next release-critical gaps are source publication and repeatable CI provenance, signed packages, native macOS qualification, safe native updating and rollback, and independent-machine evidence.
