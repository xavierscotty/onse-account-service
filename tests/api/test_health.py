def test_get_health(web_client):
    response = web_client.get('/accounts/health')

    assert response.status_code == 200, \
        f'Expected status code to be 200; got {response.status_code}'
    assert response.is_json, \
        f'Expected content type to be JSON; got "{response.data}'
    assert response.get_json() == {'message': 'OK'}, \
        f'Unexpected JSON; got {repr(response.get_json())}'
