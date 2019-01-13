from unittest import mock
from unittest.mock import patch

import pytest

from account_service.domain.account import Account
from account_service.domain.errors import AccountNotFound, CustomerNotFound


@patch('account_service.domain.commands.get_account')
def test_get_accounts_by_number_when_account_exists(get_account,
                                                    web_client,
                                                    account_repository):
    get_account.return_value = Account(account_number=123,
                                       account_status='active',
                                       customer_id='12345')

    response = web_client.get(f'/accounts/00000123')

    get_account.assert_called_with(account_number=123,
                                   account_repository=account_repository)

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {'customerId': '12345',
                                   'accountNumber': '00000123',
                                   'accountStatus': 'active'}


@patch('account_service.domain.commands.get_account')
def test_get_accounts_by_number_when_account_does_not_exist(get_account,
                                                            web_client):
    get_account.side_effect = AccountNotFound()

    bad_account_number = '11111111'
    response = web_client.get(f'/accounts/{bad_account_number}')

    expected_json = {'message': 'Not found'}

    assert response.status_code == 404
    assert response.is_json
    assert response.get_json() == expected_json


@patch('account_service.domain.commands.create_account')
def test_post_accounts(create_account, web_client, account_repository,
                       customer_client):
    request_body = {'customerId': '12345'}

    response = web_client.post('/accounts/', json=request_body)

    create_account.assert_called_with(account=mock.ANY,
                                      account_repository=account_repository,
                                      customer_client=customer_client)

    saved_account = create_account.mock_calls[0][2]['account']
    assert saved_account.account_number is None
    assert saved_account.account_status == 'active'
    assert saved_account.customer_id == '12345'

    assert response.status_code == 201
    assert response.is_json

    account = response.get_json()

    assert account['customerId'] == '12345'
    assert account['accountStatus'] == 'active'
    assert account['accountNumber'] is None  # None because call is mocked


@patch('account_service.domain.commands.create_account')
def test_post_accounts_when_customer_does_not_exist(create_account, web_client,
                                                    account_repository,
                                                    customer_client):
    create_account.side_effect = CustomerNotFound()

    response = web_client.post('/accounts/',
                               json={'customerId': '12345'})

    assert response.status_code == 400
    assert response.is_json
    assert response.get_json() == {'message': 'Customer not found'}


@pytest.mark.parametrize(
    'bad_payload',
    [{},
     {'customerId': '12345678', 'unknown': 'value'},
     {'customerId': ''}])
def test_post_accounts_with_bad_payload(web_client, bad_payload):
    response = web_client.post('/accounts/', json=bad_payload)
    assert response.status_code == 400


def test_post_accounts_with_bad_context_type(web_client):
    response = web_client.post('/accounts/', data='not json')
    assert response.status_code == 415
    assert response.get_json()['message'] == 'Request must be application/json'
