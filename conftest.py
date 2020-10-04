from fixture.application import  Application
import pytest

fixture = None

@pytest.fixture(scope="session")
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login("admin", "secret")
    else:
        if not fixture.isValid():
            fixture = Application()
            fixture.session.login("admin", "secret")
    return fixture


@pytest.fixture(scope="session", autouse = True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture