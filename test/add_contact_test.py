# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string
#from data.contacts import constant as testdata

#@pytest.mark.parametrize("contact", testdata,ids=[repr(x) for x in testdata])

def test_add_new_contact(app,data_contacts):
    contact = data_contacts
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

