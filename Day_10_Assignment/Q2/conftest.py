import pytest

@pytest.fixture(scope="module")
def sample_numbers():
    print("\nSetup module fixture")
    yield (10, 5)
    print("\nTeardown module fixture")

@pytest.fixture(scope="function")
def sample_string():
    return "pytest"