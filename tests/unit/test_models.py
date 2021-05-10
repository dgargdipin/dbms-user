from cms.models import User


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """
    user = User('Dipin','dgargdipin@gmail.com','abc','1',1)
    assert user.email == 'dgargdipin@gmail.com'
    assert user.password_hash != 'abc'
