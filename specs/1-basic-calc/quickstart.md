# Quickstart: PyCalc Development

**Feature**: 1-basic-calc
**Date**: 2025-01-17

## Prerequisites

- Python 3.11 or higher
- uv package manager ([install guide](https://docs.astral.sh/uv/getting-started/installation/))

## Setup

### 1. Clone and Navigate

```bash
cd spec-project
git checkout 1-basic-calc
```

### 2. Create Virtual Environment

```bash
uv venv
```

### 3. Activate Virtual Environment

**Windows (PowerShell)**:
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD)**:
```cmd
.venv\Scripts\activate.bat
```

**macOS/Linux**:
```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
uv pip install -e ".[dev]"
```

This installs:
- The `pycalc` package in editable mode
- Development dependencies (pytest, pytest-cov, ruff)

## Development Workflow

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/pycalc --cov-report=term-missing

# Run specific test file
pytest tests/unit/test_calculator.py

# Run tests matching pattern
pytest -k "test_add"
```

### Lint and Format

```bash
# Check for linting errors
ruff check src/ tests/

# Auto-fix linting errors
ruff check --fix src/ tests/

# Format code
ruff format src/ tests/

# Check formatting without changing
ruff format --check src/ tests/
```

### Run the Calculator

```bash
# After installation
pycalc add 2 3
pycalc subtract 10 4
pycalc multiply 6 7
pycalc divide 20 4

# Show help
pycalc --help
```

## Project Structure

```
spec-project/
├── src/
│   └── pycalc/
│       ├── __init__.py      # Package version
│       ├── calculator.py    # Core arithmetic
│       └── cli.py           # CLI entry point
├── tests/
│   ├── unit/
│   │   └── test_calculator.py
│   └── integration/
│       └── test_cli.py
├── specs/
│   └── 1-basic-calc/        # This feature's docs
├── pyproject.toml           # Project config
└── .specify/                # Spec templates
```

## TDD Cycle

Per constitution, follow strict TDD:

### 1. Red Phase
Write a failing test first:
```python
def test_add_two_positive_numbers():
    assert add(2, 3) == 5
```

Run it to confirm failure:
```bash
pytest tests/unit/test_calculator.py::test_add_two_positive_numbers
```

### 2. Green Phase
Write minimum code to pass:
```python
def add(a: float, b: float) -> float:
    return a + b
```

Run to confirm passing:
```bash
pytest tests/unit/test_calculator.py::test_add_two_positive_numbers
```

### 3. Refactor Phase
Improve code while keeping tests green:
```bash
pytest  # All tests should still pass
```

### 4. Commit
```bash
git add -A
git commit -m "feat: implement add operation"
```

## Verification Checklist

Before marking a task complete:

- [ ] All tests pass: `pytest`
- [ ] Coverage meets target: `pytest --cov=src/pycalc`
- [ ] No lint errors: `ruff check src/ tests/`
- [ ] Code formatted: `ruff format --check src/ tests/`
- [ ] Commit is atomic and descriptive

## Common Issues

### uv not found
Install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`

### Python version mismatch
Ensure Python 3.11+: `python --version`

### Import errors
Ensure package installed: `uv pip install -e ".[dev]"`

### Tests not found
Check you're in the project root with `pyproject.toml`
