import pytest

def add(a, b):
    return a + b

from calculator import add

def test_add():
    assert add(2, 3) == 5