# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.delete_first()
    app.session.logout()