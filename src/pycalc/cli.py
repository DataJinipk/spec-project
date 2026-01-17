"""Command-line interface for PyCalc."""

import argparse
import sys

from pycalc.calculator import add, divide, format_result, multiply, subtract

OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


def main() -> int:
    """Entry point for the pycalc CLI."""
    parser = argparse.ArgumentParser(
        prog="pycalc",
        description="A basic arithmetic calculator.",
    )
    parser.add_argument(
        "operation",
        help="Operation to perform: add, subtract, multiply, divide",
    )
    parser.add_argument("number1", help="First number")
    parser.add_argument("number2", help="Second number")

    args = parser.parse_args()

    # Get operation function
    operation_func = OPERATIONS.get(args.operation)
    if operation_func is None:
        print(
            f"Error: Unknown operation '{args.operation}'. "
            "Valid operations: add, subtract, multiply, divide",
            file=sys.stderr,
        )
        return 1

    # Parse numbers
    try:
        num1 = float(args.number1)
    except ValueError:
        print(f"Error: Invalid number '{args.number1}'", file=sys.stderr)
        return 1

    try:
        num2 = float(args.number2)
    except ValueError:
        print(f"Error: Invalid number '{args.number2}'", file=sys.stderr)
        return 1

    # Perform calculation
    try:
        result = operation_func(num1, num2)
    except ZeroDivisionError:
        print("Error: Division by zero", file=sys.stderr)
        return 1

    # Output result
    print(format_result(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
