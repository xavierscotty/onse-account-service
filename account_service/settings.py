import os


class Config:
    PORT = int(os.getenv('PORT', 5001))
    CUSTOMER_SERVICE_URL = os.getenv('CUSTOMER_SERVICE_URL')
