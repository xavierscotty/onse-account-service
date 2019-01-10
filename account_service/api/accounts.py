from flask import request, jsonify, Blueprint, current_app

accounts = Blueprint('accounts', __name__, url_prefix='/accounts/')


@accounts.route('/accounts/<string:account_number>', methods=['GET'])
def get_account(account_number):
    try:
        account_repository = current_app.account_repository

        account = account_repository.fetch_by_account_number(account_number)
        return jsonify(account)
    except AccountNotFound:
        return jsonify(message='Not found'), 404


@accounts.route('/accounts', methods=['POST'])
def post_account():
    body = request.get_json()
    customer_id = body['customerId']

    return jsonify({
        'customerId': customer_id,
        'accountNumber': 'todo',
        'accountStatus': 'active'
    }), 201


class AccountNotFound(RuntimeError):
    pass
