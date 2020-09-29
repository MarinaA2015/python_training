from model.group import Group
from fixture.application import  Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_group(app):
    app.session.login("admin", "secret")
    app.group.delete_first()
    app.session.logout()