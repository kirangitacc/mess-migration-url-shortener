import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert data['service'] == 'URL Shortener API'

def test_shorten_and_redirect(client):
    original_url = "https://example.com"
    response = client.post('/api/shorten', json={"url": original_url})
    assert response.status_code == 200
    short_url = response.get_json()['short_url']
    short_id = short_url.split('/')[-1]

    redirect_response = client.get(f'/{short_id}')
    assert redirect_response.status_code == 302
    assert redirect_response.location == original_url

def test_invalid_url(client):
    response = client.post('/api/shorten', json={"url": "not-a-url"})
    assert response.status_code == 400

def test_redirect_invalid_code(client):
    response = client.get('/invalid123')
    assert response.status_code == 404

def test_stats_endpoint(client):
    original_url = "https://example.com"
    response = client.post('/api/shorten', json={"url": original_url})
    short_id = response.get_json()['short_code']

    # Trigger a redirect to increment clicks
    client.get(f'/{short_id}')

    stats_response = client.get(f'/api/stats/{short_id}')
    assert stats_response.status_code == 200
    stats = stats_response.get_json()
    assert stats['url'] == original_url
    assert stats['clicks'] == 1
    assert 'created_at' in stats
