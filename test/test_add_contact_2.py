# -*- coding: utf-8 -*-
from model.contact import Contacts



def test_add_contact_2(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contacts_list()
    app.contact.fill_the_form(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)








