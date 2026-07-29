# Animation Design Tokens

## Purpose
Animation design tokens specify duration metrics and easing curves for interface transitions. Establishing standardized motion physics ensures that window management, workspace sliding, popup reveals, and hover states feel responsive, continuous, and natural across all AkumaOS components.

---

## Naming Conventions

Animation tokens follow a property and role structure:
`anim.duration.<scale>` and `anim.curve.<type>`

### Duration Tokens
- `anim.duration.instant`: Micro interaction feedback (e.g., button click / hover state).
- `anim.duration.fast`: Quick UI element transitions (e.g., tooltip reveal / tab switch).
- `anim.duration.normal`: Standard window management and workspace transitions.
- `anim.duration.slow`: Complex modal reveals, launcher slide-ins, and lock screen transitions.

### Easing Curve Tokens
- `anim.curve.linear`: Constant rate motion for progress indicators.
- `anim.curve.ease_in_out`: Smooth acceleration and deceleration for panel slides.
- `anim.curve.spring`: Inertia-based spring curve with subtle overshoot for floating window popups.
- `anim.curve.decelerate`: Sharp entry with smooth deceleration for application launchers.

---

## Usage Guidelines

1. **Responsiveness First**: Keep micro-interaction durations (`anim.duration.instant`) under 150ms to ensure the desktop feels immediate and lag-free.
2. **Physics Uniformity**: Use `anim.curve.spring` consistently across Hyprland window open transitions and Wofi launcher slide-ins.
3. **Accessibility**: Respect system-wide reduced motion settings by setting animation durations to zero when enabled.

---

## Component Examples

| Component | Target Element | Token Mapping Example |
|---|---|---|
| **Hyprland** | Window Open / Close | `anim.duration.normal` / `anim.curve.spring` |
| **Hyprland** | Workspace Switch Slide | `anim.duration.normal` / `anim.curve.ease_in_out` |
| **Waybar** | Module Hover State | `anim.duration.instant` / `anim.curve.linear` |
| **Wofi** | Launcher Slide-In Reveal | `anim.duration.slow` / `anim.curve.decelerate` |
| **Mako** | Notification Banner Slide | `anim.duration.fast` / `anim.curve.spring` |
