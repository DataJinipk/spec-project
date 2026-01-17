# PyCalc Constitution
<!--
  Sync Impact Report
  ==================
  Version change: 0.0.0 → 1.0.0
  Modified principles: N/A (initial ratification)
  Added sections: Core Principles (5), Development Workflow, Quality Standards, Governance
  Removed sections: None
  Templates requiring updates:
    - .specify/templates/plan-template.md ✅ (compatible - Constitution Check section aligns)
    - .specify/templates/spec-template.md ✅ (compatible - TDD principles align with test scenarios)
    - .specify/templates/tasks-template.md ✅ (compatible - test-first pattern matches)
  Follow-up TODOs: None
-->

## Core Principles

### I. Single Responsibility

Every module MUST have one clear purpose. The calculator library handles arithmetic operations; the CLI handles user interaction; tests validate behavior. No module should mix concerns.

**Rationale**: A basic calculator is simple by nature. Maintaining this simplicity prevents scope creep and ensures maintainability.

### II. CLI-First Interface

All calculator functionality MUST be accessible via command-line interface. Input comes from arguments or stdin; output goes to stdout; errors go to stderr. Human-readable output is the default.

**Rationale**: CLI-first ensures the calculator is scriptable, testable, and composable with other tools.

### III. Test-Driven Development (NON-NEGOTIABLE)

TDD is mandatory for all feature development:
1. Tests MUST be written before implementation code
2. Tests MUST fail before implementation (Red phase)
3. Implementation MUST make tests pass (Green phase)
4. Code MUST be refactored while tests stay green (Refactor phase)

**Rationale**: For a calculator, correctness is paramount. TDD guarantees that every operation is verified before being considered complete.

### IV. UV Package Management

The project MUST use `uv` for Python package management and virtual environment handling. Dependencies MUST be declared in `pyproject.toml`. No pip commands outside of uv context.

**Rationale**: uv provides fast, reproducible builds and modern Python packaging standards.

### V. Simplicity Over Features

Start with the minimum viable implementation. YAGNI (You Aren't Gonna Need It) applies strictly:
- Basic operations only: addition, subtraction, multiplication, division
- No premature optimization
- No speculative features
- Complexity MUST be justified in writing

**Rationale**: A calculator that does four operations correctly is more valuable than one that attempts many and fails.

## Quality Standards

### Code Quality

- Python 3.11+ required
- Type hints MUST be used for all public functions
- Code MUST pass `ruff` linting with no errors
- Code MUST be formatted with `ruff format`

### Testing Standards

- pytest is the testing framework
- All arithmetic operations MUST have unit tests
- Edge cases (division by zero, overflow) MUST be tested
- Test coverage target: 100% for core calculation logic

### Error Handling

- Division by zero MUST raise a clear, user-friendly error
- Invalid input MUST produce helpful error messages to stderr
- Exit codes: 0 for success, 1 for user error, 2 for system error

## Development Workflow

### Feature Development Cycle

1. Write specification in `specs/<feature>/spec.md`
2. Create implementation plan in `specs/<feature>/plan.md`
3. Generate tasks in `specs/<feature>/tasks.md`
4. Execute TDD cycle for each task:
   - Write failing test
   - Implement minimum code to pass
   - Refactor if needed
5. Commit after each completed task

### Commit Standards

- Atomic commits: one logical change per commit
- Conventional commit messages: `type: description`
- Types: feat, fix, test, docs, refactor, chore

## Governance

This constitution is the authoritative source for project standards. All code reviews and PRs MUST verify compliance with these principles.

### Amendment Process

1. Propose amendment with rationale
2. Document in ADR if architecturally significant
3. Update constitution with version increment
4. Propagate changes to dependent templates

### Versioning Policy

- MAJOR: Principle removal or incompatible redefinition
- MINOR: New principle or section added
- PATCH: Clarifications and wording improvements

**Version**: 1.0.0 | **Ratified**: 2025-01-17 | **Last Amended**: 2025-01-17
