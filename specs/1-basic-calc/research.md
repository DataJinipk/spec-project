# Research: Basic Arithmetic Calculator

**Feature**: 1-basic-calc
**Date**: 2025-01-17

## Overview

This document captures technology decisions and research findings for the basic calculator implementation.

## Decision 1: CLI Argument Parsing

**Decision**: Use Python's built-in `argparse` module

**Rationale**:
- Part of Python standard library (no additional dependencies)
- Provides automatic help generation (`--help`)
- Handles argument validation and type conversion
- Well-documented and widely understood

**Alternatives Considered**:
| Alternative | Pros | Cons | Rejected Because |
|-------------|------|------|------------------|
| `click` | Decorator-based, elegant API | External dependency | Violates simplicity principle |
| `typer` | Type hints, modern | External dependency | Violates simplicity principle |
| Manual `sys.argv` | Zero abstraction | No help generation, more code | argparse is simpler overall |

## Decision 2: Number Parsing

**Decision**: Use Python's built-in `float()` for all numeric input

**Rationale**:
- Handles both integers and decimals uniformly
- Provides clear error messages for invalid input
- Returns `int`-like behavior for whole numbers when formatted

**Alternatives Considered**:
| Alternative | Pros | Cons | Rejected Because |
|-------------|------|------|------------------|
| `int()` then `float()` fallback | Preserves integer type | More complex logic | Unnecessary complexity |
| `decimal.Decimal` | Precise decimal arithmetic | Overkill for basic calculator | Violates YAGNI |

## Decision 3: Output Formatting

**Decision**: Print raw numeric result; strip trailing zeros for floats

**Rationale**:
- `5` is cleaner than `5.0` for integer results
- `4.5` is appropriate for non-integer results
- Simple implementation with Python's string formatting

**Implementation**:
```python
def format_result(value: float) -> str:
    if value == int(value):
        return str(int(value))
    return str(value)
```

## Decision 4: Error Handling Strategy

**Decision**: Catch specific exceptions, output to stderr, exit with code 1

**Rationale**:
- Per constitution: errors to stderr, exit code 1 for user errors
- Specific error messages help users correct their input
- No stack traces for user-facing errors

**Error Categories**:
| Error | Message Format | Exit Code |
|-------|---------------|-----------|
| Division by zero | `Error: Division by zero` | 1 |
| Invalid number | `Error: Invalid number '{value}'` | 1 |
| Unknown operation | `Error: Unknown operation '{op}'. Valid: add, subtract, multiply, divide` | 1 |
| Wrong argument count | `Error: Expected 2 numbers, got {n}` | 1 |

## Decision 5: Project Configuration

**Decision**: Use `pyproject.toml` with uv-compatible configuration

**Rationale**:
- Per constitution: uv for package management
- Modern Python packaging standard (PEP 621)
- Single file for project metadata, dependencies, and tool configuration

**Configuration Sections**:
- `[project]`: Name, version, description, Python requirement
- `[project.scripts]`: CLI entry point (`pycalc = "pycalc.cli:main"`)
- `[tool.pytest.ini_options]`: Test configuration
- `[tool.ruff]`: Linting and formatting rules

## No Unresolved Items

All technical decisions have been made. No NEEDS CLARIFICATION items remain.
