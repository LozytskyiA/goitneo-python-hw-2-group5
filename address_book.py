from collections import UserDict

from custom_exceptions import IncorrectPhoneFormat


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)

    def validate(self):
        if len(self.value) != 10 or not self.value.isdigit():
            raise ValueError("Phone number must be 10 digits long")


class Record:
    def __init__(self, name, phones=None):
        self.name = Name(name)
        self.phones = phones if phones else []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        phone.validate()
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                break

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number
                break

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(map(str, self.phones))}"


class AddressBook(UserDict):
    def add_record(self, record):
        if isinstance(record, Record):
            self.data[record.name.value] = record
        else:
            raise ValueError("Record instance required")

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print("Record not found")
