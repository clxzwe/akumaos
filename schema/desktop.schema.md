# Desktop Settings Configuration Schema Specification

## Purpose
The desktop schema defines system-wide desktop environment settings, including display outputs, autostart programs, environment variables, display scaling, workspace rules, and window layout behavior in a standardized YAML format.

---

## Schema Structure Specification

### 1. Monitor Layout
Defines display output settings, resolutions, refresh rates, positions, and rotation.

```yaml
monitors:
  - name: string          # Output identifier (e.g. eDP-1, HDMI-A-1)
    resolution: string    # Resolution and refresh rate (e.g. 1920x1080@144)
    position: string      # Output position offsets (e.g. 0x0, 1920x0)
    scale: float          # Display scale factor (e.g. 1.0, 1.25, 2.0)
    transform: integer    # Rotation transform (0: normal, 1: 90 deg, etc.)
    enabled: boolean      # Output enable/disable toggle
```

### 2. Startup Applications
Specifies commands and daemons executed upon desktop session launch.

```yaml
autostart:
  - command: string       # Shell command or executable binary
    description: string   # Purpose of the autostart program
    condition: string     # Optional launch condition
```

### 3. Environment Variables
Declares global environment variables passed to the Wayland compositor and child processes.

```yaml
environment:
  XDG_CURRENT_DESKTOP: string
  XDG_SESSION_TYPE: string
  XDG_SESSION_DESKTOP: string
  QT_QPA_PLATFORM: string
  GDK_BACKEND: string
```

### 4. Cursor Settings
Defines pointer theme, cursor scale, and hardware cursor settings.

```yaml
cursor:
  theme: string           # Global cursor theme name
  size: integer           # Cursor size in pixels
  inactive_timeout: integer # Seconds before hiding idle cursor
```

### 5. Scaling & High-DPI Settings
Defines global UI scale factors and High-DPI rendering behavior.

```yaml
scaling:
  ui_scale: float         # General UI scaling factor
  font_dpi: integer       # Target font DPI value
  xwayland_scale: float   # Scaling factor for XWayland applications
```

### 6. Workspace Behavior
Defines workspace rules, default monitor bindings, and persistent workspace layouts.

```yaml
workspaces:
  default_count: integer  # Number of initial workspaces
  rules:
    - workspace: integer  # Workspace number
      monitor: string     # Assigned monitor name
      persistent: boolean # Persistent workspace toggle
```

### 7. Window Behavior
Defines window tiling layout, focus policies, window rules, and floating window behavior.

```yaml
window_behavior:
  layout_engine: string   # Tiling layout engine (e.g. dwindle, master)
  focus_follow_mouse: integer # Mouse focus policy mode
  focus_on_activate: boolean  # Focus window on activation request
  window_rules:
    - class: string       # Application window class matcher
      title: string       # Window title matcher
      action: string      # Rule action (e.g. float, tile, workspace)
```
