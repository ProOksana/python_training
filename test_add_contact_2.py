# -*- coding: utf-8 -*-
import pytest
from contact import Contacts
from application import Application_2


@pytest.fixture
def app(request):
    fixture = Application_2()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact_2(app):
    app.login(username="admin", password="secret")
    app.fill_the_form(Contacts(firstname="Oksana", middlename="Oksana", lastname="Prokopek", nickname="ProOksana", title="Test_title", company="Test_Company",
                        address="Wrocław, ul. Damrota 48/5", mobile="500300488", home="500300488", work="500300488",
                        email="prokopekoksana@gmail.com"))
    app.submit_add_new()
    app.logout()

def test_add_empty_contact_2(app):
    app.login(username="admin", password="secret")
    app.fill_the_form(Contacts(firstname="", middlename="", lastname="", nickname="",
                        title="", company="",
                        address="", mobile="", home="",
                        work="",
                        email=""))
    app.submit_add_new()
    app.logout()



