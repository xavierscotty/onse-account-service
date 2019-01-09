from flask import Flask, jsonify, request


def create():
    app = Flask(__name__)

    @app.route('/health', methods=['GET'])
    def get_health():
        return jsonify(message='OK')

    @app.route('/accounts/<string:account_number>', methods=['GET'])
    def get_account(account_number):
        return jsonify({'customerId': '12345',
                        'accountNumber': account_number,
                        'accountStatus': 'active'})

    @app.route('/accounts', methods=['POST'])
    def create_account():
        body = request.get_json()
        print(repr(body))
        customer_id = body['customerId']

        return jsonify({
            'customerId': customer_id,
            'accountNumber': 'todo',
            'accountStatus': 'active'
        }), 201

    return app
