from account_service import app
from account_service.infrastructure.postgresql_account_respository import \
    PostgreSQLAccountRepository
from account_service.infrastructure.rest_customer_client import \
    RestCustomerClient
from account_service.settings import Config

if __name__ == "__main__":
    app.create(
        account_repository=PostgreSQLAccountRepository(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            username=Config.DB_USERNAME,
            password=Config.DB_PASSWORD,
            db=Config.DB_NAME),
        customer_client=RestCustomerClient(Config.CUSTOMER_SERVICE_URL)
    ).run(host='0.0.0.0', port=Config.PORT)
