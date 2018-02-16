
from model.contact import Contacts

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.open_home_page()
        app.contact.fill_the_form(Contacts(lastname="Prokopek", firstname="Oksana", middlename="Oksana", nickname="ProOksana",
                     title="Test_title", company="Test_Company",
                     address="Wrocław, ul. Damrota 48/5", mobile="500300488", home="500300488", work="500300488",
                     email="prokopekoksana@gmail.com"))
        app.contact.submit_add_new()
    old_contacts = app.contact.get_contacts_list()
    contact = Contacts(lastname="Prokopek", firstname="Oksana", middlename="Oksana", nickname="ProOksana",
                     title="Test_title", company="Test_Company",
                     address="Wrocław, ul. Damrota 48/5", mobile="500300488", home="500300488", work="500300488",
                     email="prokopekoksana@gmail.com")
    contact.id = old_contacts[0].id
    app.contact.edit_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)