from account_service import app
from account_service.infrastructure.rest_customer_client import RestCustomerClient
from account_service.mock.mock_account_repository import MockAccountRepository
from account_service.settings import Config

if __name__ == "__main__":
    app.create(
        account_repository=MockAccountRepository(),
        customer_client=RestCustomerClient(Config.CUSTOMER_SERVICE_URL)
    ).run(host='0.0.0.0', port=Config.PORT)
