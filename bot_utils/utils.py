class ArgsBotExseption(Exception):
    pass

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

def show_help():
    """Shows help information"""
    print("Please, use only the following commands:\n")
    for command in COMMANDS:
        print("{:<20} - {:<30}".format(command, COMMANDS[command]))
    print()

def is_contact_exists(args, contacts):
    """Checks if a name exists in contacts"""
    if len(args) < 2:
        raise ArgsBotExseption("Not enough values, expected 2.")
    name = args[0]
    if name in contacts:
        return True
    return False

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

def add_contact(args, contacts):
    """Adds a new contact"""
    if len(args) < 2:
        raise ArgsBotExseption("Not enough values, expected 2.")

    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """Updates an existing contact"""
    if len(args) < 2:
        raise ArgsBotExseption("Not enough values, expected 2.")

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    
    return "Contact not found."

def show_phone(args, contacts):
    """Retuns a phone number found by a user name"""
    if len(args) < 1:
        raise ArgsBotExseption("Not enough values, expected 1.")

    name = args[0]
    if name in contacts:
        return contacts[name]
    
    return "Contact not found."