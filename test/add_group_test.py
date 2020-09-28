# -*- coding: utf-8 -*-

from model.group import Group
from fixture.application import  Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    app.open_application()
    app.login("admin", "secret")
    app.create_group(Group("GroupName", "GroupHeader", "GroupFooter"))
    app.return_to_group()
    app.logout()

def test_empty_group(app):
    app.open_application()
    app.login("admin", "secret")
    app.create_group(Group("", "", ""))
    app.return_to_group()
    app.logout()

