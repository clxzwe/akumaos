# Blur Design Tokens

## Purpose
Blur design tokens define backdrop translucency and Gaussian blur metrics. Standardizing blur passes and blur radii across Wayland compositors and UI daemons enables glassmorphic transparency while maintaining text contrast and background isolation.

---

## Naming Conventions

Blur tokens follow a scale and parameter notation:
`blur.radius.<scale>`, `blur.passes`, and `blur.vibrancy`

### Blur Radius Tokens
- `blur.radius.off`: No blur applied (0px).
- `blur.radius.light`: Subtle background softening for status bar modules and tooltips.
- `blur.radius.medium`: Balanced glassmorphic blur for notifications, launchers, and sidebars.
- `blur.radius.heavy`: Deep background isolation for floating modals and lock screens.

### Quality Parameters
- `blur.passes`: Number of blur computation passes for smooth Gaussian rendering.
- `blur.noise`: Subtle noise grain parameter to eliminate color banding on translucent surfaces.
- `blur.vibrancy`: Color saturation boost applied to background pixels under blurred layers.

---

## Usage Guidelines

1. **Legibility Protection**: Always pair blurred backdrops with semi-transparent tint layers (`color.bg.surface`) to ensure high contrast against dynamic wallpaper elements.
2. **Performance Constraints**: Limit blur passes (`blur.passes`) on integrated GPUs to prevent frame drops during window animations.
3. **Toggle Support**: Allow global disabling of blur tokens via user preference or battery saver modes.

---

## Component Examples

| Component | Target Element | Token Mapping Example |
|---|---|---|
| **Hyprland** | Window Blur Decoration | `blur.radius.medium` |
| **Waybar** | Status Bar Backdrop Blur | `blur.radius.light` |
| **Wofi** | Launcher Window Blur | `blur.radius.medium` |
| **Hyprlock** | Lock Screen Wallpaper Blur | `blur.radius.heavy` |
| **Mako** | Notification Backdrop Blur | `blur.radius.medium` |
