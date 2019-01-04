from account_service import app


def before_all(context):
    context.web_client = app.create().test_client()
