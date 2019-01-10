import requests


class RestCustomerClient:
    def __init__(self, url):
        self.url = url

    def has_customer_with_id(self, id):
        print(f'{self.url}/customers/{id}')
        response = requests.get(f'{self.url}/customers/{id}')

        return response.status_code == 200
