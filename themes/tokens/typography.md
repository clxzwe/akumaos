# Typography Design Tokens

## Purpose
Typography design tokens define font families, font sizes, weights, and line heights. Standardizing typographic metrics guarantees high legibility, clean visual hierarchy, and unified font rendering across UI labels, status bars, launchers, and terminal emulators.

---

## Naming Conventions

Typography tokens are categorized by property:
`font.<property>.<role>`

### Font Family Tokens
- `font.family.ui`: Primary sans-serif font family for system interface labels and panels.
- `font.family.mono`: Monospace font family for code editors, terminal sessions, and system stats.

### Font Size Tokens
- `font.size.xs`: Caption, micro tags, and status bar badges.
- `font.size.sm`: Secondary UI labels, list subtext, and timestamp displays.
- `font.size.base`: Default body text, button labels, and input fields.
- `font.size.md`: Section headers, active window titles, and primary list items.
- `font.size.lg`: Card titles, modal headers, and launcher section titles.
- `font.size.xl`: Large clock displays, lock screen time, and hero text.

### Font Weight Tokens
- `font.weight.regular`: Default body text and descriptive labels.
- `font.weight.medium`: Interactive buttons, active tab indicators, and widget headers.
- `font.weight.semibold`: Section titles, active window headers, and key shortcuts.
- `font.weight.bold`: Prominent clock displays and major dialog titles.

---

## Usage Guidelines

1. **Hierarchy Discipline**: Limit text sizes on a single UI card or panel to a maximum of 2 distinct steps (e.g., `font.size.md` for header and `font.size.sm` for subtext).
2. **Contextual Font Pairing**: Use `font.family.ui` for all desktop interface elements and reserved `font.family.mono` for terminal output and numerical data displays.
3. **Legibility First**: Ensure adequate line height and letter spacing across all font sizes to maintain readability on HiDPI displays.

---

## Component Examples

| Component | Target Element | Token Mapping Example |
|---|---|---|
| **Waybar** | Status Bar Text / Clock | `font.family.ui` / `font.size.sm` |
| **Wofi** | Launcher Input & Results | `font.family.ui` / `font.size.base` |
| **Ghostty** | Terminal Font Family | `font.family.mono` |
| **Hyprlock** | Main Clock Display | `font.family.ui` / `font.size.xl` |
| **Mako** | Notification Body / Title | `font.size.sm` / `font.weight.semibold` |
