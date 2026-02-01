def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Select environment")

    parser.addini("env", "Environment name", default="dev")