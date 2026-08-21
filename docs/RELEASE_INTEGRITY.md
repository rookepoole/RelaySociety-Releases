# Release integrity

## Canonical artifacts

The canonical public artifacts are attached to the corresponding immutable GitHub release tag. For v0.3.71, use the [release page](https://github.com/rookepoole/RelaySociety-Releases/releases/tag/v0.3.71).

Do not trust a filename by itself. Verify the complete byte length and SHA-256 value against the release page, `SHA256SUMS.txt`, and [`releases/current.json`](../releases/current.json).

## Windows verification

```powershell
Get-FileHash .\Relay-Society-v0.3.71-windows-x64.zip -Algorithm SHA256
```

Expected digest:

```text
9644f574cf9266e569f5f7dc9342ee71045d6f856c01c4091f537e47496ad2fc
```

Expected byte length: `10319321`.

## Linux verification

```sh
sha256sum Relay-Society-v0.3.71-linux-x64.tar.gz
```

Expected digest:

```text
f5347fd9f10c85c7c2ca101fcd8c151e7185485f87816869f9c5bfca884c5a64
```

Expected byte length: `10782000`.

## What a matching checksum proves

A matching digest proves that the downloaded file is byte-for-byte identical to the file whose digest is published by this repository. It detects truncation, transfer errors, and changed bytes.

## What it does not prove

The v0.3.71 packages are unsigned and record `sourceRevision=uncommitted-worktree`. A published checksum does not provide:

- operating-system code-signing identity;
- notarization;
- an independently attested source-to-binary chain;
- a reproducible-build seal;
- proof that the publisher account or release page was never compromised.

These are explicitly open release-engineering gaps. The packages should be used only by beta users who understand and accept that boundary.

## Machine-readable records

- [`releases/current.json`](../releases/current.json) is the mutable repository catalog pointing to the current accepted release.
- `relay.update-manifest-v0.3.71.json` on the tagged release is the immutable version-specific update manifest.
- `SHA256SUMS.txt` on the tagged release contains the package digests.
- `automaticExecution` is false. No manifest in this beta authorizes unattended replacement or execution.
