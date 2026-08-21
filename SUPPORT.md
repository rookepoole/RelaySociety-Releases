# Relay Society beta support

## Before opening an issue

1. Confirm that you are running the current accepted beta from [GitHub Releases](https://github.com/rookepoole/RelaySociety-Releases/releases).
2. Verify the package SHA-256 against the release page.
3. Read the [exact getting-started guide](docs/GETTING_STARTED.md).
4. Run `relay-society doctor` when available.
5. Preserve the console output and data directory before troubleshooting.
6. Search existing issues for the same version, platform, and symptom.

## What to include

- Relay version and schema, if shown;
- Windows or Linux version and x64 architecture;
- portable launch or current-user installation;
- exact package filename and whether its checksum matched;
- the smallest reproducible sequence of actions;
- expected and observed behavior;
- sanitized console output;
- whether Relay restarted cleanly and whether `doctor` passed;
- whether the issue affects new data, existing data, or both.

## Never post these publicly

- one-use launch codes;
- browser sessions or API bearer tokens;
- invitation packages or participant bearers;
- provider keys or vault credentials;
- portable recovery material;
- unredacted task objectives, evidence, artifacts, or receipts;
- the complete contents of the Relay data directory;
- environment dumps that may contain secrets.

Use stable placeholders such as `<REDACTED_PROVIDER_KEY>` so logs remain structurally useful.

## Where to ask

- [Bug report](https://github.com/rookepoole/RelaySociety-Releases/issues/new?template=bug_report.yml)
- [Feature request](https://github.com/rookepoole/RelaySociety-Releases/issues/new?template=feature_request.yml)
- [Private vulnerability report](https://github.com/rookepoole/RelaySociety-Releases/security/advisories/new)

This is a beta project and does not yet provide a guaranteed support SLA.
