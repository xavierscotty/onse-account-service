from flask import jsonify, Blueprint

health = Blueprint('health', __name__, url_prefix='/accounts/')


@health.route('/health', methods=['GET'])
def get_health():
    return jsonify(message='OK')
