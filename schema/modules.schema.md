# Module Configuration Schema Specification

## Purpose
The modules schema defines how individual desktop components (Waybar, Hyprlock, Hypridle, Ghostty, Mako, Wofi) are enabled, disabled, and configured. This modular design allows users to toggle or swap desktop components declaratively.

---

## Enable / Disable Behavior

Each module in the schema contains an explicit `enabled` boolean flag:
- `enabled: true`: The module generator processes the module schema and deploys the corresponding component configuration to `~/.config/<module>/`.
- `enabled: false`: The module is skipped during configuration generation, and any active daemon autostart triggers for that component are omitted.

---

## Component Module Schemas

### 1. Waybar Module Schema
Status bar module activation, positioning, and widget layouts.

```yaml
modules:
  waybar:
    enabled: boolean      # Enable status bar
    position: string      # Bar position (top, bottom, left, right)
    height: integer       # Bar height in pixels
    spacing: integer      # Inner widget spacing
    modules_left:
      - string            # Active left-aligned widget modules
    modules_center:
      - string            # Active center-aligned widget modules
    modules_right:
      - string            # Active right-aligned widget modules
```

### 2. Hyprlock Module Schema
Screen locker module configuration, auth card layout, and clock settings.

```yaml
modules:
  hyprlock:
    enabled: boolean      # Enable screen locker
    fade_on_empty: boolean# Fade password input when empty
    font_family: string   # Lock screen clock font family
    clock_format: string  # Time display string format
```

### 3. Hypridle Module Schema
Session idle daemon timeouts and power management triggers.

```yaml
modules:
  hypridle:
    enabled: boolean      # Enable idle management
    timeouts:
      - timeout: integer  # Seconds before dimming screen
        on_timeout: string# Command to run on timeout
        on_resume: string # Command to run on resume
      - timeout: integer  # Seconds before locking screen
        on_timeout: string# Lock screen command
```

### 4. Ghostty Module Schema
Terminal emulator module styling, font metrics, and padding.

```yaml
modules:
  ghostty:
    enabled: boolean      # Enable terminal configuration
    font_family: string   # Terminal monospace font family
    font_size: integer    # Font size in points
    padding_x: integer    # Horizontal window padding
    padding_y: integer    # Vertical window padding
    opacity: float        # Terminal window opacity
```

### 5. Notifications Module Schema (Mako)
Notification daemon popup layout, positioning, and timeout rules.

```yaml
modules:
  notifications:
    enabled: boolean      # Enable notification daemon
    position: string      # Popup anchor position (e.g. top-right)
    default_timeout: integer # Default notification timeout in milliseconds
    max_visible: integer  # Maximum simultaneous visible notifications
    layer: string         # Layer shell placement (overlay, top)
```

### 6. Launcher Module Schema (Wofi)
Application launcher layout, mode, and dimension metrics.

```yaml
modules:
  launcher:
    enabled: boolean      # Enable application launcher
    mode: string          # Launcher mode (drun, run, cmd)
    width: string         # Launcher window width
    height: string        # Launcher window height
    prompt: string        # Search field prompt placeholder
    allow_images: boolean # Enable application icon rendering
```
