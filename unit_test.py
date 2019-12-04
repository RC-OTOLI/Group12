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
def test_new_user(new_user):
    assert new_user.username == 'raymond'
    assert new_user.email == 'raymond@example.com'
    assert new_user.check_password != 'RaymondpassFake'

def test_new_setting_password(new_user):
    new_user.set_password('newpassword')
    assert new_user.check_password != 'newpassword'
    assert new_user.check_password('newpassword')
    assert not new_user.check_password('RaymondpassFake')
# not sure on transaction part
@pytest.fixture(scope="module")
def test_transaction():
    mytransaction = Transaction(name="user_id", amount=? ,description=?,timestamp=?)
    return mytransaction
def test_user_authentification(new_user):
    assert new_user.is_authenticated == True

@pytest.fixture(scope="module")
def new_user_transaction(new_user):
    mytransaction = Transaction(author=new_user)
    return mytransaction
    