import os

from account_service import app
from account_service.mock.mock_account_repository import MockAccountRepository
from account_service.mock.mock_customer_client import MockCustomerClient

if __name__ == "__main__":
    app.create(
        account_repository=MockAccountRepository(),
        customer_client=MockCustomerClient()
    ).run(host='0.0.0.0', port=int(os.getenv('PORT', 5001)))
