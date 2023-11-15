from bot_utils import show_help, is_contact_exists, change_contact, add_contact, show_phone, parse_input, is_yes_prompt, InputBotExseption, ArgsBotExseption


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    show_help()

    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit", "bye", "good bye"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                if is_contact_exists(args, contacts):
                    user_input = input("Contact already exists, update? (y or n): ")
                    if is_yes_prompt(user_input):
                        print(change_contact(args, contacts)) 
                else:
                    print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))    
            elif command == "phone":
                print(show_phone(args, contacts))    
            elif command == "all":
                if len(contacts):
                    for name, phone in contacts.items():
                        print(f"{name}: {phone}")
                else:
                    print("There are no contacts to display.")
            elif command == "help":
                show_help()
            else:
                print("Invalid command. Type \"help\" to see a list of commands.")
        except InputBotExseption:
            print("Please, enter a command to begin.")
        except ArgsBotExseption as error:
            print(error)
        except Exception:
            print("Oops! Something went wrong.")

if __name__ == "__main__":
    main()
