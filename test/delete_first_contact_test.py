# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="for deletion"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) -1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
