from flask import Flask, jsonify


def create():
    app = Flask(__name__)

    @app.route('/health')
    def health():
        return jsonify(message='OK')

    return app
