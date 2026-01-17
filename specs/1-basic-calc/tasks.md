# Tasks: Basic Arithmetic Calculator

**Input**: Design documents from `/specs/1-basic-calc/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, contracts/cli-interface.md

**Tests**: REQUIRED per constitution (Principle III: TDD is NON-NEGOTIABLE)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/pycalc/`, `tests/` at repository root
- Paths follow plan.md structure

---

## Phase 1: Setup

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directory structure: `src/pycalc/`, `tests/unit/`, `tests/integration/`
- [x] T002 Create `pyproject.toml` with uv configuration, pytest, ruff, and CLI entry point `pycalc = "pycalc.cli:main"`
- [x] T003 [P] Create `src/pycalc/__init__.py` with version `__version__ = "0.1.0"`
- [x] T004 [P] Create `tests/__init__.py`, `tests/unit/__init__.py`, `tests/integration/__init__.py`
- [x] T005 Initialize uv virtual environment and install dev dependencies

**Checkpoint**: Project structure ready, `uv pip install -e ".[dev]"` succeeds, `pytest` runs (0 tests)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Create empty `src/pycalc/calculator.py` with module docstring
- [x] T007 Create empty `src/pycalc/cli.py` with module docstring and `main()` stub that returns 0
- [x] T008 Verify CLI entry point works: `pycalc` runs without error (returns 0)

**Checkpoint**: Foundation ready - `pycalc` command exists and runs

---

## Phase 3: User Story 1 - Perform Single Calculation (Priority: P1)

**Goal**: Users can perform add, subtract, multiply, divide operations via CLI

**Independent Test**: Run `pycalc add 2 3` and verify output is `5`

### Tests for User Story 1 (TDD Red Phase)

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T009 [P] [US1] Write unit test for `add(a, b)` function in `tests/unit/test_calculator.py`
- [x] T010 [P] [US1] Write unit test for `subtract(a, b)` function in `tests/unit/test_calculator.py`
- [x] T011 [P] [US1] Write unit test for `multiply(a, b)` function in `tests/unit/test_calculator.py`
- [x] T012 [P] [US1] Write unit test for `divide(a, b)` function in `tests/unit/test_calculator.py`
- [x] T013 [US1] Write integration test for CLI `pycalc add 2 3` in `tests/integration/test_cli.py`
- [x] T014 [US1] Write integration test for CLI `pycalc subtract 10 4` in `tests/integration/test_cli.py`
- [x] T015 [US1] Write integration test for CLI `pycalc multiply 6 7` in `tests/integration/test_cli.py`
- [x] T016 [US1] Write integration test for CLI `pycalc divide 20 4` in `tests/integration/test_cli.py`
- [x] T017 [US1] Verify all US1 tests FAIL (Red phase complete)

### Implementation for User Story 1 (TDD Green Phase)

- [x] T018 [P] [US1] Implement `add(a: float, b: float) -> float` in `src/pycalc/calculator.py`
- [x] T019 [P] [US1] Implement `subtract(a: float, b: float) -> float` in `src/pycalc/calculator.py`
- [x] T020 [P] [US1] Implement `multiply(a: float, b: float) -> float` in `src/pycalc/calculator.py`
- [x] T021 [P] [US1] Implement `divide(a: float, b: float) -> float` in `src/pycalc/calculator.py`
- [x] T022 [US1] Implement `format_result(value: float) -> str` in `src/pycalc/calculator.py` (strips `.0`)
- [x] T023 [US1] Implement CLI argument parsing with argparse in `src/pycalc/cli.py`
- [x] T024 [US1] Implement operation dispatch and result output in `src/pycalc/cli.py`
- [x] T025 [US1] Verify all US1 tests PASS (Green phase complete)

**Checkpoint**: `pycalc add 2 3` → `5`, all four operations work, tests pass

---

## Phase 4: User Story 2 - Handle Division by Zero (Priority: P2)

**Goal**: Users receive clear error message when dividing by zero

**Independent Test**: Run `pycalc divide 10 0` and verify stderr contains "Error: Division by zero" with exit code 1

### Tests for User Story 2 (TDD Red Phase)

- [x] T026 [P] [US2] Write unit test for `divide(10, 0)` raising `ZeroDivisionError` in `tests/unit/test_calculator.py`
- [x] T027 [P] [US2] Write integration test for `pycalc divide 10 0` error output in `tests/integration/test_cli.py`
- [x] T028 [P] [US2] Write integration test for `pycalc divide 0 5` returning `0` in `tests/integration/test_cli.py`
- [x] T029 [US2] Verify all US2 tests FAIL (Red phase complete)

### Implementation for User Story 2 (TDD Green Phase)

- [x] T030 [US2] Add `ZeroDivisionError` handling in `src/pycalc/cli.py` with "Error: Division by zero" to stderr
- [x] T031 [US2] Ensure exit code 1 on division by zero in `src/pycalc/cli.py`
- [x] T032 [US2] Verify all US2 tests PASS (Green phase complete)

**Checkpoint**: `pycalc divide 10 0` → stderr "Error: Division by zero", exit 1

---

## Phase 5: User Story 3 - Handle Invalid Input (Priority: P3)

**Goal**: Users receive helpful error messages for invalid input

**Independent Test**: Run `pycalc add abc 3` and verify stderr contains "Error: Invalid number 'abc'" with exit code 1

### Tests for User Story 3 (TDD Red Phase)

- [x] T033 [P] [US3] Write integration test for `pycalc add abc 3` (invalid number) in `tests/integration/test_cli.py`
- [x] T034 [P] [US3] Write integration test for `pycalc unknown 2 3` (unknown operation) in `tests/integration/test_cli.py`
- [x] T035 [P] [US3] Write integration test for `pycalc add 5` (missing argument) in `tests/integration/test_cli.py`
- [x] T036 [P] [US3] Write integration test for `pycalc --help` (help display) in `tests/integration/test_cli.py`
- [x] T037 [US3] Verify all US3 tests FAIL (Red phase complete)

### Implementation for User Story 3 (TDD Green Phase)

- [x] T038 [US3] Add number parsing with `ValueError` handling in `src/pycalc/cli.py` for "Error: Invalid number '<value>'"
- [x] T039 [US3] Add unknown operation handling in `src/pycalc/cli.py` for "Error: Unknown operation '<op>'. Valid operations: add, subtract, multiply, divide"
- [x] T040 [US3] Add argument count validation in `src/pycalc/cli.py` for "Error: Expected 2 numbers, got <n>"
- [x] T041 [US3] Configure argparse help message per CLI contract in `src/pycalc/cli.py`
- [x] T042 [US3] Verify all US3 tests PASS (Green phase complete)

**Checkpoint**: All error messages work per contract, help displays correctly

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final quality checks and refinements

- [x] T043 [P] Run `ruff check src/ tests/` and fix any linting errors
- [x] T044 [P] Run `ruff format src/ tests/` to format all code
- [x] T045 Run `pytest --cov=src/pycalc --cov-report=term-missing` and verify 100% coverage on calculator.py
- [x] T046 [P] Add type hints to all public functions if not already present
- [x] T047 Run full test suite: `pytest -v` - all tests must pass
- [x] T048 Manual validation: run quickstart.md examples and verify expected output

**Checkpoint**: All quality gates pass, ready for PR

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1: Setup
    ↓
Phase 2: Foundational
    ↓
┌───────────────────────────────────────────┐
│  User Stories (can proceed in priority    │
│  order OR in parallel if team capacity)   │
├───────────────────────────────────────────┤
│  Phase 3: US1 (P1) ─────────────────────▶ │
│  Phase 4: US2 (P2) ─────────────────────▶ │
│  Phase 5: US3 (P3) ─────────────────────▶ │
└───────────────────────────────────────────┘
    ↓
Phase 6: Polish
```

### User Story Dependencies

- **User Story 1 (P1)**: Depends on Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Depends on US1 (needs divide function) - Can start after T021 complete
- **User Story 3 (P3)**: Depends on US1 (needs CLI structure) - Can start after T024 complete

### Within Each User Story

1. Tests (Red) MUST be written and FAIL before implementation
2. Implementation (Green) makes tests pass
3. Refactor while tests stay green
4. Story complete before moving to next priority

### Parallel Opportunities

- Setup: T003, T004 can run in parallel
- US1 Tests: T009, T010, T011, T012 can run in parallel
- US1 Implementation: T018, T019, T020, T021 can run in parallel
- US2 Tests: T026, T027, T028 can run in parallel
- US3 Tests: T033, T034, T035, T036 can run in parallel
- Polish: T043, T044, T046 can run in parallel

---

## Parallel Execution Examples

### User Story 1 - Tests (can run together)

```bash
# Launch all unit tests for US1 together:
pytest tests/unit/test_calculator.py -v
```

### User Story 1 - Implementation (can run together)

```bash
# All four operation functions can be implemented in parallel
# (different functions in same file, no dependencies between them)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: `pycalc add 2 3` works
5. Deploy/demo if ready - this IS the MVP!

### Incremental Delivery

1. Setup + Foundational → Project ready
2. Add User Story 1 → Core calculator works (MVP!)
3. Add User Story 2 → Division by zero handled
4. Add User Story 3 → All errors handled gracefully
5. Polish → Production ready

### TDD Cycle Per Task

For each implementation task:

```bash
# 1. Write test (Red)
pytest tests/unit/test_calculator.py::test_add -v
# Should FAIL

# 2. Implement (Green)
# Edit src/pycalc/calculator.py
pytest tests/unit/test_calculator.py::test_add -v
# Should PASS

# 3. Refactor
# Clean up code
pytest tests/unit/test_calculator.py::test_add -v
# Should still PASS

# 4. Commit
git add -A && git commit -m "feat: implement add operation"
```

---

## Summary

| Phase | Tasks | Parallel | Description |
|-------|-------|----------|-------------|
| Setup | 5 | 2 | Project initialization |
| Foundational | 3 | 0 | CLI stub |
| US1 (P1) | 17 | 8 | Core calculations |
| US2 (P2) | 7 | 3 | Division by zero |
| US3 (P3) | 10 | 4 | Invalid input handling |
| Polish | 6 | 3 | Quality gates |
| **Total** | **48** | **20** | |

**MVP Scope**: Phases 1-3 (25 tasks) - delivers working calculator with all four operations
