import pytest

@pytest.fixture
def setup_teardown():
    print("setup")
    yield
    print("teardown")

def test_example(setup_teardown):
    print("test running")

