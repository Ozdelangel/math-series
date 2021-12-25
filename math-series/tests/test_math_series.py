from math_series import __version__
from math_series.series import fibonacci, lucas


def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_eight():
    actual = fibonacci(8)
    expected = 21
    assert actual == expected

def test_fibonacci_is_not_eight():
    actual = fibonacci(8)
    expected = 22
    assert actual != expected

def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected
def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected
def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected
def test_lucas_eight():
    actual = lucas(8)
    expected = 47
    assert actual == expected

