# Installation Test Suite

## Purpose
This directory is reserved for integration tests, installer validation scripts, and dry-run environment testing.

## Planned Test Coverage
- **Idempotency Testing**: Verifying that running `scripts/install.sh` multiple times produces consistent, non-destructive results.
- **Backup Integrity**: Testing that pre-existing user configuration files in `~/.config/` are safely archived to `~/.config-backups/` prior to installation.
- **Dependency Checking**: Validating pre-flight script logic against missing system packages and Wayland environment prerequisites.
- **Uninstall Verification**: Testing `scripts/uninstall.sh` to ensure clean restoration of original system configurations.
