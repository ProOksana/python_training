# -*- coding: utf-8 -*-

from model.contact import Contacts


def test_add_contact_2(app):
    old_contacts = app.contact.get_contacts_list()
    app.contact.fill_the_form(Contacts(firstname="Oksana", middlename="Oksana", lastname="Prokopek", nickname="ProOksana", title="Test_title", company="Test_Company",
                        address="Wrocław, ul. Damrota 48/5", mobile="500300488", home="500300488", work="500300488",
                        email="prokopekoksana@gmail.com"))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact_2(app):
    old_contacts = app.contact.get_contacts_list()
    app.contact.fill_the_form(Contacts(firstname="", middlename="", lastname="", nickname="",
                        title="", company="",
                        address="", mobile="", home="",
                        work="",
                        email=""))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)






