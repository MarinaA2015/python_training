# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation +" "*10
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(first_name="", last_name="", company="", home_phone="")] + [
    Contact(first_name=random_string("fname-",10), last_name=random_string("lname-",20),
            company=random_string("company-",20), home_phone=random_string("hphone-",7))
    for i in range(5)
    ]

@pytest.mark.parametrize("contact", testdata,ids=[repr(x) for x in testdata])
def test_add_new_contact(app,contact):
    old_contacts = app.contact.get_contacts_list()
    #contact = Contact("FirstName", "LastName", "Company", "Telephone")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

