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
    app.session.login("admin", "secret")
    app.group.create(Group("GroupName", "GroupHeader", "GroupFooter"))
    app.session.logout()

def test_empty_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()

