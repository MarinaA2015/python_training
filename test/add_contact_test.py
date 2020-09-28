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
    app.session.login("admin", "secret")
    app.contact.create(Contact("FirstName", "LastName", "Company", "Telephone"))
    app.session.logout()
