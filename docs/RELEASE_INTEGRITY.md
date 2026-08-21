# Release integrity

## Canonical artifacts

The canonical public artifacts are attached to the corresponding immutable GitHub release tag. For v0.3.69, use the [release page](https://github.com/rookepoole/RelaySociety-Releases/releases/tag/v0.3.69).

Do not trust a filename by itself. Verify the complete byte length and SHA-256 value against the release page, `SHA256SUMS.txt`, and [`releases/current.json`](../releases/current.json).

## Windows verification

```powershell
Get-FileHash .\Relay-Society-v0.3.69-windows-x64.zip -Algorithm SHA256
```

Expected digest:

```text
29d4c92fd3117508bb5e13fe284f9a37c5049d1e171d3d1dd4e48a0d630cc17f
```

Expected byte length: `10170428`.

## Linux verification

```sh
sha256sum Relay-Society-v0.3.69-linux-x64.tar.gz
```

Expected digest:

```text
8b67e9fe0805a7e2843c029a9786a245a276d2446d440323f5ab25e2483eda8f
```

Expected byte length: `10657876`.

## What a matching checksum proves

A matching digest proves that the downloaded file is byte-for-byte identical to the file whose digest is published by this repository. It detects truncation, transfer errors, and changed bytes.

## What it does not prove

The v0.3.69 packages are unsigned and record `sourceRevision=uncommitted-worktree`. A published checksum does not provide:

- operating-system code-signing identity;
- notarization;
- an independently attested source-to-binary chain;
- a reproducible-build seal;
- proof that the publisher account or release page was never compromised.

These are explicitly open release-engineering gaps. The packages should be used only by beta users who understand and accept that boundary.

## Machine-readable records

- [`releases/current.json`](../releases/current.json) is the mutable repository catalog pointing to the current accepted release.
- `relay.update-manifest-v0.3.69.json` on the tagged release is the immutable version-specific update manifest.
- `SHA256SUMS.txt` on the tagged release contains the package digests.
- `automaticExecution` is false. No manifest in this beta authorizes unattended replacement or execution.
