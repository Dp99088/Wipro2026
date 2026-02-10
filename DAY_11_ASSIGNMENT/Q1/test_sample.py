import pytest
# Parameterization
@pytest.mark.parametrize("a, b, result", [(2, 3, 5), (4, 6, 10), (1, 1, 2)])
def test_add(a, b, result):
    assert a + b == result

# Read from pytest.ini
def test_read_ini(pytestconfig):
    env = pytestconfig.getini("env")
    assert env == "dev"

# Read from CLI option
def test_environment(request):
    env = request.config.getoption("--env")
    assert env in ["dev", "qa", "prod"]

# Skip Test
@pytest.mark.skip(reason="Under development")
def test_skip():
    assert False

# Xfail Test
@pytest.mark.xfail(reason="Not implemented")
def test_xfail():
    assert 1 == 2