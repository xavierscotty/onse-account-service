from account_service.domain.account import Account


def test_get_accounts_by_number_when_account_exists(web_client,
                                                    account_repository):
    account = Account(customer_id='12345', account_status='active')
    account_repository.store(account)

    account_number = account.formatted_account_number

    print(f'/accounts/accounts/{account_number}')
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

    account_number = account['accountNumber']

    print(f'/accounts/accounts/{account_number}')
    response = web_client.get(f'/accounts/accounts/{account_number}')
    account = response.get_json()

    assert account == {'accountNumber': account_number,
                       'accountStatus': 'active',
                       'customerId': '12345'}


def test_post_accounts_when_customer_does_not_exist(web_client):
    request_body = {'customerId': '12345'}
    response = web_client.post('/accounts/accounts', json=request_body)

    assert response.status_code == 400
    assert response.is_json
    assert response.get_json() == {'message': 'Customer not found'}
