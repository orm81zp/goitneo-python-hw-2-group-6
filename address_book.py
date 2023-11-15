from collections import UserDict

PHONE_NUMBER_COUNT = 10

def is_valid_phone_number(phone_number):
    is_in_range = len(phone_number) == PHONE_NUMBER_COUNT
    is_all_numbers = all(True for number in phone_number if number.isdecimal())

    return True if is_in_range and is_all_numbers else False


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, phone_number):
        if is_valid_phone_number(phone_number):
            self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        self.phones = list(filter((lambda phone: phone.value != phone_number), self.phones))

    def edit_phone(self, old_phone_number, new_phone_number):
        if is_valid_phone_number(new_phone_number):
            self.phones = list(map((lambda phone: Phone(new_phone_number) if phone.value == old_phone_number else phone), self.phones))

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return "Phone number not found."


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        record = self.data.get(name)
        return record

    def delete(self, name):
        self.data.pop(name, None)
