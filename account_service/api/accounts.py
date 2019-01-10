from flask import request, jsonify, Blueprint

accounts = Blueprint('accounts', __name__, url_prefix='/accounts/')


@accounts.route('/accounts/<string:account_number>', methods=['GET'])
def get_account(account_number):
    return jsonify({'customerId': '12345',
                    'accountNumber': account_number,
                    'accountStatus': 'active'})


@accounts.route('/accounts', methods=['POST'])
def post_account():
    body = request.get_json()
    print(repr(body))
    customer_id = body['customerId']

    return jsonify({
        'customerId': customer_id,
        'accountNumber': 'todo',
        'accountStatus': 'active'
    }), 201
