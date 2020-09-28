# -*- coding: utf-8 -*-
import pytest

from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.open_application()
    app.login("admin", "secret")
    app.create_contact(Contact("FirstName", "LastName", "Company", "Telephone"))
    app.logout()
