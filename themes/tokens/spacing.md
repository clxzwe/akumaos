# Spacing Design Tokens

## Purpose
Spacing design tokens establish a consistent 8pt/4pt grid system across all AkumaOS desktop components. Standardizing margins, paddings, and window gaps ensures visual balance and harmonious layout metrics across tiling windows, floating panels, and bar widgets.

---

## Naming Conventions

Spacing tokens follow a structured notation:
`space.<scale>` and `gap.<context>`

### Scale Tokens
- `space.3xs`: Micro spacing for tight element offsets (e.g., icon-to-badge gaps).
- `space.2xs`: Extra small spacing for dense list items and inline chips.
- `space.xs`: Small spacing for inner button padding and compact widget margins.
- `space.sm`: Standard internal padding for list items and widget containers.
- `space.md`: Default padding for cards, popups, and status bar modules.
- `space.lg`: Generous padding for floating panels and launcher containers.
- `space.xl`: Structural spacing for major container sections.
- `space.2xl`: Macro layout spacing for lock screen cards and main dialog windows.

### Layout Gap Tokens
- `gap.window.inner`: Inner gap distance between adjacent tiled windows.
- `gap.window.outer`: Outer gap distance between windows and screen edges.
- `gap.bar.module`: Spacing between individual Waybar status bar modules.
- `gap.launcher.item`: Vertical spacing between Wofi list items.

---

## Usage Guidelines

1. **Grid Alignment**: All spatial measurements must be multiples of the base grid unit (4px micro / 8px macro).
2. **Component Symmetry**: Ensure inner padding and outer gaps remain visually proportional across container hierarchies.
3. **Responsive Scaling**: Gap metrics scale proportionally when switching between single-monitor laptop displays and high-resolution desktop monitors.

---

## Component Examples

| Component | Target Element | Token Mapping Example |
|---|---|---|
| **Hyprland** | Window Tiling Inner Gap | `gap.window.inner` |
| **Hyprland** | Screen Edge Outer Gap | `gap.window.outer` |
| **Waybar** | Module Internal Padding | `space.sm` |
| **Waybar** | Module Separation | `gap.bar.module` |
| **Wofi** | Window Outer Padding | `space.lg` |
| **Wofi** | Result Item Spacing | `gap.launcher.item` |
| **Ghostty** | Window Margin & Padding | `space.md` |
| **Mako** | Notification Card Padding | `space.md` |
