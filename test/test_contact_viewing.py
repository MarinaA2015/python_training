from model.contact import Contact
from random import randrange
import re


def test_random_contact_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="for verification"))
    length = app.contact.count()
    index = randrange(length)
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.all_email == merge_emails_like_on_homepage(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_contact_page == merge_phones_like_on_homepage(contact_from_edit_page)


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_blanks(x),
                                filter(lambda x: x is not None,
                                       [contact.email,contact.email2,contact.email3]))))


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                            contact.second_phone]))))

def clear(s):
    return re.sub("[() -]", "", s)

def clear_blanks(s):
    return re.sub(" ", "", s)