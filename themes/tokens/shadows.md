# Shadow Design Tokens

## Purpose
Shadow design tokens define elevation and spatial depth across desktop interface layers. By specifying ambient and directional shadow metrics, AkumaOS components establish clear z-axis hierarchy between background wallpapers, tiling windows, status bars, and floating overlay modals.

---

## Naming Conventions

Shadow tokens follow an elevation-based structure:
`shadow.elevation.<level>` and `shadow.color.<role>`

### Elevation Tokens
- `shadow.elevation.none`: Flat rendering without elevation or drop shadow.
- `shadow.elevation.low`: Subtle elevation for inline buttons, active pills, and hover states.
- `shadow.elevation.medium`: Medium elevation for status bars, notification popups, and dropdown menus.
- `shadow.elevation.high`: High elevation for floating windows, application launchers, and overlay dialogs.
- `shadow.elevation.max`: Maximum depth elevation for lock screen cards and critical system alerts.

---

## Usage Guidelines

1. **Layer Hierarchy**: Reserve higher elevation shadows (`shadow.elevation.high`) exclusively for elements that float above the main window layer.
2. **Cohesive Light Source**: All drop shadows imply a uniform top-down ambient light source across components.
3. **Performance Optimization**: Disable high-elevation shadows on lower-spec hardware configurations when requested by power-saving modes.

---

## Component Examples

| Component | Target Element | Token Mapping Example |
|---|---|---|
| **Hyprland** | Floating Window Drop Shadow | `shadow.elevation.high` |
| **Waybar** | Status Bar Elevation | `shadow.elevation.medium` |
| **Wofi** | Launcher Container Shadow | `shadow.elevation.high` |
| **Hyprlock** | Center Auth Box Elevation | `shadow.elevation.max` |
| **Mako** | Notification Card Shadow | `shadow.elevation.medium` |
