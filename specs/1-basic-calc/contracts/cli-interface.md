# CLI Interface Contract: pycalc

**Feature**: 1-basic-calc
**Date**: 2025-01-17

## Command Signature

```
pycalc <operation> <number1> <number2>
pycalc --help
pycalc -h
```

## Operations

| Operation | Description | Example |
|-----------|-------------|---------|
| `add` | Addition | `pycalc add 2 3` → `5` |
| `subtract` | Subtraction | `pycalc subtract 10 4` → `6` |
| `multiply` | Multiplication | `pycalc multiply 6 7` → `42` |
| `divide` | Division | `pycalc divide 20 4` → `5` |

## Input Specification

### Arguments

| Position | Name | Type | Required | Description |
|----------|------|------|----------|-------------|
| 1 | operation | string | Yes | One of: `add`, `subtract`, `multiply`, `divide` |
| 2 | number1 | float | Yes | First operand |
| 3 | number2 | float | Yes | Second operand |

### Number Format

- Integers: `5`, `-3`, `0`
- Decimals: `2.5`, `-0.001`, `3.14159`
- Scientific notation: `1e10`, `2.5e-3`
- Negative numbers: `-5`, `-2.5`

## Output Specification

### Success (exit code 0)

**stdout**: Result of the calculation, followed by newline

```
<result>\n
```

**Formatting Rules**:
- Integer results: no decimal point (`5` not `5.0`)
- Decimal results: as-is (`4.5`, `3.333333333333333`)

### Error (exit code 1)

**stderr**: Error message, followed by newline

```
Error: <description>\n
```

**stdout**: Empty

## Error Messages

| Condition | Message |
|-----------|---------|
| Division by zero | `Error: Division by zero` |
| Invalid number | `Error: Invalid number '<value>'` |
| Unknown operation | `Error: Unknown operation '<op>'. Valid operations: add, subtract, multiply, divide` |
| Missing arguments | `Error: Expected 2 numbers, got <n>` |
| No arguments | Displays help text |

## Help Output

When invoked with `--help`, `-h`, or no arguments:

```
usage: pycalc [-h] operation number1 number2

A basic arithmetic calculator.

positional arguments:
  operation   Operation to perform: add, subtract, multiply, divide
  number1     First number
  number2     Second number

options:
  -h, --help  show this help message and exit
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success - calculation completed |
| 1 | User error - invalid input |

## Examples

### Successful Operations

```bash
$ pycalc add 2 3
5

$ pycalc subtract 10 4
6

$ pycalc multiply 6 7
42

$ pycalc divide 20 4
5

$ pycalc add 1.5 2.5
4

$ pycalc divide 10 3
3.3333333333333335

$ pycalc add -5 3
-2
```

### Error Cases

```bash
$ pycalc divide 10 0
Error: Division by zero

$ pycalc add abc 3
Error: Invalid number 'abc'

$ pycalc unknown 2 3
Error: Unknown operation 'unknown'. Valid operations: add, subtract, multiply, divide

$ pycalc add 5
Error: Expected 2 numbers, got 1

$ pycalc
usage: pycalc [-h] operation number1 number2
...
```

## Integration Examples

### Shell Scripting

```bash
# Use in arithmetic expressions
result=$(pycalc add 10 20)
echo "Result: $result"

# Chain operations (manual)
step1=$(pycalc add 5 3)
step2=$(pycalc multiply $step1 2)
echo "Final: $step2"  # 16

# Error handling
if ! pycalc divide 10 0 2>/dev/null; then
    echo "Division failed"
fi
```

### Piping

```bash
# Output can be piped
pycalc add 100 200 | xargs -I {} echo "Sum is {}"
```
