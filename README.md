# AkumaOS

![AkumaOS Banner](assets/previews/banner.png)

AkumaOS is an open-source, highly polished Linux desktop environment designed for performance, aesthetics, and modern workflow efficiency on Wayland.

---

## Project Philosophy

AkumaOS is built on three core principles:

1. **Visual Excellence & Cohesion**: Every component—from the window manager and status bar to notifications and launchers—shares a unified design language inspired by modern glassmorphism and clean typography.
2. **Modular Architecture**: Complete separation between visual styling, system configurations, and management scripts.
3. **Out-of-the-Box Usability**: Provide an intuitive, beautiful desktop environment that requires minimal manual setup while remaining fully customizable.

---

## Goals

- Create a seamless, high-performance Wayland environment powered by Hyprland.
- Establish an integrated theme and wallpaper system with real-time switching capabilities.
- Provide a non-destructive, safe installation and backup utility suite.
- Maintain comprehensive documentation for users and contributors.

---

## Current Development Status

> **Status**: Phase 2 — Product Architecture & Planning

AkumaOS is actively undergoing architecture definition and structural planning. Component configurations and installation scripts will be implemented according to the [Milestone Roadmap](docs/roadmap.md).

---

## Planned Features

- [ ] **Compositor**: Custom Hyprland window management, animations, and keybindings
- [ ] **Status Bar**: Modular Waybar layout with glassmorphic styling
- [ ] **Application Launcher**: Fast, keyboard-driven Wofi menu
- [ ] **Terminal**: Custom-styled Ghostty terminal emulator
- [ ] **Lock Screen & Idling**: Hyprlock and Hypridle integration
- [ ] **Notifications**: Sleek Mako notification daemon styling
- [ ] **On-Screen Display**: SwayOSD volume and brightness indicators
- [ ] **Wallpaper Engine**: Multi-category wallpaper switcher script
- [ ] **Automated Tooling**: Non-destructive installer and updater scripts

---

## Repository Structure

```text
AkumaOS/
├── .github/              # Issue templates, PR templates, and CI workflows
├── assets/               # Branding assets, icons, previews, and screenshots
├── config/               # Compositor, bar, launcher, and daemon configurations
├── docs/                 # Product architecture, design system, installation & roadmap
│   └── images/           # Documentation images, diagrams, and screenshots
├── scripts/              # System management, installation, and utility scripts
├── themes/               # Centralized theme definitions and color palettes
└── wallpapers/           # Curated wallpaper collections (minimal, abstract, nature, anime)
```

---

## Documentation

Explore the complete AkumaOS specifications:

- 🎨 [Design Language](docs/design-language.md) — Visual principles, typography, blur, and spacing guidelines.
- 🏗️ [Architecture Blueprint](docs/architecture.md) — Technical structure, configuration flow, and component diagrams.
- 🗺️ [Milestone Roadmap](docs/roadmap.md) — Planned development stages from v0.1 to v1.0.
- 🛠️ [Installation Guide](docs/installation.md) — Prerequisites, system requirements, and setup overview.
- ⚙️ [Customization Guide](docs/customization.md) — Planned customization points for themes, fonts, and keybinds.

---

## Contributing

We welcome contributions! Please review our [Contributing Guide](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) before submitting pull requests.

---

## License

This project is licensed under the [MIT License](LICENSE).
