# AkumaOS Installation Guide

This document outlines the planned installation procedures, system requirements, and setup phases for AkumaOS.

> **Note**: Automated installation scripts are currently under development. Detailed execution commands will be published upon completion of milestone [v0.8 Automated Installer](roadmap.md#milestone-v08--automated-installer--tooling).

---

## System Requirements

### Supported Operating System
- Linux distribution running Wayland session (Arch Linux recommended).

### Required Dependencies
- Wayland Compositor: `hyprland`
- Status Bar: `waybar`
- Application Launcher: `wofi`
- Terminal Emulator: `ghostty`
- Screen Locker & Idle Daemon: `hyprlock`, `hypridle`
- Notification Daemon: `mako`
- On-Screen Display: `swayosd`
- Core Utilities: `bash`, `git`

---

## Installation Phases

### Phase 1: Pre-Installation Check
- Verify Wayland display server compatibility.
- Ensure all required binary packages are installed on the host system.

### Phase 2: Repository Clone
- Clone the official AkumaOS repository to your local machine.

### Phase 3: Configuration Backup
- Backup pre-existing user configurations located in `~/.config/` to prevent data loss.

### Phase 4: Automated Setup
- Run the installer script (`scripts/install.sh`) to establish configuration symlinks.

### Phase 5: Post-Installation & Verification
- Log out of your current session.
- Select Hyprland from your display manager and launch AkumaOS.
