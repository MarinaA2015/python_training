from fixture.application import  Application
import pytest

fixture = None

@pytest.fixture(scope="session")
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    baseUrl = request.config.getoption("--baseUrl")
    if fixture is None:
        fixture = Application(browser=browser, baseUrl=baseUrl)
    else:
        if not fixture.isValid():
            fixture = Application(browser=browser, baseUrl=baseUrl)
    fixture.session.login(username="admin", password="secret")

    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")