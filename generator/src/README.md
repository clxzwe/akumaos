# Generator Source Logic (`generator/src/`)

## Purpose
This directory is reserved for generator source logic, parsers, template rendering engines, and schema validation utilities.

## Planned Component Responsibilities
- **Schema Parser**: Reads and parses YAML configuration schemas from `schema/` and design tokens from `themes/tokens/`.
- **Template Compiler**: Interpolates parsed token variables into target application templates located in `generator/templates/`.
- **Validation Pipeline**: Verifies output syntax correctness before staging files to `generator/output/`.
