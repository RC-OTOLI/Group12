import pytest
import tempfile, os
from app import app
from app import makeApp
from app.models import User,Transaction

@pytest.fixture(scope="module")

def test_user():
    user = User(username='raymond', email='raymond@example.com')
    user.set_password('Raymondpass')
    return user
# test1: new user validation 
def test_new_user(new_user):
    assert new_user.username == 'raymond'
    assert new_user.email == 'raymond@example.com'
    assert new_user.check_password != 'RaymondpassFake'
# test2: new user password duplication
def test_new_setting_password(new_user):
    new_user.set_password('newpassword')
    assert new_user.check_password != 'newpassword'
    assert new_user.check_password('newpassword')
    assert not new_user.check_password('RaymondpassFake')

@pytest.fixture(scope="module")

#test3: user transaction display
def test_transaction():
    mytransaction = Transaction(name="user_id")
    return mytransaction
#test4: user autherntification viewing template
def test_user_authentification(new_user):
    assert new_user.is_authenticated == True

@pytest.fixture(scope="module")

#test5: user graph and function testing
def new_user_transaction(new_user):
    mytransaction = Transaction(author=new_user)
    return mytransaction

#test6: user homepage and start an application
def test_home_page(test_transaction):
    response = test_transaction.get('/')
    assert response.status_code == 200

#test7: Validate the new user registration 
def test_valid_register(test_transaction):
    response = test_transaction.post('/register',
                                data=dict(username='testing', email='testing@testing.com', password='testing', confirm='testing'),
                                follow_redirects=True)
    assert response.status_code == 200