# AkumaOS Design Language

## Vision
AkumaOS strives to create a modern, elegant, and unified desktop experience for Linux power users. By harmonizing aesthetics, performance, and functionality, AkumaOS elevates Wayland desktop compositing into a cohesive environment that feels intuitive, responsive, and visually beautiful out of the box.

---

## Design Philosophy
The core design philosophy of AkumaOS centers around **clarity through minimalism**, **visual hierarchy**, and **context-aware interface elements**. 

1. **Form Follows Function**: Visual flourishes exist to guide user focus, indicate interactability, and provide subtle feedback—never to clutter or distract.
2. **Cohesion Across Components**: Every component—from the bar and application launcher to terminal emulators and notification popups—shares identical visual metrics (spacing, border radii, typography, and animation physics).
3. **Restraint & Precision**: Avoid unnecessary embellishments. Every pixel, margin, and animation curve is intentionally defined.

---

## Apple-Inspired Principles
AkumaOS draws inspiration from modern macOS UI principles, adapting them to the flexibility of Linux window management:
- **Clean Alignment & Symmetry**: Grid-aligned elements with consistent margins across containers.
- **Translucency & Layering**: Depth achieved through soft backdrops, multi-layered interfaces, and subtle elevation rather than harsh lines.
- **Fluid Micro-Interactions**: Direct manipulation feelings created through immediate visual responses and continuous state transitions.

---

## Glassmorphism Usage
Glassmorphism in AkumaOS provides contextual separation between interface layers.
- **Layer Elevation**: Background layers (wallpapers), midground layers (status bar, notifications, launcher), and foreground layers (active windows, modals).
- **Subtle Surface Tinting**: Translucent surfaces use light/dark tinting overlays to maintain legibility against dynamic desktop backgrounds.
- **Border Highlights**: Extremely subtle 1px inner or outer borders with low opacity highlight container edges without creating visual noise.

---

## Blur Guidelines
Blur effects establish spatial depth and separate overlay components from background windows or wallpaper.
- **Primary Overlay Blur**: Medium-to-high Gaussian blur applied behind floating panels, status bars, and notification banners to ensure contrast.
- **Secondary Modal Blur**: Heavy blur applied behind modal overlays and lock screens for deep focus isolation.
- **Performance Thresholds**: Blur radii are constrained to ensure high-frame-rate rendering on both dedicated and integrated GPUs.

---

## Border Radius Standards
Consistent corner rounding softens interface boundaries across all components.
- **Small Containers**: 6px - 8px radius for buttons, tags, tooltips, and badges.
- **Medium Containers**: 12px - 16px radius for status bar widgets, popups, notifications, and launcher cards.
- **Large Containers**: 16px - 24px radius for floating windows, main launcher windows, and lock screen cards.
- **Unified Outer & Inner Radii**: Nested containers dynamically scale inner radii so border gaps remain visually uniform (`inner_radius = outer_radius - padding`).

---

## Shadows
Shadows provide visual elevation and spatial hierarchy between z-index layers.
- **Low Elevation**: Soft, tight shadow for inline buttons, dropdown items, and active widgets.
- **Medium Elevation**: Balanced ambient shadow for status bars, notifications, and floating panels.
- **High Elevation**: Deep, wide diffuse shadow for floating windows, application launchers, and overlay modals.
- **Shadow Tinting**: Ambient shadows leverage subtle color sampling to feel integrated into the active theme rather than flat black.

---

## Typography Guidelines
Typography in AkumaOS emphasizes legibility, clean hierarchy, and geometric harmony.
- **Primary Typeface**: Clean, modern sans-serif font family optimized for screen rendering and system UI.
- **Monospace Typeface**: High-legibility monospace font for terminal emulators, code blocks, and system stats.
- **Font Weight Hierarchy**:
  - **Regular (400)**: Primary body text and descriptive UI labels.
  - **Medium (500)**: Active tab titles, widget headers, and button text.
  - **Semi-Bold (600)**: Window titles, notification headers, and key shortcuts.
- **Scaling System**: Modular font scale ratio ensuring consistent sizing across different display resolutions.

---

## Icon Style
- **Symbolic & Vector-Based**: Clean, minimalist vector icons with uniform stroke weights.
- **Contextual Sizing**: Standardized icon dimensions across bars (16px - 20px), menus (20px - 24px), and notifications (24px - 32px).
- **Unified Metaphors**: Consistent iconography across all system tools and status indicators (battery, network, audio, workspaces).

---

## Animation Philosophy
Animations in AkumaOS are designed to make the interface feel alive without introducing latency.
- **Physics-Based Motion**: Transitions utilize smooth easing curves (spring and cubic-bezier) to simulate natural inertia.
- **Purposeful Transitions**: Animations exist to communicate state changes—such as workspace switching, window opening/closing, and launcher toggling.
- **Duration Guidelines**:
  - **Instant Micro-Interactions**: 100ms - 150ms for hover states and button presses.
  - **Standard Transitions**: 200ms - 300ms for workspace switches and window management.
  - **Modal & Overlay Motion**: 250ms - 350ms for launcher and lock screen reveals.
- **Toggleable Motion**: Motion reduction options for accessibility and low-spec hardware.

---

## Spacing System
Spacing is governed by an 8pt grid system to ensure visual alignment and balance:
- **Base Grid Unit**: 4px micro / 8px macro grid.
- **Padding Metrics**: 4px (tiny), 8px (small), 16px (medium), 24px (large), 32px (extra large).
- **Window Gaps**: Uniform inner and outer gaps for tiled and floating layouts.

---

## Color System
*The AkumaOS color system defines semantic color relationships and dynamic palette structures without hardcoding specific hex values at this phase.*

- **Semantic Color Roles**:
  - **Primary / Accent**: Used for active states, key highlights, and focused controls.
  - **Surface / Neutral**: Used for container backgrounds, panels, and card bases.
  - **Text / Foreground**: High-contrast, medium-contrast, and muted text roles.
  - **System States**: Success, Warning, Error, and Info state colors.
- **Dynamic Theming**: Color palettes are dynamically generated and applied across all component configurations from a centralized theme definition.
- **Contrast Ratios**: All text and icon color pairings maintain WCAG AA compliance for legibility.

---

## Wallpaper Philosophy
Wallpapers in AkumaOS are not passive backgrounds; they anchor the entire visual aesthetic:
- **Tone & Mood Alignment**: Wallpapers guide the active theme palette and glassmorphism backdrop tinting.
- **Curated Categorization**: Abstract, minimal, nature, and anime wallpaper collections matched to theme variants.
- **Focal Points & Composition**: Wallpapers feature balanced compositions that leave central and top regions clean for status bars and desktop UI elements.

---

## Accessibility Considerations
- **High Contrast Support**: Ability to decrease translucency and increase contrast across all UI surfaces.
- **Legible Scale**: Scalable text and icon assets for high-DPI displays.
- **Keyboard Navigation**: Complete keyboard navigability across launcher, notifications, and system controls.
- **Reduced Motion**: Full support for disabling blur and complex window animation physics on demand.
