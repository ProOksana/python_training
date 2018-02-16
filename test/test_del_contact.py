
from model.contact import Contacts

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.open_home_page()
        app.contact.fill_the_form(Contacts(firstname="Oksana", middlename="Oksana", lastname="Prokopek", nickname="ProOksana",
                     title="Test_title", company="Test_Company",
                     address="Wrocław, ul. Damrota 48/5", mobile="500300488", home="500300488", work="500300488",
                     email="prokopekoksana@gmail.com"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

