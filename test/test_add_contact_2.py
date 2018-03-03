# -*- coding: utf-8 -*-
from model.contact import Contacts
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contacts(firstname="", middlename="", lastname="", nickname="",title="",
                     company="", address="", mobilephone="", homephone="", workphone="", email="")] + [
    Contacts(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
          nickname=random_string("nickname", 10), title=random_string("title", 20), company=random_string("company", 20),
          address=random_string("address", 30), mobilephone=random_string("mobilephone", 10),
          homephone=random_string("homephone", 20), workphone=random_string("workphone", 10), email=random_string("email", 20))
    for i in range(5)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])


def test_add_contact_2(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.fill_the_form(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)








