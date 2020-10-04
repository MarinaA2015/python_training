# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first(Contact("SecondName", "SecondName", "SecondCompany", "SecondTelephone"))

def test_edit_first_contact_name(app):
    app.contact.edit_first(Contact("JustFirstName"))

def test_edit_first_contact_last_name(app):
    app.contact.edit_first(Contact(last_name="JustLastName", company="JustCompany"))