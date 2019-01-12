from behave import given, when, then

from account_service.domain.account import Account

GET_ACCOUNT_URL = f'/accounts/%s'


@given('there an "{status}" account with customer id "{customer_id}"')
def create_account(context, status, customer_id):
    account = Account(customer_id=customer_id, account_status=status)
    context.account_repository.store(account)
    context.account_number = account.account_number


@given('there is no account with id "{number}"')
def do_not_create_account(context, number):
    # Intentionally left blank
    pass


@when("I get the account details")
def get_account_by_context(context):
    response = context.web_client.get(GET_ACCOUNT_URL % context.account_number)
    context.response = response


@when('I get the account details for account "{number}"')
def get_account_by_account_number(context, number):
    response = context.web_client.get(GET_ACCOUNT_URL % number)
    context.response = response


@then('I should see an "{status}" account with customer id "{customer_id}"')
def assert_account_details(context, status, customer_id):
    assert context.response.status_code == 200
    account = context.response.get_json()

    assert account['accountStatus'] == status
    assert account['customerId'] == customer_id


@then("I should get a not found message")
def assert_not_found_response(context):
    assert context.response.status_code == 404
