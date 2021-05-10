from cms import app

def test_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """

    # Create a test client using the Flask application configured for testing
    response = test_client.get('/')
    print(response.data)
    assert response.status_code == 200
    assert b"Database" in response.data
    assert b"students" in response.data
def test_home_page_post():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is is posted to (POST)
    THEN check that a '405' status code is returned
    """
    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.post('/')
        assert response.status_code == 405
        assert b"Students" not in response.data
