# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("FirstName", "LastName", "Company", "Telephone"))
    app.session.logout()
