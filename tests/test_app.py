import pytest

from account_service.app import create


@pytest.fixture(scope='function')
def web_client():
    return create().test_client()


def test_get_health(web_client):
    response = web_client.get('/health')

    assert response.status_code == 200, \
        f'Expected status code to be 200; got {response.status_code}'
    assert response.is_json, \
        f'Expected content type to be JSON; got "{response.data}'
    assert response.get_json() == {'message': 'OK'}, \
        f'Unexpected JSON; got {repr(response.get_json())} '


def test_get_accounts_by_number_when_account_exists(web_client):
    response = web_client.get('/accounts/999999')

    expected_json = {'accountNumber': '999999',
                     'accountStatus': 'active'}

    assert response.status_code == 200, \
        f'Expected status code to be 200; got {response.status_code}'
    assert response.is_json, \
        f'Expected content type to be JSON; got "{response.data}'
    assert response.get_json() == expected_json, \
        f'Unexpected JSON; got {repr(response.get_json())} '
