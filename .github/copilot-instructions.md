# Copilot Instructions for the `linefeed` Project

## Project Overview
- **Purpose:** `linefeed` is a Python project for managing print workflows, device configuration, and formatting logic. It is organized for extensibility and modularity.
- **Main Package:** All core logic is under `src/linefeed/`.

## Architecture & Key Components
- **API Layer:**
  - `api.py`, `api_config.py`: Define the main API surface and configuration for external integration.
- **Application Entrypoint:**
  - `app.py`: Main application logic and orchestration.
- **Device & Format Config:**
  - `device_config.py`, `format_config.py`: Handle device and formatting configuration schemas and logic.
- **Print Logic:**
  - `print_command.py`, `print_handler.py`, `print_segment.py`: Core print command parsing, handling, and segmenting.
- **Formatting:**
  - `formatter.py`: Implements formatting rules and helpers.
- **Initialization:**
  - `__init__.py`: Exposes package-level symbols and setup.

## Developer Workflows
- **Build/Run:**
  - Use [Poetry](https://python-poetry.org/) for dependency management and scripts.
  - Typical commands:
    - `poetry install` — install dependencies
    - `poetry run python src/linefeed/app.py` — run the main app
- **Testing:**
  - Place tests in `tests/` (not included in repo by default).
  - Run tests with: `poetry run pytest`
- **Configuration:**
  - Project config in `pyproject.toml` (Poetry, dependencies, tool settings).

## Patterns & Conventions
- **Modularity:** Each file in `src/linefeed/` encapsulates a distinct concern (API, config, print logic, formatting).
- **Extensibility:** Add new device/format types by extending `device_config.py` or `format_config.py`.
- **No hardcoded paths:** Use config files and environment variables for device/format selection.
- **Type hints:** Use type annotations for public APIs and core logic.
- **Logging:** (If present) Use standard Python `logging` for diagnostics.
- **Documentation:** Use Numpy-style docstrings for all classes/functions/modules, public and private.

## Integration Points
- **External APIs:** Integrate via `api.py` and `api_config.py`.
- **Device/Format Plugins:** Extend via config modules.

## Examples
- To add a new print command, implement logic in `print_command.py` and register in `print_handler.py`.
- To support a new device, update `device_config.py` and ensure it is referenced in `app.py`.

---
For questions or unclear patterns, review `src/linefeed/` for examples or ask for clarification.
