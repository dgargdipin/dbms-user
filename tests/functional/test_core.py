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


def test_valid_login_logout(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/login',
                                data=dict(email='dgargdipin@gmail.com', password='abc'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Dipin' in response.data
    assert b'Log Out' in response.data
    assert b'Login' not in response.data
    assert b'Register' not in response.data

    """
    GIVEN a Flask application configured for testing
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/logout', follow_redirects=True)
    print(response.data)

    assert response.status_code == 200
    assert b'Welcome' in response.data
    assert b'Logout' not in response.data
    assert b'Log In' in response.data
    assert b'Register' in response.data

