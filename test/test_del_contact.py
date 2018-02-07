
from model.contact import Contacts

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.open_add_new()
        app.contact.fill_the_form(Contacts(firstname="Oksana_new", middlename="Oksana_new", lastname="Prokopek_new", nickname="ProOksana_new", title="Test_title", company="Test_Company",
                        address="Wrocław_new, ul. Damrota 48/5", mobile="500300488", home="500300488", work="500300488",
                        email="prokopekoksana@gmail.com"))
        app.contact.submit_add_new()
    app.contact.delete_first_contact()