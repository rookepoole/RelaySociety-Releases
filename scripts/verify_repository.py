#!/usr/bin/env python3
"""Validate Relay Society public repository links and release metadata."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "releases" / "current.json"
SHA256 = re.compile(r"^[0-9a-f]{64}$")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

REQUIRED_FILES = (
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "SUPPORT.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "docs/GETTING_STARTED.md",
    "docs/CAPABILITIES.md",
    "docs/RELEASE_INTEGRITY.md",
    "docs/UPDATES.md",
    "releases/current.json",
)


def fail(message: str) -> None:
    raise ValueError(message)


def load_catalog() -> dict:
    data = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    if data.get("catalogVersion") != 1:
        fail("releases/current.json must use catalogVersion 1")
    if data.get("product") != "Relay Society":
        fail("release catalog product must be Relay Society")
    if data.get("channel") != "beta" or data.get("prerelease") is not True:
        fail("current catalog must identify the accepted beta prerelease")
    if data.get("automaticExecution") is not False:
        fail("automaticExecution must remain false for the unsigned beta")
    if data.get("signed") is not False:
        fail("current unsigned package status must be explicit")

    tag = data.get("tag")
    version = data.get("version")
    if tag != f"v{version}":
        fail(f"tag {tag!r} does not match version {version!r}")

    release_page = (
        "https://github.com/rookepoole/RelaySociety-Releases/releases/tag/" + tag
    )
    if data.get("releasePage") != release_page:
        fail("releasePage does not match the current tag")
    asset_root = (
        "https://github.com/rookepoole/RelaySociety-Releases/releases/download/" + tag
    )
    if data.get("checksums") != asset_root + "/SHA256SUMS.txt":
        fail("checksums URL does not match the current tag")
    if data.get("updateManifest") != (
        asset_root + f"/relay.update-manifest-{tag}.json"
    ):
        fail("updateManifest URL does not match the current tag")

    platforms = data.get("platforms")
    if not isinstance(platforms, list) or not platforms:
        fail("release catalog must contain at least one platform")

    names: set[str] = set()
    for platform in platforms:
        name = platform.get("file")
        if not isinstance(name, str) or not name:
            fail("each platform requires a file")
        if name in names:
            fail(f"duplicate release filename: {name}")
        names.add(name)
        if not isinstance(platform.get("bytes"), int) or platform["bytes"] <= 0:
            fail(f"invalid byte length for {name}")
        if not SHA256.fullmatch(str(platform.get("sha256", ""))):
            fail(f"invalid lowercase SHA-256 for {name}")
        expected_url = (
            "https://github.com/rookepoole/RelaySociety-Releases/releases/download/"
            f"{tag}/{name}"
        )
        if platform.get("url") != expected_url:
            fail(f"canonical URL mismatch for {name}")
    return data


def validate_release_truth_in_docs(catalog: dict) -> None:
    version = catalog["version"]
    tag = catalog["tag"]
    platform_identity_tokens: list[str] = []
    platform_size_tokens: list[str] = []
    for platform in catalog["platforms"]:
        platform_identity_tokens.extend(
            [platform["file"], platform["sha256"]]
        )
        platform_size_tokens.append(str(platform["bytes"]))

    required_tokens = {
        "README.md": [
            version,
            tag,
            *platform_identity_tokens,
            *platform_size_tokens,
        ],
        "docs/GETTING_STARTED.md": [version, *platform_identity_tokens],
        "docs/RELEASE_INTEGRITY.md": [
            version,
            *platform_identity_tokens,
            *platform_size_tokens,
        ],
        "CHANGELOG.md": [tag],
        "SECURITY.md": [version],
    }
    for filename, tokens in required_tokens.items():
        text = (ROOT / filename).read_text(encoding="utf-8").replace(",", "")
        for token in tokens:
            normalized = token.replace(",", "")
            if normalized not in text:
                fail(f"{filename} is missing current release value: {token}")


def validate_required_files() -> None:
    missing = [name for name in REQUIRED_FILES if not (ROOT / name).is_file()]
    if missing:
        fail("missing required repository files: " + ", ".join(missing))


def validate_markdown_links() -> int:
    checked = 0
    markdown_files = sorted(ROOT.glob("*.md")) + sorted((ROOT / "docs").glob("*.md"))
    for document in markdown_files:
        text = document.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            parsed = urlparse(target)
            if parsed.scheme in {"http", "https", "mailto"} or target.startswith("#"):
                continue
            local_path = unquote(parsed.path)
            if not local_path:
                continue
            resolved = (document.parent / local_path).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                fail(f"{document.relative_to(ROOT)} links outside the repository: {target}")
            if not resolved.exists():
                fail(f"{document.relative_to(ROOT)} has a missing link target: {target}")
            checked += 1
    return checked


def compare_github_release(catalog: dict, metadata_source: str) -> int:
    if metadata_source == "-":
        metadata = json.loads(sys.stdin.read())
    else:
        metadata = json.loads(Path(metadata_source).read_text(encoding="utf-8"))
    if metadata.get("tagName") != catalog["tag"]:
        fail("GitHub release tag does not match releases/current.json")
    if metadata.get("isPrerelease") is not catalog["prerelease"]:
        fail("GitHub prerelease state does not match releases/current.json")

    assets = {asset.get("name"): asset for asset in metadata.get("assets", [])}
    required_support_assets = {
        "SHA256SUMS.txt",
        f"relay.update-manifest-{catalog['tag']}.json",
    }
    missing_support_assets = sorted(required_support_assets - assets.keys())
    if missing_support_assets:
        fail(
            "GitHub release is missing support assets: "
            + ", ".join(missing_support_assets)
        )
    compared = 0
    for platform in catalog["platforms"]:
        name = platform["file"]
        asset = assets.get(name)
        if asset is None:
            fail(f"GitHub release is missing {name}")
        if asset.get("size") != platform["bytes"]:
            fail(f"GitHub byte length mismatch for {name}")
        if asset.get("digest") != "sha256:" + platform["sha256"]:
            fail(f"GitHub digest mismatch for {name}")
        if asset.get("url") != platform["url"]:
            fail(f"GitHub download URL mismatch for {name}")
        compared += 1
    return compared


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--github-release-json")
    args = parser.parse_args()

    validate_required_files()
    catalog = load_catalog()
    validate_release_truth_in_docs(catalog)
    local_links = validate_markdown_links()
    message = f"Repository contract passed: {local_links} local Markdown links"
    if args.github_release_json:
        assets = compare_github_release(catalog, args.github_release_json)
        message += f"; {assets} canonical release assets"
    print(message)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"Repository contract failed: {error}", file=sys.stderr)
        raise SystemExit(1)
