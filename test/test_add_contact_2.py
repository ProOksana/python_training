# -*- coding: utf-8 -*-

from model.contact import Contacts


def test_add_contact_2(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contacts(firstname="Oksana", middlename="Oksana", lastname="Prokopek", nickname="ProOksana", title="Test_title", company="Test_Company",
                       address="Wrocław, ul. Damrota 48/5", mobilephone="500300488", homephone="500300488", workphone="500300488",
                       email="prokopekoksana@gmail.com")
    app.contact.fill_the_form(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)


#def test_add_empty_contact_2(app):
    #old_contacts = app.contact.get_contacts_list()
    #contact = Contacts(firstname="", middlename="", lastname="", nickname="",title="", company="", address="", mobile="", home="", work="", email="")
    #app.contact.fill_the_form(contact)
    #new_contacts = app.contact.get_contacts_list()
    #assert len(old_contacts) + 1 == len(new_contacts)
    #old_contacts.append(contact)
    #assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)






