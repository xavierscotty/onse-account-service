from account_service import app
from account_service.mock.mock_account_repository import MockAccountRepository
from account_service.mock.mock_customer_client import MockCustomerClient


def before_scenario(context, scenario):
    context.account_repository = MockAccountRepository()
    context.customer_client = MockCustomerClient()

    context.web_client = app.create(
        account_repository=context.account_repository,
        customer_client=context.customer_client
    ).test_client()
