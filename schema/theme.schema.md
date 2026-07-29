# Theme Configuration Schema Specification

## Purpose
The theme schema defines the structure for AkumaOS theme definitions. Theme packages specify visual design token assignments, wallpaper selections, icon sets, and cursor themes in a standardized YAML format.

---

## Schema Structure Specification

### 1. Metadata
Defines theme identification, author details, versioning, and variant classification.

```yaml
metadata:
  name: string            # Theme display name
  id: string              # Unique identifier (kebab-case)
  version: string         # Semantic version string
  author: string          # Author or maintainer name
  description: string     # Short summary of theme aesthetic
  variant: string         # Theme variant (e.g. dark, light)
```

### 2. Colors
Maps semantic color roles to design token color values.

```yaml
colors:
  bg:
    base: string          # Base surface color
    surface: string       # Secondary surface color
    floating: string      # Elevated surface color
  fg:
    primary: string       # Primary high-contrast text color
    secondary: string     # Secondary text color
    muted: string         # Muted text color
  accent:
    primary: string       # Primary brand accent color
    secondary: string     # Secondary accent color
  border:
    active: string        # Active border color
    inactive: string      # Inactive border color
  status:
    info: string          # Info status color
    success: string       # Success status color
    warning: string       # Warning status color
    error: string         # Error status color
```

### 3. Typography
Defines UI and monospace font families, size metrics, and weights.

```yaml
typography:
  family:
    ui: string            # Interface font family name
    mono: string          # Monospace font family name
  sizes:
    xs: string            # Extra small font size
    sm: string            # Small font size
    base: string          # Base body font size
    md: string            # Medium header font size
    lg: string            # Large header font size
    xl: string            # Extra large font size
  weights:
    regular: integer      # Regular weight integer
    medium: integer       # Medium weight integer
    semibold: integer     # Semibold weight integer
    bold: integer         # Bold weight integer
```

### 4. Spacing
Defines padding metrics, margins, and window gap distances.

```yaml
spacing:
  scale:
    3xs: string           # Micro padding
    2xs: string           # Extra small padding
    xs: string            # Small padding
    sm: string            # Standard padding
    md: string            # Medium padding
    lg: string            # Large padding
    xl: string            # Extra large padding
  gaps:
    window_inner: string  # Inner gap between tiled windows
    window_outer: string  # Outer gap to screen edges
    bar_module: string    # Bar module spacing
    launcher_item: string # Launcher list item spacing
```

### 5. Radius
Defines corner curvature metrics across UI containers.

```yaml
radius:
  xs: string              # Tag/tooltip corner radius
  sm: string              # Button/input corner radius
  md: string              # Popup/dropdown corner radius
  lg: string              # Window/launcher corner radius
  xl: string              # Modal/dialog corner radius
  full: string            # Fully rounded pill radius
```

### 6. Blur
Defines backdrop blur radii and rendering parameters.

```yaml
blur:
  radius: string          # Gaussian blur radius
  passes: integer         # Number of blur passes
  noise: float            # Noise grain factor
  vibrancy: float         # Color vibrancy boost
```

### 7. Shadows
Defines z-axis drop shadow metrics and ambient colors.

```yaml
shadows:
  elevation:
    low: string           # Inline button elevation
    medium: string        # Bar/popup elevation
    high: string          # Window/launcher elevation
    max: string           # Lock screen elevation
  color: string           # Shadow color rgba
```

### 8. Animations
Defines duration scales and transition easing curves.

```yaml
animations:
  durations:
    instant: string       # Micro feedback duration
    fast: string          # Quick UI transition duration
    normal: string        # Window transition duration
    slow: string          # Modal reveal duration
  curves:
    linear: string        # Linear easing curve
    ease_in_out: string   # Ease-in-out curve
    spring: string        # Spring inertia curve
    decelerate: string    # Deceleration curve
```

### 9. Wallpaper
Specifies the default wallpaper asset path and display mode.

```yaml
wallpaper:
  path: string            # Relative or absolute wallpaper image path
  category: string        # Wallpaper category (minimal, abstract, nature, anime)
  mode: string            # Display fit mode (fill, fit, center)
```

### 10. Icons
Specifies icon theme package name and default icon sizing.

```yaml
icons:
  theme: string           # System icon theme name
  sizes:
    bar: string           # Bar icon size
    menu: string          # Menu icon size
    notification: string  # Notification icon size
```

### 11. Cursor
Specifies cursor theme package name and pointer dimensions.

```yaml
cursor:
  theme: string           # Cursor theme package name
  size: integer           # Cursor size in pixels
```
