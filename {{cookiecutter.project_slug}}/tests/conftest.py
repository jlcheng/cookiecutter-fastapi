import pytest


@pytest.fixture
def example_fixture() -> str:
    return "this is an example fixture injected by conftest.py"
