from flask import request, jsonify, Blueprint, current_app

from account_service.domain.account import Account

accounts = Blueprint('accounts', __name__, url_prefix='/accounts/')


@accounts.route('/accounts/<string:account_number>', methods=['GET'])
def get_account(account_number):
    try:
        account_repository = current_app.account_repository

        account = account_repository.fetch_by_account_number(int(account_number))

        return jsonify(accountNumber=account.formatted_account_number,
                       accountStatus=account.account_status,
                       customerId=account.customer_id)
    except AccountNotFound:
        return jsonify(message='Not found'), 404


@accounts.route('/accounts', methods=['POST'])
def post_account():
    account_repository = current_app.account_repository

    body = request.get_json()
    customer_client = current_app.customer_client
    customer_id = body['customerId']

    if not customer_client.has_customer_with_id(customer_id):
        return jsonify(message='Customer not found'), 400

    account = Account(account_status='active',
                      customer_id=customer_id)

    account_repository.store(account)

    return jsonify({
        'customerId': customer_id,
        'accountNumber': account.formatted_account_number,
        'accountStatus': 'active'
    }), 201


class AccountNotFound(RuntimeError):
    pass
