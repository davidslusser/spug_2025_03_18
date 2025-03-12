# test_calculator.py
import pytest
from src.calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(8, 2) == 4


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(5, 0)
