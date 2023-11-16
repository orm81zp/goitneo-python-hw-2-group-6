from collections import UserDict

PHONE_NUMBER_COUNT = 10

def is_valid_phone_number(phone_number):
    """Validates a phone number
            
    Parameters:
        phone_number (str) 

    Returns:
        bool
    """
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
    
    def is_phone_number_exists(self, phone_number):
        """Checks if a phone number exists in phones list
        
        Parameters:
            phone_number (str) 

        Returns:
            bool
        """
        for phone in self.phones:
            if phone.value == phone_number:
                return True
        return False

    def add_phone(self, phone_number):
        if is_valid_phone_number(phone_number):
            self.phones.append(Phone(phone_number))
        else:
            print("Сontact failed validation.")


    def remove_phone(self, phone_number):
        if self.if_number_exists(phone_number):
            self.phones = list(filter((lambda phone: phone.value != phone_number), self.phones))
            print("Contact added.")
        else:
            print("Contact not found.")

    def edit_phone(self, old_phone_number, new_phone_number):
        if self.is_phone_number_exists(old_phone_number):
            if is_valid_phone_number(new_phone_number):
                self.phones = list(map((lambda phone: Phone(new_phone_number) if phone.value == old_phone_number else phone), self.phones))
                print("Contact updated.")
            else:
                print("Сontact failed validation.")
        else:
            print("Contact not found.")

    def find_phone(self, phone_number):
        if self.is_phone_number_exists(phone_number):
            for phone in self.phones:
                if phone.value == phone_number:
                    return phone
        else:
            print("Contact not found.")


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        record = self.data.get(name)
        return record

    def delete(self, name):
        self.data.pop(name, None)


def main():
    # Creating a new address book
    book = AddressBook()

    # Create record for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Adding John to the address book
    book.add_record(john_record)

    # Create and add a new record for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Output of all entries in the address book
    for _, record in book.data.items():
        print(record)

    # Find and edit John's phone
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Output: Contact name: John, phones: 1112223333; 5555555555

    # Search for a specific phone in a John record
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Output: 5555555555

    # Delete Jane's record
    book.delete("Jane")


if __name__ == "__main__":
    main()