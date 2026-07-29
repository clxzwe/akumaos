# Generator Test Suite (`generator/tests/`)

## Purpose
This directory contains automated test suites for validating the generator compilation pipeline, schema parsing, and template rendering.

## Planned Test Coverage
- **Template Rendering Tests**: Verifies that templates render cleanly without missing variable substitutions or syntax errors.
- **Token Mapping Verification**: Tests that all design token references in templates map to valid token declarations in `themes/tokens/`.
- **Output Syntax Validation**: Validates generated configuration outputs against target application syntax checkers.
