import os

from account_service import app

if __name__ == "__main__":
    app.create().run(host='0.0.0.0', port=int(os.getenv('PORT', 5001)))
