from bot_utils import show_help, change_contact, add_contact, show_phone, parse_input, show_all, InputBotExseption


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
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))    
            elif command == "phone":
                print(show_phone(args, contacts))    
            elif command == "all":
                print(show_all(contacts))
            elif command == "help":
                show_help()
            else:
                print("Invalid command. Type \"help\" to see a list of commands.")
        except InputBotExseption:
            print("Please, enter a command to begin.")
        except Exception as err:
            print("Oops! Something went wrong.", err)


if __name__ == "__main__":
    main()
