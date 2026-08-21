# Release integrity

## Canonical artifacts

The canonical public artifacts are attached to the corresponding immutable GitHub release tag. For v0.3.72, use the [release page](https://github.com/rookepoole/RelaySociety-Releases/releases/tag/v0.3.72).

Do not trust a filename by itself. Verify the complete byte length and SHA-256 value against the release page, `SHA256SUMS.txt`, and [`releases/current.json`](../releases/current.json).

## Windows verification

```powershell
Get-FileHash .\Relay-Society-v0.3.72-windows-x64.zip -Algorithm SHA256
```

Expected digest:

```text
71bad8d9f4513082af3d9ab419ce5b1b015ee2facb5bee22fba6620d1709a205
```

Expected byte length: `10577594`.

## Linux verification

```sh
sha256sum Relay-Society-v0.3.72-linux-x64.tar.gz
```

Expected digest:

```text
cdc229d471c3ab38c9ea5f204e80a7f03c331a96e7424e0836c53b273c050c63
```

Expected byte length: `11006708`.

## What a matching checksum proves

A matching digest proves that the downloaded file is byte-for-byte identical to the file whose digest is published by this repository. It detects truncation, transfer errors, and changed bytes.

## What it does not prove

The v0.3.72 packages are unsigned and record `sourceRevision=uncommitted-worktree`. A published checksum does not provide:

- operating-system code-signing identity;
- notarization;
- an independently attested source-to-binary chain;
- a reproducible-build seal;
- proof that the publisher account or release page was never compromised.

These are explicitly open release-engineering gaps. The packages should be used only by beta users who understand and accept that boundary.

## Machine-readable records

- [`releases/current.json`](../releases/current.json) is the mutable repository catalog pointing to the current accepted release.
- `relay.update-manifest-v0.3.72.json` on the tagged release is the immutable version-specific update manifest.
- `SHA256SUMS.txt` on the tagged release contains the package digests.
- `automaticExecution` is false. No manifest in this beta authorizes unattended replacement or execution.
