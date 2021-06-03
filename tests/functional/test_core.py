from cms import app
from bs4 import BeautifulSoup
import bs4

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
    assert b"Course" in response.data
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
    print(response.data)

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


def test_user_view_quizzes(test_client, login_default_user):
    response = test_client.get('/course/1', follow_redirects=True)
    print(response.data)
    assert response.status_code == 200
    bs = BeautifulSoup(response.data, 'lxml')
    view_quiz = bs.find('a', class_='vq1')
    view_quizzes_link = view_quiz['href']
    response1 = test_client.get(view_quizzes_link, follow_redirects=True)
    assert response1.status_code == 200
    assert b'Quiz1' in response1.data
    assert b'Start Time:' in response1.data
    assert b'End Time:' in response1.data
    

    # /quiz/attempt/<quiz_id>

# def test_user_attempt_quiz(test_client, login_default_user):
#     response = test_client.get('/course/2/quizzes', follow_redirects=True)
#     assert response.status_code == 200
    
#     bs = BeautifulSoup(response.data, 'lxml')
#     quiz_link = bs.find('a', class_='c1')['href']

#     response1 = test_client.get(quiz_link, follow_redirects=True)
#     assert response1.status_code == 200
#     assert b'Odd one out' in response1.data
#     assert b'Submit' in response1.data
#     assert b'django' in response1.data
#     assert b'flask' in response1.data
#     assert b'ruby on rails' in response1.data
#     assert b'expressjs' in response1.data
    
#     reponse2 = test_client.post('/quiz/attempt/1',dict())
    


# def test_user_view_grades(test_client, login_default_user):
#     response = test_client('/course/2/quizzes', follow_redirectes=True)
#     assert response.status_code == 200
    

def test_user_enrollment_request(test_client, login_default_user):
    response = test_client.get('/', follow_redirects=True)
    assert response.status_code == 200
    bs = BeautifulSoup(response.data, 'lxml')
    enroll_link = bs.find('a', class_='enr1')['href']
    

    response1= test_client.get(enroll_link,follow_redirects=True)
    assert response1.status_code == 200
    enroll = bs.find('a', class_='enr2')
    
    response2 = test_client.get(enroll_link + '/1',follow_redirects=True)
    assert response2.status_code == 200

def test_Dropcourse(test_client,login_default_user):
    response = test_client.get('/course/drop/1', follow_redirects=True)
    assert response.status_code == 200
    assert b'Welcome Dipin' in response.data