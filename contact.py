import re


class Contact:
    def __init__(self, contact_data):
        self.lastname, \
        self.firstname, \
        self.surname, \
        self.job, \
        self.position, \
        self.phone, \
        self.email = contact_data

        self.lastname, self.firstname, self.surname = self.get_normal_name()
        self.phone = self.get_normal_phone()

    def get_normal_name(self):
        full_name = f'{self.lastname} {self.firstname} {self.surname}'
        normal_name = re.findall(r'\w+', full_name)
        if len(normal_name) == 3:
            return normal_name[0], normal_name[1], normal_name[2]
        elif len(normal_name) == 2:
            return normal_name[0], normal_name[1], ''
        else:
            return normal_name[0], '', ''

    def get_normal_phone(self):
        normal_phone = re.sub(
            r'(8|\+7)[\s-]*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})',
            r'+7(\2)\3-\4-\5',
            self.phone
        )
        normal_phone = re.sub(
            r'\s*\(?(доб\.)\s(\d+)\)?',
            r' доб.\2',
            normal_phone
        )
        return normal_phone

    def update_contact(self, new_contact):
        self.lastname = self.lastname or new_contact.lastname
        self.firstname = self.firstname or new_contact.firstname
        self.surname = self.surname or new_contact.surname
        self.job = self.job or new_contact.job
        self.position = self.position or new_contact.position
        self.phone = self.phone or new_contact.phone
        self.email = self.email or new_contact.email

    def __repr__(self):
        return f'Contact(["{self.lastname}",' \
               f'"{self.firstname}", ' \
               f'"{self.surname}", ' \
               f'"{self.job}", ' \
               f'"{self.position}", ' \
               f'"{self.phone}", ' \
               f'"{self.email}"])'

    def __str__(self):
        return f'{self.lastname},' \
               f'{self.firstname},' \
               f'{self.surname},' \
               f'{self.job},' \
               f'{self.position},' \
               f'{self.phone},' \
               f'{self.email}'