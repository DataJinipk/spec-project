# Implementation Plan: Basic Arithmetic Calculator

**Branch**: `1-basic-calc` | **Date**: 2025-01-17 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/1-basic-calc/spec.md`

## Summary

Build a command-line calculator (`pycalc`) that performs four basic arithmetic operations (add, subtract, multiply, divide) on two numeric operands. The implementation uses Python 3.11+ with uv for package management, following strict TDD practices per the project constitution.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: None (standard library only for core logic)
**Package Manager**: uv (per constitution)
**Storage**: N/A (stateless CLI tool)
**Testing**: pytest with pytest-cov for coverage
**Linting**: ruff (linting + formatting)
**Target Platform**: Cross-platform (Windows, macOS, Linux)
**Project Type**: Single project
**Performance Goals**: Sub-1-second execution for any operation
**Constraints**: No external runtime dependencies for core functionality
**Scale/Scope**: Single CLI tool, ~200 lines of code

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Requirement | Status |
|-----------|-------------|--------|
| I. Single Responsibility | Separate modules for: calculator logic, CLI interface, tests | PASS |
| II. CLI-First Interface | All operations via CLI args; stdout/stderr separation | PASS |
| III. TDD (NON-NEGOTIABLE) | Tests written before implementation; red-green-refactor | PASS |
| IV. UV Package Management | Use uv for venv and dependencies; pyproject.toml | PASS |
| V. Simplicity Over Features | Four operations only; no speculative features | PASS |

**Gate Status**: ALL PASS - Proceed to implementation

## Project Structure

### Documentation (this feature)

```text
specs/1-basic-calc/
├── spec.md              # Feature specification
├── plan.md              # This file
├── research.md          # Technology decisions
├── data-model.md        # Entity definitions
├── quickstart.md        # Developer setup guide
├── contracts/           # CLI interface specification
│   └── cli-interface.md
└── tasks.md             # Implementation tasks (from /sp.tasks)
```

### Source Code (repository root)

```text
src/
└── pycalc/
    ├── __init__.py      # Package init with version
    ├── calculator.py    # Core arithmetic operations
    └── cli.py           # CLI entry point and argument parsing

tests/
├── __init__.py
├── unit/
│   ├── __init__.py
│   └── test_calculator.py   # Unit tests for calculator module
└── integration/
    ├── __init__.py
    └── test_cli.py          # CLI integration tests

pyproject.toml           # Project configuration (uv, pytest, ruff)
```

**Structure Decision**: Single project layout chosen per constitution Principle V (Simplicity). The calculator is a small, focused tool with no need for multi-package complexity.

## Module Responsibilities

| Module | Responsibility | Dependencies |
|--------|----------------|--------------|
| `pycalc.calculator` | Pure arithmetic functions (add, subtract, multiply, divide) | None |
| `pycalc.cli` | Argument parsing, input validation, output formatting, exit codes | `pycalc.calculator` |
| `tests.unit.test_calculator` | Unit tests for arithmetic correctness | `pycalc.calculator`, `pytest` |
| `tests.integration.test_cli` | End-to-end CLI behavior tests | `subprocess`, `pytest` |

## Complexity Tracking

> No violations - design follows all constitution principles.

| Principle | Compliance | Notes |
|-----------|------------|-------|
| Single Responsibility | Full | Two modules with clear separation |
| CLI-First | Full | All functionality via CLI |
| TDD | Full | Test structure ready for red-green-refactor |
| UV Package Management | Full | pyproject.toml with uv configuration |
| Simplicity | Full | Minimal dependencies, focused scope |
