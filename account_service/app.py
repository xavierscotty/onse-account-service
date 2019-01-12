from flask import Flask

from account_service.controllers.accounts import accounts
from account_service.controllers.health import health


def create(account_repository, customer_client):
    app = Flask(__name__)

    app.account_repository = account_repository
    app.customer_client = customer_client

    app.register_blueprint(health)
    app.register_blueprint(accounts)

    return app
