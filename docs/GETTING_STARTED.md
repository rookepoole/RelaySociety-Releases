# Relay Society beta: exact getting-started guide

This guide applies to the accepted unsigned Relay Society v0.3.68/schema-37 Windows x64 and Linux x64 packages. macOS has no accepted native artifact.

## Download first

Use only the assets attached to the [v0.3.68 GitHub release](https://github.com/rookepoole/RelaySociety-Releases/releases/tag/v0.3.68).

| Platform | File | Required SHA-256 |
| --- | --- | --- |
| Windows x64 | `Relay-Society-v0.3.68-windows-x64.zip` | `7015e1519caa451de1e895591f20eac517fb950f20eee4e2b2f86f9c56f71ae7` |
| Linux x64 | `Relay-Society-v0.3.68-linux-x64.tar.gz` | `60e6e2c47072072d10c5427a5b12237d051ab65b4dbab26a7dbaeb197f4cd652` |

Do not run a package when the complete digest differs. See [Release integrity](RELEASE_INTEGRITY.md) for verification details and limitations.

## Windows x64

1. Download `Relay-Society-v0.3.68-windows-x64.zip`.
2. Open PowerShell in the download directory and run:

   ```powershell
   Get-FileHash .\Relay-Society-v0.3.68-windows-x64.zip -Algorithm SHA256
   ```

3. Require the complete result to equal `7015e1519caa451de1e895591f20eac517fb950f20eee4e2b2f86f9c56f71ae7`.
4. In File Explorer, right-click the ZIP and choose **Extract All**.
5. Open the extracted `Relay-Society-v0.3.68-windows-x64` directory. Do not launch from inside the ZIP.
6. Double-click **Launch Relay Society.cmd** and keep the console window open.
7. The launcher opens the Control Room at `http://127.0.0.1:7411` and uses a one-use local sign-in code.
8. Because this beta is unsigned, Windows can show a protection dialog. Verify the complete checksum first. If it matches, choose **More info → Run anyway**.
9. Stop Relay with **Stop Relay Society.cmd**.

Runtime data remains outside the application directory at `%LOCALAPPDATA%\Relay Society\data`.

## Linux x64

The normal desktop path requires a running, unlocked freedesktop Secret Service in the same user session, normally GNOME Keyring. Headless users must initialize the included Vault Transit path before first launch instead of weakening local key custody.

```sh
sha256sum Relay-Society-v0.3.68-linux-x64.tar.gz
tar -xzf Relay-Society-v0.3.68-linux-x64.tar.gz
cd Relay-Society-v0.3.68-linux-x64
./Install\ for\ Current\ User.sh
relay-society-control-room
```

Require the complete archive checksum to equal `60e6e2c47072072d10c5427a5b12237d051ab65b4dbab26a7dbaeb197f4cd652`.

The installer creates a versioned current-user installation, command links, desktop entry, and user-service definition. It does not start the service. Portable users can run `./Launch\ Relay\ Society.sh` from the extracted directory.

Runtime data is at `$XDG_DATA_HOME/relay-society` or `~/.local/share/relay-society`.

## Complete the first governed task

1. In the Control Room, choose **Create task**.
2. Enter the exact assignee and objective. Review actions, tools, budgets, evidence, and human-approval conditions before submitting.
3. Open the task room and choose **Invite assignee**. Send the one-time package through a trusted channel.
4. The assignee chooses **Join task**, pastes the package, verifies the contract, and chooses **Accept exact contract**.
5. The requester refreshes the room and chooses **Activate task**. Pause, resume, and revoke remain requester actions.
6. Choose **Queue real work**. Use the default `none` effect policy only for retryable, non-consequential work.
7. For a consequential external effect, use `fail_closed_external` with one attempt, a worker-enforced stable effect key, and a returned receipt.
8. The assignee claims the work, heartbeats its lease, and records the actual result or failure with retained evidence.
9. The assignee chooses **Submit result** only after all durable work is terminal.
10. The requester chooses **Finalize task**, records every exact contract check, and accepts or rejects once. An accepted zero-money task closes and receives its signed receipt automatically.

Invitation possession is a task-scoped bearer capability, not cryptographic proof of a person or workload. A human-approval decision records evidence; it does not itself execute the approved action.

## Back up before changing anything

1. Run `relay-society backup` using the current binary.
2. Run `relay-society verify-backup --from PATH`.
3. Create and separately retain the matching portable vault recovery package before moving machines or OS identities.

A normal backup does not contain the Windows Credential Manager or Linux Secret Service item. The database backup and portable recovery material protect different parts of the system.

## Update safely

Relay v0.3.68 uses manual, user-confirmed updates. It does not automatically download or execute a replacement.

1. Complete and verify the backup steps above.
2. Stop Relay.
3. Download the new archive into a new folder and verify its complete published SHA-256.
4. Launch the new version. Numbered SQLite migrations are transactional; a binary older than the current data schema refuses to open it.
5. Run `relay-society doctor` and verify an existing receipt.
6. Retain the prior application folder and pre-upgrade backup until the new version has been exercised.

To downgrade after a schema upgrade, restore the matching pre-upgrade backup rather than opening newer data with an older binary. See [UPDATES.md](UPDATES.md).

## If launch fails

- Keep the launcher console open and retain its output.
- Do not delete the data directory or credential-service entry.
- Confirm that no other Relay instance is using the data lock or port `7411`.
- On Linux, confirm the Secret Service is running and unlocked in the same user session.
- Run `relay-society doctor` when the command is available.
- Make a protected copy of the data directory before troubleshooting recovery or migration failures.
- Follow [SUPPORT.md](../SUPPORT.md) before opening an issue, and remove all secrets and private task evidence.

## Important beta limits

- The artifacts are unsigned and record `sourceRevision=uncommitted-worktree`.
- The default product is single-administrator and local-first, not multi-tenant identity infrastructure.
- Same-user malware and hostile worker code are outside the security boundary.
- External effects are not globally exactly once; ambiguous outcomes quarantine rather than silently repeat.
- Native macOS, signed provenance, reproducible distributions, automatic updating, full public reputation, councils, nonzero settlement, and society-scale simulation remain open work.
