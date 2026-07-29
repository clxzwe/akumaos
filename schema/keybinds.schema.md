# Keybinds Configuration Schema Specification

## Purpose
The keybinds schema defines a declarative format for keybindings across AkumaOS. By specifying shortcuts in a structured YAML schema, keymaps can be validated, listed in help overlays, and translated into compositor configurations automatically.

---

## Schema Structure Specification

Each keybinding definition contains the following required fields:

- `modifiers`: Array of modifier keys (e.g. `SUPER`, `ALT`, `CTRL`, `SHIFT`).
- `key`: Primary trigger key or mouse button (e.g. `Return`, `Q`, `mouse:272`).
- `action`: Dispatcher command or application launch directive executed upon trigger.
- `description`: Human-readable summary of the keybinding's purpose.
- `category`: Functional category grouping for documentation and search menus.

---

## YAML Schema Example

```yaml
keybinds:
  - modifiers:
      - SUPER
    key: Return
    action: exec ghostty
    description: Open terminal emulator
    category: Applications

  - modifiers:
      - SUPER
    key: Q
    action: killactive
    description: Close active window
    category: Window Management

  - modifiers:
      - SUPER
      - SHIFT
    key: Space
    action: togglefloating
    description: Toggle floating state for active window
    category: Window Management

  - modifiers:
      - SUPER
    key: D
    action: exec wofi --show drun
    description: Open application launcher
    category: Navigation

  - modifiers:
      - SUPER
    key: L
    action: exec hyprlock
    description: Lock screen session
    category: System

  - modifiers:
      - SUPER
    key: "1"
    action: workspace 1
    description: Switch to workspace 1
    category: Workspaces
```

---

## Categorization Standards

Standard keybinding categories include:
- **Applications**: Launching system terminal, browser, file manager, and tools.
- **Window Management**: Window closing, tiling, floating, splitting, and resizing.
- **Workspaces**: Workspace switching, window movement between workspaces, and monitor focus.
- **Navigation**: Application launcher, window switcher, and menu toggles.
- **Media & System**: Volume controls, brightness adjustment, screenshots, and lock screen triggers.
