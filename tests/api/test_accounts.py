def test_get_accounts_by_number_when_account_exists(web_client,
                                                    account_repository):
    account_number = account_repository.store({'customerId': '12345',
                                               'accountStatus': 'active'})

    response = web_client.get(f'/accounts/accounts/{account_number}')

    expected_json = {'customerId': '12345',
                     'accountNumber': account_number,
                     'accountStatus': 'active'}

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == expected_json


def test_get_accounts_by_number_when_account_does_not_exist(web_client):
    bad_account_number = '11111111'
    response = web_client.get(f'/accounts/accounts/{bad_account_number}')

    expected_json = {'message': 'Not found'}

    assert response.status_code == 404
    assert response.is_json
    assert response.get_json() == expected_json


def test_post_accounts(web_client, customer_client):
    customer_client.add_customer_with_id('12345')

    request_body = {'customerId': '12345'}
    response = web_client.post('/accounts/accounts', json=request_body)

    assert response.status_code == 201
    assert response.is_json
    account = response.get_json()
    assert account['customerId'] == '12345'
    assert account['accountStatus'] == 'active'
    assert 'accountNumber' in account


def test_post_accounts_when_customer_does_not_exist(web_client):
    request_body = {'customerId': '12345'}
    response = web_client.post('/accounts/accounts', json=request_body)

    assert response.status_code == 400
    assert response.is_json
    assert response.get_json() == {'message': 'Customer not found'}
