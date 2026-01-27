import pytest

def setup_function():
    print("\nSetup function")

def teardown_function():
    print("Teardown function")

class TestMathOperations:
    def setup_method(self):
        print("\nsetup before test")

    def teardown_method(self):
        print("Teardown after test")

    def test_addition(self, sample_numbers):
        a, b = sample_numbers
        assert a + b == 15

    def test_subtraction(self, sample_numbers):
        a, b = sample_numbers
        assert a - b == 5

    def test_division(self):
        with pytest.raises(ZeroDivisionError):
            result = 10 / 0