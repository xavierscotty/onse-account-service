import pytest

from account_service.app import create


@pytest.fixture(scope='function')
def web_client():
    return create().test_client()
