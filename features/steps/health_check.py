from behave import *


@when("I check the health of the service")
def check_service_health(context):
    context.response = context.web_client.get('/health')


@then("I should receive an OK response")
def assert_service_health(context):
    response = context.response
    status_code = response.status_code

    assert status_code == 200, f'Expected status code to be 200; got {status_code}'
    assert response.is_json, f'Expected content type to be JSON; got "{response.data}'
    assert response.get_json() == dict(message='OK'), f'Unexpected JSON; got {repr(response.get_json())} '
