# Contributing

Thank you for helping make Relay Society understandable, verifiable, and usable.

## Repository scope

This public repository is currently the official release and documentation channel. It is not yet the complete Relay Society development source tree. Useful contributions include:

- corrections to setup, security, update, and recovery documentation;
- reproducible packaging or runtime bug reports;
- accessibility and usability reports;
- release-catalog validation improvements;
- clear feature proposals grounded in an end-user outcome.

Do not submit reverse-engineered or reconstructed application source and represent it as authoritative Relay Society source.

## Before contributing

- Search existing issues and pull requests.
- Use the current accepted beta when reporting product behavior.
- Keep one issue or pull request focused on one outcome.
- Remove every token, credential, invitation, bearer, recovery value, and private task detail.
- For vulnerabilities, follow [SECURITY.md](SECURITY.md) and report privately.

## Documentation pull requests

1. Create a focused branch from `main`.
2. Preserve evidence boundaries; do not turn partial or planned work into an unqualified feature claim.
3. Keep release filenames, byte lengths, digests, tag URLs, and schema values synchronized.
4. Run:

   ```sh
   python scripts/verify_repository.py
   ```

5. Explain what changed, why it is accurate, and how it was verified.

## Release-maintenance contract

Every accepted release should update, in the same reviewed change:

- the GitHub release page and immutable assets;
- `releases/current.json`;
- the README download and quick-start sections;
- release-specific setup and integrity values;
- `CHANGELOG.md`;
- supported-version statements in `SECURITY.md`;
- any capability or boundary changed by the release.

Repository checks compare `releases/current.json` with the real GitHub release assets so a stale filename, byte length, digest, tag, or URL fails the change.

## License

By contributing, you agree that your contribution is licensed under the repository's [Apache License 2.0](LICENSE).
