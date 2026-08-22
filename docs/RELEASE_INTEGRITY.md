# Release integrity

## Canonical artifacts

The canonical public artifacts are attached to the corresponding immutable GitHub release tag. For v0.3.76, use the [release page](https://github.com/rookepoole/RelaySociety-Releases/releases/tag/v0.3.76).

Do not trust a filename by itself. Verify the complete byte length and SHA-256 value against the release page, `SHA256SUMS.txt`, and [`releases/current.json`](../releases/current.json).

## Windows verification

```powershell
Get-FileHash .\Relay-Society-v0.3.76-windows-x64.zip -Algorithm SHA256
```

Expected digest:

```text
42e00042e8e2c6ed2869b82a3a1d01311daa325b194be4a6897b4c13c91aa78f
```

Expected byte length: `10589025`.

## Linux verification

```sh
sha256sum Relay-Society-v0.3.76-linux-x64.tar.gz
```

Expected digest:

```text
c1c70921fbddde2ae5b08b0619da13c6ef816dc5a143cc967bd8d5be4e50e853
```

Expected byte length: `11289544`.

## What a matching checksum proves

A matching digest proves that the downloaded file is byte-for-byte identical to the file whose digest is published by this repository. It detects truncation, transfer errors, and changed bytes.

## What it does not prove

The v0.3.76 packages are unsigned and record `sourceRevision=uncommitted-worktree`. A published checksum does not provide:

- operating-system code-signing identity;
- notarization;
- an independently attested source-to-binary chain;
- a reproducible-build seal;
- proof that the publisher account or release page was never compromised.

These are explicitly open release-engineering gaps. The packages should be used only by beta users who understand and accept that boundary.

## Machine-readable records

- [`releases/current.json`](../releases/current.json) is the mutable repository catalog pointing to the current accepted release.
- `relay.update-manifest-v0.3.76.json` on the tagged release is the immutable version-specific update manifest.
- `SHA256SUMS.txt` on the tagged release contains the package digests.
- `automaticExecution` is false. No manifest in this beta authorizes unattended replacement or execution.
