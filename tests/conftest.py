import pytest

from account_service.app import create
from account_service.mock.mock_account_repository import \
    InMemoryAccountRepository


@pytest.fixture(scope='function')
def web_client(account_repository):
    return create(account_repository=account_repository).test_client()


@pytest.fixture(scope='function')
def account_repository():
    return InMemoryAccountRepository()
