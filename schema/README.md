# AkumaOS Configuration Schema Specification

## Overview
The schema layer defines the declarative data structures used to specify desktop behavior, visual themes, component modules, and keybindings in AkumaOS. 

By separating declarative configuration schemas from component generation logic, AkumaOS ensures that configuration specifications remain human-readable, machine-validatable, and fully independent of specific application formats.

---

## Schema Documents

- [theme.schema.md](theme.schema.md): Declarative specification for visual theme packages (colors, typography, spacing, radius, blur, shadows, animations, wallpaper, icons, cursor).
- [desktop.schema.md](desktop.schema.md): System-wide desktop settings (monitors, startup apps, environment variables, scaling, window & workspace behavior).
- [modules.schema.md](modules.schema.md): Enable/disable behavior and feature configuration for desktop components (Waybar, Hyprlock, Hypridle, Ghostty, Mako, Wofi).
- [keybinds.schema.md](keybinds.schema.md): Declarative keybinding definitions (modifiers, key, action, description, category).

---

## Data Pipeline Architecture

```text
Design Tokens (themes/tokens/)
       ↓
Configuration Schema (schema/*.schema.md)
       ↓
Generator Engine (scripts/ & tools/)
       ↓
Native Application Configs (config/*)
```
