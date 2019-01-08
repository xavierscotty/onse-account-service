from flask import Flask, jsonify


def create():
    app = Flask(__name__)

    @app.route('/health', methods=['GET'])
    def get_health():
        return jsonify(message='OK')

    @app.route('/accounts/<string:account_number>', methods=['GET'])
    def get_accounts(account_number):
        return jsonify({'accountNumber': account_number,
                        'state': 'active'})

    return app
