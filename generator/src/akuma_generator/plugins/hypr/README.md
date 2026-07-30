# Hyprland Plugin (`plugins/hypr/`)

## Purpose
The Hyprland plugin handles configuration generation for the Hyprland Wayland compositor, including monitors (`monitors.conf`), window rules, workspace bindings, keybindings, and decoration settings.

## Compatibility Target
AkumaOS currently targets **Hyprland 0.56.x**.

### Directive Rules
- **Obsolete/Deprecated Directives**: Directives such as `<dwindle:pseudotile>` are not emitted. Pseudotile behavior is supported via the `pseudo` keybind dispatcher.
- **Keybind Dispatchers**: All keybind dispatchers are audited against Hyprland 0.56.x (e.g., layout split toggling uses `layoutmsg, togglesplit`). Standalone `togglesplit` is unsupported.
- **Future Releases**: Future Hyprland releases require explicit compatibility updates and validation before modifying generator syntax.

