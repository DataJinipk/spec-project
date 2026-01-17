"""Unit tests for calculator module."""

import pytest

from pycalc.calculator import add, divide, multiply, subtract


class TestAdd:
    """Tests for add function."""

    def test_add_two_positive_numbers(self) -> None:
        """Add two positive numbers."""
        assert add(2, 3) == 5

    def test_add_negative_numbers(self) -> None:
        """Add negative numbers."""
        assert add(-5, 3) == -2

    def test_add_floats(self) -> None:
        """Add floating-point numbers."""
        assert add(1.5, 2.5) == 4.0


class TestSubtract:
    """Tests for subtract function."""

    def test_subtract_two_positive_numbers(self) -> None:
        """Subtract two positive numbers."""
        assert subtract(10, 4) == 6

    def test_subtract_negative_result(self) -> None:
        """Subtract resulting in negative."""
        assert subtract(3, 5) == -2


class TestMultiply:
    """Tests for multiply function."""

    def test_multiply_two_positive_numbers(self) -> None:
        """Multiply two positive numbers."""
        assert multiply(6, 7) == 42

    def test_multiply_by_zero(self) -> None:
        """Multiply by zero."""
        assert multiply(5, 0) == 0


class TestDivide:
    """Tests for divide function."""

    def test_divide_two_positive_numbers(self) -> None:
        """Divide two positive numbers."""
        assert divide(20, 4) == 5

    def test_divide_with_remainder(self) -> None:
        """Divide with decimal result."""
        result = divide(10, 3)
        assert abs(result - 3.333333333333333) < 0.0001

    def test_divide_by_zero_raises_error(self) -> None:
        """Division by zero should raise ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

    def test_divide_zero_by_number(self) -> None:
        """Zero divided by non-zero is valid."""
        assert divide(0, 5) == 0
