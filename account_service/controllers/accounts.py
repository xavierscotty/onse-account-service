from flask import request, jsonify, Blueprint, current_app

from account_service.domain import commands
from account_service.domain.account import Account
from account_service.domain.errors import CustomerNotFound, AccountNotFound

accounts = Blueprint('accounts', __name__, url_prefix='/accounts/')


@accounts.route('/<string:account_number>', methods=['GET'])
def get_account(account_number):
    try:
        account = commands.get_account(
            account_number=int(account_number),
            account_repository=current_app.account_repository)

        return jsonify(accountNumber=account.formatted_account_number,
                       accountStatus=account.account_status,
                       customerId=account.customer_id)
    except AccountNotFound:
        return jsonify(message='Not found'), 404


@accounts.route('/', methods=['POST'])
def post_account():
    body = request.get_json()
    customer_id = body['customerId']

    account = Account(account_status='active',
                      customer_id=customer_id)
    try:
        commands.create_account(account=account,
                                account_repository=current_app.account_repository,
                                customer_client=current_app.customer_client)

        return jsonify({
            'customerId': customer_id,
            'accountNumber': account.formatted_account_number,
            'accountStatus': 'active'
        }), 201
    except CustomerNotFound:
        return jsonify(message='Customer not found'), 400
