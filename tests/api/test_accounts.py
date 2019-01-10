def test_get_accounts_by_number_when_account_exists(web_client,
                                                    account_repository):
    account_number = account_repository.store({'customerId': '12345',
                                               'accountStatus': 'active'})

    response = web_client.get(f'/accounts/accounts/{account_number}')

    expected_json = {'customerId': '12345',
                     'accountNumber': account_number,
                     'accountStatus': 'active'}

    assert response.status_code == 200, \
        f'Expected status code to be 200; got {response.status_code}'
    assert response.is_json, \
        f'Expected content type to be JSON; got "{response.data}'
    assert response.get_json() == expected_json, \
        f'Unexpected JSON; got {repr(response.get_json())}'


def test_get_accounts_by_number_when_account_does_not_exist(web_client):
    bad_account_number = '11111111'
    response = web_client.get(f'/accounts/accounts/{bad_account_number}')

    expected_json = {'message': 'Not found'}

    assert response.status_code == 404, \
        f'Expected status code to be 404; got {response.status_code}'
    assert response.is_json, \
        f'Expected content type to be JSON; got "{response.data}'
    assert response.get_json() == expected_json, \
        f'Unexpected JSON; got {repr(response.get_json())}'


def test_post_accounts(web_client):
    request_body = {'customerId': '12345'}
    response = web_client.post('/accounts/accounts', json=request_body)

    assert response.status_code == 201, \
        f'Expected status code to be 201; got {response.status_code}'
    assert response.is_json, \
        f'Expected content type to be JSON; got "{response.data}'
    account = response.get_json()
    assert account['customerId'] == '12345', \
        f'Expected customerId to be 12345, got account {account}'
    assert account['accountStatus'] == 'active', \
        f'Expected accountStatus to be "active", got account {account}'
    assert 'accountNumber' in account, \
        f'Expected account to have accountNumber, got account {account}'
