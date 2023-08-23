from currency.models import Source


def test_get_api_rates(api_client_authorized):
    response = api_client_authorized.get('/api/v1/currency/rates/')
    assert response.status_code == 200
    assert response.json()


def test_post_api_rates_empty(api_client):
    response = api_client.post('/api/v1/currency/rates/')
    assert response.status_code == 400
    assert response.json() == {
        'buy': ['This field is required.'],
        'sell': ['This field is required.'],
        'source': ['This field is required.']
    }


def test_post_api_rates_valid(api_client):
    source = Source.objects.create(name='test', code_name='test')
    payload = {
        'buy': '30.00',
        'sell': '40.00',
        'source': source.id
    }
    response = api_client.post('/api/v1/currency/rates/', data=payload)
    assert response.status_code == 201
