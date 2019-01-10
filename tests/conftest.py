import pytest

from account_service.app import create
from account_service.mock.mock_account_repository import \
    MockAccountRepository
from account_service.mock.mock_customer_client import MockCustomerClient


@pytest.fixture
def web_client(account_repository, customer_client):
    return create(account_repository=account_repository,
                  customer_client=customer_client).test_client()


@pytest.fixture
def account_repository():
    return MockAccountRepository()


@pytest.fixture
def customer_client():
    return MockCustomerClient()
