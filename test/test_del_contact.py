
from model.contact import Contacts
import random

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contact.open_home_page()
        app.contact.fill_the_form(Contacts(firstname="Oksana", middlename="Oksana", lastname="Prokopek", nickname="ProOksana",
                                           title="Test_title", company="Test_Company",
                                           address="Wrocław, ul. Damrota 48/5", mobilephone="500300488", homephone="500300488", workphone="500300488",
                                           email="prokopekoksana@gmail.com"))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(id)
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contacts.id_or_max)

