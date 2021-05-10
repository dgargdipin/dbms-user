import pytest
from cms import app, db
from cms.models import User,Professor


@pytest.fixture(scope='module')
def new_user():
    user = User('Dipin','dgargdipin@gmail.com','abc','1',1)
    return user


@pytest.fixture(scope='module')
def test_client():
    flask_app = app

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    # Insert user data
    user1 = User('Dipin','dgargdipin@gmail.com','abc','1',1)
    user2 = Professor("Professor 1","prof1@gmail.com","prof1",2)
    db.session.add(user1)
    db.session.add(user2)

    # Commit the changes for the users
    db.session.commit()

    yield db # this is where the testing happens!

    db.drop_all()


@pytest.fixture(scope='function')
def login_default_user(test_client):
    test_client.post('/login',
                     data=dict(email='patkennedy79@gmail.com', password='FlaskIsAwesome'),
                     follow_redirects=True)

    yield  # this is where the testing happens!

    test_client.get('/logout', follow_redirects=True)
