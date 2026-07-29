# AkumaOS Customization Guide

AkumaOS is designed to be easily customizable while maintaining a cohesive visual language. This guide documents the planned customization architecture and configuration points.

---

## Wallpapers

### Managing Wallpaper Collections
Wallpapers are stored in categorized subdirectories under `wallpapers/`:
- `wallpapers/anime/`
- `wallpapers/minimal/`
- `wallpapers/nature/`
- `wallpapers/abstract/`

### Changing Wallpapers
Custom wallpapers can be added to any category folder. The wallpaper management script (`scripts/wallpaper.sh`) handles dynamic switching and applies appropriate background effects.

---

## Themes

### Visual Themes
Themes define overall color schemes, translucency levels, and visual tokens.
- Theme definitions reside in `themes/`.
- Switch themes using central management scripts to update all desktop components simultaneously.

---

## Fonts

### Typography Customization
System UI fonts and terminal monospace fonts are configured globally across UI components:
- UI Sans-Serif Font: Configured in Waybar, Wofi, and Hyprland window decorations.
- Terminal Monospace Font: Configured in Ghostty terminal settings.

---

## Keybinds

### Customizing Shortcuts
Keybindings are declared centrally within the Hyprland configuration (`config/hypr/`):
- Application Spawners: Workspace navigation, terminal, launcher, file manager.
- Window Management: Focus movement, tiling, floating toggles, resizing.
- Media & System Controls: Volume, brightness, media playback, screenshot utilities.

---

## Colors

### Color Scheme Overrides
The color system supports both predefined themes and user-defined color overrides:
- Accent Colors: Active window borders, active workspace indicators, button highlights.
- Background Colors: Translucent surface layers, status bar backgrounds, launcher cards.

---

## Animations

### Motion & Easing Adjustment
Window management animations and workspace transitions can be tuned in the compositor configuration:
- Animation Speed: Adjust duration for workspace sliding, window fading, and scale effects.
- Easing Curves: Configure spring and bezier curves for custom motion feel.
- Reduced Motion Mode: Option to disable complex animations for performance optimization.

---

## Modules

### Status Bar & Panel Modules
Waybar modules (`config/waybar/`) can be customized, rearranged, or extended:
- Custom Scripts: Add custom shell scripts for system monitoring or news feeds.
- Module Placement: Move modules between left, center, and right bar sections.
