# Data Model: Basic Arithmetic Calculator

**Feature**: 1-basic-calc
**Date**: 2025-01-17

## Overview

The basic calculator is a stateless CLI tool with no persistent data storage. This document defines the conceptual entities and their relationships for implementation clarity.

## Entities

### Operation

Represents one of four arithmetic operations the calculator can perform.

| Attribute | Type | Description |
|-----------|------|-------------|
| name | string | Command name: `add`, `subtract`, `multiply`, `divide` |
| symbol | string | Mathematical symbol: `+`, `-`, `*`, `/` |
| function | callable | Python function implementing the operation |

**Valid Operations**:
```
add       → addition (+)
subtract  → subtraction (-)
multiply  → multiplication (*)
divide    → division (/)
```

### Operand

A numeric value provided as input to an operation.

| Attribute | Type | Constraints |
|-----------|------|-------------|
| value | float | Any valid Python float (including integers) |

**Validation Rules**:
- Must be parseable by Python's `float()` function
- Can be positive, negative, or zero
- Can be integer or decimal format

**Examples**:
- Valid: `5`, `-3`, `2.5`, `0`, `-0.001`, `1e10`
- Invalid: `abc`, `1.2.3`, ``, `NaN` (rejected as user error)

### Result

The computed output of applying an operation to two operands.

| Attribute | Type | Description |
|-----------|------|-------------|
| value | float | Computed result of the operation |
| formatted | string | Human-readable output (strips unnecessary decimals) |

**Formatting Rules**:
- Integer results display without decimal: `5` not `5.0`
- Decimal results display as-is: `4.5`
- Very large/small numbers use Python's default representation

## Relationships

```
┌───────────┐     ┌───────────┐     ┌───────────┐
│ Operand 1 │────▶│ Operation │────▶│  Result   │
└───────────┘     └───────────┘     └───────────┘
                        ▲
┌───────────┐           │
│ Operand 2 │───────────┘
└───────────┘
```

**Relationship Description**:
- An Operation takes exactly two Operands as input
- An Operation produces exactly one Result as output
- The relationship is stateless (no memory between invocations)

## State Transitions

The calculator is stateless. Each invocation is independent:

```
[Start] → Parse Args → Validate → Calculate → Format → Output → [End]
                │           │          │
                ▼           ▼          ▼
            [Error]     [Error]    [Error]
```

**Error States**:
- Parse failure → Invalid number error
- Validation failure → Wrong argument count or unknown operation
- Calculation failure → Division by zero

## Type Definitions (for implementation)

```python
from typing import Callable, TypeAlias

# Type aliases
Number: TypeAlias = float
OperationFunc: TypeAlias = Callable[[Number, Number], Number]

# Operation registry type
OPERATIONS: dict[str, OperationFunc] = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b,  # Raises ZeroDivisionError
}
```
