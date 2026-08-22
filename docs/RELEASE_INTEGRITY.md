# Release integrity

## Canonical artifacts

The canonical public artifacts are attached to the corresponding immutable GitHub release tag. For v0.3.79, use the [release page](https://github.com/rookepoole/RelaySociety-Releases/releases/tag/v0.3.79).

Do not trust a filename by itself. Verify the complete byte length and SHA-256 value against the release page, `SHA256SUMS.txt`, and [`releases/current.json`](../releases/current.json).

## Windows verification

```powershell
Get-FileHash .\Relay-Society-v0.3.79-windows-x64.zip -Algorithm SHA256
```

Expected digest:

```text
96f4842efc088e5b8bc5857c229cf19914c1d131c4cfbefdd441c8332b8b2e99
```

Expected byte length: `11165036`.

## Linux verification

```sh
sha256sum Relay-Society-v0.3.79-linux-x64.tar.gz
```

Expected digest:

```text
d92a1e2371b0a98a3a4dfc0db6e2fd67f09c2b54dc34c446b3d1f31d460a4972
```

Expected byte length: `11467622`.

## What a matching checksum proves

A matching digest proves that the downloaded file is byte-for-byte identical to the file whose digest is published by this repository. It detects truncation, transfer errors, and changed bytes.

## What it does not prove

The v0.3.79 packages are unsigned and record `sourceRevision=uncommitted-worktree`. A published checksum does not provide:

- operating-system code-signing identity;
- notarization;
- an independently attested source-to-binary chain;
- a reproducible-build seal;
- proof that the publisher account or release page was never compromised.

These are explicitly open release-engineering gaps. The packages should be used only by beta users who understand and accept that boundary.

## Machine-readable records

- [`releases/current.json`](../releases/current.json) is the mutable repository catalog pointing to the current accepted release.
- `relay.update-manifest-v0.3.79.json` on the tagged release is the immutable version-specific update manifest.
- `SHA256SUMS.txt` on the tagged release contains the package digests.
- `automaticExecution` is false. No manifest in this beta authorizes unattended replacement or execution.
