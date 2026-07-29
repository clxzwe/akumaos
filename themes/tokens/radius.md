# Corner Radius Design Tokens

## Purpose
Corner radius design tokens define the curvature metrics for container boundaries across AkumaOS. Standardizing corner radii ensures consistent softening of interface boundaries across window managers, popups, launchers, notifications, and status bar modules.

---

## Naming Conventions

Radius tokens follow a scale notation:
`radius.<scale>` and `radius.context.<role>`

### Scale Tokens
- `radius.none`: Sharp rectangular corners (0px).
- `radius.xs`: Micro curvature for tags, tooltips, and small badges.
- `radius.sm`: Small curvature for buttons, input fields, and inline controls.
- `radius.md`: Medium curvature for status bar widgets, popups, and dropdown menus.
- `radius.lg`: Large curvature for floating windows, notification cards, and launcher frames.
- `radius.xl`: Extra-large curvature for lock screen cards and major dialog overlays.
- `radius.full`: Fully rounded pill shapes for workspace indicators and toggle switches.

---

## Usage Guidelines

1. **Hierarchy Scaling**: Match corner radius scale to container size (smaller elements use `radius.sm`, larger containers use `radius.lg`).
2. **Nested Curvature Match**: When nesting rounded containers, calculate inner radius to maintain uniform visual border width (`inner_radius = outer_radius - padding`).
3. **Compositor Alignment**: Match Hyprland window rounding (`radius.lg`) with floating launcher boundaries for a seamless desktop experience.

---

## Component Examples

| Component | Target Element | Token Mapping Example |
|---|---|---|
| **Hyprland** | Window Decoration Rounding | `radius.lg` |
| **Waybar** | Bar Module Pill Shape | `radius.full` |
| **Waybar** | Popup Menu Corners | `radius.md` |
| **Wofi** | Outer Window Frame | `radius.lg` |
| **Wofi** | Input Field Corners | `radius.sm` |
| **Hyprlock** | Password Input Box | `radius.md` |
| **Mako** | Notification Banner | `radius.lg` |
