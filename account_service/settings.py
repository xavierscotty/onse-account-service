import os


class Config:
    PORT = int(os.getenv('PORT', 5001))

    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = int(os.getenv('DB_PORT'))
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    CUSTOMER_SERVICE_URL = os.getenv('CUSTOMER_SERVICE_URL')
