"""Core arithmetic operations for PyCalc."""


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b."""
    return a / b


def format_result(value: float) -> str:
    """Format a numeric result for display.

    Strips trailing .0 for integer results.
    """
    if value == int(value):
        return str(int(value))
    return str(value)
