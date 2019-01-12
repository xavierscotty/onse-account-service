from behave import given, when, then

from features.steps.get_account import get_account_by_context, \
    assert_account_details

CREATE_ACCOUNT_URL = f'/accounts/'


@given('I am a registered customer with ID "{customer_id}"')
def create_customer(context, customer_id):
    context.customer_client.add_customer_with_id(customer_id)


@given('there is no customer with ID "{customer_id}"')
def do_not_create_customer(context, customer_id):
    # Intentionally left blank
    pass


@when('I create an account with customer ID "{customer_id}"')
def create_account(context, customer_id):
    response = context.web_client.post(CREATE_ACCOUNT_URL,
                                       json={"customerId": customer_id})

    if response.status_code == 201:
        context.account_number = response.get_json()['accountNumber']

    context.response = response


@then('my account should be "{status}" and have customer ID "{customer_id}"')
def step_impl(context, status, customer_id):
    get_account_by_context(context)
    assert_account_details(context, status, customer_id)


@then("then account should not be created")
def assert_not_created_response(context):
    assert context.response.status_code == 400
