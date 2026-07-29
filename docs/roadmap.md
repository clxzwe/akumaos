# AkumaOS Milestone Roadmap

This roadmap outlines the planned development milestones for AkumaOS from initial repository scaffolding to the v1.0 stable release.

---

## Milestone v0.1 — Repository Bootstrap (Completed)

### Goals
Establish the official repository architecture, project standards, documentation framework, and CI linting pipelines.

### Deliverables
- Initial repository layout (`config/`, `scripts/`, `docs/`, `assets/`, `themes/`, `wallpapers/`).
- Standard project governance files (`LICENSE`, `README.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`).
- Repository configuration files (`.editorconfig`, `.gitignore`, `.github/workflows/lint.yml`).
- Scaffolding for documentation suite.

### Exit Criteria
- Clean directory layout committed and pushed to `main`.
- All baseline governance documents and CI workflows validated.

---

## Milestone v0.2 — Design Token Foundation (Completed)

### Goals
Define abstract, reusable design token specifications across colors, spacing, typography, corner radii, shadows, blur, and animations before component implementation begins.

### Deliverables
- Design token specification suite (`themes/tokens/colors.md`, `spacing.md`, `typography.md`, `radius.md`, `shadows.md`, `blur.md`, `animations.md`).
- Default theme package directory (`themes/default/`).
- Test suite structure (`tests/config/`, `tests/install/`).
- Developer tooling scripts (`tools/validate.sh`, `tools/format.sh`).

### Exit Criteria
- Abstract token specifications fully documented with usage guidelines and component mappings.
- Architecture blueprint updated to reflect testing, tools, and token structures.

---

## Milestone v0.3 — Hyprland Core

### Goals
Build the foundational Hyprland compositor configuration focused on window management, input rules, monitor layouts, and keybindings based on design token standards.

### Deliverables
- Core Hyprland configuration structure (`config/hypr/`).
- Default window rules, workspace rules, and layout settings.
- Essential keybinding map (window control, workspace switching, application execution).
- Multi-monitor auto-configuration logic.

### Exit Criteria
- Smooth Hyprland session startup without syntax errors.
- Fully functional workspace and window management controls.

---

## Milestone v0.4 — Waybar Status Bar

### Goals
Design and configure a modular status bar using Waybar that aligns with the AkumaOS design language and token metrics.

### Deliverables
- Waybar layout and styling configuration (`config/waybar/`).
- Essential modules (workspaces, active window title, clock, battery, network, audio volume, system tray).
- Custom CSS styling implementing glassmorphism and rounded container standards.

### Exit Criteria
- Waybar renders smoothly on session start.
- Modules reflect accurate real-time system state.

---

## Milestone v0.5 — Application Launcher (Wofi)

### Goals
Implement a fast, keyboard-driven application launcher and menu system using Wofi.

### Deliverables
- Wofi configuration and CSS theme (`config/wofi/`).
- Application runner mode, window switcher mode, and custom action menu.
- Smooth transition animations and keybinding integration with Hyprland.

### Exit Criteria
- Launcher opens instantly on hotkey activation.
- Search and application launching work cleanly without visual artifacts.

---

## Milestone v0.6 — Wallpaper Engine

### Goals
Construct a wallpaper management system capable of background setting, collection switching, and visual synchronization.

### Deliverables
- Curated wallpaper collections (`wallpapers/anime/`, `wallpapers/minimal/`, `wallpapers/nature/`, `wallpapers/abstract/`).
- Executable wallpaper switcher script (`scripts/wallpaper.sh`).
- Integration with Wayland wallpaper daemons.

### Exit Criteria
- Seamless wallpaper transitions without screen flickering.
- Wallpapers correctly persist across reboot cycles.

---

## Milestone v0.7 — Screen Lock & Power Management (Hyprlock & Hypridle)

### Goals
Provide secure screen locking, session idling, and power management integrated with the desktop design system.

### Deliverables
- Hyprlock lock screen layout (`config/hyprlock/`).
- Hypridle daemon configuration (`config/hypridle/`) for screen dimming, locking, and suspend triggers.
- Visual alignment with active wallpaper and theme styles.

### Exit Criteria
- Screen locks cleanly upon idle timeout or manual hotkey invocation.
- System unlocks reliably with user credentials.

---

## Milestone v0.8 — Terminal Emulator (Ghostty)

### Goals
Integrate Ghostty as the default terminal emulator with matching typography, padding, and color schemes.

### Deliverables
- Ghostty configuration (`config/ghostty/`).
- Custom color theme matching AkumaOS visual language.
- Keybindings for quick terminal spawning.

### Exit Criteria
- Terminal opens with correct font metrics, transparency, and padding.
- High performance rendering verified.

---

## Milestone v0.9 — Automated Installer & Tooling

### Goals
Build a reliable, user-friendly installation and update utility suite.

### Deliverables
- Automated installer (`scripts/install.sh`).
- Backup and restore logic for existing user configurations.
- Update script (`scripts/update.sh`) and bootstrap utility (`scripts/bootstrap.sh`).

### Exit Criteria
- Installation script executes cleanly on target Arch/Linux systems.
- Existing user files are backed up safely prior to deployment.

---

## Milestone v1.0 — Stable Release

### Goals
Publish the official v1.0 release of AkumaOS desktop environment.

### Deliverables
- Tagged v1.0 release on GitHub.
- Finalized installation script and documentation suite.
- Official release announcement and screenshots showcase.

### Exit Criteria
- All previous milestone deliverables fully merged and verified.
- Production-ready stability and performance.
