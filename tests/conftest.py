import pytest
from cms import app, db
from datetime import datetime
from cms.models import User,Professor, Course, Quiz, Question, Request, Option


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
    user1 = User('Dipin','dgargdipin@gmail.com','abc','1',2)
    user2 = Professor("Professor 1","prof1@gmail.com","prof1",2)
    db.session.add(user1)
    db.session.add(user2)

    # Commit the changes for the users
    db.session.commit()

    course = Course(details="Course on Data structures", prof_id=user2.id, name="Data structures", course_code='203', 
        can_apply=True)
    db.session.add(course)
    db.session.commit()

    quiz = Quiz(course_id= course.id,name="Quiz1",start_time= datetime(2015, 6, 5, 8, 10, 10, 10), end_time=datetime(2015, 6, 5, 8, 10, 12, 10))
    db.session.add(quiz)
    db.session.commit()

    # Adding two Question in Quiz1
    question1 = Question(quiz_id=quiz.id, question="Odd one out", ans='4', marks=2, is_multicorrect=True , is_partial=True)
    # question2 = Question(quiz_id=quiz.id, question="Cities in Maharastra", ans='2,3,4', marks=4, is_multicorrect=True , is_partial=True)
    db.session.add(question1)
    # db.session.add(question2)
    db.session.commit()

    # Options for 1st question
    option1 = Option(question_id=question1.id, option='django', is_right=False)
    option2 = Option(question_id=question1.id, option='flask', is_right=False)
    option3 = Option(question_id=question1.id, option='ruby on rails', is_right=False)
    option4 = Option(question_id=question1.id, option='expressjs', is_right=True)
    db.session.add(option1)
    db.session.add(option2)
    db.session.add(option3)
    db.session.add(option4)
    db.session.commit()

    # # Options for 2nd question
    # option1 = Option(question_id=question2.id, option='Indore', is_right=False)
    # option2 = Option(question_id=question2.id, option='Nasik', is_right=True)
    # option3 = Option(question_id=question2.id, option='Mumbai', is_right=True)
    # option4 = Option(question_id=question2.id, option='Bombay', is_right=True)
    # db.session.add(option1)
    # db.session.add(option2)
    # db.session.add(option3)
    # db.session.add(option4)
    # db.session.commit()
    

    # Request for enrollment in course
    # req = Request(user_id=user1.id, course_id=course.id, title="Request to Access Course", details="Please allow me!!")
    # db.session.add(req)
    # db.session.commit()

    yield db # this is where the testing happens!

    db.drop_all()


@pytest.fixture(scope='function')
def login_default_user(test_client):
    test_client.post('/login',
                     data=dict(email='dgargdipin@gmail.com', password='abc'),
                     follow_redirects=True)

    yield  # this is where the testing happens!

    test_client.get('/logout', follow_redirects=True)

@pytest.fixture(scope='module')
def enrollinCourse(test_client):
    user = User.query.filter_by(email='dgargdipin@gmail.com').first()
    user.courses.append(1)

    yield  # this is where the testing happens!

    test_client.get('/logout', follow_redirects=True)

