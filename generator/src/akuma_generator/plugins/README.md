# Generator Plugins Subsystem (`plugins/`)

## Overview
The plugins subsystem decouples component-specific configuration generators (Hyprland, Waybar, Ghostty, Wofi, Hyprlock, Hypridle, Mako) into isolated, modular plugin packages.

## Plugin Structure
Each plugin resides in its own directory under `plugins/` and implements component-specific generation methods using the core parser, loader, validator, and renderer utilities in `akuma_generator.core`.

## Available Plugins
- `hypr/`: Hyprland compositor plugin (monitors, window rules, keybindings, animations).
- `waybar/`: Waybar status bar layout and CSS generator plugin.
- `ghostty/`: Ghostty terminal emulator styling and configuration plugin.
- `wofi/`: Wofi application launcher menu generator plugin.
- `hyprlock/`: Hyprlock screen locker layout generator plugin.
- `hypridle/`: Hypridle session idle daemon configuration plugin.
- `mako/`: Mako notification daemon styling plugin.
