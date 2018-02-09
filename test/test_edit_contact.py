
from model.contact import Contacts

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.open_home_page()
        app.contact.fill_the_form(Contacts(firstname="Oksana", middlename="Oksana", lastname="Prokopek", nickname="ProOksana",
                     title="Test_title", company="Test_Company",
                     address="Wrocław, ul. Damrota 48/5", mobile="500300488", home="500300488", work="500300488",
                     email="prokopekoksana@gmail.com"))
        app.contact.submit_add_new()
    app.contact.edit_contact()