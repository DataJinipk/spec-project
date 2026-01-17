"""Integration tests for PyCalc CLI."""

import subprocess
import sys


def run_pycalc(*args: str) -> subprocess.CompletedProcess[str]:
    """Run pycalc with given arguments and return result."""
    return subprocess.run(
        [sys.executable, "-m", "pycalc.cli", *args],
        capture_output=True,
        text=True,
    )


class TestCLIAdd:
    """Tests for add operation via CLI."""

    def test_add_two_positive_numbers(self) -> None:
        """CLI add 2 3 should output 5."""
        result = run_pycalc("add", "2", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "5"

    def test_add_floats(self) -> None:
        """CLI add 1.5 2.5 should output 4."""
        result = run_pycalc("add", "1.5", "2.5")
        assert result.returncode == 0
        assert result.stdout.strip() == "4"


class TestCLISubtract:
    """Tests for subtract operation via CLI."""

    def test_subtract_two_positive_numbers(self) -> None:
        """CLI subtract 10 4 should output 6."""
        result = run_pycalc("subtract", "10", "4")
        assert result.returncode == 0
        assert result.stdout.strip() == "6"


class TestCLIMultiply:
    """Tests for multiply operation via CLI."""

    def test_multiply_two_positive_numbers(self) -> None:
        """CLI multiply 6 7 should output 42."""
        result = run_pycalc("multiply", "6", "7")
        assert result.returncode == 0
        assert result.stdout.strip() == "42"


class TestCLIDivide:
    """Tests for divide operation via CLI."""

    def test_divide_two_positive_numbers(self) -> None:
        """CLI divide 20 4 should output 5."""
        result = run_pycalc("divide", "20", "4")
        assert result.returncode == 0
        assert result.stdout.strip() == "5"

    def test_divide_by_zero_error(self) -> None:
        """CLI divide 10 0 should error with division by zero."""
        result = run_pycalc("divide", "10", "0")
        assert result.returncode == 1
        assert "Error: Division by zero" in result.stderr

    def test_divide_zero_by_number(self) -> None:
        """CLI divide 0 5 should output 0."""
        result = run_pycalc("divide", "0", "5")
        assert result.returncode == 0
        assert result.stdout.strip() == "0"


class TestCLIInvalidInput:
    """Tests for invalid input handling."""

    def test_invalid_number(self) -> None:
        """CLI add abc 3 should error with invalid number."""
        result = run_pycalc("add", "abc", "3")
        assert result.returncode == 1
        assert "Error: Invalid number 'abc'" in result.stderr

    def test_unknown_operation(self) -> None:
        """CLI unknown 2 3 should error with unknown operation."""
        result = run_pycalc("unknown", "2", "3")
        assert result.returncode == 1
        assert "Error: Unknown operation 'unknown'" in result.stderr
        assert "Valid operations: add, subtract, multiply, divide" in result.stderr

    def test_missing_argument(self) -> None:
        """CLI add 5 (missing second number) should error."""
        result = run_pycalc("add", "5")
        assert result.returncode != 0  # argparse exits with 2

    def test_help_display(self) -> None:
        """CLI --help should display usage information."""
        result = run_pycalc("--help")
        assert result.returncode == 0
        assert "usage: pycalc" in result.stdout
        assert "add, subtract, multiply, divide" in result.stdout
