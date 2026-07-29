# Color Design Tokens

## Purpose
The color token specification provides a semantic, system-wide color taxonomy. By referencing abstract semantic tokens rather than hardcoded hex values, all AkumaOS desktop components (Hyprland, Waybar, Wofi, Ghostty, Hyprlock, Mako) achieve unified color management and seamless theme swapping.

---

## Naming Conventions

Color tokens follow a hierarchical dot-notation structure:
`color.<category>.<role>.<variant>`

### Categories & Semantic Roles
- `color.bg.base`: Primary surface background for application windows and panels.
- `color.bg.surface`: Secondary surface background for cards, popups, and widgets.
- `color.bg.floating`: Elevated surface background for floating windows, launchers, and modals.
- `color.accent.primary`: Main brand accent color for active states, key focus, and active window borders.
- `color.accent.secondary`: Secondary accent color for supplementary highlights and active indicators.
- `color.fg.primary`: Primary text and high-contrast foreground element color.
- `color.fg.secondary`: Medium-contrast text color for subheadings and secondary labels.
- `color.fg.muted`: Muted color for disabled controls, placeholders, and subtle icons.
- `color.border.active`: Active window or focused container border color.
- `color.border.inactive`: Inactive container or subtle divider border color.
- `color.status.info`: Informational state color.
- `color.status.success`: Success or confirmation state color.
- `color.status.warning`: Warning or caution state color.
- `color.status.error`: Critical error or alert state color.

---

## Usage Guidelines

1. **Semantic Selection**: Always choose token names based on UI intent rather than literal color names (e.g., use `color.accent.primary` instead of `blue`).
2. **Contrast Standards**: Foreground tokens paired with background tokens must meet WCAG AA legibility standards.
3. **Consistency**: Use `color.border.active` consistently across Hyprland active borders, Wofi active selections, and Waybar focused workspace buttons.

---

## Component Examples

| Component | Target Element | Token Mapping Example |
|---|---|---|
| **Hyprland** | Active Window Border | `color.border.active` |
| **Hyprland** | Inactive Window Border | `color.border.inactive` |
| **Waybar** | Bar Background | `color.bg.base` |
| **Waybar** | Active Workspace Pill | `color.accent.primary` |
| **Wofi** | Launcher Input Field | `color.bg.surface` |
| **Wofi** | Selected Item Text | `color.fg.primary` |
| **Ghostty** | Background / Foreground | `color.bg.base` / `color.fg.primary` |
| **Hyprlock** | Password Prompt Card | `color.bg.floating` |
| **Mako** | Urgent Notification Border | `color.status.error` |
