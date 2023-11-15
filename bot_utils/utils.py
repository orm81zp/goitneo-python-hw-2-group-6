class InputBotExseption(Exception):
    pass

COMMANDS = {
    "hello": "used to show a welcome message",
    "add": "used to add a new contact: \"add username phone\"",
    "change": "used to change a contact phone number: \"change username phone\"",
    "phone": "used to show a phone number: \"phone username\"",
    "all": "used to show all saved contacts with phone numbers",
    "help": "used to show commands",
    "close or exit": "used to terminate the program",
}

def input_error(error):
    """Decorator takes an error message and return the error"""
    def error_handler(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return error
            except IndexError:
                return error
        return inner
    return error_handler

def show_help():
    """Shows help information"""
    print("Please, use only the following commands:\n")
    for command in COMMANDS:
        print("{:<20} - {:<30}".format(command, COMMANDS[command]))
    print()

def parse_input(user_input):
    """Lowers the value entered by the user and removes extra spaces around the sides. Returns a command and the rest of arguments"""
    if not user_input:
        raise InputBotExseption
    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def is_yes_prompt(user_input):
    """Checks if the value entered by the user either yes or y"""
    if not user_input:
        raise InputBotExseption

    prompt = user_input.strip().lower()
    return prompt in ["yes", "y",]

@input_error("Give me name and phone please.")
def add_new_contact(args, contacts):
    """Adds a new contact"""
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error("Give me name and phone please.")
def change_contact(args, contacts):
    """Updates an existing contact"""
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."

@input_error("Give me name please.")
def show_phone(args, contacts):
    """Retuns a phone number found by a user name"""
    name = args[0]
    if name in contacts:
        return contacts[name]
    return "Contact not found."

def show_all(contacts):
    result = ""

    if len(contacts):
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.rstrip()
    else:
        return "There are no contacts to display."

@input_error("Give me name and phone please.")
def add_contact(args, contacts):
    """Checks if a contact exists and ask approval for updating one or add a new contact"""
    name, _ = args

    if name in contacts:
        user_input = input("Contact already exists, update? (y or n): ")
        if is_yes_prompt(user_input):
            return change_contact(args, contacts)
        else:
            return "Contact updating canceled."
    else:
        return add_new_contact(args, contacts)
