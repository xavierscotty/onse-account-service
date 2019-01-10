from flask import Flask

from account_service.api.accounts import accounts
from account_service.api.health import health


def create():
    app = Flask(__name__)

    app.register_blueprint(health)
    app.register_blueprint(accounts)

    return app
