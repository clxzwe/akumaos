# Contributing to AkumaOS

Thank you for your interest in contributing to AkumaOS! Please review the guidelines below before submitting your contributions.

---

## Branch Naming

Use descriptive branch names with appropriate prefixes:

- `feat/feature-name` — for new features or configurations
- `fix/bug-description` — for bug fixes
- `docs/doc-update` — for documentation updates
- `chore/task-name` — for maintenance or setup tasks

---

## Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat: add new waybar module`
- `fix: resolve hyprlock keybinding issue`
- `docs: update installation guide`
- `chore: update repository structure`

Keep commit titles concise and under 72 characters.

---

## Pull Requests

1. Fork and clone the repository.
2. Create your feature or fix branch from `main`.
3. Keep pull requests focused on a single change or feature.
4. Provide a clear description of changes and any testing performed.
5. Ensure all status checks and linting pass.

---

## Code Style

- Adhere to the formatting defined in [.editorconfig](.editorconfig).
- **Lua**: Use 4 spaces for indentation.
- **YAML / JSON**: Use 2 spaces for indentation.
- **Shell Scripts**: Follow ShellCheck standards and use UTF-8 / LF line endings.

---

## Testing Before Merge

- Test all scripts and configurations locally before submitting a pull request.
- Verify syntax correctness and ensure no broken paths or missing assets exist.
