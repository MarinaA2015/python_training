# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.edit_first(Contact("SecondName", "SecondName", "SecondCompany", "SecondTelephone"))
    app.session.logout()

def test_edit_first_contact_name(app):
    app.session.login("admin", "secret")
    app.contact.edit_first(Contact("JustFirstName"))
    app.session.logout()

def test_edit_first_contact_last_name(app):
    app.session.login("admin", "secret")
    app.contact.edit_first(Contact(last_name="JustLastName", company="JustCompany"))
    app.session.logout()