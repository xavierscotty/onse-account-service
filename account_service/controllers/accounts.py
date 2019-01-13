from http import HTTPStatus

from flask import request, jsonify, Blueprint, current_app
from schema import Schema, SchemaError, And

from account_service.domain import commands
from account_service.domain.account import Account
from account_service.domain.errors import CustomerNotFound, AccountNotFound

accounts = Blueprint('accounts', __name__, url_prefix='/accounts/')

POST_ACCOUNT_PAYLOAD_SCHEMA = Schema({'customerId': And(str, len)})


@accounts.route('/<int:account_number>', methods=['GET'])
def get_account(account_number):
    account = commands.get_account(
        account_number=account_number,
        account_repository=current_app.account_repository)

    return jsonify(accountNumber=account.formatted_account_number,
                   accountStatus=account.account_status,
                   customerId=account.customer_id)


@accounts.route('/', methods=['POST'])
def post_account():
    if not request.is_json:
        raise ContentTypeError()

    body = request.get_json()

    POST_ACCOUNT_PAYLOAD_SCHEMA.validate(body)

    customer_id = body['customerId']

    account = Account(account_status='active',
                      customer_id=customer_id)

    commands.create_account(
        account=account,
        account_repository=current_app.account_repository,
        customer_client=current_app.customer_client)

    return jsonify({
        'customerId': customer_id,
        'accountNumber': account.formatted_account_number,
        'accountStatus': 'active'
    }), HTTPStatus.CREATED


@accounts.errorhandler(AccountNotFound)
def account_not_found(e):
    return jsonify(message='Not found'), HTTPStatus.NOT_FOUND


@accounts.errorhandler(CustomerNotFound)
def customer_not_found(e):
    return jsonify(message='Customer not found'), HTTPStatus.BAD_REQUEST


@accounts.errorhandler(SchemaError)
def schema_error(e):
    return jsonify(message=str(e)), HTTPStatus.BAD_REQUEST


class ContentTypeError(RuntimeError):
    pass


@accounts.errorhandler(ContentTypeError)
def content_type_error(e):
    return jsonify(message='Request must be application/json'), \
           HTTPStatus.UNSUPPORTED_MEDIA_TYPE
