# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.edit_first(Contact("SecondName", "SecondName", "SecondCompany", "SecondTelephone"))
    app.session.logout()