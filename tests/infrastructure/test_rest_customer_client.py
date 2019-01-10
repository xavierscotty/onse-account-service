import requests_mock

from account_service.infrastructure.rest_customer_client import \
    RestCustomerClient


def test_has_customer_with_id_when_customer_exists():
    with requests_mock.mock() as m:
        m.get('http://customer.service/customers/1234',
              status_code=200,
              json={'name': 'Tom'})

        client = RestCustomerClient('http://customer.service')

        assert client.has_customer_with_id('1234') is True


def test_has_customer_with_id_when_customer_not_exists():
    with requests_mock.mock() as m:
        m.get('http://customer.service/customers/5678',
              status_code=404,
              json={'message': 'Not found'})

        client = RestCustomerClient('http://customer.service')

        assert client.has_customer_with_id('5678') is False
