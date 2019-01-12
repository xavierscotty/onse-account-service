from flask import jsonify, Blueprint

health = Blueprint('health', __name__)


@health.route('/health', methods=['GET'])
def get_health():
    return jsonify(message='OK')
