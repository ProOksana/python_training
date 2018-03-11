from model.contact import Contacts



def test_contacts_list(app, db):
    ui_list = app.contact.get_contacts_list()
    def clean(contact):
        return (Contacts(id=id, firstname=contact.firstname, middlename=contact.middlename, lastname=contact.lastname, nickname=contact.nickname,
                         company=contact.company, title=contact.title, address=contact.address, homephone=contact.homephone, mobilephone=contact.mobilephone, workphone=contact.workphone,
                         email=contact.email, email2=contact.email2, email3=contact.email3))
    db_list = db.get_contacts_list()
    assert sorted(ui_list, key=Contacts.id_or_max) == sorted(db_list, key=Contacts.id_or_max)