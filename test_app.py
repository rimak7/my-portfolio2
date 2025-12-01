# content of test_app.py (Recommended)
import pytest
from app import app # Assuming your Flask app instance is named 'app' in app.py

# A fixture is a setup function used by tests.
@pytest.fixture
def client():
    # Set Flask to testing mode
    app.config['TESTING'] = True
    # Create a test client
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test that the main '/' route loads successfully."""
    response = client.get('/')
    
    # Check if the HTTP status code is 200 (OK)
    assert response.status_code == 200
    
    # Check if a known phrase (like the title or a heading) is in the response body
    # NOTE: You may need to change "Welcome to my portfolio" to match content in index.html
    assert b"Welcome to my project" in response.data