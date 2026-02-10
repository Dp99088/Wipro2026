import pytest

@pytest.fixture(scope="session")
def setup_environment():
    print("\n--- Test Environment Setup ---")
    yield
    print("\n--- Test Environment Teardown ---")


@pytest.fixture(scope="function")
def login_data():
    return {
        "username": "admin",
        "password": "admin123"
    }