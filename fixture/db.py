import pymysql.cursors
from model.group import Group
from model.contact import Contacts

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contacts_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, homephone, mobilephone, workphone, email, email2, email3) = row
                list.append(Contacts(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname,
                                     company=company, title=title, address=address, homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                                     email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()

