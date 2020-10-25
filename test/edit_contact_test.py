# -*- coding: utf-8 -*-
from model.contact import Contact

from random import randrange

def test_edit_some_contact(app):
    if app.contact.count()==0:
        app.contact.create(Contact(first_name="for edition"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact("SecondName", "SecondName", "SecondCompany", "SecondTelephone")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_edit_first_contact_name(app):
#     if app.contact.count()==0:
#         app.contact.create(Contact(first_name="for edition"))
#     app.contact.edit_first(Contact("JustFirstName"))
#
# def test_edit_first_contact_last_name(app):
#     if app.contact.count()==0:
#         app.contact.create(Contact(first_name="for edition"))
#     app.contact.edit_first(Contact(last_name="JustLastName", company="JustCompany"))
