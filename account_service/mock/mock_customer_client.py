class MockCustomerClient:
    def __init__(self):
        self.customers = set()

    def add_customer_with_id(self, id):
        self.customers.add(id)

    def has_customer_with_id(self, id):
        return id in self.customers
