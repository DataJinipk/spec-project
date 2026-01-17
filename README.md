# PyCalc

[![CI](https://github.com/DataJinipk/spec-project/actions/workflows/ci.yml/badge.svg)](https://github.com/DataJinipk/spec-project/actions/workflows/ci.yml)

A basic arithmetic calculator CLI.

## Installation

```bash
uv pip install -e ".[dev]"
```

## Usage

```bash
pycalc add 2 3        # 5
pycalc subtract 10 4  # 6
pycalc multiply 6 7   # 42
pycalc divide 20 4    # 5
```

## Development

```bash
pytest              # Run tests
ruff check src/     # Lint
ruff format src/    # Format
```
