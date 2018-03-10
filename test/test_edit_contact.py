
from model.contact import Contacts
import random

def test_edit_contact(app, db):
    if len(db.get_contacts_list()) == 0:
        app.contact.open_home_page()
        app.contact.fill_the_form(Contacts(lastname="Prokopek", firstname="Oksana", middlename="Oksana", nickname="ProOksana",
                                           title="Test_title", company="Test_Company",
                                           address="Wrocław, ul. Damrota 48/5", mobilephone="500300488", homephone="500300488", workphone="500300488",
                                           email="prokopekoksana@gmail.com"))
        app.contact.submit_add_new()
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    contact = Contacts(lastname="Prokopek", firstname="Oksana", middlename="Oksana", nickname="ProOksana",
                       title="Test_title", company="Test_Company",
                       address="Wrocław, ul. Damrota 48/5", mobilephone="500300488", homephone="500300488", workphone="500300488",
                       email="prokopekoksana@gmail.com")
    contact.id = old_contacts.id
    app.contact.edit_contact_by_id(contact.id)
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    #old_contacts = contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)