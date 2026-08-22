# Release integrity

## Canonical artifacts

The canonical public artifacts are attached to the corresponding immutable GitHub release tag. For v0.3.78, use the [release page](https://github.com/rookepoole/RelaySociety-Releases/releases/tag/v0.3.78).

Do not trust a filename by itself. Verify the complete byte length and SHA-256 value against the release page, `SHA256SUMS.txt`, and [`releases/current.json`](../releases/current.json).

## Windows verification

```powershell
Get-FileHash .\Relay-Society-v0.3.78-windows-x64.zip -Algorithm SHA256
```

Expected digest:

```text
82d250988b970b11119cee06ac3dc1d6dd3d1f3b36451f1e42c1acd4cf9d3774
```

Expected byte length: `11088423`.

## Linux verification

```sh
sha256sum Relay-Society-v0.3.78-linux-x64.tar.gz
```

Expected digest:

```text
b0ce04dff71badf817cb384f6888da0a732111802f31d55f822a9c1a6d43bc40
```

Expected byte length: `11437455`.

## What a matching checksum proves

A matching digest proves that the downloaded file is byte-for-byte identical to the file whose digest is published by this repository. It detects truncation, transfer errors, and changed bytes.

## What it does not prove

The v0.3.78 packages are unsigned and record `sourceRevision=uncommitted-worktree`. A published checksum does not provide:

- operating-system code-signing identity;
- notarization;
- an independently attested source-to-binary chain;
- a reproducible-build seal;
- proof that the publisher account or release page was never compromised.

These are explicitly open release-engineering gaps. The packages should be used only by beta users who understand and accept that boundary.

## Machine-readable records

- [`releases/current.json`](../releases/current.json) is the mutable repository catalog pointing to the current accepted release.
- `relay.update-manifest-v0.3.78.json` on the tagged release is the immutable version-specific update manifest.
- `SHA256SUMS.txt` on the tagged release contains the package digests.
- `automaticExecution` is false. No manifest in this beta authorizes unattended replacement or execution.
