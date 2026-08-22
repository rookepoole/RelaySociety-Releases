# Updates, rollback, and the release channel

## Update policy

Relay Society beta updates are manual and user-confirmed. The v0.3.80 runtime does not silently download or execute a replacement.

GitHub Releases is the canonical binary store. The mutable [`releases/current.json`](../releases/current.json) catalog helps humans and repository checks find the current tag. Every tag also carries an immutable version-specific update manifest.

## Before upgrading

1. Run `relay-society backup` using the currently installed binary.
2. Run `relay-society verify-backup --from PATH`.
3. Create and separately retain a matching portable vault recovery package.
4. Stop Relay cleanly.
5. Preserve the current application folder and verified backup.

The normal backup does not contain the Windows Credential Manager or Linux Secret Service master-key item. Portable recovery material is required when moving to a different machine or OS identity.

## Install the new version

1. Open the new version's GitHub release page.
2. Read its release notes and boundaries.
3. Download the package into a new folder.
4. Verify the complete byte length and SHA-256 digest.
5. Extract or install without overwriting the prior versioned application folder.
6. Launch the new version against the existing data location.
7. Run `relay-society doctor`.
8. Verify at least one existing signed receipt.
9. Exercise a non-consequential governed task before relying on consequential workflows.

SQLite migrations are numbered and transactional. A binary older than the current data schema refuses to open it.

The exact v0.3.71/schema-40 to v0.3.72/schema-41 adjacent migration and v0.3.72-to-v0.3.73 same-schema upgrade remain qualified. The exact v0.3.73/schema-41 to v0.3.75/schema-43 migration and v0.3.75/schema-43 to v0.3.76/schema-44 migration install the cultural schemas transactionally. The v0.3.76-to-v0.3.77 same-schema upgrade, v0.3.77/schema-44 to v0.3.78/schema-45 migration, v0.3.78/schema-45 to v0.3.79/schema-46 migration, and v0.3.79/schema-46 to v0.3.80/schema-47 migration are qualified on Windows Credential Manager and Linux Secret Service. These paths preserve canonical task, event, artifact, receipt, settlement, culture, specialization, provider, schedule, and credential-custody state, verify the prior receipt, and pass authenticated backup/restore plus post-restore diagnostics. This evidence does not replace the user's own backup.

## Rollback

If the new version has not upgraded the data schema, stop it and relaunch the preserved prior application folder.

If the data schema changed, do not force an older binary to open newer data. Restore the verified pre-upgrade backup using the matching older binary and retain the newer data copy for investigation.

## Manifest behavior

The current beta channel uses:

- channel: `beta`;
- confirmation mode: manual/user-confirmed;
- automatic execution: false;
- canonical asset URLs: immutable GitHub release assets;
- package verification: exact SHA-256 and byte length.

Future signed update work must preserve explicit user confirmation, safe rollback, version/schema compatibility checks, and fail-closed verification before any installer or replacement runs.
