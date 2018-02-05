# -*- coding: utf-8 -*-

from model.contact import Contacts


def test_add_contact_2(app):
    app.contact.fill_the_form(Contacts(firstname="Oksana", middlename="Oksana", lastname="Prokopek", nickname="ProOksana", title="Test_title", company="Test_Company",
                        address="Wrocław, ul. Damrota 48/5", mobile="500300488", home="500300488", work="500300488",
                        email="prokopekoksana@gmail.com"))


def test_add_empty_contact_2(app):
    app.contact.fill_the_form(Contacts(firstname="", middlename="", lastname="", nickname="",
                        title="", company="",
                        address="", mobile="", home="",
                        work="",
                        email=""))




